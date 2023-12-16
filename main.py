from sklearn import datasets
import math


def main():
	res=None
	while(res is None):
		act=int(input("Выберите из предложенного, \n 0. Проверка в заданной точке X1\n 1. Проверка вектора X\n"))
		if(act==0):
			x1_inp()
			res = func(x1)
		elif(act==1):
			x_inp()
			res = func(x)
		else:
			print("Ошибка выбора. Попробуйте еще раз :)")
	if(isinstance(res,list)is not True):
		print (f"Результат вычисления функции в точке X1={x1}: {res}")
	else:
		for i in range(len(res)):
			print(f"Результат вычисления функции в точке X{i}: {res[i]}")



def func(x):
	if(isinstance(x,list)is not True):
		res=0
		res=(x*math.log(0.25*x)+12)/(x*math.log(math.pow(0.25*x,2))+0.8)
	else:
		res=[]
		for i in x:
			res.append((i*math.log(0.25*i)+12)/(i*math.log(math.pow(0.25*i,2))+0.8))
	return res

def x1_inp():
	global x1
	x1=int(input("Введите точку X1: "))

def x_inp():
	global x
	x=[]
	x1=int(input("Введите нижнюю границу вектора: "))
	x2=int(input("Введите верхнюю границу вектора, "))
	dx=float(input("Введите шаг: "))

	xt=x1
	while(xt<=x2):
		x.append(xt)
		xt+=dx
	


main()