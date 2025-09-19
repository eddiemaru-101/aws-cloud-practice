## 1. 관리 범위

- 네트워크: VPC, 서브넷, 라우팅 테이블, IGW, NAT GW, 보안 그룹, NACL
- 컴퓨팅: EC2 (웹/앱 서버), Auto Scaling Group, Launch Template/Configuration
- 스토리지: EBS, S3 버킷, RDS (DB), EFS/NFS
- 로드밸런싱 & DNS: ALB/NLB, Route53 레코드
- IAM: 역할(Role), 정책(Policy)
- 옵션/보조 서비스: CloudWatch Alarm, SNS Topic, Parameter Store

->핵심은 “환경을 코드로 재현 가능하게” 만드는 것. 배포, 확장, 재생성할 때 수동 작업 최소화.
<br>

## 2. 기초용어
### (1)CloudFormation
- AWS 리소스를 코드로 관리하는 도구
- 사용목적
    - 수동 콘솔 작업 실수 방지
    - 재현성
    - 버전관리
<br>

### (2)스택
- CloudFormation(CFN)에서 리소스들의 집합
- CloudFormation 템플릿 = 설계도
- 형태
    - YAML이나 JSON 형식
<br>

## 3. 간단히 해볼 실습
- YAML 파일 작성 → 검증 → 배포 → 관리 순서로 진행
첫 단계에서 해볼 것들
1단계: 간단한 S3 버킷 하나 만들기
2단계: EC2 인스턴스 하나 만들기
3단계: VPC + 서브넷 만들기
4단계: 웹서버 + 데이터베이스 조합
