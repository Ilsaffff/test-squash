from unittest import TestCase
import numpy as np
from main import get_model, get_square


class LinearRegressionTest(TestCase):

    def test_predictions(self):
        x_test = np.array([[75], [125], [175]])
        model = get_model()
        y_pred = get_square(model, x_test)

        self.assertAlmostEqual(y_pred[0], 375000, delta=1000)
        self.assertAlmostEqual(y_pred[1], 625000, delta=1000)
        self.assertAlmostEqual(y_pred[2], 875000, delta=1000)

