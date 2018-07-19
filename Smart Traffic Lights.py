class SmartTrafficLight():
    def __init__(self, st1, st2):
        #Your code here
        self.st1 = st1
        self.st2 = st2
        
    def turngreen(self):
        #Your code here
        if self.st1[0] > self.st2[0]:
            self.st1[0] = 0
            return self.st1[1]
        elif self.st1[0] < self.st2 [0]:
            self.st2[0] = 0
            return self.st2[1]  
