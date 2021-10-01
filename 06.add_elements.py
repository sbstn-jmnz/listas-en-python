todo_list = ['Sacar la basura','Barrer la entrada','Pasear al Boby','Regar las plantas']

# Para agregar elementos podemos utilizar la función insert() que viene el todas las listas. El primer parámetro es el índice que ocupará el nuevo elemento

todo_list.insert(2, 'Dejar la Cocacola')

# Podemos agregar directamente al final con el método append() que también viene con todas las listas

todo_list.append('Cocinar saludable')

print(todo_list)

# Mezclar listas

movies = ['Matris', 'Wars Star', 'El viejo de las argollas']
books = ['Poemas de Baldor', 'Chistes de Proschle', 'Horóscopo Xino']

# El método extend incorpora al arreglo lo que está "extendiendo"
movies.extend(books)
# Acá movies tendrá el contenido de ambas listas
print(movies)
# La lista books sigue existiendo
print(books)

