import requests
import json

def postData(data):
    if(data is None):
        print("params is empty")
        return False
    
    payload = {
        "data": data
    }
    url = "https://script.google.com/macros/s/AKfycbxYZl3c24Uc_6FL06EsAHcf_PTFAiN3XHHaTU77exuWDhrGt5a6MWS0w6RHPyMf1r-e/exec"

    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if(response.status_code == 200 and response.text == "success"):
        print("post success!")
        return True
    print(response.text)
    return False

if __name__ == "__main__":
    # postしたいデータを渡す
    postData("hello yeah!!")