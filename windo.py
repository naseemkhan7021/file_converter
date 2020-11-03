# import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import os
import re
import Controller
### ************ all command hare  ************* ###
# to exit forme the app


def openfile():
    print('hellow this openfile function')
    global urlOpen
    urlOpen = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', file=((
        ('all file', '*.*'), ("Text Documents", "*.txt"))))  # open file explorer ussing filedialog
    file.set(os.path.basename(urlOpen))  # show the file in entery element
    # newFile.set
# Controller.textTopdf()


def fetch():
    global urlSave
    print('convert started')
    fileSplite = file.get().split('.')
    fileSplite[1] = extensions.get()
    newFile = '.'.join(fileSplite)
    urlSave = filedialog.asksaveasfile(title='Save -'+newFile, defaultextension='.'+fileSplite[1], file=((
        ('all file', '*.*'), ("Text Documents", "*.txt"))))

    urlSave.close()  # close the file becose only creating the file
    # copy path
    copyurl = urlSave
    name,ext = os.path.splitext(file.get())
    print('fileSplite[1] = pdf ' ,fileSplite[1] )
    # the following try exept will go to controller file
    if ext not in [".jpg", ".jpeg",".png" ,".mp3",".mp4"] and fileSplite[1] in ["pdf"]:
        info = Controller.txtTopdfConvert(urlOpen, copyurl.name)
        if info == True:
            # show massage if success to make pdf 
            messagebox.showinfo(title='Success',message='Success to make pdf file')
            # show the new file path to user 
            newpath.set(copyurl.name)
        
        else:
            # show error in fail to make pdf
            messagebox.showerror(title='Error',message=info)

    elif ext in ['.png','.jpeg','.jpg'] and fileSplite[1] in ["pdf"]:  # regular express true or false to checking the extensions
        info = Controller.imgTopdf(urlOpen, copyurl.name)
        if info == True:
            # show massage if success to make pdf 
            messagebox.showinfo(title='success',message='success to make pdf file')
            # show the new file path to user 
            newpath.set(copyurl.name)
        else:
            # show error in fail to make pdf 
            messagebox.showerror(title='Error', message=info)
    elif ext in ['.pdf'] and fileSplite[1] in ["jpg","jpeg"]:
        # print('this is pdf to img file')
        info = Controller.pdfToImg(copyurl.name,urlOpen)
        if info == True:
            # show massage if success to make img file
            messagebox.showinfo(title='Success',message='Success to make image file')
            # show the new file path to user 
            newpath.set(copyurl.name)
        else:
            #show error in fail to make image file
            messagebox.showerror(title='Error',message='Please try another pdf file !!')
        
    elif ext in ['.pdf'] and fileSplite[1] in ['txt']:
        print('hellow')
        info = Controller.pdfTotxt(urlOpen,copyurl.name)
        if info == True:
            # show message if success to make text file
            messagebox.showinfo(title='Success',message='Success to make text file')
            # show the new file path to user 
            newpath.set(copyurl.name)
        else:
            # show error if fail to make text file
            messagebox.showerror(title='Error',message='Please try another file !!')
    else:
        # show error if extensions not found 
        messagebox.showinfo(title='info', message='please try again')


# main window configration
root = Tk()
root.geometry('500x600')
root.config(bg='white')
root.title('File Converter')

# tittle of  application
title = Label(root, text='This Is Text Center', justify='center',
              bg='white', width=30, font=('Serif', 20))

''' hare is selected file show '''
# now to select file by user
Label(root, text='select file :', bg='white', font=(
    'Serif', 10)).place(x=10, y=50)  # here is label
Button(root, text='Browse', borderwidth=0, command=openfile).place(
    x=150, y=50)  # here is browse button

# the Entry element is show the selected file 
# making the string variable for storing the values
file = StringVar()
filePath = Entry(root, borderwidth=1, textvariable=file, width=30,
                 font=('Serif', 10))  # here is entry configrations
filePath.insert(0, 'selected file')
filePath.place(x=195, y=50)
 
''' hare is choose the new file extension '''
# now here is select extension converter
Label(root, text='select Extension :', bg='white', font=(
    'Serif', 10)).place(x=10, y=80)  # here is label
extensions = ttk.Combobox(root)
extensions['value'] = ['pdf', 'jpg', 'jpeg', 'mp3', 'mp4','txt' ]
extensions.config(width=39)
extensions.current(1)
extensions.place(x=150, y=80)


''' new path sections lable and Entry element '''
# now here is converted file path show
Label(root, text='This is file Path :', bg='white',
      font=('Serif', 10)).place(x=10, y=110)

# hare show the new genrated file path 
newpath = StringVar()
newfilePath = Entry(root, borderwidth=1, textvariable=newpath, width=36,
                 font=('Serif', 10))  # here is entry configrations
newfilePath.insert(0, 'new file')
newfilePath.place(x=150, y=110)

''' hare is butto close and conver Button '''
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
