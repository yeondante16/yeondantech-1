import os
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 한글 폰트 설정 함수
def get_korean_font(size=12):
    font_path = os.path.join("fonts", "NanumGothic-Regular.ttf")
    return fm.FontProperties(fname=font_path, size=size)

def display_simulation(force, distance, font_prop):
    torque = force * distance
    fig, ax = plt.subplots(figsize=(4, 4))
    pedal_circle = plt.Circle((0, 0), 0.5, color='lightgray', fill=False, linewidth=2)
    ax.add_patch(pedal_circle)

    pedal_x = distance * np.cos(np.pi / 4)
    pedal_y = distance * np.sin(np.pi / 4)
    ax.plot([0, pedal_x], [0, pedal_y], color='red', linewidth=3)
    ax.plot(pedal_x, pedal_y, marker='o', color='blue', markersize=10)
    ax.text(pedal_x + 0.05, pedal_y + 0.05, f"힘: {force}N", fontproperties=font_prop)
    ax.text(-0.3, -0.6, "페달 중심", fontproperties=font_prop)
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-0.6, 0.6)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("자전거 페달에 작용하는 토크", fontproperties=font_prop)
    return fig, torque

font_prop = get_korean_font()

# Streamlit 앱 구성
st.title("⚙️ 기계는 왜 회전할까? - 회전력과 토크 이해하기")

st.markdown("## ✅ 토크란?")
st.markdown("""
**토크(Torque)**는 물체를 회전시키는 힘입니다.  
예를 들어 자전거 페달을 밟으면 뒷바퀴가 회전하게 되죠.  
이처럼 회전을 만들어내는 힘이 바로 **토크**입니다.

> **토크 = 힘 × 거리**  
*(거리: 회전 중심에서 힘이 작용하는 지점까지의 수직 거리)*
""")

st.markdown("---")
st.markdown("## 🎯 실생활 문제 예시")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Torque_animation.gif/220px-Torque_animation.gif", 
         caption="100N 짐을 회전축에서 0.2m 거리에서 들어올리는 상황 (대체 이미지)", 
         use_container_width=True)


st.markdown("**문제:** 100N의 짐을 들어올리기 위해 필요한 토크는 얼마일까요?")
if st.button("🧮 정답 확인"):
    example_torque = 100 * 0.2
    st.success(f"필요한 토크는 **{example_torque} Nm**입니다.")

st.markdown("---")
st.markdown("## 🧪 나만의 페달 세팅 실험")

force = st.slider("밟는 힘 (N)", 10, 200, 80)
distance = st.slider("페달 중심으로부터 거리 (m)", 0.1, 0.5, 0.3, step=0.05)
fig, torque = display_simulation(force, distance, font_prop)
st.write(f"🧮 계산된 토크: **{torque:.2f} Nm**")
st.pyplot(fig)

st.markdown("---")
st.markdown("## 🚀 직접 회전 운동 시뮬레이션 만들어보기")

st.markdown("""
### [Glowscript 회전체 만들기 실습](https://www.glowscript.org)
Glowscript에서는 회전하는 물체를 직접 만들고 관찰할 수 있어요.

1. Glowscript.org 접속 후 [New Program]을 선택  
2. 아래 코드를 붙여넣고 실행하세요 👇
""")

glow_code = """
# Glowscript 3.2 VPython
scene.background = color.white
scene.title = "⚙️ 회전 운동 실험"

힘 = float(input("작용하는 힘 (N)을 입력하세요: "))
거리 = float(input("회전축에서 힘까지의 거리 (m)를 입력하세요: "))
토크 = 힘 * 거리
print(f"계산된 토크는 {토크:.2f} Nm 입니다.")

축 = cylinder(pos=vector(0,0,0), axis=vector(0,0.05,0), radius=0.05, color=color.gray(0.5))
판 = cylinder(pos=vector(0,0.05,0), axis=vector(0,0.01,0), radius=0.3, color=color.orange)
화살표 = arrow(pos=vector(거리,0.05,0), axis=vector(0,0.2,0), color=color.red, shaftwidth=0.02)

각속도 = 토크 * 0.05
t = 0
dt = 0.01
while t < 3:
    rate(60)
    판.rotate(angle=각속도*dt, axis=vector(0,1,0), origin=vector(0,0,0))
    t += dt
"""

st.code(glow_code, language="python")
st.markdown("*💡 입력값을 바꿔가며 회전 속도의 변화를 관찰해보세요!*")
