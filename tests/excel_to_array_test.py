import math
import unittest
from ecommercelib.userlib import arrayfromexcel as lib
from parameterized import parameterized


class Excel_To_Array_Testing(unittest.TestCase):

    def setUp(self):
        global start_row
        global end_row
        global col
        global file_path

    def test_gendata_not_zero(self):
        data = lib.gendata(start_row, end_row, col,
                           filepath=file_path,
                           sheetname="GDP")
        self.assertTrue(len(data) > 0)

    @parameterized.expand([
        ("negative", -1.5, -2.0),
        ("integer", 1, 1.0)
    ])
    def test_trainee_results(self, name,input, expected):
        self.assertEquals(math.floor(input), expected)

    def tearDown(self):
        pass


start_row = 7
end_row = 200
col = 5
file_path = "F:/Local disk/pythoninteljun2024/AdvancePythonTraining/resources/GDP.xlsx"
