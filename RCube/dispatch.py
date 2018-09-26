#parm ={'op':'create', 'f': 'f' }
def dispatch(parm={}):
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'
    elif(parm['op'] == 'create'):
        httpResponse['status'] = 'created'
        httpResponse['cube']=createCube(parm)
    return httpResponse
    
def createCube(parm):
    cube=['green','green','green',
          'green','green','green',
          'green','green','green']
    return cube