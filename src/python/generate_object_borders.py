# TODO: grab the data from some other python file
# this function is designed to be called by flask
def generate_object_borders() -> dict:
    # TODO - ADD ACTUAL LOGIC 
    
    jsonToSend = {}
    
    # borders are lines, in (x1,y1,x2,y2) notation
    bordersToSend = ["(0,0,100,100)", "(100,100,200,100)"]
    
    jsonToSend['borders'] = bordersToSend
    
    return jsonToSend