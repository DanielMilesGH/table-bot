# TODO: grab the data from some other python file
# this function is designed to be called by flask
def move_generation():
    # TODO - ADD ACTUAL LOGIC 
    
    jsonToSend = {}
    
    # moves in (x,y), where increasing goes right,down
    movesToSend = ["(0,0)","(0,5)","(0,10)","(5,10)"]
    
    jsonToSend['moves'] = movesToSend
    
    return jsonToSend