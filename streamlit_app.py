import streamlit as st
import graphviz
import random

st.set_page_config(page_title="오토마타 설계 흐름", layout="wide")

st.markdown("""
    <style>
    /* 전체 배경색 */
    body {
        background-color: #f8f4fc;
    }

    /* 🌸 콘텐츠 카드 스타일 (1.5배 확장) */
    .block-container {
        background-color: #fefaff;
        max-width: 1440px;  /* 기존 1200px → 1440px */
        margin: 60px auto;
        padding: 80px 65px;  /* 기존 padding보다 넓게 */
        border-radius: 30px;
        box-shadow: 0 0 30px rgba(0,0,0,0.15);
    }

    .intro-box {
        background-color: #eae2f8;
        padding: 20px 26px;
        border-radius: 18px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.04);
        margin-bottom: 30px;
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



# === 제목 ===
st.markdown("## 🛠️ 오토마타 설계 프로젝트")

# === 오토마타 소개 ===
st.markdown("<div class='tight-col'>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    st.image("pages/오토마타.jpg", width=160)
with col2:
    st.markdown("""
    <div class='intro-box'>
    <h3>“기계의 움직임은 어떻게 만들어질까?”</h3>
    오토마타는 톱니바퀴나 캠, 크랭크처럼 기계요소들이 결합되어 움직이는 장난감이에요.  
    이 프로젝트에서는 직접 오토마타를 설계하고 제작하면서 회전 운동의 원리를 배울 거예요.  
    챗봇 도우미의 도움도 받아가며, 멋진 창작품을 만들어봅시다! 😎✨
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# === 학습 흐름도 ===
st.markdown("### 🧭 학습 단계 흐름도")

flow = graphviz.Digraph()
flow.attr(rankdir='LR', size='10,4')

flow.node("1", "🔍 회전력 이해", shape="box", width="1.5")
flow.node("2", "📈 캠 장치", shape="box", width="1.5")
flow.node("3", "🎚️ 크랭크 장치", shape="box", width="1.5")
flow.node("4", "⚙️ 기어 장치", shape="box", width="1.5")
flow.node("5", "🔧 링크 장치", shape="box", width="1.5")
flow.node("6", "🛠️ 오토마타 설계\n(챗봇 도우미 포함)", shape="box", width="2", style="filled", fillcolor="#e6f7ff")

flow.edges([("1", "2"), ("2", "3"), ("3", "4"), ("4", "5"), ("5", "6")])
st.graphviz_chart(flow)

# === 페이지 바로가기 ===
st.markdown("### 🔗 페이지 바로가기")
col1, col2, col3 = st.columns(3)
with col1:
    st.page_link("pages/1_회전 운동의 이해.py", label="1단계: 회전력", icon="🔍")
    st.page_link("pages/2_캠 장치.py", label="2단계: 캠 장치", icon="📈")
with col2:
    st.page_link("pages/3_크랭크 장치.py", label="3단계: 크랭크", icon="🎚️")
    st.page_link("pages/4_기어 장치.py", label="4단계: 기어 장치", icon="⚙️")
with col3:
    st.page_link("pages/5_링크 장치.py", label="5단계: 링크", icon="🔧")
    st.page_link("pages/6_오토마타 설계.py", label="6단계: 오토마타 설계", icon="🛠️")

# === 닫기용 div ===
st.markdown("</div>", unsafe_allow_html=True)

# === 사이드바 요소 ===
messages = [
    "시작이 반이에요! 🚀",
    "이제부터 함께해요! 🤝",
    "잘 오셨어요! 준비되셨나요? 👀",
    "마음의 엔진 시동 걸기! 🔧",
    "오늘도 멋진 하루예요! 🌞",
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
