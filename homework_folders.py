import os

new_dir = "Temp_hw/folder/new_dir"
file_name = ('Temp_hw/folder/file.txt')


with open(file_name) as file:
    file = file.read().splitlines()
    while '' in file:
        file.remove('')
    new_file1 = file[0]
    new_file2 = file[1]
    new_file3 = file[2]
    new_file4 = file[3]
    print(new_file1)
    print(new_file2)
    print(new_file3)
    print(new_file4)

try:
    os.mkdir(new_dir)
except:
    print("Папка с таким названием уже существует")

first_file = open("Temp_hw/folder/new_dir/first_file", "w")
first_file.write(new_file1)
first_file.close()

second_file = open("Temp_hw/folder/new_dir/second_file", "w")
second_file.write(new_file2)
second_file.close()

third_file = open("Temp_hw/folder/new_dir/third_file", "w")
third_file.write(new_file3)
third_file.close()

fourth_file = open("Temp_hw/folder/new_dir/fourth_file", "w")
fourth_file.write(new_file4)
fourth_file.close()

os.remove(file_name)


