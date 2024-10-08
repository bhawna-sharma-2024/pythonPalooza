import pytest
import os
import json
import requests
import allure
from pojo.user import *
from faker import Faker
from utilities.logging_decorator import log_function_call

userId=None

def getJsonData(filename):
    file_path = os.path.join("tests/data/",filename)
    print(f"the file path is :{file_path}")
    with open(file_path, "r") as f:
        json_file = json.load(f)
    return json_file

@allure.title("Test adding user")
@allure.description("This test attempts to add user in system ")
@allure.tag("Sanity", "Essentials")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Bhawna Sharma")
@allure.testcase("TMS-142")
@pytest.mark.parametrize("jsonData",getJsonData("createUserData.json"))
@pytest.mark.dependency
@log_function_call
@pytest.mark.DBTest
def test_creatinguser(jsonData,readConfig,logging_fixture,getConnection):
    logger = logging_fixture
    logger.info(f"Starting test with input_data: {jsonData}")
    response=requests.post(readConfig.get("baseurl")+"/createuser/",data=jsonData)
    response_json = response.json()
    print(f"The response message is: {response.json()}")
    assert response.status_code==201
    assert "User has been created successfully" in response_json["message"]
    assert "userid" in response_json and response_json["userid"] is not None

    #verifying response against DB and checking if row gets created in DB
    cursor=getConnection.cursor()
    print(f"SELECT * FROM expense_tracker.budget_user where email like '%{jsonData['email']}%'")
    cursor.execute(f"SELECT * FROM expense_tracker.budget_user where email like '%{jsonData['email']}%'")
    results=cursor.fetchone()
    print(f"The results are {results}")
    assert len(results) >= 1, f"Expected db row creation for {jsonData.email} "
    if not jsonData['firstname'] in results:
        assert False,f"Expected {jsonData['firstname']} in DB results"
    if not jsonData['lastname'] in results:
        assert False,f"Expected {jsonData['lastname']} in DB results"
    if not jsonData['location'] in results:
        assert False,f"Expected {jsonData['location']} in DB results"



def test_getEnvironmentSettings(env_type):
    print(f"The command line environment value is {env_type}")

@allure.title("Test Creating duplicate email")
@allure.description("This test attempts to create 2 users with same email")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Bhawna Sharma")
@allure.testcase("TMS-1456")
@pytest.mark.sanity
@pytest.mark.dependency()
@log_function_call
def test_given_userswithsameemail_thenfail(readConfig,logging_fixture):
    logger = logging_fixture
    fake=Faker()
    global userId
    emailid=fake.email();
    user1=user("bhawna","sharma",emailid,"canada")
    user2=user("nishhita","aggarwal",emailid,"canada")
    logger.info(f"The details of user1 is: {user1.to_dict()}")
    logger.info(f"The details of user2 is: {user2.to_dict()}")
    response=requests.post(readConfig.get("baseurl")+"/createuser/",data=user1.to_dict())
    assert response.status_code==201,f"Expected 201 but got {response.status_code}"
    with allure.step("Capturing response for valid user creation"):
        logger.info(f"The response message is {response.json()['message']}")
        assert True
    logger.info(f"The response message is {response.json()['message']}")
    userId = response.json()["userid"]

    response = requests.post(readConfig.get("baseurl") + "/createuser/", data=user2.to_dict())
    assert response.status_code != 201, f"Expected 400 but got {response.status_code}"
    with allure.step("Capturing response for valid user creation"):
        logger.info(f"The response message is {response.json()['message']}")
    logger.info(f"The response message is {response.json()['message']}")





@allure.title("Test adding income and check the created income value")
@allure.description("This test attempts to add income to the already existing user in system ")
@allure.tag("NewUI", "Essentials")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Bhawna Sharma")
@allure.testcase("TMS-1426")
@log_function_call
@pytest.mark.sanity
@pytest.mark.dependency(depends=["test_given_userswithsameemail_thenfail"])
def test_getIncome(readConfig,logging_fixture):
    create_income={
        "userid": userId,
        "start_date": "2024-01-29",
        "end_date": "2024-01-29",
        "salary": 5800

    }
    response=requests.post(readConfig["baseurl"] + f"/createincome/",data=create_income)
    assert response.status_code==201,f"Expected status code was 201 but got {response.status_code}"
    create_income_json=response.json()

    response=requests.get(readConfig["baseurl"]+f"/getincome/?user_id={userId}")
    assert response.status_code == 200, f"Expected status code was 200 but got {response.status_code}"

    get_income_json=response.json()
    get_income_dict=get_income_json[len(get_income_json)-1]

    for key,value in get_income_dict.items():
        if key in create_income_json:
            assert get_income_dict[key]==create_income_json[key],f"Expected get income api {key} and {value} to match create income api {create_income_json[key]}"





