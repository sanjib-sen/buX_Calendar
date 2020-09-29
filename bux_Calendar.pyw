from tkinter import *
from tkinter import ttk
import tkinter as tk
from bs4 import BeautifulSoup as bs
import requests
import re
import threading
from datetime import date
today = date.today()
date1 = today.strftime("%Y-%m-%d")


s = requests.session()
text=""
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        canvas.config(width=500, height=400)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        canvas.bind_all("<MouseWheel>",
            lambda event: canvas.yview_scroll( int(-1*(event.delta/120)), "units")
        )
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        

        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(self, event):
        self.yview_scroll(-1*(event.delta/120), "units")

file4 = open('courses', 'r')
listcourses = file4.readlines()
file4.close()

def one():
    file4 = open('courses', 'r')
    listcourses = file4.readlines()
    file4.close()
    course = listcourses[0]
    url = "https://bux.bracu.ac.bd" + course.split()[1]
    t = threading.Thread(target=datecheck(url, course.split()[0]))
    t.daemon = True
    t.start()

def two():
    file4 = open('courses', 'r')
    listcourses = file4.readlines()
    file4.close()
    course = listcourses[1]
    url = "https://bux.bracu.ac.bd" + course.split()[1]
    t = threading.Thread(target=datecheck(url, course.split()[0]))
    t.daemon = True
    t.start()

def three():
    file4 = open('courses', 'r')
    listcourses = file4.readlines()
    file4.close()
    course = listcourses[2]
    url = "https://bux.bracu.ac.bd" + course.split()[1]
    t = threading.Thread(target=datecheck(url, course.split()[0]))
    t.daemon = True
    t.start()

def four():
    file4 = open('courses', 'r')
    listcourses = file4.readlines()
    file4.close()
    course = listcourses[3]
    url = "https://bux.bracu.ac.bd" + course.split()[1]
    t = threading.Thread(target=datecheck(url, course.split()[0]))
    t.daemon = True
    t.start()

def five():
    file4 = open('courses', 'r')
    listcourses = file4.readlines()
    file4.close()
    course = listcourses[4]
    url = "https://bux.bracu.ac.bd" + course.split()[1]
    t = threading.Thread(target=datecheck(url, course.split()[0]))
    t.daemon = True
    t.start()

def six():
    file4 = open('courses', 'r')
    listcourses = file4.readlines()
    file4.close()
    course = listcourses[5]
    url = "https://bux.bracu.ac.bd" + course.split()[1]
    t = threading.Thread(target=datecheck(url, course.split()[0]))
    t.daemon = True
    t.start()


def createbtn1(window):
    rw = 5
    crsbtn1 = Button(window, text="See Tasks", anchor='center', command=one).grid(row=rw, column=2)

def createbtn2(window):
    rw = 5
    crsbtn1 = Button(window, text="See Tasks", anchor='center', command=one).grid(row=rw, column=2)
    rw +=1
    crsbtn2 = Button(window, text="See Tasks", anchor='center', command=two).grid(row=rw, column=2)

def createbtn3(window):
    rw = 5
    crsbtn1 = Button(window, text="See Tasks", anchor='center', command=one).grid(row=rw, column=2)
    rw +=1
    crsbtn2 = Button(window, text="See Tasks", anchor='center', command=two).grid(row=rw, column=2)
    rw +=1
    crsbtn3 = Button(window, text="See Tasks", anchor='center', command=three).grid(row=rw, column=2)

def createbtn4(window):
    rw = 5
    crsbtn1 = Button(window, text="See Tasks", anchor='center', command=one).grid(row=rw, column=2)
    rw +=1
    crsbtn2 = Button(window, text="See Tasks", anchor='center', command=two).grid(row=rw, column=2)
    rw +=1
    crsbtn3 = Button(window, text="See Tasks", anchor='center', command=three).grid(row=rw, column=2)
    rw +=1
    crsbtn4 = Button(window, text="See Tasks", anchor='center', command=four).grid(row=rw, column=2)
    
