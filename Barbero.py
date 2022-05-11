from threading import Thread, Lock, Event
import time, random

mutex = Lock()

#Interval in seconds
clienteIntervaloMin = 5
clienteIntervaloMax = 15
duracionCorteMin = 3
duracionCorteMax = 15

class BarberShop:
	waitingCustomers = []

	def __init__(self, barber, numberOfSeats):
		self.barber = barber
		self.numberOfSeats = numberOfSeats
		print ('Barberia inicializa con {0} sitios'.format(numberOfSeats))
		print ('Cliente min intervalo {0}'.format(clienteIntervaloMin))
		print ('Cliente max interval {0}'.format(clienteIntervaloMax))
		print ('Haircut min duration {0}'.format(duracionCorteMin))
		print ('Haircut max duration {0}'.format(clienteIntervaloMax))
		print ('---------------------------------------')

	def openShop(self):
		print ('Barberia esta abierto')
		workingThread = Thread(target = self.barberGoToWork)
		workingThread.start()

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
				barber.dormir()
				print('Barbero se despierta')

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
			barber.despertar()

class Customer:
	def __init__(self, name):
		self.name = name

class Barber:
	barberWorkingEvent = Event()

	def dormir(self):
		self.barberWorkingEvent.wait()

	def despertar(self):
		self.barberWorkingEvent.set()

	def cortarPelo(self, customer):
		#Establece barbero como ocupado
		self.barberWorkingEvent.clear()

		print ('{0} se está cortando el pelo'.format(customer.name))

		randomHairCuttingTime = random.randrange(duracionCorteMin, duracionCorteMax+1)
		time.sleep(randomHairCuttingTime)
		print ('{0} está teminado'.format(customer.name))


if __name__ == '__main__':
	customers = []
	customers.append(Customer('Rubén'))
	customers.append(Customer('Pablo'))
	customers.append(Customer('Lorenzo'))
	customers.append(Customer('Alberto'))
	customers.append(Customer('David'))
	customers.append(Customer('Javier'))
	customers.append(Customer('Alejandro'))
	customers.append(Customer('Enrique'))
	customers.append(Customer('Héctor'))
	customers.append(Customer('Jorge'))
	customers.append(Customer('Jaime'))
	customers.append(Customer('Asier'))
	customers.append(Customer('Carlos'))
	customers.append(Customer('Juan'))


	barber = Barber()

	barberShop = BarberShop(barber, numberOfSeats=3)
	barberShop.openShop()

	while len(customers) > 0:
		c = customers.pop()
		#nuevos clientes entran a la tienda
		barberShop.enterBarberShop(c)
		customerInterval = random.randrange(clienteIntervaloMin,clienteIntervaloMax+1)
		time.sleep(customerInterval)