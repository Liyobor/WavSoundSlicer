class Ray_Counter:

    def __init__(self,digits:int =3) -> None:
        self.count = []
        self.__digits = digits
        for i in range(digits):
            self.count.append(0)
    
    def plusOne(self):
        self.count[-1] = self.count[-1]+1
        self.count.reverse()
        index=0
        while(index != self.__digits):
            if index == len(self.count)-1 and self.count[index] == 10:
                print(index)
                print('num exceed digits,increase your digits!')
                break

            if(self.count[index]==10):
                self.count[index] = 0
                self.count[index+1]+=1
            index+=1
        self.count.reverse()

    def getFormattedCount(self)->str:
        formattedNum = ''
        for i in self.count:
            formattedNum += str(i)
        return formattedNum


    def resetCount(self):
        self.count.clear()
        for i in range(self.__digits):
            self.count.append(0)