import os.path
path_to_file = os.path.join('../..', 'requirements.txt')
file_descriptor = open ('../requirements.txt', encoding='utf-16')
file_text = file_descriptor.read()
print(file_text)


# from os.path import exists, join
# path_to_file = join('..','requirements.txt')
# file_exists = exists(path_to_file)
# if file_exists:
#     file_descriptor = open(path_to_file, 'r', encoding='utf-16')
#     file_text = file_descriptor.read()
#     print(file_text)
# else:
#     print(f'no file: {path_to_file}')