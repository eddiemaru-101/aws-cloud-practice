### 실행환경
- 윈도우 cmd설치

### 명령어
- 전체 의미:
    - AWS CLI 설치 파일을 다운로드 → 자동 설치 → 임시 파일 삭제
```
curl "https://awscli.amazonaws.com/AWSCLIV2.msi" -o "AWSCLIV2.msi"
msiexec /i AWSCLIV2.msi /quiet
del AWSCLIV2.msi
```
### 첫 번째 명령어
`curl "https://awscli.amazonaws.com/AWSCLIV2.msi" -o "AWSCLIV2.msi"`

- 의미:
    - `curl` = 인터넷에서 파일 다운로드하는 명령어
    - `"https://awscli.amazonaws.com/AWSCLIV2.msi"` = AWS 공식 설치파일 주소
    - `-o "AWSCLIV2.msi"` = 다운로드한 파일을 "AWSCLIV2.msi"라는 이름으로 저장

결과: 현재 폴더에 설치파일이 다운로드됨
<br>


### 두 번째 명령어
`cmdmsiexec /i AWSCLIV2.msi /quiet`

- 의미:
    - msiexec = 윈도우 설치파일(.msi) 실행하는 명령어
    - /i AWSCLIV2.msi = "AWSCLIV2.msi" 파일을 설치(install)
    - /quiet = 조용히 설치 (팝업창 없이 자동으로)

결과: AWS CLI가 컴퓨터에 설치됨

<br>

### 세 번째 명령어
`cmddel AWSCLIV2.msi`

- 의미:
    - del = 파일 삭제 명령어
    - AWSCLIV2.msi = 다운로드한 설치파일

결과: 설치 완료 후 불필요한 파일 정리
