
import requests
from bs4 import BeautifulSoup

class Semester:

    studyProgram=''
    semester=''
    academicYear=0
    cookie=''

    def __init__(self,studyProgram,semester,academicYear):
        self.studyProgram=studyProgram
        self.semester=semester
        self.academicYear=academicYear

    def searchCourseList(self,courseNo,courseName,courseType):
        ##calculate course type to fill gened code
        param={ 'examdateCombo':'I2017207/05/1475',
                'studyProgram':self.studyProgram, #S
                'semester':self.semester, #1/2/3
                'acadyearEfd':self.academicYear,
                'submit.x':'0',
                'submit.y':'0',
                'courseno':courseNo,
                'coursename':courseName,
                'examdate':'',
                'examstartshow':'',
                'examendshow':'',
                'faculty':'',
                'coursetype':'',
                'genedcode':'',
                'cursemester':'1',
                'curacadyear':self.academicYear,
                'examstart':'',
                'examend':'',
                'activestatus':'OFF',
                'acadyear':self.academicYear,
                'lang':'T',
                'download':'download'}
        url_head = 'https://cas.reg.chula.ac.th/servlet/com.dtm.chula.cs.servlet.QueryCourseScheduleNew.QueryCourseScheduleNewServlet'
        head = requests.get(url_head, verify=False)
        self.cookie = head.cookies
        url_left = "https://cas.reg.chula.ac.th/servlet/com.dtm.chula.cs.servlet.QueryCourseScheduleNew.CourseListNewServlet"
        result_left = requests.get(url_left, verify=False, cookies=self.cookie,params=param)
        result_left.encoding = 'utf-8'
        soup_all = BeautifulSoup(result_left.content, "html.parser")
        data_all=soup_all("tr")
        course_list=[]
        for data in data_all:
            soup_sub = BeautifulSoup(str(data), "html.parser")
            courseID=soup_sub.find("font",{"face":"MS Sans Serif",'size':'-1'})
            courseName = soup_sub.find("font", {"face": "MS Sans Serif", 'size': '-2', 'color': "#660000"})
            if courseID and courseName is not None:
                courseID=courseID.get_text()
                courseName=courseName.get_text()
            if courseID is not None and len(courseID)>2 and courseName is not None:
                course_list.append((courseID,courseName[2:]))
        #data=soup.find_all("font",{"face":"MS Sans Serif",'color':'#660000'})"""
        return course_list

    def getCourse(self,courseID):
        s = Subject(self.studyProgram,courseID,self.cookie)
        return s


class Subject(Semester):

    courseID=''
    section=[]

    def __init__(self,studyProgram,courseID,cookie):
        self.studyProgram=studyProgram
        self.courseID=courseID
        self.cookie=cookie

    def getCourseDetail(self):
        param={
            'courseNo': self.courseID,
            'studyProgram': self.studyProgram #S
        }
        url_cen = "https://cas.reg.chula.ac.th/servlet/com.dtm.chula.cs.servlet.QueryCourseScheduleNew.CourseScheduleDtlNewServlet"
        result_center = requests.get(url_cen, verify=False, cookies=self.cookie,params=param)
        soup_all = BeautifulSoup(result_center.content, "html.parser")
        data_all = soup_all("td")
        return data_all



class Section(Subject):

    section=0
    teaching=''
    teachTime=[]
    remark=''
    studentRegis=''
    studentMax=''

    def __init__(self):
        pass

