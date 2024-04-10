# 删除argv[0]下所有目录名称为argv[1]的目录

import os
import sys

def delete_abc_directories(root_dir):
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if dir_name == sys.argv[1]:
                delete_dir(dir_path)
                print(f"Deleted directory: {dir_path}")
                continue
            delete_abc_directories(dir_path)

        # for file_name in files:
        #     file_path = os.path.join(root, file_name)
        #     # 可选：在这里可以添加其他操作，例如删除文件
        #     print(f"Deleted file: {file_path}")
        #     os.remove(file_path)

def delete_dir(dir_path):
    for root, dirs, files in os.walk(dir_path, topdown=False):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

        for sub_dir in dirs:
            sub_dir_path = os.path.join(root, sub_dir)
            delete_dir(sub_dir_path)
    os.rmdir(dir_path)

# 输入目标路径
target_path = sys.argv[0]
print("目标路径：", target_path)

delete_abc_directories(target_path)
