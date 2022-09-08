import sqlite3
con = sqlite3.connect("Election.db")
cur = con.cursor()
def Verify(Voter_id):
    print("Verifying...")
#     con = sqlite3.connect("Election.db")
#     cur = con.cursor()
    cur.execute("SELECT Voter_id,Nom_Voter_id from Voter,Nominee")
    rows = cur.fetchall()
#     con.close()
    a=[]
    for x in rows:
        a.append(rows[0])
        a.append(rows[1])
    if Voter_id in set(a):
        return True
    else:
        return False
        
#Calculate Age:
from datetime import date
 
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
 
    return age
     
#print(calculateAge(date(1997, 2, 3)))                
                
            
#Insert into Voter Table:
def addVoter():
    Voter_id =int(input("Enter Voter_ID: "))
    if len(str(Voter_id))!=6:
        print("Invalid Please Enter valid Voter_ID")
        return
    if Verify(Voter_id)==True:
        print("Data already present")
        return
    Voter_Name = input("Enter your Name: ")
    Voter_Location=input("Enter Your Location: ")
    DOB = input("Enter your DOB in YY-MM-DD format: ")
    yyyy,mm,dd=map(int,DOB.split("-"))
    DOB=date(yyyy,mm,dd)
    if calculateAge(date(yyyy,mm,dd))<18:
        print("Under age to Vote!")
        return
#     con = sqlite3.connect("Election.db")
#     cur = con.cursor()
    cur.execute("INSERT INTO Voter VALUES (?,?,?,?) ", (Voter_id,Voter_Name,Voter_Location,DOB))
    con.commit()
#     con.close()
    print("Data Inserted in Voter-List")
    return
        
        
        
        
    
def updateVoter():
    Voter_id =input("Enter your Voter_ID: ")
    if len(Voter_id)!=6:
        print("Invalid Please Enter6-digits valid Voter_ID")
        return
    if Verify(Voter_id)==False:
        Voter_Name = input("Enter your New Voter_Name: ")
        Voter_Location=input("Enter Your new Location: ")
        cur.execute("UPDATE Voter SET Voter_Name=?, Voter_Location=? WHERE Voter_id=?", (Voter_Name,Voter_Location,Voter_id))
        con.commit()
        print("Data updated successfully!")
        return
    else:
        print("Please Add Voter First")
        return
    
def addNominee():
    Nom_Voter_id =int(input("Enter Voter_ID: "))
    if len(str(Nom_Voter_id))!=6:
        print("Invalid Please Enter valid Nom_Voter_ID")
        return
    if Verify(Nom_Voter_id)==True:
        print("Data already present")
        return
    Nom_Name = input("Enter your Name: ")
    Nom_Location=input("Enter Your Location: ")
    DOB = input("Enter your DOB in YY-MM-DD format: ")
    yyyy,mm,dd=map(int,DOB.split("-"))
    DOB=date(yyyy,mm,dd)
    if calculateAge(date(yyyy,mm,dd))<28:
        print("Under age to Nominate")
        return
#     con = sqlite3.connect("Election.db")
#     cur = con.cursor()
    cur.execute("INSERT INTO Nominee VALUES (?,?,?,?) ", (Nom_Voter_id,Nom_Name,Nom_Location,DOB))
    con.commit()
#     con.close()
    print("Data Inserted in Nominee-List")
    return
        
    
def updateNominee():
    
    Nom_Voter_id =input("Enter your Nom_Voter_ID: ")
    if len(Nom_Voter_id)!=6:
        print("Invalid Please Enter6-digits valid Nom_Voter_ID")
        return
    if Verify(Nom_Voter_id)==False:
        Nom_Name = input("Enter your New Nom_Name: ")
        Nom_Location=input("Enter Your new Location: ")
        cur.execute("UPDATE Nominee SET Nom_Name=?, Nom_Location=? WHERE Nom_Voter_id=?", (Nom_Name,Nom_Location,Nom_Voter_id))
        con.commit()
        print("Data updated successfully!")
        return
    else:
        print("Please Add nominee First")
        return
        
        
def seeResult():
    cur.execute("SELECT * FROM Voter")
    rows = cur.fetchall()
    print("Total Vote Count is: ",len(rows))
    print("Nominee Name  |  Total Votes")
    L1={}
    for row in cur.execute("Select n.Nom_name,count(v.Nom_Voter_id) from Nominee n left join Voting_Details v on(n.Nom_Voter_id=v.Nom_Voter_id) group by Nom_Name"):#correct
        print(row[0],"  |  ",row[1])
        L1[row[0]]=row[1]
    v = list(L1.values())
    k = list(L1.keys())
    print("Winner: ",k[v.index(max(v))])
    return
    


