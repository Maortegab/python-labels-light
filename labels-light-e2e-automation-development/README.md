# Playwright Python

<img src="https://playwright.dev/python/img/playwright-logo.svg" alt="Playwright" style="display: block; margin: 0 auto;">

## Prerequisites

* [Python 3.12.6](https://www.python.org/downloads/release/python-3126/)
* [Pip 24.2](https://pypi.org/project/pip/)
* [Allure](https://allurereport.org/docs/install/)

## Steps to run project

1. **Clone project from Github repo**

```bash
https://github.com/Skydropx/labels-light-e2e-automation.git
```

2. Create virtual environment

``` bash
python3 -m venv ./.venv
```

3. Initialize virtual environment

```bash
source .venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Install browsers

```bash
playwright install
```

6. Copy `.env.template`, rename to `.env` and replace variables.

7. Execute tests with

```bash
pytest
```

8. Generate and create server to see Allure report

```bash
allure serve allure-results
```

## How to tag and execute certain tests?

### Assign a tag

To assign a tag you must use the `@pytest.mark` decorator followed by the name that will identify the test also add in the `pytest.ini` file in the `markers` section the description of the label.

```python
@pytest.mark.sanity()
def test_login_success(page: Page) -> None:
    login_page.navigate()
```

### Execute tests by tag

In order to perform certain tests, they will be executed by means of the test identifier.

```bash
pytest -m sanity
```

## Project Structure

```text
labels-light-e2e-automation/
│
├── data/
│   └── archives/
├── pages/
│   └── admin/
│   └── user/
├── tasks/
│   └── admin/
│   └── user/
├── tests/
│   └── frontend/
├── utils/
│   └── decorators/
│   └── helpers/
│
├── .env.template
├── .gitignore
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## Description project structure

* **data**: Stores information that will be used during testing
* **pages**: Contains a class related to the web page that will be automated. Each file in this folder represents a different page, encapsulating its locators. This folder has 2 subfolders that represent the normal user and admin user view with the aim of improving code distribution and readability.
* **tasks**: Contains a class that performs a specific action on the page, whether interacting, entering information, or validating the state of the page. This folder has 2 subfolders that represent the normal user and admin user view with the aim of improving code distribution and readability.
* **tests**: Stores all test cases. Within this folder, the frontend/ subfolder contains tests specific to the user interface, backend subfolder contains tests in private or public APIs.
* **utils**: Save all project utilities like decorators, helpers, constants, types, etc.
* **.env.template**: A template for the environment variables required for the project's configuration. It serves as a reference to create a custom .env file.
* **gitignore**: Specifies the files and directories that Git should ignore, such as virtual environments, installed dependencies, and temporary files.
* **conftest.py**: A configuration file for `pytest`. This is where fixtures, hooks, and additional test configurations are defined.
* **pytest.ini**: Configuration file for `pytest`, used to define default options and behavior when running the tests.
* **README.md**: Project documentation. It contains information on how to set up, run, and maintain the project.
* **requirements.txt**: A file listing all Python dependencies required to run the project. These can be installed with `pip`.

## Naming conventions

* For python files use lowercase_underscore, example: ***my_file.py***
* For folders use lowercase_underscore, example: ***my_folder***
* For packages and modules use opt for short and concise names, without underscores or hyphens, example: ***mypackage***
* For classes follow CamelCase convention, example: ***MyClass***

## Don't forget

* When external packages are added, the requirements.txt file must be updated. If the file is not updated and uploaded to the remote repository, the lack of the package when installing dependencies can cause problems in local or cloud execution.

```bash
pip freeze > requirements.txt
```
