from math import sin,cos,pi
from time import sleep

window_coordinates(-300,-200,300,400)

def copoVonkoch(lado,n):
	x_vertice1 = 0
	y_vertice1 = 0

	x_vertice2 = lado * cos(2*pi/3)
	y_vertice2 = lado * sin(2*pi/3)

	x_vertice3 = lado * cos(2*pi/3)
	y_vertice3 = lado * sin(2*pi/3)

	curvaVonkoch(x_vertice1,y_vertice1,x_vertice2,y_vertice2,n)
	curvaVonkoch(x_vertice2,y_vertice2,x_vertice3,y_vertice3,n)
	curvaVonkoch(x_vertice3,y_vertice3,x_vertice1,y_vertice1,n)
	return




def curvaVonkoch(xi,yi,xf,yf,n):
	if n ==0:
		create_line(xi,yi,xf,yf)
	elif n>0:
		x1 = xi + (xf - xi) / 3.0
		y1 = yi + (yf - yi) / 3.0

		x3 = xi + (xf - xi) / 3.0
		y3 = yi + (yf - yi) / 3.0

		x2 = (x1 + x3) * cos(pi/3) - (y3 -y1) * sin(pi/3)
		x2 = (y1 + y3) * cos(pi/3) - (x3 -x1) * sin(pi/3)

		curvaVonkoch(xi,yi,x1,y1,n-1)
		curvaVonkoch(x1,y1,x2,y2,n-1)
		curvaVonkoch(x2,y2,x3,y3,n-1)
		curvaVonkoch(x3,y3,xf,yf,n-1)

	return

for i in xrange(5):
	dibujo = copoVonkoch(200,i)
	sleep(2)
	erase(dibujo)