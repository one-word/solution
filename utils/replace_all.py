# 替换argv[1]路径下的所有目录名、文件名、文件内容，匹配和替换文本为Json字符串类型argv[2]

import os
import sys
import json

def replace_in_files(root_dir, replacements):
    if root_dir.endswith("target"):
        return
    for root, dirs, files in os.walk(root_dir):
        for dir_name in dirs:
            old_dir_path = os.path.join(root, dir_name)
            new_dir_name = dir_name
            for old_str, new_str in replacements.items():
                new_dir_name = new_dir_name.replace(old_str, new_str)
            new_dir_path = os.path.join(root, new_dir_name)
            if old_dir_path != new_dir_path:
                os.rename(old_dir_path, new_dir_path)
                print(f"Renamed directory: {old_dir_path} -> {new_dir_path}")
            replace_in_files(os.path.join(new_dir_path), replacements)

        for file_name in files:
            old_file_path = os.path.join(root, file_name)
            new_file_name = file_name
            for old_str, new_str in replacements.items():
                new_file_name = new_file_name.replace(old_str, new_str)
            new_file_path = os.path.join(root, new_file_name)
            if old_file_path != new_file_path:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed file: {old_file_path} -> {new_file_path}")

            replace_in_file(new_file_path, replacements)

def replace_in_file(file_path, replacements):
    if file_path.endswith(".java") or file_path.endswith(".xml"):
        with open(file_path, 'r') as file:
            file_contents = file.read()

        updated_contents = file_contents
        for old_str, new_str in replacements.items():
            if old_str in updated_contents:
                updated_contents = updated_contents.replace(old_str, new_str)

        if updated_contents != file_contents:
            with open(file_path, 'w') as file:
                file.write(updated_contents)

# 输入目标路径
target_path = sys.argv[1]

# 替换字典，键是需要替换的字符串，值是替换后的字符串
replacements = json.loads(sys.argv[2])

replace_in_files(target_path, replacements)
