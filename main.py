import json
import py_compile
import subprocess
import sys
import time
import dotenv
from openai import OpenAI
from contextlib import redirect_stdout

from additional import create_test_template, filter_page_html

dotenv.load_dotenv()

client = OpenAI()

# URL = "https://sea-lion-app-q6nwz.ondigitalocean.app/sample1"
# URL = "https://www.saucedemo.com/"
# URL = "https://www.ss.lv/lv/search/"
# URL = "https://demoqa.com/automation-practice-form"

prompt_tokens = 0
response_tokens = 0

# model = "gpt-3.5-turbo"
# model = "gpt-4-turbo"
# model = "gpt-4o"

# Evaluation of the test script: check if the test script covers the requirements and evaluate implementation quality
def evaluate_code_and_requirements(requirements: list, code: str, evaluate_code=False, stdout_output="",
                                   stderr_output=""):
    global prompt_tokens
    global response_tokens
    page_source = filter_page_html(URL)
    system_prompt_requirements = """
    You are responsible of doing the requirement review of the test script of automatic GUI tests.
    You will receive the test script written in Python using Selenium framework and requirements it must cover.
    Make your review comments as specific as possible.
    You will receive test script, requirements.
    You return JSON format similar to this one:
    {
        "missing_requirements": [],
    }
    """

    system_prompt_code = """
    You are responsible of doing the test script review of automatic GUI tests.
    You will receive the test script written in Python using Selenium framework and requirements it must cover.
    Make your review comments as specific as possible.
    You will receive test script, requirements.
    You return JSON format similar to this one:
    {
        "implementation_errors": [],
    }
    """

    user_prompt_requirements = f"""
    Evaluate if the test script covers these requirements.
    Requirements:
    {requirements}
    Test script:
    {code}
    """

    user_prompt_code = f"""
    Evaluate the test script for bugs and make suggestion how to fix them.
    Page HTML content:
    {page_source}
    Stdout output: {stdout_output}
    Stderr output: {stderr_output}
    Test script:
    {code}
    """

    messages = [
        {"role": "system", "content": system_prompt_requirements},
        {"role": "user", "content": user_prompt_requirements},
    ]

    if evaluate_code:
        messages = [
            {"role": "system", "content": system_prompt_code},
            {"role": "user", "content": user_prompt_code},
        ]

    ## LLM gpt-3.5-turbo-0125
    ## gpt-4-turbo
    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=messages,
        temperature=0.1
    )
    prompt_tokens += response.usage.prompt_tokens
    response_tokens += response.usage.completion_tokens
    print(response.choices[0].message.content)
    return json.loads(response.choices[0].message.content)


