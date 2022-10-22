import gspread, pandas as pd
import qrcode
#import datetime
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe
#jsonファイルを使って認証情報を取得
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
c = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

#認証情報を使ってスプレッドシートの操作権を取得
gs = gspread.authorize(c)

#共有したスプレッドシートのキー（後述）を使ってシートの情報を取得
SPREADSHEET_KEY = '1QK-3Jt2wWMpXYGQtA07hKyTcH0VYZVleToFHdDtwMQg'
worksheet = gs.open_by_key(SPREADSHEET_KEY).worksheet('情報')
#ws1= gc.open_by_key(SPREADSHEET_KEY).worksheet('データ')
#print(worksheet.acell('A1').value)

workbook = gs.open_by_key(SPREADSHEET_KEY)
worksheet = workbook.worksheet('情報')
#client = gspread.authorize(c)
#sheet = client.open("codeQR").sheet1
#df_sum=sheet.get_all_records()
df=pd.DataFrame(worksheet.get_all_values())
df.head()
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)
sh = client.open_by_key(SPREADSHEET_KEY)
worksheet2 = sh.worksheet('シート1')
df.columns = df.iloc[0]
df = df.drop(df.index[[0]])
df['完了している数']=df['完了している数'].str.replace(",","")
#df.head()
a1 = worksheet.acell('J3').value
a=int(a1)
#print(int(a1)+1)
#df['完了している数']=df['完了している数'].astype(int)
#print(df.dtypes)
df_sum=df[['タイムスタンプ',"ご来場日",'お名前',"フリガナ",'ご住所1(都道府県)','ご住所2(市区都まで)','電話番号(ハイフンなしで入力)','Eメールアドレス','区分']].groupby('タイムスタンプ').sum()
df_num=df[['電話番号(ハイフンなしで入力)']]
#df_num=df_num.drop(df_num.index[[]])
#print(df_num.head())
#print(df_sum.head())
#print(df.head())
#workbook.add_worksheet(title='シート2',rows=1000,cols=15)
set_with_dataframe(workbook.worksheet('シート1'), df_sum, include_index=True)
l=len(df_num[['電話番号(ハイフンなしで入力)']])
#print(df_num[['電話番号(ハイフンなしで入力)']].shape)
print(l)
num=worksheet.get_all_values()
#num=df_num[['電話番号(ハイフンなしで入力)']]
print(type(num[5][6]))
for a in range(l+1):
    worksheet2.update_cell(a+1,10,'0')
    img = qrcode.make(num[a][6])
    file_name=num[a][6]+'.png'
    #print(type(img))
    #print(img.size)
    # <class 'qrcode.image.pil.PilImage'>
    # (290, 290)

    img.save(file_name)

worksheet.update_acell('J3', l)  	