from sentence_transformers import SentenceTransformer, util
import numpy as np
import socket
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import re


def cleanText(readData):
    text = re.sub(
        '[-=+,#/\?:^$.@*\"※~&%ㆍ!』△◆→◇▶ⓒ▲“’”\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text.strip()


app = Flask(__name__)


def test_news(corpus, query):
    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

    top_k = 1
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
    cos_scores = cos_scores.cpu()

    top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]

    t = 0
    for idx in top_results[0:top_k]:
        t = cos_scores[idx]

    return str(t)



@app.route('/', methods=['GET', 'POST'])
def hello_worlds():
    return render_template('index.html')


@app.route('/post', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':

        val = request.form['id_name']
        val2 = request.form['id_name2']
        texts = []
        texts.append(val2)
        score = test_news(texts, val)
        score = score[7:13]

        return render_template('result.html', title=val, output=val2, score=score)


@app.route('/get', methods=['GET', 'POST'])
def hello_worldsss():
    if request.method == 'POST':
        val = request.form['id_name']
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        r = requests.get(val, headers=head)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = cleanText(soup.find('h3', {'id': 'articleTitle'}).text)

        text = cleanText(soup.find('div', {'id': 'articleBodyContents'}).text)
        text = text.replace(
            'flash 오류를 우회하기 위한 함수 추가', '')
        text = text.replace(
            'function _flash_removeCallback {}', '')
        datas = {
            "title": title,
            "text": text,
        }
        res = requests.post('http://0.0.0.0:80/get',
                            headers=head, json=datas).text

        texts = []
        texts.append(res)
        score = test_news(texts, title)
        score = score[7:13]
        s = float(score)
        result = ''
        if s > 0.66:
            result = '상'
        elif s > 0.33:
            result = '중'
        else:
            result = '하'

        return render_template('result.html', title=title, text=text, output=res, score=score, result=result)


if __name__ == "__main__":
    model_path = './output/leeeeeoy-2021-06-28_09-55-50'
    embedder = SentenceTransformer(model_path)
    app.run(host='0.0.0.0', port=90, debug=True)
