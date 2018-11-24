front = 'green'
right = 'yellow'
bottom = 'blue'
left = 'white'
top = 'red'
under = 'orange'
faces = [front, right, bottom, left, top, under]

face = ['f','F','r','R','b','B','l','L','t','T','u','U']
edges = []
middle = []
corners = []

def dispatch(parm={}): 
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'
    elif(parm['op'] == 'create'):                
        response = createCube(parm)
        if(response != 'error: duplicate faces'):
            httpResponse['status'] = 'created'
            httpResponse['cube'] = response
        else:
            httpResponse['status'] = response
            
    elif(parm['op'] == 'check'):
        if(not('cube' in parm)):
            httpResponse['status'] = 'error: missing cube'
        else:
            response = checkSize(parm)
            if(response == 'error: invalid size'):
                httpResponse['status'] = response
            else:
                response = determineConfig(parm)
                httpResponse['status'] = response

    elif(parm['op'] == 'rotate'):
        if(not('cube' in parm)):
            httpResponse['status'] = 'error: missing cube'
        if(not('face' in parm)):
            httpResponse['status'] = 'error: missing face'
        if(not(parm['face'] in face)):
            httpResponse['status'] = 'error: face is unknown'
            
    return httpResponse

#----------inward facing methods----------------

def checkSize(parm):
    cube=parm['cube']
    cubelist=cube.split(",")
    if((len(cubelist))!=54):
        error_message = 'error: invalid size'
    return error_message

def duplicateFaces(parm):
    for indexFace in range(0, 6):
        for indexFace2 in range(0, 6):
            if (indexFace != indexFace2):
                if faces[indexFace] == faces[indexFace2]:
                    error_message = 'error: duplicate faces'
                    return error_message
                
def chunks(cube,n):
    for i in range(0,54,n):
        yield cube[i:i+n]

def determineConfig(parm):
    cube = parm['cube']
    splitcube = list(chunks(cube,9))
        
    if( splitcube[0].count(splitcube[0][1]) == 9 & splitcube[1].count(splitcube[1][1]) == 9 & splitcube[2].count(splitcube[2][1]) == 9 & splitcube[3].count(splitcube[3][1]) == 9 & splitcube[4].count(splitcube[4][1]) == 9 & splitcube[5].count(splitcube[5][1]) == 9 ):
        message = 'FULL'
    
    elif(cube=='r,w,r,w,w,w,r,w,r, w,g,w,g,g,g,w,g,w,o,y,o,y,y,y,o,y,o, y,b,y,b,b,b,y,b,y, g,r,g,r,r,r,g,r,g, b,o,b,o,o,o,b,o,b'):
        #cube[0] == cube[2] == cube[6] == cube[8] & cube[1] == cube[3]== cube[4]== cube[5]== cube[7]
        message = 'CROSSES'
        
    elif(cube=='y,y,y,y,r,y,y,y,y, o,o,o,o,b,o,o,o,o,w,w,w,w,o,w,w,w,w,r,r,r,r,g,r,r,r,r,b,b,b,b,w,b,b,b,b, g,g,g,g,y,g,g,g,g'):
        message = 'SPOTS'
        
    else:
        message = 'UNKNOWN'
        
    return message

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
    for f in faces:
        for _ in range(0,9):
            cube.append(f)
            
    return cube