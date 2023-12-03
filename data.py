import pandas as pd

single_choice_df = pd.read_excel('单选.xlsx')
multiple_choice_df = pd.read_excel('多选.xlsx')
true_false_df = pd.read_excel('判断.xlsx')
subjective_df = pd.read_excel('主观题.xlsx')

def get_random_questions(df, num_questions):
    return df.sample(num_questions)

def Choice(type):
    if type=="单选":
        qus=get_random_questions(single_choice_df,1)
        qus=[list(qus["序号"])[0],list(qus["题型"])[0],list(qus["题干（试题正文)"])[0],list(qus["试题选项"])[0],list(qus["试题答案"])[0],list(qus["答案解析"])[0]]
    if type=="多选":
        qus=get_random_questions(multiple_choice_df,1)
        qus=[list(qus["序号"])[0],list(qus["题型"])[0],list(qus["题干（试题正文)"])[0],list(qus["试题选项"])[0],list(qus["试题答案"])[0],list(qus["答案解析"])[0]]
    if type=="判断":
        qus=get_random_questions(true_false_df,1)
        qus=[list(qus["序号"])[0],list(qus["题型"])[0],list(qus["题干（试题正文)"])[0],list(qus["试题选项"])[0],list(qus["试题答案"])[0],list(qus["答案解析"])[0]]
    if type=="主观":
        qus=get_random_questions(subjective_df,1)
        qus=[list(qus["序号"])[0],list(qus["题型"])[0],list(qus["题干（试题正文)"])[0],list(qus["试题选项"])[0],list(qus["试题答案"])[0],list(qus["答案解析"])[0]]

    return qus