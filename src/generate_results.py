"""
Main module to create:
- CSV file
- Excel file
- Pie Chart

"""

import os
import pandas as pd

from tables import csv_api_test_api
from tables import csv_api_postman
from charts import coverage_pie_chart

# Path for test_api.py file
TEST_API_FILE_PATH = "imported_files/test_api.py"

# Path for test_api.py file
API_FILE_PATH = "imported_files/api.py"

# Path to postman file
POSTMAN_FILE_PATH = "imported_files/Testrun.postman_collection.json"

RESULTS_DIR = "results"

def generate_results():
  """ Main function to create csv, excel files """

  # Name for api.py vs. postman csv file
  api_postman_filename = "api_vs_postman.csv"

  # Name for api.py vs. test_api.py csv file
  api_test_api_filename = "api_vs_test_api.csv"

  # Name for api vs. postman pie chart
  api_postman_chart = "api_vs_postman_chart.png"

  # Name for api.py vs. test_api.py chart
  api_test_api_chart = "api_vs_test_api.png"

  # Create api.py vs postman CSV file
  csv_api_postman.create_api_postman_csv(POSTMAN_FILE_PATH,
                                API_FILE_PATH, api_postman_filename)

  # Construct the full path for api.py vs. postman csv file
  api_postman_csv_path = os.path.join(RESULTS_DIR, api_postman_filename)

  # Check if the api.py vs. postman csv file exists
  if os.path.exists(api_postman_csv_path):

    # Read the api_vs_postman CSV file and convert it into a dictionary
    api_vs_postman_rows = pd.read_csv(os.path.join(RESULTS_DIR,
                                    api_postman_filename)).to_dict("records")

    # Create the api.py vs. postman pie chart
    coverage_pie_chart.plot_test_coverage(api_vs_postman_rows, api_postman_chart)

  else:

    # Print error messages
    print(f"Error: Pie chart '{api_postman_chart}' could not be created")
    print(f"Info: {api_postman_filename} must be in '{RESULTS_DIR}' folder")

  # Create the api.py vs test_api.py CSV file
  csv_api_test_api.create_api_test_api_csv(TEST_API_FILE_PATH, API_FILE_PATH,
                                           api_test_api_filename)

  # Construct the full path for api.py vs. test_api.py csv file
  api_test_api_csv_path = os.path.join(RESULTS_DIR, api_test_api_filename)

  # Check if the api.py vs. test_api.py csv file exists
  if os.path.exists(api_test_api_csv_path):

    # Read the api_vs_test_api CSV file and convert it into a dictionary
    api_vs_test_api_rows = pd.read_csv(os.path.join(RESULTS_DIR,
                                    api_test_api_filename)).to_dict("records")

    # Create the api.py vs. test_api.py pie chart
    coverage_pie_chart.plot_test_coverage(api_vs_test_api_rows, api_test_api_chart)

  else:

    # Print error messages
    print(f"Error: Pie chart '{api_test_api_chart}' could not be created")
    print(f"Info: {api_test_api_filename} must be in '{RESULTS_DIR}' folder")

if __name__ == "__main__":
  generate_results()
