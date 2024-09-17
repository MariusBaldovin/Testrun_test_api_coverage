"""
Checks if Postman file exists and is a valid JSONReturns the JSON data if valid
"""

import os
import json

def load_postman(postman_file):
  """Loads the postman file"""

  # Check if the Postman file exists
  if not os.path.exists(postman_file):
    print(f"Error: The Postman file '{postman_file}' was not found.")
    print("Postman file must be placed in the 'imported_files' directory.")
    return None

  try:
    # Attempt to open and load the Postman file
    with open(postman_file, "r", encoding="utf-8") as file:
      return json.load(file)
  except FileNotFoundError:
    print(f"Error: The Postman file '{postman_file}' was not found.")
    return None
  except json.JSONDecodeError:
    print(f"Error: The Postman file '{postman_file}' is not a valid JSON file.")
    return None
