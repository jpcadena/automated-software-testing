# automated-software-testing

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** Markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="assets/images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Automated software testing</h3>

  <p align="center">
    Automated software testing
    <br />
    <a href="https://github.com/jpcadena/automated-software-testing"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
       <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
        <li><a href="#built-with">Built with</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
         <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#security">Security</a></li>
    <li><a href="#code-of-conduct">Code of Conduct</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>  </ol>
</details>


<!-- ABOUT THE PROJECT -->

## About the Project

![Project][project-screenshot]

This project focuses on implementing automated software testing for two types of applications: a simple CLI app and a RESTful API built with Flask. The goal is to ensure robust and reliable functionality through comprehensive test coverage, utilizing both unit and integration tests.

### Key Features

- **CLI App Testing**: Automates the testing of command-line interface applications, verifying correct input handling, output generation, and error management.
- **RESTful API Testing**: Implements automated tests for the Flask-based API, covering various endpoints, HTTP methods, and expected responses.
- **Test Frameworks**: Leverages popular Python testing frameworks such as `pytest` and `unittest` to structure and execute tests efficiently.
- **Continuous Integration**: Integrates with CI tools to run tests automatically on code changes, ensuring consistent code quality and functionality.
- **Mocking and Patching**: Uses mocking and patching techniques to simulate external dependencies and isolate test environments.

By automating the testing process, this project aims to enhance development efficiency, reduce bugs, and maintain high code quality.

### Built with

[![Python][python-shield]][python-url] [![Pytest][pytest-shield]][pytest-url][![flask][flask-shield]][flask-url] [![isort][isort-shield]][isort-url][![Black][black-shield]][black-url] [![Ruff][ruff-shield]][ruff-url] [![MyPy][mypy-shield]][mypy-url] [![pre-commit][pre-commit-shield]][pre-commit-url] [![GitHub Actions][github-actions-shield]][github-actions-url] [![Poetry][poetry-shield]][poetry-url] [![Pycharm][pycharm-shield]][pycharm-url] [![Visual Studio Code][visual-studio-code-shield]][visual-studio-code-url] [![Markdown][markdown-shield]][markdown-url] [![License: MIT][license-shield]][license-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->

## Getting started

### Prerequisites

* [Python 3.12][python-docs]

### Installation

1. Clone the **repository**
    
   ```bash
    git clone https://github.com/jpcadena/automated-software-testing.git
    ```
2. Change the directory to **root project**

    ```bash
    cd automated-software-testing
    ```
3. Install **Poetry** package manager

   ```bash
   pip install poetry
   ```

4. Install the project's **dependencies**

   ```bash
   poetry install
   ```

5. Activate the **environment**

   ```bash
   poetry shell
   ```


<!-- USAGE EXAMPLES -->

### Usage

1. If found **sample.env**, copy it and rename it to **.env**.
2. Replace your **credentials** into the *.env* file.
3. Execute with console
   
   ```bash
    python main.py
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->

## Contributing

[![GitHub][github-shield]][github-url]

Please read our [contributing guide](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SECURITY -->

## Security

For security considerations and best practices, please refer to our [Security Guide](SECURITY.md) for a detailed guide.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CODE_OF_CONDUCT -->

## Code of Conduct

We enforce a code of conduct for all maintainers and contributors. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to understand the expectations before making any contributions.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

- [![LinkedIn][linkedin-shield]][linkedin-url]

- [![Outlook][outlook-shield]](mailto:jpcadena@espol.edu.ec?subject=[GitHub]automated-software-testing)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[project-screenshot]: assets/images/project.png
[python-docs]: https://docs.python.org/3.12/
[linkedin-shield]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white
[outlook-shield]: https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white
[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[pycharm-shield]: https://img.shields.io/badge/PyCharm-21D789?style=for-the-badge&logo=pycharm&logoColor=white
[markdown-shield]: https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white
[github-shield]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[ruff-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json
[black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge&logo=appveyor
[mypy-shield]: https://img.shields.io/badge/mypy-checked-2A6DB2.svg?style=for-the-badge&logo=appveyor
[visual-studio-code-shield]: https://img.shields.io/badge/Visual_Studio_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white
[poetry-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/python-poetry/website/main/static/badge/v0.json
[isort-shield]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
[github-actions-shield]: https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white
[pre-commit-shield]: https://img.shields.io/badge/pre--commit-F7B93E?style=for-the-badge&logo=pre-commit&logoColor=white
[pytest-shield]: https://img.shields.io/badge/logo-pytest-blue?logo=pytest&labelColor=5c5c5c&label=%20
[flask-shield]: https://img.shields.io/badge/flask-%23BCE3E6.svg?style=for-the-badge&logo=flask&logoColor=white
[license-shield]: https://img.shields.io/badge/License-MIT-yellow.svg

[linkedin-url]: https://linkedin.com/in/juanpablocadenaaguilar
[python-url]: https://docs.python.org/3.12/
[pycharm-url]: https://www.jetbrains.com/pycharm/
[markdown-url]: https://daringfireball.net/projects/markdown/
[github-url]: https://github.com/jpcadena/automated-software-testing
[ruff-url]: https://beta.ruff.rs/docs/
[black-url]: https://github.com/psf/black
[mypy-url]: http://mypy-lang.org/
[visual-studio-code-url]: https://code.visualstudio.com/
[poetry-url]: https://python-poetry.org/
[isort-url]: https://pycqa.github.io/isort/
[github-actions-url]: https://github.com/features/actions
[pre-commit-url]: https://pre-commit.com/
[pytest-url]: https://docs.pytest.org/en/8.2.x/
[flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[license-url]: https://opensource.org/licenses/MIT
