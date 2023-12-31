import sqlite3
from tkinter import *
import ttkthemes
from tkinter import ttk, messagebox
from database import cursor, conn

def show_tenant_details():
		for widget in right_frame.winfo_children():
			widget.destroy()

		query = 'SELECT * FROM tenants'
		cursor.execute(query)
		fetched_tenants = cursor.fetchall()

		for data in fetched_tenants:
			tenant_table.insert('', 'end', values=data)


def show_add_form():
		global name_entry, email_entry, phone_entry, id_entry, Emergency_Contact_entry, Pet_Info_entry, employer_entry, dob_entry, move_in_entry, rent_entry,security_entry

		for widget in right_frame.winfo_children():
				widget.destroy()
				
		ttk.Label(right_frame, text="Name:", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10, pady=10)
		name_entry = ttk.Entry(right_frame, font=("Arial", 14))
		name_entry.grid(row=0, column=1, padx=10, pady=10)

		ttk.Label(right_frame, text="Email:", font=("Arial", 14, "bold")).grid(row=1, column=0, padx=10, pady=10)
		email_entry = ttk.Entry(right_frame, font=("Arial", 14))
		email_entry.grid(row=1, column=1, padx=10, pady=10)
		
		ttk.Label(right_frame, text="Phone No:", font=("Arial", 14, "bold")).grid(row=2, column=0, padx=10, pady=10)
		phone_entry = ttk.Entry(right_frame, font=("Arial", 14))
		phone_entry.grid(row=2, column=1, padx=10, pady=10)

		ttk.Label(right_frame, text="ID NO:", font=("Arial", 14, "bold")).grid(row=3, column=0, padx=10, pady=10)
		id_entry = ttk.Entry(right_frame, font=("Arial", 14))
		id_entry.grid(row=3, column=1, padx=10, pady=10)

		ttk.Label(right_frame, text="Tenant's Employer:", font=("Arial", 14, "bold")).grid(row=4, column=0, padx=10, pady=10)
		employer_entry = ttk.Entry(right_frame, font=("Arial", 14))
		employer_entry.grid(row=4, column=1, padx=10, pady=10)

		ttk.Label(right_frame, text="D.O.B:", font=("Arial", 14, "bold")).grid(row=5, column=0, padx=10, pady=10)
		dob_entry = ttk.Entry(right_frame, font=("Arial", 14))
		dob_entry.grid(row=5, column=1, padx=10, pady=10)

		ttk.Label(right_frame, text="Move-In Date:", font=("Arial", 14, "bold")).grid(row=6, column=0, padx=10, pady=10)
		move_in_entry = ttk.Entry(right_frame, font=("Arial", 14))
		move_in_entry.grid(row=6, column=1, padx=10, pady=10)

		ttk.Label(right_frame, text="Rent Amount:", font=("Arial", 14, "bold")).grid(row=7, column=0, padx=10, pady=10)
		rent_entry = ttk.Entry(right_frame, font=("Arial", 14))
		rent_entry.grid(row=7, column=1, padx=10, pady=10)

		ttk.Label(right_frame, text="Security Deposit:", font=("Arial", 14, "bold")).grid(row=8, column=0, padx=10, pady=10)
		security_entry = ttk.Entry(right_frame, font=("Arial", 14))
		security_entry.grid(row=8, column=1, padx=10, pady=10)

		ttk.Label(right_frame, text="Emergency Contact:", font=("Arial", 14, "bold")).grid(row=9, column=0, padx=10, pady=10)
		Emergency_Contact_entry = ttk.Entry(right_frame, font=("Arial", 14))
		Emergency_Contact_entry.grid(row=9, column=1, padx=10, pady=10)

		ttk.Label(right_frame, text="Nat Id:", font=("Arial", 14, "bold")).grid(row=9, column=0, padx=10, pady=10)
		Emergency_Contact_entry = ttk.Entry(right_frame, font=("Arial", 14))
		Emergency_Contact_entry.grid(row=9, column=1, padx=10, pady=10)

		ttk.Label(right_frame, text="Room No:", font=("Arial", 14, "bold")).grid(row=9, column=0, padx=10, pady=10)
		Emergency_Contact_entry = ttk.Entry(right_frame, font=("Arial", 14))
		Emergency_Contact_entry.grid(row=9, column=1, padx=10, pady=10)

		clear_button = ttk.Button(right_frame, text="Clear Form", command=clear_form)
		clear_button.grid(row=10, column=0)
		
		submit_button = ttk.Button(right_frame, text="Add Tenant", command=save_data)
		submit_button.grid(row=10, column=1)

