import streamlit as st
import random

# 웹 페이지의 제목을 설정합니다.
st.title("🎮 숫자 맞히기 웹 게임")
st.write("1부터 20 사이의 숫자 중 하나를 맞춰보세요!")

# 게임 상태(정답, 시도 횟수)를 브라우저에 저장합니다.
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 20)
    st.session_state.attempts = 0

# 사용자로부터 숫자를 입력받는 칸을 만듭니다.
guess = st.number_input("숫자를 입력하세요 (1~20):", min_value=1, max_value=20, step=1)

if st.button("정답 확인"):
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.warning("더 큰 숫자입니다! (Up)")
    elif guess > st.session_state.secret_number:
        st.warning("더 작은 숫자입니다! (Down)")
    else:
        st.success(f"🎉 정답입니다! {st.session_state.attempts}번 만에 맞히셨네요!")
        if st.button("게임 다시 시작"):
            del st.session_state.secret_number
            st.rerun()