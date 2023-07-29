import streamlit as st

def main():
    st.title("Main Page")

    if st.button("Go to Page 1"):
        # 버튼이 클릭되면 Page 1로 이동
        page_1()

    if st.button("Go to Page 2"):
        # 버튼이 클릭되면 Page 2로 이동
        page_2()

def page_1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")
    st.write("Page 1 내용을 보여줍니다.")

    # 버튼 클릭 시 해당 페이지의 내용을 지워줍니다.
    if st.button("Go back"):
        st.empty()

def page_2():
    st.title("Page 2")
    st.write("Welcome to Page 2!")
    st.write("Page 2 내용을 보여줍니다.")

    # 버튼 클릭 시 해당 페이지의 내용을 지워줍니다.
    if st.button("Go back"):
        st.empty()

if __name__ == "__main__":
    main()