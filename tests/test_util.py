import unittest
from unittest.mock import patch, mock_open
from util.filehelper import (
    file_to_array,
    get_number_list_from_file,
    get_string_lists_from_file,
)


class TestUtil(unittest.TestCase):
    def test_file_to_array_opens_the_corrrect_file(self):
        path = "./puzzles/01/puzzle.txt"
        with patch("builtins.open", mock_open(read_data="8\n9\n10")) as mock_file:
            file_to_array(path)
            assert open(path).read() == "8\n9\n10"
            mock_file.assert_called_with(path)
            mock_file.reset_mock()

    def test_file_to_array_transforms_file_content_to_array(self):
        path = "./puzzles/01/puzzle2.txt"
        with patch("builtins.open", mock_open(read_data="8\n9\n10")) as mock_file:
            expected = [8, 9, 10]
            result = file_to_array(path)
            assert len(expected) == len(result)
            assert sorted(expected) == sorted(result)
            mock_file.reset_mock()

    def test_get_number_list_from_file_transforms_file_content_to_array(self):
        path = "./puzzles/02/puzzle.txt"
        with patch("builtins.open", mock_open(read_data="8,9,10")) as mock_file:
            expected = [8, 9, 10]
            result = get_number_list_from_file(path)
            assert len(expected) == len(result)
            assert sorted(expected) == sorted(result)
            mock_file.reset_mock()

    def test_get_string_lists_from_file_transforms_file_content_to_array(self):
        path = "./puzzles/02/puzzle.txt"
        with patch("builtins.open", mock_open(read_data="a,b,c\nd,e,f")) as mock_file:
            expected = [["a", "b", "c"], ["d", "e", "f"]]
            result = get_string_lists_from_file(path)
            assert len(expected) == len(result)
            assert sorted(expected) == sorted(result)
            mock_file.reset_mock()


if __name__ == "__main__":
    unittest.main()
