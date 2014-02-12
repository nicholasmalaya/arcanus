% Number of discretization points
% N = 200;
close all
N = 200;
C = 0.2;

K = zeros(N,N);
h = 1/N;
x = linspace(0,1,N)';

% discrete convolution matrix
for l = 1:N
    for k = 1:N
      %K(l,k)  = h * power(C,-2) * max(0,C-abs((l-k)*h));
      K(l,k)  = h * power(C,-2) * max(0,C-abs((l-k)*h));
    end
end

% exact parameters
p = 0.75 * (x > .1).*(x < .25) + 0.25 * (x > .3).*(x < .32) + power(sin(2*pi*x),4).*(x > 0.5) + 0.0 * cos(30*pi*x);

% convolved parameters
d = K * p;

% noisy data, noise has sigma (standard deviation) = 0.1
%dn = d + 0.1 * randn(N,1);
%n = sqrt(0.1)*randn(N,1);
n = 0.1*randn(N,1);
dn = d + n;
plot(x,d,x,dn,'Linewidth', 2);
legend('data', 'noisy data');
print('data.pdf')

% Tikhonov regularization parameter
% alpha = 0.05;
alpha = 0.1;

% solve Tikhonov system
p_alpha = (K'*K + alpha * eye(N))\(K'*dn);
% comment out next 3 if you dont want figure
figure;
plot(x,p,x,p_alpha,'Linewidth', 2), axis([0,1,-1.5,1.5]);
legend('exact data', 'Tikhonov reconstruction');
title(['Alpha= ',num2str(alpha)])
print(['reconstruct',num2str(alpha),'.pdf'])

% solve TSVD
%p_tsvd = (K'*K + alpha * eye(N))\(K'*dn);
% comment out next 3 if you dont want figure
%figure;
%plot(x,p,x,p_tsvd,'Linewidth', 2), axis([0,1,-1.5,1.5]);
%legend('exact data', 'TSVD reconstruction');

% plot L-curve
alpha_list = [1e-4, 1e-3, 1e-2, 5e-2, 1e-1, 3e-1, 5e-1, 1, 1e1, 1e2, 1e3];
no = length(alpha_list);
misfit = zeros(no,1);
reg = zeros(no,1);

for k = 1:no
    alpha = alpha_list(k);
    p_alpha = (K'*K + alpha * eye(N))\(K'*dn);
    misfit(k) = norm(K*p_alpha - dn);
    reg(k) = norm(p_alpha);
end

figure;
loglog(misfit, reg, 'Linewidth', 3);
hold on;
loglog(misfit(3), reg(3), 'ro', 'Linewidth', 3);
%axis([9e-1,10,1e-1,500]);
xlabel('||K*p - d||'); ylabel('||p||');
print('L-curve.pdf')

%
% discover alpha using morozov's discrepancy criterion
%
delta = norm(n);

for k = 1:no
    alpha = alpha_list(k);
    p_alpha = (K'*K + alpha * eye(N))\(K'*dn);
    misfit(k) = norm(K*p_alpha - dn);
    reg(k) = norm(p_alpha);
end

figure;
loglog(alpha_list,misfit, 'Linewidth', 3);
hold on;
loglog(alpha_list(5), delta, 'ro', 'Linewidth', 3);
%axis([9e-1,10,1e-1,500]);
xlabel('\alpha'); ylabel('||K*p - d||');
%mu = 0;
%hold on;
%line = refline([alpha_list(5) mu]);
%set(line,'Color','r')
title('Morozov Discrepancy')
print('morozov.pdf')

%
% discover alpha against the 'true' error
%
delta = norm(n);

for k = 1:no
    alpha = alpha_list(k);
    p_alpha = (K'*K + alpha * eye(N))\(K'*dn);
    misfit(k) = norm(K*p_alpha - d);
end

figure;
loglog(alpha_list,misfit, 'Linewidth', 3);
hold on;
loglog(alpha_list(3), misfit(3), 'ro', 'Linewidth', 3);
xlabel('\alpha'); ylabel('||m_{true} - m_{\alpha}||');
title('Error in Reconstruction')
print('true1d.pdf')
