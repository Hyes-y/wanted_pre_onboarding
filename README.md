# wanted_pre_onboarding
원티드 프리온보딩 backend 과제 레포지토리



## 과제: 채용 공고 CRUD API 구현

| 구현 내용 | 구현 여부 |
| --- | --- |
| 채용 공고 등록 | ✅ |
| 채용 공고 수정 | ✅ |
| 채용 공고 삭제 | ✅ |
| 채용 공고 리스트 조회 | ✅ |
| 채용 공고 상세 내용 조회 | ✅ |
| (Optional) 채용 공고 검색 | ✅ |
| (Optional) 채용 공고 상세 내용 조회시 해당 기업의 다른 공고 목록도 포함 | ✅ |
| (Optional) 채용 공고 지원 | |

<br>

---

### 0. 예시데이터
```json
# 회사
[
  {
      "id": 1,
      "name": "원티드잇",
      "country": "KR",
      "location": "서울특별시 강남구"
  },
  {
      "id": 2,
      "name": "구글링코리아",
      "country": "US",
      "location": "Los Angeles"
  }
]
# 채용공고
{
    "id": 1,
    "uid": "6facc04c",
    "position": "백엔드 주니어 개발자",
    "reward": 600000,
    "skill": "Python, Django",
    "description": "원티드잇에서 백엔드 주니어 개발자를 채용합니다.",
    "company_name": "원티드잇",
    "company_country": "KR",
    "company_location": "서울특별시 강남구"
}
```

<br>

---

### 1. 채용 공고 등록
- 채용 포지션, 채용 보상금, 사용 기술, 채용 내용, 채용할 기업의 id 를 입력 받아 채용 공고 데이터 생성
- 요청 URL : `POST: {HOST}/api/posts/`

ex>

![image](https://user-images.githubusercontent.com/55697800/186227525-67417c96-883c-4e4e-8469-d8bb50ea26ee.png)

---

<br>

### 2. 채용 공고 수정
- 채용 포지션, 채용 보상금, 사용 기술, 채용 내용 중 수정할 부분을 입력받아 채용 공고 수정
- 회사는 수정할 수 없음 (요청이 올 경우 무시)
- DB 자체 ID, 외부 공개용 ID(UID)가 있으나 현재 URL 접근은 DB 자체 ID로만 가능(추후 수정 예정)
- 요청 URL : `PUT: {HOST}/api/posts/<int:pk>`

#### 2-1. 정상적인 수정 요청
- 채용 보상금 600000 => 700000 <br>

![image](https://user-images.githubusercontent.com/55697800/186228565-ab7e9c82-c842-4855-893a-70bc4f051012.png)

#### 2-2. 회사id 수정 요청
- 회사코드 1 => 2 <br>

![image](https://user-images.githubusercontent.com/55697800/186228847-967d711e-c648-4bae-ad89-3df735a9f104.png)

---

<br>

### 3. 채용 공고 삭제
- 요청 URL의 pk에 해당하는 공고를 삭제
- 요청 URL : `DELETE: {HOST}/api/posts/<int:pk>`
- 없는 공고 삭제시

![image](https://user-images.githubusercontent.com/55697800/186229169-e606f1cb-af2c-4c07-be58-a8823bd220a1.png)


---

<br>

### 4. 채용 공고 리스트 조회
- 전체 채용 공고 리스트 조회
- 요청 URL : `GET: {HOST}/api/posts/`

ex>

![image](https://user-images.githubusercontent.com/55697800/186229594-3b427273-5f8f-42c3-a08a-6563fbc9b0be.png)


---

<br>

### 5. 채용 공고 상세 내용 조회
- 요청 URL의 pk에 해당하는 채용 공고의 상세 내용 조회(채용 내용이 추가적으로 표시됨)
- 요청 URL : `GET: {HOST}/api/posts/<int:pk>`

ex>

![image](https://user-images.githubusercontent.com/55697800/186229960-157ec107-2de3-4325-b579-3446ced3e682.png)



<br>

---

### 6. (Optional) 채용 공고 상세 내용 조회시 해당 기업의 다른 공고 목록도 포함
- 채용 공고 상세 내용 조회시 기업의 다른 공고의 [id, uid] 를 함께 표시
- 요청 URL : `GET: {HOST}/api/posts/<int:pk>`

- 현재 3개의 채용 공고중 1개만 다른 기업인 상태

![image](https://user-images.githubusercontent.com/55697800/186366889-8cc8686b-e050-41f3-971b-a937f67d875e.png)

- 1번 공고와 4번 공고의 기업이 같음

![image](https://user-images.githubusercontent.com/55697800/186367031-60c57083-c7f3-4b0e-9c81-f75b34bec0bd.png)




<br>

---

<br>

### 7. (Optional) 채용 공고 검색
- 채용포지션('position'), 사용기술('skill'), 채용내용('description') 에 대해 해당 키워드가 있는지 검색한 결과를 조회
- 요청 URL : `GET: {HOST}/api/posts?search={params}`

![image](https://user-images.githubusercontent.com/55697800/186370273-0daa93ec-7d06-43a7-b4e0-1e251b0db287.png)

<br>

---

<br>
