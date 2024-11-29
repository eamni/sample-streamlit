import streamlit as st

st.title("テスト：Streamlit App")


file = st.file_uploader(label="テスト：ファイル", type='pdf')
radio = st.radio(label="テスト：ラジオボタン", options=["a","b","c"])
text_box = st.text_input(label="テスト：テキストボックス")

if st.button(label="テスト：ボタン"):
    st.write(file.name)
    st.write(radio)
    st.write(text_box)