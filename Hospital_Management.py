import mysql.connector
import random
from tabulate import tabulate
from datetime import datetime
pss=input("Enter your database password: ")
cn=mysql.connector.connect(host="localhost", user="root" , passwd=pss)
c=cn.cursor()
#Creating DATABASE
c.execute("Create Database if not exists hospital")
c.execute("Use hospital")
#Creating Table for patients
c.execute("create table  if not exists patient\
(name varchar(33),gender varchar(10),address varchar(100),\
aadhar varchar(12),email varchar(100),\
contact varchar(10),docid int,ptid int unique)")
#Inserting Data for patients
c.execute("insert ignore into patient values('Shyam kumar','Male','Aruna Nagar,Etah','347578686543',\
'shyam.kumar@xyz.com','9867966786',9,101)")
c.execute("insert ignore into patient values('Vineet Mishra','Male','Kasganj Road,Etah','127454686543',\
'vineet@gmail.com','9867934091',1,105)")
c.execute("insert ignore into patient values('Shyama Devi','Female','Shanti Nagar,Etah','347578123456',\
'mrsshyama@yahoo.com','4445666786',9,107)")
#Creating table for doctors
c.execute("create table if not exists doctors\
(name varchar(20) ,gender varchar(10),\
aadhar bigint(12) ,\
speciality varchar(20),\
department varchar(30),\
mobile bigint(10),\
fees integer,\
docid int primary key)")
#Inserting Data for doctors
c.execute("insert ignore into doctors values('Vishal Kumar','Male',688696974467,'Cardiologist','Surgical Department'\
          ,7687656780,1000,1)")
c.execute("insert ignore into doctors values('Palak Jha','Female',965432458750,'Physician','Outpatient Department'\
          ,7698787659,500,9)")
c.execute("insert ignore into doctors values('Kusum Singhal','Female',122334577500,'Physical Surgeon','Surgical Department'\
          ,1234667880,2000,5)")
cn.commit()

#Function for patient's details entry
def adm ():
    print("\n\n         ____ENTER PATIENT DETAILS____\n")
    while True:
        pt_name=input("Enter Patient's name: ")
        pt_gender=input("Patient's Gender: ")
        pt_address=input("Enter Patient's address: ")
        pt_aadhar=int(input("Enter Patient's aadhar no.: "))
        pt_email=input("Enter Patient's email id: ")
        pt_contact=int(input("Enter Patient's contact no.: "))
        pt_doc=int(input("Enter ID of the Doctor assigned: "))
        pt_id=random.randint(110,200)
        insert="insert into patient values ('{}','{}','{}',{},'{}',{},{},{})".format(pt_name,pt_gender,pt_address,pt_aadhar,pt_email,pt_contact,pt_doc,pt_id)
        c.execute(insert)
        cn.commit()
        print("Patient's ID is :",pt_id)
        print("Data entered successfully...!")
        yes=int(input("Press 1 to add more\nPress 2 to exit\nYour choice:"))
        if yes==2:
            break
#Function for viewing patient's details
def pt_detailsview():
    k=int(input("\nEnter Patient's ID: "))
    c.execute("select * from patient where ptid={}".format(k))
    print(c.fetchone())

#Function for updating patient's details
def pt_upd():
    print("From the following list select the Patient you want to update:--->>\n")
    c.execute("select * from patient")
    z=c.fetchall()
    for i in z:
        print(i)
    y=int(input("\n\nEnter Patient's ID you want to update: "))
    print("Select what you want to update:--->>\n"
           ," \n 1. Patient's name  ","\n 2. Patient's address","\n 3. Patient's aadhar",
          "\n 4. Patient's email","\n 5. Patient's mobile No.","\n 6. Patient's Gender")
    x=int(input("Enter your choice:  "))
    if x==1:
        choice="name"
    if x==2:
        choice="address"
    if x==3:
        choice="aadhar"
    if x==4:
        choice="email"
    if x==5:
        choice="contact"
    if x==6:
        choice="gender"
    cv=input("Enter the corrected value: ")
    query="update patient set {} = '{}' where ptid={}".format(choice,cv,y)
    c.execute(query)
    cn.commit()
    print("Data corrected successfully:---->>> ")
    c.execute("select * from patient where ptid={}".format(y))
    print(c.fetchone())

