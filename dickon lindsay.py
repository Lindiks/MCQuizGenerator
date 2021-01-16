#Lindsay Dickson
# 01 / 2018
#Final ISU


import sys
import random
from random import shuffle
import Tkinter as tk
from Tkinter import *
import tkMessageBox
from tkFileDialog import askopenfilename      
from Tkinter import StringVar

#___________________________________________________________________________________________________________________________

#This procedure will end the program
def ask_quit():
    sys.exit("You have quit")
    root.destroy    
#end ask_quit

#this function will allow the user to open a file
#RETURN : STRING : File path
def find_Answer():
    fileName = askopenfilename(parent=root, title='Choose your answer file', initialdir='C:\\')
    afile= open(fileName, 'r')
    return afile
#end find_Answer

#This procedure will call a function to obtain a file path and then add each line of text to a list
def Answer_Key():
    f=find_Answer()
    string=f.readline()
    while (string!=""):
        string=string.strip() # this will remove the ne line character from the string
        answerKey.append(string)
        string=f.readline()
        #end while string
#End Answer_key

#This procedure will calculate ones score 
# array : List : the users answers 
def correction(array):
    array = [item.lower() for item in array]
    
    for i in range(0,len(array),1):   
        if array[i]==answerKey[i]:
            print ("correct!")
        else:
            print "Incorrect"
    del answerKey[0:len(array)]
        #end if
    #end for 
#end correction 

#This function will prompt the user to provide the number of questions for each section 
#RETURN : INT : the number of questions 
def number_MC():
    master = Tk()
    Label(master, text="# of Questions (M/C): ").grid(row=1)      
    e2 = Entry(master)
    e2.grid(row=1, column=1)
    
    Button(master, text='Continue', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='QUIT', command=ask_quit).grid(row=3, column=1, sticky=W, pady=4) 
    master.mainloop()
    if e2!="-":
        v=int(e2.get())
        e2.delete(0,END)
        return v
    else:
        print ":("
    #end if 
#end number_MC

#This function will prompt the user to provide the number of questions for each section 
#RETURN : INT : the number of questions 
def number_SA():
    master = Tk()
    Label(master, text="# of Questions (Short Answer): ").grid(row=1)      
    e2 = Entry(master)
    e2.grid(row=1, column=1)
    
    Button(master, text='Continue', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='QUIT', command=ask_quit).grid(row=3, column=1, sticky=W, pady=4) 
    master.mainloop()
    if e2!="-":
        v=int(e2.get())
        e2.delete(0,END)
        return v
    else:
        print ":( what a mess"
        ask_quit
    #end if 
#end number_SA

#This function will prompt the user to provide the number of questions for each section 
#RETURN : INT : the number of questions 
def number_TF():
    master = Tk()
    Label(master, text="# of Questions (T/F): ").grid(row=1)      
    e2 = Entry(master)
    e2.grid(row=1, column=1)
    
    Button(master, text='Continue', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='QUIT', command=ask_quit).grid(row=3, column=1, sticky=W, pady=4) 
    master.mainloop()
    if e2!="-":
        v=int(e2.get())
        e2.delete(0,END)
        return v
    else:
        print ":("
    #end if 
#end number_TF

##This procedure will allow the user to create a file
##def create_file(array):
    ##f = open ("a mess.txt", 'w+')
    ##for i in range(0,total,1):
        ##f.write(array[i]+"\n")
    ###end for 
    ##f.close()  
##end create_file

#This function will allow the user to browse their files and open it
#RETURN : file name   
def find_file():
    fileName = askopenfilename(parent=root, title='Choose a file', initialdir='C:\\')   
    fi= open(fileName, 'r')
    nom.append(fileName)
    return fi
#end find_file

#this function will indicate a users selection
#RETURN : y : the value of the users selecttion
def testmulti():
    y=0
    y+=1
    return y
#end testmulti

#this function will indicate a users selection
#RETURN : y : the value of the users selecttion
def tf():
    y=0
    y+=1
    return y
#end testmulti

#this function will indicate a users selection
#RETURN : y : the value of the users selecttion
def shortAnswer():
    y=0
    y+=1
    return y    
#end shortAnswer

#This procedure will add the users selection to a list   
def ChoiceA():
    answersmulti.append(que[i])
#end ChoiceA

#This procedure will add the users selection to a list   
def ChoiceB():
    answersmulti.append(que[i])
#end ChoiceB

#This procedure will add the users selection to a list   
def ChoiceC():
    answersmulti.append(que[i]) 
#end ChoiceC

#This procedure will add the users selection to a list   
def ChoiceD():
    answersmulti.append(que[i])
#end ChoiceD

class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)
        #end for
    #end __init__
    def __getitem__(self, key):
        return self.vars[key].get()   
    #end __getitem__
    def state(self):
        return map((lambda var: var.get()), self.vars) 
    #end state


#This procedure will show the users input and save it to a list
def show_entry_fields():
    answers.append(e1.get())
    e1.delete(0,END)
#end show_entry_fields

#This procedure will show the users input and save it to a list
def true():
    answer_Q.append('True')  
#end false

#This procedure will show the users input and save it to a list    
def false():
    
    answer_Q.append('False')
#ned false

#___________________________________________________________________________________________________________________________

root = tk.Tk() #creates a window
master = Tk() #creates a window
master.withdraw()

x=0
McNum=0
ShortNum=0
TFNum=0
v = IntVar()
#___________________________________________________________________________________________________________________________


