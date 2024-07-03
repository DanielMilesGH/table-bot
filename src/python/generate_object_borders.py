# this function is designed to be called by flask
def generate_object_borders() -> dict:
    # TODO - ADD ACTUAL LOGIC 
    
    jsonToSend = {}
    
    # borders in LineString WKT notation
    bordersToSend = ["(0 0, 100 100, 200 100)"]
    
    jsonToSend['borders'] = bordersToSend
    
    return jsonToSend