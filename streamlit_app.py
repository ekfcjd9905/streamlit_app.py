import streamlit as st
st.write("Hello World")

st.divider()

import streamlit as st
from openai import OpenAI

st.title("GPT-5-mini 질문 응답 웹앱")

st.write("사용자의 질문을 GPT-5-mini 모델에 보내고, 응답을 확인해보는 예제입니다.")

# 1) API Key 입력 (웹 페이지에서 입력 받기)
api_key = st.text_input("OpenAI API Key를 입력하세요 (sk-...)", type="password")

# 2) 질문 입력
question = st.text_area("질문을 입력하세요", placeholder="예: 파이썬과 자바스크립트의 차이를 설명해줘")

# 3) 버튼 눌렀을 때만 호출
if st.button("GPT-5-mini에게 물어보기"):
    if not api_key:
        st.error("먼저 OpenAI API Key를 입력해주세요.")
    elif not question.strip():
        st.error("질문을 입력해주세요.")
    else:
        try:
            # 4) OpenAI 클라이언트 생성 (입력받은 키 사용)
            client = OpenAI(api_key=api_key)

            with st.spinner("GPT-5-mini가 답변을 생성 중입니다..."):
                # ✅ Chat Completions API 사용 (더 단순하고 안정적)
                response = client.chat.completions.create(
                    model="gpt-5-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": question},
                    ],
                )

            # 5) 응답 텍스트 추출 (chat.completions 구조)
            answer = response.choices[0].message.content

            st.subheader("모델의 응답")
            st.write(answer)

        except Exception as e:
            st.error(f"에러가 발생했습니다: {e}")
            st.info("API Key가 올바른지, 모델 이름(gpt-5-mini)이 맞는지 확인해보세요.")


st.title("gpt-image-1-mini 이미지 생성 웹앱")

import base64  

st.subheader("🖼 gpt-image-1-mini 이미지 생성")

image_prompt = st.text_area(
    "만들고 싶은 이미지를 설명해주세요",
    placeholder="예: 부산 광안대교 야경을 고흐풍으로 그려줘",
    key="image_prompt"
)

if st.button("이미지 생성하기"):
    if not api_key:
        st.error("먼저 OpenAI API Key를 입력해주세요.")
    elif not image_prompt.strip():
        st.error("이미지 설명을 입력해주세요.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            with st.spinner("gpt-image-1-mini가 이미지를 생성 중입니다..."):

                # ✔ 프롬프트를 UTF-8로 강제 인코딩
                prompt_text = image_prompt.encode("utf-8").decode()

                img = client.images.generate(
                    model="gpt-image-1-mini",
                    prompt=prompt_text,
                    size="auto",
                    n=1
                )

            b64_image = img.data[0].b64_json
            image_bytes = base64.b64decode(b64_image)

            st.image(image_bytes, caption="gpt-image-1-mini가 생성한 이미지")

        except Exception as e:
            st.error(f"에러가 발생했습니다: {e}")
