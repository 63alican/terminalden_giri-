#author Emyounoone
import os
import time
import sys


def banner():
        print("Alican Karakuş :)")
while True :
    secenek=int(input("işlem için 1 çıkmak için ise 2 tuşlaynız :"))
    if secenek==1 :
            
            kullanici=input("lütfen kullanıcı adı giriniz :")
            parola=input("lütfen şifre belirleyiniz :")
        
            def sifre_data():
                print("""
                    Şifreleriniz:
                İnstagram:...
                Facebook:...                        
                Gmail:...
                """)


            def giris():
                user = input("Kullanıcı adınız: ")
                sifre = input("Şifreniz:")
                if user == kullanici:
                    print("Kullanıcı Adı Doğru")
                else:
                    print("Hatalı Giriş!")
                    quit()
                if sifre == parola :
                    print("Şifre Doğru")
                else:
                    print("Hatalı Giriş")
                    quit()


            def giris_basarili():
                print("---Giriş Başarılı Sisteme Yönlendiriliyorsunuz---")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                sifre_data()


            banner()
            giris()
            giris_basarili()
    else :
            secenek==2 
            break         
            