import pytest
import os
import json
import requests
import allure
from pojo.user import *
from faker import Faker
from utilities.logging_decorator import log_function_call

userId = None


def getJsonData(filename):
    file_path = os.path.join("tests/data/", filename)
    print(f"the file path is :{file_path}")
    with open(file_path, "r") as f:
        json_file = json.load(f)
    return json_file


@allure.title("Test New User Creation")
@allure.description(
    "This test creates a new user in toolsQA")
@allure.tag("NewUI", "ToolsQA", "User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.parametrize("jsonData", getJsonData("createUserData.json"))
@pytest.mark.dependency
@log_function_call
@pytest.mark.DBTest
def test_create_user(jsonData,readConfig,logging_fixture):
    print(f"Creating data")
