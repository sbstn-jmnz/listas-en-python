todo_list = ['Sacar la basura','Barrer la entrada','Pasear al Boby','Regar las plantas']

# Partir recorriendo con el clásico "for"
for todo in todo_list:
  print(todo)

print('----------------------------')

# También podemos utilizar la estructura de control "while"
index = 0
while index < len(todo_list):
  print(todo_list[index])
  index += 1

print('----------------------------')

# Hay otra forma de recorre las listas
# Una forma más avanzada utilizando lists comprehensios
[print(todo) for todo in todo_list]

