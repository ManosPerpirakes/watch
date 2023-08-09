from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QLineEdit, QHBoxLayout, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
from time import time, ctime
from PyQt6.QtGui import QFont

def refresh():
    global timevar
    global timervar
    global timeforalarm
    text1 = str(ctime(time()))
    if timerstarted and timervar != 0:
        timervar -= 1
    if stopwatchstarted:
        timevar += 1
    text2 = 'Stopwatch: ' + str(timevar) + ' seconds'
    text3 = 'Timer: ' + str(timervar) + ' seconds'
    display.setText(text1 + '\n' + text2 + '\n' + text3)

def start():
    global stopwatchstarted
    stopwatchstarted = True

def stop():
    global stopwatchstarted
    stopwatchstarted = False

def reset():
    global timevar
    global stopwatchstarted
    stopwatchstarted = False
    timevar = 0

def startt():
    try:
        global timervar
        global timerstarted
        timervar = int(timerinput.text())
        timerinput.clear()
        timerstarted = True
    except:
        pass

def stopt():
    global timerstarted
    timerstarted = False

def resett():
    global timervar
    global timerstarted
    timervar = 0
    timerstarted = False

app = QApplication([])
w = QWidget()
timevar = 0
timervar = 0
timeforalarm = None
timerstarted = False
stopwatchstarted = False
w.resize(800, 500)
w.setWindowTitle("Watch")
display = QTextEdit('')
display.setFont(QFont('Arial', 15))
text1 = str(ctime(time()))
text2 = 'Stopwatch: ' + str(timevar) + ' seconds'
text3 = 'Timer: ' + str(timervar) + ' seconds'
l1 = QLabel('stopwatch controls')
l1.setFont(QFont('Arial', 15))
l2 = QLabel('timer controls')
l2.setFont(QFont('Arial', 15))
pb1 = QPushButton("start")
pb2 = QPushButton("stop")
pb3 = QPushButton("reset")
pb4 = QPushButton("start")
pb5 = QPushButton("stop")
pb6 = QPushButton("reset")
timerinput = QLineEdit()
timerinput.setPlaceholderText('input seconds:')
timer = QTimer()
lv1 = QVBoxLayout()
lh1 = QHBoxLayout()
lh2 = QHBoxLayout()
lh3 = QHBoxLayout()
lh1.addWidget(pb1)
lh1.addWidget(pb2)
lh1.addWidget(pb3)
lh2.addWidget(pb4)
lh2.addWidget(pb5)
lh2.addWidget(pb6)
lh3.addWidget(display)
lv1.addWidget(l1, alignment = Qt.AlignmentFlag.AlignHCenter)
lv1.addLayout(lh1)
lv1.addWidget(l2, alignment = Qt.AlignmentFlag.AlignHCenter)
lv1.addLayout(lh2)
lv1.addWidget(timerinput)
lh3.addLayout(lv1)
w.setLayout(lh3)
display.setText(text1 + '\n' + text2 + '\n' + text3)
w.show()
pb1.clicked.connect(start)
pb2.clicked.connect(stop)
pb3.clicked.connect(reset)
pb4.clicked.connect(startt)
pb5.clicked.connect(stopt)
pb6.clicked.connect(resett)
timer.timeout.connect(refresh)
timer.start(1000)
app.exec()