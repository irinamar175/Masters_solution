# Master's Solution for Test Automation Using LLM

## Description
This solution is created for automated test generation of graphical user interfaces using Large Language Models (LLMs).

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/irinamar175/Masters_solution
    ```
2. Navigate to the project directory:
    ```sh
    cd Masters_solution
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Add your `.venv` LLM API credentials.

## Usage
1. For test running, use the latest stable version of `chromedriver.exe` (Chrome):
   [ChromeDriver Download](https://googlechromelabs.github.io/chrome-for-testing/)

2. It is possible to use other browsers. In that case, you will need to install the corresponding browser driver and adjust the prompts appropriately.

3. To run the code, use the `main.py` file. All output files will be created inside the `outputs` directory.

4. If you need to use images, PDFs, and other documents, add them to the `Documents` directory and adjust the analyst system prompt in `configs/analyst_system_prompt.txt`.

5. Before testing your URL, adjust the `URL` argument and choose your `model` for testing in `main.py`.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/Feature`).
3. Commit your changes (`git commit -m 'Add some Feature'`).
4. Push to the branch (`git push origin feature/Feature`).
5. Open a pull request.

## License
Distributed under the MIT License. See [`LICENSE`](./LICENSE) for more information.

## Contact
Irina Ozolina _(Marcenko)_ - [irina.marchenko175@gmail.com](mailto:irina.marchenko175@gmail.com)
