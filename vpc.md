1단계: 개발환경 준비

    VSCode에 AWS 확장 설치 및 설정
    AWS CLI 설정 (자격증명)
    CloudFormation 템플릿 파일 생성

2단계: VPC 기본 네트워크 구성

    VPC 생성 (전체 네트워크 영역)
    Internet Gateway 생성 (인터넷 연결용)
    VPC-IGW 연결

3단계: 서브넷 설계 및 생성

    Public Subnet (Web Server용)
    Private Subnet 1 (WAS용)
    Private Subnet 2 (DB용)
    각각 다른 AZ에 배치 (고가용성)

4단계: 라우팅 설정

    Public Route Table + IGW 연결
    Private Route Table (내부 통신용)
    서브넷-라우팅테이블 연결

5단계: 보안 그룹 생성

    Web Server 보안그룹 (80,443,22 포트)
    WAS 보안그룹 (8080포트, Web에서만 접근)
    DB 보안그룹 (3306포트, WAS에서만 접근)

6단계: EC2 인스턴스 배포

    각 서브넷에 EC2 배치
    보안그룹 적용
    키페어 설정
