# Fast R-CNN

## 기본 프로세스

- Selective Search를 통해 RoI를 찾음
- 전체 이미지를 CNN에 통과시켜 feature map을 추출
- Selective Search로 찾았던 RoI를 feature map 크기에 맞춰서 projection 시킴
- projection 시킨 RoI에 대해 RoI Pooling을 진행하여 고정된 크기의 feature vector를 얻음
- feature vector는 FC layer를 통과한 뒤, 구 브랜치로 나뉨
- 하나는 softmax를 통과하여 RoI에 대해 object classification
- bounding box regression을 통해 selective search로 찾은 box 위치 조정

## RoI (Region of Interest) Pooling

: feature map에서 관심 영역을 지정한 크기의 grid로 나눈 후 max pooling을 수행하는 방법

- 원본 이미지를 CNN 모델에 통과시켜 feature map을 얻음
- 이미지에 Selective Search 알고리즘을 적용하여 region proposals를 얻음
- feature map에서 region proposals에 해당하는 영역 추출
- 추출한 RoI feature map을 지정한 크기에 맞게 grid로 나눔
- grid의 각 셀에 대하여 max pooling을 수행, 고정된 크기의 feature map을 얻음

## Multi-task loss

: feature vector를 multi-task loss를 사용하여 Classifier와 Bounding box regressior을 동시에 학습

## Hierarchical Sampling

- SGD mini-batch를 구성할 때 N개의 이미지를 sampling하고, R개의 region proposal을 사용한다고 가정
- 각 이미지로부터 R/N개의 region proposals를 sampling 하는 방법
- 같은 이미지에서 추출 된 region proposals 끼리는 forward, backward propogation 시, 연산과 메모리 공유 가능

## Truncated SVD

: fc layer를 압축하는 방법
