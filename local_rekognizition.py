# 讀取本機檔案識別
# 檔名預設從1開始
# 辨識臉部
def rekog(client, count = 1):

    imgfilename = 'E:/Cloud/OneDrive/課/人工智慧/pic/'+str(count)+'.jpg'
    with open(imgfilename, 'rb') as imgfile:
        imgbytes = imgfile.read()
    rekresp = client.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])
    rekfd = rekresp['FaceDetails'][0]


# 讀取本機檔案識別
# 檔名預設從1開始
# 如要計數，需要建立dict用以計數
# 辨識情緒並計數
def emotions(client, count = 1):

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

# This function will return bolling, if eyes are close, it return 'True'
def eyes_close(client, count = 1):

    imgfilename = 'E:/Cloud/OneDrive/課/人工智慧/pic/' + str(count) +'.jpg'
    with open(imgfilename, 'rb') as imgfile:
        imgbytes = imgfile.read()
    rekresp = client.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])
    rekfd = rekresp['FaceDetails'][0] # 沒打[0]會跑錯
    eyes_close = rekfd['EyesOpen']['Value']
    return not eyes_close

# This founction will return the number of people
def count_face(client, count=1):  

    imgfilename = 'E:/Cloud/OneDrive/課/人工智慧/pic/' + str(count) + '.jpg'
    with open(imgfilename, 'rb') as imgfile:
        imgbytes = imgfile.read()
    rekresp = client.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])
    rekfd = rekresp['FaceDetails']
    return (len(rekfd))

# if have equipment on face, it will return true.
def detect_face_eqp(client, count=1):

    imgfilename = 'E:/Cloud/OneDrive/課/人工智慧/pic/'+str(count)+'.jpg'
    with open(imgfilename, 'rb') as imgfile:
        imgbytes = imgfile.read()
    rekresp = client.detect_protective_equipment(Image={'Bytes': imgbytes}, 
        SummarizationAttributes={'MinConfidence':80, 'RequiredEquipmentTypes':['FACE_COVER', 'HAND_COVER', 'HEAD_COVER']})
        
    '''
    rekresp['Persons'][0]['BodyParts'][indices]["EquipmentDetections"]

    different indices can check different position' equipment.
    indices = 0 : FACE
    indices = 1 :LEFT_HAND
    indices = 2 :RIGHT_HAND
    indices = 3 :HEAD

    '''
    dt_face_eqp = rekresp['Persons'][0]['BodyParts'][0]["EquipmentDetections"]
 
    return dt_face_eqp

# if have equipment on head, it will return true.
def detect_head_eqp(client, count=1):

        imgfilename = 'E:/Cloud/OneDrive/課/人工智慧/pic/'+str(count)+'.jpg'
    with open(imgfilename, 'rb') as imgfile:
        imgbytes = imgfile.read()
    rekresp = client.detect_protective_equipment(Image={'Bytes': imgbytes}, 
        SummarizationAttributes={'MinConfidence':80, 'RequiredEquipmentTypes':['FACE_COVER', 'HAND_COVER', 'HEAD_COVER']})

    dt_head_eqp = rekresp['Persons'][0]['BodyParts'][3]["EquipmentDetections"]
    
    return dt_head_eqp

