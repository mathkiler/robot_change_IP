import requests
import os




html = requests.get("http://monip.org/")
tex = html.text
new_ip_tamp = tex[tex.find('<P ALIGN="center"><FONT size=8><BR>IP : ')+40:tex.find('<P ALIGN="center"><FONT size=8><BR>IP : ')+55]
new_ip = ""
for k in range(len(new_ip_tamp)) :
    if new_ip_tamp[k] in ".0123456789" :
        new_ip+=new_ip_tamp[k]

print(new_ip)
f = open("./IP.txt", "w")
f.write(new_ip)
f.close()



os.system('git add "IP.txt"')
os.system('git commit -m "IP.txt"')
os.system('git push')

