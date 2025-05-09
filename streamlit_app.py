import streamlit as st
st.title("유영준의 첫 번쨰 앱!")
st.info("안녕하세요! 반갑습니다. 저는 유영준입니다.")
st.write("안녕하세요! 반갑습니다. 저는 유영준입니다.")
#페이지 구조용 제목 출력
st.title("메인 제목입니다")
st.header("중간 제목입니다")
st.subheader("하위 제목입니다")



name=st.text_input("이름을 입력해주세요")
st.write(name+"님 반갑습니다!")

# 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("선택한 성별:", gender)

if name=="유영준":
    st.success(name+"님 반갑습니다")
else:
    st.error("접근 권한이 없습니다")