"""
Module to create CSV file
"""

import os
import pandas as pd
from counter import test_api_counter
from util import postman

def extract_endpoint_path(path_elements):
  """ Joins the components of the 'path' key to create the endpoint """
  endpoint = "/" + "/".join(path_elements)
  # print(f"Extracted endpoint path from Postman: {endpoint}")
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

def create_csv(postman_file, test_file_path, csv_filename):
  """ Create the CSV file """

  # Load the Postman file
  postman_data = postman.load_postman(postman_file)

  # Error handling if postman file is not available
  if not postman_data:
    return

  # Parse the test file to get the endpoint counts
  endpoint_test_counts = test_api_counter.parse_test_api_file(test_file_path)

  # Stop execution if the test file couldn't be processed
  if endpoint_test_counts is None:
    print(f"Error: Failed to create the CSV file '{csv_filename}'")
    return

  # Empty list to be assigned with rows to be written in the csv
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
    endpoint = extract_endpoint_path(path)

    # Create a set of unique response codes
    unique_responses = {response["code"] for response in responses}

    # Combine each endpoint responses into a string (one response per line)
    combined_responses = "\n".join(
      [response["name"] for response in responses]
    )

    # Use the function from api_test_counter to get test count for this endpoint
    test_count = test_api_counter.get_test_count_for_endpoint(
                                    endpoint_test_counts,
                                    endpoint,
                                    method)

    # Calculate DONE and TO DO percentages
    done_percentage, todo_percentage = calculate_percentages(
                           test_count, len(unique_responses))

    # Not tested endpoints
    not_tested = len(unique_responses) - test_count

    # Construct the dictionary which represents a row in the table
    row = {
      "ENDPOINT NAME": item["name"],
      "ENDPOINT PATH": endpoint,
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

  # Convert rows to a table
  df = pd.DataFrame(rows)

  # Ensure the 'results' folder exists, if not, create it
  if not os.path.exists("results"):
    os.makedirs("results")

  # Save the DataFrame to CSV inside the 'results' folder
  df.to_csv(os.path.join("results", csv_filename), index=False)
  print(f"The CSV file was successfully exported to 'results/{csv_filename}'")
