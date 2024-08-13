import pytest
import json
import os

@pytest.fixture(scope="session")
def readConfig(env_type):
    with open("tests/data/stageconfig.json","r") as f:
        json_file=json.load(f)
    for item in json_file:
        if env_type in item:
            return item[env_type]

    return None

'''
@pytest.fixture
def readCreateUserFile():
    #print(f"The file name is......{file_name}")
    file_path=os.path.join("tests/data/","createUserData.json")
    print(f"the file path is :{file_path}")
    with open(file_path,"r") as f:
        json_file=json.load(f)
    return json_file



@pytest.fixture(params=lambda request: request.getfixturevalue('readCreateUserFile'))
def fetchAPIData(request):
    # Make sure request.param is an iterable (e.g., a list)
    for data in request.param:
        yield data
'''




