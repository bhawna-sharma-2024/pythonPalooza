import pytest
import os
import json
import requests
import allure
from pojo.user import *
from faker import Faker

userId=None

def getJsonData(filename):
    file_path = os.path.join("tests/data/",filename)
    print(f"the file path is :{file_path}")
    with open(file_path, "r") as f:
        json_file = json.load(f)
    return json_file

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.parametrize("jsonData",getJsonData("createUserData.json"))
@pytest.mark.dependency
def test_post_api(jsonData,readConfig,logging_fixture):
    #print(jsonData)
    logger = logging_fixture
    logger.info(f"Starting test with input_data: {jsonData}")
    logger.warning(f"Starting test with input_data: {jsonData}")
    logger.error(f"Starting test with input_data: {jsonData}")
    response=requests.post(readConfig.get("baseurl")+"/createuser/",data=jsonData)
    response_json = response.json()
    print(f"The response message is: {response.json()}")
    assert response.status_code==201
    assert "User has been created successfully" in response_json["message"]
    assert "userid" in response_json and response_json["userid"] is not None



def test_getEnvironmentSettings(env_type):
    print(f"The command line environment value is {env_type}")

@allure.title("Test Creating duplicate email")
@allure.description("This test attempts to create 2 users with same email")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.issue("AUTH-1213")
@allure.testcase("TMS-1456")
@pytest.mark.sanity
@pytest.mark.dependency()
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





