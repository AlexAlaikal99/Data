from PIL import Image
import pyperclip
while True:
    print("*********GAK JELAS APP*********")
    print("login app")
    us = ("admin")
    ps = ("administrator")
    print("-------------------------------")
    username = input("Username : ")
    password = input("Password : ")
    print("************WELCOME************")
    if(username==us and password==ps): 
            print("--- ALL MENU ---")
            print("1. Profile")
            print("2. Images")
            print("3. Pesan")
            menu = int(input("PILIH MENU (1 / 2 /3) : "))
            if(menu==1):
                MOD = 128
                pasw = ps
                print("!!! THE KEY MUST BE TWO NUMBERS ONLY")
                print("          NUM1+SPACE+NUM2           \n")
                key = list(map(int ,input("Key:").rstrip().split()))

                cipher=[]
                for tx in pasw:
                    cipher.append(chr((key[0] * ord(tx) + key[1]) %MOD))
        
                print("\n===================================")
                print("USERNAME = "+us)
                print("PASSWORD = "+ps)
                print("AFFINE PASSWORD = ","".join(cipher))  
                print("===================================\n")
            elif(menu==2):
                MOD = 128
                img = input("gambar:")
                gambar = Image.open(img, 'r')
                gambar.show()
                print("!!! THE KEY MUST BE TWO NUMBERS ONLY")
                print("          NUM1+SPACE+NUM2           \n")
                key = list(map(int ,input("Key:").rstrip().split()))

                cipher=[]
                for foto in img:
                    cipher.append(chr((key[0] * ord(foto) + key[1]) %MOD))
        
                print("\n===================================")
                print("         !!! Encrypted !!!         ")
                print("HASIL ENKRIPSI :","".join(cipher))  
                print("===================================\n")
            elif(menu==3):
                print("-- AFFINE CIPHER --")
                print("-- VIGENERE CIPHER --")
                crip=int(input("Pilih Metode 1 / 2 : "))
                if crip == 1:
                    print("**affine**")
                    MOD = 128
                    pesan = input("ISI PESAN : ")
                    print("!!! THE KEY MUST BE TWO NUMBERS ONLY")
                    print("          NUM1+SPACE+NUM2           \n")
                    key = list(map(int ,input("Key:").rstrip().split()))

                    cipher=[]
                    for sms in pesan:
                        cipher.append(chr((key[0] * ord(sms) + key[1]) %MOD))
        
                    print("\n===================================")
                    print("PESAN : "+pesan)
                    print("AFFINE PESAN = ","".join(cipher))  
                    print("===================================\n")
                else:
                    print("**vigenere**")
                    HURUF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    def main():
                        pesanSaya = input("ISI PESAN: ")
                        kunciSaya = 'ALEX'
                        modeSaya = 'enkripsi'
                        if modeSaya == 'enkripsi':
                            ubah = enkripsiPesan(kunciSaya, pesanSaya)
                        elif modeSaya == 'dekripsi':
                            ubah = dekripsiPesan(kunciSaya, pesanSaya)

                        print('%sed pesan : ' % (modeSaya.title()))
                        print(ubah)
                        pyperclip.copy(ubah)
                        print()
                        print('Pesan akan disalin kedalam papan klip.')
                    def enkripsiPesan(kunci, pesan):
                        return ubahPesan(kunci, pesan, 'enkripsi')
                    def dekripsiPesan(kunci, pesan):
                        return ubahPesan(kunci, pesan, 'dekripsi')
                    def ubahPesan(kunci, pesan, mode):
                        ubah = []
                        kunciIndex = 0
                        kunci = kunci.upper()
                        for symbol in pesan:
                            nomor = HURUF.find(symbol.upper())
                            if nomor != -1: 
                                if mode == 'enkripsi':
                                    nomor += HURUF.find(kunci[kunciIndex]) 
                                elif mode == 'dekripsi':
                                    nomor -= HURUF.find(kunci[kunciIndex]) 
                                nomor %= len(HURUF) 
                                if symbol.isupper():
                                    ubah.append(HURUF[nomor])
                                elif symbol.islower():
                                    ubah.append(HURUF[nomor].lower())
                                kunciIndex += 1 
                                if kunciIndex == len(kunci):
                                    kunciIndex = 0
                                else:
                                    ubah.append(symbol)

                            return ''.join(ubah)
                    if __name__ == '__main__':
                        main()
            else:
                print("no item")
    else:
        print("Alert : username or password incorrect")
