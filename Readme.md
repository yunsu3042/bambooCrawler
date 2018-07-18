## 대나무숲 데이터 분석에 대한 생각
1. 대나무 숲에 있는 글 중 최근 1년간 글들을 무작위로 수집해 자주 등장하는 단어들을 뽑아낸다.   50개에서 100개 정도 
2. 자주 등장했던 단어들 중에서 취업, 진로에 관련된 단어가 있는지 퍼센트는 얼마나 되는지 확인한다. 
3. 최근 1년간 글의 자주 등장한 단어에서 스트레스와 같은 부정적인 단어의 비율을 확인한다. 
4. 취업, 진로와 같은 키워드를 사용해서 서울대생이 취업에 대해서 가지고 있는 생각들을 알아본다. 최근 2년간 취업에 관련된 글중 자주 등장하는 단어들을 뽑아낸다. 50개에서 100개정도. 
5. 취업에 관한 글들에서 자주 등장하는 단어들에서 서울대생들이 취업에 대해서 가지고 있는 생각들을 분석해본다. (가능하다면 가정에 맞는 연구 결과를 끌어낼 수 있도록)
6. 취업에 관한 글들중에서 스트레스와 같은 부정적인 단어들의 비율을 확인한다.  
7. 무작위로 추출한 글들에서 발생하는 부정적인 단어와 비율을 비교해 취업에 대해서 서울대생들이 스트레스를 받고 있다는 것을 증명한다. 
8. 그 외에 서울대생들이 부여받았거나 체화된 이미지를 키워드를 잘 선택해 단어 분석해본다. 


### 진행된 사항
- 위의 사항들은 대부분 완료됨. 
- 크롤러를 제작해 최근 1년간 글들 약 5000 - 6000개를 가져와 텍스트 파일로 저장함. 
- 진로, 취업, 스트레스, 취직 키워드로 검색한 글들이 각각 100개정도씩 가져와 텍스트 파일로 저장함.
- 단어 추출 코드를 짜서 해당 파일들에서 자주 등장하는 단어들 추출했음. 


### 데이터 시각화
- 워드 클라우드를 사용해서 자주 등장하는 단어들을 시각화처리중 
https://worditout.com/user/1516498/settings/c10b8665e408b70db9e6098228f0c65f


### 데이터 분석 결과
아직 진짜 정말과 같은 단어를 지우지 않았는데 실제로 유용한 단어만 남겨놓는 필터링 작업이 필요함.
- 취업이라는 키워드로 100개의 글을 분석했을 때 나온 단어들.
```
[{'count': 271, 'tag': '사람'},
 {'count': 159, 'tag': '생각'},
 {'count': 140, 'tag': '취업'},
 {'count': 111, 'tag': '지금'},
 {'count': 109, 'tag': '친구'},
 {'count': 109, 'tag': '문제'},
 {'count': 106, 'tag': '너무'},
 {'count': 100, 'tag': '우리'},
 {'count': 94, 'tag': '사회'},
 {'count': 92, 'tag': '여성'},
 {'count': 91, 'tag': '대한'},
 {'count': 86, 'tag': '공부'},
 {'count': 84, 'tag': '대학'},
 {'count': 82, 'tag': '정말'},
 {'count': 81, 'tag': '때문'},
 {'count': 80, 'tag': '마음'},
 {'count': 76, 'tag': '학교'},
 {'count': 74, 'tag': '그냥'},
 {'count': 72, 'tag': '남성'},
 {'count': 71, 'tag': '사실'},
 {'count': 69, 'tag': '다른'},
 {'count': 68, 'tag': '학생'},
 {'count': 65, 'tag': '학점'},
 {'count': 64, 'tag': '자신'},
 {'count': 63, 'tag': '군대'},
 {'count': 61, 'tag': '학벌'},
 {'count': 57, 'tag': '시간'},
 {'count': 56, 'tag': '이제'},
 {'count': 56, 'tag': '정도'},
 {'count': 55, 'tag': '대해'},
 {'count': 52, 'tag': '이야기'},
 {'count': 51, 'tag': '하나'},
 {'count': 50, 'tag': '서울대'},
 {'count': 50, 'tag': '교대'},
 {'count': 46, 'tag': '조금'},
 {'count': 45, 'tag': '대숲'},
 {'count': 45, 'tag': '보고'},
 {'count': 44, 'tag': '능력'},
 {'count': 43, 'tag': '모든'},
 {'count': 42, 'tag': '남자친구'},
 {'count': 41, 'tag': '얘기'},
 {'count': 41, 'tag': '연애'},
 {'count': 41, 'tag': '남자'},
 {'count': 40, 'tag': '전공'},
 {'count': 40, 'tag': '일이'},
 {'count': 39, 'tag': '이번'},
 {'count': 39, 'tag': '이유'},
 {'count': 38, 'tag': '한번'},
 {'count': 38, 'tag': '처음'},
 {'count': 38, 'tag': '자기'},
 {'count': 38, 'tag': '가장'},
 {'count': 37, 'tag': '노력'},
 {'count': 37, 'tag': '물론'},
 {'count': 34, 'tag': '인생'},
 {'count': 34, 'tag': '아직'},
 {'count': 34, 'tag': '엄마'},
 {'count': 34, 'tag': '교사'},
 {'count': 33, 'tag': '노래'},
 {'count': 32, 'tag': '고민'},
 {'count': 32, 'tag': '여자'},
 {'count': 32, 'tag': '지방'},
 {'count': 32, 'tag': '여러분'},
 {'count': 32, 'tag': '모두'},
 {'count': 32, 'tag': '현재'},
 {'count': 32, 'tag': '다시'},
 {'count': 31, 'tag': '경우'},
 {'count': 31, 'tag': '항상'},
 {'count': 30, 'tag': '아빠'},
 {'count': 30, 'tag': '제도'},
 {'count': 30, 'tag': '일반'},
 {'count': 30, 'tag': '소리'},
 {'count': 30, 'tag': '표현'},
 {'count': 30, 'tag': '부모님'},
 {'count': 30, 'tag': '고등학교'},
 {'count': 29, 'tag': '교육'},
 {'count': 29, 'tag': '서로'},
 {'count': 29, 'tag': '학기'},
 {'count': 29, 'tag': '목소리'},
 {'count': 28, 'tag': '진짜'},
 {'count': 28, 'tag': '기업'},
 {'count': 28, 'tag': '차별'},
 {'count': 28, 'tag': '서울'},
 {'count': 27, 'tag': '학년'},
 {'count': 27, 'tag': '여기'},
 {'count': 27, 'tag': '상황'},
 {'count': 27, 'tag': '발언'},
 {'count': 27, 'tag': '너무나'},
 {'count': 27, 'tag': '모습'},
 {'count': 27, 'tag': '누구'},
 {'count': 26, 'tag': '블라인드'},
 {'count': 26, 'tag': '요즘'},
 {'count': 26, 'tag': '페미니즘'},
 {'count': 26, 'tag': '가지'},
 {'count': 26, 'tag': '위해'},
 {'count': 25, 'tag': '시험'},
 {'count': 25, 'tag': '미래'},
 {'count': 25, 'tag': '아이'},
 {'count': 25, 'tag': '동안'},
 {'count': 25, 'tag': '얼마나'},
 {'count': 24, 'tag': '이상'}]
 
```
