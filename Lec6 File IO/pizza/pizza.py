from tabulate import tabulate
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as file:
            row_num = 0
            table = []
            headers = []

            for line in file:
                row = line.rstrip().split(",")

                if row_num == 0:
                    headers = row
                else:
                    table.append(row)
                
                row_num += 1

        print(tabulate(table, headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()