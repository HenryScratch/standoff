import os


def main():
    png_files = [i for i in os.listdir() if '.' in i and i.split('.')[1] == 'png']
    for file in png_files:
        os.rename(file, file.replace(' ', '_'))


if __name__ == '__main__':
    main()
