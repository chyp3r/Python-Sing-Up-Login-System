# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\giris.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Uii_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(717, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 100, 591, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.kullaniciadigiris_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.kullaniciadigiris_label.setFont(font)
        self.kullaniciadigiris_label.setObjectName("kullaniciadigiris_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.kullaniciadigiris_label)
        self.kullaniciadigiri_text = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.kullaniciadigiri_text.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.kullaniciadigiri_text.setFont(font)
        self.kullaniciadigiri_text.setObjectName("kullaniciadigiri_text")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kullaniciadigiri_text)
        self.sifregiris_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sifregiris_label.setFont(font)
        self.sifregiris_label.setObjectName("sifregiris_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sifregiris_label)
        self.sifregiris_text = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sifregiris_text.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.sifregiris_text.setFont(font)
        self.sifregiris_text.setObjectName("sifregiris_text")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sifregiris_text)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 701, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.girisyap_buton = QtWidgets.QPushButton(self.centralwidget)
        self.girisyap_buton.setGeometry(QtCore.QRect(110, 250, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.girisyap_buton.setFont(font)
        self.girisyap_buton.setObjectName("girisyap_buton")
        self.kayitol_buton = QtWidgets.QPushButton(self.centralwidget)
        self.kayitol_buton.setGeometry(QtCore.QRect(430, 250, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.kayitol_buton.setFont(font)
        self.kayitol_buton.setObjectName("kayitol_buton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 21))
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
        self.kullaniciadigiris_label.setText(_translate("MainWindow", "KULLANICI ADI"))
        self.sifregiris_label.setText(_translate("MainWindow", "ŞİFRE"))
        self.label_3.setText(_translate("MainWindow", "ÜYE GİRİŞİ"))
        self.girisyap_buton.setText(_translate("MainWindow", "GİRİŞ YAP"))
        self.kayitol_buton.setText(_translate("MainWindow", "KAYIT OL"))