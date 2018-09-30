
global estado
global signo
global inicial
global corrimiento
global uno
global david
global davi
corrimiento=0
ceros=["+",0]
uno=[0,0]
inicial=(ceros,uno)
estado=" "
signo="a"
david=" "
davi=" "
def desenca(a):
	g=0
	mensaje=a[0][0]
	while g<len(a[0])-2:
		mensaje += str( a[0][g+1] )
		g=g+1
	g=0
	mensaje +="."
	while g<len(a[1]):
		mensaje += str( a[1][g] )
		g=g+1
	mensaj=float(mensaje)
	return mensaj
def quitarc(aj):
	
	 entero=len(aj[0])
	 decimal=len(aj[1])
	 g=0
	 while g<entero-1:
		 aux=aj[0][1]
		 if aux==0:
			 aj[0].pop(1)
		 else:
			 g=entero
		 g=g+1
	 g=decimal-1
	 while g>0:
		 aux=aj[1][g]
		 if aux==0:
			 aj[1].pop(g)
		 else:
			 g=0
		 g=g-1
	 g=0
	 return aj
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
	a=(po,pb)
	return a
def comparacion(a, b):
	global david
	global davi
	davi="rf"
	a1=quitarc(a)[0][:]
	a2=quitarc(a)[1][:]
	a=(a1,a2)
	b1=quitarc(b)[0][:]
	b2=quitarc(b)[1][:]
	b=(b1,b2)
	entero=len(a[0])
	decimal=len(a[1])
	kll=50
	entero2=len(b[0])
	decimal2=len(b[1])
	
	if entero>entero2:
		respuesta="a>b"
	else:
		if entero2>entero:
			respuesta="b>a"
		else:
			g=0
			while g<entero2-1:
				if a[0][g+1]==b[0][g+1]:
					kll=9
				else:
					kll=23
					if a[0][g+1]>b[0][g+1]:
						respuesta="a>b"
					else:
						respuesta="b>a"
					g=entero2
				
				g=g+1
		g=0
		if kll<20:
			a=completar(a,b)
			b=completar(b,a)
			entero2=len(b[0])
			decimal2=len(b[1])
			g=0
			while g<decimal2:
				
				if a[1][g]==b[1][g]:
					kll=99
				else:
					kll=23
					if a[1][g]>b[1][g]:
						respuesta="a>b"
					else:
						respuesta="b>a"
					g=decimal2
				g=g+1
		if kll==99:
			respuesta="b=a"
	
	david=respuesta
	return respuesta
def sign(a,b,op,c,d):
	global estado
	global signo
	global inicial
	respuesta1=inicial[0][:];
	respuesta2=inicial[1][:];
	respuesta=(respuesta1,respuesta2)
	cc= MyFloat(c[0],c[1])
	dd= MyFloat(d[0],d[1])
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
						respuesta=cc-dd
						respuesta=volvertup(respuesta)
					else :
						estado="resta"
						signo="+"
						respuesta=dd-cc
						respuesta=volvertup(respuesta)
				else:
					ff=comparacion(c,d)
					if ff=="a>b":
						estado="resta"
						signo="+"
						respuesta=cc-dd
						respuesta=volvertup(respuesta)
					else :
						estado="resta"
						signo="-"
						respuesta=dd-cc
						respuesta=volvertup(respuesta)
	if op=="-":
		if a=="-" and b=="+":
			estado="suma"
			signo="-"
			respuesta=cc+dd
			respuesta=volvertup(respuesta)
		else:
			if a=="+" and b=="-":
				estado="suma"
				signo="+"
				respuesta=cc+dd
				respuesta=volvertup(respuesta)
			else:
				if a=="-" and b=="-":
					ff=comparacion(c,d)
					if ff=="a>b":
						estado="resta"
						signo="-"
						respuesta=cc-dd
						respuesta=volvertup(respuesta)
						estado=" "
					else :
						estado="resta"
						signo="+"
						respuesta=dd-cc
						respuesta=volvertup(respuesta)
						estado=" "
				else:
					ff=comparacion(c,d)
					if ff=="a>b":
						estado="resta"
						signo="+"
						respuesta=cc-dd
						respuesta=volvertup(respuesta)
						estado=" "
					else :
						estado="resta"
						signo="-"
						respuesta=dd-cc
						respuesta=volvertup(respuesta)
						estado=" "
	if op=="*":
		estado="*"
		if (a=="+" and b=="+") or (a=="-" and b=="-"):
			signo="+"
		else:
			signo="-"
	if op=="/":
		estado="/"
		if (a=="+" and b=="+") or (a=="-" and b=="-"):
			signo="+"
		else:
			signo="-"
	
	return respuesta