#Function for  entering the details of the doctor
def doctor():
    print(" \n\n                 ____ENTER DOCTOR'S DETAILS____")
    while True:
        doc_name=input("\nEnter the name of the doctor: ")
        doc_gender=input("Doctor's Gender: ")
        doc_aadhar=int(input("Enter the Aadhar number of the doctor: "))
        doc_spec=input("Enter the doctor's speciality: ")
        doc_dep=input("Enter the doctor's department: ")
        doc_mob=int(input("Enter the doctor's mobile number: "))
        doc_fees=int(input("Enter Doctor's fees: "))
        doc_id=random.randint(10,99)
        query="insert into doctors values('{}','{}',{},'{}','{}',{},{},{})".format(doc_name,doc_gender,doc_aadhar,doc_spec,doc_dep,doc_mob,doc_fees,doc_id)
        c.execute(query)
        cn.commit()
        print("Doctor's Id is : ",doc_id)
        print("Data entered successfully...!")
        x=int(input("\nPress 1 to add more \nPress 2 to exit \nYour Choice:  "))
        if x==2:
            break

#function for updation of details of doctor
def doc_upd():
    c.execute("select * from doctors")
    z=c.fetchall()
    print("From the following list select the Doctor you want to update:--->>\n")
    for i in z:
        print("\n",i)
    y=int(input("\nEnter Doctor's ID you want to update: "))
    print("\nSelect what you want to update:--->>\n"
                 ," \n 1. Doctor's name  ","\n 2. Doctor's aadhar","\n 3. Doctor's speciality","\n 4. Doctor's department",
                  "\n 5. Doctor's mobile No.","\n 6. Doctor's Gender")
    x=int(input("Enter your choice:  "))
    if x==1:
        choice="name"
    if x==2:
        choice="aadhar"
    if x==3:
        choice="speciality"
    if x==4:
        choice="department"
    if x==5:
        choice="mobile"
    if x==6:
        choice="gender"
    cv=input("Enter the corrected value: ")
    query="update doctors set {} = '{}' where docid={}".format(choice,cv,y)
    c.execute(query)
    cn.commit()
    print("Data corrected successfully:---->>> ")
    c.execute("select * from doctors where docid={}".format(y))
    print(c.fetchone())

#Function for removal of doctor
def doc_del():
    j=int(input("\nEnter the doctor's ID to be removed from the database: "))
    c.execute("select * from doctors where docid={}".format(j))
    r=c.fetchone()
    print("Do you want to Permanently delete this record:---->>>\n")
    print(r)
    rv=int(input("Press 1 for Yes \nPress 2 for No \nYour Choice: "))
    if rv==1:
        query="delete from doctors where docid={}".format(j)
        c.execute(query)
        cn.commit()
        print("Doctor removed successfully..!")
    else:
        main_menu()
#Creating Treatment Table for existing Patients

c.execute("create table if not exists patient101(ptid int,Dt date unique,xraycount int,xraycost int,bloodcount int,bloodcost int,\
mricount int,mricost int,docfees int,other int,icu_charge int default 5000,amount int)")
c.execute("create table if not exists patient105(ptid int,Dt date unique,xraycount int,xraycost int,bloodcount int,bloodcost int,\
mricount int,mricost int,docfees int,other int,icu_charge int default 5000,amount int)")
c.execute("create table if not exists patient107(ptid int,Dt date unique,xraycount int,xraycost int,bloodcount int,bloodcost int,\
mricount int,mricost int,docfees int,other int,icu_charge int default 5000,amount int)")

#Inserting Values into above tables

c.execute("insert ignore into patient101 values(101,20221111,2,400,0,0,1,1000,500,450,5000,7350)")
c.execute("insert ignore into patient101 values(101,20221112,1,200,2,300,0,0,500,130,5000,6130)")
c.execute("insert ignore into patient101 values(101,20221113,3,600,0,0,1,1000,500,250,5000,7350)")
c.execute("insert ignore into patient105 values(105,20221001,3,600,3,450,1,1000,1000,550,5000,7600)")
c.execute("insert ignore into patient105 values(105,20221002,0,0,0,0,2,2000,1000,850,5000,8350)")
c.execute("insert ignore into patient105 values(105,20221003,2,400,1,150,1,1000,1000,200,5000,7250)")
c.execute("insert ignore into patient107 values(107,20221121,4,800,2,300,2,2000,500,120,5000,8720)")
c.execute("insert ignore into patient107 values(107,20221122,2,400,3,450,0,0,500,130,5000,6380)")
cn.commit()


