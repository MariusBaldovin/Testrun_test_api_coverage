"""
Main module to create:
- CSV file
- Excel file
- Pie Chart

"""

import os
import pandas as pd

# pylint: disable=C0413
from src.create_csv import create_csv
from src.create_excel import create_excel
from src.charts.testing_coverage import plot_test_coverage # pylint: disable=E0611

# Path for test_api.py file
TEST_FILE_PATH = 'imported_files/test_api.py'

# Path to the exported Postman JSON file
POSTMAN_FILE_PATH = "imported_files/Testrun.postman_collection.json"

def generate_results():
  """ Main function to create csv, excel files """

  # Name for the created CSV file
  csv_filename = "Api_testing_coverage.csv"

  # Name for the created excel file
  excel_filename = "Api_testing_coverage.xlsx"

  # Create the CSV file
  create_csv(POSTMAN_FILE_PATH, TEST_FILE_PATH, csv_filename)

  # Create the excel file
  create_excel(POSTMAN_FILE_PATH, TEST_FILE_PATH, excel_filename)

  # Read the generated CSV file and convert it into a dictionary
  rows = pd.read_csv(os.path.join("results", csv_filename)).to_dict('records')

  # Create the pie chart
  plot_test_coverage(rows, "results")

if __name__ == "__main__":
  generate_results()
