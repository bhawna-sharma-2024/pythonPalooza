
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
 ├── data         # Store JSON files
 ├── fixture      # Define all the fixtures in this folder
 ├── pojo         # Contains classes that map JSON requests or responses to classes
 ├── utilities    # Contains utility methods
 ├── configuration # Add environment-specific configurations
 ├── conftest.py  
 └── testModules  # stores all the test files
```
# How to Run the Project
**To run the tests, execute the following command:**
<p><span style="background-color: black; color: white; font-weight: bold;">pytest -m DBTest --env-type=staging --alluredir=allure-results</span></p>

# How to View Allure Reports
**After running the tests, generate and view Allure reports using:**
<p style="background-color: black; "><span style="color: white; font-weight: bold;">allure serve allure-report</span></p>

![image](https://github.com/user-attachments/assets/57e45a2b-132c-45af-bb90-8fd2f26ffd4c)





 
   
