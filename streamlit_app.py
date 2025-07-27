import streamlit as st

st.set_page_config(
    page_title="기계 요소 시뮬레이터",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.sidebar.markdown("### 📘 주제 선택")
page = st.sidebar.radio("탐색할 기계 요소를 선택하세요", [
    "기초 역학: 힘과 거리",
    "기어 (Gear)",
    "크랭크 (Crank)",
    "캠 (Cam)",
    "링크 (Link)"
])

# 페이지 연결
if page == "기초 역학: 힘과 거리":
    import modules.physics as physics
    physics.run()

elif page == "기어 (Gear)":
    import modules.gear as gear
    gear.run()

elif page == "크랭크 (Crank)":
    import modules.crank as crank
    crank.run()

elif page == "캠 (Cam)":
    import modules.cam as cam
    cam.run()

elif page == "링크 (Link)":
    import modules.link as link
    link.run()


import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# ✅ 한글 폰트 직접 로드
def get_korean_font(size=12):
    font_path = os.path.join("fonts", "NanumGothic.ttf")
    return fm.FontProperties(fname=font_path, size=size)
