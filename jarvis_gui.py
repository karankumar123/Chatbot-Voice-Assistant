from jarvisUi4 import Ui_jarvisUi
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QTimer,QTime,QDate
from PyQt5.uic import loadUiType
#import main
import jarvis_main
import sys
import datetime



class MainThread(QThread):


    def __init__(self):

        super(MainThread , self).__init__()
    
    def run(self):
        
        jarvis_main.Task_Exe()
        
 
startExe = MainThread()
  
    
class Gui_Start(QMainWindow):
    

    def __init__(self):
        super().__init__()
        
        self.gui = Ui_jarvisUi()
        self.gui.setupUi(self)
          
        
        
        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)
       
        
    
    def startTask(self):
        
        self.gui.label1 = QtGui.QMovie("jarvis Gui Materail//B.G//Iron_Template_1.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()
        
        
        self.gui.label2 = QtGui.QMovie("jarvis Gui Materail//ExtraGui//live.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()
        
        
        self.gui.label3 = QtGui.QMovie("jarvis Gui Materail//VoiceReg//__1.gif")
        self.gui.Gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()
        
        self.gui.label4 = QtGui.QMovie("jarvis Gui Materail/ExtraGui/Earth.gif")
        self.gui.Gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()
        
        
        self.gui.label5 = QtGui.QMovie("jarvis Gui Materail/ExtraGui/B.G_Template_1.gif")
        self.gui.Gif_5.setMovie(self.gui.label5)
        self.gui.label5.start()
        
        
        
        
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(999)
        startExe.start()
        
        
        
        
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        label = "Time is:  " +label_time
        label1 ="Date is:  " +label_date
        
        self.gui.text_time.setText(label)  
        self.gui.text_date.setText(label1)
        # self.gui.textBrowser.setText("Listening......")
        
        
        
        
        
        
        
        

        
    
        
        
        
        
        
    
        
        
       
        
       
       
        
        
          
        

        
    
        
        
        
        
        
        
        

        
        
    
        
    
        
        
    
        
            
GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())

        
        
       
        
        
        
        
        
        
        
       
   
        
        
        