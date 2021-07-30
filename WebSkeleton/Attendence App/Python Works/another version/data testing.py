from datetime import datetime



def namecheck(name,date):
    with open("Testingdata.csv", 'r+') as file:
        data = file.readlines()
        names = []
        dates=[]
        for x in data:
            xdata = x.split(",")
            names.append(xdata[0])
            dates.append(xdata[1])
        if((name not in names) and (date not in dates)):
            now=datetime.now()
            timedate = now.strftime("%d-%m-%Y %H:%M:%S")
            Attendence_Record_Date, Attendence_Record_Time = timedate.split(" ")
            dates.append(Attendence_Record_Date)
            file.writelines(f'\n{name},{Attendence_Record_Date},{Attendence_Record_Time}')

namecheck("Varun","25-07-21")