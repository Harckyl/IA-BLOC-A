import threading
import environment as env
class cleaningAgent:
    test = 1

    def __init__(self):
        self.test = 2
        self.position = 0

    def observeEnvironment(self):
        env.environment.getChoice(self.position)

    def testing(self, testingvariable):
        self.test = self.test + testingvariable
        print(self.test)
    
    
    

cleaningagent = cleaningAgent()
cleaningagent.testing(12)

