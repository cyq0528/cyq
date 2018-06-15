import smtpd,unittest

class sendEmail(unittest.TestCase):
    def setUp(self):
        smtpserver='smtp.163.com'
        pass
    def tearDown(self):
        pass
    def sendEmailDef(self,userName,password,sender,receiver):
        self.userName=userName
        self.password=password
        self.sender=sender
        self.receiver=receiver
        pass