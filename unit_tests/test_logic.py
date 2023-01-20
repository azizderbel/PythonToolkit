import unittest
import logic

class TestLogic(unittest.TestCase):

    def test_add(self):
        self.assertEqual(logic.add(10,5),15)
        self.assertEqual(logic.add(10,4),14)



if __name__ == "__main__":
    unittest.main()
