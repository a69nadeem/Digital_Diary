import os, json

####------------ Task 1  ----------------completed------

folder_name = "Jan24_db_fileSys"
os.makedirs(folder_name, exist_ok=True)

file_path = os.path.join(folder_name, "my_data.txt")

try:
    with open(file_path, mode="w", encoding="utf-8") as file:
        
        file.write("Hello, this is some text data that I'm saving to a file.")

    print(f'Data saved to {file_path} successfully.')

except IOError as e:
    print(f'Error: {e}')

current_working_directory = os.getcwd()
print(f'Current working directory: {current_working_directory}')

####-------------------- Alternate way-----Task 1 ---------completed

my_folder = "Jan24_db_fileSys"
my_file = "my_data.txt"

if not os.path.exists(my_folder):
    os.makedirs(my_folder)

file_path = os.path.join(my_folder,my_file)

save_data = "Good Day it's my sample data to transfer to the other file and save it"

with open(file_path, mode="w", encoding="utf-8") as file:
    file.write(save_data)


print(f"The data has been saved to '{file_path}' successfully")

#------------Task 2 ---------------completed-----

file_path = "/home/dci-student/Python/Jan24_db_fileSys/python-databases-overview-filesystem-a69nadeem/src/files/data.txt"

try:
    with open(file_path, mode="r", encoding="utf-8") as file:
        
        file_contents = file.read()

    print(file_contents)

except FileNotFoundError:
    print(f"Error: File not found, Please check your file path. ")

except IOError as e:
    print(f'Error: {e}')


##------------Task 3------------------

student_data = {"name": "Paul", "role": "Teacher"}

json_data = json.dumps(student_data, indent=4)  

file_path = "/home/dci-student/Python/Jan24_db_fileSys/example.json"

try:
    with open(file_path, mode="w") as file:
        file.write(json_data)

    print(f'Student data transfer to the given file path {file_path} successfully.')

except FileNotFoundError:
    print(f"Error: File not found, Please check your file path. ")

except IOError as e:
    print(f'Error: {e}')


# ###------------Task 4----------------------
    
json_file_path = "/home/dci-student/Python/Jan24_db_fileSys/example.json"  


try:
    with open(json_file_path, 'r', encoding='utf-8') as file:
        
        json_data = json.load(file)

        print(json.dumps(json_data, indent=4))  

except FileNotFoundError:
    print(f'Error: File not found. Please check the file path.')

except json.JSONDecodeError:
    print(f'Error: Invalid JSON format in the file.')

