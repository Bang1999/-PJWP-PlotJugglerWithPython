import os
import sys
import numpy as np
import pandas as pd
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyqtgraph import *


#### Step Load UI
def resource_path(relative_path): # 파일과 리소스의 경로 찾기
    # 리소스가 내부이면 파일 경로를, 외부이면 sys._MEIPASS를 base_path에 할당
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path) # 파일의 총 경로를 반환

UI_form = resource_path('./MainWindow.ui') # ui 파일의 총 경로를 form에 할당
UI_form_class = uic.loadUiType(UI_form)[0] # 해당 파일을 uic class형태로 변환



class MainWindow(QMainWindow, UI_form_class): #QMainWindow와 ui를 변환한 class의 다중상속
    def __init__(self): # 초기값 설정
        super( ).__init__( ) # 부모 클래스의 초기값 호출
        self.setupUi(self) # Ui 를 셋업
        self.setAcceptDrops(True)
        

        self.tree_fields = []                               # 트리에있는 전체 데이터가 들어있는 영역
        self.time = 0                                       # 시간 초기환
        self.time_started = False                           # Start, Stop Button
        self.wnum = 0                                       # create window 클릭 횟수 저장소
        self.graph_window = []                              # graph window 몇번 째인지
        self.recent_data = []                               # 처음 불러들인 데이터의 columns이름 저장소
        
        
        # Load File 버튼이나 메뉴바 action
        self.actionLoad_File.triggered.connect(self.Load_File)
        self.btn_Load.clicked.connect(self.Load_File)
        
        # 새로운 윈도우 창 버튼 클릭          
        self.btn_Create.clicked.connect(self.create_graph_window)
        self.actionCreate_Graph_Window.triggered.connect(self.create_graph_window)

        # 그래프들 동기화 버튼
        self.btn_Syn.clicked.connect(self.InfiniteLine)
        self.actionSyn.triggered.connect(self.InfiniteLine)
        
        # 동기화된 그래프들 분석 시작~
        self.btn_Start.clicked.connect(self.start_movement)
        self.actionStart_Time.triggered.connect(self.start_movement)
        
        # 동기화된 그래프들 잠깐 멈춰!!
        self.btn_Stop.clicked.connect(self.stop_movement)
        self.actionStop_Time.triggered.connect(self.stop_movement)

    # csv 파일 load하는 함수
    def Load_File(self):
            ftype = "*.csv"
            load_file = QFileDialog.getOpenFileName(self, filter=ftype, initialFilter='')      # csv파일만 읽을 수 있게
            fpath = load_file[0]
            self.filename = os.path.basename(fpath)
            if not fpath: 
                return
            if "csv" in fpath:
                self.setup_csv_file(fpath)
    
    # 선택한 csv파일 읽는 함수
    def setup_csv_file(self, csv_path):
        self.data = pd.read_csv(csv_path)
        self.setup_loaded_data()
        
        
    # 불러온 csv file의 데이터 columns의 이름들을 self.recent_data에 저장
    def setup_loaded_data(self):
        for name in self.data.columns:
            self.recent_data.append(name)
            self.tree_fields.append(name)                   # self.tree_fields안에 트리에 있는 데이터 columns이름들이 들어있다
        self.update_selection_list()    

    # load한 csv의 columns의 목록들을 tree에 표시하는 함수
    def update_selection_list(self):
        # tree에 columns의 이름들 삽입
        parent = QTreeWidgetItem(self.Data_treeWidget)
        parent.setText(0, self.filename)
        for name in self.data.columns:
            child = QTreeWidgetItem(parent)
            child.setText(0, name)
            
    # 새로운 Graph Window를 띄우게하는 함수
    def create_graph_window(self):
        name = self.Data_treeWidget.currentItem()
        self.selected = name.text(0)        # -> Tree에서 선택한 것의 이름
        
        self.wnum = len(self.graph_window) + 1
        graph = self.Plot()
        self.graph_window.append(graph)
        self.graph_window[self.wnum-1].show()
    
    # 그래프 그리기
    def Plot(self):
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('w')
        self.plot_widget.setTitle("{} Graph".format(self.selected))
        self.plot_widget.showGrid(x=True, y=True)
        data = self.data[self.selected]
        self.x = []
        self.curve = []
        for i in range(len(data)):
            self.x.append(i)
        
        self.y = data
        
        self.plot_widget.plot(self.x, self.y)
        self.curve.append(self.plot_widget.plotItem.curves[0])
        return self.plot_widget        
    
    # 동기화 선 그리기
    def InfiniteLine(self):
        self.lines = []
        self.labels = []
        for i in range(self.wnum):
            self.line = pg.InfiniteLine(angle=90, movable=False)
            self.graph_window[i].addItem(self.line)
            self.lines.append(self.line)
            
            self.line_value_label = QLabel(self)
            self.line_value_label.move(100, 100)
            self.labels.append(self.line_value_label)
            
        self.x_val = 0
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.move_line)
        
    # Start to move InfiniteLine
    def start_movement(self):
        self.timer.start(100)
    
    # Stop moving InfiniteLine
    def stop_movement(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timers.start()
    
    # InfiniteLine Movement Setting
    def move_line(self):
        self.x_val += 0.1
        for i in range(self.wnum):
            self.lines[i].setValue(self.x_val)
            # Slider setting
            self.Slider.setRange(0, len(self.data)*10)
            self.Slider.setValue(self.Slider.value()+1)
            # y좌표 설정
            self.y_val = self.curve[i-1].getData()[1][np.argmin(np.abs(self.curve[i-1].getData()[0] - self.lines[i].value()))]
            self.labels[i].setText("Line value: {}".format(self.y_val))
            self.labels[i].show()
            

if __name__ == '__main__':
    app = QApplication(sys.argv) # app 생성
    Window = MainWindow( ) # Ui를 myWindow에 할당
    Window.show( ) # Ui 출력
    app.exec_( ) # app무한루프