def createbtn5(window):
    rw = 5
    crsbtn1 = Button(window, text="See Tasks", anchor='center', command=one).grid(row=rw, column=2)
    rw +=1
    crsbtn2 = Button(window, text="See Tasks", anchor='center', command=two).grid(row=rw, column=2)
    rw +=1
    crsbtn3 = Button(window, text="See Tasks", anchor='center', command=three).grid(row=rw, column=2)
    rw +=1
    crsbtn4 = Button(window, text="See Tasks", anchor='center', command=four).grid(row=rw, column=2)
    rw +=1
    crsbtn5=Button(window, text="See Tasks", anchor='center', command=five).grid(row=rw, column=2)
    
def createbtn6(window):
    rw = 5
    crsbtn1 = Button(window, text="See Tasks", anchor='center', command=one).grid(row=rw, column=2)
    rw +=1
    crsbtn2 = Button(window, text="See Tasks", anchor='center', command=two).grid(row=rw, column=2)
    rw +=1
    crsbtn3 = Button(window, text="See Tasks", anchor='center', command=three).grid(row=rw, column=2)
    rw +=1
    crsbtn4 = Button(window, text="See Tasks", anchor='center', command=four).grid(row=rw, column=2)
    rw +=1
    crsbtn5=Button(window, text="See Tasks", anchor='center', command=five).grid(row=rw, column=2)
    rw +=1
    crsbtn6 = Button(window, text="See Tasks", anchor='center', command=six).grid(row=rw, column=2)

def datecheck(url, curs):
    notes =""
    soup = bs(s.get(url).text, 'html.parser')

    notes+="\n\n Showing Tasks for Course : "+ curs+ "\n\n"
    for a in soup.findAll("li", {"class": "subsection accordion"}):
        b = a.find("span", {"class": "localized-datetime subtitle-name"}, "data-datetime")
        month = {'01': 'January',
                '02': 'February',
                '03': 'March',
                '04': 'April',
                '05': 'May',
                '06': 'June',
                '07': 'July',
                '08': 'August',
                '09': 'September',
                '10': 'October',
                '11': 'November',
                '12': 'December'}
        if b != None and len(b['data-datetime'])>10:
            c = a.find("h4", {"class": "subsection-title"})
            count = b['data-datetime'][5:7]
            intcount = int(b['data-datetime'][5:7])
            time = int(b['data-datetime'][11:13])
            time += 6
            strdate = b['data-datetime'][8:10]
            date = int(strdate);
            mins = b['data-datetime'][14:16]
            if (time == 24):
                time = 11
                mins = '59'
                if (date == 0):
                    intcount -= 1
                    if (count[0] == '0'):
                        count += '0' + str(intcount)
                    else:
                        count += str(intcount)
                    if (intcount == 4 or intcount == 6 or intcount == 9 or intcount == 11):
                        date = 30
                    else:
                        date = 31
                
            notes += "    " + month[count] + "  " + str(date) + " at " + str(time) + ":" + mins + " :    " + c.text.rstrip().lstrip() + "\n"
    view(notes)

def allDueCheck():
    file4 = open('courses', 'r')
    listcourses = file4.readlines()
    file4.close()
    notes=""
    for course in listcourses:
        url = "https://bux.bracu.ac.bd" + course.split()[1]
        soup = bs(s.get(url).text, 'html.parser')
        notes+="\n\n Showing Tasks for Course : "+ course.split()[0]+ "\n\n"
        for a in soup.findAll("li", {"class": "subsection accordion"}):
            b = a.find("span", {"class": "localized-datetime subtitle-name"}, "data-datetime")
            month = {'01': 'January',
                    '02': 'February',
                    '03': 'March',
                    '04': 'April',
                    '05': 'May',
                    '06': 'June',
                    '07': 'July',
                    '08': 'August',
                    '09': 'September',
                    '10': 'October',
                    '11': 'November',
                    '12': 'December'}
            if b != None and len(b['data-datetime'])>10 and b['data-datetime'][:11]>date1:
                c = a.find("h4", {"class": "subsection-title"})
                count = b['data-datetime'][5:7]
                intcount = int(b['data-datetime'][5:7])
                time = int(b['data-datetime'][11:13])
                time += 6
                strdate = b['data-datetime'][8:10]
                date = int(strdate);
                mins = b['data-datetime'][14:16]
                if (time == 24):
                    time = 11
                    mins = '59'
                    if (date == 0):
                        intcount -= 1
                        if (count[0] == '0'):
                            count += '0' + str(intcount)
                        else:
                            count += str(intcount)
                        if (intcount == 4 or intcount == 6 or intcount == 9 or intcount == 11):
                            date = 30
                        else:
                            date = 31
                
                notes +="    "+ month[count]+"  " +str(date)+" at "+str(time)+":"+mins+ " :    " + c.text.rstrip().lstrip() + "\n"
    view(notes)

