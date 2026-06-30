Virtual Environment
What is Virtual Environment?

An isolated Python environment for a project.

Why Use It?

Without venv:

Project A
Project B
Project C

All use same packages

Problem:

Version Conflicts ❌

With venv:

Each Project Has Its Own Packages
Example 1

Create environment.

python -m venv venv
Example 2

Activate.

Windows:

venv\Scripts\activate
Example 3

Install package.

pip install fastapi
Example 4

Deactivate.

deactivate