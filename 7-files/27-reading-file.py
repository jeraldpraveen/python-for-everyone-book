import os;

script_dir = os.path.dirname(__file__) 
file_path = os.path.join(script_dir, 'read-content.txt')

test_file = open(file_path, 'r')
print(test_file.read())
test_file.close()

# Write to a file
# 'w' will overwrite the file if it exists
# 'a' will append to the end of the file if it exists
# 'r+' will open the file for reading and writing
# 'w+' will open the file for reading and writing, overwriting the file if it exists
# 'a+' will open the file for reading and writing, appending to the end of the file if it exists
with open('write-content.txt', 'w+') as test_file:
    test_file.write('This is a test')
    
    # Move the cursor back to the beginning of the file
    test_file.seek(0) 
    
    content = test_file.read()
    print(content)