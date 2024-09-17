"""
Main module to create the API testing coverage csv table

"""
import sys
import os

# Add the parent directory to the sys.path to import 'src'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# pylint: disable=C0413
from src.convert_postman_to_csv import convert_postman_to_csv
from src.convert_postman_to_excel import convert_postman_to_excel

def main():
  """ Main function to run the script """

  # Path to the exported Postman JSON file
  postman_json_file = "imported_files/Testrun.postman_collection.json"

  # Path for test_api.py file
  test_file_path = 'imported_files/test_api.py'

  # Path to the output CSV file
  output_csv_file = "Api_testing_coverage.csv"

  # Path to the output Excel file
  output_excel_file = "Api_testing_coverage.xlsx"

  # Call the function to convert Postman JSON to CSV
  convert_postman_to_csv(postman_json_file, test_file_path, output_csv_file)

  # Call the function to convert Postman JSON to Excel
  convert_postman_to_excel(postman_json_file, test_file_path, output_excel_file)

if __name__ == "__main__":
  main()
