import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm
import numpy as np
import os

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
