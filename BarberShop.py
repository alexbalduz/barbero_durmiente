import random
import time
from threading import Thread, Lock, Event
from Cliente import Customer
from Barber import Barber

mutex = Lock()

#Interval in seconds
clienteIntervaloMin = 5
clienteIntervaloMax = 15
duracionCorteMin = 3
duracionCorteMax = 15
waitingCustomers = []
	#constructor de la clase
def __init__(self, barber, numberOfSeats):
	self.barber = barber
	self.numberOfSeats = numberOfSeats
	print ('Barberia inicializa con {0} sitios'.format(numberOfSeats))
	print ('Cliente min intervalo {0}'.format(clienteIntervaloMin))
	print ('Cliente max interval {0}'.format(clienteIntervaloMax))
	print ('Haircut min duration {0}'.format(duracionCorteMin))
	print ('Haircut max duration {0}'.format(clienteIntervaloMax))
	print ('---------------------------------------')
	#Abre la barberia
def openShop(self):
	print ('Barberia esta abierto')
	workingThread = Thread(target = self.barberGoToWork)
	workingThread.start()
	#barbero se pone a trabajar
def barberGoToWork(self):
	while True:
		mutex.acquire()

		if len(self.waitingCustomers) > 0:
			c = self.waitingCustomers[0]
			del self.waitingCustomers[0]
			mutex.release()
			self.barber.cortarPelo(c)
		else:
			mutex.release()
			print('Aaah, todo terminado, se va a dormir')
			Barber.dormir()
			print('Barbero se despierta')
	#entra un cliente a la barberia
def enterBarberShop(self, customer):
	mutex.acquire()
	print ('>> {0} entra a la barberia y busca un asiento'.format(customer.name))

	if len(self.waitingCustomers) == self.numberOfSeats:
		print ('Esperando habitación está llena, {0} esta  yéndose.'.format(customer.name))
		mutex.release()
	else:
		print ('{0} se siente en la sala de espera'.format(customer.name))
		self.waitingCustomers.append(c)
		mutex.release()
		Barber.despertar()