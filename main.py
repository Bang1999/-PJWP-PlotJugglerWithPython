import os
import sys
import numpy as np
import pandas as pd
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import matplotlib.pyplot as plt
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyqtgraph import *


PLOT_DT = 0.00001
VERSION = "0.1.0"

#### Step Load UI
def resource_path(relative_path): # 파일과 리소스의 경로 찾기
    # 리소스가 내부이면 파일 경로를, 외부이면 sys._MEIPASS를 base_path에 할당
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path) # 파일의 총 경로를 반환

UI_form = resource_path('MainWindow.ui') # ui 파일의 총 경로를 form에 할당
UI_form_class = uic.loadUiType(UI_form)[0] # 해당 파일을 uic class형태로 변환

class WindowClass(QMainWindow, UI_form_class): #QMainWindow와 ui를 변환한 class의 다중상속
    def __init__(self): # 초기값 설정
        super( ).__init__( ) # 부모 클래스의 초기값 호출
        self.setupUi(self) # Ui 를 셋업
        

        self.tree_fields = []           # 트리에있는 전체 데이터가 들어있는 영역
        self.time = 0                       # 시간 초기환
        self.time_started = False 
        self.wnum = 0                       # create window 클릭 횟수 저장소
        self.graph_window = []              # graph window 몇번 째인지
        self.recent_data = []               # 처음 불러들인 데이터의 columns이름 저장소
        
        
        # Load File 버튼이나 메뉴바 action
        self.actionLoad_File.triggered.connect(self.Load_File)
        self.btn_Load.clicked.connect(self.Load_File)
        
        # 새로운 윈도우 창 버튼 클릭          
        self.btn_Create.clicked.connect(self.create_graph_window)
        self.actionCreate_Graph_Window.triggered.connect(self.create_graph_window)

        
        # 천천히 구현할 close 하는 기능(클릭시)
        #self.actionExit.triggered.connect(self.on_closing)


    ###Bang의 코드 설계도를 바탕으로 한 코드###
    
    # 동기화하여 시작하게 끔 도와주는 함수
    '''def start_time(self):
        self.actionStart_Time'''
        
    # Main Window가 닫히면 메시지 뜨게 하는 함수
    '''def on_closing(self):
        #self.WindowClass.close()
        sys.exit()'''

        
    # csv 파일 load하는 함수
    def Load_File(self):
        ftype = [("CSV", "*.csv")]
        load_file = QFileDialog.getOpenFileName(self, filter='*csv', initialFilter='')      # csv파일만 읽을 수 있게
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
            self.tree_fields.append(['{}'.format(name)])         # self.tree_fields안에 트리에 있는 데이터 columns이름들이 들어있다
        self.update_selection_list()    


        # time slider 범위
        self.max_time = len(self.data.iloc[:, 0])
        self.Time_horizontalSlider.setRange(0, self.max_time)
        
    # 상단바 help -> about 버튼 클릭시 메시지 나오게 하는 함수
    '''def show_about_message(self):'''
        
        
    # 선택하는 event발생시, 인식하는 함수
    '''def on_select(self):'''
              
        
    # load한 csv의 columns의 목록들을 tree에 표시하는 함수
    def update_selection_list(self):
        # tree에 columns의 이름들 삽입

        parent = QTreeWidgetItem(self.Data_treeWidget)
        parent.setText(0, self.filename)

        for name in self.data.columns:
            child = QTreeWidgetItem(parent)
            child.setText(0, name)

    '''def Start_Drag(self, supportedActions):
        drag = QDrag(self)
        mimedata = self.model().mimeData(self.selectedIndexes())
        
        encoded = QByteArray()
        stream = QDataStream(encoded, QIODevice.WriteOnly)
        self.encodeDAta'''
        
    
    
    
    ''' 구현할 것들~~
    # 동기화 되어 진행할 때, 진행도를 나타나게끔 도와주는 slider를 change하게 해주는 함수
    def slider_changed(self, event):
        
        
    # list -> clear
    def clear_selection(self):
        
    
    # 동기화된 그래프가 진행되다 정지하게끔 해주는 함수
    def stop_time(self):
        
        
    # 진행 시간 제한 설정(최대 범위같은?)
    def proceed_time(self):
        
    '''    
    
    
    # 새로운 Graph Window를 띄우게하는 함수
    def create_graph_window(self):     

        self.x = self.data['x']                             # x data
        self.y = self.data['y']                             # y data
        
        
        # 그래프 그리는 창 갯수 늘리기
        self.graph_window.append(pg.PlotWidget())
        self.graph_window[self.wnum].setTitle("{} Graph Window".format(self.wnum+1))
        
        self.graph_window[self.wnum].setLabel("left", "{}".format('y'))
        self.graph_window[self.wnum].setLabel("bottom", "{}".format('x'))
        
        self.graph_window[self.wnum].showGrid(x=True, y=True)
        
        self.graph_window[self.wnum].plot(self.x,self.y)
        
        self.graph_window[self.wnum].show()
        
        self.wnum += 1                                      # 그래프 창 갯수 늘리는 변수 몇 번째 인지
     
        
if __name__ == '__main__':
    app = QApplication(sys.argv) # app 생성
    Window = WindowClass( ) # Ui를 myWindow에 할당
    Window.show( ) # Ui 출력
    app.exec_( ) # app무한루프