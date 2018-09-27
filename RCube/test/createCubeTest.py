import unittest
import RCube.dispatch as RCube

class createCubeTest(unittest.TestCase):

    # def test100_610_ShouldCreateOneElementCube(self):
    #     parm = {'op' : 'create'}
    #     expectedResult = ['green']
    #     actualResult = RCube.createCube(parm)
    #     self.assertListEqual(expectedResult, actualResult)
    
    # def test100_620_ShouldCreateMultipleElementCube(self):
    #     parm = {'op' : 'create'}
    #     expectedResult = 'green'
    #     actualResult = RCube.createCube(parm)
    #     for elementIndex in range(0,9):
    #         self.assertEqual(expectedResult, actualResult[elementIndex])

    def test100_630_ShouldCreateMultipleFaceCube(self):
        parm={'op':'create','f':'f','r':'r','b':'b','l':'l','t':'t','u':'u'}
        expectedFaces = ['green', 'yellow', 'blue', 'white', 'red', 'orange']
        actualResult= RCube.createCube(parm)
        elementIndex=0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                print(actualResult[elementIndex])
                elementIndex += 1