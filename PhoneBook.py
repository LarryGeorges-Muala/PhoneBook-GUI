#App Name: PhoneBook Contacts
#Python Version 3.5
#Developper: Larry Georges Muala

import tkinter
from tkinter import messagebox
import collections

#instantiate the window
window = tkinter.Tk()

#name the window
window.title('Contact List')

#resize the window
window.geometry("200x470")

#disable maximize
window.resizable(0,0)

#set background color
window.configure(background="midnight blue")

#modify window icon
#window.wm_iconbitmap('lelu.ico')


#menu Bar

def about_app():
	print("App Name: PhoneBook Contacts")
	print("App Description: Contacts List with search, view, edit, delete and add options")
	print("Python Version 3.5")
	print("Developper: Larry Georges Muala")
	
	messagebox.showinfo("App Info", "App Name: PhoneBook Contacts\n" + 
						"\nApp description:  Contacts List with search, view, edit, delete and add options\n" + 
						"\nPython Version 3.5 \n" + 
						"\nDevelopper: Larry Georges Muala")

menubar = tkinter.Menu(window)
myMenu = tkinter.Menu(menubar, tearoff=0)
myMenu.add_command(label="About", command=about_app)
myMenu.add_separator()
myMenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="App Info", menu=myMenu)

#display the menu
window.config(menu=menubar)


#contact names
contacts = ['Kirikou', 'Carmen Luna', 'Marisol', 'Vandal Savage', 'Sherara', 'Pablo Escobar', 'Effe', 'Gustavo', 'James St Patrick'
			,'Rip Hunter', 'Cataleya', 'Aladeen', 'Lorem Ipsum', 'Emma', 'Con SkyCrew', 'Con TreeCrew', 'Con Azgeda', 'Audrey', 'Noah', 'Murphy', 'Jaha']

#contact numbers
contacts_numbers = ['k_000000001', 'c_000000002', 'm_000000003', 'v_000000004','s_000000005', 'p_000000006', 'e_000000007', 'g_000000008', 'j_000000009', 'r_000000010',
					 'c_000000011', 'a_000000012', 'l_000000013', 'e_000000014', 'c_000000015', 'c_000000016', 'c_000000017', 'a_000000018', 'n_000000019', 'm_000000020', 'j_000000021']


#sorting both lists					 
contacts.sort()
contacts_numbers.sort()


#Application header text
lbl_main = tkinter.Label(window, text="Contact List: ", font=("Helvetica", 20), bg="gray1", fg="white")
lbl_main.pack(fill=tkinter.X)

#blank label to create a gap of space
lbl_blank = tkinter.Label(window, text=" ", bg="midnight blue")
lbl_blank.pack()


#function Search Contacts
def ctc_search(*args):
	
	var = search_box.get()
	var_ctc = search_box.get()
	count = 0
			
	for x in contacts:
	
		var = var.lower()
		var_ctc = var_ctc.lower()
		x = x.lower()
		y = x.split()
		
		#counter value to generate the index number of the value found		
		count += 1
		
		if var_ctc == x:
			listNumbers.selection_clear(0, tkinter.END)
			listNumbers.select_set(count - 1)
			listNumbers.see(count - 1)
			
		if var in y:
			print(True)
			print(var)
			listNumbers.selection_clear(0, tkinter.END)
			listNumbers.select_set(count - 1)
			listNumbers.see(count - 1)
				
		else:
			print(False)
			search_box.delete(0, tkinter.END)

			
#bind function Search Contacts to button Enter		
window.bind("<Return>", ctc_search)


#creating search box and description label
search_box = tkinter.Entry(window)
btn_search = tkinter.Button(window, text="Search", command=ctc_search)
search_box.pack()
search_box.focus()
btn_search.pack()

#blank label for space separator
lbl_blank = tkinter.Label(window, text=" ", bg="midnight blue")
lbl_blank.pack()


#creating scroll bar
Scrolls = tkinter.Scrollbar(window)
Scrolls.pack(side=tkinter.RIGHT,fill=tkinter.Y)

#creating listbox
listNumbers = tkinter.Listbox(window, height=12, yscrollcommand=Scrolls.set)
listNumbers.pack()

#loop to generate listbox items
for item in contacts:
    listNumbers.insert(tkinter.END, item)

#attaching the scroll bar to the listbox
Scrolls.configure(command=listNumbers.yview)


#blank label for space separator
lbl_blank = tkinter.Label(window, text=" ", bg="midnight blue")
lbl_blank.pack()


