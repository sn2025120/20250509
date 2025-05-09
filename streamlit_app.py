import streamlit as st
st.title("유영준의 첫 번쨰 앱!")
st.info("안녕하세요! 반갑습니다. 저는 유영준입니다.")
st.write("안녕하세요! 반갑습니다. 저는 유영준입니다.")
#페이지 구조용 제목 출력
st.title("메인 제목입니다")
st.header("중간 제목입니다")
st.subheader("하위 제목입니다")



import streamlit as st

st.title("사용자 인증")

# 이름 입력
name = st.text_input("이름을 입력해주세요")

# 성별 선택 (선택되지 않게 초기화)
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"], index=None)

# 조건 검사
if name:
    if name == "유영준":
        if gender is None:
            st.warning("성별을 선택해주세요!")
        else:
            st.success(f"{name}님 반갑습니다! (성별: {gender})")
    else:
        st.error("접근 권한이 없습니다")
else:
    st.info("이름을 입력해주세요.")

# 여러 옵션 중 하나 선택

import streamlit as st

st.title("성별 선택 예제")

gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"], index=None)

if gender is None:
    st.warning("성별을 선택해주세요!")
else:
    st.success(f"선택한 성별: {gender}")




    # 날짜 입력
date = st.date_input("날짜를 선택하세요")
st.write("선택한 날짜:", date)

# 시간 입력
time = st.time_input("시간을 선택하세요")
st.write("선택한 시간:", time)


# 체크 여부에 따라 분기
agree = st.checkbox("위 조건에 동의합니다")
if agree:
    st.write("감사합니다! 계속 진행합니다.")