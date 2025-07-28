import streamlit as st
from PIL import Image
import os

# 프로젝트 소개
st.title("⚙️ 기계요소의 움직임을 이해하고 오토마타 만들기")

st.markdown("""
### 📌 프로젝트 개요
이 웹앱은 기계의 기본 원리를 배우고, 실제로 오토마타를 설계·제작해보는 프로젝트형 학습 도구입니다.

**학습 흐름:**
1. 회전력의 기본 개념 이해 (힘, 토크, 모멘트)
2. 다양한 회전 장치 학습 (캠, 크랭크, 기어, 링크)
3. 나만의 오토마타 설계 및 제작
4. AI 챗봇 도우미와 함께 문제 해결하기

---

### 🧭 탐색 메뉴
아래 버튼을 클릭하면 각 세부 학습 페이지로 이동할 수 있어요.
""")

# 탐색 메뉴
col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_rotation_basics.py", label="🔁 1. 회전력 기초 이해", icon="🔍")
    st.page_link("pages/2_cam_module.py", label="📐 2. 캠의 원리", icon="📈")
    st.page_link("pages/3_crank_module.py", label="🔄 3. 크랭크의 원리", icon="🎚️")

with col2:
    st.page_link("pages/4_gear_module.py", label="⚙️ 4. 기어의 원리", icon="⚙️")
    st.page_link("pages/5_link_module.py", label="🔗 5. 링크의 원리", icon="🔧")
    st.page_link("pages/6_automata_final.py", label="🎨 6. 오토마타 설계 및 제작", icon="🛠️")

# 이미지 (선택)
img_path = os.path.join("assets", "automata_preview.png")
if os.path.exists(img_path):
    st.image(img_path, caption="예시: 오토마타 완성 모습", use_container_width=True)

st.markdown("---")

# AI 챗봇 안내
st.subheader("💬 AI 도우미 챗봇")
st.markdown("""
학습 중 어려운 개념이 있다면, 챗봇에게 질문해보세요!  
기어비 계산, 캠 운동 거리, 개념 설명 등도 도와줍니다.
""")
st.page_link("pages/7_chatbot_helper.py", label="🤖 챗봇 도우미 열기")

