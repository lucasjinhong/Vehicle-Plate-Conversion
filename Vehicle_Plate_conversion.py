import sys

def main():
    plate = input('Enter the plate number (ex. 1234AD):')

    if plate[:1].isdigit():
        print(plate[4:] + plate[:4])
    else:
        print(plate[2:] + plate[:2])

if __name__ == "__main__":
    sys.exit(main())