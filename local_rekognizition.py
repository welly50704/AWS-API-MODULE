# 讀取本機檔案識別
# 檔名預設從1開始
def rekog(count = 1):

    imgfilename = 'E:/Cloud/OneDrive/課/人工智慧/pic/'+str(count)+'.jpg'
    with open(imgfilename, 'rb') as imgfile:
        imgbytes = imgfile.read()
    rekresp = client.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])
    rekfd = rekresp['FaceDetails'][0]


# 讀取本機檔案識別
# 檔名預設從1開始
# 需要建立dict用以計數
def emotions(imgfilename = imgfilename, count = 1):

    imgfilename = 'E:/Cloud/OneDrive/課/人工智慧/pic/'+str(count)+'.jpg'
    with open(imgfilename, 'rb') as imgfile:
        imgbytes = imgfile.read()
    rekresp = client.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])
    rekfd = rekresp['FaceDetails'][0]
    
    for i in range(3):
        print(rekfd['Emotions'][i])
    emotion = rekfd['Emotions'][0]['Type']
    print(emotion)
    print(f'根據資料分析，照片中的人物應該屬於"{emotion}"心情狀態')
    # 計算情緒數量
    emotion_dict[emotion] += 1                                                  
    print(emotion_dict)
    # 取最多單位的情緒
    most_emotion = max(emotion_dict, key = emotion_dict.get)                    
    print(f'目前最多的情緒是{most_emotion}')
    return most_emotion

def eyes_close(count = 1):
    imgfilename = 'E:/Cloud/OneDrive/課/人工智慧/pic/' + str(count) +'.jpg'
    with open(imgfilename, 'rb') as imgfile:
        imgbytes = imgfile.read()
    rekresp = client.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])
    rekfd = rekresp['FaceDetails'][0] # 沒打[0]會跑錯
    eyes_close = rekfd['EyesOpen']['Value']
    return not eyes_close