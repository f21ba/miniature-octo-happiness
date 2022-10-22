import cv2
import requests
import json
import gspread
import tkinter as tk
import datetime
from pygame import mixer
from oauth2client.service_account import ServiceAccountCredentials


# カメラデバイス取得
cap = cv2.VideoCapture(0)
# QRCodeDetectorを生成
detector = cv2.QRCodeDetector()
wdata=""
while True:
    # カメラから1フレーム読み取り
    ret, frame = cap.read()

    # QRコードを認識
    da = detector.detectAndDecode(frame)
    
    # 読み取れたらデコードした内容をprint
    if da[0] != "":
        wdata=da[0]
#        print(wdata)
        #if wdata!="":
         #   break
        scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
        client = gspread.authorize(creds)
        SPREADSHEET_KEY = '1QK-3Jt2wWMpXYGQtA07hKyTcH0VYZVleToFHdDtwMQg'
        sh = client.open_by_key(SPREADSHEET_KEY)
        worksheet1 = sh.sheet1
        worksheet2 = sh.worksheet('シート1')
        worksheet3 = sh.worksheet('シート2')

        list_of_lists = worksheet2.get_all_values()
        o=len(list_of_lists)
        #print(list_of_lists)
        #print(o)
        cnt=0
        root = tk.Tk()
        root.geometry('1000x1000')
        for i in list_of_lists:
                if wdata in i[6] :
                    #worksheet2.append_row(i, table_range='A1')
                    #print(i)
#                    r=len(i)
                    mixer.init()        #初期化
                    #mixer.music.load("魔王魂 効果音 システム35.mp3")
                    mixer.music.load("Doorbell-Melody01-1.mp3")
                    mixer.music.play(1)
                    label = tk.Label(root, text="タイムスタンプ  " + i[0],
                                        font=("",20), bg="#faaaff")
                    label.pack(pady=10)
                    label = tk.Label(root, text="ご来場日  " + i[1],
                                        font=("",20), bg="#faaaff")
                    label.pack(pady=10)
                    label = tk.Label(root, text="お名前  " + i[2],
                                        font=("",20), bg="#faaaff")
                    label.pack(pady=10)
                    label = tk.Label(root, text="フリガナ  " + i[3],
                                        font=("",20), bg="#faaaff")
                    label.pack(pady=10)
                    label = tk.Label(root, text="ご住所1(都道府県)  " + i[4],
                                        font=("",20), bg="#faaaff")
                    label.pack(pady=10)
                    label = tk.Label(root, text="ご住所2(市区都)  " + i[5],
                                        font=("",20), bg="#faaaff")
                    label.pack(pady=10)
                    label = tk.Label(root, text="電話番号  " + i[6],
                                        font=("",20), bg="#faaaff")
                    label.pack(pady=10)
                    label = tk.Label(root, text="Eメールアドレス  " + i[7],
                                        font=("",20), bg="#faaaff")
                    label.pack(pady=10)
                    label = tk.Label(root, text="区分  " + i[8],
                                        font=("",20), bg="#faaaff")
                    label.pack(pady=10)

                   # label = tk.Label(root, text="Hellow World!!",
                    #                font=("",20), bg="#aafaff")
                    #label.pack(pady=10)

                    root.mainloop()
                    dt_now = datetime.datetime.now()
                    dt =dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
                    #str(dt_now)
                    #worksheet2.update_cell(cnt+1,r+1,dt)
                    #a1 = worksheet3.acell('L1').value
                    
                   # worksheet3.update_cell(int(a1)+2,1,dt)
                    #worksheet3.update_cell(int(a1)+2,2,i[2])
                    #worksheet3.update_cell(int(a1)+2,3,i[6])
                    #worksheet3.update_acell('L1', int(a1)+1)
                    if i[9] == '0':
                           worksheet2.update_cell(int(cnt)+1,11,dt)
                           worksheet2.update_cell(int(cnt)+1,10,'1')
                    elif i[9]=='1':
                        worksheet2.update_cell(int(cnt)+1,12,dt)
                        worksheet2.update_cell(int(cnt)+1,10,'0')
                    break
                else:
                    #print(cnt)
                    cnt+=1
                    pass
        if int(cnt)==int(o):

            label = tk.Label(root, text="データがありません",
                            font=("",20), bg="#aafaff")
            label.pack(pady=10)
            root.mainloop()
            #print(10)
       # break
        #break
    # ウィンドウ表示
    cv2.imshow('frame', frame)

    # Qキー押すと終了
    if cv2.waitKey(1) & 0xFF == ord('q'):#data[0]==""
        cap.release()
        cv2.destroyAllWindows()
        break

#print(3)
# 終了処理
""""
def postData(data):
    if(data is None):
        print("params is empty")
        return False
    
    payload = {
        "data": data
    }
    url ="https://script.google.com/macros/library/d/1-OOZ1J9ZhNFjp2Aiptq1V-vXOxtC1zwByo-FlGYBFYmTRw36uvYQP8QH/2" 
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if(response.status_code == 200 and response.text == "success"):
        print("post success!")
        return True
    print(response.text)
    return False 
"""

#if __name__ == "__main__":
    # postしたいデータを渡す
 #   postData(wdata)
"""
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)
SPREADSHEET_KEY = '1QK-3Jt2wWMpXYGQtA07hKyTcH0VYZVleToFHdDtwMQg'
sh = client.open_by_key(SPREADSHEET_KEY)
worksheet1 = sh.sheet1
worksheet2 = sh.worksheet('シート1')

list_of_lists = worksheet2.get_all_values()
o=len(list_of_lists)
print(list_of_lists)
print(o)
cnt=0
root = tk.Tk()
root.geometry('1000x1000')
for i in list_of_lists:
        if wdata in i[6] :
            #worksheet2.append_row(i, table_range='A1')
            #print(i)
            

            label = tk.Label(root, text="タイムスタンプ  " + i[0],
                                font=("",20), bg="#faaaff")
            label.pack(pady=10)
            label = tk.Label(root, text="ご来場日  " + i[1],
                                font=("",20), bg="#faaaff")
            label.pack(pady=10)
            label = tk.Label(root, text="お名前  " + i[2],
                                font=("",20), bg="#faaaff")
            label.pack(pady=10)
            label = tk.Label(root, text="フリガナ  " + i[3],
                                font=("",20), bg="#faaaff")
            label.pack(pady=10)
            label = tk.Label(root, text="ご住所1(都道府県)  " + i[4],
                                font=("",20), bg="#faaaff")
            label.pack(pady=10)
            label = tk.Label(root, text="ご住所2(市区都まで)  " + i[5],
                                font=("",20), bg="#faaaff")
            label.pack(pady=10)
            label = tk.Label(root, text="電話番号(ハイフンなしで入力)  " + i[6],
                                font=("",20), bg="#faaaff")
            label.pack(pady=10)
            label = tk.Label(root, text="Eメールアドレス  " + i[7],
                                font=("",20), bg="#faaaff")
            label.pack(pady=10)
            label = tk.Label(root, text="区分  " + i[8],
                                font=("",20), bg="#faaaff")
            label.pack(pady=10)

            label = tk.Label(root, text="Hellow World!!",
                            font=("",20), bg="#aafaff")
            label.pack(pady=10)

            root.mainloop()
            break
        else:
            print(cnt)
            cnt+=1
            pass
if int(cnt)==int(o):

    label = tk.Label(root, text="データがありません",
                    font=("",20), bg="#aafaff")
    label.pack(pady=10)
    root.mainloop()
    #print(10)
    """