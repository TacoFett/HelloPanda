from direct.showbase.ShowBase import ShowBase
import math, sys, random
#Set the assets
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.fighter = self.loader.loadModel('./Assets/sphere')
        self.fighter.reparentTo(self.render)
        self.fighter.setColorScale(1.0, 0.0, 0.0, 1.0)
        self.parent = self.loader.loadModel('.//Assets/cube')
        #Sets the "base" for our character in a circle of cubes with a gap
        x = 0
        for i in range(100):
            theta = x
            self.placeholder2 = self.render.attachNewNode('Placeholder2')
            self.placeholder2.setPos(50.0 * math.cos(theta), 50.0 * math.sin(theta), 0.0 * math.tan(theta))
            red = 0.6 + random.random() * 0.4
            green = 0.6 + random.random() * 0.4
            blue = 0.6 + random.random() * 0.4
            self.placeholder2.setColorScale(red, green, blue, 1.0)
            self.parent.instanceTo(self.placeholder2)
            x = x + 0.06
        #Left movement (this had to be here because it applies to self, you are moving)
        self.accept('a', self.negativeX, [1])
        self.accept('a-up', self.negativeX, [0])
        self.accept('escape', self.quit)
        #Right movement
        self.accept('d', self.positiveX, [1])
        self.accept('d-up', self.positiveX, [0])
        self.accept('escape', self.quit)
        #Up movement
        self.accept('w', self.positiveY, [1])
        self.accept('w-up', self.positiveY, [0])
        self.accept('escape', self.quit)
        #Down movement
        self.accept('s', self.negativeY, [1])
        self.accept('s-up', self.negativeY, [0])
        self.accept('escape', self.quit)

        #Disables the mouse    
        base.disableMouse()
        #Set the camera angle to be top down
        base.camera.setPos(0.0, 0.0, 250.0)
        base.camera.setHpr(0.0, -90.0, 0.0)
        #Adds the ability to stop moving
    #Left
    def negativeX(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.moveNegativeX, 'moveNegativeX')
        else:
            self.taskMgr.remove('moveNegativeX')
    def moveNegativeX(self,task):
        self.fighter.setX(self.fighter, -1)
        return task.cont
    #Down
    def negativeY(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.moveNegativeY, 'moveNegativeY')
        else:
            self.taskMgr.remove('moveNegativeY')
    def moveNegativeY(self,task):
        self.fighter.setY(self.fighter, -1)
        return task.cont
    #Right
    def positiveX(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.movepositiveX, 'movepositiveX')
        else:
            self.taskMgr.remove('movepositiveX')
    def movepositiveX(self,task):
        self.fighter.setX(self.fighter, 1)
        return task.cont
    #Up
    def positiveY(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.movePositiveY, 'movePositiveY')
        else:
            self.taskMgr.remove('movePositiveY')
    def movePositiveY(self,task):
        self.fighter.setY(self.fighter, 1)
        return task.cont
    def quit(self):
        sys.exit()    
app = MyApp()
app.run()
