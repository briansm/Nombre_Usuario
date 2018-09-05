# -*- Coding: utf-8 -*-


#---------------Funcion de verificacion------------------
def verification_user(user):
    cont_c=0
    for c in user:
        cont_c=cont_c+1
    if cont_c>=6 and cont_c<=12:
        print("Entrando...")
    elif cont_c<6:
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
