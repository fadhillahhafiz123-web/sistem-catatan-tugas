# Sistem Catatan Tugas Mahasiswa

tugas = []


def tampilkan_tugas():
    print("\n=== DAFTAR TUGAS ===")

    if len(tugas) == 0:
        print("Belum ada tugas.")
    else:
        for i, item in enumerate(tugas, 1):
            status = "Selesai" if item["selesai"] else "Belum selesai"
            print(f"{i}. {item['nama']} - {status}")


def tambah_tugas():
    nama = input("Masukkan nama tugas: ")
    tugas.append({
        "nama": nama,
        "selesai": False
    })
    print("Tugas berhasil ditambahkan!")


def tandai_selesai():
    tampilkan_tugas()

    if len(tugas) > 0:
        nomor = int(input("Pilih nomor tugas yang selesai: "))

        if 1 <= nomor <= len(tugas):
            tugas[nomor - 1]["selesai"] = True
            print("Tugas berhasil ditandai selesai!")
        else:
            print("Nomor tugas tidak valid.")


def hapus_tugas():
    tampilkan_tugas()

    if len(tugas) > 0:
        nomor = int(input("Pilih nomor tugas yang ingin dihapus: "))

        if 1 <= nomor <= len(tugas):
            tugas.pop(nomor - 1)
            print("Tugas berhasil dihapus!")
        else:
            print("Nomor tugas tidak valid.")


while True:
    print("\n================================")
    print("    SISTEM CATATAN TUGAS")
    print("================================")
    print("1. Lihat Tugas")
    print("2. Tambah Tugas")
    print("3. Tandai Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")
    print("================================")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_tugas()

    elif pilihan == "2":
        tambah_tugas()

    elif pilihan == "3":
        tandai_selesai()

    elif pilihan == "4":
        hapus_tugas()

    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak tersedia.")