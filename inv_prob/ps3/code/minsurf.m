% Solve the minimal surface problem
%  -div(1/sqrt(1+|grad u|^2)*grad) u = 0     on Omega
%                                  u = g     on boundary Gamma

clear all; clear fem;

% initialize geometry;
% a rectangle with unit side length
% fem.geom = rect2(1,1);

% a circle with radius 1
fem.geom = circ2(1);

figure; geomplot(fem, 'Edgelabels', 'on');
% discretize problem (create a triangle mesh, meshmap for quad meshes)

fem.mesh = meshinit(fem);    % initialize mesh
figure; meshplot(fem);
% order of ansatz and test functions (variation), we use linears here
fem.shape = 1;
% ansatz function name
fem.dim = 'u';

% specify weak form, the minus is since this is assumed to be on the
% right hand side of an equation
fem.equ.weak = '-(1/sqrt(1 + ux*ux + uy*uy) * (ux*ux_test + uy*uy_test))';

% Dirichlet boundary conditions
% this sets the boundary conditions individually for each edge
% fem.bnd.r = {{'u-2*x'} {'u-2+2*y'} {'u-1+x'} {'u-y'}};

% this sets the same boundary condition for all edges
fem.bnd.r = {'u-x^2'};

% setup mesh and unknowns...
fem.xmesh = meshextend(fem);

% solve using a nonlinear solver; this is a nonlinear problem. Comsol
% internally uses a damped Newton iteration.
fem.sol = femnlin(fem);

% plot solution surface
figure; postplot(fem, 'tridata', 'u', 'triz', 'u');