import Def.googlemap

my_url = soup_obj.select("em.info_variation") # url로 데이터 가져오기
cnt = 0

key = ["코로나 확진자","검사 중인 환자"] # key값 가져오기
value = []

for j in my_url:  # class -> em.info_variation를 순서대로 Parsing한것
    cnt += 1
    value.append(j.text)
    if cnt > 1:
        break

Corona = {} # 코로나 Dictionary Data
for i in range(len(key)):
    Corona[key[i]] = value[i]
    
# 해당 날짜
now = datetime.datetime.now()
nowdate = now.strftime('%Y-%m-%d')

def getDay():
    now = time.localtime()
    of = ['월', '화', '수', '목', '금', '토', '일']
    return of[now.tm_wday]
weekday = getDay()

# 프린트 내용
print(nowdate +  ".("+ weekday+ ")")
for i in range(0,2):
    print(key[i] + " : " +  value[i])
    
# time.sleep(6000)
