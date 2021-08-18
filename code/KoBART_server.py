from flask import Flask, render_template, request
import torch
from kobart import get_kobart_tokenizer
from transformers.models.bart import BartForConditionalGeneration
import socket
import requests
from bs4 import BeautifulSoup
import re


def cleanText(readData):
    text = re.sub(
        '[-=+,#/\?:^$.@*\"※~&%ㆍ!』△◆→◇▶ⓒ▲“’”\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text.strip()


def load_model():
    model = BartForConditionalGeneration.from_pretrained('./kobart_summary')
    return model


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_worlds():
    return render_template('index.html')


@app.route('/post', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':

        val = request.form['id_name']
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

        r = requests.get(
            val, headers=head)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = cleanText(soup.find('h3', {'id': 'articleTitle'}).text)

        text = cleanText(soup.find('div', {'id': 'articleBodyContents'}).text)
        print(text)
        text = text.replace(
            'flash 오류를 우회하기 위한 함수 추가', '')
        text = text.replace(
            'function _flash_removeCallback {}', '')
        print(text)
        data = title + ',' + text

        text = text.replace('\n', '')
        input_ids = tokenizer.encode(text)
        input_ids = torch.tensor(input_ids)
        input_ids = input_ids.unsqueeze(0)
        output = model.generate(input_ids, eos_token_id=1,
                                max_length=512, num_beams=5)
        output = tokenizer.decode(output[0], skip_special_tokens=True)

        return output


@app.route('/get', methods=['GET', 'POST'])
def hello_worldss():
    if request.method == 'POST':
        print(request.is_json)
        datas = request.get_json()
        text = datas["text"]
        text = text.replace('\n', '')
        input_ids = tokenizer.encode(text)
        input_ids = torch.tensor(input_ids)
        input_ids = input_ids.unsqueeze(0)
        output = model.generate(input_ids, eos_token_id=1,
                                max_length=512, num_beams=5)
        output = tokenizer.decode(output[0], skip_special_tokens=True)

        return output


if __name__ == "__main__":
    model = load_model()
    tokenizer = get_kobart_tokenizer()
    app.run(host='0.0.0.0', port=80, debug=True)
