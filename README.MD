# Create .gitignore file FIRST. ignore .env and venv

# Creates a virtual environment within python. 
'''Powershell.

python -m venv venv
'''

# Upgrading pip
'''Powershell.

pip install --upgrade pip
'''

# Purpose of program
This program will be utilized to compile and convert historical record data from hockey-reference.com. The data is segmented by draft year over the course of 38 seperate draft classes. This file is seperated into different python files based on the intended purpose of the user. This includes the converter, uploader, 



Converter.py: This component of the program will parse through a specified CSV, convert this CSV format to JSON. This .json file will then be created and stored in a seperate file. 

Uploader.py while iterate over the list of files in the .csv or .json file folders and copy the contents of each draft year into a postgresql datatable that already exists within database. 




All data is provided by hockey-reference.com
