def file_to_array(path):
    return [int(line.strip()) for line in open(path, "r")]


def get_list_from_file(path):
    with open(path, "r") as f:
        return [int(opcode) for opcode in f.read().split(",")]
