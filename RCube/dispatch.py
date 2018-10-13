front = 'f'
right = 'r'
bottom = 'b'
left = 'l'
top = 't'
under = 'u'

faces = [front, right, bottom, left, top, under]

def dispatch(parm={}):
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'
        
    elif(parm['op'] == 'create'):
        response = createCube(parm)
        if(response != 'error: duplicate faces'):
            httpResponse['status'] = 'created'
            httpResponse['cube']=response
            
    elif(parm['op'] == 'check'):
        if(not('cube' in parm)):
            httpResponse['status'] = 'error: cube must be specified'
        #=======================================================================
        # else:
        #     response = checkSize(parm)
        #     if(response != 'error: cube is not sized properly'):
        #         httpResponse['status'] = 'size checked'
        #         httpResponse['cube']=response
        #=======================================================================
                
    return httpResponse

def checkDupeColors(parm):
    for indexFace in range(0, 6):
        for indexFace2 in range(0, 6):
            if (indexFace != indexFace2):
                if(faces[indexFace] == faces[indexFace2]):
                    error_message = 'error: duplicate faces'
                    return error_message
    
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

    response = checkDupeColors(parm)
    
    if(response != 'error: duplicate faces'):
        cube = []
        for face in faces:
            for _ in range(0,9):
                cube.append(face)
                    
    return cube