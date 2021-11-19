# 원티드x위코드 백엔드 프리온보딩 과제5 :: deer(디어코퍼레이션)

# 배포 주소 : 13.209.21.70

# 1. [TEAM] WithCODE

#### Members

| 이름   | github                         |
| ------ | ------------------------------ |
| 김민호 | https://github.com/maxkmh712   |
| 김주형 | https://github.com/BnDC        |
| 박치훈 | https://github.com/chihunmanse |
| 박현우 | https://github.com/Pagnim      |
| 이기용 | https://github.com/leeky940926 |
| 이정아 | https://github.com/wjddk97     |

------

# 2. 과제

#### [필수 포함 사항]

- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

#### [주요 평가 사항]

- 주어진 정보를 기술적으로 설계하고 구현할 수 있는 역량
- 확장성을 고려한 시스템 설계 및 구현

#### [과제 안내]

디어는 사용자의 요금을 계산하기 위해 다양한 상황을 고려합니다. 

- 우선 지역별로 다양한 요금제를 적용하고 있습니다. 예를 들어 건대에서 이용하는 유저는 기본요금 790원에 분당요금 150원, 여수에서 이용하는 유저는 기본요금 300원에 분당요금 70원으로 적용됩니다.
- 할인 조건도 있습니다. 사용자가 파킹존에서 반납하는 경우 요금의 30%를 할인해주며, 사용자가 마지막 이용으로부터 30분 이내에 다시 이용하면 기본요금을 면제해줍니다.
- 벌금 조건도 있습니다. 사용자가 지역 바깥에 반납한 경우 얼마나 멀리 떨어져있는지 거리에 비례하는 벌금을 부과하며, 반납 금지로 지정된 구역에 반납하면 6,000원의 벌금을 요금에 추과로 부과합니다.
- 예외도 있는데, 킥보드가 고장나서 정상적인 이용을 못하는 경우의 유저들을 배려하여 1분 이내의 이용에는 요금을 청구하지 않고 있습니다.

최근에 다양한 할인과 벌금을 사용하여 지자체와 협력하는 경우가 점점 많아지고 있어 요금제에 새로운 할인/벌금 조건을 추가하는 일을 쉽게 만드려고 합니다. 어떻게 하면 앞으로 발생할 수 있는 다양한 할인과 벌금 조건을 기존의 요금제에 쉽게 추가할 수 있는 소프트웨어를 만들 수 있을까요? 

우선은 사용자의 이용에 관한 정보를 알려주면 현재의 요금 정책에 따라 요금을 계산해주는 API를 만들어주세요. 그 다음은, 기능을 유지한 채로 새로운 할인이나 벌금 조건이 쉽게 추가될 수 있게 코드를 개선하여 최종 코드를 만들어주세요.

**다음과 같은 정보들이 도움이 될 것 같아요.**

---

- 요금제가 사용자 입장에서 합리적이고 이해가 쉬운 요금제라면 좋을 것 같아요.
- 앞으로도 할인과 벌금 조건은 새로운 조건이 굉장히 많이 추가되거나 변경될 것 같아요.
- 가장 최근의 할인/벌금 조건의 변경은 '특정 킥보드는 파킹존에 반납하면 무조건 무료' 였습니다.

**이용에는 다음과 같은 정보들이 있습니다.**

---

```
use_deer_name (사용자가 이용한 킥보드의 이름)
use_end_lat, use_end_lng (사용자가 이용을 종료할 때 위도 경도)
use_start_at, use_end_at (사용자가 이용을 시작하고 종료한 시간)
```

**데이터베이스에는 킥보드에 대해 다음과 같은 정보들이 있습니다.**

---

```
deer_name (킥보드의 이름으로 고유한 값)
deer_area_id (킥보드가 현재 위치한 지역의 아이디)
```

**데이터베이스에는 지역에 대해 다음과 같은 정보들이 있습니다.**

---

```
area_id (지역 아이디로 고유한 값)
area_bounday (지역을 표시하는 MySQL spatial data로 POLYGON)
area_center (지역의 중심점)
area_coords (지역의 경계를 표시하는 위도, 경도로 이루어진 점의 리스트)
```

**데이터베이스에는 파킹존에 대해 다음과 같은 정보들이 있습니다.**

---

```
parkingzone_id (파킹존 아이디로 고유한 값)
parkingzone_center_lat, parkingzone_center_lng (파킹존 중심 위도, 경도)
parkingzone_radius (파킹존의 반지름)
```

**데이터베이스에는 반납금지구역에 대해 다음과 같은 정보들이 있습니다.**

---

```
forbidden_area_id (반납금지구역 아이디로 고유한 값)
forbidden_area_boundary (반납금지구역을 표시하는 MySQL spatial data로 POLYGON)
forbidden_area_coords (반납금지구역의 경계를 표시하는 위도, 경도로 이루어진 점의 리스트)
```

------

# 3. Skill & Tools

