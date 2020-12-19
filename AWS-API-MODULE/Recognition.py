class FaceDetails:
    def __init__(self, client, imgfilename):
        self.dict = []
        with open(imgfilename, 'rb') as imgfile:
            self.imgbytes = imgfile.read()

        self.response = client.detect_faces(Image={'Bytes': self.imgbytes}, Attributes=['ALL'])
        self.response_data = self.response  
        self.rekfd = self.response_data['FaceDetails'][0]
    
    def get_data(self):
        return self.response_data

    def emotion(self):
        try:
            
            self.emotion = self.rekfd['Emotions'][0]['Type']
            return self.emotion
        except IndexError:
            print('沒偵測到臉部!')

    def count_face(self):
        print(self.rekfd)
        return (len(self.rekfd))

    def eyes_closed(self):

        self.eyes_close = self.rekfd['EyesOpen']['Value']
        return not self.eyes_close

class DetectPPE:
    def __init__(self, client, imgfilename):
        self.dict = []
        with open(imgfilename, 'rb') as imgfile:
            self.imgbytes = imgfile.read()

        self.response = client.detect_protective_equipment(Image={'Bytes': self.imgbytes}, 
        SummarizationAttributes={'MinConfidence':80, 'RequiredEquipmentTypes':['FACE_COVER', 'HAND_COVER', 'HEAD_COVER']})
        self.response_data = self.response  

    def detect_face_eqp(self):
        self.no_eqp_list = []

        self.persons = self.response_data['Persons']
        for self.person in self.persons:
            self.Id = self.person['Id']
            print(self.Id)

            self.body_parts = self.person['BodyParts']

            if len(self.body_parts) == 0:
                print('\t\tNo body_part detected')
                
            else:
                for self.body_part in self.body_parts:
                    # check have detected head.
                    if self.body_part['Name'] == 'FACE':  
                        self.ppe_items = self.body_part['EquipmentDetections']
                        
                        if not self.ppe_items:
                            
                            no_eqp_list.append(Id)
                            print(f'{self.Id}, not have face_epq')
                            

                        for self.ppe_item in self.ppe_items:
                            self.head_eqp = self.ppe_item['CoversBodyPart']['Value']
                            
                            if self.head_eqp == 'False':
                                self.no_eqp_list.append(Id)
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
                print(f'\t\t{self.Id}:No body_part detected')
                
            else:
                for self.body_part in self.body_parts:
                    # check have detected head.
                    if self.body_part['Name'] == 'HEAD':  
                        self.ppe_items = self.body_part['EquipmentDetections']
                        
                        if not self.ppe_items:
                            
                            self.no_eqp_list.append(self.Id)
                            
                            

                        for self.ppe_item in self.ppe_items:
                            self.head_eqp = self.ppe_item['CoversBodyPart']['Value']
                            
                            if self.head_eqp == 'False':
                                self.no_eqp_list.append(Id)
                                
                            
        if len(self.no_eqp_list) != 0:
                
            return False, self.no_eqp_list
        else:
            return True, self.no_eqp_list
