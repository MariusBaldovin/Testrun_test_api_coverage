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

### 2. Create and Activate a Virtual Environment (Linux)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create 'imported_files' folder

```bash
mkdir -p imported_files results
```        

### 5. Place testrun Postman collection (Testrun.postman_collection.json) in the 'imported_files' folder.

### 6. Place 'test_api.py' file in the 'imported_files' folder.

### 7. Make the create_table Script Executable

```bash
chmod +x generate_results
```

### 7. Add the PATH for your folder

```bash
export PATH=$PATH:/path/to/your/folder 
```

### 8. Running the Script

``` bash
 generate_results
```

### 8. The csv file and the pie chart will be created in the 'results' folder








