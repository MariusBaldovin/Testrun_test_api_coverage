# Testrun api tests coverage

This project creates CSV File, Excel File, and Pie Chart for API test coverage for Testrun project.

## Features

- Counts all the enpoints and responses from postman file
- Counts the number of API tests from 'test_api.py' for each unique response code across all endpoints tested 
- Creates a CSV file
- Creates an Excel file
- Creates a Pie Chart for test coverage

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Testrun_test_api_coverage.git
cd Testrun_test_api_coverage
```
### 2. Run this command in terminal to make 'setup' script executable

```bash 
chmod +x ./setup
```

### 3. Run the setup script. You might be asked to restart the terminal or run 'source $BASH_CONFIG' in terminal

```bash
./setup
```

### 4. Copy the Testrun postman collection in the 'imported_files' folder. The file must be named 'Testrun.postman_collection.json'

### 5. Copy 'test_api.py' file in the 'imported_files' folder

### 6. Running the Script

``` bash
 generate_results
```

### 7. The csv file, excel file and the pie chart will be created in the 'results' folder
