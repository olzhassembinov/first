class Upper:
    def getString(self, string):
        self.string = string.upper()
        pass
    def printString(self):
        print(self.string)
        pass

p1 = Upper()
p1.getString(input())
p1.printString()
