# Ordenar listas
fruits = ['Mango', 'Piña','Guindas', 'Guayaba', 'Maracuyá']

# Ordenanos con el método sort(). Mucha atención, este método cambia la lista original de forma irreversible
# fruits.sort()
fruits.sort(reverse = True)
print(fruits)

grades = [10,9,8,10,8,8]
grades.sort(reverse = True)
print(grades)

# Atención: No funciona con listas que contienen elementos mixtos
cat_bag = [12, "Hola", True]
# cat_bag.sort()
# print(cat_bag)

# Cuidado con las mayúsculas

veggie_list = ["Papas","Quinoa", "Maíz", 'choclito', 'papitas']

# veggie_list.sort()
veggie_list.sort(key = str.lower)
print(veggie_list)