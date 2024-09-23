# Testrun API tests coverage

This project creates CSV Files and Pie Charts for API test coverage for Testrun project.

## Features

- Counts all the endpoints and responses from api.py 
- Counts all the enpoints and responses from postman file
- Counts the number of API tests from 'test_api.py' for each unique response code across all endpoints tested 
- Creates a CSV file with data from api.py versus data from postman file
- Creates a CSV file wit data from api.py versus data from test_api.py
- Creates a Pie Chart for postman coverage
- Creates a Pie Chart for test_api.py coverage

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

### 3. Run the setup script. You might be asked to restart the terminal or run 'source $BASH_CONFIG' in terminal.

```bash
./setup
```

### 4. Copy 'api.py' file in the 'imported_files' folder

### 5. Copy the Testrun postman collection in the 'imported_files' folder. The file must be named 'Testrun.postman_collection.json'

### 6. Copy 'test_api.py' file in the 'imported_files' folder

### 7. Running the Script

``` bash
 generate_results
```

### 8. The csv files and the pie charts will be created in the 'results' folder
