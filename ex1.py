import numpy as np
import json

data_set = [
	((0, 0, 0), 0), ((0, 0, 1), 0),
	((0, 1, 0), 0), ((0, 1, 1), 0),
	((1, 0, 0), 1), ((1, 0, 1), 1),
	((1, 1, 0), 0), ((1, 1, 1), 1)]


def activation_function(x):
	return int(x >= 1)


def predict(cool_hero, horror, sci_fi):
	x = np.array([cool_hero, horror, sci_fi])
	weights = np.array([[1.5], [-1], [1]])
	sum_out = np.dot(x, weights)
	out = np.array([activation_function(x) for x in sum_out])
	return out


with open('some_books.json', 'r') as _file:
	data = json.load(_file)

for el in data:
	name = el['name_rus']
	author = el['author']
	cool, horror, sci_fi = el['params']
	s_l = []
	if cool:
		s_l.append('крутой главный герой')
	if horror:
		s_l.append('ужасы')
	if sci_fi:
		s_l.append('научная фантастика')
	info = ',\n'.join(s_l)
	if info:
		info = 'Её тэги: ' + info + '.\n'
	if predict(cool, horror, sci_fi):
		print(f"Книга {name}.\nЕё автор: {author}.\n{info}Эта книга была посоветована Вам.")
	else:
		print(f"Книга {name}.\nЕё автор: {author}.\n{info}Возможно, она Вам не понравится.")
	print('--------------')

