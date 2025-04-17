class Camera:
    """없으면 안되겠더라. ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ"""
    position = (int,int)
    def __init__(self, 
                 pos:(int,int)):
        
        self.position = pos
    
    
    def move(self, dx:int = 0, dy:int = 0):
        self.position = (self.position[0] + dx, self.position[1] + dy)
        
        