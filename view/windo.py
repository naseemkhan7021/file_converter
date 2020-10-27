# import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import os
import txtTopdf
### ************ all command hare  ************* ###
# to exit forme the app
'''
def exitB():
    root.destroy()
'''


def openfile():
    print('hellow this openfile function')
    global urlOpen
    urlOpen = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', file=((
        ('all file', '*.*'), ("Text Documents", "*.txt"))))  # open file explorer ussing filedialog
    file.set(os.path.basename(urlOpen))  # show the file in entery element
# txtTopdf.textTopdf()


def fetch():
    global urlSave
    print('convert started')
    fileSplite = file.get().split('.')
    fileSplite[1] = extensions.get()
    newFile = '.'.join(fileSplite)
    urlSave = filedialog.asksaveasfile(
        mode='wb', title='Save -'+newFile, defaultextension='.'+fileSplite[1], file=((
            ('all file', '*.*'), ("Text Documents", "*.txt"))))
    # print(urlSave)
    with open(urlOpen, 'rb') as rfile:
        data = rfile.read()
        # print(type(data))
        # print(type(str(data)))
    txtTopdf.txtTopdfConvert(data, urlSave)


# main window configration
root = Tk()
root.geometry('500x600')
root.config(bg='white')
root.title('File Converter')

# tittle of  application
title = Label(root, text='This Is Text Center', justify='center',
              bg='white', width=30, font=('Serif', 20))

# now to select file by user
Label(root, text='select file :', bg='white', font=(
    'Serif', 10)).place(x=10, y=50)  # here is label
Button(root, text='Browse', borderwidth=0, command=openfile).place(
    x=150, y=50)  # here is browse button configrations
file = StringVar()
filePath = Entry(root, textvariable=file, width=30, borderwidth=2,
                 font=('Serif', 10))  # here is entry configrations
filePath.insert(0, 'selected file')
filePath.place(x=195, y=50)

# now here is select extension converter
Label(root, text='select Extension :', bg='white', font=(
    'Serif', 10)).place(x=10, y=80)  # here is label
extensions = ttk.Combobox(root)
extensions['value'] = ['pdf', 'jpg', 'jpeg', 'mp3', 'mp4', ]
extensions.config(width=39)
extensions.current(1)
extensions.place(x=150, y=80)

# now here is converted file path show
Label(root, text='This is file Path :', bg='white',
      font=('Serif', 10)).place(x=10, y=110)
# for the Convertions submition
convertButton = Button(root, text='Convert', bg='red', justify='left', fg='white',
                       font=('Serif', 13), command=fetch)
convertButton.config(padx=30, pady=2)
convertButton.place(x=100, y=400)


# for the exit form the app
exitButton = Button(root, text='Close', bg='red', justify='right', fg='white',
                    font=('Serif', 13), command=root.destroy)
exitButton.config(padx=30, pady=2)
exitButton.place(x=300, y=400)


# can = Canvas(root, bg='red', height=100, width=100)
# can.place(relx=0.5, rely=0.5, anchor=CENTER)

# close the window commad
root.mainloop()
