import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="프로젝트 개요", layout="wide")

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
    st.page_link("pages/1_회전 운동의 이해.py", label="1. 회전력 기초 이해", icon="🔍")
    st.page_link("pages/2_캠 장치.py", label="2. 캠의 원리", icon="📈")
    st.page_link("pages/3_크랭크 장치.py", label="3. 크랭크의 원리", icon="🎚️")

with col2:
    st.page_link("pages/4_기어 장치.py", label="4. 기어의 원리", icon="⚙️")
    st.page_link("pages/5_링크 장치.py", label="5. 링크의 원리", icon="🔧")
    st.page_link("pages/6_오토마타 설계.py", label="6. 오토마타 설계 및 제작", icon="🛠️")


