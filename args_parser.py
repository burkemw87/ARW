import argparse


def parse_the_file_path():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="enter the file path")
    args = parser.parse_args()
    return args.file_path


def main():
    file_path = parse_the_file_path()
    print(file_path)


if __name__ == '__main__':
    main()

