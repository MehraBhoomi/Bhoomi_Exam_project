import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date

def AutoGenerate_EventID():
    #generate a random Event ID
    Event_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Event_ID

def Register(type,member_json_file,organizer_json_file,Full_Name,Email,Password):
    '''Register the member/ogranizer based on the type with the given details'''
    if type.lower()=='organizer':
        f=open(organizer_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    else:
        f=open(member_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()


def Login(type,members_json_file,organizers_json_file,Email,Password):
    '''Login Functionality || Return True if successful else False'''
    d=0
    if type.lower()=='organizer':
        f=open(organizers_json_file,'r+')
    else:
        f=open(members_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            d=1
            break
    if d==0:
        f.close()
        return False
    f.close()
    return True

def Create_Event(org,Event_Name,Start_Date,Start_Time,End_Date,End_Time,seats):
    '''Create an Event with the details entered by organizer'''
    Event_ID = random.randint(35678,9874637)
    d={
        "org":org,
        "ID":Event_ID,
        "Name":Event_Name,
        "Organizer":org,
        "Start Date":Start_Date,
        "Start Time":Start_Time,
        "End Date": End_Date,
        "End Time":End_Time,
        "seats":seats
    }
    f=open("events.json",'r')
    try:
        Content=json.load(f)
        if d not in Content:
            Content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(Content,f)
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l,f)
    f.close() 
    return False

def View_Events(org,events_json_file):
    '''Return a list of all events created by the logged in organizer'''
    '''Return a list of all events created by the logged in organizer'''
    org=input()
    f=open(events_json_file,'r')
    for sub in f:
      if sub['org']==org:
        print(sub.items())
    f.close()    

def View_Event_ByID(events_json_file,Event_ID):
    '''Return details of the event for the event ID entered by user'''
    Details=[]
    f=open(events_json_file,'r+')
    content2=json.load(f)
    for i in range(len(content2)):
        if content2[i]['ID']==Event_ID:
            Details.append(content2[i])
            break
    f.close()
    return Details   

def Update_Event(org,events_json_file,event_id,detail_to_be_updated,updated_detail):
    '''Update Event by ID || Take the key name to be updated from member, then update the value entered by user for that key for the selected event
    || Return True if successful else False'''
    f=open(events_json_file,'r+')
 
    content3=json.load(f)
    for i in range(len(content3)):
        if content3[i]["Organizer"]==org and content3[i]['ID']==event_id:
            content3[i][detail_to_be_updated]=updated_detail
            f.seek(0)
            f.truncate()
            json.dump(content3,f)
            f.close()
            return True
    f.close()
    return False    

def Delete_Event(org,events_json_file,event_ID):
    '''Delete the Event with the entered Event ID || Return True if successful else False'''
    f=open(events_json_file,'r+')
    content4=json.load(f)
    for i in range(len(content4)):
        if content4[i]["ID"]==event_ID and content4[i]['Organizer']==org:
            del content4[i]
            f.seek(0)
            f.truncate()
            json.dump(content4,f)
            f.close()
            return True
    f.close()
    return False


def Register_for_Event(events_json_file,event_id,Full_Name):
    '''Register the logged in member in the event with the event ID entered by member. 
    (append Full Name inside the "Users Registered" list of the selected event)) 
    Return True if successful else return False'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
    event_id=input()
    f=open(events_json_file,'r')
    content=json.load(f)
    for sub in f:
      if sub ['Event_ID']==event_id:
        d={
            "fullname":Full_Name
        }
        f=open(events_json_file,'w')
        json.dump(d,f)
      return True
    else:
      return False
    f.close()       

def fetch_all_events(events_json_file,Full_Name,event_details,upcoming_ongoing):
    '''View Registered Events | Fetch a list of all events of the logged in memeber'''
    '''Append the details of all upcoming and ongoing events list based on the today's date/time and event's date/time'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    '''Write your code below this line'''
    date_today=str(date.today())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(date_today)
    print(current_time)
    '''Write your code below this line'''
 
    
    event_id=input()
    f=open(events_json_file,'r')
    for sub in f:
       if sub['Event_ID']==event_id:
           print(sub.items())
    f.close()    

def Update_Password(members_json_file,Full_Name,new_password):
    '''Update the password of the member by taking a new passowrd || Return True if successful else return False'''
    f=open(members_json_file,'r+')
    content7=json.load(f)
    for i in range(len(content7)):
        if content7[i]["Full Name"]==Full_Name:
            content7[i]["Password"]=new_password
            f.seek(0)
            f.truncate()
            json.dump(content7,f)
            f.close()
            return True
    f.close()
    return False    

def View_all_events(events_json_file):
    '''Read all the events created | DO NOT change this function'''
    '''Already Implemented Helper Function'''
    details=[]
    f=open(events_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details