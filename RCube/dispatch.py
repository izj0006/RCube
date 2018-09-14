
def dispatch(parm={}):
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'
    elif(parm['op'] == 'create'):
        httpResponse['status'] = 'create'
        # replace this with your code
        cube = None
        httpResponse['cube'] = cube
    return httpResponse
