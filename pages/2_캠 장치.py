import streamlit as st
import streamlit.components.v1 as components
import requests

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

st.set_page_config(page_title="캠 장치", layout="wide")


# ---- 헤더 영역 ----
col1, col2 = st.columns([1, 3])

with col1:
    st.image("cam.gif", caption="캠 운동 예시", use_container_width=True)


with col2:
    st.markdown("### 🛠️ 캠(Cam) 장치에 대해 알아봅시다!")
    st.markdown("""
    캠은 회전 운동을 직선 운동으로 바꿔주는 부품입니다. 생김새는 둥글지만 한쪽이 불룩하게 튀어나와 있어서, 캠이 돌 때마다 연결된 막대나 판이 위아래로 움직이게 됩니다. 이 원리를 이용하면 인형이 춤을 추거나, 동물이 고개를 끄덕이는 것처럼 다양한 움직임을 만들 수 있어요. 쉽게 말해, 캠은 ‘돌리는 힘을 위아래로 바꿔주는 마법 부품’이라고 할 수 있지요. 캠의 모양을 어떻게 설계하느냐에 따라 움직임도 달라지기 때문에, 오토마타를 만들 때 아주 중요한 역할을 한답니다.
    """)

    st.markdown("📎 [오토마타 캠 장치 예시 링크](https://www.youtube.com/watch?si=DtWbvdwF49ZN3B5Z&v=4u0JA9NJt2g&feature=youtu.be)")

st.markdown("---")


# ---- 섹션 1: 캠 크기 계산기 ----

import streamlit.components.v1 as components

# 캠 계산기 섹션 제목
st.markdown("## 1️⃣ 캠 크기 계산기")
st.markdown("자동 계산기를 활용해 오토마타 제작을 위한 캠의 크기를 직접 설정해보세요!")

# GAS 웹 앱 iframe 삽입
components.html(
    '<iframe src="https://script.google.com/macros/s/AKfycbynwf2JhuSbnAAlqmc7XByofMMyTfCb7ql_WELld2Vb3YR8lHqmezSlGoHwk922evAb/exec" width="100%" height="600" frameborder="0" allowfullscreen></iframe>',
    height=600
)


# ---- 섹션 2: 캠 활용 예시 ----
st.subheader("2️⃣ 캠 장치의 활용 예시")
st.image("pen.png", caption="캠과 펜 연결 예시", width=300)
st.markdown("연필깎이부터 자동차 엔진까지, 일상 속에서 캠이 활용되는 다양한 예시를 알아봅니다.")

import random
step_num = 2  # 현재 페이지 번호 (1~6)
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
step_num = 2  # 현재 페이지 번호 (1~6)
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
    st.markdown("### 🎯 프로젝트 홈")
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
