import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll_no TEXT UNIQUE NOT NULL,
    department TEXT,
    semester INTEGER,
    marks REAL,
    grade TEXT
)
""")

conn.commit()


def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def add_student():
    try:
        name = name_var.get()
        roll = roll_var.get()
        dept = dept_var.get()
        sem = int(sem_var.get())
        marks = float(marks_var.get())

        grade = calculate_grade(marks)

        cursor.execute("""
        INSERT INTO students
        (name, roll_no, department, semester, marks, grade)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, roll, dept, sem, marks, grade))

        conn.commit()

        messagebox.showinfo("Success", "Student Added Successfully")

        clear_fields()
        display_students()

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Roll Number Already Exists")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def display_students():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM students")

    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)


def clear_fields():
    name_var.set("")
    roll_var.set("")
    dept_var.set("")
    sem_var.set("")
    marks_var.set("")


def delete_student():
    selected = tree.focus()

    if not selected:
        messagebox.showwarning("Warning", "Select a Student")
        return

    values = tree.item(selected, "values")
    student_id = values[0]

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    display_students()
    messagebox.showinfo("Success", "Student Deleted")


def select_student(event):
    selected = tree.focus()

    if not selected:
        return

    values = tree.item(selected, "values")

    name_var.set(values[1])
    roll_var.set(values[2])
    dept_var.set(values[3])
    sem_var.set(values[4])
    marks_var.set(values[5])


def update_student():
    selected = tree.focus()

    if not selected:
        messagebox.showwarning("Warning", "Select a Student")
        return

    values = tree.item(selected, "values")
    student_id = values[0]

    name = name_var.get()
    roll = roll_var.get()
    dept = dept_var.get()
    sem = int(sem_var.get())
    marks = float(marks_var.get())

    grade = calculate_grade(marks)

    cursor.execute("""
    UPDATE students
    SET name=?,
        roll_no=?,
        department=?,
        semester=?,
        marks=?,
        grade=?
    WHERE id=?
    """,
    (name, roll, dept, sem, marks, grade, student_id))

    conn.commit()

    display_students()
    clear_fields()

    messagebox.showinfo("Success", "Student Updated")


def search_student():
    keyword = search_var.get()

    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("""
    SELECT * FROM students
    WHERE name LIKE ?
       OR roll_no LIKE ?
    """,
    (f"%{keyword}%", f"%{keyword}%"))

    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)



root = tk.Tk()
root.title("Student Management System")
root.geometry("1000x600")

# Variables
name_var = tk.StringVar()
roll_var = tk.StringVar()
dept_var = tk.StringVar()
sem_var = tk.StringVar()
marks_var = tk.StringVar()
search_var = tk.StringVar()

# Form Frame
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(form_frame, textvariable=name_var).grid(row=0, column=1)

tk.Label(form_frame, text="Roll No").grid(row=0, column=2)
tk.Entry(form_frame, textvariable=roll_var).grid(row=0, column=3)

tk.Label(form_frame, text="Department").grid(row=1, column=0)
tk.Entry(form_frame, textvariable=dept_var).grid(row=1, column=1)

tk.Label(form_frame, text="Semester").grid(row=1, column=2)
tk.Entry(form_frame, textvariable=sem_var).grid(row=1, column=3)

tk.Label(form_frame, text="Marks").grid(row=2, column=0)
tk.Entry(form_frame, textvariable=marks_var).grid(row=2, column=1)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame,
          text="Add Student",
          command=add_student,
          bg="green",
          fg="white").grid(row=0, column=0, padx=5)

tk.Button(btn_frame,
          text="Update Student",
          command=update_student,
          bg="blue",
          fg="white").grid(row=0, column=1, padx=5)

tk.Button(btn_frame,
          text="Delete Student",
          command=delete_student,
          bg="red",
          fg="white").grid(row=0, column=2, padx=5)

tk.Button(btn_frame,
          text="Clear",
          command=clear_fields).grid(row=0, column=3, padx=5)

# Search
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Entry(search_frame,
         textvariable=search_var,
         width=30).grid(row=0, column=0)

tk.Button(search_frame,
          text="Search",
          command=search_student).grid(row=0, column=1, padx=5)

tk.Button(search_frame,
          text="Show All",
          command=display_students).grid(row=0, column=2)

# Table
columns = (
    "ID",
    "Name",
    "Roll No",
    "Department",
    "Semester",
    "Marks",
    "Grade"
)

tree = ttk.Treeview(root,
                    columns=columns,
                    show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(fill=tk.BOTH, expand=True)

tree.bind("<ButtonRelease-1>", select_student)

display_students()

root.mainloop()

conn.close()
