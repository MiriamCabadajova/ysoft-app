import argparse
import json
import sys


class MyParser(argparse.ArgumentParser):
    """
    Modified function error in class ArgumentParser so that if error occurs, help is printed.
    """

    def error(self, message):
        sys.stderr.write("error: " + message + "\n")
        self.print_help()
        sys.exit(2)


def parse_arguments():
    """
    Function which parses the arguments in the command line, prints help if incorrect
    amount of parameters is provided.

    :return: returns parsed arguments
    """

    parser = MyParser()

    parser.add_argument("user_name", help="user name")
    parser.add_argument("printer_name", help="printer name")
    parser.add_argument("input_file", help="path to the input file")
    parser.add_argument("output_file", help="path to the output file")

    args = parser.parse_args()
    return args


def is_ascii_char(char):
    """
    Boolean function which checks whether given character is ascii and not a space.

    :param char: input character
    :return: true / false
    """

    return ord(char) < 128 and char not in '\n\t" "'


def letter_freq(data):
    """
    Function which counts the frequency of each letter and stores it in a dictionary.

    :param data: string representation of input data
    :return: dictionary of letter frequencies
    """

    data = "".join(filter(is_ascii_char, data))
    data = data.lower()

    letter_list = list(data)
    frequency = {}

    for letter in letter_list:
        frequency[letter] = frequency.get(letter, 0) + 1

    return frequency


def write_data_to_output(user_name, printer_name, output_file, data):
    """
    Function which prints frequency of letters in input data to stout and also stores
    the user name, printer name and input data in a JSON file. If the output file does
    not have .json extension, it prints help and ends the program.

    :param user_name: name of the user
    :param printer_name: name of the printer
    :param output_file: the JSON output file
    :param data: input string data
    """

    if len(output_file) < 6 or output_file[-5:] != ".json":
        print("the file must contain \".json\" file extension")
        sys.exit(2)

    frequency = letter_freq(data)

    for key, value in frequency.items():
        print(str(key) + ": " + str(value))

    content_of_json = {"userName: ": user_name, "printerName: ": printer_name, "data: ": data}
    with open(output_file, "w") as json_file:
        json.dump(content_of_json, json_file, indent=5)


def read_input_file(args):
    """
    Function that reads input file from an argument if it exists and returns string
    representation of its content. If it doesn't, it prints help and exits the program.

    :param args: parsed arguments from the command line
    :return: string representation of content of the file
    """
    try:
        f = open(args.input_file, "r")
    except FileNotFoundError:
        print("the input file does not exist")
        sys.exit(2)

    data = ""
    for line in f.readlines():
        data += line

    f.close()
    return data


if __name__ == "__main__":
    arguments = parse_arguments()
    file_content = read_input_file(arguments)
    write_data_to_output(arguments.user_name, arguments.printer_name, arguments.output_file, file_content)
