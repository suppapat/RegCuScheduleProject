from django.contrib.sites import requests


class Semester():

    studyProgram=''
    semester=''
    academicYear=0
    cookie=''

    def __init__(self,studyProgram,semester,academicYear):
        self.studyProgram=studyProgram
        self.semester=semester
        self.academicYear=academicYear

    def searchCourseList(self,courseNo,courseName,courseType):
        url_head = 'https://cas.reg.chula.ac.th/servlet/com.dtm.chula.cs.servlet.QueryCourseScheduleNew.QueryCourseScheduleNewServlet'
        cook = requests.get(url_head, verify=False)
        self.cookie = cook.cookies
