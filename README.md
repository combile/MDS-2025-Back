# MDS-2025-Back
> HBNU SW 2025 다학제 캡스톤 백엔드 작업 공간
#
## 가상환경 생성
```
python -m venv venv
```

## 가상환경 구동
```
source venv/bin/activate
```


> 서버 가동 (app 디렉토리에서 실행)
```
uvicorn main:app --realod
```
> 의존성 명세 파일 내보내기
```
pip freeze > requirements.txt
```

> 의존성 패키지 설치

```
python -r install requirements.txt
```

## Commit Convention

`Feat(component, ui) : 버튼 컴포넌트 ui 구현`

### Type

|type|	description|
|--|--|
|Feat|	새로운 화면, 기능, 이미지 등 추가 작업|
|Fix|	버그, 기능 등 오류 수정|
|Style|	여백(padding), 색상(Color) 등 UI 디테일 변경|
|Chore|	설정, 파일정리, 리소스 관리(이미지 삭제, 파일 이름 변경 등) 기능 외 작업|
|Docs|	문서(README) 작성 및 주석 추가/삭제/수정|
|Refactor|	내부 코드 구조 개선(변수명 정리, 코드 분리, 모듈화 등)|
|Perf|	성능 최적화(루프 최적화, 중복제거, 연산량 감소 등)|

