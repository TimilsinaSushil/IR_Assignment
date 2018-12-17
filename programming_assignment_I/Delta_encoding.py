def binary(number):
    binr = []
    while number > 0:
        binr.append(number % 2)
        number = number // 2
    binr.reverse()
    return binr


def gamma(binary_array):
    binary_array.pop(0)
    offset_length = len(binary_array)
    unary = []
    while offset_length > 0:
        unary.append(1)
        offset_length -= 1
    unary.append(0)
    gamma = unary + binary_array
    return gamma


def encoding():
    num = int(input("Enter the decimal to encode"))
    binum = binary(num)
    binum.pop(0)
    offset_length = len(binum)
    offset_length_binary = binary(offset_length)
    print(offset_length_binary)
    delta_encoded = gamma(offset_length_binary)
    print(delta_encoded)


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
    elif action == '3':
        print('Terminating')
        exit()
    else:
        print('Please choose  the valid option')


main()
