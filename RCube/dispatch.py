
def dispatch(parm={}):
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'
    elif(parm['op'] == 'create'):
        httpResponse['status'] = 'created'
              
        
        # replace this with your code
        cube = [ ]
        # replace this with your code
             
        
        httpResponse['cube'] = cube
    return httpResponse
