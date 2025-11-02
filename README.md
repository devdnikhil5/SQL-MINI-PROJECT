# SQL-MINI-PROJECT
# Hospital Management System

A comprehensive full-stack web application for managing hospital operations including patient records, doctor information, treatments, and appointment scheduling. Built with Python Flask, SQLite, and Bootstrap.

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [API Routes](#api-routes)
- [Database Schema](#database-schema)
- [CRUD Operations](#crud-operations)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## ✨ Features

### Patient Management
- ✅ Add new patient records with personal information
- ✅ View all patients in a table format
- ✅ Edit existing patient information
- ✅ Delete patient records
- ✅ Store detailed patient data (Name, DOB, Gender, Contact, Address)

### Doctor Management
- ✅ Add doctor profiles with specialty information
- ✅ View all doctors with their specialties
- ✅ Manage doctor contact information and email
- ✅ Delete doctor records

### Appointment Scheduling
- ✅ Book appointments between patients and doctors
- ✅ Track appointment status (Scheduled, Completed, Cancelled)
- ✅ Add notes for each appointment
- ✅ View all appointments with patient and doctor details
- ✅ Delete appointments

### Treatments
- ✅ Maintain treatment catalogue with descriptions and costs
- ✅ Link treatments to appointments
- ✅ Track treatment costs

### Dashboard
- ✅ Quick overview with statistics
- ✅ Total patient count
- ✅ Total doctor count
- ✅ Total appointment count
- ✅ Quick action buttons for common tasks

### User Interface
- ✅ Responsive Bootstrap design
- ✅ User-friendly navigation bar
- ✅ Flash messages for user feedback
- ✅ Professional styling with custom CSS
- ✅ Data validation on forms

## 🛠️ Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Backend** | Python Flask | 3.0.0 |
| **Database** | SQLite 3 | Built-in |
| **Frontend** | HTML5, CSS3 | Latest |
| **Framework** | Bootstrap | 5.3.0 |
| **Server** | Flask Development Server | - |
| **Language** | Python | 3.7+ |

## 📁 Project Structure

```
hospital_management_system/
│
├── app.py                          # Main Flask application
├── schema.sql                      # Database schema
├── requirements.txt                # Python dependencies
├── hospital.db                     # SQLite database (created at runtime)
├── README.md                       # Project documentation
│
├── static/
│   ├── css/
│   │   └── style.css              # Custom CSS styling
│   └── js/
│       └── script.js              # JavaScript (optional)
│
└── templates/
    ├── base.html                  # Base template with navbar
    ├── index.html                 # Dashboard/Home page
    ├── patients.html              # View all patients
    ├── add_patient.html           # Add new patient form
    ├── edit_patient.html          # Edit patient form
    ├── doctors.html               # View all doctors
    ├── add_doctor.html            # Add new doctor form
    ├── appointments.html          # View all appointments
    └── add_appointment.html       # Book appointment form
```

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Git (optional)

### Step 1: Clone or Download Repository

```bash
# Clone from GitHub
git clone https://github.com/yourusername/hospital-management-system.git
cd hospital_management_system

# Or download and extract ZIP file
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt contains:**
```
Flask==3.0.0
```

## 🗄️ Database Setup

### Step 1: Initialize Database

**Option A: Using Python shell**
```bash
python
>>> from app import init_db
>>> init_db()
>>> exit()
```

**Option B: Uncomment init_db() in app.py**

Open `app.py` and find the main block:
```python
if __name__ == '__main__':
    init_db()  # Uncomment this line
    app.run(debug=True)
```

Run the application once:
```bash
python app.py
```

Then comment it back out to avoid reinitializing on every run.

### Step 2: Verify Database Creation

Check that `hospital.db` file is created in the project root directory.

### Step 3: Sample Data

Sample patients, doctors, treatments, and appointments are automatically inserted during initialization. You can view them by running the application.

## 💻 Usage

### Start the Application

```bash
python app.py
```

**Output:**
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Access the Application

Open your web browser and navigate to:
```
http://localhost:5000/
```

### Navigation

**Dashboard** → Overview with statistics and quick actions

**Patients** → Manage patient records
- View all patients
- Add new patient
- Edit patient info
- Delete patient

**Doctors** → Manage doctor profiles
- View all doctors
- Add new doctor
- Delete doctor

**Appointments** → Schedule and manage appointments
- View all appointments
- Book new appointment
- Delete appointment

## 📸 Screenshots

### Dashboard
Shows total patients, doctors, and appointments with quick action buttons.

### Patients List
Table displaying all patients with Edit and Delete options.

### Add Patient Form
Form to enter new patient information with validation.

### Appointments View
Shows all appointments with linked patient and doctor names.

## 🔗 API Routes

### Home & Dashboard
| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Display dashboard with statistics |

### Patient Routes
| Route | Method | Description |
|-------|--------|-------------|
| `/patients` | GET | View all patients |
| `/add_patient` | GET | Show add patient form |
| `/add_patient` | POST | Create new patient |
| `/edit_patient/<id>` | GET | Show edit patient form |
| `/edit_patient/<id>` | POST | Update patient record |
| `/delete_patient/<id>` | GET | Delete patient record |

### Doctor Routes
| Route | Method | Description |
|-------|--------|-------------|
| `/doctors` | GET | View all doctors |
| `/add_doctor` | GET | Show add doctor form |
| `/add_doctor` | POST | Create new doctor |
| `/delete_doctor/<id>` | GET | Delete doctor record |

### Appointment Routes
| Route | Method | Description |
|-------|--------|-------------|
| `/appointments` | GET | View all appointments |
| `/add_appointment` | GET | Show booking form |
| `/add_appointment` | POST | Create appointment |
| `/delete_appointment/<id>` | GET | Delete appointment |

## 🗂️ Database Schema

### Patients Table
```sql
CREATE TABLE Patients (
    PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    DOB TEXT NOT NULL,
    Gender TEXT CHECK(Gender IN ('M', 'F', 'Other')),
    ContactInfo TEXT,
    Address TEXT
);
```

### Doctors Table
```sql
CREATE TABLE Doctors (
    DoctorID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Specialty TEXT,
    ContactInfo TEXT,
    Email TEXT
);
```

### Treatments Table
```sql
CREATE TABLE Treatments (
    TreatmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    TreatmentName TEXT NOT NULL,
    Description TEXT,
    Cost REAL
);
```

### Appointments Table
```sql
CREATE TABLE Appointments (
    AppointmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    PatientID INTEGER,
    DoctorID INTEGER,
    TreatmentID INTEGER,
    AppointmentDate TEXT NOT NULL,
    Notes TEXT,
    Status TEXT DEFAULT 'Scheduled',
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID) ON DELETE CASCADE,
    FOREIGN KEY (TreatmentID) REFERENCES Treatments(TreatmentID) ON DELETE SET NULL
);
```

## 🔄 CRUD Operations

### CREATE (Add)
```python
# Add new patient
conn.execute('INSERT INTO Patients (Name, DOB, Gender, ContactInfo, Address) VALUES (?, ?, ?, ?, ?)',
             (name, dob, gender, contact, address))
conn.commit()
```

### READ (View)
```python
# Get all patients
patients = conn.execute('SELECT * FROM Patients').fetchall()

# Get specific patient
patient = conn.execute('SELECT * FROM Patients WHERE PatientID = ?', (id,)).fetchone()
```

### UPDATE (Edit)
```python
# Update patient info
conn.execute('UPDATE Patients SET Name=?, DOB=?, Gender=?, ContactInfo=?, Address=? WHERE PatientID=?',
             (name, dob, gender, contact, address, id))
conn.commit()
```

### DELETE (Remove)
```python
# Delete patient
conn.execute('DELETE FROM Patients WHERE PatientID=?', (id,))
conn.commit()
```

## 🔍 Database Relationships

- **One-to-Many**: One Doctor can have Many Appointments
- **One-to-Many**: One Patient can have Many Appointments
- **One-to-Many**: One Treatment can be used in Many Appointments
- **Foreign Keys** ensure referential integrity

## 📝 Key Concepts Covered

- ✅ Database Design and Normalization
- ✅ SQL CRUD Operations
- ✅ Primary Keys and Foreign Keys
- ✅ Flask Routing and Templates
- ✅ HTML Forms and Bootstrap
- ✅ Database Connections in Python
- ✅ MVC Architecture
- ✅ Template Inheritance
- ✅ Flash Messages
- ✅ HTTP Methods (GET, POST)

## 🐛 Troubleshooting

### Port 5000 Already in Use
```bash
# Change port in app.py
app.run(debug=True, port=5001)
```

### Database Not Found
```bash
# Reinitialize database
python
>>> from app import init_db
>>> init_db()
```

### Flask Not Installed
```bash
pip install Flask==3.0.0
```

### Template Not Found Error
- Ensure `templates/` folder exists in project root
- Check template file names match exactly

## 📚 Learning Resources

- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Python SQLite Tutorial](https://docs.python.org/3/library/sqlite3.html)

## 🚀 Future Enhancements

- [ ] User authentication and login system
- [ ] Search and filter functionality
- [ ] Export data to CSV/PDF
- [ ] Email notifications for appointments
- [ ] Appointment reminders
- [ ] Payment tracking
- [ ] Medical history records
- [ ] Prescription management
- [ ] Billing system
- [ ] Advanced reporting and analytics
- [ ] Mobile responsive improvements
- [ ] Database backups and restore

## 📄 File Descriptions

| File | Description |
|------|-------------|
| `app.py` | Main Flask application with routes and database logic |
| `schema.sql` | Database schema and sample data |
| `requirements.txt` | Python package dependencies |
| `hospital.db` | SQLite database file (created at runtime) |
| `base.html` | Base template with navbar and layout |
| `style.css` | Custom CSS styles and overrides |
| `script.js` | Client-side JavaScript (optional) |

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Bootstrap team for amazing CSS framework
- Flask community for excellent documentation
- SQLite for reliable database engine
- All contributors and users of this project

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: your.email@example.com
- Check existing documentation

## 🎓 Project Info

- **Type**: Educational Mini Project
- **Level**: Beginner to Intermediate
- **Concepts**: Database Design, SQL, Flask, Web Development
- **Use Case**: Hospital Management
- **Status**: Active Development

---

## Quick Start Summary

```bash
# 1. Clone repository
git clone https://github.com/yourusername/hospital-management-system.git
cd hospital_management_system

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize database
python
>>> from app import init_db
>>> init_db()
>>> exit()

# 5. Run application
python app.py

# 6. Open browser
http://localhost:5000/
```

