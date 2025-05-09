import streamlit as st
st.title("유영준의 첫 번쨰 앱!")

import openai

user_api_key = st.text_input("키를 입력해주세요.")

from openai import OpenAI

client = OpenAI(api_key = user_api_key)
prompt = st.text_input("프롬프트를 입력해주세요.")

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}]
)
st.markdown("### 💡 GPT의 답변:")
st.write(completion.choices[0].message.content)
