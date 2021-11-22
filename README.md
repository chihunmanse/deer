# 원티드x위코드 백엔드 프리온보딩 과제6 :: deer(디어코퍼레이션)

# 배포 주소 : 

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

------

- 요금제가 사용자 입장에서 합리적이고 이해가 쉬운 요금제라면 좋을 것 같아요.
- 앞으로도 할인과 벌금 조건은 새로운 조건이 굉장히 많이 추가되거나 변경될 것 같아요.
- 가장 최근의 할인/벌금 조건의 변경은 '특정 킥보드는 파킹존에 반납하면 무조건 무료' 였습니다.

**이용에는 다음과 같은 정보들이 있습니다.**

------

```
use_deer_name (사용자가 이용한 킥보드의 이름)
use_end_lat, use_end_lng (사용자가 이용을 종료할 때 위도 경도)
use_start_at, use_end_at (사용자가 이용을 시작하고 종료한 시간)
```

**데이터베이스에는 킥보드에 대해 다음과 같은 정보들이 있습니다.**

------

```
deer_name (킥보드의 이름으로 고유한 값)
deer_area_id (킥보드가 현재 위치한 지역의 아이디)
```

**데이터베이스에는 지역에 대해 다음과 같은 정보들이 있습니다.**

------

```
area_id (지역 아이디로 고유한 값)
area_bounday (지역을 표시하는 MySQL spatial data로 POLYGON)
area_center (지역의 중심점)
area_coords (지역의 경계를 표시하는 위도, 경도로 이루어진 점의 리스트)
```

**데이터베이스에는 파킹존에 대해 다음과 같은 정보들이 있습니다.**

------

```
parkingzone_id (파킹존 아이디로 고유한 값)
parkingzone_center_lat, parkingzone_center_lng (파킹존 중심 위도, 경도)
parkingzone_radius (파킹존의 반지름)
```

**데이터베이스에는 반납금지구역에 대해 다음과 같은 정보들이 있습니다.**

------

```
forbidden_area_id (반납금지구역 아이디로 고유한 값)
forbidden_area_boundary (반납금지구역을 표시하는 MySQL spatial data로 POLYGON)
forbidden_area_coords (반납금지구역의 경계를 표시하는 위도, 경도로 이루어진 점의 리스트)
```

------



## 3. Skill & Tools

> **Skill :** <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/JWT-232F3E?style=for-the-badge&logo=JWT&logoColor=white"/>&nbsp;<br>
> **Depoly :** <img src="https://img.shields.io/badge/AWS EC2-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/AWS RDS-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white"/> <br>
> **ETC :**  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

------



# 4. 모델링

