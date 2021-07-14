import mysql.connector

def display(aadhar):
    db = mysql.connector.connect(host='localhost',
                                 database='cwpcp',
                                 user='root',
                                 password='toor')

    insert = """select name, age, centre, date(date),time, vaccine, dose_no 
                from personal p inner join medical m 
                on p.aadhar_no = m.a_no
                where m.a_no = %s 
                """
    record = (aadhar,)
    mycursor = db.cursor()
    mycursor.execute(insert, record)
    for i in mycursor:
        print("Name: ", i[0])
        print("Age: ", i[1])
        print("Centre: ", i[2])
        print("DOV: ", i[3])
        print("TOV: ", i[4])
        print("Vaccine:", i[5])
        print("Dose:", i[6])

display(int(input("Enter the aadhar no: ")))


