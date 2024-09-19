# Testrun test_apy.py coverage

This project creates CSV file, Excel file and Pie Chart for test_api.py from Testrun project.

## Features

- Counts the number of API tests from 'test_api.py' for each unique response code across all endpoints tested .
- Creates a CSV file
- Creates an Excel file
- Creates a Pie Chart for test coverage


## Requirements

### Dependencies

The dependencies are listed in the `requirements.txt` file for easy installation.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Testrun_test_api_coverage.git
cd Testrun_test_api_coverage
```
### 2. Run this command in terminal to make setup executable

```bash 
chmod +x ./setup
```

### 3. Run the setup script and add the command line from the terminal or restart the terminal

```bash
./setup
```

### 4. Place testrun Postman collection (Testrun.postman_collection.json) in the 'imported_files' folder.

### 5. Place 'test_api.py' file in the 'imported_files' folder.

### 6. Running the Script

``` bash
 generate_results
```

### 7. The csv file, excel file and the pie chart will be created in the 'results' folder
