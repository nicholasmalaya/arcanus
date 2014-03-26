% Simple COMSOL model problem for solving the Laplace equation
%       - Laplace u = sin(2*pi*x)   on Omega
%                 u = 0             on Dirichlet boundary Gamma_d
%             du/dn = -1            on Neumann boundary Gamma_n

clear all; clear fem;

% initialize geometry; other options are circ2(r) for a circle with radius r
% you can add and substract geometries to create geometries with holes
fem.geom = rect2(1,1);
figure; geomplot(fem, 'Edgelabels', 'on');

% discretize problem (create a triangle mesh), for quad meshes use
% fem.mesh = meshmap(fem, 'Edgelem', {1,20,2,20});
fem.mesh = meshinit(fem, 'hauto', 4);
figure; meshplot(fem);
% order of ansatz and test functions; 1 uses linear elements, 2
% quadratic elements etc.
fem.shape = 1;
% name of function name; the corresponding test function is called u_test
fem.dim = 'u';

% define an expression called f, that can be used in the definition of
% a weak form
fem.equ.expr.f = 'sin(2*pi*x)';

% specify weak form---note that the whole week form is assumed to be
% moved to the right hand side, which explains the negative sign
% Note that the derivative of u with respect to x is called ux, the
% derivative of the test function/variation with respect to x is
% called ux_test etc.
fem.equ.weak = '-(ux * ux_test + uy * uy_test) + f * u_test';

% weak form of boundary tractions, bdry numbers according to plot
% we assume no boundary traction on the first and 4th side, and a
% traction of sigma0=-1 on the 2nd and 3rd side of the domain
fem.bnd.weak = {{} {'-1 * u_test'} {'-1 * u_test'} {}};

% Dirichlet boundary conditions on Gamma_d: On the first and 4th side
% of the domain, we use the Dirichlet condition u=0; the structure
% fem.bnd.r imposes this constraint
fem.bnd.r = {{'u-0'} {} {} {'u-0'}};

% setup mesh and unknowns...this does all the messy discretization
% work for you. This function needs to be called before every solve if
% you change anything in the problem such as boundary conditions or
% the weak form.
fem.xmesh = meshextend(fem);

% solve using a linear solver
fem.sol = femlin(fem);

% plot solution surface
% a 3D surface plot -- remove triz part to get a top view
figure;
postplot(fem, 'tridata', 'u', 'triz', 'u');

