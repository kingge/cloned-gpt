import streamlit as st
import pandas as pd
import numpy as np
 
st.write("## 早上好")
st.write("#### 早上好")

with st.sidebar:    
    name = st.text_input("请输入名称：")
    if name:
        st.write(f"你好,{name}")

#col1,col2,col3 = st.columns(3)        
col1,col2,col3 = st.columns([1,2,3])    
with col1:    
    passwd = st.text_input("请输入名称：",type="password")
    paragraph = st.text_area("请输入长篇大论:")
    age = st.number_input("请输入年龄:",step=1,value=24,max_value=70,min_value=18)

with col2:        
    radio = st.radio("你的单选：",["A","B","C"],index=None)
    if radio:
        st.write(f"选择{radio}")
            
    select = st.selectbox("联系方式多选：",["tel","WX","QQ","eMail"])    
    if select:
        st.write(f"选择{select}")

with col3:    
    list1 = st.multiselect("联系方式多选：",["tel","WX","QQ","eMail"])    
    for ele in list1:
        st.write(f"选择{ele}")
    
    height = st.slider("身高:",min_value=100,max_value=190,value=162,step=10)    
    st.write(f"身高{height}cm")

tab1,tab2,tab3 = st.tabs(["上传","同意","提交"])
with tab1:    
    uploaded=st.file_uploader("请上传文件",type=["pdf","png","jpg","csv","xls","py"])     
    if uploaded:
        st.write(f"上传文件名:{uploaded.name}")
        st.write(f"上传文件名:{uploaded.read()}")

with tab2:            
    checked = st.checkbox("我同意以上条款")
    if checked:
        st.write("感谢你的同意")

#print (st.session_state)        
with tab3:    
    x = 0    
    if "x" not in st.session_state:
        st.session_state.x = 0
    submmitted = st.button("提交")    
    if submmitted:
        st.session_state.x += 1
        st.write(f"提交成功,x={st.session_state.x}")

with st.expander("math:"):        
    a = 222*7
    a

    [11,22,33]
    {"aa":"111","bb":"999"}

    st.image("./1.jpg",width=100)

# 创建标题和描述
st.title("简单的数据分析应用")
st.write("这是一个使用 Streamlit 创建的简单应用")

# 生成一些示例数据
data = pd.DataFrame({
    '列A': np.random.randn(50),
    '列B': np.random.randn(50)
})

# 展示数据表
st.write("数据表：")
st.write(data)
st.divider()
st.dataframe(data)
st.divider()
st.table(data)

# 创建一个简单的线图
st.line_chart(data)


# pip freeze > requirements.txt #生成txt文件,记录所需库
# 上传到gitHub  代码托管网站

#