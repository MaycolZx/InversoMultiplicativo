def ExtEuclides(a,b):
  if (b==0):
    return a,1,0
  d,x1,y1 = ExtEuclides(b,a%b)
  x = y1
  y = x1 - y1 * int(a/b)
  return d,x,y

def Euclides(a,b):
  if b ==0:
    return a
  else:
    return Euclides(b,a%b)

def inverso(a,n):
  if (Euclides(a,n)==1):
    d,x,y = ExtEuclides(a,n)
    return (f"Su inverso multiplicativo es {(x%n)}")
  else:
    return "No tiene inverso multiplicativo."

a=(int(input("Ingrese 'a': ")))
n=(int(input("Ingrese 'n': ")))
print(inverso(a,n))