def save_data():
	name = name_entry.get()
	email = email_entry.get()
	phone = phone_entry.get()
	id = id_entry.get()
	employer = employer_entry.get()
	dob = dob_entry.get()
	move_in = move_in_entry.get()
	rent = rent_entry.get()
	security = security_entry.get()
	emergency_contact = Emergency_Contact_entry.get()

	
	query = "INSERT INTO tenants (name, email, phone, id, employer, dob, move_in, rent, security, emergency_contact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
	values = (name, email, phone, id, employer, dob, move_in, rent, security, emergency_contact)

	try:
		cursor.execute(query, values)
		conn.commit()
		messagebox.showinfo("Data Saved Successfully")
	except sqlite3.Error as a:
		messagebox.showerror("Error occured while saving data:", a)

def clear_form():
	name_entry.delete(0, END)
	email_entry.delete(0, END)
	phone_entry.delete(0, END)
	id_entry.delete(0, END)
	employer_entry.delete(0, END)
	dob_entry.delete(0, END)
	move_in_entry.delete(0, END)
	rent_entry.delete(0, END)
	security_entry.delete(0, END)
	Emergency_Contact_entry.delete(0, END)


window = Tk()
window.title('House Management System')
window.geometry('1280x700+0+0')
window.resizable(False, False)

top_bar = Frame(window, bg="blue")
top_bar.place(x=0, y=0, width=1080, height=50)

label_text = "House Management System"
top_text = ttk.Label(top_bar, text=label_text, font=("Arial", 18, "bold"))
top_text.grid(row=0, column=3, padx=20, pady=10)


left_frame = Frame(window)
left_frame.place(x=100, y=50)


addStudentButton = ttk.Button(left_frame, text='Add Tenant', width=25, command=show_add_form)
addStudentButton.grid(row=1, column=2, pady=20)

tenant_details = ttk.Button(left_frame, text='Tenant Details', width=25, command=show_tenant_details)
tenant_details.grid(row=2, column=2, pady=20)

edit_tenant = ttk.Button(left_frame, text='Edit Tenant', width=25)
edit_tenant.grid(row=3, column=2, pady=20)

remove_tenant = ttk.Button(left_frame, text='Remove Tenant', width=25)
remove_tenant.grid(row=4, column=2, pady=20)

manage_payments = ttk.Button(left_frame, text='Manage Payments', width=25)
manage_payments.grid(row=5, column=2, pady=20)


right_frame = Frame(window)
right_frame.configure(background="grey",pady=20, padx=200)
right_frame.place(x=350, y=80, width=820, height=600)

ScrollbarX = Scrollbar(right_frame, orient=HORIZONTAL)
ScrollbarY = Scrollbar(right_frame, orient=VERTICAL)

tenant_table = ttk.Treeview(right_frame, columns=('Nat Id', 'Room No', 'Name','Email', 'Rent Bal', 'Mob No',
						  'D.O.B', 'Added Day', 'Added Time' ),
			     xscrollcommand = ScrollbarX.set,
					 yscrollcommand=ScrollbarY.set)

ScrollbarX.config(command=tenant_table.xview)
ScrollbarY.config(command=tenant_table.yview)

ScrollbarX.pack(side=BOTTOM, fill=X)
ScrollbarY.pack(side=RIGHT, fill=Y)

tenant_table.pack(fill=BOTH, expand=1)


tenant_table.heading("Nat Id", text='Nat ID')
tenant_table.heading("Room No", text='Room No')
tenant_table.heading("Name", text='Name')
tenant_table.heading("Email", text='Email')
tenant_table.heading("Rent Bal", text='Rent Bal')
tenant_table.heading("Mob No", text='Mobile NO')
tenant_table.heading('D.O.B', text='D.O.B')
tenant_table.heading('Added Day', text='Added Day')
tenant_table.heading('Added Time', text='Added Time')

tenant_table.column("Nat Id", width=50, anchor=CENTER)
tenant_table.column("Room No", width=50, anchor=CENTER)
tenant_table.column("Name", width=300, anchor=CENTER)
tenant_table.heading("Email", text='Email')
tenant_table.column("Rent Bal", width=50, anchor=CENTER)
tenant_table.column("Mob No", width=200, anchor=CENTER)
tenant_table.column('D.O.B', width=100, anchor=CENTER)
tenant_table.column('Added Day', width=200, anchor=CENTER)
tenant_table.column('Added Time', width=200, anchor=CENTER)

style = ttk.Style()

style.configure('Treeview', rowheight=30, font=('arial', 12, 'bold'),
		background='white', fieldbackground='white')
style.configure('Treeview.Heading', font=('arial', 14, 'bold'), foreground='red')

tenant_table.config(show='headings')


window.mainloop()

conn.close
