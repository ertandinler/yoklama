# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kisi_ekle.ui'
#
# Created: Mon Sep  1 10:57:35 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("simgeler/ekle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(388, 307)
        Form.setWindowIcon(icon)
        self.pushButton_ekle = QtGui.QPushButton(Form)
        self.pushButton_ekle.setGeometry(QtCore.QRect(100, 190, 190, 31))
        self.pushButton_ekle.setObjectName(_fromUtf8("pushButton_ekle"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 41, 351, 101))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_ad = QtGui.QLabel(self.layoutWidget)
        self.label_ad.setObjectName(_fromUtf8("label_ad"))
        self.gridLayout_2.addWidget(self.label_ad, 1, 0, 1, 1)
        self.label_soyad = QtGui.QLabel(self.layoutWidget)
        self.label_soyad.setObjectName(_fromUtf8("label_soyad"))
        self.gridLayout_2.addWidget(self.label_soyad, 2, 0, 1, 1)
        self.label_tc = QtGui.QLabel(self.layoutWidget)
        self.label_tc.setObjectName(_fromUtf8("label_tc"))
        self.gridLayout_2.addWidget(self.label_tc, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_ad = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_ad.setObjectName(_fromUtf8("lineEdit_ad"))
        self.lineEdit_ad.setInputMask('')
        self.lineEdit_ad.setMaxLength(40)
        self.gridLayout.addWidget(self.lineEdit_ad, 0, 0, 1, 1)
        self.lineEdit_soyad = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_soyad.setObjectName(_fromUtf8("lineEdit_soyad"))
        self.lineEdit_soyad.setInputMask('')
        self.lineEdit_soyad.setMaxLength(40)
        self.gridLayout.addWidget(self.lineEdit_soyad, 1, 0, 1, 1)
        self.lineEdit_tc = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_tc.setInputMask('9'*11)
        self.lineEdit_tc.setObjectName(_fromUtf8("lineEdit_tc"))
        self.gridLayout.addWidget(self.lineEdit_tc, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.label_ad.setBuddy(self.lineEdit_ad)
        self.label_soyad.setBuddy(self.lineEdit_soyad)
        self.label_tc.setBuddy(self.lineEdit_tc)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_ekle, QtCore.SIGNAL(_fromUtf8("clicked()")),self.Kaydet)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_ad, self.lineEdit_soyad)
        Form.setTabOrder(self.lineEdit_soyad, self.lineEdit_tc)
        Form.setTabOrder(self.lineEdit_tc, self.pushButton_ekle)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Kişi Ekleme Sayfası", None))
        self.pushButton_ekle.setText(_translate("Form", "Ekle", None))
        self.label_ad.setText(_translate("Form", "Adı :", None))
        self.label_soyad.setText(_translate("Form", "Soyadı :", None))
        self.label_tc.setText(_translate("Form", "T.C No :", None))

