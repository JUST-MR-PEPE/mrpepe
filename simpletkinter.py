from tkinter import*
from socket import*
def getip():
    link = entry.get()
    host = gethostbyname(link)
    entry.delete(0, 'end')
    entry.insert(0,host)

win = Tk()
label = Label(win,text="get ip")
entry = Entry(win,text="")
button = Button(win,text="getip",command=getip) 
label.pack()
entry.pack()
button.pack()
win.mainloop()
