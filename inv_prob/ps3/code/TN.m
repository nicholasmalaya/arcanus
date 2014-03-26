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

fem.xmesh = meshextend(fem);
% plot noisy data
figure;
postplot(fem, 'tridata', 'ustar_fun(x,y)');

% plot the mesh
%figure; meshplot(fem);

% Input the Boundaries
fem.bnd.weak = {{'0 * u_test'} {'0 * u_test'} {'0 * u_test'} {'0 * u_test'}};
%fem.bnd.r = {{'u-10'} {'u-10'} {'u-10'} {'u-10'}};

% Loop to get the optimal alpha
alphaInp = linspace(1e-2, 5e-1, 10);
alphaInp = [alphaInp, 1, 5];
alphaInp = 0.005
N_alpha = length(alphaInp);
regularization = zeros(N_alpha,1);
misfit = zeros(N_alpha,1);
for i = 1:N_alpha
    fem.equ.expr.alpha = num2str(alphaInp(i));
    fem.equ.expr.u0 = 'ustar_fun(x,y)';
    fem.equ.weak = '2 * (u - u0) * u_test + 0.5 * alpha * (ux * ux_test + uy * uy_test)';
    % this function sets up the finite element mesh and structures and
    % needs to be called before every solve
    fem.xmesh = meshextend(fem);
    fem.sol = femlin(fem);
    %K=femlin(fem,'out','Kc');
    %d=femlin(fem,'out','lc');
    %u=femlin(fem,'out','u');
    %misfit(i) = norm(K*u-d);
    %regularization(i) = norm(u);
end
%figure;
%loglog(misfit,regularization);
%hold on;
%loglog(misfit(6),regularization(6), 'redX','Linewidth',2);
%legend('L Curve', 'Optimal Alpha');
%ylabel('Regularization ||u||');
%xlabel('Misfit || K * u - d ||');
%title('L Curve');

figure; postplot(fem, 'tridata', 'u'); 
