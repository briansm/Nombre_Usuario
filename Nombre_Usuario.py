# -*- Coding: utf-8 -*-


#---------------Funcion de verificacion------------------
def verification_user(user):

    if len(user)>=6 and len(user)<=12:
        print("Entrando...")
    elif len(user)<6:
        print("Minimo 6 caracteres")
    else:
        print("Maximo 12 caracteres")

#-----------------Funcion que solicita datos-----------------
def run():
    while True:
        user=str(input('''
                    --------------------------
                    Ingrese Nombre de Usuario:

                   '''))
        verification_user(user)



if __name__== '__main__':
    run()
