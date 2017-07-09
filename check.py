# -*- coding: utf-8 -*-
import requests,re
import time
url='http://daoluyunshu.com/StudyExam/study'

headers = {'Cookie':'set cookie here'}

r = requests.get(url,headers=headers)

html=r.text
print html
p_projectid = 'data-projectid="(.*?)"' 
p_courseid = 'data-courseid="(.*?)"' 
p_resourceid = 'data-resourceid="(.*?)"' 
p_time = u'<span>视频总长：(.*?)分钟</span>' 

def post(project,course,resource,t):
    t=int(t*60)
    data = {'projectId': 932966,
            'courseId': course,
            'courseId': course,
            'resourceId':resource,
            'time':t,
            't':'Tue Jun 11 2017 20:15:29 GMT+0800 (CST)'
            }
    print data
    requests.post("http://daoluyunshu.com/StudyExam/recordStudyTime", data=data,headers=headers)
    time.sleep(60)

projectid = re.findall(p_projectid, html, re.S) 
courseid = re.findall(p_courseid, html, re.S) 
resourceid = re.findall(p_resourceid, html, re.S) 
t=re.findall(p_time, html, re.S) 

for i in range(20,len(t)):
    post(projectid[i],courseid[i],resourceid[i],int(t[i]))