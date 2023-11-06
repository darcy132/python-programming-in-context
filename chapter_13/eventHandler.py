AttributeError#Author : Darcy Brown
#Author email : Yuzhoulky@gmail.com
#Coding date: Oct 2023
'''
    * This code implement a simple event handling simulation program:
'''
class EventHandler:
    def __int__(self):
        self.__queue = []                           #save the event
        self.__eventKeeper = {}                     #Dictionary for storing event types and callback functions
    def addEvent(self,eventName):                   
        self.__queue.append(eventName)
    
    def registerCallback(self,event,func):
        self.__eventKeeper[event] = func
    
    def run(self):
        while(True):
            if len(self.__queue) > 0:
                nextEvent = self.__queue.pop(0)
                self.__eventKeeper[nextEvent]()
            else:
                print('queue is empty')
def myMouse(void):
    print('Oh no,the mouse was clicked!')
def myKey(void):
    print('A key has been pressed.')

if __name__== '__main__':
    eh = EventHandler()
    eh.registerCallback('key',myKey)
    eh.registerCallback('mouse',myMouse)
    eh.addEvent('mouse')
    eh.addEvent('key')
    eh.addEvent('mouse')
    eh.run()



