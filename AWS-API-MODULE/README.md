# AWS-API-MODULE
AWS-API-MODEL

***利用class使同一張圖的辨識不用每次都上傳，可以有效降低上傳次數***

1.函式的client參數記得要帶入含api token的變數:
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key

2.imgfilename參數為檔案路徑

需要注意一下回傳的值為何!大部分都為bool或list,再依你的需求做使用


class:  1.DetectPPE 2.FaceDetails

  1.DetectPPE
  
    1.a. detect_hand_eqp
    1.b. detect_face_eqp
    1.c. detect_head_eqp 

  2.FaceDetails
  
    2.a emotion
    2.b count_face
    2.c eyes_open
    2.d age
    2.e smile
    2.f mouth_open
