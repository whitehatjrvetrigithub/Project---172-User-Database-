from tkinter import *
root = Tk()

root.title("Inheritance")
root.geometry("600x600")

lbl_name = Label(root, text = "User Name :")
lbl_name.place(relx = 0.3, rely = 0.2, anchor = CENTER)

entry_name = Entry(root)
entry_name.place(relx = 0.6, rely = 0.2, anchor = CENTER)

lbl_email = Label(root, text = "Email id :")
lbl_email.place(relx = 0.3, rely = 0.3, anchor = CENTER)

entry_email = Entry(root)
entry_email.place(relx = 0.6, rely = 0.3, anchor = CENTER)

lbl = Label(root)

dictionary = {}

class Users: 
    
    def addUser(key, value): 
        global dictionary
        dictionary[key] = value
        lbl["text"] = dictionary

class GetUsers(Users): 
        
    def getUser(self):
        un = entry_name.get()
        ei = entry_email.get()
        Users.addUser(un, ei)

user = GetUsers()

btn = Button(root, text="Add User Details", command = user.getUser)
btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)

lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()