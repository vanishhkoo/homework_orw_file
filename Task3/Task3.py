import os.path
import os

file_wid = r".txt"
files_txt = [_ for _ in os.listdir() if _.endswith(file_wid)]

def open_files(files):
    file_list = []
    for r_files in files:
        with open(r_files) as r_f:
            o_files = r_f.readlines()
            len_files = len(o_files)
            for x in sorted(files):
                name_files = x
                file_list.append({"file": name_files, "len": len_files, "text": o_files})
    sorted_dict = sorted(file_list[0].values(), key=lambda x: x["len"])
    print(file_list)


open_files(files_txt)





