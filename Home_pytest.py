import pyodbc
import pytest

try:
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};Server=EPPLWARW01A1\\SQLEXPRESS;Database=TRN;username= testuser;password=test')
    print("There is connection to DB")
except Exception as ex:
    print(ex)

def test01():
    """
    test_1: [Locations] completeness
    Find out if table Locations exists
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("Select top 1 location_id from hr.locations")
    rows = cursor.fetchall()
    assert len(rows)==1
    print(f'Table Locations exists')

def test02():
    """
    test_2: [Locations] completeness
    Find out if table Locations is not empty
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("Select count(*) from hr.locations")
    rows = cursor.fetchall()
    assert len(list(rows)) > 0
    print(f'Table Locations is not empty')

def test03():
    """
    test_3: [Locations] uniqueness
    Find out if the quantity of expecting result is the same as in query
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("select count(*) from hr.locations where city='London'")
    rows = cursor.fetchall()[0][0]
    assert  rows == 1
    print(f'London exists in the table hr.locations without duplicates')

def test04():
    """
    test_4: [Jobs] completeness
    Find out about the existence of following position - President
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("select count(job_id) from hr.jobs where job_title='President'")
    rows = cursor.fetchall()[0][0]
    assert rows==1
    print(f'President exists in the table')

def test05():
    """
    test_5: [Jobs] completeness
    Find out if duplicate rows exist
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("select employee_id, job_id, manager_id, department_id, count(*) from hr.employees group by employee_id, job_id, manager_id, department_id having count(*)>1")
    rows = cursor.fetchall()
    assert len(list(rows)) == 0
    print(f'There are no duplicates in hr.employees table')

def test06():
    """
    test_06: [Employees] validity
    Be sure that average salary of employees - 8060
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("SELECT avg(salary) as average_salary FROM hr.employees")
    rows = cursor.fetchall()[0][0]
    assert  rows == 8060
    print(f'The average salary is as in expected result')

def test07():
    """
    test_07: [Employees] validity
    Find that min_salary of all employees not more 2500
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("select min(salary) as min_salary from hr.employees")
    rows = cursor.fetchall()[0][0]
    assert rows <= 2500
    print(f'There is min salary is 2500')


def test08():
    """
    test_8: [Employees] additional verification
    Check the quantity of Employees whose name John
    result: pass
    """
    cursor = connection.cursor()
    cursor.execute("select count(*) from hr.employees where first_name='John'")
    rows = cursor.fetchall()[0][0]
    assert rows == 2
    print(f'The quantity of Employees, whose name is John, is 2')


