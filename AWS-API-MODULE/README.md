# AWS-API-MODULE
AWS-API-MODEL

***利用class使同一張圖的辨識不用每次都上傳，可以有效降低上傳次數***

1.函式的client參數記得要帶入含api token的變數:
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key

2.imgfilename參數為檔案路徑

需要注意一下回傳的值為何!大部分都為bool或list,再依你的需求做使用
