import json


sample_dic = {"ключ21": "занчение 21", "ключ22": "значение 22"}
sample_array = ["значение 31", "значение 32", "значение 33"]

main_dic = {"ключ1": "значение 1"}
main_dic["ключ2"] = sample_dic
main_dic["ключ3"] = sample_array

print(main_dic)
print(json.dumps(main_dic, ensure_ascii=False))

json_str = json.dumps(main_dic, ensure_ascii=False, indent=2)
print(json_str)


file_descriptor = open(r'lesson2.json', 'w', encoding='utf-16')
file_descriptor.write(json_str)
file_descriptor.close()


file_descriptor = open('lesson2.json', 'r', encoding='utf-16')
json_str = file_descriptor.read()
main2_dic = json.loads(json_str)

print(main2_dic)
print(main_dic)