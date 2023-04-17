import numpy as np


def relu(x):  # activation function
	return int(x >= 1)


def predict(cool_hero, horror, sci_fi):
	x = np.array([cool_hero, horror, sci_fi])
	w11 = [0.6, 0.3, 0]
	w12 = [0.5, -0.5, 1]
	weight1 = np.array([w11,  w12])
	weight2 = np.array([-1, 1])
	
	sum_hidden = np.dot(weight1, x)
	
	out_hidden = np.array([relu(x) for x in sum_hidden])
	
	sum_end = np.dot(weight2, out_hidden)
	return relu(sum_end)


for cool in (0, 1):
	for horror in (0, 1):
		for sci_fi in (0, 1):
			print(f"({cool, horror, sci_fi}) - {predict(cool, horror, sci_fi)}")
