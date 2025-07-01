def menu(titulo,opciones):
    print(titulo)
    print('=====================')
    i=1
    for opc in opciones:
        print(i,'.-',opc)
        i=i+1
    print(i,'.- Salir')
    opcion=input('Ingrese Opción: ')
    return opcion

def suma(a,b):
    try:
        op1=int(a)
        op2=int(b)
        return op1+op2
    except:
        return None

def leer_operando():
    while True:
        try:
            num=int(input('Ingrese Número: '))
            return num
        except:
            print('Debe ser un número')

while True:
    opc=menu('Menú Calculadora',['Sumar'])
    if opc=='2':
        print('Salir')
        break
    a=leer_operando()
    b=leer_operando()
    if opc=='1':
        print(suma(a,b))
    else:
        print('Opción Inválida')
