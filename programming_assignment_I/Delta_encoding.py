def encoding():
    count = int(input("Enter the size of posting list"))


def decoding():
    bytestring = int(input('Enter a bytestream to decode: '))


def main():
    print("""
    Welcome to Delta Encoder/Decoder 
    [1] - Delta Encoding
    [2] - Delta Decoding
    [3] - Exit
    """)

    action = input('What would you like to do? (Enter a option number). ')

    if action == '1':
        print(' Moving for Encoding')
        encoding()
    elif action == '2':
        print('Moving for Decoding')
        decoding()
        1
    elif action == '3':
        print('Terminating')
        exit()
    else:
        print('Please choose  the valid option')


main()
