import os.path
import os

# with open("1.txt") as f:
#     len_files = f.readlines()
#     print(len(len_files))
#     for index, l in enumerate(f):
#         print(index, l.strip())

# def len_files(files):
#     with open(files) as f:
#         open_files = f.readlines()
#         files_len = len(open_files)
#         print(files_len)
#     print(open_files)
#
# len_files('1.txt')

# print(os.path.join(os.getcwd(), '1.txt'))
# print(os.getcwd())

# sorted_dict = sorted(file_list.__dict__.items(), key=lambda x: x[1])

file_wid = r".txt"
files_txt = [_ for _ in os.listdir() if _.endswith(file_wid)]

def open_files(files):
    file_list = []
    for r_files in files:
        with open(r_files) as r_f:
            o_files = r_f.readlines()
            len_files = len(o_files)
            for x in files:
                name_files = x
                file_list.append({"file": name_files, "len": len_files, "text": o_files})                # sorted_dict = sorted(file_list.__dict__.items(), key=lambda x: x[1])
    print(file_list)

open_files(files_txt)





