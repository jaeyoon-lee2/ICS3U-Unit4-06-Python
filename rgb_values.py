#!/user/bin/env python3

# Created by: Jaeyoon Lee
# Created on: Nov 2019
# This program prints out all the valid RGB values


def main():
    # this function prints out all the valid RGB values

    counterR = 0
    counterG = 0
    counterB = 0

    # process & output
    for counterR in range(256):
        for counterG in range(256):
            for counterB in range(256):
                print("RGB ({0},{1},{2})"
                      .format(counterR, counterG, counterB))


if __name__ == "__main__":
    main()
