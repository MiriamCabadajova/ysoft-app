import unittest
import sys
from printing_app import letter_freq, write_data_to_output


def create_correct_output_file(correct_answer, a, b, c, d):
    """
    Function which puts the string obtained in the correct_answer parameter
    into file "correct_output.txt" and stdout of write_data_to_output function
    into "your_output.txt" file.

    :param correct_answer: string interpretation of correct data
    :param a: user name
    :param b: printer name
    :param c: output file
    :param d: input data
    """

    file = open("correct_output.txt", "w")
    file.write(correct_answer)

    original = sys.stdout

    sys.stdout = open("your_output.txt", "w")
    write_data_to_output(a, b, c, d)
    sys.stdout.close()

    sys.stdout = original
    file.close()


def output(name):
    """
    Function which opens the file whose name is passed as a parameter and returns
    its content in a string representation, throws an exception if the file does not
    exist.

    :param name: name of the file
    :return: string representation of the content of the file
    """

    try:
        file = open(name, "r")
    except FileNotFoundError:
        print("the input file does not exist")
        sys.exit(2)

    string = file.read()
    file.close()
    return string


# a dictionary used in advanced tests for letter frequency (letter_freq function)
correct_dictionary = {"y": 1, "s": 1, "o": 1, "f": 1, "t": 3, "p": 1, "r": 1,
                      "i": 1, "n": 3, "m": 2, "a": 2, "g": 1, "e": 2}


class TestLetterFrequency(unittest.TestCase):

    def test_frequency_empty(self):
        self.assertEqual({}, letter_freq(" "), "Your dictionary should be empty")
        self.assertEqual({}, letter_freq("   \t\n\n  \n"), "Your dictionary should be empty")
        self.assertEqual({}, letter_freq("\n   \t  "), "Your dictionary should be empty")

    def test_frequency_basic(self):
        self.assertEqual({"a": 1}, letter_freq("a"), "One letter input data")
        self.assertEqual({"a": 2}, letter_freq("aa"), "Two same letter input data")
        self.assertEqual({"a": 1, "b": 1}, letter_freq("ab"), "Two different letter input data")
        self.assertEqual({"a": 2}, letter_freq("\n  a a  \t\n\n\n\t "), "Two same letter input data with spaces")

    def test_frequency_advanced(self):
        output_dictionary = letter_freq("ysoftprintmanagement")
        self.assertEqual(correct_dictionary, output_dictionary, "Your dictionary is not correct")

    def test_frequency_advanced_with_spaces(self):
        output_dictionary = letter_freq("ysoft print management")
        self.assertEqual(correct_dictionary, output_dictionary, "Your dictionary is not correct")

        output_dictionary = letter_freq("\t\t  ysoftp\nrintman agem  ent\t\n")
        self.assertEqual(correct_dictionary, output_dictionary, "Your dictionary is not correct")

    def test_frequency_advanced_upper_case(self):
        output_dictionary = letter_freq("YSOFT PRINT MANAGEMENT")
        self.assertEqual(correct_dictionary, output_dictionary, "The keys in your dictionary should be lowercase")

        output_dictionary = letter_freq(" Yso\tftPRI n\nt mana  geME\nNT \t")
        self.assertEqual(correct_dictionary, output_dictionary, "Your dictionary is not correct")


class TestCorrectStdOut(unittest.TestCase):

    def test_stdout_empty(self):
        create_correct_output_file("", "u", "p", "your_json.json", "")
        self.assertEqual(output("correct_output.txt"), output("your_output.txt"),
                         "Your stdout should be empty")

    def test_stdout_basic(self):
        create_correct_output_file("a: 1\n", "u", "p", "your_json.json", "a")
        self.assertEqual(output("correct_output.txt"), output("your_output.txt"),
                         "Your stdout is not correct")

    def test_stdout_advanced(self):
        create_correct_output_file("y: 1\ns: 1\no: 1\nf: 1\nt: 3\np: 1\nr: 1\ni: 1\nn: 3\nm: 2\na: 2\ng: 1\ne: 2\n",
                                   "u", "p", "your_json.json", "ysoftprintmanagement")

        self.assertEqual(output("correct_output.txt"), output("your_output.txt"),
                         "Your stdout is not correct")


if __name__ == '__main__':
    unittest.main()