#Add contact function
def add_ctc():
	#toplevel to create pop up window
	toplevel = tkinter.Toplevel()
	toplevel.resizable(0,0)
	toplevel.configure(background="beige")
	#toplevel.wm_iconbitmap('lelu.ico')
	
	label1 = tkinter.Label(toplevel, text="Add New Contact", font=("Helvetica", 20), bg="gray1", fg="white")
	label1.pack()
	
	lbl_top_name = tkinter.Label(toplevel, text="Name: ")
	lbl_top_name.pack()
	
	ent_top_name = tkinter.Entry(toplevel)
	ent_top_name.pack()
	ent_top_name.focus()
	
	lbl_top_number = tkinter.Label(toplevel, text="Number: ")
	lbl_top_number.pack()
	
	ent_top_number = tkinter.Entry(toplevel)
	ent_top_number.pack()
	
	def save_ctc():
		var_save = ent_top_name.get()
		var_save_1 = var_save[:1]
		var_save_1 = var_save_1.upper()
		var_save_2 = var_save[1:]
		var_save = var_save_1 + var_save_2
		contacts.append(var_save)
		
		var_save_num = ent_top_number.get()
		contacts_numbers.append(var_save.lower()[:1] + "_" + var_save_num)
		
		print(contacts)
		print("$$$$$$$$$$$$$$$$$$")
		print(contacts_numbers)
		#
		contacts.sort()
		contacts_numbers.sort()
		
		listNumbers.delete(0,tkinter.END)
		
		for item in contacts:
			listNumbers.insert(tkinter.END, item)
		
		toplevel.destroy()
		
	btn_save = tkinter.Button(toplevel, text="Save", command=save_ctc)
	btn_save.pack()

	
#View contacts function when double-clicking listbox entry
def view_ctc(event):
	selection = listNumbers.curselection()
	selection = selection[0]
	var_select = contacts[selection]
	var_select_num = contacts_numbers[selection]
	
	#pop up message box
	messagebox.showinfo("Contact Details", "Contact Name is " + var_select + "\nContact Number is " + var_select_num[2:])

	
#View contacts function when clicking view button	
def view_ctc_btn():
	selection = listNumbers.curselection()
	selection = selection[0]
	var_select = contacts[selection]
	var_select_num = contacts_numbers[selection]
	
	#pop up message box
	messagebox.showinfo("Contact Details", "Contact Name is " + var_select + "\nContact Number is " + var_select_num[2:])


#Delete contacts function
def delete_ctc():
		selection = listNumbers.curselection()
		selection = selection[0]

		del contacts[selection]
		del contacts_numbers[selection]
		
		contacts.sort()
		contacts_numbers.sort()
		
		listNumbers.delete(0,tkinter.END)
		
		for item in contacts:
			listNumbers.insert(tkinter.END, item)


#Edit contacts function
def edit_ctc():
		selection = listNumbers.curselection()
		selection = selection[0]
		
		#toplevel pop up window
		toplevel = tkinter.Toplevel()
		toplevel.resizable(0,0)
		toplevel.configure(background="beige")
		#toplevel.wm_iconbitmap('lelu.ico')

		label1 = tkinter.Label(toplevel, text="Edit Contact", font=("Helvetica", 20), bg="gray1", fg="white")
		label1.pack()
		
		lbl_top_name = tkinter.Label(toplevel, text="Name: ")
		lbl_top_name.pack()
		
		ent_top_name = tkinter.Entry(toplevel)
		ent_top_name.insert(0, contacts[selection])
		ent_top_name.pack()
		ent_top_name.focus()
		
		lbl_top_number = tkinter.Label(toplevel, text="Number: ")
		lbl_top_number.pack()
		
		ent_top_number = tkinter.Entry(toplevel)
		ent_top_number.insert(0, contacts_numbers[selection][2:])
		ent_top_number.pack()
		
		
		def save_from_edit_ctc():
			del contacts[selection]
			del contacts_numbers[selection]
			
			var_save = ent_top_name.get()
			var_save_1 = var_save[:1]
			var_save_1 = var_save_1.upper()
			var_save_2 = var_save[1:]
			var_save = var_save_1 + var_save_2
			contacts.append(var_save)
			
			var_save_num = ent_top_number.get()
			contacts_numbers.append(var_save.lower()[:1] + "_" + var_save_num)
			
			contacts.sort()
			contacts_numbers.sort()
			#
			print(contacts)
			print("$$$$$$$$$$$$$$$$$$")
			print(contacts_numbers)
			#

			
			listNumbers.delete(0,tkinter.END)
			
			for item in contacts:
				listNumbers.insert(tkinter.END, item)
			
			toplevel.destroy()
			
		btn_save_edit = tkinter.Button(toplevel, text="Save", command=save_from_edit_ctc)
		btn_save_edit.pack()

#Buttons
btn_view_details = tkinter.Button(window, text="View Contact Details", command=view_ctc_btn)
btn_view_details.pack(fill=tkinter.X)

btn_edit_ctc = tkinter.Button(window, text="Edit Contact", command=edit_ctc)
btn_edit_ctc.pack(fill=tkinter.X)

btn_delete_ctc = tkinter.Button(window, text="Delete Contact", command=delete_ctc)
btn_delete_ctc.pack(fill=tkinter.X)
 
btn_Add = tkinter.Button(window, text="Add New Contact", command=add_ctc)
btn_Add.pack(fill=tkinter.X)


#bind double-clicking event to view contacts function
listNumbers.bind('<Double-Button-1>', view_ctc)


window.mainloop()