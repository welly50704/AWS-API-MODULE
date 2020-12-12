##此module為讀取本機檔案版，因此輸入的檔案位置需要自行調整 3Q

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

    different indices can check different position' equipment. ###在全部部位都有被偵測到時才成立，因此會做大改########
    indices = 0 : FACE
    indices = 1 :LEFT_HAND
    indices = 2 :RIGHT_HANDx
    indices = 3 :HEAD

    '''
    dt_face_eqp = rekresp['Persons'][0]['BodyParts'][0]["EquipmentDetections"]
 
    return dt_face_eqp

# if have equipment on head, it will return true.
# if someone doesn't have equipment on head, it will print his Id and return false.
def detect_head_eqp(client, count=1):
    no_eqp_list = []
    imgfilename = 'E:/Cloud/OneDrive/課/人工智慧/pic/'+str(count)+'.jpg'
    with open(imgfilename, 'rb') as imgfile:
        imgbytes = imgfile.read()
    rekresp = client.detect_protective_equipment(Image={'Bytes': imgbytes}, 
        SummarizationAttributes={'MinConfidence':80, 'RequiredEquipmentTypes':['FACE_COVER', 'HAND_COVER', 'HEAD_COVER']})

    persons = rekresp['Persons']
    for person in persons:
        Id = person['Id']
        print(Id)

        body_parts = person['BodyParts']

        if len(body_parts) == 0:
            print('\t\tNo body_part detected')
            
        else:
            for body_part in body_parts:
                # check have detected head.
                if body_part['Name'] == 'HEAD':  
                    ppe_items = body_part['EquipmentDetections']
                    
                    if not ppe_items:
                        
                        no_eqp_list.append(Id)
                        print(f'{Id}, not have head_epq')
                        

                    for ppe_item in ppe_items:
                        head_eqp = ppe_item['CoversBodyPart']['Value']
                        
                        if head_eqp == 'False':
                            no_eqp_list.append(Id)
                            print(f'{Id}, not have head_epq')
                           
    if len(no_eqp_list) != 0:
        print('以下這些Id可能沒戴安全帽:')
        for number in no_eqp_list:
            print(f'Id:{number} ')
        return False
    else:
        return True