def allDatecheck():
    file4 = open('courses', 'r')
    listcourses = file4.readlines()
    file4.close()
    notes=""
    for course in listcourses:
        url = "https://bux.bracu.ac.bd" + course.split()[1]
        soup = bs(s.get(url).text, 'html.parser')
        notes += "\n\n Showing Tasks for Course : " + course.split()[0] + "\n\n"
        for a in soup.findAll("li", {"class": "subsection accordion"}):
            b = a.find("span", {"class": "localized-datetime subtitle-name"}, "data-datetime")
            month = {'01': 'January',
                    '02': 'February',
                    '03': 'March',
                    '04': 'April',
                    '05': 'May',
                    '06': 'June',
                    '07': 'July',
                    '08': 'August',
                    '09': 'September',
                    '10': 'October',
                    '11': 'November',
                    '12': 'December'}
            if b != None and len(b['data-datetime'])>10:
                c = a.find("h4", {"class": "subsection-title"})
                count = b['data-datetime'][5:7]
                intcount = int(b['data-datetime'][5:7])
                time = int(b['data-datetime'][11:13])
                time += 6
                strdate = b['data-datetime'][8:10]
                date = int(strdate);
                mins = b['data-datetime'][14:16]
                if (time == 24):
                    time = 11
                    mins = '59'
                    if (date == 0):
                        intcount -= 1
                        if (count[0] == '0'):
                            count += '0' + str(intcount)
                        else:
                            count += str(intcount)
                        if (intcount == 4 or intcount == 6 or intcount == 9 or intcount == 11):
                            date = 30
                        else:
                            date = 31
                notes += "    " + month[count] + "  " + str(date) + " at " + str(time) + ":" + mins + " :    " + c.text.rstrip().lstrip() + "\n"
    view(notes)

def view(text):
    window2 = tk.Tk()
    window2.title('Tasks')
    window2.resizable(False,False)
    frame = ScrollableFrame(window2)
    ttk.Label(frame.scrollable_frame, text=text).pack()
    frame.pack()
    window2.mainloop()

def showAllDates():
    
    t = threading.Thread(target=allDatecheck())
    t.daemon = True 
    t.start()
def showAllDues():
    t = threading.Thread(target=allDueCheck())
    t.daemon = True 
    t.start()

def signin():
    root = tk.Tk()
    root.geometry('250x200')
    root.resizable(False, False)
    root.title('Login')
    top = Label(root, text = "        ").grid(row =0)
    mlp = Label(root, text="buX Email  ").grid(row=1, column=1)
    em = Entry(root, width=20)
    em.grid(row=1, column=2)
    brk1 = Label(root, text ="").grid(row = 2)
    sltp = Label(root, text="Password ").grid(row=3, column=1)
    ep = Entry(root, width = 20,show="*")
    ep.grid(row=3, column=2)
    brk4 = Label(root, text="").grid(row=4)
    myButton = Button(root, text="Login", anchor='center', command=lambda:get_Courses(em.get(),ep.get(),root)).grid(row=5, column=2)
    root.mainloop()
def authentication():
    filehand = open('.config', 'r')
    read = filehand.readline()
    mail = read.split()[0]
    passwd = read.split()[1]
    URL = 'https://bux.bracu.ac.bd/'
    LOGIN_ROUTE = 'login_ajax'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36', 'origin': URL, 'referer': URL + LOGIN_ROUTE}
    csrf_token = s.get(URL).cookies['csrftoken']
    login_payload = {
        'email': mail,
        'password': passwd,
        'remember': 'true',
        'csrfmiddlewaretoken': csrf_token
        }

    login_req = s.post(URL + LOGIN_ROUTE, headers=HEADERS, data=login_payload)
    status=login_req.status_code
    if (status != 200):
        return False
    cookies = login_req.cookies
    return True

