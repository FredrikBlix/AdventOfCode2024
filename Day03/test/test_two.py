import unittest
import os

from partTwo import part_two, parse_input, mul

class TestMainFunctions(unittest.TestCase):

    def setUp(self):
        base_path = os.path.dirname(__file__)
        with open(os.path.join(base_path, 'input_sample_one.txt'), 'r') as file:
            self.input_sample_one = file.read()
        with open(os.path.join(base_path, 'input_sample_two.txt'), 'r') as file:
            self.input_sample_two = file.read()
        with open(os.path.join(base_path, 'row0.txt'), 'r') as file:
            self.row0 = file.read()
        with open(os.path.join(base_path, 'row1.txt'), 'r') as file:
            self.row1 = file.read()
        with open(os.path.join(base_path, 'row2.txt'), 'r') as file:
            self.row2 = file.read()
        with open(os.path.join(base_path, 'row3.txt'), 'r') as file:
            self.row3 = file.read()
        with open(os.path.join(base_path, 'row4.txt'), 'r') as file:
            self.row4 = file.read()
        with open(os.path.join(base_path, 'row5.txt'), 'r') as file:
            self.row5 = file.read()
  
    def test_parse_input(self):
        result = parse_input(self.input_sample_one)
        self.assertEqual(result, [['mul(2,4)',
                                   'mul(5,5)',
                                   'mul(11,8)',
                                   'mul(8,5)']])
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
        
    def test_mul_8(self):
        result = mul(['mul(2,4)',
                      "don't()",
                      "don't()",
                      "don't()",
                      "don't()",
                      'mul(5,5)',
                      'mul(11,8)',
                      'do()',
                      'mul(8,5)'])
        self.assertEqual(result, 48)

    def test_mul_9(self):
        result = mul(['mul(2,4)',
                      "don't()",
                      'mul(5,5)',
                      'mul(11,8)',
                      'mul(5,5)',
                      'mul(11,8)',
                      "don't()",
                      'mul(5,5)',
                      'mul(11,8)',
                      "don't()",
                      'mul(5,5)',
                      'mul(11,8)',
                      "don't()",
                      'mul(5,5)',
                      'mul(11,8)',
                      'mul(5,5)',
                      'mul(11,8)',
                      "don't()",
                      "don't()",
                      "don't()",
                      'do()',
                      'mul(8,5)'])
        self.assertEqual(result, 48)
            
    def test_part_two(self):
        result = part_two(self.input_sample_one)
        self.assertEqual(result, 161)
        result = part_two(self.input_sample_two)
        self.assertEqual(result, 48)
        
    def test_row0(self):
        result = part_two(self.row0)
        self.assertEqual(result, 33516115)

    def test_row1(self):
        result = part_two(self.row1)
        self.assertEqual(result, 30393460)

    def test_row2(self):
        result = part_two(self.row2)
        self.assertEqual(result, 28656543)

    def test_row3(self):
        result = part_two(self.row3)
        self.assertEqual(result, 33439870)

    def test_row4(self):
        result = part_two(self.row4)
        self.assertEqual(result, 30788967)

    def test_row5(self):
        result = part_two(self.row5)
        self.assertEqual(result, 26874088)

if __name__ == '__main__':
    unittest.main()