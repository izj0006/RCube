
def dispatch(parm={}):
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'
    elif(parm['op'] == 'create'):
        httpResponse['status'] = 'created'
        #httpResponse['cube']=createCube(parm)
        cube=['green','green','green',
          'green','green','green',
          'green','green','green',
          'yellow','yellow','yellow',
          'yellow','yellow','yellow',
          'yellow','yellow','yellow',
          'blue','blue','blue',
          'blue','blue','blue',
          'blue','blue','blue',
          'white','white','white',
          'white','white','white',
          'white','white','white',
          'red','red','red',
          'red','red','red',
          'red','red','red',
          'orange','orange','orange',
          'orange','orange','orange',
          'orange','orange','orange']
    return cube
    #return httpResponse
    
    if(parm['op'] == 'create' & parm['f']=='f'):
        httpResponse['status'] = 'created'
        #httpResponse['cube']=createCube(parm)
        cube=['f','f','f',
          'f','f','f',
          'f','f','f',
          'yellow','yellow','yellow',
          'yellow','yellow','yellow',
          'yellow','yellow','yellow',
          'blue','blue','blue',
          'blue','blue','blue',
          'blue','blue','blue',
          'white','white','white',
          'white','white','white',
          'white','white','white',
          'red','red','red',
          'red','red','red',
          'red','red','red',
          'orange','orange','orange',
          'orange','orange','orange',
          'orange','orange','orange']
    return cube
    
def createCube(parm):
    cube=['green','green','green',
          'green','green','green',
          'green','green','green',
          'yellow','yellow','yellow',
          'yellow','yellow','yellow',
          'yellow','yellow','yellow',
          'blue','blue','blue',
          'blue','blue','blue',
          'blue','blue','blue',
          'white','white','white',
          'white','white','white',
          'white','white','white',
          'red','red','red',
          'red','red','red',
          'red','red','red',
          'orange','orange','orange',
          'orange','orange','orange',
          'orange','orange','orange']
    return cube