#Function for Patient treatment information


def pt_treatment():
    k=int(input("Enter Patient's ID: "))
    c.execute("create table if not exists patient{}\
    (ptid int,Dt date unique,xraycount int,xraycost int,bloodcount int,bloodcost int,\
mricount int,mricost int,docfees int,other int,icu_charge int default 5000,amount int)".format(k))
    z=int(input("Enter the No. of Days of Stay: "))
    m,u=0,0
    icu=5000
    c.execute("select fees from patient,doctors where patient.docid=doctors.docid and ptid={}".format(k))
    xyz=c.fetchone()
    for i in xyz:
        docfees=i
    while True:
        m=m+1
        u=u+1
        dt_adm=int(input(f"Enter the date for Day {u} (YYYYMMDD): "))
        dt_str=str(dt_adm)
        print("\nEnter data for",dt_str[6:8],"-",dt_str[4:6],"-",dt_str[0:4],"--->>")
        xraycount=int(input("Enter the number of X-rays done: "))
        xray_cost=xraycount*200
        bloodcount=int(input("Enter the number of blood test done: "))
        bloodcost=bloodcount*150
        mricount=int(input("Enter the number of MRI done: "))
        mricost=mricount*1000
        other=int(input("Any Other Expenses: "))
        amount=xray_cost+bloodcost+mricost+docfees+other+5000
        c.execute("insert into patient{} values({},{},{},{},{},{},{},{},{},{},{},{})".format(k,k,dt_adm,xraycount,
                        xray_cost,bloodcount,bloodcost,mricount,mricost,docfees,other,icu,amount))
        dt_adm=dt_adm+1
        br=int(input("Press 1 to add information for next day\nPress 2 for main menu\nYour Choice: "))
        cn.commit()
        if br==2:
            break
        elif m==z:
            print("\nAll entries are already done for given number of Days")
            break

#Function for viewing Patient's Treatment History
def pt_totalview():
    l=[]
    x=int(input("Enter the Patient's ID to be searched: "))
    c.execute("select * from patient where ptid={}".format(x))
    nm=c.fetchone()
    print("\n\n\nName of the Patient: ",nm[0])
    print("Gender: ",nm[1])
    print("Patient's Contact Number: ",nm[5])
    print("Patient's email: ",nm[4])
    c.execute("select * from doctors where docid={}".format(nm[6]))
    dm=c.fetchone()
    print("Doctor treating the patient: Dr.",dm[0],"(",dm[3],")")
    print("Doctor's Contact Number: ",dm[5])
    print("Doctor's Fees per Day: Rs",dm[6])
    print("ICU charges per Day: Rs 5000")
    print("Xray charges: Rs 200")
    print("Blood Test Charges: Rs 150")
    print("MRI Charges: Rs 1000\n\n\n")
    print("Patient's Per day Expenses are :------->>>\n")
    c.execute("select * from patient{}".format(x))
    km=c.fetchall()
    for i in km:
        l.append(i)
    print(tabulate(l,headers=["Pt. ID","Date","X-Rays Nos","X-Ray Cost","Bd Tests Nos",
                   "Blood Test Cost","MRI Nos","MRI Cost","Doc's Fees","Other Expenses","ICU Charges","Total"]  
                              ,tablefmt="fancy_grid"))

