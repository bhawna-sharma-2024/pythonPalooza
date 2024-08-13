

import pytest

def pytest_addoption(parser):
   parser.addoption("--env-type",action="store",default="local",help="command line option to specify env")

@pytest.fixture(scope="session")
def env_type(request):
   return request.config.getoption("--env-type")

pytest_plugins = [
   "fixtures.readFiles",
   "fixtures.log_fixture"
]





