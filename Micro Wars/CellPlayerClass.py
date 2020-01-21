#cellPlayer class
class CellPlayer:
    def __init__(self, pos, sprite, direction, speed, hp, DNA):
        self.pos = pos
        self.sprite = sprite
        self.direction = direction
        self.speed = speed
        self.hp = hp
        self.DNA = DNA

    #getters
    def getPos(self):
        return pos
    
    def getDirection(self):
        return direction

    def getSprite(self):
        return sprite

    def getSpeed(self):
        return speed

    def getHP(self):
        return hp

    def getDNA(self):
        return DNA
        
    #setters
    def setPos(self, newPos):
        pos = newPos

    def setDirection(self, newDirection):
        direction = newDirection

    def setSpeed(self, newSpeed):
        speed = newSpeed

    def setHp(self, newHp):
        hp = newHp

    def setDNA(self, newDNA):
        DNA = newDNA
        
