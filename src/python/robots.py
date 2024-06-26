class BaseRobot():
    x: int # positive integer
    y: int # positive integer 
    def __init__(self, x:int, y:int, pos:tuple[int,int] | None = None):
        if (pos != None):
            self.x=pos[0]
            self.y=pos[1]
        else:  
            self.x = x
            self.y = y 
        
        # images should be 400x400, making robot length 0.05 image
        self.size = 20

    def get_pos(self) -> tuple[int,int]:
        return (self.x, self.y)
    def get_x(self) -> int:
        return self.x
    def get_y(self) -> int:
        return self.y 

    # returns params to make pygame rect
    def to_pygame_rect(self) -> tuple[int,int,int,int]:
        return (self.x, self.y, self.size, self.size)
    
    def update_pos(self, pos:tuple[int,int]):
        self.x=pos[0]
        self.y=pos[1]

    def move(self, dx, dy):
        self.x += dx 
        self.y += dy
    



if __name__ == "__main__":
    print("hello!")