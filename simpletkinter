from tkinter import*
from socket import*
def getip():
    link = entry.get()
    host = gethostbyname(link)
    #label2.configure(text="ip:"+host)
    entry.delete(0, 'end')
    #entry.configure(text="ip:"+host)
    insert(0, "a default value")



win = Tk()
label = Label(win,text="get ip")
entry = Entry(win,text="")
button = Button(win,text="getip",command=getip) 
label2 = Label(win,text="")
label.pack()
entry.pack()
label2.pack()
button.pack()
win.mainloop()
