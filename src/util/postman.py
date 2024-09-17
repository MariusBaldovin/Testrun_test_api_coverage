"""
Checks if Postman file exists and is a valid JSONReturns the JSON data if valid
"""

import json

def load_postman(postman_file):
  """Loads the postman file"""

  try:

    # Attempt to open and load the Postman file
    with open(postman_file, "r", encoding="utf-8") as file:

      # Return the postman file
      return json.load(file)

  # Error handling if postman file is not found
  except FileNotFoundError:
    print(f"Error: The Postman file '{postman_file}' was not found.")
    print("Postman file must be placed in the 'imported_files' directory.")
    return None

  # Error handling if postman file is not valid json
  except json.JSONDecodeError:
    print(f"Error: The Postman file '{postman_file}' is not a valid JSON file.")
    return None
