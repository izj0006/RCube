import unittest
import httplib
import json

class DispatchTest(unittest.TestCase):
        
    def setUp(self):
        self.key = "status"
        self.errorValue = "error:"
        self.operation ="op"
        self.scramble ="create"

    @classmethod
    def setUpClass(cls):
        cls.ERROR = "error:"
        cls.DEFAULT_SIZE = 3
        cls.MICROSERVICE_PATH = "/rcube?"
        cls.MICROSERVICE_URL="127.0.0.1"
        cls.MICROSERVICE_PORT = 5000
#         cls.MICFROSERVICE_URL="umphrda-rcube.mybluemix.net"
#         cls.MICROSERVICE_PORT = 80
        
    def httpGetAndResponse(self, queryString):
        '''Make HTTP request to URL:PORT for /rcube?querystring; result is a JSON string'''
        try:
            theConnection = httplib.HTTPConnection(self.MICROSERVICE_URL, self.MICROSERVICE_PORT)
            theConnection.request("GET", self.MICROSERVICE_PATH + queryString)
            theStringResponse = theConnection.getresponse().read()
            return theStringResponse 
        except Exception as e:
            theStringResponse = "{'diagnostic': 'error: " + str(e) + "'}"
            return theStringResponse
        
    def string2dict(self, httpResponse):
        '''Convert JSON string to dictionary'''
        result = {}
        try:
            jsonString = httpResponse.replace("'", "\"")
            unicodeDictionary = json.loads(jsonString)
            for element in unicodeDictionary:
                if(isinstance(unicodeDictionary[element],unicode)):
                    result[str(element)] = str(unicodeDictionary[element])
                else:
                    result[str(element)] = unicodeDictionary[element]
        except Exception as e:
            result['diagnostic'] = str(e)
        return result
        
#Acceptance Tests
#
# 100 dispatch - basic functionality
# Desired level of confidence: boundary value analysis
# Analysis 
# inputs:     http:// ...myURL... /httpGetAndResponse?parm
#            parm is a string consisting of key-value pairs
#            At a minimum, parm must contain one key of "op"
#
# outputs:    A JSON string containing, at a minimum, a key of "status"
#
# Happy path 
#      input:   parm having at least one element with a key of "op"        
#      output:  JSON string containing a key of "status" 
#
# Sad path 
#      input:   no string       
#      output:  dictionary consisting of an element with a key of "status" and value of "error: missing op"
#
#      input:   valid parm string with at least one key-value pair, no key of "op"
#      output:  dictionary consisting of an element with a key of "status" and value of "error: missing op"
#
#
#
# Note:  These tests require an active web service
#
#
# Happy path assignment 4
    def test100_010_ShouldReturnSuccessKey(self):
        queryString="op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
    
    def test100_030_ShouldCreateDefaultCubeStatus(self):
        queryString="op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status',resultDict)
        self.assertEquals('created',resultDict['status'][0:7])

    def test100_040_ShouldCreateDefaultCubeKey(self):
        queryString="op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube',resultDict)

    def test100_050_ShouldCreateDefaultCubeValue(self):
        queryString="op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        expectedFaces = ['green','yellow','blue','white','red','orange']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEquals(face, actualResult[elementIndex])
                elementIndex += 1  
                
    def test100_060_SpecificExampleNoTwo(self):
        queryString="op=create&f=f&r=r&b=b&l=l&t=t&u=u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        expectedFaces = ['f', 'r', 'b', 'l', 't', 'u']
        elementIndex=0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEquals(face, actualResult[elementIndex])
                elementIndex += 1
    
    def test100_070_SpecificExampleNoThree(self):
        queryString="op=create&f=f&r=r&b=b&l=l&t=1"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        expectedFaces = ['f','r','b','l','1','orange']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEquals(face, actualResult[elementIndex])
                elementIndex += 1       
                
    def test100_080_SpecificExampleNoFour(self):
        queryString="op=create&f=f&r=r&b=b&l=l&t=1&under=42"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        expectedFaces = ['f','r','b','l','1','orange']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEquals(face, actualResult[elementIndex])
                elementIndex += 1
                
    #happy path assignment 5
    
    def test300_010_ShouldReturnStatusFull(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('full',resultDict['status'])
        
    def test300_020_ShouldReturnStatusCrosses(self):
        queryString = "op=check&f=w&r=g&b=r&l=b&t=r&u=o&cube=r,w,r,w,w,w,r,w,r, w,g,w,g,g,g,w,g,w,o,y,o,y,y,y,o,y,o, y,b,y,b,b,b,y,b,y, g,r,g,r,r,r,g,r,g, b,o,b,o,o,o,b,o,b"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('crosses',resultDict['status'])
    
    def test300_030_ShouldReturnStatusSpots(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=y,y,y,y,r,y,y,y,y, o,o,o,o,b,o,o,o,o,w,w,w,w,o,w,w,w,w,r,r,r,r,g,r,r,r,r,b,b,b,b,w,b,b,b,b, g,g,g,g,y,g,g,g,g"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('spots',resultDict['status'])
        
    def test300_040_ShouldReturnStatusUnknown(self):
        queryString = "op=check&f=2&r=o&b=g&l=r&t=b&u=y&cube=y,y,b,b,o,g,o,b,w, r,b,b,r,b,w,b,w,r,o,g,g,o,r,g,g,b,b,y,y,o,y,g,o,o,o,g,r,w,w,r,y,r,g,o,y, w,y,r,g,w,r,y,w,w"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertEquals('unknown',resultDict['status'])
        
    #happy path assignment 6
    
    def test300_050_ShouldRotateToF(self):
        queryString="op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b, o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=F"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        expectedFaces = ['g','r','b','o','w','y']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEquals(face, actualResult[elementIndex])
                elementIndex += 1
    
    def test300_060_ShouldRotateTof(self):
        queryString="op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b, o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        expectedFaces = ['g','r','b','o','w','y']
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEquals(face, actualResult[elementIndex])
                elementIndex += 1
                        
    #Sad path assignment 4
    
    def test100_900_ShouldReturnErrorOnEmptyParm(self):
        queryString=""
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])
    
    def test100_910_ShouldReturnErrorOnMissingOp(self):
        queryString="f=red"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])
        
    #sad path assignment 5
    
    def test100_920_ShouldReturnErrorOnMissingCube(self):
        queryString = "op=check"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])
        
    def test100_930_ShouldReturnErrorOnInvalidCubeSize(self):
        queryString = "op=check&f=2&r=o&b=g&l=r&t=b&u=y&cube=y,y,b,b,o,g,o,b,w,r"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])
        
    def test100_940_ShouldReturnErrorOnIllegalCube(self):
        queryString = "op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube=f,f,f,f,f,b,f,f,f,r,r,r,r,r,r,r,r,r,f,b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('illegal cube',resultDict['status'][0:6])
        
    #sad path assignment 6
    
    def test100_950_ShouldReturnErrorOnMissingCube(self):
        queryString = "op=rotate"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])
        
    def test100_960_ShouldReturnErrorOnMissingFace(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b, o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])
        
    def test100_960_ShouldReturnErrorOnUnknownFace(self):
        queryString = "op=rotate&f=g&r=r&b=b&l=o&t=w&u=y&cube=g,g,g,g,g,g,g,g,g,r,r,r,r,r,r,r,r,r,b,b,b,b,b,b,b,b,b,o,o,o,o,o,o,o,o,o,w,w,w,w,w,w,w,w,w,y,y,y,y,y,y,y,y,y&face=w"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])