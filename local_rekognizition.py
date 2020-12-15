##此module為讀取本機檔案版，因此輸入的檔案位置需要自行調整 3Q

# 讀取本機檔案識別
# 檔名預設從1開始
# 辨識臉部
def rekog(client, imgfilename):

    with open(imgfilename, 'rb') as imgfile:
        imgbytes = imgfile.read()
    rekresp = client.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])
    rekfd = rekresp['FaceDetails'][0]

#辨識情緒並回傳情緒
def emotions(client, imgfilename):
    
    with open(imgfilename, 'rb') as imgfile:
        imgbytes = imgfile.read()
    rekresp = client.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])
    rekfd = rekresp['FaceDetails'][0]
    
    emotion = rekfd['Emotions'][0]['Type']
    
    return emotion

# 讀取本機檔案識別
# 檔名預設從1開始
# 如要計數，需要建立dict用以計數
# 辨識情緒並計數
def emotions_count(client, imgfilename):
    
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
    most_emotions = max(emotion_dict, key = emotion_dict.get)                    
    print(f'目前最多的情緒是{most_emotions}')
    return most_emotions

# This function will return bolling, if eyes are close, it return 'True'
def eyes_close(client, imgfilename):

    with open(imgfilename, 'rb') as imgfile:
        imgbytes = imgfile.read()
    rekresp = client.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])
    rekfd = rekresp['FaceDetails'][0] # 沒打[0]會跑錯
    eyes_close = rekfd['EyesOpen']['Value']
    return not eyes_close

# This founction will return the number of people
def count_face(client, imgfilename):  

    with open(imgfilename, 'rb') as imgfile:
        imgbytes = imgfile.read()
    rekresp = client.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])
    rekfd = rekresp['FaceDetails']
    return (len(rekfd))

# if have equipment on face, it will return true.
def detect_face_eqp(client, imgfilename):
    no_eqp_list = []

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
                if body_part['Name'] == 'FACE':  
                    ppe_items = body_part['EquipmentDetections']
                    
                    if not ppe_items:
                        
                        no_eqp_list.append(Id)
                        print(f'{Id}, not have face_epq')
                        

                    for ppe_item in ppe_items:
                        head_eqp = ppe_item['CoversBodyPart']['Value']
                        
                        if head_eqp == 'False':
                            no_eqp_list.append(Id)
                            print(f'{Id}, not have face_epq')
                           
    if len(no_eqp_list) != 0:
            
        return False, no_eqp_list
    else:
        return True, no_eqp_list

# if have equipment on head, it will return true.
# if someone doesn't have equipment on head, it will print his Id and return false.
def detect_head_eqp(client, imgfilename):
    no_eqp_list = []

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
            
        return False, no_eqp_list
    else:
        return True, no_eqp_list

