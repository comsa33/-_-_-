import pymysql
import sqlalchemy
import pandas as pd

df = pd.read_excel('한국어_단발성_대화_데이터셋.xlsx')
print(df.head())

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='160813',
                       db='chatbot')

cur = conn.cursor()
try:
    #{user}:{pw}@localhost/{db}
    engine = sqlalchemy.create_engine("mysql+pymysql://root:160813@localhost/chatbot")
    df.to_sql('short_sent_emo', engine)
except ValueError:
    print("Table already exists.")

cur.execute('select * from short_sent_emo')
short_sents = cur.fetchall()
train_X = []
train_Y = []
for sent in short_sents:
    train_X.append(sent[1])
    train_Y.append(sent[2])
print(train_X[:5])
print(train_Y[:5])