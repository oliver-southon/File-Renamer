import os
import PySimpleGUI as sg 

path = input("Enter path of foler: ")
new_name = input("Rewrite the original file path with the new file name")

def RenameImage(path, new_name):
    os.rename(path, new_name)

RenameImage(path, new_name)