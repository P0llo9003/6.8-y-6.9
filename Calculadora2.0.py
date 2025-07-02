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

while True:
    opc=menu('Menú Calculadora',['Sumar',"Restar","Multiplicar", "Division"])
    if opc=='5':
        print('Salir')
        break
    a=leer_operando()
    b=leer_operando()
    if opc=='1':
        print(suma(a,b))
    elif opc=="2":
        print(resta(a,b))
    elif opc=="3":
        print(multiplicacion(a,b))
    elif opc=="4":
        print(division(a,b))
    else:
        print('Opción Inválida')