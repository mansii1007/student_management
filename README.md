# 🎓 Student Management System

A Python-based Student Management System built using **Tkinter** and **SQLite**. This application allows users to manage student records through an easy-to-use graphical interface.

## 🚀 Features

- Add new students
- Update student information
- Delete student records
- Search students by Name or Roll Number
- View all student records
- Automatic grade calculation
- SQLite database integration
- User-friendly GUI with Tkinter

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)
- SQLite3 (Database)

---

## 📂 Project Structure

```text
StudentManagementSystem/
│
├── student_management.py
├── students.db
└── README.md
```

---

## 📸 Application Modules

### Student Information
- Name
- Roll Number
- Department
- Semester
- Marks

### Operations
- Add Student
- Update Student
- Delete Student
- Search Student
- Display All Students

### Grade Calculation

| Marks | Grade |
|--------|--------|
| 90+ | A |
| 75-89 | B |
| 60-74 | C |
| 40-59 | D |
| Below 40 | F |

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
```

### Run the Application

```bash
python student_management.py
```

or

```bash
python3 student_management.py
```

---

## 📊 Database Schema

```sql
CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roll_no TEXT UNIQUE NOT NULL,
    department TEXT,
    semester INTEGER,
    marks REAL,
    grade TEXT
);
```

---

## 🔮 Future Enhancements

- Student Login System
- Admin Authentication
- Attendance Management
- Export Data to CSV
- PDF Report Generation
- Data Visualization Charts
- Dark Mode Interface
- Student Profile Pictures

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python Programming
- Object-Oriented Programming
- Database Management with SQLite
- GUI Development using Tkinter
- CRUD Operations
- Data Validation

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Mansi Patil*

GitHub:https://github.com/mansii1007
