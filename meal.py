import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import formatdate
from email import encoders

# SMTPサーバー情報
smtp_id = 'iwairyoya@gmail.com'
smtp_ps = 'ryoya0122'
smtp_ad = 's3.xrea.com'
smtp_po = 587

# メール情報
ml_jp = 'iso-2022-jp'
ml_from = smtp_id
ml_to = 'webmaster@infomixer.net'
ml_title = "Python3でメール送信のテストやってます"
ml_text = \
'abcdefg\r\n' \
'0123456789\r\n' \
'ひらがら、カタカナ、漢字\r\n' \
'\r\n' \
'まるむしアンテナ\r\n' \
'https://antenna.infomixer.net\r\n'


#メッセージ　編集
message = MIMEMultipart() # 添付があるのでMultipart
message['Date'] = formatdate()
message['Subject'] = str(Header(ml_title,ml_jp))
message['From'] = ml_from
message['To'] = ml_to
message.attach(MIMEText(ml_text)) # 本文（テキスト）をattach

#画像を添付（Chart.jpg）
attachment = MIMEBase('image', 'jpeg;name="0901234324567.png"')
#file = open('chart.png','rb') # 画像なのでバイナリーモードで
#attachment.set_payload(file.read())
#file.close()
encoders.encode_base64(attachment) # base64でエンコード
attachment.add_header("Content-Dispositon","attachment",filename='Fig1.jpg') 
message.attach(attachment) # 画像をattach

# メール送信
srv = smtplib.SMTP(smtp_ad,smtp_po)
srv.ehlo()
srv.starttls()
srv.ehlo()
srv.login(smtp_id,smtp_ps)
srv.sendmail( ml_from, [ml_to], message.as_string(),)
srv.close()