
import hashlib
hashOrChipher=raw_input("Hash veya Sifrelenmis metni giriniz: ")
def hashDegil():
    print "[-] Hash algoritması MD4 olmayabilir"
    print "[-] Hash algoritması MD5 olmayabilir"
    print "[-] Hash algoritması NTLM olmayabilir"
    print "[-] Hash algoritması LM olmayabilir"
    print "[-] Hash algoritması SHA1 olmayabilir"
    print "[-] Hash algoritması SHA224 olmayabilir"
    print "[-] Hash algoritması SHA256 olmayabilir"
    print "[-] Hash algoritması SHA384 olmayabilir"
    print "[-] Hash algoritması SHA512 olmayabilir"


if len(hashOrChipher) == 4:
    print "[+] Hash algoritması CRC-16 olabilir"
    print "[+] Hash algoritması CRC-16-CCITT olabilir"
    print "[+] Hash algoritması FCS-16 olabilir"
elif len(hashOrChipher) == 6:
    print "[+] Hash algoritması CRC-24 olabilir"
elif len(hashOrChipher) == 8:
    print "[+] Hash algoritması Adler-32 olabilir"
    print "[+] Hash algoritması CRC-32B olabilir"
    print "[+] Hash algoritması FCS-32 olabilir"
    print "[+] Hash algoritması GHash-32-3 olabilir"
    print "[+] Hash algoritması GHash-32-5 olabilir"
    print "[+] Hash algoritması FNV-132 olabilir"
    print "[+] Hash algoritması Fletcher-32 olabilir"
    print "[+] Hash algoritması Joaat olabilir"
    print "[+] Hash algoritması ELF-32 olabilir"
    print "[+] Hash algoritması XOR-32 olabilir"
elif len(hashOrChipher) == 16:
    print "[+] Hash algoritması MySQL323 olabilir"
    print "[+] Hash algoritması DES(Oracle) olabilir"
    print "[+] Hash algoritması Half MD5 olabilir"
    print "[+] Hash algoritması Oracle 7-10g olabilir"
    print "[+] Hash algoritması FNV-164 olabilir"
    print "[+] Hash algoritması CRC64 olabilir"
elif len(hashOrChipher) == 24:
    print "[+] Hash algoritması CRC-96(ZIP) olabilir"
elif len(hashOrChipher) == 32:
    print "[+] Hash algoritması MD4 olabilir"
    print "[+] Hash algoritması MD5 olabilir"
    print "[+] Hash algoritması NTLM olabilir"
    print "[+] Hash algoritması LM olabilir"
elif len(hashOrChipher) == 40:
    print "[+] Hash algoritması SHA-1 olabilir"
    print "[+] Hash algoritması Double SHA-1 olabilir"
    print "[+] Hash algoritması RIPEMD-160 olabilir"
    print "[+] Hash algoritması Haval-160 olabilir"
    print "[+] Hash algoritması Tiger-160 olabilir"
    print "[+] Hash algoritması HAS-160 olabilir"
elif len(hashOrChipher) == 48:
    print "[+] Hash algoritması Haval-192 olabilir"
    print "[+] Hash algoritması Tiger-192 olabilir"
    print "[+] Hash algoritması SHA-1(Oracle) olabilir"
    print "[+] Hash algoritması OSX v10.4 olabilir"
    print "[+] Hash algoritması OSX v10.5 olabilir"
    print "[+] Hash algoritması OSX v10.6 olabilir"
elif len(hashOrChipher) == 51:
    print "[+] Hash algoritması Cryptocurrency-PrivateKey olabilir"
elif len(hashOrChipher) == 56:
    print "[+] Hash algoritması SHA-224 olabilir"
    print "[+] Hash algoritması SHA3-224 olabilir"
    print "[+] Hash algoritması Haval-224 olabilir"
elif len(hashOrChipher) == 64:
    print "[+] Hash algoritması SHA-256 olabilir"
elif len(hashOrChipher) == 96:
    print "[+] Hash algoritması SHA-384 olabilir"
elif len(hashOrChipher) == 128:
    print "[+] Hash algoritması SHA-512 olabilir"
    print "[+] Hash algoritması Whirlpool olabilir"
    print "[+] Hash algoritması SHA3-512 olabilir"
else:
    hashDegil()
    print "[-]Herhangi bir hash algrotiması ile eşleşmedi"
    print "[+]Ceaser kontrolü başladı"
    duzyazi = ""
    yaziListe = []
    yaziSayi = []
    yaziListe = list(hashOrChipher)
    for otelemeMiktari in range(1,29):
        for i in yaziListe:
            yaziSayi = ord(i) - otelemeMiktari
            duzyazi = duzyazi + chr(yaziSayi)
        print "[+]",str(otelemeMiktari)+" harf kadar ötelenmiş düz metin : "+ duzyazi
        duzyazi=""
    print "[+]Ceaser kontrolü tamamlandı"
