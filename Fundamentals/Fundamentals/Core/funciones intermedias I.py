"""Actualizar valores en diccionarios y listas"""
x = [ [5,2,3], [10,8,9] ]
estudiantes = [
    {'first_name' :  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Cambiar el valor 10 en x a 15
x[1][0] = 15;

#Cambia el "apellido" del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name'] = "Bryant"

#En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['fútbol'][0] = "Andrés"

#Cambia el valor 20 en z a 30.
z[0]['y'] = 30

print(x, estudiantes, directorio_deportes)




"""Iterar a través de una lista de diccionarios"""
estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(lista):
    for obj in lista:
        for key, val in obj.items():
            if(key=='last_name'):
                print(key, "-", val)
            else:
              print(key, "-", val, end=', ')

iterateDictionary(estudiantes)


"""Obtener valores de una lista de diccionarios"""
def iterateDictionary2(key_name, some_list):
    for obj in some_list:
        print(obj.get(key_name, "La clave no existe"))

iterateDictionary2('first_name', estudiantes)



"""Iterar a través de un diccionarios con valores de lista"""
dojo = {
  'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
  'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(value), key)
        for dato in value:
            print(dato)
        print()

printInfo(dojo)





