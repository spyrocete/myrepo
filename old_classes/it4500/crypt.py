#This program will encrypt files and decrypt as well.
#By Andrew Coulter
#This command will below will clear terminal screen in windows, mac, and linux.
#os.system(['clear', 'cls' ][ os.name == 'nt' ])

import random
import os  #used for the terminal clear command

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypt_or_decrypt_choice=''


def main():
    main_menu()
    
def main_menu():
    menu_encrypt()

def menu_encrypt():
    flag=True
    while flag:
         print "type d for decrypt e to encrypt"
         choice=raw_input()
         Caesarian(choice, alphabet)
         os.system(['clear', 'cls' ][ os.name == 'nt' ])
         print "File operations complete"
         flag=False


def file_names():
    print "Type the name of the file you want to encrypt or decrypt"
    name=raw_input()
    fin = open(name, "rb")
 

    print "Type the new name of the file"
    outname=raw_input()
    fout = open(outname, "wb")


def Caesarian(encrypt_or_decrypt_choice, alphabet):
    # Determine the offset by generating a random number in the correct range.
    # This will be the same random number, if the password sent to random.seed is the same.
    print "Type the name of the file you want to encrypt or decrypt"
    name=raw_input()
    fin = open(name, "rb")
 
    print "Type the new name of the file"
    outname=raw_input()
    fout = open(outname, "wb")
 
    offset = 5
 
    if encrypt_or_decrypt_choice=='d':
        offset = -offset
        print "decrypting"
    print "Using the secret offset of", offset
    
    # Read every line of the input file.
    for line1 in fin:
        # Alter each character of the line1, putting the result into line2.
        line2 = ""
        for c in line1:
            up_c=c.upper()
            if up_c in alphabet:
                pos1 = alphabet.find(up_c)
                pos2 = (pos1+offset)%len(alphabet)
                line2 += alphabet[pos2]

        # Write each resulting line2 to the output file.
        fout.write(line2)

    fin.close()
    fout.close()
    
    print "Would you like to encrypt another file? Type y for yes and n for no"
    pick=raw_input()
    if pick=='y':
        menu_encrypt()
        
    else:
        exit()


def txt2lst(txt):
    lst=[]
    for char in txt:
        lst.append(char)
    return lst

def lst2txt(lst):
    txt=""
    for char in lst:
        txt=txt+char
    return txt


main()
