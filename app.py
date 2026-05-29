import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="연애 코칭 앱",
    page_icon="💝",
    layout="centered"
)

# 제목
st.title("💝 연애 코칭 앱")
st.write("연애 고민을 입력하면 간단한 조언을 해드립니다.")

# 고민 입력
problem = st.text_area(
    "고민을 입력하세요",
    placeholder="예: 연락이 점점 줄어들어요..."
)

# 버튼 클릭
if st.button("조언 받기"):

    # 입력 안 했을 때
    if problem == "":
        st.warning("고민을 입력해주세요.")
    
    else:
        # 아주 단순한 코칭 로직
        if "연락" in problem:
            advice = """
            📱 연락 문제 조언
            
            - 상대를 너무 몰아붙이지 마세요.
            - 감정보다 차분한 대화를 시도해보세요.
            - 자신의 생활 리듬도 유지하는 것이 중요합니다.
            """

        elif "싸움" in problem:
            advice = """
            😥 싸움 문제 조언
            
            - 누가 맞는지보다 이해가 중요합니다.
            - 감정이 심할 때는 잠시 시간을 가지세요.
            - 서운했던 부분을 차분히 설명해보세요.
            """

        elif "이별" in problem:
            advice = """
            💔 이별 고민 조언
            
            - 억지로 붙잡기보다 감정을 정리하세요.
            - 자신을 돌보는 시간이 필요합니다.
            - 새로운 인간관계와 취미를 만들어보세요.
            """

        else:
            advice = """
            🌸 연애 기본 조언
            
            - 솔직한 대화가 가장 중요합니다.
            - 상대방의 감정도 존중해주세요.
            - 자신의 행복도 함께 챙기세요.
            """

        # 결과 출력
        st.success("코칭 결과")
        st.write(advice)

# 하단 문구
st.divider()
st.caption("Made with Streamlit 💕")
