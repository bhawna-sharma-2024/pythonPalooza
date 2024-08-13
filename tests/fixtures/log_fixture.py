from utilities.logging_config import setup_logging

import pytest
import logging

@pytest.fixture(scope='session', autouse=True)
def logging_fixture():
    yield setup_logging()

    # Optionally, you can configure more complex logger setup here
    # Optionally, add teardown code if needed (e.g., close log files)
