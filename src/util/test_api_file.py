"""
Loads the test_api.py file
Checks if test_api.py file exists in 'imported_files' directoy
"""

def load_test_api_file(test_api_file):
  """Loads the test_api.py file"""

  try:

    # Attempt to open and load the Postman file
    with open(test_api_file, "r", encoding="utf-8") as file:

      # Return a list with all lines from the file
      return file.readlines()

  # Error handling if test_api.py file is not found
  except FileNotFoundError:
    print("Error: The 'test_api.py' file was not found.")
    print("Info: 'test_api.py' must be placed in the 'imported_files' folder")
    return None
