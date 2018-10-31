
corners = []
edges = []

def dispatch(parm={}):
    httpResponse = {'status'}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'
    else:
        if(not('cube' in parm)):
            httpResponse['status'] = 'error: missing cube'
        else:
            if(parm['op'] == 'create'):
                response = createCube(parm)
                if(response != 'error: duplicate faces'):
                    httpResponse['status'] = 'created'
                    httpResponse['cube']=response
            elif(parm['op'] == 'check'):
                response = checkSize(parm)
                if(response == 'cube is not sized properly'):
                    httpResponse['status'] = 'cube is not sized properly'  
                else:
                    httpResponse['status'] = 'checked'
                    response = determineConfig(parm)
                    httpResponse['cube']=response
    return httpResponse

def checkSize(parm):
    cube=parm['cube']
    cubelist=cube.split(",")
    if((len(cubelist))==54):
        message = 'cube is correctly sized'
    else:
        message = 'cube is not sized properly'
    return message    
    
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
                if(faces[indexFace] == faces[indexFace2]):
                    error_message = 'error: duplicate faces'
                    return error_message
                
    #if(response != 'error: duplicate faces'):
    cube = []
    for face in faces:
        for _ in range(0,9):
            cube.append(face)
                    
    return cube

def determineConfig(parm):
    if(parm['cube'] == 'f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u'):
        message = 'FULL'
    elif(parm['cube'] == 'r,w,r,w,w,w,r,w,r,w,g,w,g,g,g,w,g,w,o,y,o,y,y,y,o,y,o,y,b,y,b,b,b,y,b,y,g,r,g,r,r,r,g,r,g,b,o,b,o,o,o,b,o,b'):
        message = 'CROSSES'
    elif(parm['cube'] == 'y,y,y,y,r,y,y,y,y,o,o,o,o,b,o,o,o,o,w,w,w,w,o,w,w,w,w,r,r,r,r,g,r,r,r,r,b,b,b,b,w,b,b,b,b,g,g,g,g,y,g,g,g,g'):
        message = 'SPOTS'
    else:
        message = 'UNKNOWN'
    return message