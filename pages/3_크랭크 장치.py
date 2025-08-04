import streamlit as st


st.set_page_config(page_title="크랭크 기구의 원리", layout="wide")

import random
step_num = 3  # 현재 페이지 번호 (1~6)
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
