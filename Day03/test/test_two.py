import unittest
import os

from partTwo import part_two, parse_input, mul

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        base_path = os.path.dirname(__file__)
        with open(os.path.join(base_path, 'input_sample_two.txt'), 'r') as file:
            self.input_sample_two = file.read()
  
    def test_parse_input(self):
        result = parse_input(self.input_sample_two)
        self.assertEqual(result, [['mul(2,4)',
                                   "don't()",
                                   'mul(5,5)',
                                   'mul(11,8)',
                                   'do()',
                                   'mul(8,5)']])
        
    def test_mul(self):
        result = mul(['mul(2,4)',
                      'mul(5,5)',
                      'mul(11,8)',
                      'mul(8,5)'])
        self.assertEqual(result, 161)
    
    def test_mul_2(self):
        result = mul(['mul(2,4)',
                      "don't()",
                      'mul(5,5)',
                      'mul(11,8)',
                      'do()',
                      'mul(8,5)'])
        self.assertEqual(result, 48)

    def test_mul_3(self):
        result = mul(["don't()",
                      'mul(5,5)'])
        self.assertEqual(result, 0)
        
    def test_mul_4(self):
        result = mul(["do()",
                      'mul(5,5)'])
        self.assertEqual(result, 25)

    def test_mul_5(self):
        result = mul(['do()'])
        self.assertEqual(result, 0)
        

    def test_mul_6(self):
        result = mul(["don't()"])
        self.assertEqual(result, 0)
        
    
    def test_mul_7(self):
        result = mul(['mul(2,4)',
                      "don't()",
                      'mul(5,5)',
                      'mul(11,8)',
                      'do()',
                      'mul(8,5)'])
        self.assertEqual(result, 48)
        
            
    def test_part_two(self):
        result = part_two(self.input_sample_two)
        self.assertEqual(result, 48)

if __name__ == '__main__':
    unittest.main()