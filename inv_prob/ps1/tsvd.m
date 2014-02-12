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
      K(l,k)  = h * (power(C,-2)) * max(0,C-abs((l-k)*h));
    end
end

% exact parameters
p = 0.75 * (x > .1).*(x < .25) + 0.25 * (x > .3).*(x < .32) + power(sin(2*pi*x),4).*(x > 0.5) + 0.0 * cos(30*pi*x);

% convolved parameters
d = K * p;

% noisy data, noise has sigma (standard deviation) = 0.1
%dn = d + 0.1 * randn(N,1);
n = sqrt(0.1)*randn(N,1);
%n = 0.1*randn(N,1);
dn = d + n;
plot(x,d,x,dn,'Linewidth', 2);
legend('data', 'noisy data');
print('data.pdf')

% TSVD regularization parameter
% alpha = 0.05;
%alpha = 0.0001;
alpha = 0.0001;

% solve TSVD
[U,S,V] = svd(K);
for j=1:N,
  if S(j , j)*S(j , j) < alpha
    S(j , j) = 0;
  end    
end

% s is diag matrix of eigenvalues, so lets filter them
p_tsvd = U*S*V' * dn;
% comment out next 3 if you dont want figure
figure;
plot(x,p,x,p_tsvd,'Linewidth', 2), axis([0,1,-1.5,1.5]);
legend('exact data', 'TSVD reconstruction');
title(['T_{SVD}, \alpha=',num2str(alpha)])
print(['tsvd',num2str(alpha),'.pdf'])