# Environment setup
### Automation Testing Framework
Framework to run data-related tests on Database MS SQL SERVER.
Tests are based on pytest framework.There are basic SQL-based tests.

## Name and description of project
Project pythonPytest contains determined automated test cases
of 3 tables - Jobs,Employees,Locations that have specific tag-name to link to Jira issues.

## Test cases creation and management
Tests should be atomic, independent, reasonable and self-described.

## Create virtual environment for tests execution
```bash
pip install -r requirements.txt
```
## Deploy and configure Data Quality solution
Follow [instructions](../README.md)

## Project location
The project can be found in repository:

git clone: https://git.epam.com/natallia_semianiuk/pytest.git## Run tests
```bash
pytest Home_pytest.py  
pytest Home_pytest.py  --html=MyHTMLReport.html

```
# Report portal 
There are HTML outputs of test that are run. It's going to tell it to copy it into an object store, 
just it's accessible to everybody to monitoring about the quality of the database.
All the results after execution following commands can be found in root of the project with names: 
MyHTMLReport.html with all received information.