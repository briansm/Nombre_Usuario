# -*- Coding: utf-8 -*-


#---------------Funcion de verificacion------------------
def verification_user(user):

    if len(user)>=6 and len(user)<=12:
        print("Entrando...")

    else:
        print("ERROR: No cumple con normas establecidas")
#---------------Funcion de verificacion------------------
def verification_password(password):
    cont_min=0
    cont_mayus=0
    cont_digit=0
    cont_simbol=0
    if len(password)>=8:
        for c in password:
            if c.isdigit():
                cont_digit=cont_digit+1
            elif c>='a' and c<='z':
                cont_min=cont_min+1
            elif c>='A' and c<='Z':
                cont_mayus=cont_mayus+1
            else:
                cont_simbol=cont_simbol+1
        if cont_min>=1 and cont_digit>=1 and cont_mayus>=1 and cont_simbol>=1:
            print("Entrando...")
        else:
            print("ERROR")
    else:
        print("ERROR: No cumple con normas establecidas")

#-----------------Funcion que solicita datos-----------------
def run():
    while True:
        user=str(input('''
                    --------------------------
                    Ingrese Nombre de Usuario:

                   '''))
        verification_user(user)
        password=str(input('''
                    --------------------------
                    Ingrese Nombre de password:

                   '''))
        verification_password(password)



if __name__== '__main__':
    run()
