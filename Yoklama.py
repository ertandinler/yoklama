#! python
# -*- coding: utf-8 -*-
#
#
#
#
####################	İmports Part 	################################

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_yoklama import Ui_MainWindow
from Yoklama_kisiEkle.ui_kisi_ekle import Ui_Form
from Yoklama_kisiAraSil.Ui_kisi_araSil import Ui_Form1
from Cihaz_test.Ui_cihaz_test import Ui_CihazTest
from Kart_tanimla.Ui_kartTanimla import Ui_Dialog

from seri_port import PortDinle, portSec
import sys
import sqlite3
import serial
import serial.tools.list_ports


PORT = ''
####################	Set Serial Part	 ###############################



class PortSecTest(QDialog, Ui_CihazTest):
	def __init__(self):
		super(PortSecTest, self).__init__()
		self.setupUi(self)
		ports = list(serial.tools.list_ports.comports())
		for port in ports:
			p = port[0]
			self.comboBox_cihaz.addItem("{}".format(p))

	@pyqtSignature("bool")
	def cihaz_test(self):
		prt = str(self.comboBox_cihaz.currentText())
		global PORT
		
		#burası sei_port.py ile yeniden düzenlenecek
		#
		if len(prt) == 0:
			self.label_cihaz.setText("Cihaz bağlı değil\nBağlayıp tekrar deneyin")
		if len(prt) == 4:
			ser = serial.Serial()
			ser.port = prt
			#ser.timeout = 1
			ser.open()
			al = ser.read(12)
			veri = int(al[1:9].decode('utf-8'), 16)
			
			if ser.isOpen() and len(al)==12:
				self.label_cihaz.setStyleSheet("background: #9fc;\n"			#buradaki styleSheet önemli
										"color : #090;\n"
										"border-radius : 10px;")
				self.label_cihaz.setText("Bağlantı başarılı : {}\n{} portuna bağlandınız".format(veri, prt))
				PORT = prt
				ser.close()


####################	Kişi işlemleri		############################
#
####################	kişi ekleme			############################

class KisiEkle(QWidget, Ui_Form):
	def __init__(self):
		super(KisiEkle, self).__init__()
		self.setupUi(self)

	@pyqtSignature("bool")
	def Kaydet(self):
		ad = str(self.lineEdit_ad.text())
		soyad = str(self.lineEdit_soyad.text())
		tc = str(self.lineEdit_tc.text())



		if ad.startswith("i"):				# alınan bilgiler baş harfleri büyütülerek veritabanına eklenir.
			ad = "İ" + ad[1:]
			ad = ad.title()
		else:
			ad = ad.title()

		if soyad.startswith("i"):
			soyad = "İ" + soyad[1:]
			soyad = soyad.title()
		else:
			soyad = soyad.title()

		if len(ad)==0 or len(soyad)==0 or len(tc)==0:
			QMessageBox.warning(self, "Hata", u"Lütfen Tüm Alanları Doldurunuz...", "Kapat")
		elif len(tc) !=11:
			QMessageBox.warning(self, "Hata", u"Lütfen TC no kısmına 11 haneli rakam girin", "Kapat")
		else:
			db = sqlite3.connect("database\\yoklama.db")
			imlec = db.cursor()

			imlec.execute("""SELECT k.tc FROM kisiler AS k WHERE tc='{}'""".format(tc))
			t = imlec.fetchall()
			self.m = ""
			for a in t:
				self.m = a[0]
			if self.m == tc:
				QMessageBox.warning(self, "Hata", u"{} TC nolu kişi sistemde kayıtlıdır".format(tc), "Kapat")
			else:
				imlec.execute("""INSERT INTO kisiler(tc, ad, soyad)
						VALUES('{}', '{}', '{}')""".format(tc, ad, soyad))
				db.commit()
				db.close()
				QMessageBox.warning(self, "İşlem Tamam", u"Kişi kaydı yapılmıştır", "Kapat")
				#self.mesaj()
				self.lineEdit_ad.setText("")
				self.lineEdit_soyad.setText("")
				self.lineEdit_tc.setText("")

#		self.close()		# bu satır kişi ekleme ekranını kapatır.

####################	Kişi Arama Silme			############################

class KisiAraSil(QWidget, Ui_Form1):
	def __init__(self):
		super(KisiAraSil, self).__init__()
		self.setupUi(self)

	@pyqtSignature("bool")
	def kisi_ara(self):
		ad = str(self.lineEdit_ad.text())
		soyad = str(self.lineEdit_soyad.text())
		tc = str(self.lineEdit_tc.text())

		if ad.startswith("i"):
			ad = "İ" + ad[1:]
			ad = ad.title()
		else:
			ad = ad.title()

		if soyad.startswith("i"):
			soyad = "İ" + soyad[1:]
			soyad = soyad.title()
		else:
			soyad = soyad.title()

		db = sqlite3.connect("database\\yoklama.db")
		imlec = db.cursor()
		imlec.execute("""SELECT k.ad, k.soyad, k.tc FROM kisiler AS k
					WHERE ad LIKE '%{}%' AND soyad LIKE '%{}%' AND tc LIKE '%{}%'""".format(ad, soyad, tc))
		self.veriler = imlec.fetchall()
		db.close()

		if len(self.veriler) > 1:
			self.label_Ssoyad.setText("Birden fazla sonuç bulundu.\nLütfen arama kriterlerinizi daraltın.")
		if len(self.veriler) == 0:
			self.label_Ssoyad.setText("Aradığınız kriterde kayıtlı\nkullanıcı bulunamadı")
		for m in self.veriler:
			self.ad_ = m[0]
			self.soyad_ = m[1]
			self.tc_ = m[2]
		if len(self.veriler) == 1:
			self.label_Sad.setText("<b>İsim:</b>\t\t{}".format(self.ad_))
			self.label_Sad.setStyleSheet("""background : red; color : blue; text-indent: 50px;
						border-radius: 8px;
                        border-width: 2px;
                        border-style: solid;
                        border-color: rgb(0, 0, 255);
                """)	#css ile şekillenebilir
			self.label_Ssoyad.setText("<b>Soyisim: </b>\t{}".format(self.soyad_))
			self.label_Stc.setText("<b>T.C. No : </b>\t{}".format(self.tc_))

	@pyqtSignature("bool")
	def kisi_sil(self):
		if len(self.veriler) == 1:
			#####	 önemli ==> bu question mesaj kutusu seçenekli kullanım örneği
			uyari = QMessageBox.question(self, "Uyarı", "silme işi eminmisin", QMessageBox.Yes | QMessageBox.No)
			if uyari == QMessageBox.Yes:
				db = sqlite3.connect("database\\yoklama.db")
				imlec = db.cursor()
				imlec.execute("""DELETE FROM kisiler
							WHERE ad='{}' AND soyad='{}' AND tc='{}'""".format(self.ad_, self.soyad_, self.tc_))
				db.commit()
				db.close()

				self.label_Ssoyad.setText("silme işi tamam")	#Buraya database silme kodları yaz
			else :
				self.label_Ssoyad.setText("silme olmadı")

