import mysql.connector


def personal(dict):
    db = mysql.connector.connect(host='localhost',
                                         database='cwpcp',
                                         user='root',
                                         password='toor')

    insert = "insert into personal (name,age,aadhar_no) values (%s,%s,%s)"
    mycursor = db.cursor()
    record = (dict.get('name'), dict.get('age'), dict.get('aadhar'))
    mycursor.execute(insert, record)
    db.commit()


def medical(dict):
    db = mysql.connector.connect(host='localhost',
                                         database='cwpcp',
                                         user='root',
                                         password='toor')
    insert = "insert into medical (a_no, centre,date, time, vaccine, dose_no) values (%s,%s,%s,%s,%s,%s)"
    mycursor = db.cursor()
    record = (dict.get('aadhar'), dict.get('centre'), dict.get('date'),dict.get('time'), dict.get('vaccine'), dict.get('shot no.'))
    mycursor.execute(insert, record)
    db.commit()


