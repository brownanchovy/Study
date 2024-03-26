###READ ME
#https://www.mit.edu/~ecprice/wordlist.10000에서 단어장 긁어옴 (완)
#지정한 횟수만큼 반복 가능 (완)
## ver2 확률분포 데이터 값 확보를 위해 5회로 지정하였음 (완)
### ver3 확률분포 새 데이터를 기존 데이터에 추가 (완)
## 데이터 확보를 위해 10회 실행하였음
#지정한 횟수 이후 각각의 시행 횟수를 도표로 확인가능
## ver2 각각의 시행 횟수를 리스트에 추가하여 확률분포로 확인 (완)
#정답과 오답에 추가음을 삽입 (완)
##정답을 맞출때까지 반복실행 (완)
#로그인 패스워드 기능 만들기 (완)
## ver2 텍스트 파일 만들어서 로그인 패스워드 정보 저장 및 불러오기 (완)
### ver3 계정에 사용 내역을 저장하여 기록 호출하는 기능 만들기(완)

#######마지막으로 코딩 최적화(진행 중)
import os.path
import random
import time
import matplotlib.pyplot as plt
import pandas as pd
import urllib.request
import winsound as sd
import numpy as np
from scipy.stats import norm
import Portal as P
import os
from pytube import YouTube
from playsound import playsound
def beepsound (fr, du):
    sd.Beep(fr, du)

def index_num (name):
    return database["name"].index(name)

class nomal_devi:
    def __init__(self, n, start, end, sec, what, loc, scale, c, f_end):
        x = np.arange(start, end, sec)
        axes[n].set_title(f'{what} Standard Normal Distribution')
        axes[n].set_xlabel('x')
        axes[n].set_ylabel('f(x)')
        axes[n].grid()
        axes[n].plot(x, norm.pdf(x, loc=loc, scale=scale))
        cum = np.arange(0, f_end, sec)
        axes[n].fill_between(cum, norm.pdf(cum, loc=loc, scale=scale), alpha=0.5, color=c)
        pro = norm(loc, scale).cdf(f_end) - norm(loc, scale).cdf(0)  # 3
        axes[n].text(0, 0.02, round(pro, 2), fontsize=20)

def loc(n,m):
    re = round(np.mean(n), m)
    return re
def scale(n,m):
    re = round(np.std(n), m)
    return re

def onlystr(str):
    try:
        int(str)
    except ValueError:
        return True

def get_val(str, col):
    return database.loc[database.index[(database["name"] == str)].tolist()[0],f"{col}"]

def save_val(str, col, val):
    database.loc[database.index[(database["name"] == str)].tolist()[0], f"{col}"] = val
def mk_file(out, str):
    try:
        if os.path.getsize(f'{str}.csv') > 0:
            out = pd.read_csv(f'{str}.csv')
            return out
        else:
            pass
    except FileNotFoundError:
        out.to_csv(f'{str}.csv', index=False)
def save(df, save):
    df.to_csv(f'{save}.csv', index=False)

#워드 크롤링
word_site = 'https://www.mit.edu/~ecprice/wordlist.10000'
response = urllib.request.urlopen(word_site)
long_txt = response.read().decode()
words = long_txt.splitlines()

#노래
if not os.path.isfile("Portal 2 Cara Mia Addio (full HQ audio).wav"):
    yt = YouTube('https://www.youtube.com/watch?v=tL_TFXbSnLY&ab_channel=LtCook')
    filepath = yt.streams.filter(only_audio=True).first().download()
    wavfilepath = filepath.replace('mp4', 'wav')
    os.rename(filepath, wavfilepath)

#시작
marker = 0
database = pd.DataFrame(columns =["name","passwd","ans_rate","es_time"])
num_his = pd.DataFrame({'correct_rate':[83.3, 71.4, 62.5, 100, 100, 71.4, 100, 83.3, 100, 100],
                        'time_took':[22.06, 35.56, 46.33, 15.61, 18.98, 26.97, 16.69, 22.28, 16.86, 15.46]}, dtype=float)

#파일 관리 해싱 불가능
database = mk_file(database,'Database').copy(deep=True)
num_his = mk_file(num_his, 'Number').copy(deep=True)

