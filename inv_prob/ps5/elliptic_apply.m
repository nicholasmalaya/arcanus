% Apply the reduced GN system

function GNV = elliptic_apply(V, chi, W, A, C, R, X)

% solve the state equation
du = A \ (chi.*(-C*V));
% solve the adjoint equation
dp = A' \ (chi.*(-W*du));
% compute the Hessian-vector application
GNV = C' * dp + R * V;


