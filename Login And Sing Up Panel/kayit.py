# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\kayit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 80, 391, 351))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.tc_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.tc_label.setFont(font)
        self.tc_label.setObjectName("tc_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tc_label)
        self.tc_text = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tc_text.setFont(font)
        self.tc_text.setObjectName("tc_text")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tc_text)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.ad_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.ad_label.setFont(font)
        self.ad_label.setObjectName("ad_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ad_label)
        self.ad_text = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ad_text.setFont(font)
        self.ad_text.setObjectName("ad_text")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ad_text)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.soyad_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.soyad_label.setFont(font)
        self.soyad_label.setObjectName("soyad_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.soyad_label)
        self.soyad_text = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.soyad_text.setFont(font)
        self.soyad_text.setObjectName("soyad_text")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.soyad_text)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.kullanici_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.kullanici_label.setFont(font)
        self.kullanici_label.setObjectName("kullanici_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.kullanici_label)
        self.kullanici_text = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kullanici_text.setFont(font)
        self.kullanici_text.setObjectName("kullanici_text")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.kullanici_text)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.parola_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.parola_label.setFont(font)
        self.parola_label.setObjectName("parola_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.parola_label)
        self.parola_text = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parola_text.setFont(font)
        self.parola_text.setObjectName("parola_text")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.parola_text)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.parolatekrar_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.parolatekrar_label.setFont(font)
        self.parolatekrar_label.setObjectName("parolatekrar_label")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.parolatekrar_label)
        self.parolatekrar_text = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parolatekrar_text.setFont(font)
        self.parolatekrar_text.setObjectName("parolatekrar_text")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.parolatekrar_text)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.FieldRole, spacerItem5)
        self.ulke_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.ulke_label.setFont(font)
        self.ulke_label.setObjectName("ulke_label")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.ulke_label)
        self.ulkesec = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.ulkesec.setFont(font)
        self.ulkesec.setObjectName("ulkesec")
        self.ulkesec.addItem("")
        self.ulkesec.addItem("")
        self.ulkesec.addItem("")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.ulkesec)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(450, 80, 131, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.kurallar = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.kurallar.setFont(font)
        self.kurallar.setObjectName("kurallar")
        self.verticalLayout.addWidget(self.kurallar)
        self.sozlesme = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sozlesme.setFont(font)
        self.sozlesme.setObjectName("sozlesme")
        self.verticalLayout.addWidget(self.sozlesme)
        self.abonelik = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.abonelik.setFont(font)
        self.abonelik.setObjectName("abonelik")
        self.verticalLayout.addWidget(self.abonelik)
        self.ivirzivir = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.ivirzivir.setFont(font)
        self.ivirzivir.setObjectName("ivirzivir")
        self.verticalLayout.addWidget(self.ivirzivir)
        self.uyeol_buton = QtWidgets.QPushButton(self.centralwidget)
        self.uyeol_buton.setGeometry(QtCore.QRect(440, 260, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.uyeol_buton.setFont(font)
        self.uyeol_buton.setObjectName("uyeol_buton")
        self.durum_label = QtWidgets.QLabel(self.centralwidget)
        self.durum_label.setGeometry(QtCore.QRect(20, 450, 591, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.durum_label.setFont(font)
        self.durum_label.setObjectName("durum_label")
        self.uyeliksistemi_label = QtWidgets.QLabel(self.centralwidget)
        self.uyeliksistemi_label.setGeometry(QtCore.QRect(0, 10, 641, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uyeliksistemi_label.sizePolicy().hasHeightForWidth())
        self.uyeliksistemi_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.uyeliksistemi_label.setFont(font)
        self.uyeliksistemi_label.setAlignment(QtCore.Qt.AlignCenter)
        self.uyeliksistemi_label.setObjectName("uyeliksistemi_label")
        self.girisyap_buton = QtWidgets.QPushButton(self.centralwidget)
        self.girisyap_buton.setGeometry(QtCore.QRect(440, 370, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.girisyap_buton.setFont(font)
        self.girisyap_buton.setObjectName("girisyap_buton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tc_label.setText(_translate("MainWindow", "TC KİMLİK NUMARASI*"))
        self.ad_label.setText(_translate("MainWindow", "AD*"))
        self.soyad_label.setText(_translate("MainWindow", "SOYAD*"))
        self.kullanici_label.setText(_translate("MainWindow", "KULLANICI ADI*"))
        self.parola_label.setText(_translate("MainWindow", "PAROLA*"))
        self.parolatekrar_label.setText(_translate("MainWindow", "PAROLA TEKRAR*"))
        self.ulke_label.setText(_translate("MainWindow", "ÜLKE"))
        self.ulkesec.setItemText(0, _translate("MainWindow", "A1"))
        self.ulkesec.setItemText(1, _translate("MainWindow", "A2"))
        self.ulkesec.setItemText(2, _translate("MainWindow", "A3"))
        self.kurallar.setText(_translate("MainWindow", "KURALLAR*"))
        self.sozlesme.setText(_translate("MainWindow", "SÖZLEŞME*"))
        self.abonelik.setText(_translate("MainWindow", "ABONELİK"))
        self.ivirzivir.setText(_translate("MainWindow", "IVIR ZIVIR"))
        self.uyeol_buton.setText(_translate("MainWindow", "ÜYE OL!"))
        self.durum_label.setText(_translate("MainWindow", "DURUM:"))
        self.uyeliksistemi_label.setText(_translate("MainWindow", "ÜYELİK SİSTEMİ"))
        self.girisyap_buton.setText(_translate("MainWindow", "GİRİŞ YAP !"))