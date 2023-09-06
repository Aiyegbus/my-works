import os

directory_path = "config"
file_path1 = os.path.join(directory_path, "random.txt")
file_path2 = os.path.join(directory_path, "webserver.config")
files_to_be_created = [file_path1, file_path2]
os.makedirs(directory_path, exist_ok= True)

for file_path in files_to_be_created:
    try:
        with open(file_path, "a") as file:
            file.write("This is a test, I am enjoying it")
            print(file_path + " file created succesfully")
    except FileExistsError:
        print(file_path + " file already exist")
    except Exception:
        print('error creating ' + file_path + ' file')