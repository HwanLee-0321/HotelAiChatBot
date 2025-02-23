###########################################################
## data.txt파일을 불러와서 scraped.csv 파일로 변환하는 코드 ##
## Code to load data.txt and convert it into scraped.csv ##
###########################################################

import os
import pandas as pd
import re

def remove_newlines(text):
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r' +', ' ', text)
    return text

def text_to_df(data_file):
    texts = []
    with open(data_file, 'r', encoding="utf-8") as file:
        text = file.read()
        sections = text.split('\n\n')
        for section in sections:
            lines = section.split('\n')
            fname = lines[0]
            content = ' '.join(lines[1:])
            texts.append([fname, content])

    df = pd.DataFrame(texts, columns=['fname', 'text'])
    df['text'] = df['text'].apply(remove_newlines)
    return df

# 현재 스크립트 경로 기반으로 파일 경로 설정
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, 'data.txt')

df = text_to_df(data_file_path)
df.to_csv(os.path.join(script_dir, 'scraped.csv'), index=False, encoding='utf-8')