def pasaraunosolo(ag):
	decimal=len(ag[1])	
	ga=0
	while ga<decimal-1:
		ag[0].append(ag[1][0])
		ag[1].pop(0)
		ga=ga+1
		
	a123=ag[0][:]
	a223=ag[1][:]
	a123.append(a223[0])
	a223.pop(0)	
	ag=(a123,a223)
	
	return ag
def vnew(a,tamaño,e):
	if e>0:
		a[0].pop(0)
	g=0
	while g<tamaño:
		a[0].append(0)
		g=g+1
	return a
def vnow(a,tamaño,e):
	if e>0:
		a[1].pop(0)
	g=0
	while g<tamaño:
		a[1].append(0)
		g=g+1
	return a
def recuf(a,b):
	global inicial
	entero=len(a[0])
	decimal=len(a[1])
	c=a[0][entero-1]
	d=b[0][entero-1]
	lespesta1=inicial[0][:];
	tespesta1=inicial[0][:];
	lespesta2=inicial[1][:];
	tespesta2=inicial[1][:];
	lespesta=(lespesta1,lespesta2);
	tespesta=(tespesta1,tespesta2)

	a1=a[0][:]
	b1=b[0][:]
	a2=a[1][:]
	b2=b[1][:]
	a1.pop(entero-1)	
	b1.pop(entero-1)
	a=(a1,a2)
	b=(b1,b2)
	lespesta=completar(lespesta,a);
	tespesta=completar(tespesta,b);
	g=entero-2
	re1=0
	re2=0

	
	while g>0:
		lespesta[0][g]=a[0][g]*d+re1
		if lespesta[0][g]>9:
			interm=lespesta[0][g]/10
			re1=int(interm)
			mut=lespesta[0][g]%10
			lespesta[0][g]=mut
			
		else:
			re1=0
		tespesta[0][g]=b[0][g]*c+re2
		if tespesta[0][g]>9:
			interm=tespesta[0][g]/10
			re2=int(interm)
			mut=tespesta[0][g]%10
			tespesta[0][g]=mut
		else:
			re2=0
		g=g-1
	if re1>0:

		lespesta[0].insert(1,re1)
		#tespesta[0].insert(1,0)
	if re2>0:
		tespesta[0].insert(1,re2)
		#lespesta[0].insert(1,0)
	tespesta=quitarc(tespesta)
	lespesta=quitarc(lespesta)
	reptu=suma(tespesta,lespesta)
	return reptu
def dfimal(a,deci):
	g=0
	a=vnow(a,deci,0)
	tama=len(a[0])
	while g<deci:
		a[1][deci-g-1]=a[0][tama-1-g]
		a[0].pop(tama-1-g)
		g=g+1
	return a
def division(a, b):
	global inicial
	olucion1=inicial[0][:];
	olucion2=inicial[1][:];
	olucion=(olucion1,olucion2)
			
	aa=desenca(a)
	ba=desenca(b)
	respt=aa/ba;
	azucal=str(respt)
	tamaño=len(azucal)
	g=0
	variab=9
	olucion=quitarc(olucion)
	olucion[1].pop(0)
	while g<tamaño:
		if azucal[g]=="." or variab==4:
			if azucal[g]=="." :
				variab=4
			else:
				variab=4
				olucion[1].append(azucal[g])
		else:
			olucion[0].append(azucal[g])
			variab=0
		
		g=g+1
	if olucion[0][1]=="+" or olucion[0][1]=="-":
		olucion[0][0]=olucion[0][1]
		olucion[0][1]=0
		olucion=quitarc(olucion)
	variab=9
	g=0
	return olucion