########################################################################
#																	   #
####						Kart Tanımlama 				################

class KartTanimla(QDialog, Ui_Dialog):
	def __init__(self):
		super(KartTanimla, self).__init__()
		self.setupUi(self)
		self.pd = PortDinle(PORT)
		self.pd.calistir = True
		self.pd.start()
	
			
	@pyqtSignature("bool")
	def kisi_bul(self):
		tc = str(self.lineEdit_tcBul.text())
		self.kid_ = ''
		self.tc_ = ''
		self.ad_ = ''
		self.soyad_ = ''
		db = sqlite3.connect("database\\yoklama.db")
		imlec = db.cursor()
		imlec.execute(""" SELECT * FROM kisiler 
					WHERE tc = '{}'""".format(tc))
		self.veriler = imlec.fetchall()
	
		if len(self.veriler) == 0:
			self.label_kisi.setText("Kişi bulunamadı")
		for m in self.veriler:
			self.kid_ = m[0]
			self.tc_ = m[1]
			self.ad_ = m[2]
			self.soyad_ = m[3]
			self.label_kisi.setText("Ad\t:{}\nSoyad\t:{}\nTc\t:{}".format(self.ad_, self.soyad_, self.tc_ ))
		db.close()
		
	@pyqtSignature("bool")
	def kart_format(self):
		global PORT
		if PORT == '':
			QMessageBox.warning(self, "Uyarı", u"Lütfen önce cihazı Test edin", "Kapat")
			self.pd.calistir = False
			self.close()
		else:
			QMessageBox.warning(self, "Uyarı", u"Lütfen okuyucuya kart okutun", "Kapat")
			self.label_uyari.setText("{}"format(self.pd.text_veri))
			
			#burası veritabanında sorgulancak..
				
				
			#uyari = QMessageBox.question(self, "Uyarı", "silme işi eminmisin", QMessageBox.Yes | QMessageBox.No)
			#if uyari == QMessageBox.Yes:
			#	pass
			#else :
			#	pass
			
			self.okunan_veri = self.pd.veri				# buraya seri porttan gelen veri eklenir
			self.text_veri = self.str(okunan_veri)
			db = sqlite3.connect("database\\yoklama.db")
			imlec = db.cursor()
			imlec.execute("""INSERT INTO kartlar(kart_no, kid)
							VALUES('{}', '{}')""".format(self.okunan_veri, self.kid_))
			db.commit()
			db.close()
			self.pd.calistir = False


####################	Main Window Part	 ###########################

class AnaProgram(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(AnaProgram, self).__init__()
		self.setupUi(self)
		self.statusBar().showMessage("Program Hazır\n") 	# Status Bar kısmına mesaj yazılır
		self.port_SecTest = PortSecTest()
		
	@pyqtSignature("bool")
	def baglan(self):
		pass

	@pyqtSignature("bool")
	def iptal(self):
		pass

	@pyqtSignature("bool")
	def on_action_cikis_triggered(self):		# Dosya Menüsündeki çıkış sinyalini yakalar
		exit()

	@pyqtSignature("bool")
	def on_actionYeni_Kisi_Ekle_triggered(self):			# Kişi ekleme sinyalini yakalar
		self.kisi_ekle = KisiEkle()
		self.kisi_ekle.show()

	@pyqtSignature("bool")
	def on_actionKisi_Ara_triggered(self):
		self.kisi_AraSil = KisiAraSil()
		self.kisi_AraSil.show()

	@pyqtSignature("bool")
	def on_actionKisi_Sil_triggered(self):
		self.kisi_AraSil = KisiAraSil()
		self.kisi_AraSil.show()

	@pyqtSignature("bool")
	def on_actionCihaz_Test_triggered(self):
		#self.port_SecTest.comboBox_cihaz.clear()
		self.port_SecTest.show()

	@pyqtSignature("bool")
	def on_actionCihaz_Test_2_triggered(self):
		self.on_actionCihaz_Test_triggered()

	@pyqtSignature("bool")
	def on_actionKart_Tan_mla_2_triggered(self):
		self.kart_tanimla = KartTanimla()
		self.kart_tanimla.show()


####################	Application Exec Part	########################

def main():
	app = QApplication(sys.argv)
	win = AnaProgram()
	win.show()
	return app.exec_()

if __name__ == '__main__':
	main()

