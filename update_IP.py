import requests
import os

def get_next_line(text, ind) :
    try :
        while True :
            if text[ind] == "\n" :
                return ind
            ind+=1
    except :
        return 0


html = requests.get("http://monip.org/")
tex = html.text
new_ip = tex[tex.find('<P ALIGN="center"><FONT size=8><BR>IP : ')+40:get_next_line(tex, tex.find('<P ALIGN="center"><FONT size=8><BR>IP : '))-156]
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
