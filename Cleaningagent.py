import threading

class cleaningAgent:
    test = 1
    def __init__(self):
        self.test = 2
    
    def testing(self, testingvariable):
        self.test = self.test + testingvariable
        print(self.test)

cleaningagent = cleaningAgent()
cleaningagent.testing(12)
