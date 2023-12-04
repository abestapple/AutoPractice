import streamlit as st
from data import Choice

st.set_page_config(page_title="答题")
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
	if len(content)==3:
		choices=["A: {}".format(content[0]), "B: {}".format(content[1]), "C: {}".format(content[2])]
	if len(content)==4:
		choices=["A: {}".format(content[0]), "B: {}".format(content[1]), "C: {}".format(content[2]),"D: {}".format(content[3])]
	st.info(st.session_state["question1"][2])
	#st.info("请根据题目选出正确答案!")
	answer4=False
	genre = st.radio(
	"",choices)


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
			A=Choice("单选")
			st.session_state["question1"]=A	
		else:
			st.error("答错了！，正确答案是 {}".format(st.session_state["question1"][4]))
			st.write("答案解析：")
			if st.session_state["question1"][5]:
				st.write("")
			else:
				st.write(st.session_state["question1"][5])		
	if b01:
		print(1)
with tab2:
	st.write("")
	if not st.session_state["state2"]:
		A=Choice("多选")
		st.session_state["state2"]=True
		st.session_state["question2"]=A
	content=st.session_state["question2"][3].split("$;$")
	st.info(st.session_state["question2"][2])
	#st.info("请根据题目选出正确答案!")
	answer=[]

	option_1 = st.checkbox("A: {}".format(content[0]))
	option_2 = st.checkbox("B: {}".format(content[1]))
	option_3 = st.checkbox("C: {}".format(content[2]))
	if len(content)==4:
		option_4 = st.checkbox("D: {}".format(content[3]))
	if len(content)==5:
		option_4 = st.checkbox("D: {}".format(content[3]))
		option_5 = st.checkbox("E: {}".format(content[4]))
	if option_1:
		answer.append("A")
	if option_2:
		answer.append("B")
	if option_3:
		answer.append("C")
	if len(content)==4:
		if option_4:
			answer.append("D")
	if len(content)==5:
		if option_4:
			answer.append("D")
		if option_5:
			answer.append("E")
	col1, col2= st.columns(2)
	with col1:
		b1=st.button("提交答案")
	with col2:
		b2=st.button("下一题",key="ss",type="primary")
	if b1:

		if "".join(answer)==st.session_state["question2"][4]:
			st.success("答对了！")
			A=Choice("多选")
			st.session_state["question2"]=A	
		else:
			st.error("答错了！，正确答案是 {}".format(st.session_state["question2"][4]))
			st.write("答案解析：")
			if st.session_state["question2"][5]:
				st.write("")
			else:
				st.write(st.session_state["question2"][5])
			#A=Choice("多选")
			#st.session_state["question2"]=A	
#	else:
#		A=Choice("多选")
#		st.session_state["question2"]=A				
	if b2:
		print("1")
with tab3:
	st.write("")
	if not st.session_state["state3"]:
		A=Choice("判断")
		st.session_state["state3"]=True
		st.session_state["question3"]=A
	content=st.session_state["question3"][3].split("$;$")
	st.info(st.session_state["question3"][2])
	#st.info("请根据题目选出正确答案!")
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
			A=Choice("判断")
			st.session_state["question3"]=A	
		else:
			st.error("答错了！，正确答案是 {}".format(st.session_state["question3"][4]))
			st.write("答案解析：")
			if st.session_state["question3"][5]:
				st.write("")
			else:
				st.write(st.session_state["question3"][5])		
	if b4:
		print(1)
with tab4:
	st.write("")
	if not st.session_state["state4"]:
		A=Choice("主观")
		st.session_state["state4"]=True
		st.session_state["question4"]=A
	st.info(st.session_state["question4"][2])
	st.write("答：",st.session_state["question4"][4])
	if st.button("下一题",key="csss",type="primary"):
		st.session_state["state4"]=False

css = '''
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 3rem;
    }

	.stTabs [data-baseweb="tab"] {
		height: 40px;
		width: 40px;
        white-space: pre-wrap;
		border-radius: 4px 4px 0px 0px;
		gap: 0px;
		padding-top: 10px;
		padding-bottom: 10px;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #FFFFFF;
	} 
	p {font-size:16px;}

	.stTabs st-bq{
		width:auto;
	}
	#tabs-bui2-tab-0 {
		width:50px;
	}
	#tabs-bui2-tab-1 {
		width:50px;
	}
	#tabs-bui2-tab-2{
		width:50px;
	}
	#tabs-bui2-tab-3{
		width:50px;
	}
	.css-14xtw13.e8zbici0{visibility:hidden;

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
