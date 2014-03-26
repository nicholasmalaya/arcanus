%% function for an image

function  ustar = ustar_fun(x,y)

global xx yy I;

% ramp
ustar = interp2(xx, yy, I, x, y);

