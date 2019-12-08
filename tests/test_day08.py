from day08 import parse_image


class TestDay08:
    def test_parse_image_works(self):
        image_data = "123456789012"
        width = 3
        height = 2
        expected = [
            [["1", "2", "3"], ["4", "5", "6"]],
            [["7", "8", "9"], ["0", "1", "2"]],
        ]

        result = parse_image(image_data, width, height)
        print(f"{result}")
        assert result == expected

