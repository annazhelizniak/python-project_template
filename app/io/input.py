import pandas as pd


def input_from_console():
    """
    Inputting value from console

    Returns:
        str. The value, that was entered to console by user.
    """
    return input("Enter your text: ")


def input_from_file(file):
    """
    Inputting value from file using Python's built-in functions

    Args:
        file (str): path to the file to read

    Returns:
        str. The content of the file.
    """
    with open(file, 'r') as f:
        content = f.read()
    return content


def input_from_file_with_pandas(file):
    """
    Inputting value from file using Pandas functions

    Args:
        file (str): path to the file to read

    Returns:
        pandas.DataFrame. The content of the file as DataFrame object.
    """
    return pd.read_csv(file)
