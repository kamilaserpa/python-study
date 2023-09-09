import unittest
import StudyPythonFunctions

class TestStudyPythonFunctions(unittest.TestCase): # herança
    def test_soma(self):
        result = StudyPythonFunctions.soma(25,6)
        self.assertEqual(result, 31)

    def test_multiplicacao(self):
        result = StudyPythonFunctions.multiplicacao(3,4)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()