# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yoklama_main.ui'
#
# Created: Sun Sep 21 01:22:41 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(776, 607)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("simgeler/ana_pencere.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableView_yoklama = QtGui.QTableView(self.centralwidget)
        self.tableView_yoklama.setGeometry(QtCore.QRect(310, 0, 461, 511))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_yoklama.sizePolicy().hasHeightForWidth())
        self.tableView_yoklama.setSizePolicy(sizePolicy)
        self.tableView_yoklama.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableView_yoklama.setFrameShape(QtGui.QFrame.Panel)
        self.tableView_yoklama.setLineWidth(2)
        self.tableView_yoklama.setMidLineWidth(1)
        self.tableView_yoklama.setAlternatingRowColors(True)
        self.tableView_yoklama.setObjectName(_fromUtf8("tableView_yoklama"))
        self.tableView_yoklama.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView_yoklama.verticalHeader().setCascadingSectionResizes(True)
        self.label_cihazDurum = QtGui.QLabel(self.centralwidget)
        self.label_cihazDurum.setGeometry(QtCore.QRect(5, 12, 301, 41))
        self.label_cihazDurum.setObjectName(_fromUtf8("label_cihazDurum"))
        self.pushButton_baglan = QtGui.QPushButton(self.centralwidget)
        self.pushButton_baglan.setGeometry(QtCore.QRect(10, 110, 161, 31))
        self.pushButton_baglan.setObjectName(_fromUtf8("pushButton_baglan"))
        self.pushButton_iptal = QtGui.QPushButton(self.centralwidget)
        self.pushButton_iptal.setGeometry(QtCore.QRect(210, 110, 75, 31))
        self.pushButton_iptal.setObjectName(_fromUtf8("pushButton_iptal"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuDosya = QtGui.QMenu(self.menubar)
        self.menuDosya.setObjectName(_fromUtf8("menuDosya"))
        self.menuKi_i_i_lemleri = QtGui.QMenu(self.menubar)
        self.menuKi_i_i_lemleri.setObjectName(_fromUtf8("menuKi_i_i_lemleri"))
        self.menuRaporlar = QtGui.QMenu(self.menubar)
        self.menuRaporlar.setObjectName(_fromUtf8("menuRaporlar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar_2.sizePolicy().hasHeightForWidth())
        self.toolBar_2.setSizePolicy(sizePolicy)
        self.toolBar_2.setAcceptDrops(True)
        self.toolBar_2.setMovable(True)
        self.toolBar_2.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar_2.setIconSize(QtCore.QSize(40, 24))
        self.toolBar_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar_2.setFloatable(True)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionYeni_Kisi_Ekle = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("simgeler/kisi_ekle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionYeni_Kisi_Ekle.setIcon(icon1)
        self.actionYeni_Kisi_Ekle.setObjectName(_fromUtf8("actionYeni_Kisi_Ekle"))
        self.actionKisi_Ara = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("simgeler/kisi_ara.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionKisi_Ara.setIcon(icon2)
        self.actionKisi_Ara.setObjectName(_fromUtf8("actionKisi_Ara"))
        self.actionKisi_Sil = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("simgeler/kisi_sil.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionKisi_Sil.setIcon(icon3)
        self.actionKisi_Sil.setObjectName(_fromUtf8("actionKisi_Sil"))
        self.actionKisi_Raporu = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("simgeler/kisisel_rapor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionKisi_Raporu.setIcon(icon4)
        self.actionKisi_Raporu.setObjectName(_fromUtf8("actionKisi_Raporu"))
        self.actionGenel_Rapor = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("simgeler/genel_rapor.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGenel_Rapor.setIcon(icon5)
        self.actionGenel_Rapor.setObjectName(_fromUtf8("actionGenel_Rapor"))
        self.action_cikis = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("simgeler/kapat.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_cikis.setIcon(icon6)
        self.action_cikis.setObjectName(_fromUtf8("action_cikis"))
        self.actionCihaz_Test = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("simgeler/cihaz_test.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCihaz_Test.setIcon(icon7)
        self.actionCihaz_Test.setObjectName(_fromUtf8("actionCihaz_Test"))
        self.actionKart_Tan_mla = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("simgeler/kart_tanimla.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionKart_Tan_mla.setIcon(icon8)
        self.actionKart_Tan_mla.setObjectName(_fromUtf8("actionKart_Tan_mla"))
        self.actionCihaz_Test_2 = QtGui.QAction(MainWindow)
        self.actionCihaz_Test_2.setIcon(icon7)
        self.actionCihaz_Test_2.setObjectName(_fromUtf8("actionCihaz_Test_2"))
        self.actionKart_Tan_mla_2 = QtGui.QAction(MainWindow)
        self.actionKart_Tan_mla_2.setIcon(icon8)
        self.actionKart_Tan_mla_2.setObjectName(_fromUtf8("actionKart_Tan_mla_2"))
        self.menuDosya.addAction(self.action_cikis)
        self.menuDosya.addAction(self.actionCihaz_Test_2)
        self.menuDosya.addAction(self.actionKart_Tan_mla_2)
        self.menuKi_i_i_lemleri.addAction(self.actionYeni_Kisi_Ekle)
        self.menuKi_i_i_lemleri.addSeparator()
        self.menuKi_i_i_lemleri.addAction(self.actionKisi_Ara)
        self.menuKi_i_i_lemleri.addSeparator()
        self.menuKi_i_i_lemleri.addAction(self.actionKisi_Sil)
        self.menuRaporlar.addAction(self.actionKisi_Raporu)
        self.menuRaporlar.addSeparator()
        self.menuRaporlar.addAction(self.actionGenel_Rapor)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuKi_i_i_lemleri.menuAction())
        self.menubar.addAction(self.menuRaporlar.menuAction())
        self.toolBar_2.addAction(self.actionCihaz_Test)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_cikis, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.pushButton_baglan, QtCore.SIGNAL(_fromUtf8("clicked()")),self.baglan)
        QtCore.QObject.connect(self.pushButton_iptal, QtCore.SIGNAL(_fromUtf8("clicked()")),self.iptal)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Yoklama Sistemi", None))
        self.label_cihazDurum.setText(_translate("MainWindow", "Cihaz bağlı değil. Lütfen önce cihazı test edin", None))
        self.pushButton_baglan.setText(_translate("MainWindow", "Bağlan", None))
        self.pushButton_iptal.setText(_translate("MainWindow", "İptal", None))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya", None))
        self.menuKi_i_i_lemleri.setTitle(_translate("MainWindow", "Kişi işlemleri", None))
        self.menuRaporlar.setTitle(_translate("MainWindow", "Raporlar", None))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionYeni_Kisi_Ekle.setText(_translate("MainWindow", "Yeni Kişi Ekle", None))
        self.actionKisi_Ara.setText(_translate("MainWindow", "Kişi Ara", None))
        self.actionKisi_Sil.setText(_translate("MainWindow", "Kişi Sil", None))
        self.actionKisi_Raporu.setText(_translate("MainWindow", "Kişi Raporu", None))
        self.actionGenel_Rapor.setText(_translate("MainWindow", "Genel Rapor", None))
        self.action_cikis.setText(_translate("MainWindow", "Çıkış", None))
        self.actionCihaz_Test.setText(_translate("MainWindow", "Cihaz_test", None))
        self.actionCihaz_Test.setIconText(_translate("MainWindow", "Test", None))
        self.actionCihaz_Test.setToolTip(_translate("MainWindow", "Cihazı Test Eder", None))
        self.actionCihaz_Test.setWhatsThis(_translate("MainWindow", "cihaz test", None))
        self.actionCihaz_Test.setShortcut(_translate("MainWindow", "Ctrl+T", None))
        self.actionKart_Tan_mla.setText(_translate("MainWindow", "Kart Tanımla", None))
        self.actionCihaz_Test_2.setText(_translate("MainWindow", "Cihaz Test", None))
        self.actionKart_Tan_mla_2.setText(_translate("MainWindow", "Kart Tanımla", None))

