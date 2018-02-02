import numpy as np
from sklearn.linear_model import LinearRegression

def regression_coef(X, Y, part=1):
    model = LinearRegression(fit_intercept=True)
    lx = int(len(X)*part)
    inds = np.array([[x] for x in X[-lx:]])
    deps = np.array(Y[-lx:])
    model.fit(inds, deps)
    return (model.coef_[0], model.intercept_)
