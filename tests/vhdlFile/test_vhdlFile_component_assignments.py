
import unittest
from modules import vhdlFile

class testVhdlFileComponentAssignments(unittest.TestCase):


    def test_isComponent_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_component/component_test_input.vhd')
        lExpected = [5,16,27,36,45,56,66]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insideComponent_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_component/component_test_input.vhd')
        lExpected = [5,6,7,8,9,10,11,12,16,17,18,19,20,21,22,23,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insideComponent:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isComponentEnd_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_component/component_test_input.vhd')
        lExpected = [12,23,34,43,52,65,75]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_insidePortMap_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_component/component_test_input.vhd')
        lExpected = [6,7,8,9,10,11,17,18,19,20,21,22,28,29,30,31,32,33,37,38,39,40,41,42,46,47,48,49,50,51,58,59,60,61,62,63,67,68,69,70,71,72,73,74]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.insidePortMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPortKeyword_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_component/component_test_input.vhd')
        lExpected = [6,17,28,37,46,58,67]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isEndPortMap_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_component/component_test_input.vhd')
        lExpected = [11,22,33,42,51,63,74]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isEndPortMap:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_isPortDeclaration_assignment(self):
        oFile = vhdlFile.vhdlFile('tests/rule_component/component_test_input.vhd')
        lExpected = [7,8,9,10,18,19,20,21,29,30,31,32,38,39,40,41,47,48,49,50,59,60,61,62,69,70,71,72]
        # Generic actual list
        lActual = []
        for iIndex, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                lActual.append(iIndex)
        # Compare
        self.assertEqual(lActual, lExpected)

    def test_componentIndent_assignment(self):
        self.maxDiff = None
        oFile = vhdlFile.vhdlFile('tests/rule_component/component_test_input.vhd')
#       lExpected = [   0,   1,2,   3,4,5,6,7,8,9,10,11,12,  13]
        lExpected = [None,None,0,None,1,1,2,3,3,3, 3, 2, 1,None]
        # Generic actual list
        lActual = []
        iMaxCheck = len(lExpected)
        for iIndex, oLine in enumerate(oFile.lines):
            if iIndex == iMaxCheck:
                break
            lActual.append(oLine.indentLevel)
        # Compare
        self.assertEqual(lActual, lExpected)


if __name__ == '__main__':
    unittest.main()
