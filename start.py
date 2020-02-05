import os
import PySimpleGUI as sg 

folder = input("Enter path of folder: ")
file_type = input("Enter type of files in that folder (.jpg, .png, etc): ")

def main(folder, file_type):

    i=1
    for filename in os.listdir(folder):
        src = folder + "\\" + filename
        new_src = folder + "\\" + str(i) + file_type
        os.rename(src, new_src)
        i = int(i)
        i += 1


main(folder, file_type)