import os

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"C:\Users\chris\Downloads\prank")
    # print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"C:\Users\chris\Downloads\prank")
    saved_path = os.getcwd()
    print("Current Working Directory changed to "+saved_path)

    # (2) for each file, rename filename
    for file_name in file_list:
        print("Old name = "+file_name)
        print("New name = "+file_name.translate(str.maketrans('', '', '0123456789')))
        os.rename(file_name, file_name.translate(str.maketrans('', '', '0123456789')))
        # print(file_name+" is now "+file_name.translate(str.maketrans('', '', '0123456789')))
    os.chdir(saved_path)

rename_files()