![](https://user-images.githubusercontent.com/61782539/142759916-09b5194c-437d-4921-b04b-a6b6b6d792eb.png)

------



# 5. Postman API 테스트

### API 테스트 : https://www.postman.com/cloudy-resonance-766003/workspace/deer

### API 명세서 : https://documenter.getpostman.com/view/17663987/UVJWqfVJ

### 기본 주소는 배포주소로 되어 있으며, 콜렉션 fork 후 테스트 부탁드립니다.

### Data Reference

유저 정보

1. phone_number = '01011111111' / password = '1234' (이용내역 존재해서 첫이용 쿠폰 적용되지 않음)  

   토큰 = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MX0.8SfW-rdiggsjQ91oOb9hS-7tub81_UL9oHv-qgcHE5U

2. phone_number = '01022222222' / password = '1234'

   토큰 = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Mn0.eVdLVy6A6u7U2mQui17ZcVDK5rovEcvcFpcw-fBNi3M



군자동 요금 : 기본 요금 1000원 / 분당 요금 200원

군자동에 속한 킥보드 이름 정보 : '썬더볼트', '씽씽이', '붕붕이 (이벤트 중인 킥보드)',  

군자동 지역 반납 위도 경도 : 37.556251, 127.074597

군자동 파킹존 반납 위도 경도 : 37.555379, 127.075750 / 37.550365, 127.071446

군자동 반납금지구역 위도 경도 : 37.551319, 127.074239

군자동 지역 외 위도 경도 : 37.544353, 127.068393



온천동 요금 : 기본 요금 500원 / 분당 요금 100원

온천동에 속한 킥보드 이름 정보 : "방방이", '슝슝이', '독수리'

온천동 지역 반납 위도 경도 : 35.21324123862374, 129.0677494260041

온천동 파킹존 반납 위도 경도 : 35.205903, 129.068146 / 35.207491, 129.070197

온천동 반납금지구역 위도 경도 : 35.212870, 129.061417

온천동 지역 외 위도 경도 : 35.198830, 129.059440


------



# 6. 구현 사항 상세 설명

### 1. POST /users/signin (로그인)

#### **body Key list**

**phone_number**

**password**

휴대폰 번호와 비밀번호를 입력받아 로그인 성공시 jwt 토큰값을 반환합니다.

휴대폰 번호나 비밀번호가 올바르지 않을시 401 code를 반환합니다.

body의 key값이 올바르지 않을시 400 code를 반환합니다.



### 2. POST /services/settlement (이용요금 계산 / 이용내역 저장)

#### **body Key list**

 **kickboard_name** (킥보드 이름)

 **end_lat** (반납 위도)

 **end_lng** (반납 경도)   

 **start_at** (이용시작 시간)    

 **end_at**  (이용종료 시간)    

이용한 킥보드가 속한 지역의 기본요금, 분당요금을 기반으로 사용요금을 계산합니다.

반납 위치와 시간에 따라 여러 조건의 패널티 및 할인을 적용하여 최종적인 요금을 계산합니다.

이용내역을 생성하고 최종요금값과 201 code를 반환합니다.

header에 로그인토큰이 없을 경우 401 code를 반환합니다.

start_at 과 end_at 값이 적절하지 않을시 400 code를 반환합니다.

end_lat 과 end_lng 값이 적절하지 않을시 400 code를 반환합니다.

잘못된 킥보드 이름값이 들어왔을 때 400 code를 반환합니다.

body의 key값이 올바르지 않을시 400 code를 반환합니다.



# 7. 할인 및 벌금 조건 구현과정

![](https://user-images.githubusercontent.com/61782539/142759410-9c8699d3-58f5-4132-b14f-a732ab1c0791.jpg)

![](https://user-images.githubusercontent.com/61782539/142759435-128d05d8-5e73-4269-9628-e8407e6c6ba3.jpg)

**서울시 광진구 군자동과 부산시 동래구 온천동 두 지역을 서비스 지역으로 설정하고 POLYGON을 생성했습니다.**

![](https://user-images.githubusercontent.com/61782539/142759800-1d442310-5438-49d3-8773-962f18d99c2b.png)

GDAL 라이브러리를 사용하여 django orm을 통해 Polygon 및 Point 데이터타입을 다룰 수 있었습니다.

![](https://user-images.githubusercontent.com/61782539/142760381-032ab5a2-9a85-49af-9d4f-02579e50631d.png)

처음엔 View 안에서 할인 및 벌금 조건들의 로직을 순서대로 나열하는 식으로 코드를 작성하였습니다. 기능에는 문제가 없었지만, 적용중인 할인과 벌금 조건을 추가,수정하거나 삭제한다고 했을 때 매우 비효율적인 구성으로 느껴졌습니다.

수정해야하는 조건의 로직을 찾기도 힘들었고, 조건을 추가하거나 삭제할 때 잘못하면 전체 로직에 영향을 주기도 쉬웠습니다. 또 어떤 조건은 정지됐다가 후에 다시 진행될 수도 있기 때문에 조건을 재사용하는 측면에서도 효율이 떨어졌습니다.



저희는 할인 및 벌금 정책들을 각각의 class로 만들어 개별적인 단위로 구성될 수 있도록 개선을 시도하였습니다.

조건은 크게 벌금과 할인으로 나누고 할인 안에서는 요율로 적용되는 할인과 쿠폰 할인으로 나누어 관리하기로 했습니다.

#### **penalty.py**

![](https://user-images.githubusercontent.com/61782539/142761041-d7fffe92-e1c1-4ec3-aadc-40ea4437f4e5.png)

penalty.py 파일에는 벌금 정책들이 각각의 class로 작성되어 관리됩니다.

#### **discount.py**

![](https://user-images.githubusercontent.com/61782539/142761130-36e5084d-7978-47d1-87a0-8da4270d6776.png)

discount.py 파일에는 요율로 적용되는 할인 정책들이 각각의 class로 작성되어 관리됩니다.

#### **coupon.py**

![](https://user-images.githubusercontent.com/61782539/142761226-c77fd07d-121c-4f75-868b-0e36482e3c9d.png)

coupon.py 파일에는 쿠폰 할인 정책들이 각각의 class로 작성되어 관리됩니다.

#### **calculator.py**

![](https://user-images.githubusercontent.com/61782539/142761343-8b762e75-f6da-4cb3-830b-34ae2aff7557.png)

calculator.py 파일에는 적용된 벌금, 할인, 쿠폰 조건들의 총 금액을 계산해주는 class들을 작성하였습니다.

#### **views.py**

![](https://user-images.githubusercontent.com/61782539/142761649-e21bf2bd-6d95-4f0f-a5be-007778f89965.png)

View에서는 요금을 계산할 때 적용할 조건들을 지정해주고 calcutaor.py에 있는 class들을 활용해 최종적인 할인율과 벌금, 쿠폰액을 구하여 최종 이용요금을 구합니다.



이렇게 구성을 변경한 후에 실제로 새로운 할인, 쿠폰 조건들을 추가해보면서 전보다 요금정책을 관리하는 효율성이 크게 개선되었음을 느낄 수 있었습니다.

만약 반납금지구역에 반납했을 때 패널티가 6000원에서 7000원으로 변경되었다고 한다면 penalty.py에서 해당 class의 속성값만 변경해주면 되기 때문에 기존처럼 전체 로직에서 바꿔야하는 조건이 무엇인지 찾을 필요가 없고 수정할 때 다른 로직에 영향을 줄 위험도 훨씬 줄었습니다.

또 주말 21시 이후 10% 할인 정책을 잠시 중지한다고 하면 View의 discounts 리스트에서 해당 class를 빼주었다가 다시 정책을 적용한다고 했을 때 추가해주면 되기 때문에 재사용할 수 있는 효율도 크게 개선되었습니다.

------

# 8. UnitTest 결과

![](https://user-images.githubusercontent.com/61782539/142762530-bc0e90e6-b409-4a5a-b049-f401498ee083.png)

# 9. Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 디어코퍼레이션에서 출제한 과제를 기반으로 만들었습니다. 감사합니다.
