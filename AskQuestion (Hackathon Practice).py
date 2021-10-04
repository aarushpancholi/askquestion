import tkinter as tk

root = tk.Tk()
root.title("Hackathon Practice")

root.geometry("500x400")

root["bg"] = "yellow"

space = tk.Label (root, text="\n", bg="yellow")
space.pack()
info = tk.Label(root, text="Please enter your name", bg = "white", fg ="black", font="Comicsans 30 bold")
info.pack()
space = tk.Label (root, text="\n", bg="yellow")
space.pack()
name = tk.Entry(root)
name.pack()

gotten = ""

def science():
    global ne
    global gotten
    def sq1():
        global ne
        global gotten
        answerbutton.pack_forget()
        answer = tk.Entry(sciencewid)
        answer.pack(side=tk.BOTTOM)
        def scienceanswered():
            global ne
            global gotten
            gotten = answer.get()
            postbutton.pack_forget()
            answer.pack_forget()
            answered = tk.Label(sciencewid, text=gotten,fg="black", font="Comicsans 30", bg = "white")
            answered.pack()
            namelabel = tk.Label(sciencewid, text=ne, fg="black", font="Comicsans 15", bg = "white")
            namelabel.pack()

        postbutton = tk.Button(sciencewid, text="Post", highlightbackground = "blue", fg="white", font="Comicsans 30", command = scienceanswered)
        postbutton.pack(side = tk.RIGHT)
        
    root.destroy()
    sciencewid = tk.Tk()
    sciencewid.title("science")
    sciencewid.geometry("500x400")
    sciencewid["bg"] = "yellow"
    q1 = tk.Label(sciencewid, text="I have a question! What are the parts of a leaf?", bg = "white", fg="black", font="Comicsans 20 bold")
    q1.pack()
    falsename = tk.Label(sciencewid, text="John Appleseed", bg = "white", fg="black", font="Comicsans 10")
    falsename.pack()
    answerbutton = tk.Button(sciencewid, text="Answer Question", highlightbackground = "blue", fg="white", font="Comicsans 15", command = sq1)
    answerbutton.pack()


    
def math():
    global ne
    global gotten
    def mathq1():
        global ne
        global gotten
        answerbutton.pack_forget()
        answer = tk.Entry(mathwid)
        answer.pack(side=tk.BOTTOM)
        def mathanswered():
            global ne
            global gotten
            gotten = answer.get()
            postbutton.pack_forget()
            answer.pack_forget()
            answered = tk.Label(mathwid, text=gotten,fg="black", font="Comicsans 30", bg = "white")
            answered.pack()
            namelabel = tk.Label(mathwid, text=ne, fg="black", font="Comicsans 15", bg = "white")
            namelabel.pack()

        postbutton = tk.Button(mathwid, text="Post", highlightbackground = "blue", fg="white", font="Comicsans 30", command = mathanswered)
        postbutton.pack(side = tk.RIGHT)
        
    root.destroy()
    mathwid = tk.Tk()
    mathwid.title("Math")
    mathwid.geometry("500x400")
    mathwid["bg"] = "yellow"
    q1 = tk.Label(mathwid, text="I have a question! What is the square root of 42?", bg = "white", fg="black", font="Comicsans 20 bold")
    q1.pack()
    falsename = tk.Label(mathwid, text="John Appleseed", bg = "white", fg="black", font="Comicsans 10")
    falsename.pack()
    answerbutton = tk.Button(mathwid, text="Answer Question", highlightbackground = "blue", fg="white", font="Comicsans 15", command = mathq1)
    answerbutton.pack()


ne = ""

def pressed():
    global ne
    ne = name.get()
    name.delete(0,100)
    info.pack_forget()
    enter.pack_forget()
    name.pack_forget()
    namelab = tk.Label(root,text=ne,bg = "white", fg ="black", font="Comicsans 30 bold")
    namelab.pack()
    space = tk.Label (root, text="\n", bg="yellow")
    space.pack()
    space = tk.Label (root, text="\n", bg="yellow")
    space.pack()
    categories = tk.Label(root, text="Choose category", bg = "white", fg ="blue", font="Comicsans 30 bold")
    categories.pack()
    space = tk.Label (root, text="\n", bg="yellow")
    space.pack()
    sciencelab = tk.Button(root, text="Science", highlightbackground = "black", fg ="white", font="Comicsans 30 bold", command = science)
    sciencelab.pack(side=tk.RIGHT)
    mathlab = tk.Button(root, text="Math", highlightbackground = "black", fg ="white", font="Comicsans 30 bold", command = math)
    mathlab.pack(side=tk.LEFT)


space = tk.Label (root, text="\n", bg="yellow")
space.pack()
    
enter = tk.Button(root, text="Enter", highlightbackground="blue", fg="black", font="Comicsans 30 bold", command = pressed)
enter.pack()