def volvertup(a):
	global inicial
	a=str(a)
	tamaño=len(a)
	variab=43
	respuest1=inicial[0][:];
	respuest2=inicial[1][:];
	respuest=(respuest1,respuest2)
	respuest=quitarc(respuest)
	respuest[1].pop(0)
	g=0
	while g<tamaño:
		if a[g]=="." or variab==4:
			if a[g]=="." :
				variab=4
			else:
				variab=4
				respuest[1].append(a[g])
		else:
			respuest[0].append(a[g])
			variab=0
		
		g=g+1
	variab=45
	
	return respuest
def suma(a, b):
	hg=len(a[0])
	pg=len(b[0])
	if hg<2:
		hg=hg
	else:
		if a[0][1]=="+" or a[0][1]=="-":
			a[0][1]=0
	if pg<2:
		pg=pg
	else:
		if b[0][1]=="+" or b[0][1]=="-":
			b[0][1]=0
	global estado
	global signo
	global inicial
	global davi
	davi="rf"
	if estado==" ":
		respuesta=sign(a[0][0],b[0][0],"+",a,b)
		g=0
		
	if estado=="suma" or estado=="*" or estado=="/":
		g=0
		a=completar(a,b)
		b=completar(b,a)
		respuesta1=inicial[0][:];
		respuesta2=inicial[1][:];
		respuesta=(respuesta1,respuesta2)
		respuesta=completar(respuesta,a)
		ente=len(a[0])
		deci=len(a[1])
		residuo=0
		g=deci-1
		
		while g>-0.001:
			tmaj=len(a[1])
			tmbj=len(b[1])
			if tmaj<2 :
				a[1].append(0)
				
			if tmbj<2 :
				b[1].append(0)			
			if a[1][0]=="0" or b[1][0]=="0" or a[1][1]=="0" or b[1][1]=="0":
				if a[1][0]=="0" or b[1][0]=="0":
					if a[1][0]=="0":
						a[1][0]=0
					else:
						b[1][0]=0
				else:
					if a[1][1]=="0":
						a[1][1]=0
					else:
						b[1][1]=0
						
					
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
				respuesta[0].insert(1,residuo)
		if estado=="*":
			estado="*"
		else:
			estado=" "
	if estado=="*":
		estado="*"
	else:
		estado=" "
	respuesta1=quitarc(respuesta)[0][:]
	respuesta2=quitarc(respuesta)[1][:]
	respuesta=(respuesta1,respuesta2)
	return respuesta	
def resta(a, b):
	hg=len(a[0])
	pg=len(b[0])
	if hg<2:
		hg=hg
	else:
		if a[0][1]=="+" or a[0][1]=="-":
			a[0][1]=0
	if pg<2:
		pg=pg
	else:
		if b[0][1]=="+" or b[0][1]=="-":
			b[0][1]=0
	global estado
	global signo
	global inicial
	global davi
	comparacion(a,b)
	respuesta1=inicial[0][:];
	respuesta2=inicial[1][:];
	respuesta=(respuesta1,respuesta2)

	if estado==" ":
		respuesta=sign(a[0][0],b[0][0],"-",a,b)
		g=0
		
	if estado=="resta":
		davi="tres"
		g=0
		a=completar(a,b)
		b=completar(b,a)
		respuesta1=inicial[0][:];
		respuesta2=inicial[1][:];
		respuesta=(respuesta1,respuesta2)
		respuesta=completar(respuesta,a)
		a=completar(a,respuesta)
		b=completar(b,respuesta)
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
			
				respuesta[0].insert(1,"error")
	estado=" "
	respuesta1=quitarc(respuesta)[0][:]
	respuesta2=quitarc(respuesta)[1][:]
	respuesta=(respuesta1,respuesta2)
	return respuesta
