class Data:
    __instance = None

    __X = []
    __Y = []
    __Poles = []

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Data.__instance == None:
            Data()
        return Data.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Data.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Data.__instance = self

    def getX(self):
        return self.__X
    def getY(self):
        return self.__Y
    def getPoles(self):
        return self.__Poles

    def setX(self,X):
        self.__X = X
    def setY(self,Y):
        self.__Y = Y
    def setPoles(self,Poles):
        self.__Poles = Poles