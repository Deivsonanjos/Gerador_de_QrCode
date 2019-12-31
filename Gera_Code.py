'''Todos Creditos reservados a KranioDEV'''

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqrcode
import os.path
import random
import string


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(415, 283)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 401, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Bt_random = QtWidgets.QPushButton(self.layoutWidget)
        
        self.Bt_random.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bt_random.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.Bt_random.setObjectName("Bt_random")
        self.gridLayout_2.addWidget(self.Bt_random, 2, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        
        self.label_2.setStyleSheet("font: 10pt \"Vani\";")
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.L_Nome = QtWidgets.QLineEdit(self.layoutWidget)
        self.L_Nome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.L_Nome.setObjectName("L_Nome")
        self.gridLayout_2.addWidget(self.L_Nome, 2, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.layoutWidget)
        
        self.label_1.setStyleSheet("font: 11pt \"Vani\";")
        self.label_1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_1.setObjectName("label_1")
        self.gridLayout_2.addWidget(self.label_1, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.L_Mensagem = QtWidgets.QLineEdit(self.layoutWidget)
        self.L_Mensagem.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.L_Mensagem.setObjectName("L_Mensagem")
        self.gridLayout_2.addWidget(self.L_Mensagem, 1, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 1, 1, 1)
        self.Bt_Create = QtWidgets.QPushButton(self.centralwidget)
        self.Bt_Create.setGeometry(QtCore.QRect(90, 170, 241, 23))
  
        self.Bt_Create.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.Bt_Create.setObjectName("Bt_Create")
        self.Lb_by = QtWidgets.QLabel(self.centralwidget)
        self.Lb_by.setGeometry(QtCore.QRect(320, 260, 91, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(True)
        self.Lb_by.setFont(font)
        self.Lb_by.setTextFormat(QtCore.Qt.PlainText)
        self.Lb_by.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.Lb_by.setObjectName("Lb_by")
        self.logs = QtWidgets.QLabel(self.centralwidget)
        self.logs.setGeometry(QtCore.QRect(70, 209, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.logs.setFont(font)
        self.logs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logs.setStyleSheet("color: rgb(56, 216, 32);")
        self.logs.setText("")
        self.logs.setAlignment(QtCore.Qt.AlignCenter)
        self.logs.setObjectName("logs")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setObjectName("actionHome")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerador de QRCode"))
        self.Bt_random.setText(_translate("MainWindow", "RANDOM"))
        self.label_2.setText(_translate("MainWindow", "FILE NAME"))
        self.label_1.setText(_translate("MainWindow", "MESSAGE"))
        self.Bt_Create.setText(_translate("MainWindow", "CREATE"))
        self.Lb_by.setText(_translate("MainWindow", "By: Deivson Anjos"))


#script com toda a funcionalidade do programa

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)


		#funcao para gera o Qr code
		def QrCode():
			
			#atribuindo o que esta nas caixas para cada variavel determinada
			mensagem = self.L_Mensagem.text()
			nome = self.L_Nome.text()

			letra_aleatoria = random.choice(string.ascii_uppercase)
			
			#verifica se ja existe algum arquivo no mesmo direorio com esse nome
			if os.path.exists(nome+".png"):

				#seta esta mensagem no lebal vazio(oculto)
				self.logs.setText("JA EXISTE:  "+nome+'.png'+"\nNOVO NOME: "+ nome+letra_aleatoria+".png")
				
				#novo nome para a imagem
				nome = nome + letra_aleatoria

			else:
				#seta esta mensagem no lebal vazio
				self.logs.setText("SALVO COM SUCESSO!")

			#gera o Qr code
			code = pyqrcode.create(mensagem)
			code.png(nome + ".png", scale=8)

		#Sequencia de caracter que usaremos na funcao 'palavras_random()'
		char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
		quantidade_de_caracter = 5
		
		#Gera uma sequencia de 5 caracteres como sugestões no botao RANDOM
		def palavras_random():
			palavra = ""

			while len(palavra) != quantidade_de_caracter:
				palavra = palavra + random.choice(char)
				self.L_Nome.setText(palavra)

				if len(palavra) == quantidade_de_caracter:
					return palavra


		#Limpa a caixa de sugestões
		self.L_Nome.setText("")

		#Invoca a funcao que gera o QR
		self.Bt_Create.clicked.connect(QrCode)

		#Invoca a funcao que as sugestões aleatorias
		self.Bt_random.clicked.connect(palavras_random)

		

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
