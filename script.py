#!/usr/bin/env python3

# Author Yasir Ahmad

def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54

def main():
    print("Convert inches -> cm")
    print("Convert cm -> inches")
    selection = input("Make your selection (1,2): ")

    if selection == '1':
        inches = int(input("Enter inches: "))
        print(f"Number of cm: {inches_to_cm(inches)}")
    elif selection == '2':
        cm = int(input("Enter cm: "))
        print(f"Number of inches: {cm_to_inches(cm)}")
    else:
        print("Invalid entry")

if __name__ == "__main__":
    main()
