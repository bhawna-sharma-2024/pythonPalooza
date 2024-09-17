
# pythonPalooza

**The Python code repository**

This is a sample Python project that touches upon all the concepts used in Python:

- Fixtures
- Data handling
- POJOs
- Adding command line parameters
- Marking tests and dividing into groups
- Decorators

## Project Structure

```bash
test
 ├── data         # Store JSON files, also has config file to read values depending upon the test environment
 ├── fixture      # Define all the fixtures in this folder
 ├── pojo         # Contains classes that map JSON requests or responses to classes
 ├── utilities    # Contains utility methods
 ├── configuration # Add environment-specific configurations
 ├── conftest.py  
 └── testclasses

# How to Run the Project
## To run the tests, execute the following command:
pytest -m DBTest --env-type=staging --alluredir=allure-results

# How to View Allure Reports
## After running the tests, generate and view Allure reports using:
allure serve allure-report


 
   
