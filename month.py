#!usr/bin/env python3
# Created By: Marli Peters
# Date: Oct. 30, 2023
# This program asks the user for a number displays
# the corresponding month.


def main():
    # get user month number
    month = int(input("Enter month number as integer: "))
    print("")

    # display month for number
    match month:
        case 1:
            print("{} is January!".format(month))
        case 2:
            print("{} is February!".format(month))
        case 3:
            print("{} is March!".format(month))
        case 4:
            print("{} is April!".format(month))
        case 5:
            print("{} is May!".format(month))
        case 6:
            print("{} is June!".format(month))
        case 7:
            print("{} is July!".format(month))
        case 8:
            print("{} is August!".format(month))
        case 9:
            print("{} is September!".format(month))
        case 10:
            print("{} is October!".format(month))
        case 11:
            print("{} is November!".format(month))
        case 12:
            print("{} is December!".format(month))


if __name__ == "__main__":
    main()