#___________________________________________________________________________________________________________________________


nom=[]    
question=[]
functionList=[testmulti(), shortAnswer(), tf()]
que=[]
answersmulti=[]
answers=[]
answer_Q=[]
answerKey=[]

##___________________________________________________________________________________________________________________________
##_____________________________Checkbox widget (M/c,shortanswer,t/f)________________________________________________

if __name__ == '__main__':
    
    lng = Checkbar(root, ['Multiple Choice', 'Short Answer', 'True/False'])
    lng.pack(side=TOP,  fill=X)
    lng.config(relief=GROOVE, bd=2)
#end if

Button(root, text='Quit', command=ask_quit).pack(side=RIGHT)
Button(root, text='Continue', command=root.quit).pack(side=RIGHT)

root.mainloop()

for i in range(0,3,1):
    if lng[i]>0:
        x+= functionList[i]   
    else:
        pass
    #end if 
#end for i


##___________________________________________________________________________________________________________________________
while x>0:
    
    errmsg = 'Error!'
    Button(text='Browse Files', command=root.quit).pack(fill=X)
    Button(text='Continue', command=root.quit).pack(fill=X)
    Button(text='Quit', command=ask_quit).pack(fill=X)
    
    root.mainloop()
    
    
    f=find_file()
    string=f.readline()
    while (string!=""):
        string=string.strip() # this will remove the ne line character from the string
        question.append(string)
        string=f.readline()
    f.close()
    root.mainloop()
    
    
    errmsg = 'Error!'
    Button(text='Browse Files', command=root.quit).pack(fill=X)
    Button(text='Continue', command=root.quit).pack(fill=X)
    Button(text='Quit', command=ask_quit).pack(fill=X)
    
    root.mainloop()
    
    Answer_Key()
    root.mainloop()
    x-=1    
    #end while 
#end while 

#while x>0:
##___________________________________________________________________________________________________________________________
##___________________________________________________________________________________________________________________________
if lng[0]>0:
    McNum=number_MC()
    #Answer_Key()
    for i in range(0,McNum,1):
        que.append(answerKey[i])
    #end for i
   
    for i in range(0,McNum,1):
        master = Tk()
        l1= tk.Label(master, text=question[i], justify = tk.LEFT, padx = 20).grid(row=0)
        f1=tk.Frame(master)
        ##Labels
        tk.Label(master, text=que[i], justify = tk.LEFT, padx = 20).grid(row=1, column=1)
        tk.Label(master, text=que[i], justify = tk.LEFT, padx = 20).grid(row=2, column=1)
        tk.Label(master, text=que[i], justify = tk.LEFT, padx = 20).grid(row=3, column=1)
        tk.Label(master, text=que[i], justify = tk.LEFT, padx = 20).grid(row=4, column=1)
    
        ##Radio buttons 
        Radiobutton(master, text="a", padx = 20, variable=v, value=1, command=ChoiceA).grid(row=1, column=0, sticky=W, pady=4)
        Radiobutton(master, text="b", padx = 20, variable=v, value=2, command=ChoiceB).grid(row=2, column=0, sticky=W, pady=4)
        Radiobutton(master, text="c", padx = 20, variable=v, value=3, command=ChoiceC).grid(row=3, column=0, sticky=W, pady=4)
        Radiobutton(master, text="d", padx = 20, variable=v, value=4, command=ChoiceD).grid(row=4, column=0, sticky=W, pady=4)
        Button(master, text="Continue", command=master.quit).grid(row=5, column=1, sticky=E, pady=4, padx=4)
        Button(master, text="Quit", command=ask_quit).grid(row=5, column=0, sticky=W, pady=4, padx=4)
        
        master.mainloop()
    #end for    
    
    #print answersmulti
    #answerKey = [item.lower() for item in answerKey]
    correction(answersmulti)
    
    del question[0:McNum]
    
#end if
##___________________________________________________________________________________________________________________________
##___________________________________________________________________________________________________________________________
        
if lng[1]>0:   
    ShortNum=number_SA()  
    for i in range(0,ShortNum,1):
            master = Tk()
            Label(master, text=question[i]).grid(row=1)      
            e1 = Entry(master)
            e1.grid(row=1, column=1)
            Button(master, text='Continue', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
            Button(master, text='QUIT', command=ask_quit).grid(row=3, column=1, sticky=W, pady=4) 
                
            master.mainloop()
            
            show_entry_fields()
    #end for     

            
    
    #print answers
    #Answer_Key()
    answerKey = [item.lower() for item in answerKey]
    correction(answers)
    del question[0:McNum]

#end if
##___________________________________________________________________________________________________________________________
##___________________________________________________________________________________________________________________________

if lng[2]>0:
    TFNum=number_TF()

    for i in range(0,TFNum,1):
        master = Tk()
        l1= tk.Label(master, text=question[i], justify = tk.LEFT, padx = 20).pack()
        f1=tk.Frame(master)
        Radiobutton(master, text="True", padx = 20, variable=v, value=1, command=true).pack(anchor=tk.W)
        Radiobutton(master, text="False", padx = 20, variable=v, value=2, command=false).pack(anchor=tk.W)
        Button(master, text="Continue", command=master.quit).pack(fill=X)
        Button(master, text="Quit", command=ask_quit).pack(fill=X)
        master.mainloop()

        
    
           
    #Answer_Key()
    #answerKey = [item.lower() for item in answerKey]
    correction(answer_Q)

