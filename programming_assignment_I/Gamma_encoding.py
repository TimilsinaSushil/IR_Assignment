def binary(number):
    binr = []
    while number > 0:
        binr.append(number % 2)
        number = number // 2
    binr.reverse()
    return binr


def encoding():
    num = int(input("Enter the decimal to encode"))
    binum = binary(num)
    # offset
    binum.pop(0)
    offset_length = len(binum)
    # print(offset_length)
    unary = []
    while offset_length > 0:
        unary.append(1)
        offset_length -= 1
    unary.append(0)
    gamma = unary + binum
    return gamma


def decoding():
    bytestring = int(input('Enter a bytestream to decode: '))


def main():
    print("""
    Welcome to Gamma Encoder/Decoder 
    [1] - Gamma Encoding
    [2] - Gamma Decoding
    [3] - Exit
    """)

    action = input('What would you like to do? (Enter a option number). ')

    if action == '1':
        print(' Moving for Encoding')
        gamma = encoding()
        print(gamma)
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
