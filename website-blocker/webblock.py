import time
from datetime import datetime as dat

hosts_temp = "hosts"
hosts_name = "/private/etc/hosts"               #always make sure to use the absolute path as the crontab will execute the reboot from a different directory so relative path to the file will not work
redirect_to = "127.0.0.1"
site_blocklist = ["www.facebook.com","facebook.com","www.linkedin.com","linkedin.com"]

while True:
    if dat(dat.now().year, dat.now().month, dat.now().day,2) < dat.now() < dat(dat.now().year, dat.now().month, dat.now().day,2):
        print("Working hours")
        with open(hosts_name, 'r+') as file:
            data = file.read()
            for site in site_blocklist:
                if site in data:
                    pass
                else:
                    file.write(redirect_to + " " + site + '\n')
    else:
        print("Leisure Hours")
        with open(hosts_name, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                flag = 1                    #flag denotes whether that line should be added to the hosts file or not
                for site in site_blocklist:
                    if site in line:
                        flag = 0
                if flag == 1:
                    file.write(line)
            file.truncate()

    time.sleep(2)
