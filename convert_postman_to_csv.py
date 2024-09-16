"""
This module handles the conversion of Postman JSON to CSV format
"""

import json
import os
import pandas as pd
import api_test_counter
import charts

def extract_endpoint_path(path_elements):
  """ Joins the components of the 'path' key to create the endpoint """
  endpoint = "/" + "/".join(path_elements)
  # print(f"Extracted endpoint path from Postman: {endpoint}")
  return endpoint

def convert_postman_to_csv(postman_json_file, test_file_path, output_csv_file):
  """ Utility method to convert Postman JSON to CSV"""

  # Load the Postman file
  with open(postman_json_file, "r", encoding="utf-8") as file:
    postman_data = json.load(file)

  # Parse the test file to get the endpoint test counts api_test_counter
  endpoint_test_counts = api_test_counter.parse_test_api_file(test_file_path)

  # Empty list to be assigned with rows to be written in the csv
  rows = []

  # Iterate over all the endpoints data
  for item in postman_data["item"]:

    # Assign the 'request' field
    request = item["request"]

    # Assign the 'path' field
    path = request["url"]["path"]

    # Extract the endpoint method
    method = request["method"]

    # Assign the 'response' field
    responses = item["response"]

    # Extract the endpoint path from 'path' field using 'extract_endpoint_path'
    endpoint_path = extract_endpoint_path(path)

    # Create a list of unique response codes
    unique_responses = {response['code'] for response in responses}

    # Combine each endpoint responses into a string (one response per line)
    combined_responses = "\n".join(
      [response["name"] for response in responses]
    )

    # Use the function from api_test_counter to get test count for this endpoint
    test_count = api_test_counter.get_test_count_for_endpoint(
                  endpoint_test_counts, endpoint_path, method)

    # Check if test_count is zero
    if test_count == 0:
      done_percentage = 0
      todo_percentage = 100
    else:
      done_percentage = (test_count / len(unique_responses)) * 100
      todo_percentage = 100 - done_percentage

    # Format percentages to two decimal places
    done_percentage = f"{done_percentage:.2f} %"
    todo_percentage = f"{todo_percentage:.2f} %"

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
      # "DESCRIPTION": request["description"]
    }

    # Append the row to the list
    rows.append(row)

  # Convert to DataFrame
  df = pd.DataFrame(rows)

  # Ensure the 'results' folder exists, if not, create it
  if not os.path.exists("results"):
    os.makedirs("results")

  # Save the DataFrame to CSV inside the 'results' folder
  df.to_csv(os.path.join("results", output_csv_file), index=False)
  print(f"The CSV file was successfully exported to results/{output_csv_file}")

  # Plotting a pie graph showing done and to do
  charts.plot_test_coverage(rows, "results")

def main():
  """ Main function to run the script """

  # Path to the exported Postman JSON file
  postman_json_file = "imported_files/Testrun.postman_collection.json"

  # Path for test_api.py file
  test_file_path = 'imported_files/test_api.py'

  # Path to the output CSV file
  output_csv_file = "Api_testing_coverage.csv"

  # Call the function to convert Postman JSON to CSV
  convert_postman_to_csv(postman_json_file, test_file_path, output_csv_file)

# Run the script when executed
if __name__ == "__main__":
  main()
