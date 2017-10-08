import json

def load_data(filepath):
    with open(filepath, 'r') as file_json:
        json_content = json.loads(file_json.read())
        return json_content

def pretty_print_json(data):
    pretty_print = json.dumps(data, sort_keys=True, indent=4, ensure_ascii = False)
    print(pretty_print)

if __name__ == '__main__':
    path_to_file = input('Filepath: ')
    json_content = load_data(path_to_file)
    pretty_print_json(json_content)
