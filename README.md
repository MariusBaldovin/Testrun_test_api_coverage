# Testrun Postman to CSV Conversion Utility

This project provides a Python script to convert the Testrun Postman collection JSON file into CSV format. Additionally, it integrates with the test_api.py to calculate and visualise test coverage.

## Features
- Converts Postman JSON collections to CSV format.
- Counts the number of API tests from 'test_api.py' executed for each endpoint.
- Provides coverage statistics and generates a pie chart visualising the API testing status.

## Requirements

### Dependencies

The dependencies are listed in the `requirements.txt` file for easy installation.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/postman_to_csv.git
cd postman_to_csv
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

### 4. Create 'imported_files' and 'results' folders

```bash
mkdir -p imported_files results
```        

### 5. Place testrun Postman collection (Testrun.postman_collection.json) in the 'imported_files' folder.

### 6. Place 'test_api.py' file in the 'imported_files' folder.

### 7. Make the create_table Script Executable

```bash
chmod +x create_table
```

### 7. Add the PATH for your folder

```bash
export PATH=$PATH:/path/to/your/folder
```

### 8. Running the Script

``` bash
create_table
```

### 8. The csv file and the pie chart will be created in 'results' folder








