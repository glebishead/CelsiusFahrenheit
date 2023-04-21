import json


data = [
	{"name_rus": "Нейромант", "author": "Уилльям Гибсон", "params": (1, 0, 1)},
	{"name_rus": "Маленький принц", "author": "Антуан де Сент-Экзюпери", "params": (0, 0, 0)},
	{"name_rus": "Призрак в доспехах", "author": "Масамунэ Сиро", "params": (0, 0, 1)},
	{"name_rus": "Зов Ктулху", "author": "Говард Филлипс Лавкрафт", "params": (0, 1, 0)},
	{"name_rus": "Пробуждение Левиафана", "author": "Джеймс Кори", "params": (0, 1, 1)},
	{"name_rus": "Бойцовский клуб", "author": "Чак Паланик", "params": (1, 0, 0)},
	{"name_rus": "Пищеблок", "author": "Алексей Иванов", "params": (1, 1, 0)},
	{"name_rus": "Я - легенда", "author": "Ричард Мэтисон", "params": (1, 1, 1)},
	{"name_rus": "Мечтают ли андроиды об электроовцах?", "author": "Филип Дик", "params": (1, 0, 1)},
	{"name_rus": "Лавина", "author": "Нил Стивенсон", "params": (1, 0, 1)},
	]

with open('some_books.json', 'w') as _file:
	json.dump(data, _file, ensure_ascii=False)