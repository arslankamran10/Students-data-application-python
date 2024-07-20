#!/usr/bin/env python
# coding: utf-8

# In[1]:


def a1(csv_reader,id):
    for row in csv_reader:
        if row[0]==id:
            print(f" ID: {row[0]} \t Sex: {row[1]} \t Age: {row[2]} \t Family relative: {row[21]} \t State: {row[26]} \t Race: {row[27]}" )
            return ("")
    return "Student ID not found"


def a2(csv_reader,race):
    result=[]
    for row in csv_reader:
        if row[27]==race:
            result.append({"Sex": row[1], "School Support": row[14], "Access Internet": row[19], "Attendance rate": row[31], "Parental Involvement": row[37]})
    if result:
        #return result
        print(*result, sep = "\n")
        return("")
    return("Race not found")


def a3(csv_reader,involvement):
    result2=[]
    absent=50
    for row in csv_reader:
        if row[37]==involvement and int(row[25])<absent:
            result2.append({"ID": row[0],"Free time": row[22],"Maths Score": row[28],"Reading Score": row[29],"Writing Score": row[30]})
    if result2:
        print(*result2, sep = "\n")
        return("")
    return("Enter correct involvement")


def a4(csv_reader,guardian):
    result3=[]
    for row in csv_reader:
        if row[10]==guardian and row[14]=="yes":
            result3.append({"Travel time": row[11],"Study time": row[12],"Failures": row[13]})
    if result3:
        print(*result3, sep = "\n")
        return("")
    return("Enter correct guardian")


# In[ ]:




