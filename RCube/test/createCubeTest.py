import unittest
import RCube.dispatch as RCube

class createCubeTest(unittest.TestCase):
    def test100_610_ShouldCreateOneElementCube(self):
        parm = {'op' : 'create'}
        expectedResult = ['green']
        actualResult = RCube.createCube(parm)
        self.assertListEqual(expectedResult, actualResult)