#Function for Bill Making of the Patient        
def bill():
    s=[]
    insy=0
    x=int(input("Enter the Patient's ID to be searched: "))
    ins=int(input("Do you have insurance \nPress 1 for Yes \nPress 2 for No \nYour choice:"))
    if ins==1:
        inscd=input("Enter Insurance Code:")
        if inscd in ("acs001","acs002","acs003","acs004","acs005"):
            print("Congrats You have claimed your Insurance!")
            insy=1
        else:
            print("Invalid code :(")
    else:
        print("Better luck next time !")
    print("\n\n     --------------------------------------------------------------------------\n\
    ---------------------------- Assisi Charitable Hospital--------------------\n\
    -----------------------------------------------------------------------------\
    \n\n")
    print("             'Medicines cure Disease, but only doctors can cure patients'\n\n")
    print("\n\n\n                                    Final Bill")
    c.execute("select * from patient where ptid={}".format(x))
    xy=c.fetchall()
    c.execute("select DT from patient{}".format(x))
    yz=c.fetchall()
    dtadm=yz[0][0]
    c.execute("select doctors.name from doctors,patient where\
               doctors.docid=patient.docid and ptid={}".format(x))
    uv=c.fetchall()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    billno=random.randint(10000000,99999999)
    print("_______________________________________________________________________________________")
    print("\n Patient's ID: ",x,"                       Bill NO.:AC",billno)
    print(" Patient's Name:",xy[0][0],"             Billing Date and Time:",dt_string)
    print(" Gender:",xy[0][1],"                            Date of Visit:",dtadm)
    print(" Patient's Contact Number:",xy[0][5],"          Consulting Doctor:",uv[0][0])     
    print(" Patient's email:",xy[0][4],"            Invoice No.:GST",random.randint(100000,999999))
    print("_______________________________________________________________________________________")

    c.execute("select * from patient{}".format(x))
    bil=c.fetchall()
    for i in bil:
        s.append(i)
    print("\n\n                                     Bill Summary",
          "\n                                     -------------\n\n")
    xrcnt=0
    blcnt=0
    mrcnt=0
    other=0
    icu=0
    docfs=0
    for i in range(0,len(s)):
        xrcnt=xrcnt+s[i][2]
        blcnt=blcnt+s[i][4]
        mrcnt=mrcnt+s[i][6]
        other=other+s[i][9]
        icu=icu+s[i][10]
        docfs=docfs+s[0][8]
    xrcst=xrcnt*200
    blcst=blcnt*150
    mrcst=mrcnt*1000
    final=xrcst+blcst+mrcst+docfs+icu+other
    tax=final*0.05
    if insy==1:
        insurance=(final+tax)*0.2
    else:
        insurance=0
    bill=[[1,"Xray Cost",xrcst],[2,"Blood Test Cost",blcst],[3,"MRI cost",mrcst],
          [4,"Doctor's fees",docfs],[5,"ICU Charges",icu],[6,"Other Charges",other],
          [7,"Taxes(5%)",tax],[8,"Insurance Discount(20%)",f"-{insurance}"],
          ["","Final Amount",tax+final-insurance]]
    print(tabulate(bill,headers=["S.No.","Particulars","Cost"],tablefmt="fancy_grid"))
    print("\n\n                              Thanks For Visiting ✿\
                    \n                       We Wish you a very speedy recovery :)")

    dlr=int(input("\nWant to Delete this record from the Database?\nPress 1 for yes\
\nand 2 for no \nYour Choice:"))
    if dlr==1:
        c.execute("drop table patient{}".format(x))
        c.execute("delete from patient where ptid={}".format(x))

def main_menu():
    print("\n\n     --------------------------------------------------------------------------\n\
    ----------------------Welcome To Assisi Charitable Hospital------------------\n\
    -----------------------------------------------------------------------------\
    \n\nPlease Select what you want to do:------>>>\n\n")
    print("1. Doctor's Entry ","\n2. Update Doctor's Info","\n3. Delete Doctor's Record",
          "\n4. Patient's Entry ","\n5. View Patient's Basic detail ","\n6. Update Patient's Info",
            "\n7. Enter Patient's Treatment Details","\n8. View Patient's Treatment Expenses ",
          "\n9. Final Bill")
    sel=int(input("\n\nEnter your Choice : "))
    if sel==1:
        doctor()
    if sel==2:
        doc_upd()
    if sel==3:
        doc_del()
    if sel==4:
        adm()
    if sel==5:
        pt_detailsview()
    if sel==6:
        pt_upd()
    if sel==7:
        pt_treatment()
    if sel==8:
        pt_totalview()
    if sel==9:
        bill()
    main_menu()
main_menu()        



