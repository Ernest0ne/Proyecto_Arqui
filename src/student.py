from tkinter import Tk, Canvas, Label, Frame, Entry, Button, W, E, Listbox, END
import psycopg2 

root = Tk()
root.title("python & pstgresSQL")

def sav_new_student(name, age, address):
    conn = psycopg2.connect(dbname="d55j547n4hvhpg", 
        user="ctyoycwrtksvbw", 
        password="51d77bad7009efc8478b86b0a88ec7eab7f47713eb7424a45e06ef6a0a98580a", 
        host="ec2-54-166-167-192.compute-1.amazonaws.com", 
        port="5432")

    cursor = conn.cursor()
    query = '''INSERT INTO students(name, age, address) VALUES(%s, %s, %s)'''
    cursor.execute(query, (name, age, address))
    print("Date save")
    conn.commit()
    conn.close()
    # refresh with new students
    display_student()

def display_student():
    conn = psycopg2.connect(dbname="d55j547n4hvhpg", 
        user="ctyoycwrtksvbw", 
        password="51d77bad7009efc8478b86b0a88ec7eab7f47713eb7424a45e06ef6a0a98580a", 
        host="ec2-54-166-167-192.compute-1.amazonaws.com", 
        port="5432"
    )

    cursor = conn.cursor()
    query = '''SELECT * FROM students'''
    cursor.execute(query)
    
    row = cursor.fetchall()

    listbox = Listbox(frame, width=20, height=10)
    listbox.grid(row=10, columnspan=4, sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

def search(id):
    conn = psycopg2.connect(dbname="d55j547n4hvhpg", 
        user="ctyoycwrtksvbw", 
        password="51d77bad7009efc8478b86b0a88ec7eab7f47713eb7424a45e06ef6a0a98580a", 
        host="ec2-54-166-167-192.compute-1.amazonaws.com", 
        port="5432"
    )

    cursor = conn.cursor()
    query = '''SELECT * FROM students WHERE id=%s'''
    cursor.execute(query, (id))
    
    row = cursor.fetchone()

    display_search_result(row)

    '''listbox = Listbox(frame, width=20, height=6)
    listbox.grid(row=10, columnspan=4, sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()'''

def display_search_result(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, columnspan=4, sticky=W+E)
    listbox.insert(END, row)

#canvas
canvas =Canvas(root, height=380, width=400)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text='Agregar Estudiante')
label.grid(row=0, column=1)

# Name input
label = Label(frame, text="Nombre")
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

# Age input
label = Label(frame, text="Edad")
label.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

# Address input
label = Label(frame, text="Dirección")
label.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

button = Button(frame, text="Agregar", command=lambda:sav_new_student(
    entry_name.get(),
    entry_age.get(),
    entry_address.get()
    ))
button.grid(row=4, column=1, sticky=W+E)

# Search
label = Label(frame, text="buscar Datos")
label.grid(row=5, column=0)

label = Label(frame, text="Bsucar por ID")
label.grid(row=6, column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

button = Button(frame, text="Buscar", command=lambda:search(id_search.get()))
button.grid(row=6, column=2)

display_student()

root.mainloop()