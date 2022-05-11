import random, time
from threading import Thread, Lock, Event
mutex = Lock()

#Interval in seconds
clienteIntervaloMin = 5
clienteIntervaloMax = 15
duracionCorteMin = 3
duracionCorteMax = 15

class Barber:
    barberWorkingEvent = Event()
	#Establece barbero como domido
def dormir(self):
		self.barberWorkingEvent.wait()
	#Establece barbero como despierto
def despertar(self):
		self.barberWorkingEvent.set()
	#Corta el pelo
def cortarPelo(self, customer):
		#Establece barbero como ocupado
		self.barberWorkingEvent.clear()

		print ('{0} se está cortando el pelo'.format(customer.name))
		#Espera un tiempo aleatorio
		randomHairCuttingTime = random.randrange(duracionCorteMin, duracionCorteMax+1)
		time.sleep(randomHairCuttingTime)
		print ('{0} está teminado'.format(customer.name))