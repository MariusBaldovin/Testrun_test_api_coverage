"""
Main module to create:
- CSV file
- Excel file
- Pie Chart

"""

import os
import pandas as pd

# pylint: disable=C0413
from tables.create_csv import create_csv
from tables.create_excel import create_excel
from charts import test_coverage

# Path for test_api.py file
TEST_FILE_PATH = "imported_files/test_api.py"

# Path to postman file
POSTMAN_FILE_PATH = "imported_files/Testrun.postman_collection.json"

RESULTS_DIR = "results"

def generate_results():
  """ Main function to create csv, excel files """

  # Name for the created CSV file
  csv_filename = "Api_testing_coverage.csv"

  # Name for the created excel file
  excel_filename = "Api_testing_coverage.xlsx"

  # Name for the created pie chart
  chart_filename = "test_coverage_chart.png"

  # Create the CSV file
  create_csv(POSTMAN_FILE_PATH, TEST_FILE_PATH, csv_filename)

  # Create the excel file
  create_excel(POSTMAN_FILE_PATH, TEST_FILE_PATH, excel_filename)

  # Construct the full path for csv file
  csv_path = os.path.join(RESULTS_DIR, csv_filename)

  # Check if the csv file exists
  if os.path.exists(csv_path):

    # Read the generated CSV file and convert it into a dictionary
    rows = pd.read_csv(os.path.join(RESULTS_DIR,
                                    csv_filename)).to_dict("records")

    # Create the pie chart
    test_coverage.plot_test_coverage(rows, chart_filename)

  else:

    # Print error messages
    print(f"Error: Pie chart '{chart_filename}' could not be created")
    print(f"Info: {csv_filename} must be in '{RESULTS_DIR}' folder")

if __name__ == "__main__":
  generate_results()
