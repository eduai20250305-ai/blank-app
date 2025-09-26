import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
if st.button('클릭!'):
    st.write('버튼이 눌렸습니다!')

if st.checkbox('데이터프레임 표시'):
    st.dataframe(df)
