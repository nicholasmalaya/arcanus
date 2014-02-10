% apply K'*K + alpha*I to an input vector

function   out = apply(in,K1,K2,N1,N2,alpha)

% reshape vector of size N2*N1 to N2xN1-matrix
in_matrix = reshape(in,N2,N1);

% compute alpha*in
alpha_in_matrix = in_matrix * alpha;

% compute K*in
Kin = (K1 * (K2 * in_matrix)')';
% compute K'*K*in (note that K is symmetric)
KKin = (K1 * (K2 * Kin)')';

% output (K*K + alpha*I)*in again as vector
out = KKin(:) + alpha_in_matrix(:);


