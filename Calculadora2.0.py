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
        op1=float(a)
        op2=float(b)
        return op1+op2
    except:
        return None
    
def resta(a,b):
    try:
        op1=float(a)
        op2=float(b)
        return op1-op2
    except:
        return None
    
def multiplicacion(a,b):
    try:
        op1=float(a)
        op2=float(b)
        return op1*op2
    except:
        return None

def division(a,b):
    try:
        op1=float(a)
        op2=float(b)
        if op2==0:
            print("No se puede dividir por cero...")
            return
        else:
            return op1/op2
    except:
        return None

def leer_operando():
    while True:
        try:
            num=float(input('Ingrese Número: '))
            return num
        except:
            print('Debe ser un número')




