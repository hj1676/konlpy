# -*- coding: utf-8 -*-
from konlpy.tag import Hannanum
hannanum = Hannanum()
doc1 = input("첫번쨰 문장을 입력해주세요 : ")
doc2 = input("첫번쨰 문장을 입력해주세요 : ")
hannanum1 = hannanum.morphs(doc1) ## 문장 1을 형태소 단위로 쪼개준다
hannanum2 = hannanum.morphs(doc2) ## 문장 2를 형태소 단위로 쪼개준다
hannanum1_size = len(hannanum1)
hannanum2_size = len(hannanum2)
hannanum_intersection = [value for value in hannanum1 if value in hannanum2] ## 문장 1과 문장 2에서의 형태소 교집합
hannanum_intersection_size = len(hannanum_intersection) ## hannanum intersection_size : 겹치는 형태소의 개수(사이즈)
if len(doc1) <= len(doc2):
    short_hannanum = hannanum1_size
else:
    short_hannanum = hannanum2_size  ## 문장 1과 문장 2의 길이를 비교하여 짧은 문장의 형태소 개수를 short_hannanum에 저장
simillarity = float(hannanum_intersection_size) / float(short_hannanum)  ## 공통 형태 개수 / 짧은 문장소 형태소 개수 = 유사도
print(simillarity*100) ##형태소 유사도 출력



