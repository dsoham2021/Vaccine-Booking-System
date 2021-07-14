import sys, db
from datetime import date, timedelta


record_dict = {}


def age_sel():
    age_ch = int(input("Enter your age: "))
    if age_ch >= 18:
        record_dict['age'] = age_ch
        name_sel()
    else:
        sys.exit("\nYou need to be above 18 years of age to get vaccinated")


def name_sel():
    name_ch = input("\nEnter your name: ")
    record_dict['name'] = name_ch
    aadhar_sel()


def aadhar_sel():
    aadhar_ch = int(input("\nEnter your Aadhar card no.: "))
    record_dict['aadhar'] = aadhar_ch
    date_sel()


def date_sel():
    dt_1 = date.today()
    delta_1 = timedelta(days=1)
    dt_2 = dt_1 + delta_1
    dt_3 = dt_2 + delta_1

    print("\n")
    print(1, "--", dt_1)
    print(2, "--", dt_2)
    print(3, "--", dt_3)
    date_ch = int(input("\nChoose the date for vaccination: "))
    if date_ch == 1:
        record_dict['date'] = dt_1
        time_sel()
    elif date_ch == 2:
        record_dict['date'] = dt_2
        time_sel()
    elif date_ch == 3:
        record_dict['date'] = dt_3
        time_sel()
    else:
        print("\nInvalid option")
        ret_1 = int(input("\nEnter 1 to retry. Enter any key to exit"))
        if ret_1 == 1:
            date_sel()
        else:
            sys.exit()


def time_sel():
    time_list = {1: "10 am", 2: "12 am", 3: "2 pm", 4: "4 pm"}
    print("\n")
    for i in time_list:
        print(i, "--", time_list[i])

    time_ch = int(input("\nChoose the time for vaccination: "))
    if time_ch == 1 or time_ch == 2 or time_ch == 3 or time_ch == 4:
        record_dict['time'] = time_list[time_ch]
        centre_sel()
    else:
        print("\nInvalid option")
        ret_2 = int(input("\nEnter 1 to retry. Enter any key to exit"))
        if ret_2 == 1:
            time_sel()
        else:
            sys.exit()


def centre_sel():
    centre_list = {1: "Ruby Hospital", 2: "City Hospital", 3: "Pearl Hospital"}
    print("\n")
    for i in centre_list:
        print(i, "--", centre_list[i])

    centre_ch = int(input("\nChoose the vaccination center: "))
    if centre_ch == 1 or centre_ch == 2 or centre_ch == 3:
        record_dict['centre'] = centre_list[centre_ch]
        vaccine_sel()
    else:
        print("\nInvalid option")
        ret_3 = int(input("\nEnter 1 to retry. Enter any key to exit"))
        if ret_3 == 1:
            centre_sel()
        else:
            sys.exit()


def vaccine_sel():
    vaccine_list = {1: "Covaxin", 2: "Covishield"}
    print("\n")
    for i in vaccine_list:
        print(i, "--", vaccine_list[i])
    vaccine_ch = int(input("\nSelect the vaccine: "))
    if vaccine_ch == 1 or vaccine_ch == 2:
        pass
    else:
        print("\nInvalid option")
        ret_4 = int(input("\nEnter 1 to retry. Enter any key to exit"))
        if ret_4 == 1:
            vaccine_sel()
        else:
            sys.exit()

    s_no = int(input("\nEnter the dose number(1 or 2): "))
    record_dict['shot no.'] = s_no

    if s_no == 1:
        record_dict['vaccine'] = vaccine_list[vaccine_ch]
        summary()
    elif s_no == 2:
        interval_ver(vaccine_list[vaccine_ch])
    else:
        print("\nInvalid option")
        ret_5 = int(input("\nEnter 1 to retry. Enter any key to exit"))
        if ret_5 == 1:
            vaccine_sel()
        else:
            sys.exit()


def interval_ver(vaccine):
    date_entry = input('\nEnter the date of first shot (YYYY-MM-DD format): ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = date(year, month, day)
    date_t = date.today()
    delta = (date_t - date1).total_seconds()                            #Convert timedate.delta to float(sec)

    if vaccine == 'Covaxin':
        if delta >= 2.419e+6:                                             #28 days to seconds
            record_dict['vaccine'] = 'Covaxin'
            summary()
        else:
            sys.exit("\nYou need to wait for 28 days after first Covaxin dose")
    elif vaccine == 'Covishield':
        if delta >= 7.258e+6:                                             #84 days to seconds
            record_dict['vaccine'] = 'Covishield'
            summary()
        else:
            sys.exit("\nYou need to wait for 84 days after first Covishield dose")


def summary():
    print("\nYOU HAVE SUCCESSFULLY REGISTERED FOR VACCINATION!!\n")
    print("Personal details")
    print("\t\tName: ", record_dict.get('name'))
    print("\t\tAge: ", record_dict.get('age'))
    print("\t\tAadhar no: ", record_dict.get('aadhar'))
    print("\nCentre details")
    print("\t\tCentre: ", record_dict.get('centre'))
    print("\t\tDate: ", record_dict.get('date'))
    print("\t\tTime: ", record_dict.get('time'))
    print("\nVaccine detail")
    print("\t\tVaccine name: ", record_dict.get('vaccine'))
    print("\t\tDose number: ", record_dict.get('shot no.'))
    database()


def database():
    db.personal(record_dict)
    db.medical(record_dict)

age_sel()
