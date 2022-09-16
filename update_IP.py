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




html = requests.get("https://github.com/mathkiler/robot_change_IP/blob/main/IP.txt")
tex = html.text
print(tex[tex.find('<td id="LC1" class="blob-code blob-code-inner js-file-line">')+60:get_next_line(tex, tex.find('<td id="LC1" class="blob-code blob-code-inner js-file-line">'))-5])

while True :
    pass
