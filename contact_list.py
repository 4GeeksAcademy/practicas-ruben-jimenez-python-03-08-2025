# Coloca el python y nombre del archivo en te Terminal, en este caso => python contact_list.py  pulase Enter.
# Recordatorio: clear =para limpiar la terminar pero permacercer donde estabas.
# Recordatorio: Control + C para salir de ese apartado de la terminal.

def show_options():
    print('''Elige una opciòn:
          1.Agregar contacto
          2.Mostrar contacto
          3.Eliminar contacto
          4.Buscar contacto
          5.Salir''')

contact_list =[]

# input_user=input('Elige una opciòn:')
# Cuando creemos el while, moveremos esta línea a su interior.

def add_contact():
    name= input('Nombre:')
    phone=input('Telefono:')

    new_contact={
        'name' : name,
        'phone' : phone
    }
    contact_list.append(new_contact)
    print('Contactos guardados:')

def show_contact():
    if not contact_list:
        print('no hay ningun contacto')
    else:
     print('Contactos guardados:')
    for index, contact in enumerate(contact_list,1): 
           print(f"{index}. {contact['name']} - {contact['phone']}")
# Usamos enumerate() para sacar el ítem con el índice.
# En el paréntesis de enumerate indicamos (la lista, string, ... todo lo que sea iterable), y el índice desde el que empezará.
# En Python, primero se coloca el índice en la parte del (for). => for index, contact

def delete_contact():
    delete = input('Nombre a eliminar:')
    for contact in contact_list:
        if delete.lower() == contact['name'].lower():
            contact_list.remove(contact)
            print('Contacto eliminado')
            return
    print('Contacto no encontrado')

def search_contact():

    search = input('Buscar contacto: ')
    results = [contact for contact in contact_list if search.lower() in contact['name'].lower()]

# Lo que primero,
# que se devuelva como  (contact), lo que sacamos con un (for ) contact in contact_list,
# si cumple (if) lo que escriba el usuario (search).todo en minusculas (.lower()),
#  si lo contiene (in), en  contact['name'].lower()

    if not results:
         print('No hay nada')
    else:
        for contact in results:
            print(f"Nombre: {contact['name']}")

while True:
# while crear un bucle, mientras se cumplan las condiciones.
# input siempre retornara un string.g
        show_options()
        input_user=input('Elige una opciòn:')

        if  input_user== '1':
            add_contact()
        elif input_user== '2':
            show_contact()
        elif input_user== '3':
            delete_contact()
        elif input_user== '4':
            search_contact()
        elif input_user=='5':
            print('Hasta la proxima')
            break
# break finalizar el bucle.
        else:
            print('No encontrada, prueva otra vez')

            

                
        
        