def ViewVoter_Details():
    cur.execute("select * from Voting_Details")
    rows = cur.fetchall()
    return rows

def ViewVoter_():
    cur.execute("select * from Voter")
    rows = cur.fetchall()
   
    return rows

def ViewNominee():
    cur.execute("select * from Nominee")
    rows = cur.fetchall()
   
    return rows



def download():
    import csv
    h=['Voter_ID','Nominee_ID','Voting_Time']
    cur.execute("select * from Voting_Details")
    x = cur.fetchall()
    with open('Voting.csv','w') as f:
        w=csv.writer(f)
        w.writerow(h)
        for i in x:
            w.writerow(i)
    print("Downloaded! To see open C:/Drive/user & file name as Voting.csv")
    return
        
    
def validate(id):
    cur.execute('SELECT Voter_ID from Voter where Voter_ID={}'.format(id))
    x=cur.fetchall()
    for row in x:
        print(row)
        if id not in row:
            print("User not voted")
            return True
        elif id in row:
            print("User already voted")
            return False
    print("Enter valid Voter_Id")
    return False
            
def Voting_Details():
    import datetime as dt
    Timestamp = dt.datetime. now()
    Voter_id = input("Enter Voter_ID")
    Nom_Voter_ID =  input("Enter Nom_Voter_ID")
    cur.execute("INSERT INTO Voting_Details VALUES (?,?,?)",(Voter_id, Nom_Voter_ID,Timestamp))
    print("Voting added in Voting_Details!")
    con.commit()
    
    
def vote(id):
    #Voter_id = input("Enter Your Voter_ID: ")
    import datetime
    Voter_id=id
    L=[]
    x = cur.execute("Select Voter_id from Voting_Details")
    for row in x:
        L.append(row[0])
    if Voter_id in L:
        
        print("You have been already Voted!")
        return
    elif Voter_id not in L:
        L1=[]
        x = cur.execute("select Voter_id from Voter")
        for row in x:
            L1.append(row[0])
            if Voter_id not in L1:
                print("Invalid Voter_ID")
                return
        else:
            print("Nominee Name: ")
            x = cur.execute("select Nom_Voter_id,Nom_Name from Nominee")
            for row in x:
                print(row[0],")",row[1])
            inp=int(input("select one of the above Nominee(Enter Nominee_ID as above):  "))
            cur.execute("Insert into Voting_Details values (?,?,?)",(Voter_id,inp,datetime.datetime.now()))
            con.commit()
            print("Thanks for voting!")
            return
    else:
        print("Record not found!")
        return
                
   #E-Voting system:
def welcome():
    print("*****************************")
    print("Welcome to E-Voting system : ")
    print("*****************************")
    flag = True
    while flag:
        flag = False
        print("1. Voter \n2. Election Commision \n3. Exit")
        choice = int(input("Enter your response: "))
        if choice==0:
            print("=================")
            print("Thank you!")
            print("=================")
            break
            
        elif choice==1:
            print("---------------------------")
            print("Welcome to E-Voting portal!")
            print("---------------------------")
            id = int(input("Enter your Voter_ID: "))
            valid = False
            con = sqlite3.connect("Election.db")
            cur = con.cursor()
            cur.execute("select*from Voter")
            res = cur.fetchall()
            for row in res:
                if row[0]==id:
                    valid = True
                    user = row[1]
            if valid:
                print("******************************")
                print("Happy Voting!, {}".format(user))
                print("******************************")
                vote(id)
            else:
                print("Try again incorrect Voter_ID! ")
        
        elif choice==2:
            print("--------------------------------------")
            print("Welcome to Election-Commison Portal! :")
            print("--------------------------------------")
            print("1. Add Voter \n2. Update Voter \n3. Add Nominee \n4. Update Nominee \n5. See Result \n6. Download Result")
            print("--------------------------------------")
            r = int(input("Enter your response: "))
            
            if r ==1:
                print("Add Voter: ")
                addVoter()
            elif r==2:
                print("Update Voter: ")
                updateVoter()
            elif r==3:
                print("Add Nominee: ")
                addNominee()
            elif r==4:
                print("Update Nominee: ")
                updateNominee()
            elif r==5:
                print("See Result: ")
                print(seeResult())
            elif r==6:
                print("Download Result in CSV form: ")
                download()
            else:
                print("Invalid Response Try again!")
                
        else:
            print("Thank you!...exit")
                
                