from struct import pack,unpack
def encoding():
    count = int(input("Enter the size of posting list"))
    bitstream = []
    while count > 0:
        number = int(input('Enter a number to encode: '))
        bitstream.insert(0, number % 128)
        print(bitstream)
        if number < 128:
            break
        number = number // 128
    bitstream[-1] += 128

    count -= 1


def decoding():
    bytestring = int(input('Enter a bytestream to decode: '))
    print(type(bytestring))
    print(bytestring)


def main():
    print("""
    Welcome to VB Encoder/Decoder 
    [1] - VB Encoding
    [2] - VB Decoding
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
