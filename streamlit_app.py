from collections import namedtuple
import altair as alt
import math
import streamlit as st
from time import sleep
import pandas as pd
import numpy as np

from time import sleep

st.set_page_configg(
  page_icon="이모지",
  page_title="i5-여행경비예측",
  layout="wide",  #넓은 화면으로 보기
)

st.header("i5사이트에 오신 것을 환영합니다")
st.subheader("여행경비예측 서비스란?")

st.caption('여행경비 사이트란~~')
st.caption('이러이러하다~')


#페이지 기본 설정
st.set_page_configg(
  page_icon="이모지",
  page_title="i5-여행경비예측",
  layout="wide",  #넓은 화면으로 보기
)

st.subheader("여행경비예측")
st.markdown("여행예측서비스")


cols = st.columns((2,2,2,2))
with col1:
    data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)
st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            help="Streamlit **widget** commands 🎈",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic",
)

st.set_page_configg(
  page_icon="이모지",
  page_title="i5-여행경비예측",
  layout="wide",  #넓은 화면으로 보기
)

st.subheader("chart")

