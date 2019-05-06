from Robo import *

cor     = input('Cor: ')
sentido = input('Sentido: ')
vel     = int(input('Velocidade: '))
posX    = int(input('PosX: '))
posY    = int(input('PosY: '))
comando = input("Comando: ")

robot = Robo(vel, cor, sentido, posX, posY)

while (comando != "exit"):

	if comando == 'w':
		robot.moverFrente()

	elif comando == 'a':
		robot.moverEsquerda()

	elif comando == 's':
		robot.moverRetornar()

	elif comando == 'd':
		robot.moverDireita()

	elif comando == 'v':
		vel = int(input("Velocidade: "))
		robot.setVel(vel)

	elif comando == 'c':
		cor = input("Cor: ")

	elif comando == 'auto':
		l = []
		ans = 's'
		while ans == 's':
			posX = int(input('PosX tesouro: '))
			posY = int(input('PosY tesouro: '))
			coord = posX, posY
			l.append(coord)
			ans = input('Continuar? [s]')

		robot.moverAutomatico(l)

	comando = input("comando: ")