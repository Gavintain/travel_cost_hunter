import streamlit as st

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