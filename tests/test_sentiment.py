import unittest
import pandas as pd
from scripts.eda_analyzer import NewsEDA

class TestNewsEDA(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Sample mock data to simulate the CSV file
        cls.mock_data = pd.DataFrame({
            'headline': [
                "Stocks surge after strong earnings",
                "Market dips due to inflation fears",
                "Tech giants report record profits"
            ],
            'date': [
                "2023-01-01 08:00:00",
                "2023-01-02 10:30:00",
                "2023-01-03 14:15:00"
            ],
            'publisher': [
                "bloomberg",
                "reuters",
                "cnbc"
            ]
        })

        # Save to a temporary CSV
        cls.test_csv_path = "tests/temp_test_data.csv"
        cls.mock_data.to_csv(cls.test_csv_path, index=False)

    def setUp(self):
        self.eda = NewsEDA(self.test_csv_path)
        self.eda.preprocess()

    def test_headline_lengths_computed(self):
        self.assertIn('headline_length_words', self.eda.df.columns)
        self.assertIn('headline_length_chars', self.eda.df.columns)
        self.assertTrue((self.eda.df['headline_length_words'] > 0).all())

    def test_date_parsing(self):
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.eda.df['date']))
        self.assertIn('publish_day', self.eda.df.columns)
        self.assertIn('hour', self.eda.df.columns)

    def test_top_publishers_output(self):
        top_publishers = self.eda.df['publisher'].value_counts()
        self.assertEqual(top_publishers.index[0], 'bloomberg')

    @classmethod
    def tearDownClass(cls):
        import os
        os.remove(cls.test_csv_path)

if __name__ == '__main__':
    unittest.main()
