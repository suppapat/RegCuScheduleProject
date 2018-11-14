import pymongo as pymongo


class User():

    studentID=''
    studyTable =[]

    def __init__(self):
        uri = ""
        client = pymongo.MongoClient(uri)
        db = client.RegCuScheduleDB
        self.collection=db.user

    def encryptpassword(self,password):
        import hashlib
        md5 =  hashlib.md5()
        md5.update(password.encode('utf-8'))
        return md5.digest()

    def register(self,student_id,firstname,lastname,password,email):
        if self.collection.find_one({"_id": student_id}) == None:
            self.collection.insert({"_id":student_id,
                                    "firstname":firstname,
                                    "lastname":lastname,
                                    "password": self.encryptpassword(password),
                                    "email":email})
            self.studentID = student_id

    def verify_user(self,student_id,password):
        student=self.collection.find_one({"_id": student_id})
        if student==None:
            return 'Not found'
        else:
            if student['password']==self.encryptpassword(password):
                self.studentID=student['_id']
                return 'Valid'
            else:
                return 'invalid'