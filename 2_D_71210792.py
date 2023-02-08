K = input("Kalimat yang ingin diteliti : ")
K1 = input("Kata yang dicari : ")


for i in K:
    jumlah_kata = K.count(K1)
    print("Jumlah kata yang dicari : ", jumlah_kata)
    break