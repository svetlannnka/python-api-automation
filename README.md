# python-api-automation

written in
### Python 3, py.test


## Installation

1. Download [Python 3.8](https://www.python.org/downloads/)
2. Install Python from the downloaded package.
3. Clone the project, navigate to project directory from your terminal, run:
```pip3 install -r requirements.txt```

## Running the tests
To start all the final tests from a terminal, inside the project, run ```python3 -m pytest --alluredir=test_results/ -m final_tests```

## Report
To generate the report, run ```allure serve test_results```

More about Allure implementation for pytest is [here](https://docs.qameta.io/allure/#_pytest).


## How to add a test:
1. Create a new .py file under 'tests'. Note: name should be test_*.py or *_test.py (otherwise it will not run!)
2. Create a test suite, add a class Test* into your .py file
3. Inside the test class, add tests. Note: every test method should start with 'test_'.
4. To generate a good report, do not forget to use @allure decorators and mark features and steps.

[More about pytest.](https://docs.pytest.org/en/latest/getting-started.html#create-your-first-test)


##### _Happy testing!_