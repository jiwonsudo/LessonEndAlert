# 강의 배속 알림 프로그램 by Jiwon Jeong.
# Copyright 2021. Jiwon Jeong All rights reserved.

import time
from datetime import datetime as dt
from tkinter import *
from tkinter import messagebox as msgbox
    
def alert():
    msgbox.showinfo("알림", "수업이 종료 되었습니다.")

root = Tk()
root.withdraw()

#"crt" means "current" in this code.
crtTime = dt.now()
crtHour = crtTime.hour
crtMin = crtTime.minute

print("현재 시간은", crtHour, "시", crtMin, "분 입니다.")

lectureTime = int(input("강의 총 시간(분)을 입력하세요 (자연수) : "))

accelValue = float(input("사용된 배속을 입력하세요 (양의 유리수) : "))

shortenTime = lectureTime / accelValue
endHour = crtHour
endMin = crtMin + shortenTime

if endMin > 59:
    endHour = endHour + 1
    endMin = endMin - 60

print("강의가 끝날 때의 시간은 지금으로부터 '", shortenTime, "'분 후인 '", endHour, "시", endMin, "분 입니다.")

ans = str(input("강의가 끝나는 시간에 타이머 알람을 설정하시겠습니까? y/n : "))

if ans == "y":
    msgbox.showinfo("알림","타이머 알람을 설정하셨습니다. 남은 시간(분:초)은 프로그램 창에 나타납니다. '확인' 클릭 또는 'Enter' 입력 시 타이머가 시작됩니다.")
    timerSec = shortenTime*60
    while timerSec != 0:
        timerSec = timerSec - 1
        time.sleep(1)
        roundSec = round(timerSec)
        prtMin = roundSec // 60
        prtSec = roundSec % 60
        print(prtMin, ":", prtSec)
elif ans == "n":
    msgbox.showinfo("알림","타이머 알람을 설정하시지 않으셨습니다. '확인' 클릭 또는 'Enter' 입력 시 프로그램이 종료됩니다.")
    exit()
else:
    msgbox.showerror("에러","다른 키를 입력하셨습니다. '확인' 클릭 또는 'Enter' 입력 시 프로그램이 종료됩니다.")
    exit()

if timerSec == 0:
    alert()
    msgbox.showinfo("프로그램 종료", "'확인' 클릭 또는 'Enter' 입력 시 프로그램이 종료됩니다.")
    exit()
