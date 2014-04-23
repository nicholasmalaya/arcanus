%% Inexact Gauss-Newton-Conjugate-Gradient solution of inverse
%% model problem:
%% Inversion for the parameter field in an elliptic equation
%%
%%    min  1/2 * ||u - ud||^2 + gamma/2 * ||grad a ||^2
%%     a
%%         where u is the solution of
%%
%%              - div (a * grad u) = f     on Omega
%%                               u = 0     on bdry(Omega)
%%
%% for given force f, gamma >= 0, data ud.
%% The data ud is synthesized using a "true" parameter field atrue
%% Authors: Georg Stadler, georgst@ices.utexas.edu
%%          Noemi Petra, noemi@ices.utexas.edu
%% Last update: April 19, 2012

clear all; close all;

% setup geometry and mesh
fem.geom = rect2(0,1,0,1);
fem.mesh = meshmap(fem, 'Edgelem', {1,20,2,20});

% finite element functions (ordered alphabetically) and polynomial order
fem.dim = {'a' 'delta_a' 'delta_p' 'delta_u' 'g' 'p' 'u' 'ud'};
fem.shape = [1 1 1 1 1 1 1 1];

% target coefficient atrue, noise ratio, rhs f, regularization weight gamma
fem.equ.expr.atrue = '2 + 6*(sqrt((x-0.5)^2 + (y-0.5)^2) > 0.2)';
datanoise = 0.01;
fem.equ.expr.f = '1';
fem.equ.expr.gamma = '1e-10';
% maximal number of iterations, norm of gradient at convergence
maxiter = 100;
tol     = 1e-12;
% constants for the line search
c        = 1e-4;
rho      = 0.5;

% other constants: overall number of CG iterations
nrCGiter = 0;

% Dirichlet boundary conditions for state and adjoint: if one
% expression is given it applies to all boundary pieces
fem.bnd.r =  {{'delta_u - 0' 'delta_p - 0' 'u - 0' 'ud - 0'}};

% weak forms to make up data ud, state, adjoint and control equation
fem.equ.expr.goal    = '-(atrue * (udx * udx_test + udy * udy_test) - f * ud_test)';
fem.equ.expr.state   = '-(a * (ux * ux_test + uy * uy_test) - f * u_test )';

fem.equ.expr.incstate   = ['-(a * (delta_ux * delta_px_test + delta_uy *' ...
	'delta_py_test) + delta_a * (ux * delta_px_test + uy * delta_py_test))'];
fem.equ.expr.incadjoint = ['-(a * (delta_px * delta_ux_test + delta_py *' ...
	'delta_uy_test) + delta_u * delta_u_test )'];
fem.equ.expr.inccontrol = ['-(gamma * (delta_ax * delta_ax_test + delta_ay' ...
	'* delta_ay_test) + (delta_px * ux + delta_py * uy) * delta_a_test)'];

% synthesize data ud
fem.equ.weak = 'goal';
fem.xmesh = meshextend(fem);
fem.sol = femlin(fem, 'Solcomp', 'ud');

% get indices for dofs corresponding to FE functions
nodes = xmeshinfo(fem ,'out', 'nodes');
dofs = nodes.dofs';
AI  = dofs(dofs(:,1)>0,1);
dAI = dofs(dofs(:,2)>0,2);
dPI = dofs(dofs(:,3)>0,3);
dUI = dofs(dofs(:,4)>0,4);
GI  = dofs(dofs(:,5)>0,5);
PI  = dofs(dofs(:,6)>0,6);
UI  = dofs(dofs(:,7)>0,7);
UDI = dofs(dofs(:,8)>0,8);

% copy FEM coefficients from Comsol structure to vector of unknowns
X = fem.sol.u;

% extract mass matrix for the gradient
fem.equ.weak = '- g * g_test';
fem.xmesh = meshextend(fem);
K = assemble(fem, 'out', 'K');
M = K(GI,GI);

% add noise to synthesized data to lessen the inverse crime
randn('seed', 0);
X(UDI) = X(UDI) + datanoise * max(abs(X(UDI))) * randn(length(UDI),1);
% initialize coefficients for function a
X(AI)  = 8.0;

% weak form for state solve and GN iteration
fem.equ.weak = 'state + incstate + incadjoint + inccontrol';

fprintf(' %s \n', ['it CGit         cost         misfit            reg '...
    '    ||delta_a||        ||grad||    ||a - atrue||      alpha       cgtol']);


