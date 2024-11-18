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

    def canalUp(self):
        if self.tv.getCanal() < 120:
            self.tv.canalUp()

    def canalDown(self):
        if self.tv.getCanal() > 1:
            self.tv.canalDown()

    def volumenUp(self):
        if self.tv.getVolumen() < 7:
            self.tv.volumenUp()

    def volumenDown(self):
        if self.tv.getVolumen()> 0:
            self.tv.volumenDown()

    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()

    def setCanal(self,canal):
        self.tv.setCanal(canal)

    def setVolumen(self,volumen):
        self.tv.setVolumen(volumen)