while True:
    print('****************')
    name = str(input("player name: ")).strip()
    if name in database["name"].tolist():
        passwd = str(input("passwd: ")).strip()
        while passwd != get_val(name,"passwd"):
            print("wrong passwd")
            passwd = input("passwd: ")
        else:
            print('****************')
            print(f"Welcome to Aperture Science, {name}")
            break
    else:
        marker = 1
        while True:
            print('****************')
            name = input("sign up: ").strip()
            passwd = input("passwd: ").strip()
            if onlystr(name) and onlystr(passwd):
                new_row = pd.DataFrame({'name': [name], 'passwd': [passwd], 'ans_rate': [0.0], 'es_time' : [0.0]})
                database = pd.concat([database, new_row], ignore_index=True)
                break
            else:
                pass

print("press enter to start game")
input()
print(database[['name', 'ans_rate', 'es_time']])

while True:
    # 정규분포 기반 세트 만들기
    fo, axes = plt.subplots(2, 1)

    if 'y' == input("wanna try? [Y/N]: ").lower():

        loc_1 = loc(num_his["correct_rate"].tolist(),1)
        loc_2 = loc(num_his["time_took"].tolist(),2)
        scale_1 = scale(num_his["correct_rate"].tolist(),1)
        scale_2 = scale(num_his["time_took"].tolist(),2)

        # 정답횟수
        n = 0
        # 오답횟수
        m = 0
        # 시작시간
        start_time = time.time()
        # 표준편차 데이터 값을 위해 5회로 지정
        while n < 5:
            print(f"*****round{n+1}*****")
            current_word = random.choice(words)
            print(f"word : {current_word}")
            user_input = input("type in  words: ")

            if user_input == current_word:
                print("correct!")
                beepsound(100, 1000)
                n += 1
            else:
                while user_input != current_word:
                    print("wrong, try again")
                    beepsound(7900,1000)
                    user_input = input("type in  words: ")
                    m += 1
                else:
                    print("correct!")
                    beepsound(100, 1000)
                    n +=1
                    pass

        end_time = time.time()
        es_time = round(end_time - start_time, 2)
        ans_rate = round((n / (n + m)) * 100, 1)
        print(f"{name}'s typing took {es_time}s")

        # 정답률 정규분포
        nomal_devi(0, 0, 100, 0.014, 'Answer', loc_1, scale_1, 'g', ans_rate)
        # 시간 정규 분포
        nomal_devi(1, 0, 40, 0.01, 'Time', loc_2, scale_2, 'r', es_time)
        # 그리기
        plt.show()

        #데이터 추가
        num_row = pd.DataFrame({"correct_rate": [ans_rate], "time_took": [es_time]})
        num_his = pd.concat([num_his, num_row], ignore_index=True)

        #저장
        if marker == 0:
            match (ans_rate >= get_val(name, "ans_rate"), es_time <= get_val(name, "es_time")):
                case (1, 1):
                    save_val(name,"ans_rate", ans_rate)
                    save_val(name,"es_time", es_time)
                    save(database, 'Database')
                    save(num_his, 'Number')
                    P.GLaDOS()
                    print('Here is your cake, HA-HA')
                case (1, 0):
                    save_val(name,"ans_rate", ans_rate)
                    save(database, 'Database')
                    save(num_his, 'Number')
                    P.Cube()
                    print('half cake')
                case (0, 1):
                    save_val(name,"es_time", es_time)
                    save(database, 'Database')
                    save(num_his, 'Number')
                    P.Cube()
                    print('half cake')
                case _:
                    P.Potato()
                    print('no cake')
        else:
            marker = 0
            save_val(name,"ans_rate", ans_rate)
            save_val(name,"es_time", es_time)
            save(database, 'Database')
            save(num_his, 'Number')
            print("Freshman")

        print(database, '\n')
        plt.cla()
        plt.clf()
        plt.close()

    else:
        #전적
        try:
            playsound("Portal 2 Cara Mia Addio (full HQ audio).wav")
        except:
            pass
        print(f'player {name}, your best answer rate is {get_val(name, "ans_rate")}, and shortest time in {get_val(name, "es_time")}')
        print('*****************')
        print(database[['name', 'ans_rate', 'es_time']])
        print('BYE')
        quit()
