import os,psutil
while(1):
    for pro in psutil.process_iter():
        if pro.name() == "chrome.exe":
            pid= pro.pid     
            p= pro.cpu_percent()//8
            if(p>50):
                os.system("taskkill /f /im "+str(pid))
                exit()
                
            
                    
