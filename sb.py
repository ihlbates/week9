# Isaiah Bates
# Week 9
# directories

import os


def main():
    print(os.getcwd())

    file = input('What would you like to name your file? ', )
    directory = input("Enter the directory that you want to save the file: ")

    name = input('Please input your name: ', )
    phone = input('Please input your phone number: ', )
    address = input('Please enter your address: ', )

    if os.path.isdir(directory):

        writefile = open(os.path.join(directory, file), 'w')
        writefile.write(name + ',' + address + ',' + phone + '\n')
        writefile.close()

        #
        print('Please review your information to ensure it is correct.')
        print(f'Your name: ',name)
        print(f'Your phone: ',phone)
        print(f'Your address: ',address)

        readfile = open(os.path.join(directory, file), 'r')
        for line in readfile:
            print('Your information has been saved.')

        readfile.close()

    else:
        print(f'Error: {directory} does not exist. ')



main()