def session():
    filehand = open('.config', 'r')
    read = filehand.readline()
    mail = read.split()[0]
    passwd = read.split()[1]
    URL = 'https://bux.bracu.ac.bd/'
    LOGIN_ROUTE = 'login_ajax'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36', 'origin': URL, 'referer': URL + LOGIN_ROUTE}
    csrf_token = s.get(URL).cookies['csrftoken']
    login_payload = {
        'email': mail,
        'password': passwd,
        'remember': 'true',
        'csrfmiddlewaretoken': csrf_token
        }
    login_req = s.post(URL + LOGIN_ROUTE, headers=HEADERS, data=login_payload)
    status=login_req.status_code

def courseupdate(wind):
    filehand = open('.config', 'r')
    line = filehand.readline()
    filehand.close()
    get_Courses(line.split()[0],line.split()[1],wind)

def get_Courses(a, b, root):
    
    filehand = open('.config', 'w')
    wr = a + " " + b
    filehand.write(wr)
    filehand.close()
    root.destroy()
    session()
    soup = bs(s.get('https://bux.bracu.ac.bd/dashboard').text, 'html.parser')
    dct = {}
    for a in soup.find_all('a', href=re.compile("/courses/course-v1:buX")):
        datas = a['href']
        key = datas[23:29]
        if not key in dct.keys() and key != "/cours":
            dct[key] = datas
        else:
            continue
    file2 = open('courses', 'w');
    for crs in dct:
        name = crs + " " + dct[crs] + "\n"
        file2.write(name)
    file2.close()
    dashboard()

def logout(wind):
    file2 = open('courses', 'w');
    file2.write("")
    file3 = open('.config', 'w')
    file3.write("")
    file2.close()
    file3.close()
    wind.destroy()
    signin()

def dashboard():
    session()
    file3 = open('.config', 'r')
    file3read = file3.readline()
    user = file3read.split(" ")[0]
    file3.close()
    username = "Account:   "+user
    window = tk.Tk()
    window.title('Dashboard')
    window.geometry('500x500')
    window.resizable(False, False)
    win1label1 = Label(window, text = "").grid(row =0)
    win1label2 = Label(window, text=username).grid(row=1, column=1)
    win1label3 = Label(window, text="\n"+"Enrolled Courses:").grid(row=3, column=1)
    file4 = open('courses', 'r')
    listcourses = file4.readlines()
    file4.close()
    rw = 5
    i=0
    for each in listcourses:
        win1label4 = Label(window, text="\n" + each[:6] + "   \n").grid(row=rw, column=1)
        rw += 1
        i += 1
    
    if (i == 1):
        createbtn1(window)
    elif (i == 2):
        createbtn2(window)
    elif (i == 3):
        createbtn3(window)
    elif (i == 4):
        createbtn4(window)
    elif (i == 5):
        createbtn5(window)
    elif (i == 6):
        createbtn6(window)
    alldates = Button(window, text="See All Tasks", anchor='center',command=showAllDates).grid(row=rw + 1, column=1)
    duedatesdates = Button(window, text="See All Due Tasks", anchor='center',command=showAllDues).grid(row=rw + 1, column=2)
    brksp4 = Label(window, text="           ").grid(row=rw + 4, column=3)
    brkln1 = Label(window, text="           ").grid(row=rw + 5)
    update = Button(window, text="Update Courses", anchor='center',command=lambda:courseupdate(window)).grid(row=rw + 6, column=2)
    signout = Button(window, text="Sign Out", anchor='center',command=lambda: logout(window)).grid(row=rw+6, column=3)
    window.mainloop()
file8 = open('.config', 'r')
info = file8.readline()
file8.close()
if (info == " " or info==""):
    signin()
else:
    dashboard()
