import streamlit as st

# Streamlit 앱 초기화
def main():
    st.title("Multi-Page Web App")

    # 현재 페이지 번호 가져오기 (없으면 1로 설정)
    page_number = st.session_state.get("page_number", 1)

    if page_number == 1:
        page_1()
    elif page_number == 2:
        page_2()
    elif page_number == 3:
        page_3()

def page_1():
    st.header("Page 1")

    # 데이터 입력 받기
    data_input = st.text_input("Enter some data:")
    if st.button("Save Data"):
        # 입력 받은 데이터를 세션 상태에 저장하고 페이지 전환
        st.session_state.data = data_input
        st.session_state.page_number = 2
        st.success("Data saved successfully! Moving to Page 2.")
        st.experimental_rerun()

def page_2():
    st.header("Page 2")

    # 이전 페이지에서 저장한 데이터 표시
    if "data" in st.session_state:
        st.write("Data from Page 1:", st.session_state.data)
    else:
        st.write("No data from Page 1")

    # 추가 작업 수행 후 다음 페이지로 이동
    if st.button("Next"):
        st.session_state.page_number = 3
        st.experimental_rerun()

def page_3():
    st.header("Page 3")

    # 이전 페이지에서 저장한 데이터 표시
    if "data" in st.session_state:
        st.write("Data from Page 1:", st.session_state.data)
    else:
        st.write("No data from Page 1")

    # 추가 작업 수행 후 완료
    st.write("Page 3 작업 완료!")

    # 다시 처음 페이지로 돌아가기
    if st.button("Start Over"):
        st.session_state.clear()  # 세션 상태 초기화하여 페이지 전환
        st.experimental_rerun()

if __name__ == "__main__":
    main()