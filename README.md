# _A.C.D Study_

## 공부내용

- <a href="https://github.com/leeeeeoy/A.C.D-study/blob/master/keras/README.md">Keras
- <a href="https://github.com/leeeeeoy/A.C.D-study/blob/master/RNN/README.md">RNN
- <a href="https://github.com/leeeeeoy/A.C.D-study/blob/master/keras/Functional-API/README.md">Functional-API
- <a href="https://github.com/leeeeeoy/A.C.D-study/blob/master/transformer/README.md">Transformer
- <a href="https://github.com/leeeeeoy/A.C.D-study/blob/master/attention%20mechanism/REAEME.md"/>Attention-Mechanism
- <a href="https://github.com/leeeeeoy/A.C.D-study/blob/master/bert/README.md">BERT</a>

## 참고 자료들

- <a href = "https://github.com/kavgan/ROUGE-2.0"/>ROUGE-2.0 - java
- <a href = "https://github.com/pltrdy/rouge">ROUGE-2.0 - python
- <a href = "https://danbi-ncsoft.github.io/works/2020/10/19/snorkel-label.html">Snorkel
- <a href = "https://tech.kakao.com/2018/12/13/khaiii/">Khaiii
- <a href = "https://wikidocs.net/33793">영어 임베딩
- <a href = "https://github.com/ratsgo/embedding/releases">한국어 임베딩
- <a href = "https://github.com/uoneway/Text-Summarization-Repo">KoBERT
- <a href = "https://github.com/uoneway/KoBertSum">KoBertSum
- <a href = "https://github.com/SKT-AI/KoBART">KoBART
- <a href = "https://github.com/Beomi/KcBERT">KcBERT
- <a href = "https://github.com/BM-K/KoSentenceBERT_SKTBERT"/>KoSentenceBERT_SKTBERT</a>

## 분류모델

### KoBART 요약 모델

- SKT-AI 에서 공개한 요약 모델 사용
- <a href = "https://github.com/seujung/KoBART-summarization">KoBART 요약 모델 참고 링크</a>

### KoBERT 유사도 모델

- KoBERT 유사도 모델에서 데이터 변경 후 직접 학습
- <a href = "https://github.com/BM-K/KoSentenceBERT_SKT">KoBERT 분류 모델 참고 링크</a>

### 동작

- 두 모델을 Flask 서버로 연결
- KoBART 모델 80 포트, KoBERT 모델 90포트 연결
- 네이버 뉴스를 기준으로 작성
- 해당 링크를 넣으면 제목, 원문, 요약문, 유사도를 반환

#### 결과 예시

<img src = "예시.gif">
