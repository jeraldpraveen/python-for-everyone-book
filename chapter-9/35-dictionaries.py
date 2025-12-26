# Dictionary is like a list, but instead of using numerical indices to access values,
# it uses keys. Keys can be of various data types, such as strings or numbers.
# Here is an example of how to create and use a dictionary in Python:# Creating a dictionary

temp_dict = dict()  # Using the dict() constructor
print("Empty dictionary:", temp_dict)  # Output: {}

# Creating a dictionary with initial key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values using keys
print(person["name"])  # Output: Alice

# Adding a new key-value pair
person["job"] = "Engineer"
print(person)
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

print("Length:", len(person))  # Output: 4

print("Keys:", list(person.keys()))  # Output: ['name', 'age', 'city', 'job']
# Output: ['Alice', 30, 'New York', 'Engineer']
print("Values:", list(person.values()))
print("Existing Keys:", "age" in person)  # Output: True
print("Non-existing Keys:", "salary" in person)  # Output: False
