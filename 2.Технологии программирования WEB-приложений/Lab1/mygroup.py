groupmates = [
{
"name": "Александр",
"surname": "Иванов",
"exams": ["Информатика", "ЭЭиС", "Web"],
"marks": [4, 3, 5]
},
{
"name": "Иван",
"surname": "Петров",
"exams": ["История", "АиГ", "КТП"],
"marks": [4, 4, 4]
},
{
"name": "Кирилл",
"surname": "Смирнов",
"exams": ["Философия", "ИС", "КТП"],
"marks": [5, 5, 5]
},
{
"name": "Руслан",
"surname": "Трубкин",
"exams": ["История", "АиГ", "КТП"],
"marks": [3, 5, 3]
},
{
"name": "Петр",
"surname": "Семенов",
"exams": ["Философия", "ИС", "КТП"],
"marks": [4, 5, 4]
},
{
"name": "Семен",
"surname": "Сидоров",
"exams": ["Информатика", "ЭЭиС", "Web"],
"marks": [3, 4, 5]
}
]

def calc_average(_marks):
	average = 0
	num_of_marks = 0
	for mark in _marks:
		average += mark
		num_of_marks += 1
	average = average/num_of_marks
	return average


def print_students(_students, _average):
		print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
		for student in _students:
			if calc_average(student["marks"]) > _average:
				print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
			
			
average_mark = input('Введите средний балл:') 
print_students(groupmates, float(average_mark))