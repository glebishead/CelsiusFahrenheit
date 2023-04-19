import numpy as np

data_set = [
	((0, 0, 0), 0), ((0, 0, 1), 0),
	((0, 1, 0), 0), ((0, 1, 1), 0),
	((1, 0, 0), 1), ((1, 0, 1), 1),
	((1, 1, 0), 0), ((1, 1, 1), 1)]


def activation_function(x):
	return int(x >= 1)


def predict(cool_hero, horror, sci_fi):
	x = np.array([cool_hero, horror, sci_fi])
	weights = np.array([[1.5], [-1], [0.5]])
	sum_out = np.dot(x, weights)
	out = np.array([activation_function(x) for x in sum_out])
	return out


for cool in (0, 1):
	for horror in (0, 1):
		for sci_fi in (0, 1):
			print(f"({cool, horror, sci_fi}) - {predict(cool, horror, sci_fi)}")

