% Illustration of Newton method
% for Rosenbrock-like function
close all;
gamma = 3;
[xx,yy]=meshgrid(-.5:.01:1.5);
zz = gamma*(xx.^2-yy).^2 + (xx-1).^2;
figure(1);
contour(xx,yy,zz,30,'k','linewidth', 1);
axis equal tight;
pause;

figure(2);
surf(xx(1:5:end,1:5:end),yy(1:5:end,1:5:end),zz(1:5:end,1:5:end));
axis tight;

figure(1);
hold on;
plot(1,1,'rx','Linewidth',4);
title('minimizer');

X = -0.1;
Y = -0.2;

for k=1:5
    figure(1);
    contour(xx,yy,zz,30,'k','linewidth', 1);
    hold on;
    axis equal tight;
    if k == 1
	pause;
    end
    plot(1,1,'rx','Linewidth',4);
    title('Solution point');
    plot(X,Y,'bx','Linewidth',5);
    title('Iterate x_k');
    g = [4*gamma*X*(X^2-Y)+2*X-2; -2*gamma*(X^2-Y)];
    H = [4*gamma*(X^2-Y)+8*gamma*X^2+2, -4*gamma*X;
	-4*gamma*X,                       2*gamma];

    xxd = xx - X;
    yyd = yy - Y;
    zzlin = g(1)*xxd + g(2)*yyd + ...
	0.5*(xxd.*xxd*H(1,1)+2*H(1,2)*xxd.*yyd+H(2,2)*yyd.*yyd);
    pause;
    step = 1;
    plot([X,X-step*g(1)],[Y,Y-step*g(2)],'g','Linewidth',3);
    title('steepest descent direction -g');
    pause;
    contour(xx,yy,zzlin,20,'r','linewidth', 1);
    title('quadratic approximation');
    pause;
    n = -H \ g;
    Xnew = X+n(1);
    Ynew = Y+n(2);
    plot([X,Xnew],[Y,Ynew],'m','Linewidth',3);
    pause;
%    for i=1:2
%	p = mycg(H,-g,i,0,0*g);
%	Xnew = X+p(1);
%	Ynew = Y+p(2);
%	plot([X,Xnew],[Y,Ynew],'m','Linewidth',3);
%	title('p_k^i');
%	title('');
%	pause;
%    end
    X = Xnew; Y = Ynew;
    hold off;
end
