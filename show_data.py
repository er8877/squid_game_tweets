from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QWidget
from PyQt5.QtGui import QColor
import pandas as pd
from transformers import pipeline

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setStyleSheet("QWidget{\n"
        "background-color:#C7F9CC\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 260, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
        "background-color:#22577A;\n"
        "color:#80ED99;\n"
        "border:5px solid #80ED99;\n"
        "border-radius:30px\n"
        "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.label10 = QtWidgets.QLabel(self.centralwidget)
        self.label10.setGeometry(QtCore.QRect(40, 675, 180, 45))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label10.setFont(font)
        self.label10.setStyleSheet("QLabel{\n"
        "background-color:#22577A;\n"
        "color:#80ED99;\n"
        "border:5px solid #80ED99;\n"
        "border-radius:20px\n"
        "}")
        self.label10.setAlignment(QtCore.Qt.AlignCenter)
        self.label10.setObjectName("label10")
    
        self.pushButton_predict_tweet = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_predict_tweet.setGeometry(QtCore.QRect(350, 732, 170, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_predict_tweet.setFont(font)
        self.pushButton_predict_tweet.setStyleSheet("QPushButton{\n"
        "background-color:#22577A;\n"
        "color:#80ED99;\n"
        "border:5px solid #80ED99;\n"
        "border-radius:20px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:#80ED99;\n"
        "color:#22577A;\n"
        "border:2px solid #22577A\n"
        "}")
        self.pushButton_predict_tweet.setObjectName("pushButton_predict_tweet")
        
        self.line_edit_tweet = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit_tweet.setGeometry(QtCore.QRect(230, 675, 540, 45))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.line_edit_tweet.setFont(font)
        self.line_edit_tweet.setStyleSheet("QLineEdit{\n"
        "background-color:#22577A;\n"
        "color:#80ED99;\n"
        "border:5px solid #80ED99;\n"
        "border-radius:12px\n"
        "}\n"
        "QLineEdit:hover{\n"
        "background-color:#80ED99;\n"
        "color:#22577A;\n"
        "border:2px solid #22577A\n"
        "}")
        self.line_edit_tweet.setPlaceholderText("Enter your tweet...")
        self.line_edit_tweet.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_tweet.setObjectName("line_edit_tweet")
        
        self.analysis = pd.read_csv("analysis.csv")
        
        self.tableWidget_infos = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_infos.setGeometry(QtCore.QRect(40, 120, 729, 530))
        self.tableWidget_infos.setStyleSheet("QTableWidget{\n"
        "background-color:#22577A;\n"
        "color:#80ED99;\n"
        "border:5px solid #80ED99;\n"
        "}\n"
        "::section{\n"
        "background-color:#22577A;\n"
        "color:#80ED99;\n"
        "}\n"
        "QTableCornerButton::section{\n"
        "background-color: black;"
        "}"
        )
        self.tableWidget_infos.setObjectName("tableWidget_infos")
        self.tableWidget_infos.setColumnCount(2) # the number of columns in table .
        self.tableWidget_infos.setRowCount(80019) # the number of rows in table .
        item = QtWidgets.QTableWidgetItem()
        item.setFont(QtGui.QFont("Arial", 15))
        self.tableWidget_infos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(QtGui.QFont("Arial", 15))
        self.tableWidget_infos.setHorizontalHeaderItem(1, item)
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(40, 40, 121, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("QPushButton{\n"
        "background-color:#22577A;\n"
        "color:#80ED99;\n"
        "border:5px solid #80ED99;\n"
        "border-radius:20px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:#80ED99;\n"
        "color:#22577A;\n"
        "border:2px solid #22577A\n"
        "}")
        self.pushButton_exit.setObjectName("pushButton_exit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.tableWidget_infos.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)  # Stretch the first column
        
        for tweets in range(len(self.analysis['tweet'])):
                create_item = QtWidgets.QTableWidgetItem(self.analysis['tweet'][tweets])
                create_item.setFont(QtGui.QFont("Arial", 12))
                
                self.tableWidget_infos.setItem(tweets, 0, create_item)
                
        for analyze in range(len(self.analysis['sentiment_analyze'])):
                create_item = QtWidgets.QTableWidgetItem(self.analysis['sentiment_analyze'][analyze].lower().capitalize())
                create_item.setFont(QtGui.QFont("Arial", 12))

                self.tableWidget_infos.setItem(analyze, 1, create_item)
                
        
        self.pushButton_exit.clicked.connect(lambda:MainWindow.close())
        
        self.pushButton_predict_tweet.clicked.connect(self.proccess_tweet)
        
        self.proccess_model = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
    
    
    def proccess_tweet(self):
        tweet = self.line_edit_tweet.text()
        tweet_item = QtWidgets.QTableWidgetItem(tweet)
        tweet_item.setFont(QtGui.QFont("Arial", 12))

        proccess = self.proccess_model(tweet)
        proccess_result = QtWidgets.QTableWidgetItem(proccess[0]['label'].lower().capitalize())
        proccess_result.setFont(QtGui.QFont("Arial", 12))

        
        row_count = self.tableWidget_infos.rowCount()
        
        self.tableWidget_infos.insertRow(row_count)
        self.tableWidget_infos.setItem(row_count, 0, tweet_item)
        self.tableWidget_infos.setItem(row_count, 1, proccess_result)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sentiment analyze"))
        self.label.setText(_translate("MainWindow", "Sentiment analysis"))
        self.label10.setText(_translate("MainWindow", "Enter a tweet : "))
        item = self.tableWidget_infos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tweet"))
        item = self.tableWidget_infos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Analyzed"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))
        self.pushButton_predict_tweet.setText(_translate("MainWindow", "Accept"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
