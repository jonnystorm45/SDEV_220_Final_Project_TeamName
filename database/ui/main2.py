from tkinter import *
import databaseFunctions


fullName = ""
street = ""
city = ""
state = ""
emailAddress = ""
issueDescription = ""

root = Tk()
root.geometry('500x500')
root.title("Road Issue")

titleLabel = Label(root, text="Road Issue Form", width=20, font=("bold", 20))
titleLabel.place(x=90, y=53)

submitterLabel = Label(root, text="Full Name:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
submitterLabel.place(x=28, y=130)
submitterName = Entry(root)
submitterName.place(x=200, y=130, width=200)

streetLabel = Label(root, text="Street Address:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
streetLabel.place(x=28, y=180)
streetAddress = Entry(root)
streetAddress.place(x=200, y=180, width=200)

stateLabel = Label(root, text="City:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
stateLabel.place(x=28, y=230)
cityAddress = Entry(root)
cityAddress.place(x=200, y=230, width=150)

stateLabel = Label(root, text="State:", width=10, font=("bold", 10))
stateLabel.place(x=300, y=230)
stateAddress = Entry(root)
stateAddress.place(x=370, y=230, width=29)

emailLabel = Label(root, text="Email:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
emailLabel.place(x=28, y=280)
submitterEmail = Entry(root)
submitterEmail.place(x=200, y=280, width=200)

issueLabel = Label(root, text="Description of Road Issue:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
issueLabel.place(x=28, y=320)
submittedIssue = Entry(root)
submittedIssue.place(x=200, y=320, width=200)

#directionLabel = Label(root, text="Direction of Travel:", width=20, font=("bold", 10))
#directionLabel.place(x=70, y=230)

#var = IntVar()

#Radiobutton(root, text="N", padx=5, variable=var, value=1).place(x=235, y=230)
#Radiobutton(root, text="S", padx=5, variable=var, value=2).place(x=280, y=230)
#Radiobutton(root, text="E", padx=5, variable=var, value=3).place(x=325, y=230)
#Radiobutton(root, text="W", padx=5, variable=var, value=4).place(x=370, y=230)

Button(root, text='Submit', command=lambda: (openNewWindow()), width=20, bg='brown', fg='white').place(x=180, y=375)
Button(root, text='Admin Portal', width=20, bg='red', fg='white').place(x=180, y=425)


# it is use for display the registration form on the window

def submit():
    fullName = submitterName.get()
    street = streetAddress.get()
    city = cityAddress.get()
    state = stateAddress.get()
    emailAddress = submitterEmail.get()
    issueDescription = submittedIssue.get()
    databaseFunctions.createIssue(fullName, street, city, state, emailAddress, issueDescription)
    print("added to database")
    print(fullName, street, city, state, emailAddress, issueDescription)





def openNewWindow():
    submit()
    newWindow = Toplevel(root)
    newWindow.title("Issue Submitted")

    # define window geometry

    newWindow.geometry("1000x800")

    Label(newWindow,
          text="Your Issue has been submitted ... \n" + str(submitterName.get()) + "\n" + str(submitterEmail.get()) +"\n" + str(streetAddress.get()) + "\n" + str(submittedIssue.get())).place(x=425, y=250)
    Button(newWindow, text="Exit", command=newWindow.destroy).place(x=500, y=500)


root.mainloop()