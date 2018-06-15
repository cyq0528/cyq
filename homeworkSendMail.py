from email.mime.text import MIMEText
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart

def sendmail():
    server = 'smtp.163.com'  # 邮件服务器
    sender = 'cyq19920528@163.com'  # 发送人
    password = 'cyq12345'  # 发送人邮件密码
    receiver = '15902127953@163.com'  # 收件人邮箱

    data=MIMEMultipart()
    data.attach(MIMEText('附件为郑州大学用例执行报告，请查阅，谢谢！','plain','utf-8'))
    data['From']=Header(sender,'utf-8')
    data['To']=receiver
    data['Subject']=Header('陈以权的测试报告','utf-8')

    att=MIMEText(open(r'C:/Users/Administrator/Desktop/2018-06-12-16-12repot.html',encoding='utf-8').read())
    att['Content-Disposition']='attachment;filename="report.html"'
    data.attach(att)

    server=smtplib.SMTP(server,25)
    server.login(sender, password)
    server.set_debuglevel(1)
    server.sendmail(sender, receiver, data.as_string())
    server.quit()
sendmail()




