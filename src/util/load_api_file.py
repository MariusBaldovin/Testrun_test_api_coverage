"""
Loads the api.py file
Checks if api.py file exists in 'imported_files' directoy
"""

def load_api_file(api_file):
  """Loads and return the lines from the api.py file"""

  try:

    # Attempt to open and load the api.py file
    with open(api_file, "r", encoding="utf-8") as file:

      # Return a list with all lines from the file
      return file.readlines()

  # Error handling if api.py file is not found
  except FileNotFoundError:
    print("Error: The 'api.py' file was not found")
    print("Info: 'api.py' must be placed in the 'imported_files' folder")
    return None
  