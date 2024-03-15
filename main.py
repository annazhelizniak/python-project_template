from app.io.input import input_from_console, input_from_file, input_from_file_with_pandas
from app.io.output import output_to_console, output_to_file


def main():
    console_input = input_from_console()
    file_input = input_from_file("data/text_sample")
    file_input_csv = input_from_file_with_pandas("data/csv_sample.csv")

    output_to_console(console_input)
    output_to_console(file_input)
    output_to_console(file_input_csv)

    output_to_file(console_input, "data/console_input")
    output_to_file(file_input, "data/file_input")
    output_to_file(file_input_csv, "data/file_input_csv")


if __name__ == "__main__":
    main()
