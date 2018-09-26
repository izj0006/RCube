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
        parm={'op':'create'}
        expectedFaces = ['green', 'yellow', 'blue', 'white', 'red', 'orange']
        actualResult= RCube.createCube(parm)
        elementIndex=0
        for face in expectedFaces:
            for i in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1