def multiplicacion(a, b):
	global signo
	global estado
	global corrimiento
	global inicial
	global uno
	global davi
	davi="rf"
	
	aq=quitarc(a)[0][:]
	aq1=quitarc(a)[1][:]
	a=(aq,aq1)
		
	bq=quitarc(b)[0][:]
	bq1=quitarc(b)[1][:]
	b=(bq,bq1)
	
	
	sign(a[0][0],b[0][0],"*",a,b)
	entero=len(a[0])
	decimal=len(a[1])
	entero2=len(b[0])
	decimal2=len(b[1])
	corrimiento=decimal+decimal2
	
	aq=pasaraunosolo(a)[0][:]
	aq1=pasaraunosolo(a)[1][:]
	a=(aq,aq1)

	bq=pasaraunosolo(b)[0][:]
	bq1=pasaraunosolo(b)[1][:]
	b=(bq,bq1)
	
	a=completar(a,b)
	b=completar(b,a)
	
	entero=len(a[0])
	decimal=len(a[1])
	
	solucion1=inicial[0][:];
	solucion2=inicial[1][:];
	solucion=(solucion1,solucion2)

	solucion=vnew(solucion,entero*2,0)
	tama=len(solucion[0])
	A=a[0][:]
	B=b[0][:]
	aux=0
	jF1=inicial[0][:];
	jF2=inicial[1][:];
	jF=(jF1,jF2)
	g=entero-1
	multi1=inicial[0][:];
	multi2=inicial[1][:];
	multi=(multi1,multi2)
	ret1=inicial[0][:];
	ret2=inicial[1][:];
	ret=(ret1,ret2)
	an=a[0][:]
	bn=b[0][:]
	an2=a[1][:]
	bn2=b[1][:]
	asd=(an,an2)
	bsd=(bn,bn2)
	sera=89
	nsera=86
	gf=98
	while g>0:
		asd=completar(asd,bsd)
		bsd=completar(bsd,asd)
		intermedi=A[g]*B[g]/10
		residuo=int(intermedi)
		multip=A[g]*B[g]%10
		multi[0][1]=multip
		
		Nf1=suma(jF,multi)[0][:]
		Nf2=suma(jF,multi)[1][:]
		Nf=(Nf1,Nf2)
		
		multi1w=inicial[0][:];
		multi2w=inicial[1][:];
		multi=(multi1w,multi2w)		
		
		actualice=len(Nf[0])
		solucion[0][tama-1-2*aux]=Nf[0][actualice-1]
		Nf[0].pop(actualice-1)
		jF=recuf(asd,bsd)
		actu=len(asd[0])
		act=len(bsd [0])

		
		a134=asd[0][:]
		a234=asd[1][:]
		a134.pop(actu-1)	
		asd=(a134,a234)
		
		a13=bsd[0][:]
		a23=bsd[1][:]
		a13.pop(act-1)	
		bsd=(a13,a23)
		
		
		jF=suma(jF,Nf)
	
		

		ret[0][1]=residuo

		jF=suma(jF,ret)
		
				
		ret1w=inicial[0][:];
		ret2w=inicial[1][:];
		ret=(ret1w,ret2w)
		
		
		actualice=len(jF[0])
		solucion[0][tama-2-2*aux]=jF[0][actualice-1]
		
		jF[0].pop(actualice-1)
		aux=aux+1
		g=g-1
	
		asd1=quitarc(asd)[0][:]
		asd2=quitarc(asd)[1][:]
		asd=(asd1,asd2)
		
		bsd1=quitarc(bsd)[0][:]
		bsd2=quitarc(bsd)[1][:]
		
		bsd=(bsd1,bsd2)
		sera=len(asd[0])
		nsera=len(bsd[0])
		if sera==1 or nsera==1:
			g=0

	
	solucion=quitarc(solucion)
	actualice=len(jF[0])
	if actualice>1:
		g=0
		while g<actualice-1:
			solucion[0].insert(1,jF[0][actualice-g-1])
			g=g+1
		g=0
	
	solucion=dfimal(solucion,corrimiento)
	aux=0
	
	estado=" "
	
	if (solucion[0][1]=="+" or  solucion[0][1]=="-" ) :
		solucion[0][1]=0	
	solucion1a=quitarc(solucion)[0][:]
	solucion2a=quitarc(solucion)[1][:]
	solucion=(solucion1a,solucion2a)
	if (a[0][0]=="-" and b[0][0]=="+") or  (a[0][0]=="+" and b[0][0]=="-") :
		signo="-"
	else:
		signo="+"
	solucion[0][0]=signo
	return solucion


