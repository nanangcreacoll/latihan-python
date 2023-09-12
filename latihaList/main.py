# program list buku

list_buku = []
while True:
    print("\nmasukkan data buku")
    judul = input("judul buku\t: ")
    penulis = input("penulis buku\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print("\n","="*10,"data buku")
    for index, buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n","="*20)
    isContinue = input("apakah lanjut? (y/n)\t")

    if isContinue == "n":
        break

print ("\nprogram selesai\n")

