import streamlit as st

def main():
    if "predict_process_page" not in st.session_state:
        st.session_state.predict_process_page = "시작페이지"

    if st.session_state.predict_process_page == "시작페이지":
        st.write("Travel Cost Hunter는 출국 항공권, 귀국 항공권 그리고 숙박권을 바탕으로 총 여행 경비를 예측합니다. 출국 항공권, 귀국 항공권 그리고 숙박권에 대한 몇 가지 데이터를 입력해주시면 예측해드리겠습니다!")
        st.caption('\n\nTeam I5 ')

        # CSS 스타일을 사용하여 버튼을 가로 중앙에 위치시키기
        st.markdown(
            """
            <style>
            .centered-btn-container {
                display: flex;
                justify-content: center;
            }
            .centered-btn {
                width: 150px;
                margin: auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # 가로 중앙에 위치한 버튼
        st.markdown('<div class="centered-btn-container"><button class="centered-btn" onclick="startButtonClicked()">시작하기</button></div>', unsafe_allow_html=True)

    elif st.session_state.predict_process_page == "출국항공권":
        # 출국항공권 예측 페이지 구현
        # ...
        st.write("출국항공권 예측 페이지입니다.")
        st.caption('\n\nTeam I5 ')

if __name__ == "__main__":
    main()