def generate_code(requirements: list):
    # driver.get(URL)
    # html = driver.page_source
    global prompt_tokens
    global response_tokens

    html = filter_page_html(URL)

    with open("configs/generator_system_prompt.txt") as file:
        system_prompt = file.read()

    script_template = create_test_template(requirements)
    user_prompt = f"""
    Complete the test script template give to you for page {URL}. The output script must be 
    complete and executable test script that covers all the requirements defined in the template.
    Requirements:
    {requirements}
    Here is the HTML content of the page:
    {html}
    This is the script template - add all imports and fill up all test scenarios with your implementation.
    {script_template}
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    ## LLM gpt-3.5-turbo-0125
    ## gpt-4-turbo
    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=messages,
        temperature=0.1
    )

    messages_template = messages.copy()
    prompt_tokens += response.usage.prompt_tokens
    response_tokens += response.usage.completion_tokens
    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    test_script = json.loads(response.choices[0].message.content)
    test_script = test_script["test_script"]

    filename = "outputs/test_scrip.py"
    with open(filename, "w") as file:
        file.write(test_script)

    # Review the test script requirements
    for i in range(5):
        review = evaluate_code_and_requirements(requirements, test_script)
        if review.get("missing_requirements"):
            feedback = f"""
             Missing requirements: {review}
             Please review all missing requirements and implement them and return fixed test script as JSON object.
             """

            messages.append({"role": "user", "content": feedback})
            ## LLM gpt-3.5-turbo-0125
            ## gpt-4-turbo
            response = client.chat.completions.create(
                model=model,
                response_format={"type": "json_object"},
                messages=messages,
                temperature=0.1
            )
            prompt_tokens += response.usage.prompt_tokens
            response_tokens += response.usage.completion_tokens
            messages = messages_template.copy()
            messages.append({"role": "assistant", "content": response.choices[0].message.content})
            test_script = json.loads(response.choices[0].message.content)
            test_script = test_script["test_script"]

            filename = f"outputs/test_script_req_fix_{i}.py"
            with open(filename, "w") as file:
                file.write(test_script)

            print(f"You're missing this requirements in {i} run", review)
        else:
            break

    stdout_output = ""
    # Execute the test script and get all compilation and execution errors
    try:
        py_compile.compile(filename)
        output = subprocess.run([sys.executable, filename], capture_output=True)
        stdout_output = output.stdout.decode()
        stderr_output = output.stderr.decode()
    except Exception as e:
        stderr_output = str(e)

    print("Your test execution output: ", stdout_output, stderr_output)

    review = evaluate_code_and_requirements(requirements, test_script, evaluate_code=True, stdout_output=stdout_output,
                                            stderr_output=stderr_output)

    #  Evaluate the test script quality and errors
    for i in range(5):
        # review = evaluate_code_and_requirements(requirements, test_script, evaluate_code=True)
        if stdout_output or stderr_output:
            # if review.get("implementation_errors"):
            feedback = f"""
            Your test script execution standard output (stdout): {stdout_output}
            Your test script execution error output (stderr): {stderr_output}
            Review: {review}
            Please fix all implementation errors and similar issues that you find in the test script.
            Return fixed test script as JSON object.
            """

            messages.append({"role": "user", "content": feedback})
            ## LLM gpt-3.5-turbo-0125
            ## gpt-4-turbo
            response = client.chat.completions.create(
                model=model,
                response_format={"type": "json_object"},
                messages=messages,
                temperature=0.1
            )
            prompt_tokens += response.usage.prompt_tokens
            response_tokens += response.usage.completion_tokens
            messages = messages_template.copy()
            messages.append({"role": "assistant", "content": response.choices[0].message.content})
            test_script = json.loads(response.choices[0].message.content)
            test_script = test_script["test_script"]

            filename = f"outputs/test_script_fixed_{i}.py"
            with open(filename, "w") as file:
                file.write(test_script)

            stdout_output = ""
            try:
                py_compile.compile(filename)
                output = subprocess.run([sys.executable, filename], capture_output=True)
                stdout_output = output.stdout.decode()
                stderr_output = output.stderr.decode()
            except Exception as e:
                stderr_output = str(e)

            print(f"Your test execution output in {i} run", stdout_output, stderr_output)
        else:
            break


def generate_requirements():
    # driver.get(URL)
    # html = driver.page_source
    global prompt_tokens
    global response_tokens

    html = filter_page_html(URL)
    with open("configs/analyst_system_prompt.txt") as file:
        system_prompt = file.read()

    user_prompt = f"""
    Create test scenarios for the page {URL} and for each scenario provide input data.
    Here is the HTML content of the page:
    {html}

    Create test scenarios that cover the positive and negative test cases for provided page.
    """
    ## LLM gpt-3.5-turbo-0125
    ## gpt-4-turbo

    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.1
    )

    prompt_tokens += response.usage.prompt_tokens
    response_tokens += response.usage.completion_tokens

    test_scenarios = json.loads(response.choices[0].message.content)
    with open("outputs/test_scenarios.json", "w") as file:
        json.dump(test_scenarios, file)

    return test_scenarios["requirements"]


def main():
    output = f"outputs/console_output.txt"
    with open(output, "w") as file, redirect_stdout(file):
            start_time = time.time()
            requirements = generate_requirements()
            print(requirements)
            generate_code(requirements)
            end_time = time.time()
            duration = end_time - start_time
            print(f"Execution time: {duration} seconds\n")
            print(f"GPT3.5 Prompt tokens: {prompt_tokens}, ${prompt_tokens * 0.0000005}\n"
                  f"GPT3.5 Response tokens: {response_tokens}, ${response_tokens * 0.0000015}\n")
            print(f"GPT4 Prompt time: {prompt_tokens}, ${prompt_tokens * 0.00001}\n"
                  f"GPT4 Response tokens: {response_tokens}, ${response_tokens * 0.00003}\n")


if __name__ == '__main__':
    main()
