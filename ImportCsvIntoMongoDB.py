
# coding: utf-8

# In[41]:

#Simple App following tutorial at:
#http://effbot.org/tkinterbook/tkinter-dialog-windows.htm
#File Dialogue following tutorial at:
#https://en.wikibooks.org/wiki/Python_Programming/Tkinter#File_dialog
import tkinter as tk
#from tkinter import filedialog
from tkinter.filedialog import askdirectory
from os import path
import csv2mongo_win as c2m

class App:
    
    def __init__(self,master):
        self.dir_path=tk.StringVar()
        # container
        frame=tk.Frame(master)
        frame.pack()
        # author text box
        self.label=tk.Label(frame,text="Author").pack(side=tk.TOP)
        self.author_txt=tk.Entry(frame)
        self.author_txt.pack(side=tk.TOP)
        # experiment text box
        self.label=tk.Label(frame,text="Experiment").pack(side=tk.TOP)
        self.experiment_txt=tk.Entry(frame)
        self.experiment_txt.pack(side=tk.TOP)
        # experiment text box
        self.label=tk.Label(frame,text="Date").pack(side=tk.TOP)
        self.date_txt=tk.Entry(frame)
        self.date_txt.pack(side=tk.TOP)
        # Folder text box
        self.label=tk.Label(frame,text="Folder").pack(side=tk.TOP)
        self.dir_path_txt=tk.Entry(frame,textvariable=self.dir_path)
        self.dir_path_txt.pack(side=tk.TOP)
        # a select Folder button
        self.button=tk.Button(frame,text="Browse", command=self.browse)
        self.button.pack(side=tk.TOP) 
        # Submit button
        self.button=tk.Button(frame,text="Submit", command=self.check_input)
        self.button.pack(side=tk.LEFT)
        # Exit button
        self.button=tk.Button(frame,text="EXIT",fg="red",command=frame.quit)
        self.button.pack(side=tk.RIGHT)       
    
    def check_input(self):
#        print(self.author_txt.get())
#        print(self.experiment_txt.get())
#        print(self.dir_path.get())
        collection_name_parts = [self.author_txt.get() ,self.experiment_txt.get() , self.date_txt.get()]
        c2m.import_csv(directory= self.dir_path.get() , db_name=self.author_txt.get() ,collection_name= "-".join(collection_name_parts) )
    

    def browse(self):
        raw_dir = askdirectory()
        if raw_dir != "":
            clean_dir_path=path.abspath(raw_dir)
            self.dir_path.set(clean_dir_path)

#window        
root=tk.Tk()
#Set app title and logo and size
root.title("CSV 2 MongoDB")
root.wm_iconbitmap("UoD.ico")
root.geometry("250x300+30+30")
#an instance of the app with the window (root widget)
app=App(root)
#Keep running until the window or the frame is closed
root.mainloop()
#Something extra
root.destroy()


# In[ ]:



