import sqlite3 as sql

cnn = "C:\\Users\\17147\\Desktop\\SQLLite\\PythonClassDB.db"

class PatientDML:
    def insert_patient(name, birthdate, doctorid):
        try:
            conn = sql.connect(cnn)
            crs = conn.cursor()
            crs.execute("INSERT INTO patients (name, birthdate, doctorid) VALUES(?,?,?)", (name, birthdate, doctorid))
            conn.commit()   #Commit transaction
            conn.close()    #Close connection
            return 1
        except:
            return 0
    
    def update_patient(id, name, birthdate, doctorid):
        try:
            conn = sql.connect(cnn)
            crs = conn.cursor()
            crs.execute("UPDATE patients SET name=?, birthdate=?, doctorid=? WHERE patientid=?", (name, birthdate, doctorid, id))
            conn.commit()
            conn.close
            return 1
        except:
            return 0

    def delete_patient(id):
        try:
            conn = sql.connect(cnn)
            crs = conn.cursor()
            crs.execute("DELETE FROM patients WHERE patientid=?", (id))
            conn.commit()
            conn.close
            return 1
        except:
            return 0

    def check_patientexists(id):
        conn = sql.connect(cnn)
        crs = conn.cursor()
        crs.execute("SELECT patientid FROM prescriptions WHERE patientid=?", (id))
        rows = crs.fetchone()
        conn.close()    #Close connection
        return rows
        
    def get_patientlist():
        results = []
        conn = sql.connect(cnn)
        crs = conn.cursor()
        crs.execute("SELECT patientid, name FROM patients")
        rows = crs.fetchall()
        
        for row in rows:
            results.append(str(row[0])+"-"+row[1])        

        conn.close()    #Close connection
        return results
        
class DoctorDML:
    def insert_doctor(name, birthdate, license):
        try:
            conn = sql.connect(cnn)
            crs = conn.cursor()
            crs.execute("INSERT INTO doctors (name, birthdate, license) VALUES(?,?,?)", (name, birthdate, license))
            conn.commit()   #Commit transaction
            conn.close()    #Close connection
            return 1
        except:
            return 0
    
    def update_doctor(id, name, birthdate, license):
        try:
            conn = sql.connect(cnn)
            crs = conn.cursor()
            crs.execute("UPDATE doctors SET name=?, birthdate=?, license=? WHERE doctorid=?", (name, birthdate, license, id))
            conn.commit()
            conn.close
            return 1
        except:
            return 0

    def delete_doctor(id):
        try:
            conn = sql.connect(cnn)
            crs = conn.cursor()
            crs.execute("DELETE FROM doctors WHERE doctorid=?", (id))
            conn.commit()
            conn.close
            return 1
        except:
            return 0

    def check_doctorexists(id):
        conn = sql.connect(cnn)
        crs = conn.cursor()
        crs.execute("SELECT doctorid FROM prescriptions WHERE doctorid=?", (id))
        rows = crs.fetchone()
        conn.close

        return rows
    
    def get_doctorlist():
        results = []
        conn = sql.connect(cnn)
        crs = conn.cursor()
        crs.execute("SELECT doctorid, name FROM doctors")
        rows = crs.fetchall()
        for row in rows:
            results.append(str(row[0])+"-"+row[1])        
        conn.close    

        return results

class PrescriptionDML:
    def insert_prescription(patientid, doctorid, prescriptiondate, drugcode):
        try:
            conn = sql.connect(cnn)
            crs = conn.cursor()
            crs.execute("INSERT INTO prescriptions (patientid, doctorid, prescriptiondate, drugcode) VALUES(?,?,?,?)", (patientid, doctorid, prescriptiondate, drugcode))
            conn.commit()   #Commit transaction
            conn.close()    #Close connection
            return 1
        except:
            return 0
    
    def update_prescription(prescriptionid, patientid, doctorid, prescriptiondate, drugcode):
        try:
            conn = sql.connect(cnn)
            crs = conn.cursor()
            crs.execute("UPDATE prescriptions SET patientid=?, doctorid=?, prescriptiondate=?, drugcode=? WHERE prescriptionid=?", (patientid, doctorid, prescriptiondate, drugcode, prescriptionid))
            conn.commit()
            conn.close
            return 1
        except ValueError:
            print(ValueError)
            return 0
        except TypeError:
            print(TypeError)
            return 0
        except:
            return 0

    def delete_prescription(id):
        try:
            conn = sql.connect(cnn)
            crs = conn.cursor()
            crs.execute("DELETE FROM prescriptions WHERE prescriptionid=?", (id))
            conn.commit()
            conn.close
            return 1
        except:
            return 0

    def get_prescriptioncount():
        try:
            conn = sql.connect(cnn)
            crs = conn.cursor()
            crs.execute("SELECT COUNT(*) FROM doctors")
            rows = crs.fetchall()
            return 1
        except:
            return 0
