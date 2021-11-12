import time
from datetime import datetime as dt

#"crt" means "current" in this code.
crtTime = dt.now()
crtHour = crtTime.hour
crtMin = crtTime.minute

print("현재 시간은", crtHour, "시", crtMin, "분 입니다.")
lectureTime = int(input("강의 총 시간(분)을 입력하세요: "))
accelValue = float(input("사용된 배속을 입력하세요: "))

shortenTime = lectureTime / accelValue
endHour = crtHour
endMin = crtMin + shortenTime

if endMin > 59:
    endHour = endHour + 1
    endMin = endMin - 60

print("강의가 끝날 때의 시간은 지금으로부터 '", shortenTime, "'분 후인 '", endHour, "시", endMin, "분 입니다.")
print("(프로그램은 5초 후 자동으로 종료됩니다.)")

time.sleep(5)
exit()
