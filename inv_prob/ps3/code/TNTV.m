% Image denoising problem using Tikhonov and total variation regularization

clear all; clear fem;
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

% this function sets up the finite element mesh and structures and
% needs to be called before every solve
fem.xmesh = meshextend(fem);
% plot noisy data
figure;
postplot(fem, 'tridata', 'ustar_fun(x,y)');
