# _RNN (Recurrent Neural Network)_

## RNN이란?

- 입력과 출력을 시퀸스(sequence) 단위로 처리하는 모델
- 딥 러닝에 있어서 가장 기본적인 시퀸스 모델
- Recursive Neural Network와는 전혀 다른 개념!!

## RNN의 특징

- 은닉층의 노드에서 활성화 함수를 통해 나온 결과값을 출력층 방향으로 보냄
- 다시 은닉층 노드의 다음 계산의 입력으로 보내는 특징을 가짐

### RNN셀

- cell(셀): RNN에서 은닉층에서 활성화 함수를 통해 결과를 내보내는 역할을 하는 노드
- 이전의 값을 기억하려고 하는 일종의 메모리 역할을 수행하므로 메모리 셀이라고 표현
- 각각의 시점에서 바로 이전 시점에서의 은닉층의 메모리 셀에서 나온 값을 입력으로 사용하는 재귀적 활동을 함

### 은닉상태(hidden state)

- 메모리 셀이 출력층 방향으로 or 다음 시점의 자신에게 보내는 값
- t-1 시점의 메모리 셀이 보낸 은닉상태 값을 t 시점의 은닉 상태 계산을 위한 입력값으로 사용

## RNN에서의 자연어 처리

: 입력과 출력의 길이를 다르게 설계 할 수 있으므로 다양한 용도로 사용 가능

- one-to-many 모델의 경우, 하나의 이미지 입력에 대해 사진에 제목을 출력하는 이미지 캡셔닝 작업에 이용 가능
- many-to-one 모델의 경우 입력 문서가 긍정인지 부정인지를 판별하는 감성분류 or 스팸 메일 분류에 사용 간으
- many-to-many 모델의 경우 입력 문장으로 부터 대답 문장을 출력하는 챗봇과 번역기, 문서 요약 등의 작업 가능

## Keras로 RNN 구현예시

```python
# RNN 층을 추가하는 코드.
model.add(SimpleRNN(hidden_size)) # 가장 간단한 형태

# 추가 인자를 사용할 때
model.add(SimpleRNN(hidden_size, input_shape=(timesteps, input_dim)))

# 다른 표기
model.add(SimpleRNN(hidden_size, input_length=M, input_dim=N))
# 단, M과 N은 정수
```

- hidden_size = 은닉 상태의 크기를 정의. 메모리 셀이 다음 시점의 메모리 셀과 출력층으로 보내는 값의 크기(output_dim)와도 동일.
- RNN의 용량(capacity)을 늘린다고 보면 되며, 중소형 모델의 경우 보통 128, 256, 512, 1024 등의 값을 가진다.
- timesteps = 입력 시퀀스의 길이(input_length)라고 표현하기도 함. 시점의 수.
- input_dim = 입력의 크기.

## 깊은 순환 신경망(Deep Recurrent Neural Network)

- RNN도 다수의 은닉층을 가질 수 있음

ex) 은닉층 2개 추가

```python
model = Sequential()
model.add(SimpleRNN(hidden_size, return_sequences = True))
model.add(SimpleRNN(hidden_size, return_sequences = True))
```

## 양방향 순환 신경망(Bidirectional Recurrent Neural Network)

- 시점 t 에서 출력값을 예측할 때 이전 시점의 데이터뿐만 아니라, 이후 데이터로도 예측 할 수 있다는 아이디어에 기반
- 즉, RNN이 과거 시점의 데이터들뿐만 아니라 이후 시점의 데이터도 활용하기 위해 고안

ex) 은닉층이 4개인 경우

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Bidirectional

model = Sequential()
model.add(Bidirectional(SimpleRNN(hidden_size, return_sequences = True), input_shape=(timesteps, input_dim)))

model = Sequential()
model.add(Bidirectional(SimpleRNN(hidden_size, return_sequences = True), input_shape=(timesteps, input_dim)))
model.add(Bidirectional(SimpleRNN(hidden_size, return_sequences = True)))
model.add(Bidirectional(SimpleRNN(hidden_size, return_sequences = True)))
model.add(Bidirectional(SimpleRNN(hidden_size, return_sequences = True)))
```
