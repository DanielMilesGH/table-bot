class BaseRobot():
    x: int # positive integer
    y: int # positive integer 
    def __init__(self, x:int=None, y:int=None, pos:tuple[int,int]=None):
        if (pos != None):
            self.x=pos[0]
            self.y=pos[1]
        elif (x!=None & y!=None):  
            self.x = x
            self.y = y 
        else:
            raise ValueError("need to give position")

    def get_pos(self) -> tuple[int,int]:
        return (self.x, self.y)
    def get_x(self) -> int:
        return self.x
    def get_y(self) -> int:
        return self.y 

    def update_pos(self, pos:tuple[int,int]):
        self.x=pos[0]
        self.y=pos[1]
    