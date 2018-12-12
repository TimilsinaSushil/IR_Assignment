def binary(number):
    binr = ''
    while number > 0:
        div = number % 2
        number = number // 2
        binr = binr + str(div)
    return binr


def encoding():
    number = int(input("Enter a number to encode: "))
    vb = ''
    count = 0
    while number > 0:
        count += 1
        print(count)
        div = number % 2
        number = number // 2
        vb = vb + str(div)
        if count == 7:
            vb = vb + str(1)
            count = 0
    while count < 8:
        count += 1
        vb = vb + str(0)
    return vb[::-1]


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
        vb = encoding()
        print(vb)
    elif action == '2':
        print('Moving for Decoding')
        decoding()

    elif action == '3':
        print('Terminating')
        exit()
    else:
        print('Please choose  the valid option')


main()
