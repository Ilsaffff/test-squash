import numpy as np
from sklearn.linear_model import LinearRegression


def get_model():
    x_train = np.array([[50], [100], [150], [200], [250], [300]])
    y_train = np.array([250000, 500000, 750000, 1000000, 1250000, 1500000])

    model = LinearRegression()
    model.fit(x_train, y_train)
    return model


def get_square(model, x_test):
    y_pred = model.predict(x_test)
    return y_pred

