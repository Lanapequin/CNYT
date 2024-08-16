import math
def sumaC(a,b):
    partReal=round(a[0]+b[0], 1)
    partImag=round(a[1]+b[1], 1)
    return (partReal, partImag)

def multC(a,b):
    partReal=round((a[0]*b[0])-(a[1]*b[1]), 1)
    partImag=round((a[0]*b[1])+(b[0]*a[1]), 1)
    return (partReal,partImag)

def divC(a,b):
    partReal=round(((a[0]*b[0])+(a[1]*b[1]))/((b[0]**2)+(b[1]**2)), 1)
    partImag=round(((a[1]*b[0])-(a[0]*b[1]))/((b[0]**2)+(b[1]**2)), 1)
    return (partReal,partImag)

def restaC(a,b):
    partReal=round(a[0]-b[0], 1)
    partImag=round(a[1]-b[1], 1)
    return (partReal,partImag)

def moduloC(a,b):
    modulo=math.sqrt(a**2+b**2)
    return round(modulo,1)
    
def conjugadoC(a,b):
    b=b*-1
    return (a,b)

def polarC(a,b):
    magn=math.sqrt(a**2+b**2)
    phase=round(math.atan(b/a),1)
    return (magn,phase)

def cartesianoC(a,b):
    x=round(a * math.cos(b))
    y=round(a * math.sin(b))
    return(x,y)

def phaseC(a,b):
    phase=math.atan(b/a)
    return phase

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
    print(moduloC(4,3))