class enviroment:
    def __init__(self,initialState):
        self.state=initialState
    def getState(self):
        return self.state
    def setClean(self):
        self.state="Clean"
class SimpleReflex:
    def __init__(self):
        pass
    def Check(self,percept):
        if(percept=="Clean"):
            print("State is clean\n")
        else:
            print("State is dirty\n")
def RunAgent(agent,env,steps):
    for step in range (steps):
        CurrState=env.getState()
        agent.Check(CurrState)
        if(CurrState=="Dirty"):
            env.setClean()
            print("State cleaned on step ",step+1)
env=enviroment("Dirty")
SR=SimpleReflex()
RunAgent(SR,env,5)