% inexact Gauss-Newton iterations
for iter = 1:maxiter
    % solve the state problem for u
    fem.xmesh = meshextend(fem);
    fem.sol = femlin(fem, 'Solcomp', {'u'}, 'U', X);
    X(UI) = fem.sol.u(UI);
    if (iter == 1)
	[cost_old, misfit, reg] = elliptic_cost(fem, X);
    end
    % assemble the KKT system
    fem.xmesh = meshextend(fem);
    [K, N] = assemble(fem, 'U', X, 'out', {'K', 'N'});

    % extract blocks from the KKT system
    W = K(dUI,dUI);
    A = K(dPI,dUI);
    C = K(dPI,dAI);
    R = K(dAI,dAI);

    % enforce homogenous Dirichlet BCs in state operator
    ind = find(sum(N(:, dUI),1)~=0);
    A(:,ind) = 0;
    A(ind,:) = 0;
    for (k = 1:length(ind))
	i = ind(k);
	A(i,i) = 1;
    end
    chi = ones(size(A,1),1);
    chi(ind) = 0;

    % solve the adjoint problem for p
    X(PI) = A' \ (chi.*(W * (X(UDI) - X(UI))));

    % evaluate the gradient (multiplied by the mass matrix)
    MG =  C' * X(PI) + R * X(AI);

    % extract the coefficients of the gradient
    X(GI) = M \ MG;

    % compute the norm of the gradient
    gradnorm = sqrt (postint (fem, 'g^2', 'U', X));
    if iter == 1
	gradnorm_ini = gradnorm;
    end

    % compute the tolerance for CG based on the norm of the gradients
    tolcg = min(0.5, sqrt(gradnorm/gradnorm_ini));

    % the preconditioner for CG: R + 1e-10 * I
    P = R + 1e-10*eye(length(AI));

    % call pcg to compute the GN direction D
    [D, flag, relres, CGiter, resvec] = pcg (@(V)elliptic_apply(V, chi, W, ...
	A, C, R, X), -MG, tolcg, 300, P);
    % count the total number of CG iterations
    nrCGiter = nrCGiter + CGiter;

    % do a line search on delta_a
    Xtry = X;
    alpha = 1;
    descent = 0;
    no_backtrack = 0;
    while (~descent && no_backtrack < 20)
	% perform GN step with step size alpha
	Xtry(AI)  = X(AI) + alpha * D;
	Xtry(dAI) = D;

	% solve the state equation
	fem.xmesh = meshextend(fem);
	fem.sol = femlin(fem, 'Solcomp', 'u', 'U', Xtry);
	Xtry(UI)  = fem.sol.u(UI);

	[cost, misfit, reg] = elliptic_cost(fem, Xtry);
	if (cost < cost_old + c * alpha * MG' * D)
	    cost_old = cost;
	    descent = 1;
	else
	    no_backtrack = no_backtrack + 1;
	    alpha = rho * alpha;
	end
    end
    if (descent)
	X = Xtry;
    else
	error('Linesearch failed; no descent after %d backtracking steps', no_backtrack);
    end

    % write updated vector into FEM structure for statistics output
    fem.sol = femsol(X);
    a_update = sqrt (postint (fem, 'delta_a^2'));
    dist = sqrt (postint(fem, '(atrue - a)^2'));
    fprintf('%2d %3d %14.6e %14.6e %14.6e %15.6e %15.6e %15.6e %11.2e %11.2e\n', ...
	iter, CGiter, cost, misfit, reg, a_update, gradnorm, dist, alpha, tolcg);
    subplot(2,2,1);  postsurf(fem,'a'); title('a');  axis equal tight;
    subplot(2,2,2);  postsurf(fem,'u'); title('u');  axis equal tight;
    subplot(2,2,3);  postsurf(fem,'p'); title('p');  axis equal tight;
    subplot(2,2,4);  postsurf(fem,'ud'); title('u_d');  axis equal tight;
    pause (0.01);
    if ((a_update < tol && iter > 1) || gradnorm < tol)
	fprintf (' ******* GN converged after %d iterations. ********\n', iter);
	fprintf (' ******* Total number of CG iterations:  %d ********\n', nrCGiter);
	fprintf (' ******* Total number of fwd-adj solves:  %d ********\n', iter + nrCGiter);
	break;
    end
end