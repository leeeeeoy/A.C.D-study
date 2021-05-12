# _**YOLO**_

: You Only Look Once

## YOLO의 강점

### 매우 빠르다

- Detection에서 Regression 문제로 해결했기 때문에 Complex pipline이 필요 없음
- 이미지 검출을 위해선 신경망만 작동 시키면 됨

### 이미지 전체를 두고 판단

- 학습과 평가에서 전체 이미지를 보기 때문에 생김새 뿐 아니라 contextual information를 부호화 함
- Fast R-CNN의 경우 큰 맥락을 보지 못함, 배경 부분을 물체로 인식
- YOLO는 이에 비해 배경 에러가 절반 정도에 그침

### 물체의 일반적 표현 학습

- 자연 이미지에서 학습하고 예술 작품으로 평가했을 때, 다른 알고리즘에 비해 높은 성능
- 보편성이 높아 새로운 영역이나 예상치 못한 입력에도 망가지는 경우 적음

## 기본 탐지 방법

### Grid 분할

- 여러 격자로 이미지를 나눔, S x S 형태
- 나눈 각 셀의 정보를 가지게 됨
- 나눈 각 셀의 pixel size와 중앙점을 가지게 됨

### Anchor Box

- 각각의 셀이 가지는 크기가 다른 박스, 보통 개발자마다 다름
- 비율이 정해져 있고 배열을 통해 픽셀 사이즈로 정할 수 있음

### Anchor Box의 정보

- Anchor Box의 정보가 매우 중요함, 0 ~ 1 사이의 값의로 normalize 됨
- P_o: 해당 cell에 물체가 있을 확률
- b_x, b_y: 해당 cell의 x, y 값, cell의 왼쪽 위 모서리에서부터 거리 값
- b_w, b_h: 해당 cell에 있는 Anchor Box의 w, h 값

### Grid Cell의 정보

- 각 cell에선 Anchor Box의 정보들로 구성, Box가 더 많다면 해당 파라미터들이 많아짐
- Class Probability: 해당 Bounding Box가 클래스 별로 몇 퍼센트를 갖는지에 대한 파라미터
- ex) Box가 2개이고 Class가 3개라면 P_01, b_x1, b_y1, b_w1, b_h1, P_02, b_x2, b_y2, b_w2, b_h2, c1, c2, c3 : 총 3 + 5 + 5 개의 파라미터를 가짐

### 최종 파라미터

- (S x S개의 Cell) x [{Cell 당 Anchor Box 갯수 x Box 파라미터 갯수(5)} + Class Probability 갯수]
- ex) 3 x 3개의 cell, 2개의 Anchor Box, 3개의 Class라고 가정, 9 x ((2 x 5) + 3) = 117 개의 파라미터

## 결과 도출 순서

### Letter Box Image 생성

- 네트워크 Input은 1:1의 비율을 가지기 때문에, 여분의 이미지를 새로 생성하는 작엄
- 이 단계를 Letter Box Image 라고 함
- 이 후 네트워크에 입력 이미지를 넣어줌, Train Data + Network Model + image가 Input으로 들어감

### Fully Connected Layer

- 위의 파라미터 계산식에 맞게 텐서 생성
- Bounding Box에 대한 Class Confidence Score 계산
- 모든 Box에 대해서 계산 후, 각 셀은 class-specific confidence score를 가지게 됨

### NMS 계산

- NMS(None-Maximum Suppression)을 통해 중복되는 Box 제거
- NMS: 하나의 Box를 기준으로 일정 Threshold를 정한 후, 다른 Box와 비교 후 교집합이 되는 부분이 Threshold보다 적을 시 제거하는 방법
- NMS 전에 기준 Box를 잡기 위해 Class Confidence Score를 기준으로 Box를 정렬 (Quick Sort 사용), YOLO v3 기준 0.4 or 0.5

## YOLO 알고리즘 단점

- 다른 알고리즘에 비해 정확도는 떨어짐
- 빠르게 감지하는 만큼 위치 파악에 어려움이 있음
- 이미지 크기에 따라 모델의 성능이 크게 달라짐, v3에서 개선됨
- Object가 겹쳐 있으면 제대로 예측이 되지 않음

## YOLO v4

- 1개의 GPU를 사용하는 일반적인 학습환경에서 효율적이도록 개선
