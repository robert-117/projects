import json

with open("file.log", "r") as file:
    my_json_obj = json.load(file)
    for key, value in my_json_obj.items():
        print(f"{key}: {value}")