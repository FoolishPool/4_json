import json


def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.loads(f.read())
        return data

def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii = False))


if __name__ == '__main__':
    path_to_file = input('Filepath: ')
    pretty_print_json(load_data(path_to_file))
