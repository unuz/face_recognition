# face_recognition
## python 얼굴 인식 프로젝트

### 구성도

``` bash
├── deepface
│  └── knowns             //이미지 폴더
│  └── template           //html 폴더
│  └── comparison.py      //인물 이미지 비교
│  └── deepface_test.py   //인물 이미지 분석
│  └── index.py           //flask route
│
├── face_recognition
│  └── knowns             //이미지 폴더
│  └── template           //html 폴더
│  └── camera.py          //카메라 실행
│  └── face_recog.py      //얼굴 인식
│  └── live_streaming.py  //flask route
└── README.md
```
# 개발 환경
- Tool : VS code
- OS : window 10
- python : Python 3.6.13
- anaconda : conda 4.12.0
- flask : 2.0.3

# deepface
## comparison.py 실행

### 첫번째 이미지
<img width="80%" src="https://user-images.githubusercontent.com/50819145/170943460-018c4c8a-c171-4e4d-85e4-59dc80d0d885.png" />

### 두번째 이미지
<img width="80%" src="https://user-images.githubusercontent.com/50819145/170943501-d7f88563-7271-42b4-b5dd-052dc2d19df4.png" />

### 두 이미지 비교 결과
<img width="80%" src="https://user-images.githubusercontent.com/50819145/170943526-b17fb0bb-a38e-4063-b933-f94014f19c6b.png" />

```
두 이미지를 비교해 같은 사람임을 확인 할 수 있다.
```
## deepface_test.py 실행
### 분석할 이미지
<img width="40%" src="https://user-images.githubusercontent.com/50819145/172785022-9832bfd4-ddc0-40a0-a452-108575b5e801.png" />

### 분석 결과
<img width="80%" src="https://user-images.githubusercontent.com/50819145/172785198-e9ff2c14-69c8-46d7-8d4f-8e2ce8a1ca36.png" />

```
나이 : 30, 
성별 : 남자, 
인종: 아시안,  
감정 : 중립적
```

# face_recognition
## camera.py 실행
<img width="80%" src="https://user-images.githubusercontent.com/50819145/172775367-e1cec703-639f-4612-8386-640317600ef1.png" />

## face_recognition.py 실행
<img width="80%" src="https://user-images.githubusercontent.com/50819145/172775658-fea2835c-0928-45ec-82b9-cafab941d038.png" />

## live_streaming.py 실행
<img width="80%" src="https://user-images.githubusercontent.com/50819145/172776022-58fc7cd8-e444-49c3-b240-096cbe6e104a.png" />

```
  얼굴을 인식해 yunho라고 알려주고 있다.
```
