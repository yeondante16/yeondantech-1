import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm
import numpy as np
import os

def render():
    st.markdown("## 회전 운동의 이해")

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

# 시각화
fig, ax = plt.subplots(figsize=(6, 6))

# 회전 중심
ax.plot(0, 0, marker='o', color='black', markersize=10)

# 원판 배경
circle = plt.Circle((0, 0), 0.5, color='lightgray', fill=False, linewidth=2)
ax.add_patch(circle)

# 힘 방향 (빨간 화살표)
arrow_dx = distance * np.cos(np.pi / 4)
arrow_dy = distance * np.sin(np.pi / 4)
ax.arrow(0, 0, arrow_dx, arrow_dy, head_width=0.02, head_length=0.03, fc='red', ec='red', linewidth=2)

# 회전 방향 (보라색 아치형 곡선 + 화살표)
arc = patches.Arc((0, 0), 1.0, 1.0, angle=0, theta1=45, theta2=135,
                  color='purple', lw=torque / 50)  # 회전력 크기에 비례한 굵기
ax.add_patch(arc)
arrowhead_x = 0.5 * np.cos(np.pi * 3 / 4)
arrowhead_y = 0.5 * np.sin(np.pi * 3 / 4)
ax.arrow(arrowhead_x, arrowhead_y, -0.02, 0.02, head_width=0.03, head_length=0.03,
         fc='purple', ec='purple')  # 방향 표시용

# 텍스트 라벨
ax.text(arrow_dx + 0.05, arrow_dy + 0.05, f"{force}N", fontproperties=font_prop)
ax.text(-0.1, -0.6, "회전 중심", fontproperties=font_prop)

# 세팅
ax.set_xlim(-0.7, 0.7)
ax.set_ylim(-0.7, 0.7)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)

# 시각화 설명
st.markdown("""
#### 📌 시각화 설명
- **빨간 화살표**: 힘의 방향  
- **보라색 아치**: 회전 방향 (굵기 = 회전력의 크기)  
- **회전 중심점**: 정중앙 (⚙ 표시된 점)  
> 회전력은 선의 **굵기**로 표현됩니다.  
> 원의 크기는 시각적 요소로, 실제 회전력과는 무관합니다.
""")

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
