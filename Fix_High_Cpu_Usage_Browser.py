import os,getpass

os.system('cmd /c "pip install psutil"')
def changedir():
   User_Name = GetUser()
   os.chdir('C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'.format(User_Name))
   fh = open('pythonautomation.py','w')
   fh.write('''import os,psutil
while(1):
    for pro in psutil.process_iter():
        if pro.name() == "chrome.exe":
            pid= pro.pid     
            p= pro.cpu_percent()//8
            if(p>50):
                os.system("taskkill /f /im "+str(pid))
                exit()
                
            
                    
''')
   fh.close()
   

   

def GetUser():
      return getpass. getuser()[0:5]
      
changedir()      


    
    
   
