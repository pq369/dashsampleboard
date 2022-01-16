


import streamlit as st

st.set_page_config(    page_title = 'Streamlit Sample Dashboard Template',    page_icon = '✅',    layout = 'wide')


st.markdown("## KPI First Row")
# kpi 1 
kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:    
  st.markdown("**First KPI**")  
  number1 = 111   
  st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with kpi2:    
  st.markdown("**Second KPI**")  
  number2 = 222   
  st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with kpi3:    
  st.markdown("** d KPI**")  
  number3 = 222   
  st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)

st.markdown("## KPI Second Row")

kpi01, kpi02, kpi03, chart1, chart2 = st.columns(5)

# kpi 1 
with kpi1:    
  st.markdown("**First KPI**")  
  number1 = 111   
  st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with kpi2:    
  st.markdown("**Second KPI**")  
  number2 = 222   
  st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with kpi3:    
  st.markdown("** d KPI**")  
  number3 = 222   
  st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)

st.markdown("## Chart Layout")


with chart1:    
 chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])   
 st.line_chart(chart_data)

with chart2:  
  chart_data = pd.DataFrame(np.random.randn(2000, 3),columns=['a', 'b', 'c'])  
  st.line_chart(chart_data)
