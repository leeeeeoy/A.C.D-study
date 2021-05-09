# BERT

: Bidirectional Encoder Representations from Transformers<br/>
: 대부분의 NLP 분야에서 좋은 성능을 보여주고 있는 모델

## Basic idea

- 레이블이 없는 많은 데이터로 사전 훈련
- 레이블이 있는 추가 훈련을 통한 하이퍼파라미터 조절

## BERT 학습방법

- self-attention layer를 여러 개 사용하여 token사이의 의미 관계 추출
- decoder를 사용하지 않고, encoder를 학습시킨 후 특정 task에 대해 fine-tuning 활용
- 단어뿐만 아니라 문장도 학습 가능
- 문장에서 일부 단어를 Mask 토큰으로 바꾼 뒤, 단어를 예측 --> 문맥 파악
