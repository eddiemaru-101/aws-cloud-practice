#!/bin/bash

# 패키지 업데이트 및 nginx 설치
sudo apt update
sudo apt install nginx -y

# nginx 기본 설정에서 80포트를 8000으로 변경
sudo sed -i 's/listen 80 default_server;/listen 8000 default_server;/g' /etc/nginx/sites-available/default
sudo sed -i 's/listen \[::\]:80 default_server;/listen [::]:8000 default_server;/g' /etc/nginx/sites-available/default

# 홈페이지 내용 추가
echo "<H1>This is my WAS</H1><P>$HOSTNAME</P>" | sudo tee /var/www/html/index.html

# nginx 재시작
sudo systemctl restart nginx

# 로그 출력
echo "My nginx configuration has been completed"
