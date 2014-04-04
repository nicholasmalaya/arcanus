%% Steepest descent solution of inverse model problem
%% for parameter field inversion in an elliptic equation
%%
%%    min  1/2 * ||u - z||^2 + gamma/2 * ||grad a||^2,
%%     a
%%         where u is the solution of
%%
%%              - div (a * grad u) = f     on Omega
%%                               u = 0     on bdry(Omega)
%%
%% for given force f, gamma >= 0 and data z.
%% The data z is constructed using a "true" parameter field atrue
%% Authors: Georg Stadler, georgst@ices.utexas.edu
%%          Noemi Petra, noemi@ices.utexas.edu
%% Last update: April 2, 2012

clear all; close all;

% Setup geometry and mesh
fem.geom = rect2(0,1,0,1);
fem.mesh = meshmap(fem, 'Edgelem', {1,40,2,40});
% unstructure triangular mesh: use meshinit command

% finite element functions (ordered alphabetically)
fem.dim = {'a' 'grad' 'p' 'u' 'ud'};
% specify polynomial order of FEM function; these are all linear elements
fem.shape = [1 1 1 1 1];

% target coefficient, right hand side f
fem.equ.expr.atrue = '4 + 4*(sqrt((x-0.5)^2 + (y-0.5)^2) > 0.2)';
fem.equ.expr.f = '1';
% regularization parameter gamma, noise level
fem.equ.expr.gamma = '7.5e-9';
datanoise = 0.01;
% maximal number of steepest descent iterations, norm of gradient at convergence
maxiter = 300;
tol = 1e-8;
% constant c and initial step size alpha for line search (a priori, no
% good step length is known for steepest descent, so we start large)
c = 1e-4;
alpha = 1e5;
fem.equ.expr.tau = '1e-2';
% Impose Dirichlet boundary conditions; first, we number the sides;
% this numbering has to change when the geometry has more or less sides
fem.bnd.ind = [1 2 3 4];
% on each side, these Dirichlet boundary conditions are used
fem.bnd.r =  {{'u-0' 'p-0' 'ud-0'} {'u-0' 'p-0' 'ud-0'}...
    {'u-0' 'p-0' 'ud-0'} {'u-0' 'p-0' 'ud-0'}};

% weak forms to make up data ud, state, adjoint and control equation
fem.equ.expr.goal = '-(atrue * (udx * udx_test + udy * udy_test) - f * ud_test)';
fem.equ.expr.state = '-(a * (ux * ux_test + uy * uy_test) - f * u_test)';
fem.equ.expr.adjoint = '-(a * (px * px_test + py * py_test) - (ud - u) * p_test)';
%fem.equ.expr.control = ['(grad * grad_test - gamma * (ax * gradx_test + ay * grady_test)'...
%                   '-(px * ux + py * uy) * grad_test)'];
fem.equ.expr.control = ['(grad * grad_test - gamma * (ax * gradx_test + ay * grady_test) * (ax*ax+ay*ay+tau)^(-0.5)'...
                    '-(px * ux + py * uy) * grad_test)'];

% solve to construct target data ud
fem.equ.weak = 'goal';
fem.xmesh = meshextend(fem);
% solve only for ud
fem.sol = femlin(fem, 'Solcomp', {'ud'});

% get indices for dofs corresponding to functions a, grad, p, u, ud
nodes = xmeshinfo(fem ,'out', 'nodes');
dofs = nodes.dofs';
AI = dofs(dofs(:,1)>0,1);
GI = dofs(dofs(:,2)>0,2);
PI = dofs(dofs(:,3)>0,3);
UI = dofs(dofs(:,4)>0,4);
UDI = dofs(dofs(:,5)>0,5);

% copy FEM coefficients from Comsol structure to vector of unknowns
X = fem.sol.u;

% add noise to data
randn('seed', 0);
X(UDI) = X(UDI) + datanoise * max(abs(X(UDI))) * randn(length(UDI),1);

% initialize coefficients for function a
X(AI) = 8.0;

% define weak forms and initialize mesh data structure
fem.equ.weak = 'state + adjoint + control';
fem.xmesh = meshextend(fem);

% solve and compute initial cost; this only solves for u, and uses for
% the other variables whatever is stored in X (here, a is needed to
% compute u)
fem.sol = femlin(fem, 'Solcomp', {'u'}, 'U', X);
X(UI) = fem.sol.u(UI);
cost_old = elliptic_cost (fem, X);

fprintf(' %s \n', ['it          cost         misfit            reg      '...
    '  ||grad||   ||a - atrue||       alpha']);

% start gradient iteration
for iter = 1:maxiter
    % Solve state equation
    fem.sol = femlin(fem, 'Solcomp', {'u'}, 'U', X);
    X(UI) = fem.sol.u(UI);
    % Solve adjoint, using solution of state equation found above
    fem.sol = femlin(fem, 'Solcomp', {'p'}, 'U', X);
    X(PI) = fem.sol.u(PI);
    % Compute gradient
    fem.sol = femlin(fem, 'Solcomp', {'grad'}, 'U', X);
    X(GI) = fem.sol.u(GI);
    grad2 = postint (fem, 'grad * grad');
    % linesearch
    Xtry = X;
    % first try slightly bigger step size than successful previous
    % step; this is a heuristic that assumes that the step lenght
    % should be similar between steps; the factor 1.2 is to avoid
    % too small steps and thus slow convergence
    alpha = alpha * 1.2;
    descent = 0;
    no_backtrack = 0;
    while (~descent && no_backtrack < 10)
        Xtry(AI) = X(AI) - alpha * X(GI);
	% Solve state equation for new a
	fem.sol = femlin(fem, 'Solcomp', {'u'}, 'U', Xtry);
        Xtry(UI) = fem.sol.u(UI);
	% Compute cost and check for sufficient descent
	[cost, misfit, reg] = elliptic_cost (fem, Xtry);
	if (cost < cost_old - alpha * c * grad2)
            cost_old = cost;
            descent = 1;
        else
	    no_backtrack = no_backtrack + 1;
            alpha = 0.5 * alpha;
        end
    end
    X = Xtry;

    % plotting and statistics
    fem.sol = femsol(X);
    a_dist = sqrt (postint(fem, '(atrue - a)^2'));
    fprintf('%2d %14.6e %14.6e %14.6e %15.6e %15.6e %11.2e\n', ...
	iter, cost, misfit, reg, sqrt(grad2), a_dist, alpha);
    subplot(2,2,1);  postsurf(fem,'a'); title('a');  axis equal tight;
    subplot(2,2,2);  postsurf(fem,'u'); title('u');  axis equal tight;
    subplot(2,2,3);  postsurf(fem,'p'); title('p');  axis equal tight;
    subplot(2,2,4);  postsurf(fem,'ud'); title('ud');  axis equal tight;
    if (sqrt(grad2) < tol && iter > 1)
        fprintf (' *** Gradient method converged after %d iterations. ***\n\n', iter);
        break;
    end
end
