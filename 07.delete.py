todo_list = ['Hacer la cama', 'Barrer el patio', 'Comer menos azucar']

# Podemos eliminar elementos de listas con el método remove()

# todo_list.remove('Hacer la cama')

# print(todo_list)

# Podemos eliminar elementos por su índice con el método pop(indice)

# todo_list.pop(1)

# print(todo_list)

# Si llamamos al método pop() sin argumento. Se eliminan el último elemento

# todo_list.pop()

# print(todo_list)

# También tenemos el método especial "del". Esté es un método especial y no es tan frecuente
# Podemos pasar el índice para eliminar un elemento específico

del todo_list[1]
print(todo_list)

# Ó eliminar la colección completa, incluyendo la variable que lo referencia

del todo_list
# print(todo_list)

todo_list = ['Hacer la cama', 'Barrer el patio', 'Comer menos azucar']

# Existe además el método clear() para vaciar la lista

todo_list.clear()
print(todo_list)