#!/usr/bin/env python
# -*- coding: UTF-8-*-

sf=["-",2,3,4]
sg=[3,4,6,8,7]
sa=(sf,sg)



global estado
global signo
global inicial
ceros=["+",0]
uno=[0,0]
inicial=(ceros,uno)
estado=" "
signo="a"
def imprimir(a):
	g=0
	mensaje=a[0][0]
	while g<len(a[0])-1:
		mensaje += str( a[0][g+1] )
		g=g+1
	g=0
	mensaje +="."
	while g<len(a[1]):
		mensaje += str( a[1][g] )
		g=g+1
	print (mensaje)
	return mensaje
def desenca(a):
	g=0
	while g<len(a[0])-1:
		mensaje += str( a[0][g+1] )
		g=g+1
	g=0
	mensaje +="."
	while g<len(a[1]):
		mensaje += str( a[1][g] )
		g=g+1
	mensaje=float(mensaje)
	return mensaje
def quitarc(a):
	
	 entero=len(a[0])
	 decimal=len(a[1])
	 g=0
	 while g<entero-1:
		 aux=a[0][1]
		 if aux==0:
			 a[0].pop(1)
		 else:
			 g=entero
		 g=g+1
	 g=decimal-1
	 while g>0:
		 aux=a[1][g]
		 if aux==0:
			 a[1].pop(g)
		 else:
			 g=0
		 g=g-1
	 g=0
	 return a
def completar(a,b):
	entero=len(a[0])
	decimal=len(a[1])
	entero2=len(b[0])
	decimal2=len(b[1])
	po=a[0]
	pb=a[1]
	if entero<entero2:
		g=0;
		resta=entero2-entero
		while g<resta:
			po.insert(1,0)
			g=g+1;
	if decimal<decimal2:
		g=0;
		resta=decimal2-decimal
		while g<resta:
			pb.append(0)
			g=g+1
		g=0
	a=[po,pb]
	return a
def comparacion(a, b):
	a=quitarc(a)
	b=quitarc(b)
	entero=len(a[0])
	decimal=len(a[1])
	kll=50
	entero2=len(b[0])
	decimal2=len(b[1])
	
	if entero>entero2:
		respuesta="a>b"
	else:
		if entero2>entero1:
			respuesta="b>a"
		else:
			g=0
			while g<entero2:
				if a[0][g+1]==b[0][g+1]:
					kll=9
				else:
					kll=23
					g=entero2
					if a[0][g+1]>b[0][g+1]:
						respuesta="a>b"
					else:
						respuesta="b>a"
				
				g=g+1
		g=0
		if kll<20:
			a=completar(a,b)
			b=completar(b,a)
			entero2=len(b[0])
			decimal2=len(b[1])
			while g<decimal:
				if a[1][g]==b[1][g]:
					kll=99
				else:
					kll=23
					g=decimal
					if a[1][g]>b[1][g]:
						respuesta="a>b"
					else:
						respuesta="b>a"
				g=g+1
		if kll==99:
			respuesta="b=a"
	return respuesta
def sign(a,b,op,c,d):
	global estado
	global signo
	if op=="+":
		if a=="+" and b=="+":
			estado="suma"
			signo="+"
		else:
			if a=="-" and b=="-":
				estado="suma"
				signo="-"
			else:
				if a=="-" and b=="+":
					ff=comparacion(c,d)
					if ff=="a>b":
						estado="resta"
						signo="-"
						resta(c,d)
					else :
						estado="resta"
						signo="+"
						resta(d,c)
						
				else:
					ff=comparacion(c,d)
					if ff=="a>b":
						estado="resta"
						signo="+"
						resta(c,d)
					else :
						estado="resta"
						signo="-"
						resta(d,c)
	if op=="-":
		if a=="-" and b=="+":
			estado="suma"
			signo="-"
			suma(c,d)
		else:
			if a=="+" and b=="-":
				estado="suma"
				signo="+"
				suma(c,d)
			else:
				if a=="-" and b=="-":
					ff=comparacion(c,d)
					if ff=="a>b":
						estado="resta"
						signo="-"
						resta(c,d)
						estado=" "
					else :
						estado="resta"
						signo="+"
						resta(d,c)
						estado=" "
				else:
					ff=comparacion(c,d)
					if ff=="a>b":
						estado="resta"
						signo="+"
						resta(c,d)
						estado=" "
					else :
						estado="resta"
						signo="-"
						resta(d,c)
						estado=" "
	return signo
def suma(a, b):
	global estado
	global signo
	global inicial
	if estado==" ":
		signo=sign(a[0][0],b[0][0],"+",a,b)
		g=0
		
	if estado=="suma":
		g=0
		a=completar(a,b)
		b=completar(b,a)
		respuesta=inicial
		respuesta=completar(respuesta,a)
		ente=len(a[0])
		deci=len(a[1])
		residuo=0
		g=deci-1
		while g>-0.001:
			respuesta[1][g]=a[1][g]+b[1][g]+residuo
			if respuesta[1][g]>9:
				intermedio=respuesta[1][g]/10
				respuesta[1][g]=respuesta[1][g]%10
				residuo=int(intermedio)
			else:
				residuo=0
			g=g-1
				
		g=ente-1
		while g>0:
			respuesta[0][g]=a[0][g]+b[0][g]+residuo
			if respuesta[0][g]>9:
				intermedio=respuesta[0][g]/10
				respuesta[0][g]=respuesta[0][g]%10
				residuo=int(intermedio)
			else:
				residuo=0
			g=g-1
		g=0
		respuesta[0][0]=signo
		if residuo>0:
			
				a[0].insert(1,residuo)
				
	estado=" "
	return respuesta
def resta(a, b):
	
	global estado
	global signo
	global inicial
	if estado==" ":
		signo=sign(a[0][0],b[0][0],"-",a,b)
		g=0
		
	if estado=="resta":
		g=0
		a=completar(a,b)
		b=completar(b,a)
		respuesta=inicial
		respuesta=completar(respuesta,a)
		ente=len(a[0])
		deci=len(a[1])
		residuo=0
		g=deci-1
		while g>-0.001:
			respuesta[1][g]=a[1][g]-b[1][g]-residuo
			if respuesta[1][g]<0:
				respuesta[1][g]=respuesta[1][g]+10
				residuo=1
			else:
				residuo=0
			g=g-1
				
		g=ente-1
		while g>0:
			respuesta[0][g]=a[0][g]-b[0][g]-residuo
			if respuesta[0][g]<0:
				respuesta[0][g]=respuesta[0][g]+10
				residuo=1
			else:
				residuo=0
			g=g-1
		g=0
		respuesta[0][0]=signo
		if residuo>0:
			
				a[0].insert(1,"error")
				
	estado=" "
	return respuesta
def multiplicacion(a, b):
    pass


def division(a, b):
	
	
    pass

res=suma(sa,sa)
imprimir(res)

#if __name__ == "__main__":
 #   print(imprimir(pi()))
