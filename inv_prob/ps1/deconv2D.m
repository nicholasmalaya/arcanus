%
% need to import the image 'longhorn.png'
%
%import(longhorn)
longhorn = imread("longhorn.png");

% The imported image called longhorn
% is a matrix of size 100x133.
% The image has values between 0 and 255 corresponding to
% different gray values
x=linspace(0,133,133);
y=linspace(0,100,100);
[xx,yy] = meshgrid(x,y);
I = double(255-longhorn);
% draw the imported image as surface
colormap gray;
surf(xx,yy,I);

N1 = 133;
N2 = 100;
N = N1 * N2;

% Use different Gaussian blurring in x and y-direction
gamma1 = 5;
C1 = 1 / (sqrt(2*pi)*gamma1);
gamma2 = 12;
C2 = 1 / (sqrt(2*pi)*gamma2);

% blurring operators for x and y directions
K1 = zeros(N1,N1);
K2 = zeros(N2,N2);
for l = 1:N1
    for k = 1:N1
    	K1(l,k) = C1 * exp(-(l-k)^2 / (2 * gamma1^2));
    end
end
for l = 1:N2
    for k = 1:N2
    	K2(l,k) = C2 * exp(-(l-k)^2 / (2 * gamma2^2));
    end
end

% blur the image: first, K2 is applied to each column of I,
% then K1 is applied to each row of the resulting image
Ib = (K1 * (K2 * I)')';

% plot blurred image
figure;
surf(xx,yy,Ib);
title('blurred image');

% add nose and plot noisy blurred image
Ibn = Ib + 16 * randn(N2,N1);
figure;
surf(xx,yy,Ibn);
title('blurred noisy image');

% compute Tikhonov reconstruction with regularization
% parameter alpha, i.e. compute m = (K'*K + alpha*I)\(K'*d)

% first construct the right hand side K'*d
K_Ibn = (K1 * (K2 * Ibn)')';

% then set the regularization parameter 
alpha = 1.5e-3;

% now solve the regularized inverse problem to reconstruct the 
% the image using preconditioned conjugate gradients (pcg) to solve the
% system in a matrix-free way using function "apply"

I_alpha = pcg(@(in)apply(in,K1,K2,N1,N2,alpha),K_Ibn(:),1e-6,1500);
figure;
surf(xx,yy,reshape(I_alpha,N2,N1));
title('Tikhonov reconstruction');
view(0,-90);   % top view


