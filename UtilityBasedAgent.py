class env:
    def __init__(self,*state):
        self.state=list(state)
    def getpercept(self,index):
        return self.state[index]
    def clean(self,index):
        self.state[index]="Clean"
class UtilityAgent:
    def __init__(self):
        self.utility={"Dirty": -10,"Clean": 10}
    def calculateUtility(self,percept):
        return self.utility[percept]
    def act(self,percept):
        if(percept=="Dirty"):
            return("Room need cleaning")
        else:
            return("No need of cleaning")
def RunAgent(env,uti,len):
    totalUti=0
    for i in range(len):
        per=env.getpercept(i);
        action=uti.act(per)
        utility=uti.calculateUtility(per)
        print(i+1,") percept: ",per," | Action: ",action," | Utility: ",utility)
        totalUti+=utility
    print("Total utility: ",totalUti)
e=env("Dirty","Clean","Clean","Dirty")
u=UtilityAgent()
RunAgent(e,u,4)
        