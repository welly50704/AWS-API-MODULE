class DetectPPE:

    def __init__(self, client, imgfilename):

        self.dict = []
        with open(imgfilename, 'rb') as imgfile:
            self.imgbytes = imgfile.read()

        self.response = client.detect_protective_equipment(Image={'Bytes': self.imgbytes}, 
        SummarizationAttributes={'MinConfidence':80, 'RequiredEquipmentTypes':['FACE_COVER', 'HAND_COVER', 'HEAD_COVER']})
        self.response_data = self.response  

    # if have equipment on head, it will return true.
# if someone doesn't have equipment on head, it will print his Id and return false.
    def detect_hand_eqp(self):

        self.right_hand_list = []
        self.left_hand_list = []
        
        self.persons = self.response_data['Persons']

        for self.person in self.persons:
            self.Id = self.person['Id']
            self.body_parts = self.person['BodyParts']

            if len(self.body_parts) == 0:
                print(f'{self.Id}:No body_part detected')
                
            else:
                for self.body_part in self.body_parts:
                    # check have detected head.
                    if self.body_part['Name'] == 'RIGHT_HAND':  
                        self.ppe_items = self.body_part['EquipmentDetections']
                        
                        if not self.ppe_items:
                            self.right_hand_list.append(self.Id)
                            print(f'{self.Id}, not have right_hand_epq')
                                                       
                        for self.ppe_item in self.ppe_items:
                            self.right_hand = self.ppe_item['CoversBodyPart']['Value']
                            
                            if self.right_hand == 'False':
                                self.right_hand_list.append(self.Id)
                    
                    if self.body_part['Name'] == 'LEFT_HAND':  
                        self.ppe_items = self.body_part['EquipmentDetections']
                        
                        if not self.ppe_items:
                            self.left_hand_list.append(self.Id)
                            print(f'{self.Id}, not have left_hand_epq')
                                                       
                        for self.ppe_item in self.ppe_items:
                            self.left_hand = self.ppe_item['CoversBodyPart']['Value']
                            
                            if self.left_hand == 'False':
                                self.left_hand_list.append(self.Id)

        self.right_hand_set = set(self.right_hand_list)            
        self.left_hand_set = set(self.left_hand_list) 
        self.hand_set = self.right_hand_set |  self.left_hand_set
#If anyone doesn't have hand_eqp, he will be in the set.                    
        if len(self.hand_set) != 0:               
            return False, self.hand_set
            
        else:
            return True, self.hand_set
            
    def detect_face_eqp(self):

        self.no_eqp_list = []

        self.persons = self.response_data['Persons']

        for self.person in self.persons:
            self.Id = self.person['Id']
            self.body_parts = self.person['BodyParts']

            if len(self.body_parts) == 0:
                print(f'{self.Id}:No body_part detected')
                
            else:
                for self.body_part in self.body_parts:
                    # check have detected head.
                    if self.body_part['Name'] == 'FACE':  
                        self.ppe_items = self.body_part['EquipmentDetections']
                        
                        if not self.ppe_items:                            
                            self.no_eqp_list.append(self.Id)
                            print(f'{self.Id}, not have face_epq')
                            

                        for self.ppe_item in self.ppe_items:
                            self.head_eqp = self.ppe_item['CoversBodyPart']['Value']
                            
                            if self.head_eqp == 'False':
                                self.no_eqp_list.append(self.Id)
                                print(f'{self.Id}, not have face_epq')
                            
        if len(self.no_eqp_list) != 0:               
            return False, self.no_eqp_list

        else:
            return True, self.no_eqp_list

# if have equipment on head, it will return true.
# if someone doesn't have equipment on head, it will print his Id and return false.def detect_head_eqp(client, imgfilename):
    def detect_head_eqp(self):

        self.no_eqp_list = []

        self.persons = self.response_data['Persons']

        for self.person in self.persons:
            self.Id = self.person['Id']
            self.body_parts = self.person['BodyParts']

            if len(self.body_parts) == 0:
                print(f'{self.Id}:No body_part detected')
                
            else:
                for self.body_part in self.body_parts:
                    # check have detected head.
                    if self.body_part['Name'] == 'HEAD':  
                        self.ppe_items = self.body_part['EquipmentDetections']
                        
                        if not self.ppe_items:
                            self.no_eqp_list.append(self.Id)
                            print(f'{self.Id}, not have head_epq')
                                                       
                        for self.ppe_item in self.ppe_items:
                            self.head_eqp = self.ppe_item['CoversBodyPart']['Value']
                            
                            if self.head_eqp == 'False':
                                self.no_eqp_list.append(self.Id)
                                
#If anyone doesn't have head_eqp, it will be append to the list.                    
        if len(self.no_eqp_list) != 0:               
            return False, self.no_eqp_list

        else:
            return True, self.no_eqp_list


class FaceDetails:
    def __init__(self, client, imgfilename):

        with open(imgfilename, 'rb') as imgfile:
            self.imgbytes = imgfile.read()

        self.response = client.detect_faces(Image={'Bytes': self.imgbytes}, Attributes=['ALL'])
        self.response_data = self.response
        try:
            self.rekfd = self.response_data['FaceDetails'][0]
        except IndexError:
            print('偵測不到臉部!')
            
    def emotion(self):

        try:
            self.emotion = self.rekfd['Emotions'][0]['Type']
            return self.emotion

        except (IndexError, AttributeError):
            print('沒偵測到臉部!')

# This function will return the number of people
    def count_face(self):

        self.count_face = self.response_data['FaceDetails']
        return (len(self.count_face))

# This function will return bolling, if eyes are close, it return 'True'
    def eyes_open(self):

        self.eyes_open_list = []

        for self.eop in self.response_data['FaceDetails']:
            self.eyes_open = self.eop['EyesOpen']
            self.eyes_open_list.append(self.eyes_open)

        return self.eyes_open_list

#This function will return list
    def age(self):

        self.age_list = []
        try:
            for self.rd in self.response_data['FaceDetails']:
                self.age = self.rd['AgeRange']
                self.age_list.append(self.age)

        except (NameError, IndexError):
            print('沒有偵測到臉部!無法判斷年齡')

        return self.age_list
    
#This function will return list
    def smile(self):

        self.smile_list = []

        for self.sm in self.response_data['FaceDetails']:
            self.smile = self.sm['Smile']
            self.smile_list.append(self.smile)

        return self.smile_list

#This function will return list    
    def mouth_open(self):

        self.mouth_open_list = []

        for self.mo in self.response_data['FaceDetails']:
            self.mouth_open = self.mo['MouthOpen']
            self.mouth_open_list.append(self.mouth_open)

        return self.mouth_open_list


