-- Drop existing tables if they exist
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS Treatments;
DROP TABLE IF EXISTS Doctors;
DROP TABLE IF EXISTS Patients;

-- Create Patients table
CREATE TABLE Patients (
    PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    DOB TEXT NOT NULL,
    Gender TEXT CHECK(Gender IN ('M', 'F', 'Other')),
    ContactInfo TEXT,
    Address TEXT
);

-- Create Doctors table
CREATE TABLE Doctors (
    DoctorID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Specialty TEXT,
    ContactInfo TEXT,
    Email TEXT
);

-- Create Treatments table
CREATE TABLE Treatments (
    TreatmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    TreatmentName TEXT NOT NULL,
    Description TEXT,
    Cost REAL
);

-- Create Appointments table
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

-- Insert sample data
INSERT INTO Patients (Name, DOB, Gender, ContactInfo, Address) VALUES
('John Doe', '1990-05-15', 'M', '9876543210', '123 Main St, City'),
('Jane Smith', '1985-08-22', 'F', '9876543211', '456 Oak Ave, Town'),
('Robert Brown', '2000-12-10', 'M', '9876543212', '789 Pine Rd, Village');

INSERT INTO Doctors (Name, Specialty, ContactInfo, Email) VALUES
('Dr. Sarah Johnson', 'Cardiology', '9988776655', 'sarah.j@hospital.com'),
('Dr. Michael Chen', 'Neurology', '9988776656', 'michael.c@hospital.com'),
('Dr. Emily Davis', 'Pediatrics', '9988776657', 'emily.d@hospital.com');

INSERT INTO Treatments (TreatmentName, Description, Cost) VALUES
('General Checkup', 'Routine health examination', 500.00),
('Blood Test', 'Complete blood count analysis', 800.00),
('X-Ray', 'Radiographic imaging', 1200.00);

INSERT INTO Appointments (PatientID, DoctorID, TreatmentID, AppointmentDate, Notes, Status) VALUES
(1, 1, 1, '2025-11-05 10:00:00', 'Regular checkup', 'Scheduled'),
(2, 2, 2, '2025-11-06 14:30:00', 'Follow-up consultation', 'Scheduled'),
(3, 3, 1, '2025-11-07 09:00:00', 'First visit', 'Scheduled');