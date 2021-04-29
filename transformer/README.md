# Transformer

## Basic idea

- s2s 구조를 따르면서도, Attention만으로 구현한 모델
- RNN을 사용하지 않고 인코더-디코더 구로즐 설계
- Attention으로 인코더와 디코더를 설계

## 주요 하이퍼파라미터

- d_model: 인코더와 디코더에서 정해진 입력과 출력의 크기, 임베딩 벡터의 차원
- num_layer: 인코더와 디코더를 하나의 층으로 봤을 때, 층의 개수
- num_heads: Attention을 사용할 때, 병렬로 분할해서 결과값을 합침, 이 때 병렬의 개수
- d_ff: 트랜스포머 내부에는 피드 포워드 신경망 존재, 이 때 은닉층의 크기

## Basic mechanism

- s2s와 달리 인코더와 디코더가 1개 이상 존재할 수 있음
- 인코더로부터 입력 정보를 전달받아 디코더가 출력 결과를 만드는 것은 동일

## Positional Encoding

- 트랜스포머는 입력을 순차적으로 받지 않음, 단어의 위치 정보를 알려줄 다른 방법 필요
- 단어의 위치 정보를 얻기 위해 각 단어의 임베딩 벡터에 위치 정보들을 더해 입력으로 사용