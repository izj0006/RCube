front = 'green'
right = 'yellow'
bottom = 'blue'
left = 'white'
top = 'red'
under = 'orange'
faces = [front, right, bottom, left, top, under]

def dispatch(parm={}): 
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'
     
    elif(parm['op'] == 'check'):                
        response = createCube(parm)
        if(response != 'error: duplicate faces'):
            httpResponse['status'] = 'created'
            httpResponse['cube'] = response
        else:
            httpResponse['status'] = response
    
    elif(parm['op'] == 'create'):
        if(not('cube' in parm)):
            httpResponse['status'] = 'error: missing cube'   
        
    return httpResponse

#----------inward facing methods----------------

def duplicateFaces(parm):
    for indexFace in range(0, 6):
        for indexFace2 in range(0, 6):
            if (indexFace != indexFace2):
                if faces[indexFace] == faces[indexFace2]:
                    error_message = 'error: duplicate faces'
                    return error_message

def createCube(parm):
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
        
    responseDuplicateFaces=duplicateFaces(parm)
    return responseDuplicateFaces
    
    cube = []
    for face in faces:
        for _ in range(0,9):
            cube.append(face)
    return cube
