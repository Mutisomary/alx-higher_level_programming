#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]  # Exclude the script name from the arguments
    num_arguments = len(arguments)
    if num_arguments == 0:
        print("0 arguments.")
    else:
        print(f"{num_arguments} {'argument' if num_arguments == 1 else 'arguments'}:")
        for i, arg in enumerate(arguments):
            print(f"{i + 1}: {arg}")
