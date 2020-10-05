# -*- coding: utf-8 -*-
doc1 = raw_input("첫번쨰 문장을 입력해주세요 : ")
doc2 = raw_input("두번째 문장을 입력해주세요 : ")
text1 = tuple(doc1) #첫번째 입력 문장을 음절 단위로 쪼갠다
text2 = tuple(doc2) #두번째 입력 문장을 음절 단위로 쪼갠다
bigram1 = [text1[x:x+2] for x in range(0,len(text1))] # 음절 단위로 쪼개진 문장1을 bigram(음절2개)씩 묶어준다
bigram2 = [text2[x:x+2] for x in range(0,len(text2))] # 음절 단위로 쪼개진 문장1을 bigram(음절2개)씩 묶어준다
bigram1_size = len(bigram1)
bigram2_size = len(bigram2)
bigram_intersection = [value for value in bigram1 if value in bigram2] ## 문장 1과 문장 2에서의 음절 bigram 교집합
bigram_intersection_size = len(bigram_intersection) ## ngrams_intersection_size : bigram 교집합 사이즈
if bigram1_size <= bigram2_size:
    short_bigram = bigram1_size
else:
    short_bigram = bigram2_size  ## 문장 1과 문장 2의 음절 bigram 수를 비교하여 짧은 문장의 음절 bigram을 short_ngrams에 저장
simillarity = float(bigram_intersection_size) / float(short_bigram)  ## 공통 bigram 개수 / 짧은 문장 bigram 개수 = 유사도
print(simillarity*100) ##음절 bigram 유사도 출력