- **Skill :** [![img](https://camo.githubusercontent.com/0f3eb5f3e4c61d94657f16605ea420a0216673dfb085d100c458ed15be0599d2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/0f3eb5f3e4c61d94657f16605ea420a0216673dfb085d100c458ed15be0599d2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/c4c1014e1f168ff271282b67ec9059c3cfc16b2a5cba6e0c7c98c3530f47f45c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d446a616e676f266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/c4c1014e1f168ff271282b67ec9059c3cfc16b2a5cba6e0c7c98c3530f47f45c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d446a616e676f266c6f676f436f6c6f723d7768697465) 
- **Depoly :** [![img](https://camo.githubusercontent.com/9ad32f291fa1163a77cd2e919f8378b38bf66fd9de517178bf890e521178f341/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f415753204543322d3233324633453f7374796c653d666f722d7468652d6261646765266c6f676f3d416d617a6f6e20415753266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/9ad32f291fa1163a77cd2e919f8378b38bf66fd9de517178bf890e521178f341/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f415753204543322d3233324633453f7374796c653d666f722d7468652d6261646765266c6f676f3d416d617a6f6e20415753266c6f676f436f6c6f723d7768697465)
- **ETC :** [![img](https://camo.githubusercontent.com/fdb91eb7d32ba58701c8e564694cbe60e706378baefa180dbb96e2c1cfb9ec0f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d476974266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/fdb91eb7d32ba58701c8e564694cbe60e706378baefa180dbb96e2c1cfb9ec0f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d476974266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/23a917c56e310800a66c58a03447dd42c0dea2abff415ef9719e3e837c1cff82/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666f722d7468652d6261646765266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/23a917c56e310800a66c58a03447dd42c0dea2abff415ef9719e3e837c1cff82/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666f722d7468652d6261646765266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/879423585ed087f3c973857c43ba7e7d84f52c993d2c937055726339fbf921d9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d506f73746d616e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/879423585ed087f3c973857c43ba7e7d84f52c993d2c937055726339fbf921d9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d506f73746d616e266c6f676f436f6c6f723d7768697465)

------

# 4. 모델링


이



------

# 5. Postman API 테스트

### API 테스트 : https://www.postman.com/cloudy-robot-203980/workspace/humanscape

### 기본 주소는 배포주소로 되어 있으며, 콜렉션 fork 후 테스트 부탁드립니다.

### API 명세서 : https://documenter.getpostman.com/view/17666851/UVC9hkgs

------

# 6. 구현 사항 상세 설명
## 1. GET /researches/{int:research_id} (특정 임상과제 조회)
- [성공] path parameter로 임상과제 id값을 받아와서 해당 임상과제 정보를 조회합니다. ex) /researches/

![image](https://user-images.githubusercontent.com/79758688/141976381-1f22e6b4-a8c7-4696-b775-29019912c4d3.png)

- [실패] 만약 존재하지 않는 임상과제 id값을 입력할 경우 404 code를 반환해줍니다.

![image](https://user-images.githubusercontent.com/79758688/141976696-499569b9-922f-443b-aa08-bbc4cfa8e049.png)

## 2. GET /researches (전체 임상과제 리스트 조회)
- [성공] path parameter를 입력하지 않을 경우 전체 임상과제 리스트를 조회합니다. pagination을 20으로 주어 데이터를 20개씩 조회하도록 하였습니다. 

![image](https://user-images.githubusercontent.com/79758688/141977141-76fe2717-9017-4ae5-9396-74763281f65e.png)

## 3. GET /researches?search=당뇨 (과제명으로 검색)
- [성공] 임상과제 검색 API를 구현했습니다. 먼저 search라는 변수를 데이터로 받아서 검색 기능을 추가했습니다. 검색 필터는 임의로 '과제명'과 '기관명'으로 설정하였습니다.  '당뇨'라는 필터로 검색 시 '과제명'에 '당뇨'가 포함되는 데이터들이 조회됩니다.

![image](https://user-images.githubusercontent.com/79758688/141977978-cde01a72-4558-4cb3-a36e-f1b82add3fd6.png)

## 4. GET /researches?search=서울성모 (기관명으로 검색)
- '서울성모' 라는 필터로 검색시 '연구기관'에 '서울성모'가 포함된 데이터들이 조회됩니다. 

![image](https://user-images.githubusercontent.com/79758688/141978271-071bad28-b300-4bcd-ad6b-0e8f2dc5aea1.png)

## 5. Batch task

![image](https://user-images.githubusercontent.com/75020336/142137760-f1dae3b4-89f1-4f46-ab02-fb81ab3dc2ef.png)


- 계속해서 업데이트가 필요한 코드는 django에서 지원해주는 django-crontab을 통하여 batch task를 구현하였습니다.

```
CRONJOBS = [
    ('* */4 * * *', 'researches.cron.batch_task', '>> ~/humanscape/cron.log 2>&1'),
]
```
- 4시간 마다 researches app에 있는 cron.py파일의 batch_task함수가 실행되고 에러 로그는 cron.log에 기록되도록 하였습니다.

## 5-1. 기능
- 외부 api를 가져오면 기존에 있는 데이터베이스의 값과 비교하여 새로 들어온 연구는 추가해주었습니다.
- 변경사항이 없는 연구는 값이 들어와도 변하지 않고 변경사항이 있는 정보는 데이터베이스에서 업데이트 해주고 update_at시간을 주었습니다.
- 
------

# 7. UnitTest 결과

<img width="779" alt="스크린샷 2021-11-16 오후 6 39 48" src="https://user-images.githubusercontent.com/79758688/141960630-899f8ebb-d097-4380-9812-c1db2983e230.png">


# 8 . Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 휴먼스케이프(humanscape)에서 출제한 과제를 기반으로 만들었습니다. 감사합니다.

