# -*- coding: utf-8 -*-
doc1 = raw_input("첫번쨰 문장을 입력해주세요 : ")
doc2 = raw_input("두번째 문장을 입력해주세요 : ")
text1 = tuple(doc1) #첫번째 입력 문장을 음절 단위로 쪼갠다
text2 = tuple(doc2) #두번째 입력 문장을 음절 단위로 쪼갠다
trigram1 = [text1[x:x+3] for x in range(0,len(text1))] # 음절 단위로 쪼개진 문장1을 trigram(음절3개)씩 묶어준다
trigram2 = [text2[x:x+3] for x in range(0,len(text2))] # 음절 단위로 쪼개진 문장1을 trigram(음절3개)씩 묶어준다
trigram1_size = len(trigram1)
trigram2_size = len(trigram2)
trigram_intersection = [value for value in trigram1 if value in trigram2] ## 문장 1과 문장 2에서의 음절 trigram 교집합
trigram_intersection_size = len(trigram_intersection) ## trigram _intersection_size : trigram 교집합 사이즈
if trigram1_size <= trigram2_size:
    short_trigram = trigram1_size
else:
    short_trigram = trigram2_size  ## 문장 1과 문장 2의 음절 trigram 수를 비교하여 짧은 문장의 음절 trigram을 short_trigram에 저장
simillarity = float(trigram_intersection_size) / float(short_trigram)  ## 공통 trigram 개수 / 짧은 문장 trigram 개수 = 유사도
print(simillarity*100) ##음절 trigram 유사도 출력