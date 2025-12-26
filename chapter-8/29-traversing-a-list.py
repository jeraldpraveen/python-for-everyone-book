list_example = ['spam', 2.0, 5, [10, 20]]
# Traversing the list using a for loop
for item in list_example:
    print("Item:", item)
# Traversing the list using indexes
for index in range(len(list_example)):
    print("Index:", index, "Item:", list_example[index])
# Using enumerate to get index and value
for index, item in enumerate(list_example):
    print("Enumerate - Index:", index, "Item:", item)
