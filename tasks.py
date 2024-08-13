#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


def welcome():
    print("\n\n\t\t\t\t\t Welcome to US high school student records. \t\n")
    print("\nChoose from the following options[1-5]:\n\n 1-Retrieve the sex, age, number of relative in a family, state, and race based on the ID.\n 2-Retrieve the sex, school support, access internet, attendance rate, and parental involvement associated with a specific race.\n 3-Retrieve the ID, free time, math score, reading score and writing score of students whose absences are less than 50 based on the parental involvement. \n 4-Retrieve traveltime,studytime and failure of students who got school support, associated with guardian \n 5-More \n")
    return (" ")



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
    else:
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


def b1(students_df,race2):
    race_filtered_data = students_df[students_df['Race'] == race2]
    top_education = race_filtered_data.groupby(['Parental_involvement']).size().reset_index(name='Count')
    top_education = top_education.sort_values(by='Count', ascending=False).head(3)
    return top_education


def b2(students_df, parental_involvement):
    if parental_involvement=="high" or parental_involvement=="low" or parental_involvement=="medium":
        parental_involvement_data = students_df[students_df['Parental_involvement'] == parental_involvement]
        avg_absences = parental_involvement_data['Absences'].mean()
        print(f"Average for {parental_involvement} parental involvement is:")
        return avg_absences
    else:
        return("Enter correct involvement.")


def b3(students_df,min_attendance):
        attendance_data = students_df[students_df['Attendance_rate'] > min_attendance]
        avg_mathscores = attendance_data.groupby('Race')['Math_score'].mean()
        return avg_mathscores


def b4(students_df):
    internet_access_data = students_df[students_df['Access_internet'] == 'yes']
    average_reading_scores = internet_access_data.groupby('Sex')['Writing_score'].mean()
    return average_reading_scores


def c1(students_df):
    race_counts = students_df['Race'].value_counts()
    plt.figure()
    plt.pie(race_counts, labels=race_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Proportion of Students Based on Race')
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    plt.legend(loc='center',bbox_to_anchor=(1.3,1))
    plt.show()
    return("")


def c2(students_df):
    avg_writing_scores = students_df.groupby('Race')['Writing_score'].mean()
    plt.figure(figsize=(6, 4))
    avg_writing_scores.plot(kind='bar', color='blue')
    plt.title('Average Writing Scores by Race')
    plt.xlabel('Race')
    plt.ylabel('Average Writing Score')
    plt.xticks(rotation=0)
    plt.show()
    return("")


def c3(students_df):
    plt.figure(figsize=(10, 6))
    plt.scatter(students_df['Reading_score'], students_df['Writing_score'])
    plt.title('Relationship Between Reading and Writing Scores')
    plt.xlabel('Reading Score')
    plt.ylabel('Writing Score')
    plt.grid(True)
    plt.show()
    return("")

def c4(students_df):
    avg_math_scores = students_df.groupby('Access_internet')['Math_score'].mean()
    plt.figure(figsize=(10, 6))
    avg_math_scores.plot(kind='bar', color=['#FF5733', '#33FF57'])
    plt.title('Average Math Scores by Internet Access')
    plt.xlabel('Internet Access')
    plt.ylabel('Average Math Score')
    plt.xticks(rotation=0)
    plt.show()
    return("")



# In[ ]:




