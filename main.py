import smtplib  # 이메일 전송 관련 라이브러리
from email.mime.text import MIMEText
import time
import threading

from regex import P
from Crwaler import Crwaler
from ui import UserSystem


class Server:
    def __init__(self, sender_id, sender_pw):
        self.crwaler = Crwaler()
        self.user_system = UserSystem()
        self.keywords = set()
        self.sender_id = sender_id
        self.sender_pw = sender_pw
        with open("UserList.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.split()
                for word in line[1:]:
                    self.keywords.add(word)

    def run_server(self):
        self.keywords = set()
        self.user_system = UserSystem()
        with open("UserList.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.split()
                for word in line[1:]:
                    self.keywords.add(word)
        for keyword in self.keywords:
            result = self.crwaler.crwal(keyword)
            if result:  # 키워드에 대한 매물이 있다면
                for key, value in self.user_system.user.items():
                    # 유저의 키워드 목록에 있다면,
                    if keyword in self.user_system.user[key]:
                        print(f"{key} - {keyword}에 대한 매물으로 이메일 전송합니다.")
                        self.email_send(key, result)
            else:
                print(f"{keyword}에 대한 매물이 없습니다.")
        threading.Timer(30, self.run_server).start()

    def email_send(self, email, result):
        content = ''
        for sale in result:
            content += "게시글 제목 : " + sale[0] + "\n" + "주소 : " + sale[1] + "\n"
        smtp_info = {
            "smtp_server": "smtp.naver.com",  # SMTP 서버 주소
            "smtp_user_id": self.sender_id,
            "smtp_user_pw": self.sender_pw,
            "smtp_port": 587  # SMTP 서버 포트
        }
        msg = MIMEText(content)
        msg['Subject'] = "특가 알림 입니다."  # 메일 제목
        msg['From'] = smtp_info['smtp_user_id'] + '@naver.com'  # 송신자
        msg['To'] = email

        smtp = smtplib.SMTP(smtp_info['smtp_server'], smtp_info['smtp_port'])
        smtp.ehlo
        smtp.starttls()  # TLS 보안 처리
        smtp.login(smtp_info['smtp_user_id'], smtp_info['smtp_user_pw'])  # 로그인
        print("sender 로그인")

        smtp.sendmail(msg['From'], msg['To'], msg.as_string())
        print("sender 전송")

        smtp.quit()


password = ''
with open("password.txt", "r") as f:
    password = f.read()

server = Server("asegh12", password)
server.run_server()
