def print_numbers(limit):
    """
    This function for print numbers
    """
    for i in range(limit):
        print(i)

def main():
    n = int(input('Enter limit for loop: '))
    print_numbers(n)

    print(print_numbers.__doc__)

# if __name__ == '__name__':
main()