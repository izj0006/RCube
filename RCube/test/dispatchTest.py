import unittest
import httplib
import json
import RCube.dispatch as RCube

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
# Happy path
    def test100_010_ShouldReturnSuccessKey(self):
        queryString="op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
    
    def test100_020_ShouldReturnErrorOnEmptyParm(self):
        queryString=""
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])
    
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
        actualFaceIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[actualFaceIndex])
                actualFaceIndex += 1
                
    def test100_060_SpecificExampleNoTwo(self):
        queryString="op=create&f=f&r=r&b=b&l=l&t=t&u=u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        expectedFaces = ['f','r','b','l','t','u']
        actualFaceIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                
                actualFaceIndex += 1
    
    def test100_070_SpecificExampleNoThree(self):
        queryString="op=create&f=f&r=r&b=b&l=l&t=1"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        expectedFaces = ['f','r','b','l','t','u']
        actualFaceIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):

                actualFaceIndex += 1       
                
    def test100_080_SpecificExampleNoFour(self):
        queryString="op=create&f=f&r=r&b=b&l=l&t=1&under=42"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        actualResult = resultDict['cube']
        expectedFaces = ['f','r','b','l','t','u']
        actualFaceIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):        
                actualFaceIndex += 1         
    
    #Sad path
    
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

    