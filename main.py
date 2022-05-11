from threading import Thread, Lock, Event
import time, random
from Cliente import Customer
from Barbero import Barber
from BarberShop import BarberShop

mutex = Lock()

#Interval in seconds
clienteIntervaloMin = 5
clienteIntervaloMax = 15
duracionCorteMin = 3
duracionCorteMax = 15

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
		#Espera un tiempo aleatorio
		customerInterval = random.randrange(clienteIntervaloMin,clienteIntervaloMax+1)
		time.sleep(customerInterval)