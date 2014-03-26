% Image denoising problem using Tikhonov and total variation regularization
clear all; close all; clear fem;
% number of discretization points/pixels
N = 100;
% setup noisy test image
global xx yy I;
x = linspace(0,1,N);
[xx,yy] = meshgrid(x,x);
randn('seed', 0);
I = 0.25 * randn(N,N);
% iamge setup: ramp, circle and triangle
I = I + 2*(xx - 0.2) .* (yy > 0.1 & yy < 0.4) .* (xx > 0.2 & xx < 0.7);
I = I + (((xx-0.75).^2 + (yy-0.75).^2) < 0.03);
I = I + (yy > 0.5) .* (((xx - (yy - 0.5) - 0.1) > 0) & (xx < 0.45));
% initialize geometry and mesh
fem.geom = rect2(1,1);
fem.mesh = meshmap(fem, 'Edgelem', {1,N,2,N});
% order of ansatz and test functions
fem.shape = 1;
% name of unknown
fem.dim = 'u';
% Input the Boundaries
fem.bnd.weak = {{'0 * u_test'} {'0 * u_test'} {'0 * u_test'} {'0 * u_test'}};
% Loop to get the L curve
epsInp = [10 1 0.1 1e-2 1e-3 1e-4];
alphaInp = 0.03;
Neps = length(epsInp);
for i = 1:Neps
    fem.equ.expr.alpha = num2str(alphaInp);
    fem.equ.expr.epsilon = num2str(epsInp(i)); 
    fem.equ.expr.u0 = 'ustar_fun(x,y)';
    fem.equ.weak = '2 * (u - u0) * u_test + alpha * 0.5 * (ux * ux_test + uy * uy_test) * (ux * ux + uy * uy + epsilon)^(-0.5)';
    fem.xmesh = meshextend(fem);
    fem.sol = femnlin(fem,'Maxiter',150);
end
%figure; postplot(fem, 'tridata', 'u'); 
