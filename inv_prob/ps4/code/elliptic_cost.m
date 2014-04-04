%% Evaluate cost function for given dof vector X

function   [cost, misfit, reg] = evaluate_cost(fem, X)

% makes the finite element structure use the FEM vector X in
% evaluating the below integrals
fem.sol = femsol(X);

% integration of misfit and regularization
misfit = postint (fem, '0.5 * (u - ud)^2');
reg = postint (fem, '0.5 * gamma * realsqrt(ax^2+ay^2+0.1)');
cost = misfit + reg;