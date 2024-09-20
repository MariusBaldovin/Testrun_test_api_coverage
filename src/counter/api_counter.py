""" 
Module to parse api.py to extract each endpoint, methods and 
unique response codes for each (endpoint, method)

"""

import re
from util import load_api_file

def parse_api_file(file_path):
  """Extract endpoints and methods from api.py lines"""

  # Match the 'add_api_route' function calls
  route_pattern = re.compile(
    r'self\._router\.add_api_route\("([^"]+)",\s*self\.(\w+)' +
    r"(?:,\s*methods=\[(.*?)\])?\)")

  # Load the 'apy.py' lines
  api_lines = load_api_file.load_api_file(file_path)

  # Error handling if api.py file is not available
  if not api_lines:
    return

  # Dictionary to store methods and the function for each endpoint
  endpoint_method_function = {}

  # Variable to hold multiple lines
  complete_api_line = ""

  # Iterate over all api.py lines
  for api_line in api_lines:

    # Remove leading and trailing spaces
    api_line = api_line.strip()

    if api_line:

      # Append the line to complete_api_line, adding a space if it's not empty
      complete_api_line += " " + api_line if complete_api_line else api_line

      # Check if the line ends with ')'
      if complete_api_line.endswith(")"):

        # Match the pattern
        route_match = route_pattern.search(complete_api_line)

        # If found a match
        if route_match:

          # Extract endpoint, function name, and methods
          endpoint, function, methods = route_match.groups()

          # Assign the method to 'GET' if not specified
          methods = methods or "GET"

          # Clean up and split methods
          methods_list = [
            method.strip().strip('"').lower()
            for method in methods.split(",")
          ]

          # Iterate over each method in the list of methods
          for method in methods_list:

            # Check if the endpoint exists in the dictionary
            if endpoint not in endpoint_method_function:
              # If not, initialize an empty dict for this endpoint
              endpoint_method_function[endpoint] = {}

            # Check if the method exists for this endpoint
            if method not in endpoint_method_function[endpoint]:
              # If not, initialize an empty set for this method
              endpoint_method_function[endpoint][method] = set()

            # Add the function name to the set for this method
            endpoint_method_function[endpoint][method].add(function)

        # Reset complete_api_line
        complete_api_line = ""

    # Check if there are any endpoints and methods extracted
    functions = []
    for endpoint, methods in endpoint_method_function.items():
      for method, funcs in methods.items():
        for func in funcs:
          functions.append(func)
  print(functions)

  return endpoint_method_function


