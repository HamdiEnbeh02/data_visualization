# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/128OMeji47gT8IHM7nCPc3yJKIJkDtkHq
"""

import pandas as pd

#!file -bi /content/MOH-SQW_Survey.xlsx

#!iconv -f latin1 -t utf8 /content/MOH-SQW_Survey.xlsx > /content/MOH-SQW_Survey_utf8.xlsx
url = "MOH-SQW_Survey.xlsx"
df = pd.read_excel(url, engine="openpyxl")
#df = pd.read_excel("https://github.com/HamdiEnbeh02/data_visualization/blob/3a6b893857cce985b7dd644f8dfb85a41da18665/MOH-SQW_Survey.xlsx")

df.head(10)



print(df.columns)

df.columns = df.columns.str.replace('\t', '')

print(df.columns)

col_check = [' What is your gender?', 'What is your age?', 'City']
df = df.dropna(subset=col_check, how='all')

columns_1 = [
    '1. I tend to bounce back quickly after hard times',
    '2. I have a hard time making it through stressful events',
    '3. It does not take me long to recover from a stressful event. ',
    '4. It is hard for me to snap back when something bad happens.',
    '5. I usually come through difficult times with little trouble. ',
    '6. I tend to take a long time to get over set-backs in my life.'
]
columns_2 = [
       'The effects of stress are negative and should be avoided.',
       'Experiencing stress facilitates my learning and growth.',
       'Experiencing stress depletes my health and vitality.',
       'Experiencing stress enhances my performance and productivity.',
       'Experiencing stress inhibits my learning and growth.',
       'Experiencing stress improves my health and vitality.',
       'Experiencing stress debilitates my performance and productivity.',
       'The effects of stress are positive and should be utilized.',
]
df[columns_1] = df[columns_1].fillna(df[columns_1].mode().iloc[0])
df[columns_2] = df[columns_2].fillna(df[columns_2].mode())

df['2. I have a hard time making it through stressful events'] = 6 - df['2. I have a hard time making it through stressful events']
df['4. It is hard for me to snap back when something bad happens.'] = 6 - df['4. It is hard for me to snap back when something bad happens.']
df['6. I tend to take a long time to get over set-backs in my life.'] = 6 - df['6. I tend to take a long time to get over set-backs in my life.']

df['Resilience Score'] = df[['1. I tend to bounce back quickly after hard times',
       '2. I have a hard time making it through stressful events',
       '3. It does not take me long to recover from a stressful event. ',
       '4. It is hard for me to snap back when something bad happens.',
       '5. I usually come through difficult times with little trouble. ',
       '6. I tend to take a long time to get over set-backs in my life.']].sum(axis=1)


total_questions_answered = df[['1. I tend to bounce back quickly after hard times',
       '2. I have a hard time making it through stressful events',
       '3. It does not take me long to recover from a stressful event. ',
       '4. It is hard for me to snap back when something bad happens.',
       '5. I usually come through difficult times with little trouble. ',
       '6. I tend to take a long time to get over set-backs in my life.']].count(axis=1)


df['Resilience Score'] = df['Resilience Score'] / total_questions_answered


print(df[['Resilience Score']])

mapping = {
    'Strongly disagree': 0,
    'Disagree': 1,
    'Neither Agree nor Disagree': 2,
    'Agree': 3,
    'Strongly Agree': 4
}


columns = [
    'The effects of stress are negative and should be avoided.',
    'Experiencing stress facilitates my learning and growth.',
    'Experiencing stress depletes my health and vitality.',
    'Experiencing stress enhances my performance and productivity.',
    'Experiencing stress inhibits my learning and growth.',
    'Experiencing stress improves my health and vitality.',
    'Experiencing stress debilitates my performance and productivity.',
    'The effects of stress are positive and should be utilized.'
]

for col in columns:
    df[col] = df[col].map(mapping)


df['The effects of stress are negative and should be avoided.'] = 4 - df['The effects of stress are negative and should be avoided.']
df['Experiencing stress depletes my health and vitality.'] = 4 - df['Experiencing stress depletes my health and vitality.']
df['Experiencing stress inhibits my learning and growth.'] = 4 - df['Experiencing stress inhibits my learning and growth.']
df['Experiencing stress debilitates my performance and productivity.'] = 4 - df['Experiencing stress debilitates my performance and productivity.']


df['Stress Mindset Score'] = df[columns].sum(axis=1)


print(df[['Stress Mindset Score']])
