import datetime
import time

end_time = datetime.datetime(2025,12,19) # adjust the time youseslf
site_block = ["www.wscubetech.com", "www.youtube.com"] #list of the website you want to block
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

while True:
    if end_time > datetime.datetime.now():
        print("Website blocking is started.")
        with open(host_path, "r+") as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect + " " + website + "/n")
                else:
                    pass
    else:
        with open(host_path,"r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for line in content:
                if not any(website in  line for website in site_block):
                    host_file.write(line) #clear the line
            host_file.truncate() # help to adjust the file as save as it was before any editing
        time.sleep(5)

#Note: rather than running it in terminator
# Go to command prompt open it as an administrator
# redirect the path to this folder where you have written code and run it
# you you want to check go to windows/system32/drives/etc/hosts you can see the block websites