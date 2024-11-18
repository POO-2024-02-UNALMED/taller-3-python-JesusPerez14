from televisores.tv import TV

class Control:
    def __init__(self):
        self.tv = "" 
        pass

    def enlazar(self,tv):
        self.tv = tv
        tv.setControl(self)

    def getTv(self):
        return self.tv
    
    def setTv(self,tv):
        self.tv = tv

    def canalUp():
        if TV.getCanal() < 120:
            TV.canalUp()

    def canalDown():
        if TV.getCanal() > 1:
            TV.canalDown()

    def volumenUp():
        if TV.getVolumen() < 7:
            TV.volumenUp()

    def volumenDown():
        if TV.getVolumen()> 0:
            TV.volumenDown()

    def turnOn():
        TV.turnOn()

    def turnOff():
        TV.turnOff()

    def setCanal(self,canal):
        TV.setCanal(canal)

    def setVolumen(self,volumen):
        TV.setVolumen(volumen)