class MyFloat:
	

    def __init__(self,entera,decimal):
					self.entera=entera
					self.decimal=decimal
    def __add__(self,other):
					global estado
					global signo
					global inicial
					global davi
					a=(self.entera,self.decimal)
					b=(other.entera, other.decimal)
					davi="rf"
					if estado==" ":
						respuesta=sign(a[0][0],b[0][0],"+",a,b)
						g=0
						
					if estado=="suma" or estado=="*" or estado=="/":
						g=0
						a=completar(a,b)
						b=completar(b,a)
						respuesta1=inicial[0][:];
						respuesta2=inicial[1][:];
						respuesta=(respuesta1,respuesta2)
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
								respuesta[0].insert(1,residuo)
						estado=" "
					estado=" "
					respuesta1=quitarc(respuesta)[0][:]
					respuesta2=quitarc(respuesta)[1][:]
					respuesta=(respuesta1,respuesta2)
					hg=len(respuesta[0])
					if hg<2:
						hg=hg
					else:
						if respuesta[0][1]=="+" or respuesta[0][1]=="-":
							respuesta[0][0]=respuesta[0][1]
							respuesta[0][1]=0
					return MyFloat(respuesta[0],respuesta[1])	
    def __sub__(self,other):
					a=(self.entera,self.decimal)
					b=(other.entera, other.decimal)					
					global estado
					global signo
					global inicial
					global davi
					comparacion(a,b)
					respuesta1=inicial[0][:];
					respuesta2=inicial[1][:];
					respuesta=(respuesta1,respuesta2)

					if estado==" ":
						respuesta=sign(a[0][0],b[0][0],"-",a,b)
						g=0
						
					if estado=="resta":
						davi="tres"
						g=0
						a=completar(a,b)
						b=completar(b,a)
						respuesta1=inicial[0][:];
						respuesta2=inicial[1][:];
						respuesta=(respuesta1,respuesta2)
						respuesta=completar(respuesta,a)
						a=completar(a,respuesta)
						b=completar(b,respuesta)
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
							
								respuesta[0].insert(1,"error")
					estado=" "
					respuesta1=quitarc(respuesta)[0][:]
					respuesta2=quitarc(respuesta)[1][:]
					respuesta=(respuesta1,respuesta2)
					hg=len(respuesta[0])
					if hg<2:
						hg=hg
					else:
						if respuesta[0][1]=="+" or respuesta[0][1]=="-":
							respuesta[0][0]=respuesta[0][1]
							respuesta[0][1]=0
					return MyFloat(respuesta[0],respuesta[1])   
    def __mul__(self,other):
					a=(self.entera,self.decimal)
					b=(other.entera, other.decimal)	
					solucion=multiplicacion(a, b)
					return MyFloat(solucion[0],solucion[1]) 
    def __div__(self):
        pass

    def __radd__(self):
        pass

    def __rsub__(self):
        pass

    def __rmul__(self):
        pass

    def __rdiv__(self):
        pass

    def __str__(self):
					g=0
					a=(self.entera,self.decimal)
					if a=="a=b" or a=="b=a" or a=="a>b" or a=="a<b" or a=="b>a" or a=="b<a" or a=="verdadero" or a=="falso":
						mensaje=a
					else:
						if david=="b=a" and davi=="tres" :
							mensaje="0"
						else:
							mensaje=a[0][0]
							while g<len(a[0])-1:
								mensaje += str( a[0][g+1] )
								g=g+1
							g=0
							mensaje +="."
							while g<len(a[1]):
								mensaje += str( a[1][g] )
								g=g+1
						
					return mensaje

    def __repr__(self):
        pass

    def __eq__(self):
        pass

    def __ne__(self):
        pass

if __name__ == "__main__":
    # Escribir aca el codigo para calcular pi. Al finalizar el calculo solo
    # debe imprimir el valor de pi, sin otros textos ni nada
	sf2=["+",2]
	af3=[3,]
	sf3=["-",5]
	af4=[8,]
	
	tf6= MyFloat(sf2,af3)
	tf7= MyFloat(sf3,af4)
	m=tf6*tf7
	print (tf6)
	print (tf7)
	print (m)
