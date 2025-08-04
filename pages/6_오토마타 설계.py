import streamlit as st
from datetime import datetime
from PIL import Image
import base64
from io import BytesIO

# 페이지 제목
st.markdown("## 🛠️ 오토마타 설계를 위한 챗봇 활용하기")

# 이미지 base64로 변환
def get_base64_image(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 이미지 로드 및 인코딩
img_base64 = get_base64_image("pages/chatlogo.jpg")

# 두 개의 칼럼
col1, col2 = st.columns([1, 20])
with col1:
  st.markdown(
        f"""
        <style>
        .chat-img {{
            width: 150px;
            height: auto;
            border-radius: 10px;
        }}
        </style>
        <img class="chat-img" src="data:image/jpeg;base64,{img_base64}">
        """,
        unsafe_allow_html=True
    )
with col2:
    st.markdown("""
이 챗봇은 여러분이 오토마타를 설계할 때 아이디어를 떠올리고, 어떻게 움직일지 구체적으로 생각해볼 수 있도록 도와주는 친구예요.  
“무엇이 어떻게 움직이면 좋을까?”, “그 움직임은 어느 방향으로, 얼마나 크게 움직일까?” 같은 질문을 던지면서, 여러분이 스스로 상상하고 계획할 수 있도록 도와줄 거예요.  
너무 막연하다면 “다 해줘!”보다는 “조금 더 스스로 생각해보자!” 하고 한숨 쉬게 말할 수도 있어요.  
챗봇과 대화를 나눈 후에는 친구들과 아이디어를 나누고, 진짜로 움직이는 오토마타를 함께 만들게 될 거예요.  
스스로 생각하고 친구들과 협력하며 만드는 재미를 꼭 느껴보세요!
""")

# 챗봇 링크 버튼
st.markdown("[👉 챗봇 링크로 이동하기](https://chatgpt.com/g/g-688b4f233028819195ce21dc0461b654-otomata-jejag-doumi)", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 원하는 플랫폼을 선택하여 제작 과정을 기록해 주세요!")


# 구글 프레젠테이션
col1, col2 = st.columns([1, 5])
with col1:
    st.image("pages/구슬.png", width=100)
with col2:
    st.markdown("#### [구글 프레젠테이션](https://workspace.google.com/intl/ko/products/slides/)")
    st.caption("제작 과정을 순서대로 정리하고 사진과 설명을 슬라이드로 쉽게 꾸밀 수 있어요.")

# 구글 사이트도구
col3, col4 = st.columns([1, 5])
with col3:
    st.image("pages/구사.jpg", width=150)
with col4:
    st.markdown("#### [구글 사이트도구](https://sites.google.com/?hl=ko&tgif=d)")
    st.caption("제작 과정을 홈페이지 형태로 보기 좋게 정리할 수 있어요.")

import random
step_num = 6  # 현재 페이지 번호 (1~6)
total_steps = 6

progress_percent = int((step_num / total_steps) * 100)

messages = [
    "잘하고 있어요! 💪", "지금처럼만 해요! 🌟", "조금만 더 집중해볼까요? ✨",
    "와우, 벌써 여기까지 왔어요!", "스스로에게 박수! 👏", "천천히, 하지만 꾸준히 🐢", "너무 멋진 속도예요 🚀",
]

encouragement = random.choice(messages)

with st.sidebar:
    st.markdown("---")
    st.markdown("### 📊 학습 진도율")
    st.progress(progress_percent)

    st.markdown(f"""
        <div style='
            background-color:#f0f2f6;
            padding:16px;
            border-radius:12px;
            margin-top:10px;
            text-align:center;
            font-size:15px;
            color:#333'>
            <b>{encouragement}</b>
        </div>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ❓ 선생님께 질문하기")
    st.markdown("궁금한 점이 있다면 아래 버튼을 눌러 작성해 주세요 👇")
    st.markdown("[📨 질문 제출하기](https://forms.gle/c8QjUWExyaQe69XL6)", unsafe_allow_html=True)
