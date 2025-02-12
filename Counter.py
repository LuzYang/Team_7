class Counter:
    def __init__(self):
        self.__count = 0

    def addCount(self):
        self.__count += 1

    def getCount(self):
        return self.__count

    def zeroCount(self):
        self.__count = 0
 