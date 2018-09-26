#parm ={'op':'create', 'f': 'f','r':'r','b':'b','l':'l','t':'t','u':'u' }
#parm.setdefault('f','green')



def dispatch(parm={}):
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'
    elif(parm['op'] == 'create'):
        httpResponse['status'] = 'created'
        httpResponse['cube']=createCube(parm)
    elif(parm['op'] == 'create' & parm['f'] == 'f' & parm['r'] == 'r'& parm['b'] == 'b'& parm['l'] == 'l'& parm['t'] == 't'& parm['u'] == 'u'):
        httpResponse['status'] = 'created'
        httpResponse['cube']=createCube(parm)
    return httpResponse
    
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