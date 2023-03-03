# STOCKTRACKER 
개인의 자산 변동 추이를 일자별로 추적하는 앱

## Models
---
1. User

2. Account
|property|description|
|---|---|
|id||
|created_at|등록 일시|
|name|구좌 이름|
|name_bank|증권사 이름|
|balance|잔고|

3. AccountHistory
|property|description|
|---|---|
|id||
|account_id||
|created_at|생성일시|
|from_account|출금 구좌|
|to_account|입금 구좌|
|amount|금액|