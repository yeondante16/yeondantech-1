import streamlit as st
import streamlit.components.v1 as components
import requests

st.set_page_config(page_title="캠 장치", layout="wide")


# ---- 헤더 영역 ----
col1, col2 = st.columns([1, 3])

with col1:
    st.image("cam.gif", caption="캠 운동 예시", use_container_width=True)


with col2:
    st.markdown("### 🛠️ 캠(Cam) 장치에 대해 알아봅시다!")
    st.markdown("""
    캠은 회전 운동을 직선 운동으로 바꿔주는 부품입니다.  
    생김새는 둥글지만 한쪽이 불룩하게 튀어나와 있어서,  
    캠이 돌 때마다 연결된 막대나 판이 위아래로 움직이게 됩니다.  
    이 원리를 이용하면 인형에 숨을 추가하거나,  
    동물의 고개를 끄덕이는 것처럼 다양한 움직임을 만들 수 있어요.  
    오토마타를 만들 때 아주 중요한 역할을 한답니다.
    """)

    st.markdown("📎 [오토마타 캠 장치 예시 링크](https://www.youtube.com/watch?si=DtWbvdwF49ZN3B5Z&v=4u0JA9NJt2g&feature=youtu.be)")

st.markdown("---")


# ---- 섹션 1: 캠 크기 계산기 ----

import streamlit.components.v1 as components

# 캠 계산기 섹션 제목
st.markdown("## 🛠 캠 크기 계산기")
st.markdown("자동 계산기를 활용해 오토마타 제작을 위한 캠의 크기를 직접 설정해보세요!")

# GAS 웹 앱 iframe 삽입
components.html(
    '<iframe src="https://script.google.com/macros/s/AKfycbynwf2JhuSbnAAlqmc7XByofMMyTfCb7ql_WELld2Vb3YR8lHqmezSlGoHwk922evAb/exec" width="100%" height="600" frameborder="0" allowfullscreen></iframe>',
    height=600
)


# ---- 섹션 2: 캠 활용 예시 ----
st.subheader("2️⃣ 캠 장치의 활용 예시")
st.image("pen.png", caption="캠과 펜 연결 예시", width=300)
st.markdown("연필깎이부터 자동차 엔진까지, 일상 속에서 캠이 활용되는 다양한 예시를 알아봅니다.")
