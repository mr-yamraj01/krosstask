from Tkinter import *
window = Tk()
name = StringVar()
vote2 = IntVar()
def print_the_vote() :
	uname = StringVar() 
	shovan = IntVar()
	shovan = vote1.get()
	kartik = IntVar()
	kartik = vote2.get()
	uname = name.get()
	vote = Label(window, text = "%s"%(uname))
	vote.grid(column = 2)

	if (shovan == 1 & kartik != 1):
		voting = Label (window , text = "Shovan for vp")
		voting.grid(column = 2)
	elif (shovan != 1 & kartik == 1):
		voting1 = Label (window , text = "Kartik for vp")
		voting1.grid(column = 2)
	elif (shovan == 1 & kartik == 1):
		voting2 = Label (window , text = "Please be fair in voting")
		voting2.grid(column = 2)
	elif (shovan != 1 & kartik != 1):
		voting3 = Label (window , text = "dont you trust any candidate")
		voting3.grid(column = 2)
username = Label(window, text = 'username')
entry = Entry(window ,bd = 5, textvariable = name)
username.grid(column = 2, row = 2 )
entry.grid(column = 3 , row = 2)
question = StringVar()
que = Label(window , textvariable = question , relief = RAISED)
question.set("Hey! whom do you want to vote for vp.")
que.grid(column = 2,row = 3,columnspan = 2)
vp1 = Checkbutton(window, text = "Shovan Panigari",variable = vote1, \
		onvalue = 1,offvalue = 2)
vp1.grid(column = 2 , row = 4, rowspan = 2)

vp2 = Checkbutton(window, text = "Kartik Gupta",variable = vote2, \
		onvalue = 1,offvalue = 2)

vp2.grid(column = 3 , row = 4, rowspan = 2)
submit = Button(window, text = 'submit' , command = print_the_vote )
submit.grid(column = 2 ,row = 6)
window.mainloop()
