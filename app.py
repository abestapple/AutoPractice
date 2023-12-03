import streamlit as st
from data import Choice


tabs= st.tabs(["单选", "多选", "判断","主观"])
tab1, tab2, tab3,tab4=tabs
if 'question1' not in st.session_state:
	st.session_state["question1"]=[]
if 'question2' not in st.session_state:
	st.session_state["question2"]=[]
if 'question3' not in st.session_state:
	st.session_state["question3"]=[]
if 'question4' not in st.session_state:
	st.session_state["question4"]=[]
if 'state1' not in st.session_state:
	st.session_state["state1"]=False
if 'state2' not in st.session_state:
	st.session_state["state2"]=False
if 'state3' not in st.session_state:
	st.session_state["state3"]=False
if 'state4' not in st.session_state:
	st.session_state["state4"]=False
with tab1:
	st.write("")
	if not st.session_state["state1"]:
		A=Choice("单选")
		st.session_state["state1"]=True
		st.session_state["question1"]=A
	content=st.session_state["question1"][3].split("$;$")
	st.write(st.session_state["question1"][2])
	st.info("请根据题目选出正确答案!")
	answer4=False
	genre = st.radio(
	"",
	["A: {}".format(content[0]), "B: {}".format(content[1]), "C: {}".format(content[2]),"D: {}".format(content[3])])


	if genre[0] == st.session_state["question1"][4]:
		answer4=True
	col1, col2= st.columns(2)
	with col1:
		b0=st.button("提交答案",key="q0")
	with col2:
		b01=st.button("下一题",key="q11",type="primary")
	if b0:
		if answer4:
			st.success("回答正确！")
		else:
			st.error("答错了！，正确答案是 {}".format(st.session_state["question1"][4]))
			st.write("答案解析：")
			if st.session_state["question1"][5]:
				st.write("")
			else:
				st.write(st.session_state["question1"][5])
	if b01:
		A=Choice("单选")
		st.session_state["question1"]=A		
with tab2:
	st.write("")
	if not st.session_state["state2"]:
		A=Choice("多选")
		st.session_state["state2"]=True
		st.session_state["question2"]=A
	content=st.session_state["question2"][3].split("$;$")
	st.write(st.session_state["question2"][2])
	st.info("请根据题目选出正确答案!")
	answer=[]
	option_1 = st.checkbox("A: {}".format(content[0]))
	option_2 = st.checkbox("B: {}".format(content[1]))
	option_3 = st.checkbox("C: {}".format(content[2]))
	option_4 = st.checkbox("D: {}".format(content[3]))
	if option_1:
		answer.append("A")
	if option_2:
		answer.append("B")
	if option_3:
		answer.append("C")
	if option_4:
		answer.append("D")
	col1, col2= st.columns(2)
	with col1:
		b1=st.button("提交答案")
	with col2:
		b2=st.button("下一题",key="ss",type="primary")
	if b1:
		if "".join(answer)==st.session_state["question2"][4]:
			st.success("答对了！")
		else:
			st.error("答错了！，正确答案是 {}".format(st.session_state["question2"][4]))
			st.write("答案解析：")
			if st.session_state["question2"][5]:
				st.write("")
			else:
				st.write(st.session_state["question2"][5])
	if b2:
		A=Choice("多选")
		st.session_state["question2"]=A	
with tab3:
	st.write("")
	if not st.session_state["state3"]:
		A=Choice("判断")
		st.session_state["state3"]=True
		st.session_state["question3"]=A
	content=st.session_state["question3"][3].split("$;$")
	st.write(st.session_state["question3"][2])
	st.info("请根据题目选出正确答案!")
	genre = st.radio(
	"",
	["A: {}".format(content[0]), "B: {}".format(content[1])])
	answer3=False
	if genre[0] == st.session_state["question3"][4]:
		answer3=True
	col1, col2= st.columns(2)
	with col1:
		b3=st.button("提交答案",key="q1")
	with col2:
		b4=st.button("下一题",key="q2",type="primary")
	if b3:
		if answer3:
			st.success("回答正确！")
		else:
			st.error("答错了！，正确答案是 {}".format(st.session_state["question3"][4]))
			st.write("答案解析：")
			if st.session_state["question3"][5]:
				st.write("")
			else:
				st.write(st.session_state["question3"][5])
	if b4:
		A=Choice("判断")
		st.session_state["question3"]=A	
with tab4:
	st.write("")
	if not st.session_state["state4"]:
		A=Choice("主观")
		st.session_state["state4"]=True
		st.session_state["question4"]=A
	st.write(st.session_state["question4"][2])
	st.write("答：",st.session_state["question4"][4])
	if st.button("下一题",key="csss",type="primary"):
		st.session_state["state4"]=False

css = '''
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 5rem;
    }

	.stTabs [data-baseweb="tab"] {
		height: 40px;
        white-space: pre-wrap;
		border-radius: 4px 4px 0px 0px;
		gap: 10px;
		padding-top: 10px;
		padding-bottom: 10px;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #FFFFFF;
	} p {font-size:16px;white-space:nowrap;}

</style>
'''

st.markdown(css, unsafe_allow_html=True)

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:16px;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

css = '''
<style>
    .stRadio .st-dh{
    font-size:16px;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)
