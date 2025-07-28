import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 한글 폰트 설정
def get_korean_font(size=12):
    font_path = os.path.join("fonts", "NanumGothic-Regular.ttf")
    return fm.FontProperties(fname=font_path, size=size)

font_prop = get_korean_font()

st.title("🔁 캠의 원리 이해하기")

st.markdown("## 1️⃣ 캠이란?")
st.markdown("""
캠(Cam)은 **회전 운동을 직선 운동으로 바꾸는 장치**입니다.  
기계 내부에서 특정 간격으로 무언가를 밀어 올리거나 누를 때 사용됩니다.

예를 들어,  
- 인형의 눈을 깜빡이게 하거나  
- 자동 연필깎이에서 칼날을 움직이게 하거나  
- 자동차 엔진의 밸브 타이밍 제어 등  
다양한 곳에 활용됩니다.
""")

st.markdown("## 2️⃣ 캠과 일반 원형 회전체 비교")
st.markdown("아래 이미지는 **일반 원형**과 **캠 형태**의 구조를 비교한 그림입니다. 어떤 차이점이 느껴지나요?")

st.image("modules/A_two-dimensional_digital_illustration_diagram_dis.png", caption="원형과 캠 구조 비교", use_container_width=True)

st.markdown("## 3️⃣ 🤔 퀴즈: 어떤 캠이 더 높이 밀어올릴까?")
quiz_answer = st.radio("긴 반지름과 짧은 반지름의 차이가 클수록, 막대는 어떻게 움직일까요?", 
                       ["더 많이 움직인다", "덜 움직인다", "차이가 없다"])

if quiz_answer:
    st.markdown("✅ 정답 확인:")
    if quiz_answer == "더 많이 움직인다":
        st.success("정답입니다! 긴 반지름과 짧은 반지름의 차이가 클수록, 막대는 더 많이 위아래로 움직여요.")
    else:
        st.warning("아쉽지만 다시 생각해보세요. 회전하는 동안 길이가 많이 변해야, 막대도 더 많이 움직이겠죠!")

st.markdown("## 4️⃣ 🧮 캠 설계 시뮬레이션")
st.markdown("""
캠의 **짧은 반지름**과 **긴 반지름**을 조절하면, 막대를 얼마나 올릴 수 있는지를 예측할 수 있어요.

- 예를 들어, 짧은 반지름이 1cm이고 긴 반지름이 3cm라면,  
  회전하면서 막대는 **최대 2cm까지** 위로 올라갑니다.
""")

short_radius = st.slider("짧은 반지름(cm)", 0.5, 5.0, 1.0, step=0.5)
long_radius = st.slider("긴 반지름(cm)", short_radius + 0.5, short_radius + 5.0, short_radius + 2.0, step=0.5)

stroke = long_radius - short_radius
st.markdown(f"🎯 막대가 최대 **{stroke:.1f}cm** 만큼 위로 움직입니다.")

st.markdown("📝 실제 캠을 만들 때 이 값을 고려해서, 움직임의 크기를 조절할 수 있어요.")
