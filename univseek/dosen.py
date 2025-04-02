import requests
import json


class Dosen:
    def __init__(self, nama=None, nidn=None, univ=None):
        self.nama = nama
        self.nidn = nidn
        self.univ = univ

    def cari_dosen(self):
        if self.nama and self.nidn and self.univ:
            print(
                f"Mencari dosen dengan Nama: {self.nama}, NIDN: {self.nidn}, Universitas: {self.univ}"
            )
            query = f"{self.nama} {self.nidn} {self.univ}"
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/dosen/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [dosen["id"] for dosen in data]
                print(f"[+] {len(jmlh_data)} Data Dosen Ditemukan")
                if len(jmlh_data) <= 5:
                    for item in data:
                        nama = item.get("nama")
                        nidn = item.get("nidn")
                        univ = item.get("nama_pt")
                        print(f"Nama: {nama}")
                        print(f"NIDN: {nidn}")
                        print(f"Universitas: {univ}")
                else:
                    pilihan = input(
                        "[?] Apakah Anda ingin menyimpan data ke file? (y/n): "
                    )
                    if pilihan.lower() == "y":
                        with open("data_dosen.json", "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False)
                        print("Data berhasil disimpan ke file 'data_dosen.json'.")
        elif self.nama and self.nidn:
            print(f"Mencari dosen dengan Nama: {self.nama}, NIDN: {self.nidn}")
            query = f"{self.nama} {self.nidn}"
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/dosen/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [dosen["id"] for dosen in data]
                print(f"[+] {len(jmlh_data)} Data Dosen Ditemukan")
                if len(jmlh_data) <= 5:
                    for item in data:
                        nama = item.get("nama")
                        nidn = item.get("nidn")
                        univ = item.get("nama_pt")
                        print(f"Nama: {nama}")
                        print(f"NIDN: {nidn}")
                        print(f"Universitas: {univ}")
                else:
                    pilihan = input(
                        "[?] Apakah Anda ingin menyimpan data ke file? (y/n): "
                    )
                    if pilihan.lower() == "y":
                        with open("data_dosen.json", "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False)
                        print("Data berhasil disimpan ke file 'data_dosen.json'.")
        elif self.nama and self.univ:
            print(f"Mencari dosen dengan Nama: {self.nama}, Universitas: {self.univ}")
            query = f"{self.nama} {self.univ}"
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/dosen/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [dosen["id"] for dosen in data]
                print(f"[+] {len(jmlh_data)} Data Dosen Ditemukan")
                if len(jmlh_data) <= 5:
                    for item in data:
                        nama = item.get("nama")
                        nidn = item.get("nidn")
                        univ = item.get("nama_pt")
                        print(f"Nama: {nama}")
                        print(f"NIDN: {nidn}")
                        print(f"Universitas: {univ}")
                else:
                    pilihan = input(
                        "[?] Apakah Anda ingin menyimpan data ke file? (y/n): "
                    )
                    if pilihan.lower() == "y":
                        with open("data_dosen.json", "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False)
                        print("Data berhasil disimpan ke file 'data_dosen.json'.")
        elif self.nidn and self.univ:
            print(f"Mencari dosen dengan NIDN: {self.nidn}, Universitas: {self.univ}")
            query = f"{self.nidn} {self.univ}"
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/dosen/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [dosen["id"] for dosen in data]
                print(f"[+] {len(jmlh_data)} Data Dosen Ditemukan")
                if len(jmlh_data) <= 5:
                    for item in data:
                        nama = item.get("nama")
                        nidn = item.get("nidn")
                        univ = item.get("nama_pt")
                        print(f"Nama: {nama}")
                        print(f"NIDN: {nidn}")
                        print(f"Universitas: {univ}")
                else:
                    pilihan = input(
                        "[?] Apakah Anda ingin menyimpan data ke file? (y/n): "
                    )
                    if pilihan.lower() == "y":
                        with open("data_dosen.json", "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False)
                        print("Data berhasil disimpan ke file 'data_dosen.json'.")
        elif self.nama:
            print(f"Mencari dosen dengan Nama: {self.nama}")
            query = self.nama
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/dosen/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [dosen["id"] for dosen in data]
                print(f"[+] {len(jmlh_data)} Data Dosen Ditemukan")
                if len(jmlh_data) <= 5:
                    for item in data:
                        nama = item.get("nama")
                        nidn = item.get("nidn")
                        univ = item.get("nama_pt")
                        print(f"Nama: {nama}")
                        print(f"NIDN: {nidn}")
                        print(f"Universitas: {univ}")
                else:
                    pilihan = input(
                        "[?] Apakah Anda ingin menyimpan data ke file? (y/n): "
                    )
                    if pilihan.lower() == "y":
                        with open("data_dosen.json", "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False)
                        print("Data berhasil disimpan ke file 'data_dosen.json'.")
        elif self.nidn:
            print(f"Mencari dosen dengan NIDN: {self.nidn}")
            query = self.nidn
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/dosen/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [dosen["id"] for dosen in data]
                print(f"[+] {len(jmlh_data)} Data Dosen Ditemukan")
                if len(jmlh_data) <= 5:
                    for item in data:
                        nama = item.get("nama")
                        nidn = item.get("nidn")
                        univ = item.get("nama_pt")
                        print(f"Nama: {nama}")
                        print(f"NIDN: {nidn}")
                        print(f"Universitas: {univ}")
                else:
                    pilihan = input(
                        "[?] Apakah Anda ingin menyimpan data ke file? (y/n): "
                    )
                    if pilihan.lower() == "y":
                        with open("data_dosen.json", "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False)
                        print("Data berhasil disimpan ke file 'data_dosen.json'.")

        elif self.univ:
            print(f"Mencari dosen dari Universitas: {self.univ}")
            query = self.univ
            url = f"https://api-pddikti.kemdiktisaintek.go.id/pencarian/dosen/{query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                jmlh_data = [dosen["id"] for dosen in data]
                print(f"[+] {len(jmlh_data)} Data Dosen Ditemukan")
                if len(jmlh_data) <= 5:
                    for item in data:
                        nama = item.get("nama")
                        nidn = item.get("nidn")
                        univ = item.get("nama_pt")
                        print(f"Nama: {nama}")
                        print(f"NIDN: {nidn}")
                        print(f"Universitas: {univ}")
                else:
                    pilihan = input(
                        "[?] Apakah Anda ingin menyimpan data ke file? (y/n): "
                    )
                    if pilihan.lower() == "y":
                        with open("data_dosen.json", "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False)
                        print("Data berhasil disimpan ke file 'data_dosen.json'.")
        else:
            print("Data dosen tidak lengkap.")
