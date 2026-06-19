Virtual Environment

A virtual environment creates an isolated Python environment for a project.

Why Use Virtual Environment?

Without venv:

Project A
Project B
Project C

All use same packages.

Conflicts may happen ❌

With venv:

Project A → Own Packages
Project B → Own Packages
Project C → Own Packages

No conflicts ✅


Example 1

Create virtual environment.

python -m venv venv
Example 2

Activate in Windows.

venv\Scripts\activate

Output:

(venv)
Example 3

Install package.

pip install fastapi
Example 4

Deactivate environment.

deactivate