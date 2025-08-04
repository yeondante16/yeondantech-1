import streamlit as st
st.set_page_config(page_title="링크 기구의 원리", layout="wide")

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

import random
step_num = 5  # 현재 페이지 번호 (1~6)
total_steps = 6

progress_percent = int((step_num / total_steps) * 100)

messages = [
    "잘하고 있어요! 💪", "지금처럼만 해요! 🌟", "조금만 더 집중해볼까요? ✨",
    "와우, 벌써 여기까지 왔어요!", "스스로에게 박수! 👏", "천천히, 하지만 꾸준히 🐢", "너무 멋진 속도예요 🚀",
]

encouragement = random.choice(messages)

with st.sidebar:
    st.markdown("### 🎯 프로젝트 홈")
    st.markdown("학습 페이지로 이동하면 진도율과 함께 진행 상태가 표시돼요.")
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

    # ✨ 한 줄짜리 구분선 스타일로 대체
    st.markdown("<hr style='margin: 20px 0; border: none; height: 1px; background-color: #ccc;'>", unsafe_allow_html=True)

    st.markdown("### ❓ 선생님께 질문하기")
    st.markdown("궁금한 점이 있다면 아래 버튼을 눌러 작성해 주세요 👇")
    st.markdown("[📨 질문 제출하기](https://forms.gle/c8QjUWExyaQe69XL6)", unsafe_allow_html=True)
