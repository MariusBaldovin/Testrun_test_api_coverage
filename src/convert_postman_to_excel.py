"""
Module to handle the conversion of Postman JSON to Excel format
"""

import json
import os
import pandas as pd
from src import api_test_counter


def extract_endpoint_path(path_elements):
  """Joins the components of the 'path' key to create the endpoint"""

  # Combine path elements into a full API endpoint path
  endpoint = "/" + "/".join(path_elements)
  return endpoint

def calculate_percentages(test_count, unique_responses_count):
  """Calculates DONE and TO DO percentages based on test count and responses"""

  # Check if test_count is zero
  if test_count == 0:
    return "0.00 %", "100.00 %"

  # Calculate DONE percentage
  done_percentage = (test_count / unique_responses_count) * 100

  # Calculate TO DO percentage
  todo_percentage = 100 - done_percentage

  # return DONE and TO DO percentages as strings
  return f"{done_percentage:.2f} %", f"{todo_percentage:.2f} %"

def convert_postman_to_excel(postman_file, test_file_path, output_excel_file):
  """Utility method to convert Postman JSON to Excel"""

  # Load the Postman file
  with open(postman_file, "r", encoding="utf-8") as file:
    postman_data = json.load(file)

  # Parse the test file to get the endpoint counts
  endpoint_test_counts = api_test_counter.parse_test_api_file(test_file_path)

  # Empty list to be assigned with rows to be written in the Excel file
  rows = []

  # Iterate over all Postman file endpoints data
  for item in postman_data["item"]:

    # Assign the 'request' field
    request = item["request"]

    # Assign the 'path' field
    path = request["url"]["path"]

    # Extract the endpoint method and change to lowercase
    method = request["method"].lower()

    # Assign the 'response' field
    responses = item["response"]

    # Extract the endpoint path from 'path' field using 'extract_endpoint_path'
    endpoint_path = extract_endpoint_path(path)

    # Create a list of unique response codes
    unique_responses = {response['code'] for response in responses}

    # Combine each endpoint responses into a string (one response per line)
    combined_responses = "\n".join([response["name"] for response in responses])

    # Use the function from api_test_counter to get test count for this endpoint
    test_count = api_test_counter.get_test_count_for_endpoint(
                  endpoint_test_counts, endpoint_path, method)

    # Calculate DONE and TO DO percentages
    done_percentage, todo_percentage = calculate_percentages(
                           test_count, len(unique_responses))

    # Not tested endpoints
    not_tested = len(unique_responses) - test_count

    # Construct the dictionary which represents a row in the table
    row = {
      "ENDPOINT NAME": item["name"],
      "ENDPOINT PATH": endpoint_path,
      "METHOD": request["method"],
      "API RESPONSES": combined_responses,
      "NUMBER OF RESPONSES": len(unique_responses),
      "CURRENTLY TESTING": test_count,
      "NOT TESTED": not_tested,
      "DONE": done_percentage, 
      "TO DO": todo_percentage
    }

    # Append the row to the list
    rows.append(row)

  # Convert to a table (using pandas)
  df = pd.DataFrame(rows)

  # Ensure the 'results' folder exists, if not, create it
  if not os.path.exists("results"):
    os.makedirs("results")

  def apply_colour_format(worksheet, column_range, workbook):
    """ Applies colour format to columns with percentages """

    # Red colour format
    format_red = workbook.add_format({'bg_color': '#FFCCCC',
                                      'font_color': '#9C0006'})

    # Orange colour format
    format_orange = workbook.add_format({'bg_color': '#FFEB9C',
                                         'font_color': '#9C6500'})

    # Green colour format
    format_green = workbook.add_format({'bg_color': '#C6EFCE',
                                        'font_color': '#006100'})

    # Apply colour format for 100 %
    worksheet.conditional_format(column_range, {'type': 'text',
                                                'criteria': 'containing',
                                                'value': '100.00 %',
                                                'format': format_green})

    # Apply colour format for 0 %
    worksheet.conditional_format(column_range, {'type': 'text',
                                                'criteria': 'containing',
                                                'value': '0.00 %',
                                                'format': format_red})
    # Apply colour format for the rest
    worksheet.conditional_format(column_range, {'type': 'text',
                                                'criteria': 'containing',
                                                'value': '%',
                                                'format': format_orange})

  # Create an Excel writer with xlsxwriter engine
  output_excel_path = os.path.join("results", output_excel_file)
  with pd.ExcelWriter(output_excel_path, engine='xlsxwriter') as writer:
    # Write the DataFrame to an Excel sheet
    df.to_excel(writer, index=False, sheet_name='API Test Coverage')

    # Access the workbook and the worksheet
    workbook = writer.book
    worksheet = writer.sheets['API Test Coverage']

    # Apply conditional formatting to both the 'DONE' and 'TO DO' columns
    apply_colour_format(worksheet, 'H2:H1000', workbook)
    apply_colour_format(worksheet, 'I2:I1000', workbook)

  # Print a success message on terminal
  print(f"The Excel was successfully exported to results/{output_excel_file}")
