from util.filehelper import get_string_list_from_file


def print_image(layer):
    for row in layer:
        row_data = ""
        for digit in row:
            if digit == "0":
                row_data += " "
            else:
                row_data += "x"
        print(f"{row_data}")


def decode_image(layers):
    res = layers[0]
    for layer in layers[1:]:
        current_row = 0
        for row in layer:
            current_digit = 0
            for digit in row:
                if not res[current_row][current_digit] in ["1", "0"]:
                    res[current_row][current_digit] = digit
                current_digit += 1
            current_row += 1
    return res


def get_number_of_digits_in_layer(layer, number):
    digits_in_rows = 0
    for row in layer:
        digits_in_rows += row.count(str(number))
    return digits_in_rows


def get_layer_with_fewest_0_digits(layers):
    res = None
    count = None
    for layer in layers:
        zeros_in_rows = get_number_of_digits_in_layer(layer, 0)
        if count is None or zeros_in_rows < count:
            count = zeros_in_rows
            res = layer
    return res


def parse_image(picture_data, width, height):
    rows = []
    while len(picture_data) > 0:
        row_data, picture_data = picture_data[:width], picture_data[width:]
        row = []
        for digit in row_data:
            row.append(digit)
        rows.append(row)
    layers = []
    while len(rows) > 0:
        layer, rows = rows[:height], rows[height:]
        layers.append(layer)
    return layers


def day08_01():
    picture_data = get_string_list_from_file("./puzzles/08/puzzle.txt")
    layers = parse_image(picture_data=picture_data[0], width=25, height=6)
    layer_with_fewest_zeros = get_layer_with_fewest_0_digits(layers)
    res = get_number_of_digits_in_layer(
        layer_with_fewest_zeros, 1
    ) * get_number_of_digits_in_layer(layer_with_fewest_zeros, 2)
    print(f"checksum for image {res}")


def day08_02():
    picture_data = get_string_list_from_file("./puzzles/08/puzzle.txt")
    layers = parse_image(picture_data=picture_data[0], width=25, height=6)
    decoded_image = decode_image(layers)
    print_image(decoded_image)


if __name__ == "__main__":
    day08_01()
    day08_02()
