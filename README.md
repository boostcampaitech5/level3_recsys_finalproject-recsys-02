# 🍷 개인 맞춤형 와인 추천 서비스 WINERY
![web-20171215150854806914](https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-02/assets/81154552/e7ec04fe-3df7-452e-8c3e-843effe044d9)

<br/>

**🍾 [WINERY 이용하러 가기](http://101.101.209.71:30005/) 🍾** 

<br/>

## 👯 Team

**Boostcamp AI Tech 5기 Recsys 2조, Recommy입니다** 😄

| <img src="https://github.com/boostcampaitech5/level2_dkt-recsys-02/assets/81154552/724270d2-d130-4832-874f-55f6749a5138" width="100px"/> | <img src="https://github.com/boostcampaitech5/level2_dkt-recsys-02/assets/81154552/cc8fdb78-9fad-4d4d-8ab3-6651aa6fa294" width="100px"/> | <img src="https://github.com/boostcampaitech5/level2_dkt-recsys-02/assets/81154552/b0df4dd3-6806-452b-8587-a020fd12f959" width="100px"/> | <img src="https://github.com/boostcampaitech5/level2_dkt-recsys-02/assets/81154552/55c86f49-5a1d-4eb7-8eda-c81978836855" width="100px"/> | <img src="https://github.com/boostcampaitech5/level2_dkt-recsys-02/assets/81154552/cef552eb-9d54-408a-8c48-71bfac727cea" width="100px" /> |
| :---: | :---: | :---: | :---: | :---: |
| [김동환](https://github.com/dhkim77000) | [김영서](https://github.com/0seokim) | [박재성](https://github.com/jaeseong98) | [전예원](https://github.com/yewonhihi) | [진성호](https://github.com/PoPoMonS) |

<br/>

## 🤔 Project Introduction

> 개인의 취향과 개성을 중시하는 시대가 되면서 이색적인 것과 트렌트에 민감해지고 와인을 찾는 20-30대도 증가하는 추세가 되고 있다. 하지만, 처음 접하는 초보자가 자신에게 맞는 와인을 찾기는 매우 어려우며, 정보 또한 찾아보기 힘들다. 따라서, MBTI와 같은 접근성 좋은 테스트를 통해서 쉽게 맞춤형 와인 추천과 정보를 제공하고자 한다.


- 진행기간 : 6월 26일 (월) 10:00 ~ 7월 28일 (금) 13:00

<br/>

## 💎 Data
![Untitled2](https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-02/assets/81154552/07055940-ca2b-42ce-ae02-22a6070ba854)
- 세계적인 와인 커뮤니티이자 온라인 판매처인 **Vivino**의 데이터를 크롤링
- 각 와인에 대한 feedback 데이터: metadata만으로 잘 표현이 되지 않는 와인의 특성을 표현하기 위해 텍스트 리뷰를 크롤링하여 텍스트 임베딩에 활용

<br/>

## 🗺️ Service Architecture
![Untitled](https://github.com/boostcampaitech5/level3_recsys_finalproject-recsys-02/assets/81154552/1ff82225-2549-4329-9a5a-995f742d980d)

<br/>

## ⚙️ Project Architecture


```bash
├── code
│   ├── feature_map # id2idx , item2idx 등 idx를 정리한 json 파일
│   ├── text # 와인 텍스트 전처리 및 학습 코드
│	│   ├── train_bert.py
│	│   ├── train_bert_multilabel.py
│	│   └── train_utils.py
│   └── data # 데이터 전처리 파이프라인 코드
├── crawl # crawling 코드
├── EDA.ipynb # 수집된 데이터 EDA 및 전처리
├── Recbole # Recbole 실험 코드
│   ├── basic.yaml
│   ├── args.py
│   ├── train.py
│   ├── inference.py
│   ├── utils.py
├── front # Frontend 코드
│		├── Api.js
│		├── App.js
│		├── Group.js
│		├── Home.js
│		├── Login.js
│		├── Mbti.js
│		├── MbtiQ.js
│		├── MbtiS.js
│		├── Recommend.js
│		├── Search.js
│		├── Sign.js
│		├── StackNavigator.js
│		├── StarButton.js
│		├── StarRating.js
│		├── WineInfo.js
│		├── app.json
│		├── assets
│		│   ├── banner
│		│   ├── logo.png
│		│   ├── mbti
│		│   ├── splash.png
│		│   ├── splashWine.png
│		│   ├── wine.jpg
│		│   └── wineSplash2.jpg
│		├── babel.config.js
│		├── mapped_idx2item.json
│		├── node_modules
│		├── package-lock.json
│		└── package.json
└── server # Backend 코드
    ├── crud_mongo.py
    ├── crud.py
    ├── database.py
    ├── data_generator.py
    ├── main.py
    ├── models.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── routers
    │   ├── home_router.py
    │   ├── mbti_router.py
    │   ├── user_router.py
    │   └── wine_router.py 
    ├── schema.py
    ├── user_data_generator.py
    └── utils.py
```

<br/>

## ✅ Appendix

**🤖 [시연 영상](https://youtu.be/n9-FZtWDqQE)** <br/>
**🧑‍💻 [발표 영상](https://youtu.be/RDmVaZT4Ols)** <br/>
**🔖 [Wrap-Up Report](https://www.notion.so/Wrap-Up-Report-548171142d1f42db9e1f183e392b8031?pvs=4)**

<br/>
