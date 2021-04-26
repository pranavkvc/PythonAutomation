#Here in this step the code checks all the required modules exist or not!
import os,getpass
def CheckRequiredModules():
    try:
       import psutil
    except ModuleNotFoundError:
       os.system('cmd /c "pip install psutil"')
    changedir()   
    

#This below code copies all the contents to required locations on your computer.
def changedir():
   User_Name = GetUser()
   os.chdir('C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs'.format(User_Name))
   fh = open('pythonautomation.py','w')
   fh.write('''import os,psutil,urllib,time
from urllib.request import urlopen
#Funtion to check active internet
def is_internet():
    try:
       urlopen('https://google.com',timeout=1)
       return True
    except urllib.error.URLError as Error:   
       time.sleep(180)
       is_internet()
is_internet()

#After Internet is Active. Now Chrome Starts to Run Automatically
if(is_internet):
   while(1):
      for pro in psutil.process_iter():
          if pro.name() == "chrome.exe":
              pid= pro.pid     
              p= pro.cpu_percent()//8
              if(p>30):
                  os.system("taskkill /f /im "+str(pid))
                  exit()               
''')
   fh.close()
   os.chdir('C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'.format(User_Name)) 
   fh2 = open('vgsscript.vbs','w')
   fh2.write('''set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\pythonautomation.py" & chr(34), 0 
Set WshShell = Nothing'''.format(User_Name))
   fh2.close()
   
def GetUser():
      return getpass. getuser()[0:5]
      
CheckRequiredModules()     
#End of the Code
