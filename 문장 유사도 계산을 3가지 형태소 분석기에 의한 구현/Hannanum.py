import time
start = time.time()
from konlpy.tag import Hannanum
doc = input("문장을 입력해주세요 : ") ## 문장을 입력받는다
n = input("입력문장과 유사한 몇개의 문장을 출력할까요? : ") ## 유사한 문장을 몇개 출력할지 입력 받는다
print(" ")
hannanum = Hannanum() ##형태소 분석을 위하여 konlpy의 Hannanum class를 이용하여 준다
doc_tokenized = hannanum.morphs(doc) ##입력문장을 형태소 단위로 쪼개준다
doc_tokenized_size = len(doc_tokenized) ##입력문장의 형태소 개수

list=[]

with open('KCCq281000.txt', 'r', encoding='utf-8') as input:  # 유사도 검사할 말뭉치를 가져옴
    for line in input: ##말뭉치에서 라인 단위로 읽어준다
        file_tokenized = hannanum.morphs(line)  ##읽어들인 라인을 형태소 단위로 쪼개준다
        file_tokenized_size = len(file_tokenized)  ##읽어들인 라인의 형태소 개수
        intersection_size = 0  ##교집합 형태소 개수를 초기화
        for x in doc_tokenized:
            if x in file_tokenized:
                intersection_size+=1  ##입력문장과 라인문장을 비교하여 겹치는 형태소가 있다면 교집합 형태소 개수 증가시키기
        if len(doc) <= len(line):
            short = doc_tokenized_size
        else:
            short = file_tokenized_size  ## 입력문장과 파일 각 문장의(라인단위) 길이를 비교하여 짧은 문장의 형태소 개수를 short에 저장
        similarity = float(intersection_size) / float(short)  ## 공통 형태소 개수 / 짧은 문장소 형태소 개수 = 유사도
        list.append([line, similarity * 100])  ##list 배열에 문장과, 그문장의 입력문장에 대한 유사도를 집어넣어준다

    sorted_list = sorted(list, key=lambda x: -x[1])  ##list 배열을 유사도 순으로 정렬하여 준다(유사도가 높은순으로, 내림차순)
    for i in range(int(n)):
       print(sorted_list[i][0])  ##입력받은 n개의 유사도가 높은 문장을 출력한다.
       print("유사도는 " + str(sorted_list[i][1]) + "% 입니다.")  ##입력받은 n개의 유사도가 높은 문장의 유사도를 출력한다.
       print(" ")
       print(" ")

    print("소요시간 :", time.time() - start, "초")  # 소요시간 출력