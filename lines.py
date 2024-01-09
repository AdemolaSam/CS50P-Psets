import sys

def main():
    file = get_file()
    lines = count_line(file)
    print(lines)

def get_file():
    lines=[]

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith('.py') == False:
        sys.exit("Not a Python file")
    try:
        with open(f"{sys.argv[1]}") as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        sys.exit("File does not exist")
    return lines

def count_line(file):
    num_of_lines = 0
    for line in file:
        if not line.startswith("#") and line != "":
            num_of_lines += 1
    return num_of_lines



if __name__ == "__main__":
    main()
