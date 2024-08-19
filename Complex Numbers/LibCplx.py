import math

# SUMA DE NUMEROS COMPLEJOS
def sumaC(a,b):
    partReal=round(a[0]+b[0], 1)
    partImag=round(a[1]+b[1], 1)
    return (partReal, partImag)

# MULTIPLICACION DE NUMEROS COMPLEJOS
def multC(a,b):
    partReal=round((a[0]*b[0])-(a[1]*b[1]), 1)
    partImag=round((a[0]*b[1])+(b[0]*a[1]), 1)
    return (partReal,partImag)

# DIVISION DE NUMEROS COMPLEJOS
def divC(a,b):
    partReal=round(((a[0]*b[0])+(a[1]*b[1]))/((b[0]**2)+(b[1]**2)), 1)
    partImag=round(((a[1]*b[0])-(a[0]*b[1]))/((b[0]**2)+(b[1]**2)), 1)
    return (partReal,partImag)

# RESTA DE NUMEROS COMPLEJOS
def restaC(a,b):
    partReal=round(a[0]-b[0], 1)
    partImag=round(a[1]-b[1], 1)
    return (partReal,partImag)

# MODULO DE UN NUMERO COMPLEJO
def moduloC(partReal,partImag):
    modulo=math.sqrt(partReal**2+partImag**2)
    return round(modulo,1)

# CONJUGADO DE UN NUMERO COMPLEJO   
def conjugadoC(partReal,partImag):
    return (partReal,-partImag)

# CONVERSION DE REPRESENTACION CARTESIANA A POLAR
def polarC(partReal,partImag):
    magn=math.sqrt(partReal**2+partImag**2)
    fase=round(math.atan2(partImag,partReal),1)
    return (magn,fase)

# CONVERSION DE REPRESENTACION POLAR A CARTESIANA
def cartesianoC(magn,fase):
    x=round(magn * math.cos(fase))
    y=round(magn * math.sin(fase))
    return(x,y)

# FASE DE UN NUMERO COMPLEJO
def faseC(partReal,partImag):
    fase=math.atan2(partImag,partReal)
    return fase

# REPRESENTACION RECTANGULAR DE UN NUMERO COMPLEJO
def prettyPrintingC(partReal,partImag):
    if partImag<0:
        print(partReal,partImag,'i')
    else:
        print(partReal,'+',partImag,'i')


if __name__ == '__main__':
    partReal,partImag=sumaC((3,2.8),(1.5,-2))
    prettyPrintingC(partReal,partImag)
    partReal,partImag=multC((3,2.8),(1.5,-2))   
    prettyPrintingC(partReal,partImag)
    partReal,partImag=divC((3,2.8),(1.5,-2))
    prettyPrintingC(partReal,partImag)
    partReal,partImag=restaC((3,2.8),(1.5,-2))
    prettyPrintingC(partReal,partImag)
    print(moduloC(5,2))
    print(conjugadoC(5,-2))
    print(polarC(5,2))
    print(cartesianoC(5,0.6))
    print(faseC(5,2))