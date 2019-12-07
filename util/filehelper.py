def file_to_array(path):
    return [int(line.strip()) for line in open(path, "r")]


def get_number_list_from_file(path):
    with open(path, "r") as f:
        return [int(opcode) for opcode in f.read().split(",")]


def get_string_lists_from_file(path):
    res = []
    with open(path, "r") as f:
        for line in f.readlines():
            current_line = []
            for input in line.split(","):
                current_line.append(input.strip())
            res.append(current_line)
    return res


def get_string_list_from_file(path):
    return [line.strip() for line in open(path, "r")]
