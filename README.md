# JM-Aquatics
JM Aquatics Code to Automate and Organize excel Files
Install Visual Studio Code.
Install Python extension for VSCode.
Request Python 3.9.X from the software store. Alternatively, Python 3.9.6 is automatically installed with Visual Studio Professional 2019. Note: We will be using Django 4.0.4 which has a Python 3.8 minimum requirement.
Open the backend directory in VSCode (MTP-WebApp/Backend).
Press Ctrl+Shift+P and select "Python: Select Interpreter". Select Python 3.9.X. Do not use 3.11 or above because youre requirements will not match
Press Ctrl+Shift+P and select "Python: Create Terminal".
Create a virtual environment using "py -m venv venv".
Press Ctrl+Shift+P and select "Python: Select Interpreter". Select the Python with your virtual environment path.
Open another terminal. The virtual environment will automatically activate. Alternatively, type "./venv/Scripts/activate".
Install the required packages using "pip install -r requirements.txt"
Test that the installation worked. Type "python manage.py runserver". If the command works, press Ctrl+Click the localhost link that appears in terminal.
 

 