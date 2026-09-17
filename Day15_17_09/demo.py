# Notes: Environment Variables (.env) and JSON

#  Env Variables
# Environment variables are used to store settings and secrets, like
# passwords, API keys or database URLs, outside of the actual code.
# This keeps sensitive data out of the code and out of source control.

# from dotenv import load_dotenv
# import os

# # pip install python-dotenv
# python-dotenv is a package that lets Python read variables from a
# .env file (a simple text file with KEY=VALUE lines) and load them
# as environment variables, so we do not have to hardcode secrets in
# our code.

# load_dotenv()
# load_dotenv() reads the .env file in the project folder and loads
# all the key-value pairs from it into the environment

# password = os.environ.get("DB_PASSWORD")
# print(password)
# os.environ.get() reads an environment variable by name. Here it
# reads DB_PASSWORD, which must be defined inside the .env file, like:
# DB_PASSWORD=mysecretpassword

# JSON
# JSON (JavaScript Object Notation) is a common text format used to
# store and exchange data, especially between different systems,
# APIs, and config files. It looks a lot like a Python dict.

# dict -> JSON -> json.dumps()
# JSON -> DICT -> json.loads()
# dumps() converts a Python object (like a dict) into a JSON string.
# loads() converts a JSON string back into a Python object.
# (dump()/load() do the same thing, but read/write directly to a file
# instead of working with a string.)

import json

# student ={
#     "name":"Rahul",
#     "age": 20,
#     "marks": [90, 85]
# }
# A normal Python dictionary, which we want to save as JSON

# with open("demo.json", "w") as f:
#     json.dump(student, f)
# json.dump(obj, file) writes the dict directly into the file as JSON
# text, this creates demo.json

with open("demo.json", "r") as f:
    data = json.load(f)
# json.load(file) reads a JSON file and converts its content back
# into a Python object (here, a dict), ready to use in our code

print(data, type(data))
# data is a normal Python dict at this point, even though it came
# from a JSON file

print(json.dumps(data), type(json.dumps(data)))
# json.dumps(data) converts the dict back into a JSON formatted
# string, useful when sending data somewhere that expects JSON text

# Dict -> Object
# JSON -> string
# The key idea to remember: a Python dict is an actual object in
# memory, while JSON is just text, formatted in a specific way that
# looks similar to a dict but is not the same thing


# ------------------------------------------------------------
# Practice Questions
# ------------------------------------------------------------

# 1. Create a .env file with a variable APP_NAME=MyApp, then write
#    code to load it using load_dotenv() and print its value.

# 2. Add a DB_USER and DB_PASSWORD to your .env file, and print both
#    using os.environ.get().

# 3. Create a Python dict with your own name, age and city, and
#    convert it to a JSON string using json.dumps().

# 4. Take a JSON string like '{"name": "Sam", "age": 20}' and convert
#    it back into a Python dict using json.loads().

# 5. Create a dict representing a product (name, price, in_stock),
#    and save it into a file called product.json using json.dump().

# 6. Read product.json back using json.load() and print the price
#    only.

# 7. Create a dict with a nested list of items, save it as JSON, then
#    read it back and print the list.

# 8. Try using os.environ.get() for a variable that does not exist in
#    your .env file, and print the result. Then try giving it a
#    default value using os.environ.get("KEY", "default_value").

# 9. Use json.dumps() with the indent=4 argument to print a dict as
#    a nicely formatted (pretty printed) JSON string.

# 10. Write a small program that reads a .env file for a database
#     name, builds a dict with some sample data, and saves that dict
#     into a JSON file named after the database name.
