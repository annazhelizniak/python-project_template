def output_to_console(text):
    """
    Writing text to console

    Args:
        text (str): value to be written
    """
    print(text)


def output_to_file(text, file):
    """
    Writing text to file

    Args:
        text (str): value to be written
        file (str): path to the file where to write text
    """
    with open(file, 'w') as f:
        f.write(text)


def output_to_file_with_pandas(df, file):
    """
    Writing DataFrame to file using pandas

    Args:
        df (DataFrame): value to be written
        file (str): path to the file where to write text
    """
    df.to_csv(file, index=False)

