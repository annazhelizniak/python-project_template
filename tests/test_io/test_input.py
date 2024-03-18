from app.io.input import input_from_file, input_from_file_with_pandas
import unittest
import pandas as pd


class TestInput(unittest.TestCase):
    def test_input_from_file_exist(self):
        text = input_from_file("../../data/text_sample")
        self.assertIsInstance(text, str)
        self.assertTrue(len(text) > 0)

    def test_input_from_file_not_exist(self):
        text = input_from_file("data/not_existing_file.txt")
        self.assertIsNone(text)

    def test_input_from_file_builtin_empty(self):
        file_content = input_from_file("../../data/empty")
        self.assertEqual(file_content, "")

    def test_input_from_file_pandas_exist(self):
        df = input_from_file_with_pandas("../../data/csv_sample.csv")
        self.assertIsNotNone(df)
        self.assertEqual(df.shape, (4, 2))

    def test_input_from_file_pandas_not_exist(self):
        df = input_from_file_with_pandas("data/not_existing_file.csv")
        self.assertIsNone(df)

    def test_input_from_file_pandas_wrong_format(self):
        with self.assertRaises(pd.errors.ParserError):
            input_from_file_with_pandas("../../data/text_sample")
