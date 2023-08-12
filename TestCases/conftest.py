import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching from Chrome")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching from Firefox")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching from Edge")
    else:
        print('HeadlessMode')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver


def pytest_metadata(metadata):
    metadata["Class"] = "Credence"
    metadata["Batch"] = "CT14"
    metadata['URL'] = "https://automation.credence.in"
    metadata.pop("Platform", None)


@pytest.fixture(params=[
    ("Credencetest@test.com", "Credence@123"),
    ("Credencetest@test.com", "Credence@124"),
    ("Credenrcetest@test.com", "Credence@123"),
    ("Credencetst@test.com", "Credence@126")
])
def data_for_login(request):
    return request.param
