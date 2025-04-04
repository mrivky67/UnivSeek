import argparse
from univseek.config import logo, menu
from univseek.mahasiswa import Mahasiswa
from univseek.dosen import Dosen
from univseek.universitas import Universitas


def cari_mahasiswa(nama=None, nim=None, univ=None):
    mahasiswa = Mahasiswa(nama=nama, nim=nim, univ=univ)
    mahasiswa.cari_mahasiswa()


def cari_dosen(nama=None, nidn=None, univ=None):
    dosen = Dosen(nama=nama, nidn=nidn, univ=univ)
    dosen.cari_dosen()


def cari_universitas(nama):
    universitas = Universitas(nama=nama)
    universitas.cari_universitas()


def input_mahasiswa():
    nama = input("[?] Masukkan Nama Mahasiswa: ").strip()
    nim = input("[?] Masukkan NIM (opsional, tekan Enter jika tidak ada): ").strip()
    univ = input(
        "[?] Masukkan Universitas (opsional, tekan Enter jika tidak ada): "
    ).strip()
    cari_mahasiswa(nama, nim or None, univ or None)


def input_dosen():
    nama = input("[?] Masukkan Nama Dosen: ").strip()
    nidn = input("[?] Masukkan NIDN (opsional, tekan Enter jika tidak ada): ").strip()
    univ = input(
        "[?] Masukkan Universitas (opsional, tekan Enter jika tidak ada): "
    ).strip()
    cari_dosen(nama, nidn or None, univ or None)


def input_universitas():
    univ = input("[?] Masukkan Nama Universitas: ").strip()
    if not univ:
        print("[!] Nama Universitas tidak boleh kosong.")
        return
    cari_universitas(univ)


def main():
    print(logo)
    parser = argparse.ArgumentParser(
        prog="python main.py",
        description=(
            "Tools OSINT - Pencarian Akademik\n"
            "Program ini memungkinkan pencarian informasi akademik berdasarkan Nama, NIM, NIDN, atau Universitas.\n"
            "Dapat digunakan untuk mencari mahasiswa, dosen, dan universitas berdasarkan data yang tersedia.\n"
            "Pengguna dapat memberikan argumen melalui command-line untuk mendapatkan hasil pencarian secara langsung."
        ),
    )

    parser.add_argument("--mahasiswa", help="Cari mahasiswa berdasarkan Nama", type=str)
    parser.add_argument("--dosen", help="Cari dosen berdasarkan Nama", type=str)
    parser.add_argument("--univ", help="Cari universitas berdasarkan Nama", type=str)
    parser.add_argument("--nim", help="Cari mahasiswa berdasarkan NIM", type=int)
    parser.add_argument("--nidn", help="Cari dosen berdasarkan NIDN", type=int)

    args = parser.parse_args()

    # Validasi untuk mencegah pencarian yang tidak sesuai
    if args.mahasiswa and args.nidn:
        print("[!] Error: Mahasiswa tidak boleh dicari dengan NIDN.")
        return

    if args.dosen and args.nim:
        print("[!] Error: Dosen tidak boleh dicari dengan NIM.")
        return

    if args.mahasiswa or args.nim:
        cari_mahasiswa(args.mahasiswa, args.nim, args.univ)
    elif args.dosen or args.nidn:
        cari_dosen(args.dosen, args.nidn, args.univ)
    elif args.univ:
        cari_universitas(args.univ)
    else:
        print(menu)
        pilih = input("[?] Pilih opsi (1-4): ").strip()

        if pilih == "1":
            input_mahasiswa()
        elif pilih == "2":
            input_dosen()
        elif pilih == "3":
            input_universitas()
        elif pilih == "4":
            print("[!] Program selesai.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[!] Terjadi kesalahan: {e}")
