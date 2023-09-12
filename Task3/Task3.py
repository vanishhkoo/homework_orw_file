import os.path
import os

file_wid = r".txt"
files_txt = [_ for _ in os.listdir() if _.endswith(file_wid)]

def open_files(files):
    file_list = []
    for r_files in files:
        name_files = r_files
        with open(r_files) as r_f:
            o_files = r_f.readlines()
            len_files = int(len(o_files))
            file_dict = {"file": name_files, "len": len_files}
                # , "text": o_files[:2]}
            # file_dict = {"file": name_files, "len": len_files}
            file_list.append(file_dict)
            # sorted_dict = sorted(file_dict.values(), key=lambda x: x['len'])
    for x in file_list:
        for y in x.values():
            print(y)
            with open('/Users/vanishhko/Desktop/CookBook/result.txt', 'a') as f:
                f.write(f'{y}\n')
                # open_result.write(f'{y}')
                # open_result.write(f'{name_files}\n')
                # open_result.write(f'{len_files}\n')
                # i = "\n".join(o_files[:2])
                # open_result.write(f'{i}')
                f.close()

    return file_list

open_files(files_txt)





