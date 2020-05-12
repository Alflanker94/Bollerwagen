class Cont(object):
    def __init__(self, Joystick):
        self.Joystick = Joystick
        self.TastePS = False
        self.PS = 10

        self.TasteL1 = False
        self.L1 = 4
        self.TasteL2 = False
        self.L2 = 6
        self.TasteL3 = False
        self.L3 = 11

        self.TasteR1 = False
        self.R1 = 5
        self.TasteR2 = False
        self.R2 = 7
        self.TasteR3 = False
        self.R3 = 12

        self.TasteSelect = False
        self.Select = 8
        self.TasteStart = False
        self.Start = 9

        self.TasteUp = False
        self.Up = 13
        self.TasteDown = False
        self.Down = 14
        self.TasteLeft = False
        self.Left = 15
        self.TasteRight = False
        self.Right = 16

        self.TasteX = False
        self.X = 0
        self.TasteKreis = False
        self.Kreis = 1
        self.TasteDreieck = False
        self.Dreieck = 2
        self.TasteQuadrat = False
        self.Quadrat = 3
        self.Listed = [self.PS, self.L1, self.L2, self.L3, self.R1, self.R2, self.R3, self.Select, self.Start, self.Up, self.Down, self.Left, self.Right, self.X, self.Kreis, self.Dreieck, self.Quadrat, ]

    def akPS(self,zustand_Neu):
        self.TastePS = zustand_Neu
        
    def akL1(self, zustand_Neu):
        self.TasteL1 = zustand_Neu

    def akL2(self, zustand_Neu):
        self.TasteL2 = zustand_Neu

    def akL3(self, zustand_Neu):
        self.TasteL3 = zustand_Neu
    
    def akR1(self, zustand_Neu):
        self.TasteR1 = zustand_Neu
    
    def akR2(self, zustand_Neu):
        self.TasteR2 = zustand_Neu
    
    def akR3(self, zustand_Neu):
        self.TasteR3 = zustand_Neu

    def akSelect(self, zustand_Neu):
        self.TasteSelect = zustand_Neu
        
    def akStart(self, zustand_Neu):
        self.TasteStart = zustand_Neu
        
    def akUp(self, zustand_Neu):
        self.TasteUp = zustand_Neu
        
    def akDown(self, zustand_Neu):
        self.TasteDown = zustand_Neu
        
    def akLeft(self, zustand_Neu):
        self.TasteLeft = zustand_Neu
        
    def akRight(self, zustand_Neu):
        self.TasteRight = zustand_Neu
        
    def akX(self, zustand_Neu):
        self.TasteX = zustand_Neu
        
    def akKreis(self, zustand_Neu):
        self.TasteKreis = zustand_Neu
        
    def akDreieck(self, zustand_Neu):
        self.TasteDreieck = zustand_Neu
        
    def akQuadrat(self, zustand_Neu):
        self.TasteQuadrat = zustand_Neu



""" stwPS, stwL1, stwL2, stwL3, stwR1, stwR2, stwR3, stwSelect, stwStart, 
    stwUp, stwDown, stwLeft, stwRight, stwX, stwKreis, stwDreieck, stwQuadrat):
        self.PS = stwPS
        self.L1 = stwL1
        self.L2 = stwL2
        self.L3 = stwL3
        self.R1 = stwR1
        self.R2 = stwR2
        self.R3 = stwR3
        self.Select = stwSelect
        self.Start = stwStart
        self.Up = stwUp
        self.Down = stwDown
        self.Left = stwLeft
        self.Right = stwRight
        self.X = stwX
        self.Kreis = stwKreis
        self.Dreieck = stwDreieck
        self.Quadrat = stwQuadrat """


def objekt(args):
    pass


C = Cont(objekt)
print(C.__dict__)
