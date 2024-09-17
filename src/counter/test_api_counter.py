"""
This module parses 'test_api.py' to count unique API responses for each endpoint
Skipped tests are excluded from the count

"""

import re
from collections import defaultdict

# Parse the test file to count each endpoint unique status codes
def parse_test_api_file(file_path):
  """ Dictionary to store endpoints and their response code counts """

  # Initialize a set to store counts for each unique endpoint and status code
  endpoint_counts = defaultdict(set)

  # Pattern to match API requests even when split across 2 lines
  api_call_pattern = re.compile(r'requests\.(get|post|put|delete)\(f?"([^"]+)"')

  # Pattern to match status code assertions
  status_code_pattern = re.compile(r'assert r\.status_code == (\d{3})')

  # Pattern to match the skipped tests
  skip_pattern = re.compile(r'@pytest\.mark\.skip|pytest\.skip\(')

  # Pattern to detect the start of a new test
  test_pattern = re.compile(r'def test_\w+\(')

  # Variable to keep track of the current endpoint being processed
  current_endpoint = None

  # Track if the current test is skipped
  skip_test = False

  # Track when the first request is found in the test
  found_first_request = False

  # Track when the status code is checked
  checked_status_code = False

  # Open the test_api.py for reading
  with open(file_path, 'r', encoding='utf-8') as file:

    # Read all lines from the file into a list
    lines = file.readlines()

    # Iterate over each line in the file
    for i, line in enumerate(lines):

      # Strip leading and trailing whitespaces
      line = line.strip()

      # Check if the line ends with an open parenthesis
      if line.endswith('(') and i + 1 < len(lines):
        # Concatenate with the next line
        line += lines[i + 1].strip()

      # Check if the line is the start of a new test
      if test_pattern.search(line):
      # Reset the flags to false for a new test
        skip_test = False
        found_first_request = False
        checked_status_code = False


      # Check if the test is marked as skipped
      if skip_pattern.search(line):
        # Change the skip_test to true
        skip_test = True
        # Skip the line
        continue

      # If the test is skipped
      if skip_test:
        # Skip all the lines on the test
        continue

      # Try to find an API request in the current line
      if not found_first_request:

        # Try to find an API request in the current line
        api_match = api_call_pattern.search(line)

        if api_match:
          # Capture the method and the endpoint from the matched API request
          method, endpoint = api_match.groups()
          # Remove the {API} placeholder, trailing '/' and change to lowercase
          endpoint = endpoint.replace("{API}", "").lower().rstrip("/")
          # Store method and endpoint
          current_endpoint = (method, endpoint)
          # Set found_first_request to true for next requests not be counted
          found_first_request = True

      # Find the status code check line
      if found_first_request and not checked_status_code:
        # Try to find a status code assertion in the current line
        status_code_match = status_code_pattern.search(line)

        if status_code_match and current_endpoint:
          # Capture the status code from the assertion
          status_code = status_code_match.group(1)
          # Add the status code to the set for this endpoint
          endpoint_counts[current_endpoint].add(status_code)
          # Set the checked_status_code to true to skip next lines
          checked_status_code = True

      # If the status code has been processed
      if checked_status_code:
        # Skip the rest of the test lines
        continue

  # Return dictionary with unique endpoint/status code combinations
  return {key: len(value) for key, value in endpoint_counts.items()}

def get_test_count_for_endpoint(endpoint_counts, endpoint, method):
  """ Get the method and number of endpoints  """

  # Return the count for the given method and endpoint
  result = endpoint_counts.get((method, endpoint), 0)

  # print(f"Test count for {method.upper()} {endpoint}: {result}")
  return result
