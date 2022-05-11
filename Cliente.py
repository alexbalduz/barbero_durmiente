import random

class Cliente:

    def __init__ (self, numCliente, estado):
        self.numCliente = numCliente
        self.estado = estado
        self.tiempoEsperado = 0
        self.tiempoDeEspera = random.randrange(5,25)

    def getNumCliente(self):
        return self.numCliente

    def setNumCliente(self, x):
        self.numCliente = x

    def getEstado(self):
        return self.estado