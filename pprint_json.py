import json


def load_data(filepath):
    with open(filepath, 'r') as file:
        json_decode = json.loads(file.read())
        return json_decode

def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii = False))


if __name__ == '__main__':
    path_to_file = input('Filepath: ')
    json_decode = load_data(path_to_file)
    pretty_print_json(json_decode)
