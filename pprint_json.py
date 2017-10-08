import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file_json:
        json_content = json.loads(file_json.read())
        return json_content


def pretty_print_json(json_content):
    pretty_print = json.dumps(json_content, sort_keys=True, indent=4,
                              ensure_ascii=False)
    print(pretty_print)

if __name__ == '__main__':
    json_content = load_data(sys.argv[1])
    pretty_print_json(json_content)
