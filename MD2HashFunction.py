#!/usr/bin/env python3


def Best_MD2_Hash_Function_Tools(created_by="Ruben Leonardo Sigalingging."):
	from os import system
	# BERSIHKAN LAYAR DAN INSTAL MODULE PyCryptodome
	system("clear")
	system("pip install pycryptodome")
	system("pip install pyfiglet")
	system("clear")
	from pyfiglet import figlet_format
	from time import sleep
	import Crypto.Hash
	from Crypto.Hash import MD2


	# BUAT TAMPILAN PROGRAM SUPAYA LEBIH MENARIK
	tampilan_program=figlet_format("MD2",font="3-d")
	print(tampilan_program)
	print("[!] Dibuat Oleh: Ruben Leonardo Sigalingging.")
	print("[!] Dibuat Pada: Kamis, 30 Juni, 2022, Pukul 22:56 PM.")
	print("[!] Fungsi: Untuk Mengenkripsi Kata Sandi atau Pesan.")
	print("[!] Menggunakan: Metode Fungsi Hash MD2\n")


	# BUAT VARIABEL UNTUK MENAMPUNG KATA SANDI ATAU PESAN UNTUK USER.
	kata_sandi_atau_pesan=input("[!] Kata Sandi atau Pesan: ")
	fungsi_hash_md2=MD2.new()
	fungsi_hash_md2.update(kata_sandi_atau_pesan.encode("ascii"))
	print("")
	print(f"[!] Kode Hash MD2 Dari {kata_sandi_atau_pesan}: {fungsi_hash_md2.hexdigest()}\n")


# BUAT PROGRAM BARU DI DALAM FUNGSI, UNTUK BRUTE FORCE ATTACK KODE MD2, ATAU ISTILAHNYA MD2 CRACKING.
def memecahkan_kode_hash_md2(created_by="Ruben Leonardo Sigalingging."):
	from os import system
	# BERSIHKAN LAYAR DAN INSTAL MODULE PyCryptodome
	system("clear")
	system("pip install pycryptodome")
	system("pip install pyfiglet")
	system("clear")
	from pyfiglet import figlet_format
	from time import sleep
	import Crypto.Hash
	from Crypto.Hash import MD2
	import os


	# BUAT TAMPILAN PROGRAM SUPAYA LEBIH MENARIK
	tampilan_program=figlet_format("MD2",font="3-d")
	print(tampilan_program)
	print("[!] Dibuat Oleh: Ruben Leonardo Sigalingging.")
	print("[!] Dibuat Pada: Kamis, 30 Juni, 2022, Pukul 22:56 PM.")
	print("[!] Fungsi: Untuk Memecahkan Kode Hash MD2.")
	print("[!] Menggunakan: Metode Dictionary Attack.\n")


	serangan_kode_md2=0
	# BUAT INPUTAN UNTUK USER MENGINPUTKAN KODE MD2 YANG INGIN DIPECAHKAN.
	kode_md2_untuk_dipecahkan=str(input("[!] Kode Hash MD2: "))
	file_kamus=input("[!] File Kamus: ")


	# CEK APAKAH FILE KAMUS ADA DIDALAM FOLDER YANG SAMA DENGAN KODE PROGRAM INI, ATAU FILE KAMUS BERADA DI FOLDER YANG BERBEDA.
	if os.path.isfile(file_kamus)==True:
		try:
			file_kamus=open(file_kamus,"r")
			print("[!] File Kamus Ditemukan!\n")
		except:
			from sys import exit
			print("[!] File Kamus Tidak Ditemukan!\n")
			exit()
	else:
		from sys import exit
		print("[!] File Kamus Tidak Ditemukan!\n")
		exit()

	# BUAT PERULANGAN KE BAWAH, UNTUK MEMECAHKAN KODE MD2 NYA.
	for pecahkan_kode_md2_menggunakan_metode_serangan_kamus in file_kamus:
		kode_hash_md2=MD2.new()
		kode_hash_md2.update(pecahkan_kode_md2_menggunakan_metode_serangan_kamus.strip().encode("ascii"))
		from time import time,sleep
		waktu_memulai_serangan=time()
		print("[!] Coba Kata Sandi%d: %s" % (serangan_kode_md2,pecahkan_kode_md2_menggunakan_metode_serangan_kamus.strip()))


		serangan_kode_md2+=1
		waktu_mengakhiri_serangan=time()
		waktu_mengakhiri_serangan_dikurang_waktu_memulai_serangan=waktu_mengakhiri_serangan-waktu_memulai_serangan


		# CEK APAKAH KODE MD2 YANG DI INPUTKAN USER SAMA DENGAN KODE MD2 ASLI
		if kode_md2_untuk_dipecahkan.strip()==kode_hash_md2.hexdigest():
			print("[!] Kode MD2 Valid!")
			print("")
			print("[!] Kecocokan Kata Sandi Ditemukan!\n[!] Kata Sandinya Adalah: %s" % pecahkan_kode_md2_menggunakan_metode_serangan_kamus.strip())
			print("")
			print(f"[!] Total Waktu Serangan: {waktu_mengakhiri_serangan_dikurang_waktu_memulai_serangan}")
			sleep(12)
			break
		else:
			print("\n")
			print("[!] Mohon Maaf, Kecocokan Kata Sandi Tidak Ditemukan!")
			print("")


# PILIH MENU UNTUK USER
from os import system
# BERSIHKAN LAYAR DAN INSTAL MODULE PyCryptodome
system("clear")
system("pip install pycryptodome")
system("pip install pyfiglet")
system("clear")
from pyfiglet import figlet_format
from time import sleep
import Crypto.Hash
from Crypto.Hash import MD2
tampilan_program=figlet_format("MD2",font="3-d")
print(tampilan_program)
print("[1] Hashing MD2")
print("[2] MD2 Cracking Tool")
print("[3] Exit\n")
pertanyaan_untuk_user=int(input("[!] Pilih: "))
print("")
if pertanyaan_untuk_user==1:
	Best_MD2_Hash_Function_Tools()
elif pertanyaan_untuk_user==2:
	memecahkan_kode_hash_md2()
elif pertanyaan_untuk_user==3:
	from os import system
	system("clear")
	system("exit")
else:
	print("[!] Pilih Dengan Benar!")