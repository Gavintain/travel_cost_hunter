from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from time import sleep
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

def main():
    st.title("Streamlit 멀티 페이지 앱")

    # 사이드바에서 페이지 선택
    selected_page = st.sidebar.radio("페이지 선택", ["Home", "About", "Contact"])

    # 각 페이지의 내용을 표시
    if selected_page == "Home":
        st.write("이곳은 홈 페이지입니다.")
    elif selected_page == "About":
        st.write("이곳은 소개 페이지입니다.")
    elif selected_page == "Contact":
        st.write("이곳은 연락처 페이지입니다.")

if __name__ == "__main__":
    main()
