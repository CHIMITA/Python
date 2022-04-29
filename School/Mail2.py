import smtplib
from email.mime.text import MIMEText

rmail = ['sangilmhs@gmail.com', 'smile0375-@naver.com']
smail = "chimita16@naver.com"

password = "" #본인 비밀번호 입력

s = smtplib.SMTP('smtp.naver.com', 587)

r = s.starttls()

s.login(smail, password)

msg = MIMEText('안녕하세요')
msg['subject'] = '제목 : 파이썬으로 메일 보내기'
msg['From'] = smail

for i in rmail:
    msg['To'] = rmail[1] #list
    response = s.sendmail(smail, rmail[1], msg.as_string())
    if not response:
        print("response:", response)
        print("메일 보내기 성공")
    else:
        print("메일 보내기 실패", response)

s.quit()