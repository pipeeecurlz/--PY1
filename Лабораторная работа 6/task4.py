import json


INPUT_FILE = "input.csv"


def csv_to_list_dict(file_) -> list[dict]:
    with open(file_) as f:
        data = []
        titles = f.readline().strip('\n').split(',')
        lines = [line.strip('\n').split(',') for line in f.readlines()]
        for line in lines:
            dict_values = dict(zip(titles, line))
            data.append(dict_values)
    return data
    
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

