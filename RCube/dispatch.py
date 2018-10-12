def dispatch(parm={}):
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'
    elif(parm['op'] == 'create'):
        httpResponse['status'] = 'created'
        httpResponse['cube']=createCube(parm)
        
    elif(parm['op'] == 'check'):
        if(not('cube' in parm)):
            httpResponse['status'] = 'error: cube must be specified'
        #if length of cube is less than 54, 'status':'cube is not sized properly
        #cubelist=parm['cube']
        #print cubelist
        print len(parm['cube'])
        
    return httpResponse
    
def createCube(parm):
    front = 'green'
    right = 'yellow'
    bottom = 'blue'
    left = 'white'
    top = 'red'
    under = 'orange'
    
    if('f' in parm):
        front = parm['f']
    if('r' in parm):
        right = parm['r']
    if('b' in parm):
        bottom = parm['b']
    if('l' in parm):
        left = parm['l']
    if('t' in parm):
        top = parm['t']
    if('u' in parm):
        under = parm['u']
        
    faces = [front, right, bottom, left, top, under]   
    for indexFace in range(0, 6):
        for indexFace2 in range(0, 6):
            if (indexFace != indexFace2):
                if faces[indexFace] == faces[indexFace2]:
                    error_message = 'error: duplicate faces'
                    return error_message
    cube = []
    for face in faces:
        for _ in range(0,9):
            cube.append(face)
    return cube

