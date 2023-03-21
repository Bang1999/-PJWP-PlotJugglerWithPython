# [PJWP] PlotJugglerWithPython
**CP6 동계인턴십**

개발 기간 : 22.12.26 ~ 23.02.07

## Demo Video
![](https://github.com/Bang1999/PlotJugglerWithPython/blob/main/docs/Demo_Video.gif)

## Contents
- [01. Demo Video](#Demo-Video)
- [02. Environment](#Environment)
- [03. Project Goal](#Project-Goal)
- [04. Features](#Features)
- [05. Major features not implemented (Not Yet)](#Major-features-not-implemented-(Not-Yet))
- [06. Document](#Document)
- [07. Contributing & Support](#Contributing-&-Support)
- [08. Installation](#Installation)
- [09. Dependencies](#Dependencies)
- [10. LICENSE](#LICENSE)

## Environment
- MacOS Ventura 13.1
- Python 3.11.1
- Qt Designer 6.4
- VisualStudio Code 1.74.3



## Project Goal
[PlotJuggler](https://github.com/facontidavide/PlotJuggler)와 [pyplotjuggler](https://github.com/AtsushiSakai/pyplotjuggler)에서 영감을 받아 만들게 되었으며, UI 및 기능을 참조하여, CSV파일을 분석할 수 있는 애플리케이션을 만들었습니다.



## Features
- CSV File Load
- Load한 데이터를 각 columns에 맞게 MainWindow에 나타낼 수 있습니다.
- 다수의 Graph Window를 열 수 있습니다.
- MainWindow와 Graph Window의 크기를 자유롭게 조절 하실 수 있습니다.
- 각각의 x축, y축 또는 마우스 스크롤 등을 이용하여 확대/축소를 할 수 있습니다.
- Graph Window에서 마우스 오른쪽 버튼을 누르면 x축, y축의 범위를 조절할 수 있고, Plot Options, Mouse Mode 설정을 이용하여 여러 기능들을 이용하실 수 있습니다.
- Graph Synchronize 버튼을 눌러 다수의 창에 있는 그래프들을 동기화한 선을 만든 후, Start 버튼과 Stop 버튼을 이용하여 데이터를 분석 할 수 있습니다. (하나의 동기화 선만을 이용 가능 하신게 아니라 여러개의 동기화 선을 이용하실 수 있습니다.)
- 그래프의 분석이 완료가 되시면 마우스 오른쪽 버튼을 Graph Window창 위에서 누르시고 <Export..>, 그래프의 이미지를 자유로운 형식으로 다운로드 하실 수 있습니다.




## Major features not implemented (Not Yet)
- Drag and Drop 기능
- 대용량 CSV파일 수용
- 한 번에 여러 파일을 불러온 후, 자유롭게 띄우고 싶은 Column을 선택 후, Graph Window를 띄울 수 있는 기능
- 하나의 Graph Window에 여러개의 그래프를 그리는 기능
- 현재는 여러 그래프들을 동기화 하여 값을 분석 할 때, 마지막의 Graph Window만 MainWindow에 값이 나타나지만, 마지막의 그래프말고, 다른 그래프들의 값들도 나타내게끔 해주는 기능




## Document
- [요구사항 정의서](https://github.com/Bang1999/PlotJugglerWithPython/tree/main/docs/01.%20%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD%20%EC%A0%95%EC%9D%98%EC%84%9C)
- [기능 정의서](https://github.com/Bang1999/PlotJugglerWithPython/tree/main/docs/02.%20%EA%B8%B0%EB%8A%A5%20%EC%A0%95%EC%9D%98%EC%84%9C)
- [프로젝트 SRS](https://github.com/Bang1999/PlotJugglerWithPython/tree/main/docs/03.%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20SRS)
- [화면 설계서](https://github.com/Bang1999/PlotJugglerWithPython/tree/main/docs/04.%20%ED%99%94%EB%A9%B4%20%EC%84%A4%EA%B3%84%EC%84%9C)
- [아키텍처 설계서](https://github.com/Bang1999/PlotJugglerWithPython/tree/main/docs/05.%20%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98%20%EC%84%A4%EA%B3%84%EC%84%9C)
- [테스트 케이스](https://github.com/Bang1999/PlotJugglerWithPython/tree/main/docs/06.%20%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EC%BC%80%EC%9D%B4%EC%8A%A4)




## Contributing & Support
 - Contributing : **Bang1999**
 - Supported by [CP6](http://www.cp6.co.kr/)



## Installation
  1~2일이내로 올려드리겠습니다.



## Dependencies
- os : 사용자의 운영체제에서 CSV파일을 불러올 때 사용됩니다.
- sys : 파이썬 인터프리터를 제어할 수 있는 방법을 제공합니다.
- numpy : 동기화한 선이 움직일 때 현재 데이터의 값을 구할 때 사용됩니다.
- pandas : CSV파일을 읽을 때 사용됩니다.
- PyQt5 
  - QtCore : Qt프레임워크에서 사용하는 중요한 기능, 클래스 및 기타 유용한 기능을 사용합니다.
  - QtGui : Qt 응용프로그램의 GUI 구성 요소를 만드는 기능을 사용합니다.
  - QtWidgets : GUI 응용프로그램을 개발할 때 사용하는 기능을 사용합니다.
- pyqtgraph
  - PlotWidget : Graph Window를 띄울 때 사용합니다.
  - Plot : Graph Window에 그래프를 그릴 때 사용합니다.
  - InfiniteLine : 다수의 그래프를 동기화하여 분석하기 위한 선을 그릴 때 사용합니다.
  - QTimer : 위의 InfiniteLine을 움직일 때 사용합니다.


## LICENSE
[LICENSE](https://github.com/Bang1999/PlotJugglerWithPython/blob/main/LICENSE)
