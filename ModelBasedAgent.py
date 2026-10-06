class env:
    def __init__(self,*state):
        self.state=list(state)
    def getpercept(self,index):
        return self.state[index]
    def clean(self):
        self.state="Clean"
class ModelAgent:
    def __init__(self):
        self.model={}
    def update(self,percept):
        self.model['current']=percept
    def predict(self):
        if(self.model['current']=="Dirty"):
            return("Clean the room")
        else:
            return("Room is clean")
    def act(self,percept):
        self.update(percept)
        return self.predict()
def RunAgent(env,MdAg,len):
    for i in range(len):
        percept=env.getpercept(i)
        action=MdAg.act(percept)
        if (action=="Clean the room"):
            print(MdAg.predict(),end="--> ")
            MdAg.update("Clean")
            print("Action: Room Cleaned")
        else:
            print(MdAg.predict())
        

e=env("Dirty","Clean","Clean","Dirty")
m=ModelAgent()

RunAgent(e,m,4)
        
        
        