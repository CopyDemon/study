import pathlib
import json




def read_spec_file(file_path: str):
    """
    Read a spec file and return the contents
    """
    with open(file_path, "r") as file:
        print("in function")
        return json.load(file)
    
def print_keys(file_content: str):
    """
    Get the keys from the spec file
    """
    print("reading keys from spec file")
    keys = file_content.keys()
    # print(keys)
    return keys


file_path = pathlib.Path(__file__).parent / "spec.json"
file_content = read_spec_file(file_path)
keys = print_keys(file_content)

# print_keys(file_content["schemes"])


if __name__ == "__main__":
    print("start reading spec file")