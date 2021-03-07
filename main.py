from PyQt5 import QtCore, QtGui, QtWidgets
import math
import serial
import time
import logging
import os

from win_nks import Ui_Dialog_nks
from win_measCenter import Ui_Dialog_measCenter
from win_measCircle1 import Ui_Dialog_measCircle1
from win_measCircle2 import Ui_Dialog_measCircle2
from win_measCircle3 import Ui_Dialog_measCircle3

timestr = time.strftime("%Y%m%d-%H%M%S")
dirname = os.path.dirname(__file__)
fileloc = os.path.join(dirname, 'logs/')
logging.basicConfig(filename=fileloc + "WeitenMessenEDM-"+timestr+".log", level=logging.INFO, format='%(levelname)s : %(''asctime)s - %(''message)s')
logging.info("WeitenMessen EDM - Wurf/Stoss - gestartet")

# logging.info("text")
# logging.warning("text")
# logging.error("text")
# logging.critical("text")

mw = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 550))
        MainWindow.setMaximumSize(QtCore.QSize(600, 550))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(15, -1, 15, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_alles = QtWidgets.QVBoxLayout()
        self.verticalLayout_alles.setObjectName("verticalLayout_alles")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_alles.addItem(spacerItem)
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_alles.addWidget(self.label_title)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_alles.addItem(spacerItem1)
        self.horizontalLayout_com_gsi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_com_gsi.setObjectName("horizontalLayout_com_gsi")
        self.label_comport = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_comport.sizePolicy().hasHeightForWidth())
        self.label_comport.setSizePolicy(sizePolicy)
        self.label_comport.setMinimumSize(QtCore.QSize(75, 0))
        self.label_comport.setObjectName("label_comport")
        self.horizontalLayout_com_gsi.addWidget(self.label_comport)
        self.spinBox_comport = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_comport.setMinimumSize(QtCore.QSize(40, 25))
        self.spinBox_comport.setMaximumSize(QtCore.QSize(40, 25))
        self.spinBox_comport.setObjectName("spinBox_comport")
        self.horizontalLayout_com_gsi.addWidget(self.spinBox_comport)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_com_gsi.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_AbwKreis = QtWidgets.QLabel(self.centralwidget)
        self.label_AbwKreis.setEnabled(True)
        self.label_AbwKreis.setHidden(True)
        self.label_AbwKreis.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_AbwKreis.setObjectName("label_AbwKreis")
        self.verticalLayout_3.addWidget(self.label_AbwKreis)
        self.label_AbwKreis_number = QtWidgets.QLabel(self.centralwidget)
        self.label_AbwKreis_number.setEnabled(True)
        self.label_AbwKreis_number.setHidden(True)
        self.label_AbwKreis_number.setAlignment(QtCore.Qt.AlignCenter)
        self.label_AbwKreis_number.setObjectName("label_AbwKreis_number")
        self.verticalLayout_3.addWidget(self.label_AbwKreis_number)
        self.horizontalLayout_com_gsi.addLayout(self.verticalLayout_3)
        self.verticalLayout_alles.addLayout(self.horizontalLayout_com_gsi)
        spacerItem3 = QtWidgets.QSpacerItem(0, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_alles.addItem(spacerItem3)
        self.label_mittelpunkt = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_mittelpunkt.setFont(font)
        self.label_mittelpunkt.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_mittelpunkt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mittelpunkt.setObjectName("label_mittelpunkt")
        self.verticalLayout_alles.addWidget(self.label_mittelpunkt)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_alles.addItem(spacerItem4)
        self.horizontalLayout_disziplin = QtWidgets.QHBoxLayout()
        self.horizontalLayout_disziplin.setObjectName("horizontalLayout_disziplin")
        self.comboBox_AuswahlDisziplin = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_AuswahlDisziplin.sizePolicy().hasHeightForWidth())
        self.comboBox_AuswahlDisziplin.setSizePolicy(sizePolicy)
        self.comboBox_AuswahlDisziplin.setMinimumSize(QtCore.QSize(110, 30))
        self.comboBox_AuswahlDisziplin.setMaximumSize(QtCore.QSize(175, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_AuswahlDisziplin.setFont(font)
        self.comboBox_AuswahlDisziplin.setObjectName("comboBox_AuswahlDisziplin")
        self.comboBox_AuswahlDisziplin.addItem("")
        self.comboBox_AuswahlDisziplin.addItem("")
        self.comboBox_AuswahlDisziplin.addItem("")
        self.comboBox_AuswahlDisziplin.addItem("")
        self.horizontalLayout_disziplin.addWidget(self.comboBox_AuswahlDisziplin)
        self.label_Radius = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Radius.sizePolicy().hasHeightForWidth())
        self.label_Radius.setSizePolicy(sizePolicy)
        self.label_Radius.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Radius.setFont(font)
        self.label_Radius.setText("")
        self.label_Radius.setObjectName("label_Radius")
        self.horizontalLayout_disziplin.addWidget(self.label_Radius)
        self.checkBox_3NKS = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3NKS.sizePolicy().hasHeightForWidth())
        self.checkBox_3NKS.setSizePolicy(sizePolicy)
        self.checkBox_3NKS.setMinimumSize(QtCore.QSize(95, 0))
        self.checkBox_3NKS.setMaximumSize(QtCore.QSize(0, 16777215))
        self.checkBox_3NKS.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_3NKS.setObjectName("checkBox_3NKS")
        self.horizontalLayout_disziplin.addWidget(self.checkBox_3NKS)
        self.verticalLayout_alles.addLayout(self.horizontalLayout_disziplin)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_alles.addItem(spacerItem5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButton_WeiteMessen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_WeiteMessen.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_WeiteMessen.sizePolicy().hasHeightForWidth())
        self.pushButton_WeiteMessen.setSizePolicy(sizePolicy)
        self.pushButton_WeiteMessen.setMinimumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_WeiteMessen.setFont(font)
        self.pushButton_WeiteMessen.setObjectName("pushButton_WeiteMessen")
        self.horizontalLayout.addWidget(self.pushButton_WeiteMessen)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_alles.addLayout(self.horizontalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_alles.addItem(spacerItem8)
        self.horizontalLayout_weite = QtWidgets.QHBoxLayout()
        self.horizontalLayout_weite.setObjectName("horizontalLayout_weite")
        self.label_ErzielteWeite = QtWidgets.QLabel(self.centralwidget)
        self.label_ErzielteWeite.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ErzielteWeite.sizePolicy().hasHeightForWidth())
        self.label_ErzielteWeite.setSizePolicy(sizePolicy)
        self.label_ErzielteWeite.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_ErzielteWeite.setFont(font)
        self.label_ErzielteWeite.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ErzielteWeite.setObjectName("label_ErzielteWeite")
        self.horizontalLayout_weite.addWidget(self.label_ErzielteWeite)
        self.label_ErzielteWeite_number = QtWidgets.QLabel(self.centralwidget)
        self.label_ErzielteWeite_number.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ErzielteWeite_number.sizePolicy().hasHeightForWidth())
        self.label_ErzielteWeite_number.setSizePolicy(sizePolicy)
        self.label_ErzielteWeite_number.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_ErzielteWeite_number.setFont(font)
        self.label_ErzielteWeite_number.setText("")
        self.label_ErzielteWeite_number.setObjectName("label_ErzielteWeite_number")
        self.horizontalLayout_weite.addWidget(self.label_ErzielteWeite_number)
        self.verticalLayout_alles.addLayout(self.horizontalLayout_weite)
        self.horizontalLayout_letzteWeite = QtWidgets.QHBoxLayout()
        self.horizontalLayout_letzteWeite.setObjectName("horizontalLayout_letzteWeite")
        self.label_LetzteWeite = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_LetzteWeite.sizePolicy().hasHeightForWidth())
        self.label_LetzteWeite.setSizePolicy(sizePolicy)
        self.label_LetzteWeite.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_LetzteWeite.setFont(font)
        self.label_LetzteWeite.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_LetzteWeite.setObjectName("label_LetzteWeite")
        self.horizontalLayout_letzteWeite.addWidget(self.label_LetzteWeite)
        self.label_LetzteWeite_number = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_LetzteWeite_number.sizePolicy().hasHeightForWidth())
        self.label_LetzteWeite_number.setSizePolicy(sizePolicy)
        self.label_LetzteWeite_number.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_LetzteWeite_number.setFont(font)
        self.label_LetzteWeite_number.setText("")
        self.label_LetzteWeite_number.setObjectName("label_LetzteWeite_number")
        self.horizontalLayout_letzteWeite.addWidget(self.label_LetzteWeite_number)
        self.verticalLayout_alles.addLayout(self.horizontalLayout_letzteWeite)
        spacerItem9 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_alles.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.verticalLayout_alles)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMesse_Mittelpunkt = QtWidgets.QAction(MainWindow)
        self.actionMesse_Mittelpunkt.setObjectName("actionMesse_Mittelpunkt")
        self.actionMittelpunkt = QtWidgets.QAction(MainWindow)
        self.actionMittelpunkt.setObjectName("actionMittelpunkt")
        self.action3_Punkte_auf_Kreis = QtWidgets.QAction(MainWindow)
        self.action3_Punkte_auf_Kreis.setObjectName("action3_Punkte_auf_Kreis")
        self.actionBeenden = QtWidgets.QAction(MainWindow)
        self.actionBeenden.setObjectName("actionBeenden")
        self.actionLog_ffnen = QtWidgets.QAction(MainWindow)
        self.actionLog_ffnen.setObjectName("actionLog_ffnen")
        self.actionLade_Mittelpunkt = QtWidgets.QAction(MainWindow)
        self.actionLade_Mittelpunkt.setObjectName("actionLade_Mittelpunkt")
        self.actionFestpunkt_LOESCHEN = QtWidgets.QAction(MainWindow)
        self.actionFestpunkt_LOESCHEN.setCheckable(False)
        self.actionFestpunkt_LOESCHEN.setEnabled(False)
        self.actionFestpunkt_LOESCHEN.setObjectName("actionFestpunkt_LOESCHEN")
        self.menuSetup.addAction(self.actionMittelpunkt)
        self.menuSetup.addAction(self.action3_Punkte_auf_Kreis)
        self.menuSetup.addAction(self.actionFestpunkt_LOESCHEN)
        self.menuDatei.addAction(self.actionBeenden)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # noinspection PyTypeChecker
        self.comboBox_AuswahlDisziplin.currentIndexChanged.connect(self.changed_comboBox_AuswahlDisziplin)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weiten messen - Wurf/Stoß"))
        self.label_title.setText(_translate("MainWindow", "WeitenMessen EDM - Wurf/Stoß"))
        self.label_comport.setText(_translate("MainWindow", "COM-Port:"))
        self.label_AbwKreis.setText(_translate("MainWindow", "Abweichung vom Kreisdurchmesser (Soll):"))
        self.label_AbwKreis_number.setText(_translate("MainWindow", "TextLabel"))
        self.label_mittelpunkt.setText(_translate("MainWindow", "KEIN Mittelpunkt erfasst!"))
        self.comboBox_AuswahlDisziplin.setItemText(0, _translate("MainWindow", "Kugel"))
        self.comboBox_AuswahlDisziplin.setItemText(1, _translate("MainWindow", "Diskus"))
        self.comboBox_AuswahlDisziplin.setItemText(2, _translate("MainWindow", "Speer"))
        self.comboBox_AuswahlDisziplin.setItemText(3, _translate("MainWindow", "Hammer"))
        self.checkBox_3NKS.setToolTip(_translate("MainWindow", "ändert die Anzahl der Nachkommastellen, sowie das Rundungsverfahren"))
        self.checkBox_3NKS.setText(_translate("MainWindow", "Protokoll-Modus"))
        self.pushButton_WeiteMessen.setText(_translate("MainWindow", "Weite messen"))
        self.label_ErzielteWeite.setText(_translate("MainWindow", "Erzielte Weite:"))
        self.label_LetzteWeite.setText(_translate("MainWindow", "Letzte Weite:"))
        self.menuSetup.setTitle(_translate("MainWindow", "Setup"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.actionMesse_Mittelpunkt.setText(_translate("MainWindow", "Messe Mittelpunkt"))
        self.actionMittelpunkt.setText(_translate("MainWindow", "Mittelpunkt"))
        self.action3_Punkte_auf_Kreis.setText(_translate("MainWindow", "3 Punkte auf Kreis"))
        self.actionBeenden.setText(_translate("MainWindow", "Beenden"))
        self.actionLog_ffnen.setText(_translate("MainWindow", "Log öffnen"))
        self.actionLade_Mittelpunkt.setText(_translate("MainWindow", "Lade Mittelpunkt"))
        self.actionFestpunkt_LOESCHEN.setText(_translate("MainWindow", "Festpunkt LÖSCHEN"))

        self.actionBeenden.triggered.connect(self.close)
        # noinspection PyTypeChecker
        self.actionMittelpunkt.triggered.connect(self.clicked_actionMittelpunkt_messen)
        # noinspection PyTypeChecker
        self.action3_Punkte_auf_Kreis.triggered.connect(self.clicked_action3_Punkte_auf_Kreis_messen)
        self.actionFestpunkt_LOESCHEN.triggered.connect(self.clicked_actionFestpunkt_LOESCHEN)
        self.checkBox_3NKS.stateChanged.connect(self.changed_checkBox_3NKS)
        self.pushButton_WeiteMessen.clicked.connect(self.clicked_pushButton_WeiteMessen)

        self.comboBox_AuswahlDisziplin.setCurrentIndex(1)
        self.changed_comboBox_AuswahlDisziplin()
        self.changed_checkBox_3NKS()


    def serial_con(self):
        global ser
        cp = self.spinBox_comport.value()
        cp = "COM" + str(cp)
        ser = serial.Serial(port=cp, baudrate=19200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS)

        return ser

    def read(self):
        global strip1, strip2, e_data, n_data, falseGSI
        s = 'leer'
        windows_is_crap = 1
        falseGSI = 0

        sc = self.serial_con()

        while windows_is_crap == 1:
            time.sleep(0.001)
            s = str(sc.readline().decode('UTF8'))
            if s != 'leer':
                windows_is_crap = 0

        east = s.find('81.')
        north = s.find('82.')

        if s[0] == '*':
            # GSI16
            strip1 = 7 + 8
            strip2 = 15 + 8
        else:
            # GSI8
            strip1 = 7
            strip2 = 15

        e_data = float(s[east + strip1:east + strip2]) / 1000
        n_data = float(s[north + strip1:north + strip2]) / 1000

        logging.info("Messung: Neupunkt - Ost: " + str(e_data) + " Nord: " + str(n_data))
        ser.close()

        return e_data, n_data

    def beep_single(self):
        sc = self.serial_con()
        sc.write(b'%R1Q,11003:\r\n')

    def beep_triple(self):
        sc = self.serial_con()
        sc.write(b'%R1Q,11004:\r\n')

    def setup_mittelpunkt(self):
        self.Form_measCenter = QtWidgets.QWidget()
        ui = Ui_Dialog_measCenter()
        ui.setupUi(self.Form_measCenter)
        self.Form_measCenter.show()
        print("Mittelpunkt messen!")

        east_data, north_data = self.read()

        self.Form_measCenter.destroy()
        # logging.info("SERIAL: " + str(ser))
        logging.info("SETUP: Mittelpunkt - Mittelpunkt_Ost: " + str(east_data) + " Mittelpunkt_Nord: " + str(north_data))

        self.actionFestpunkt_LOESCHEN.setEnabled(True)
        return east_data, north_data

    def setup_3punkte(self):
        self.Form_measCircle1 = QtWidgets.QWidget()
        ui = Ui_Dialog_measCircle1()
        ui.setupUi(self.Form_measCircle1)
        self.Form_measCircle1.show()
        print("Punkt 1 auf dem Kreis anzielen!")

        x1, y1 = self.read()
        self.Form_measCircle1.destroy()

        self.Form_measCircle2 = QtWidgets.QWidget()
        ui = Ui_Dialog_measCircle2()
        ui.setupUi(self.Form_measCircle2)
        self.Form_measCircle2.show()
        print("Punkt 2 auf dem Kreis anzielen!")

        x2, y2 = self.read()
        self.Form_measCircle2.destroy()

        self.Form_measCircle3 = QtWidgets.QWidget()
        ui = Ui_Dialog_measCircle3()
        ui.setupUi(self.Form_measCircle3)
        self.Form_measCircle3.show()
        print("Punkt 3 auf dem Kreis anzielen!")

        x3, y3 = self.read()
        self.Form_measCircle3.destroy()

        a = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2
        b = ((x1 ** 2) + (y1 ** 2)) * (y3 - y2) + (x2 ** 2 + y2 ** 2) * (y1 - y3) + (x3 ** 2 + y3 ** 2) * (y2 - y1)
        c = (x1 ** 2 + y1 ** 2) * (x2 - x3) + (x2 ** 2 + y2 ** 2) * (x3 - x1) + (x3 ** 2 + y3 ** 2) * (x1 - x2)
        d = (x1 ** 2 + y1 ** 2) * (x3 * y2 - x2 * y3) + (x2 ** 2 + y2 ** 2) * (x1 * y3 - x3 * y1) + (
                x3 ** 2 + y3 ** 2) * (
                    x2 * y1 - x1 * y2)

        x = -b / (2 * a)
        y = -c / (2 * a)
        r = math.sqrt((b ** 2 + c ** 2 - 4 * a * d) / (4 * a ** 2))
        r = round(r, 3)

        logging.info("SETUP: 3 Punkte auf Kreis - Mittelpunkt_East: " + str(x) + " Mittelpunkt_North: " + str(y))
        self.actionFestpunkt_LOESCHEN.setEnabled(True)
        return x, y, r

    def close(self):
        logging.info("WeitenMessen EDM via Menue geschlossen")
        sys.exit()

    def log_serialException(self):
        ex = sys.exc_info()
        print(ex)
        logging.error(ex[0])
        logging.error(ex[1])
        logging.error(ex[2])

    def clicked_actionMittelpunkt_messen(self):
        global M_E, M_N
        logging.info("SETUP: Mittelpunkt - Start")
        try:
            M_E, M_N = self.setup_mittelpunkt()
            self.label_mittelpunkt.setText("Mittelpunkt erfolgreich erfasst!")
            self.label_mittelpunkt.setStyleSheet("color: rgb(50, 205, 50);")
            self.pushButton_WeiteMessen.setEnabled(True)
            logging.info("SETUP: Mittelpunkt - Beendet")
            return M_E, M_N
        except serial.SerialException:
            self.log_serialException()

    def clicked_action3_Punkte_auf_Kreis_messen(self):
        global M_E, M_N, Rbe
        logging.info("SETUP: 3 Punkte auf Kreis - Start")
        try:
            M_E, M_N, Rbe = self.setup_3punkte()
            abw = round((Rbe - R) * 1000, 1)
            self.label_AbwKreis_number.setText(str(abw) + " mm")
            self.label_AbwKreis.setHidden(False)
            self.label_AbwKreis_number.setHidden(False)
            if abw >= 5.0 or abw <= -5.0:
                self.label_AbwKreis_number.setStyleSheet("color: rgb(255, 0, 0);")
                myFont = QtGui.QFont()
                myFont.setBold(True)
                self.label_AbwKreis_number.setFont(myFont)
            self.label_mittelpunkt.setText("Mittelpunkt erfolgreich erfasst!")
            self.label_mittelpunkt.setStyleSheet("color: rgb(0, 80, 0);")
            self.pushButton_WeiteMessen.setEnabled(True)
            logging.info("SETUP: 3 Punkte auf Kreis - Beendet")
            return M_E, M_N
        except serial.SerialException:
            self.log_serialException()

    def clicked_actionFestpunkt_LOESCHEN(self):
        global M_E, M_N
        M_E, M_N = 0, 0
        logging.warning("SETUP: Mittelpunkt geloescht!")
        self.pushButton_WeiteMessen.setEnabled(False)
        self.label_mittelpunkt.setStyleSheet("color: rgb(255, 0, 0);")
        self.actionFestpunkt_LOESCHEN.setEnabled(False)

    def changed_checkBox_3NKS(self):
        if self.checkBox_3NKS.isChecked():
            logging.warning("Protokoll-Modus eingeschaltet")
            self.Form_nks = QtWidgets.QWidget()
            ui = Ui_Dialog_nks()
            ui.setupUi(self.Form_nks)
            self.Form_nks.show()
        else:
            logging.info("Protokoll-Modus ausgeschaltet")

    def clicked_pushButton_WeiteMessen(self):
        global P_E, P_N
        logging.info("Weite messen - Start")
        try:
            print("Punkt messen!")
            P_E, P_N = self.read()
            logging.info("Weite messen - Beendet")
            self.auswert(P_E, P_N, M_E, M_N)
        except serial.SerialException:
            self.log_serialException()

    def changed_comboBox_AuswahlDisziplin(self):
        global R
        if self.comboBox_AuswahlDisziplin.currentIndex() == 0:
            R = 1.0675
            self.label_Radius.setText("D = " + "%.3f" % (2*R) + "m" + " // " + "R = " + "%.4f" % R + "m")
            logging.info("Disziplin geaendert: Kugel")
        elif self.comboBox_AuswahlDisziplin.currentIndex() == 1:
            R = 1.25
            self.label_Radius.setText("D = " + "%.2f" % (2*R) + "m" + " // " + "R = " + "%.2f" % R + "m")
            logging.info("Disziplin geaendert: Diskus")
        elif self.comboBox_AuswahlDisziplin.currentIndex() == 2:
            R = 8.00
            self.label_Radius.setText("D = " + "%.2f" % (2*R) + "m" + " // " + "R = " + "%.2f" % R + "m")
            logging.info("Disziplin geaendert: Speer")
        elif self.comboBox_AuswahlDisziplin.currentIndex() == 3:
            R = 1.0675
            self.label_Radius.setText("D = " + "%.3f" % (2*R) + "m" + " // " + "R = " + "%.4f" % R + "m")
            logging.info("Disziplin geaendert: Hammer")
        return R

    def auswert(self, P_E, P_N, M_E, M_N):
        value = math.sqrt((M_E - P_E) ** 2 + (M_N - P_N) ** 2) - R
        if self.checkBox_3NKS.isChecked():
            value = round(value, 3)
            mw.append("%.3f" % value)
        else:
            value = math.floor(value * 100) / 100
            mw.append("%.2f" % value)
        logging.info("Weite messen: " + str(mw[-1]))
        self.label_ErzielteWeite_number.setText(str(mw[-1]) + " m")
        if len(mw) >= 2:
            self.label_LetzteWeite_number.setText(str(mw[-2]) + " m")
        # self.beep_triple()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
