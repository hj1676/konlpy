# -*- coding: utf-8 -*-
doc1 = raw_input("첫번쨰 문장을 입력해주세요 : ")
doc2 = raw_input("두번째 문장을 입력해주세요 : ")
text1 = tuple(doc1) #첫번째 입력 문장을 음절 단위로 쪼갠다
text2 = tuple(doc2) #두번째 입력 문장을 음절 단위로 쪼갠다

bigram1 = [text1[x:x+2] for x in range(0,len(text1))] # 음절 단위로 쪼개진 문장1을 bigram(음절2개)씩 묶어준다
trigram1 = [text1[x:x+3] for x in range(0,len(text1))] # 음절 단위로 쪼개진 문장1을 trigram(음절3개)씩 묶어준다
bitri1 = bigram1+trigram1 ##bigram으로 쪼개진 리스트와 trigram으로 쪼개진 리스트를 합쳐준다
bitri1_size = len(bitri1)

bigram2 = [text2[x:x+2] for x in range(0,len(text2))] # 음절 단위로 쪼개진 문장2를 bigram(음절2개)씩 묶어준다
trigram2 = [text2[x:x+3] for x in range(0,len(text2))] # 음절 단위로 쪼개진 문장2 trigram(음절3개)씩 묶어준다
bitri2 = bigram2+trigram2 ##bigram으로 쪼개진 리스트와 trigram으로 쪼개진 리스트를 합쳐준다
bitri2_size = len(bitri2)

bitri_intersection = [value for value in bitri1 if value in bitri2] ## 문장 1과 문장 2에서의 음절 bitrigram 교집합
bitri_intersection_size = len(bitri_intersection) ## bitri_intersection_size : bitrigram 교집합 사이즈
if bitri1_size <= bitri2_size:
    short_bitri = bitri1_size
else:
    short_bitri = bitri2_size  ## 문장 1과 문장 2의 음절 bitrigram 수를 비교하여 짧은 문장의 음절 bitrigram을 short_bitri에 저장
simillarity = float(bitri_intersection_size) / float(short_bitri)  ## 공통 bitrigram 개수 / 짧은 문장 bitrigram 개수 = 유사도
print(simillarity*100) ##음절 bi+trigram 유사도 출력