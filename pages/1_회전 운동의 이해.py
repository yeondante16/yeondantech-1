import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm
import numpy as np
import os

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    body {
        background-color: #f8f4fc;
    }

    .block-container {
        background-color: #fefaff;
        max-width: 1440px;
        margin: 60px auto;
        padding: 80px 65px;
        border-radius: 30px;
        box-shadow: 0 0 30px rgba(0,0,0,0.15);
    }

    h1, h2, h3, h4, h5, h6 {
        color: #4c3575;
    }

    p, li, a, span {
        color: #333333;
    }

    .round-img {
        border-radius: 50%;
        width: 160px;
        height: 160px;
        object-fit: cover;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }

    [data-testid="stSidebar"] {
        background-color: #f4ebff;
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="회전 운동의 이해", layout="wide")

# 한글 폰트 설정
def get_korean_font(size=12):
    font_path = os.path.join("fonts", "NanumGothic-Regular.ttf")
    return fm.FontProperties(fname=font_path, size=size)

font_prop = get_korean_font()

# 페이지 제목
st.title("🛠️ 회전력(토크)의 이해")

st.markdown("""
### ✅ 회전력이란?
물체를 회전시키려면 단순히 힘만 작용한다고 되는 것이 아니라,  
**어디에** 작용하느냐가 중요합니다.  
바로 그 개념이 **토크(Torque)** 또는 **모멘트(Moment)** 입니다.

> **토크 = 힘 × 거리**
""")

st.markdown("""
> **📎 토크와 모멘트는 같은 의미로 쓰이기도 하지만,**  
> **토크**는 엔진·기계 등 회전운동 중심에 더 자주 사용되며  
> **모멘트**는 구조물, 지레 등 정역학 상황에 주로 사용됩니다.
""")

# 사용자 입력
force = st.slider("힘의 크기 (N)", 10, 200, 80)
distance = st.slider("회전 중심으로부터 거리 (m)", 0.1, 0.5, 0.3, step=0.05)
torque = force * distance

st.markdown(f"🧮 계산된 회전력: **{torque:.2f} Nm**")


# 개념 퀴즈
st.markdown("### 🧠 개념 퀴즈")
quiz = st.radio("다음 중 회전력을 크게 만들 수 있는 방법은?", ["A. 짧은 거리에서 강한 힘", "B. 먼 거리에서 약한 힘", "C. 먼 거리에서 강한 힘"])
if quiz == "C. 먼 거리에서 강한 힘":
    st.success("정답입니다! 회전력은 힘과 거리 모두 클수록 커집니다.")
else:
    st.error("다시 생각해 보세요. 토크는 힘 × 거리랍니다!")

# 마무리 정리
st.markdown("""
---

### 📝 정리
- **토크(Torque)** = 힘 × 거리  
- 회전 중심에서 **멀리**, **강한 힘**을 작용할수록 회전력이 커져요.  
- 회전력은 **힘**뿐만 아니라, **작용 지점의 거리**도 중요합니다.
""")

import random
step_num = 1  # 현재 페이지 번호 (1~6)
total_steps = 6

progress_percent = int((step_num / total_steps) * 100)

messages = [
    "잘하고 있어요! 💪", "지금처럼만 해요! 🌟", "조금만 더 집중해볼까요? ✨",
    "와우, 벌써 여기까지 왔어요!", "스스로에게 박수! 👏", "천천히, 하지만 꾸준히 🐢", "너무 멋진 속도예요 🚀",
]

encouragement = random.choice(messages)

import random
import streamlit as st  # 혹시 위에 없으면 꼭 추가해주세요

# 현재 페이지 진도 설정
step_num = 1  # 현재 페이지 번호 (1~6)
total_steps = 6
progress_percent = int((step_num / total_steps) * 100)

# 무작위 응원 메시지
messages = [
    "잘하고 있어요! 💪", "지금처럼만 해요! 🌟", "조금만 더 집중해볼까요? ✨",
    "와우, 벌써 여기까지 왔어요!", "스스로에게 박수! 👏", "천천히, 하지만 꾸준히 🐢", "너무 멋진 속도예요 🚀",
]
encouragement = random.choice(messages)

with st.sidebar:
    # 🎯 프로젝트 홈 안내
    st.markdown("### 🎯 진도율/응원메시지")
    st.markdown("학습 페이지로 이동하면 진도율과 함께 진행 상태가 표시돼요.")

    # 🌈 무지개 진도율 바 추가
    st.markdown(f"""
        <div style="background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
                    border-radius: 10px;
                    height: 16px;
                    width: 100%;
                    max-width: 200px;
                    margin-top: 10px;
                    position: relative;">
            <div style="background-color: rgba(255,255,255,0.6);
                        width: {100 - progress_percent}%;
                        height: 100%;
                        float: right;
                        border-top-right-radius: 10px;
                        border-bottom-right-radius: 10px;"></div>
        </div>
        <p style="font-size: 13px; margin-top: 6px;">진도율: {progress_percent}%</p>
    """, unsafe_allow_html=True)

    # 📝 응원 메시지 박스
    st.markdown(f"""
        <div style='
            background-color:#ffffff;
            padding:16px;
            border-radius:12px;
            margin-top:10px;
            text-align:center;
            font-size:15px;
            color:#333'>
            <b>{encouragement}</b>
        </div>
    """, unsafe_allow_html=True)

    # ✨ 한 줄짜리 구분선 스타일
    st.markdown("<hr style='margin: 20px 0; border: none; height: 1px; background-color: #ccc;'>", unsafe_allow_html=True)

    # ❓ 질문 제출 링크
    st.markdown("### ❓ 선생님께 질문하기")
    st.markdown("궁금한 점이 있다면 아래 버튼을 눌러 작성해 주세요 👇")
    st.markdown("[📨 질문 제출하기](https://forms.gle/c8QjUWExyaQe69XL6)", unsafe_allow_html=True)

