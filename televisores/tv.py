class TV:
    numTV = 0
    canal = 1
    volumen = 1
    _precio = 500
    control = ""

    def __init__(self,marca,estado):
        self._marca = marca
        self.estado = estado

        pass

    def getNumTV():
        return TV.numTV
    
    def setNumTV(numTV):
        TV.numTV = numTV

    def canalUp(self):
        if self.canal < 120:
            self.canal +=1

    def canalDown(self):
        if self.canal > 1:
            self.canal -= 1

    def volumenUp(self):
        if self.volumen < 7:
            self.volumen += 1

    def volumenDown(self):
        if self.volumen > 0:
            self.volumen -= 1

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado

    def getMarca(self):
        return self._marca
    
    def getCanal(self):
        return self.canal
    
    def getPrecio(self):
        return self._precio
    
    def getVolumen(self):
        return self.volumen
    
    def getControl(self):
        return self.control

    def setMarca(self,marca):
        self._marca = marca

    def setCanal(self,canal):
        self.canal = canal
    
    def setPrecio(self,precio):
        self._precio = precio
    
    def setVolumen(self,volumen):
        self.volumen = volumen

    def setControl(self,control):
        self.control = control