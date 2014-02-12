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

% add noise and plot noisy blurred image
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


% plot L-curve
alpha_list = [1e-4, 1e-3, 1e-2, 5e-2, 1e-1, 3e-1, 5e-1, 1, 1e1, 1e2, 1e3];
no = length(alpha_list);
misfit = zeros(no,1);
reg = zeros(no,1);

for k = 1:no
    alpha = alpha_list(k);
    I_alpha = pcg(@(in)apply(in,K1,K2,N1,N2,alpha),K_Ibn(:),1e-6,1500);
    misfit(k) = norm((K1 * (K2 * reshape(I_alpha,N2,N1))')' - Ibn);
    reg(k) = norm(I_alpha);
end

figure;
loglog(misfit, reg, 'Linewidth', 3);
hold on;
loglog(misfit(5), reg(5), 'ro', 'Linewidth', 3);
%axis([9e-1,10,1e-1,500]);
%xlabel('||K*p - d||'); ylabel('||p||');
print('L-curve2d.pdf')
