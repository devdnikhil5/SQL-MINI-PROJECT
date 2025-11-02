from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
DATABASE = 'hospital.db'

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database
def init_db():
    conn = get_db_connection()
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.close()
    print("Database initialized successfully!")

# Home/Dashboard Route
@app.route('/')
def index():
    conn = get_db_connection()
    patient_count = conn.execute('SELECT COUNT(*) as count FROM Patients').fetchone()['count']
    doctor_count = conn.execute('SELECT COUNT(*) as count FROM Doctors').fetchone()['count']
    appointment_count = conn.execute('SELECT COUNT(*) as count FROM Appointments').fetchone()['count']
    conn.close()
    return render_template('index.html', 
                         patients=patient_count, 
                         doctors=doctor_count, 
                         appointments=appointment_count)

# ==================== PATIENTS ====================
@app.route('/patients')
def patients():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM Patients ORDER BY PatientID DESC').fetchall()
    conn.close()
    return render_template('patients.html', patients=patients)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        contact = request.form['contact']
        address = request.form['address']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO Patients (Name, DOB, Gender, ContactInfo, Address) VALUES (?, ?, ?, ?, ?)',
                     (name, dob, gender, contact, address))
        conn.commit()
        conn.close()
        flash('Patient added successfully!', 'success')
        return redirect(url_for('patients'))
    return render_template('add_patient.html')

@app.route('/edit_patient/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        contact = request.form['contact']
        address = request.form['address']
        
        conn.execute('UPDATE Patients SET Name=?, DOB=?, Gender=?, ContactInfo=?, Address=? WHERE PatientID=?',
                     (name, dob, gender, contact, address, id))
        conn.commit()
        conn.close()
        flash('Patient updated successfully!', 'success')
        return redirect(url_for('patients'))
    
    patient = conn.execute('SELECT * FROM Patients WHERE PatientID=?', (id,)).fetchone()
    conn.close()
    return render_template('edit_patient.html', patient=patient)

@app.route('/delete_patient/<int:id>')
def delete_patient(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Patients WHERE PatientID=?', (id,))
    conn.commit()
    conn.close()
    flash('Patient deleted successfully!', 'success')
    return redirect(url_for('patients'))

# ==================== DOCTORS ====================
@app.route('/doctors')
def doctors():
    conn = get_db_connection()
    doctors = conn.execute('SELECT * FROM Doctors ORDER BY DoctorID DESC').fetchall()
    conn.close()
    return render_template('doctors.html', doctors=doctors)

@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        name = request.form['name']
        specialty = request.form['specialty']
        contact = request.form['contact']
        email = request.form['email']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO Doctors (Name, Specialty, ContactInfo, Email) VALUES (?, ?, ?, ?)',
                     (name, specialty, contact, email))
        conn.commit()
        conn.close()
        flash('Doctor added successfully!', 'success')
        return redirect(url_for('doctors'))
    return render_template('add_doctor.html')

@app.route('/delete_doctor/<int:id>')
def delete_doctor(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Doctors WHERE DoctorID=?', (id,))
    conn.commit()
    conn.close()
    flash('Doctor deleted successfully!', 'success')
    return redirect(url_for('doctors'))

# ==================== APPOINTMENTS ====================
@app.route('/appointments')
def appointments():
    conn = get_db_connection()
    appointments = conn.execute('''
        SELECT A.AppointmentID, P.Name as PatientName, D.Name as DoctorName, 
               A.AppointmentDate, A.Notes, A.Status
        FROM Appointments A
        JOIN Patients P ON A.PatientID = P.PatientID
        JOIN Doctors D ON A.DoctorID = D.DoctorID
        ORDER BY A.AppointmentDate DESC
    ''').fetchall()
    conn.close()
    return render_template('appointments.html', appointments=appointments)

@app.route('/add_appointment', methods=['GET', 'POST'])
def add_appointment():
    conn = get_db_connection()
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        appointment_date = request.form['appointment_date']
        notes = request.form['notes']
        status = request.form['status']
        
        conn.execute('INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate, Notes, Status) VALUES (?, ?, ?, ?, ?)',
                     (patient_id, doctor_id, appointment_date, notes, status))
        conn.commit()
        conn.close()
        flash('Appointment booked successfully!', 'success')
        return redirect(url_for('appointments'))
    
    patients = conn.execute('SELECT * FROM Patients').fetchall()
    doctors = conn.execute('SELECT * FROM Doctors').fetchall()
    conn.close()
    return render_template('add_appointment.html', patients=patients, doctors=doctors)

@app.route('/delete_appointment/<int:id>')
def delete_appointment(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Appointments WHERE AppointmentID=?', (id,))
    conn.commit()
    conn.close()
    flash('Appointment deleted successfully!', 'success')
    return redirect(url_for('appointments'))

if __name__ == '__main__':
    # Uncomment the line below to initialize database on first run
    init_db()
    app.run(debug=True)