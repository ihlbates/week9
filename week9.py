# Isaiah Bates
# Week 9
# directories

import os


def main():
    print(os.getcwd())

    file = input('What would you like to name your file?', )
    directory = input("Enter the directory that you want to save the file : ")

    name = input('Please input your name.', )
    phone = input('Please input your phone number', )
    address = input('Please enter your address', )

    if os.path.isdir(directory):

        writeFile = open(os.path.join(directory, file), 'w')
        writeFile.write(name + ',' + address + ',' + phone + '\n')
        writeFile.close()

        name = input('Please input your name.', )
        phone = input('Please input your phone number', )
        address = input('Please enter your address', )

        #

        outfile = open(file, 'w')

        print(f' {name}, {phone}, {address}, file=outfile')
        outfile.close()
        #
        infile = open(file, 'r')

        print(f'Your name:')
        print(f'Your phone:')
        print(f'Your address:')
        infile.close()

    else:
        print(f'Error: {directory} does not exist. ')

    print(name, phone, address)


main()
