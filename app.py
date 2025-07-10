import streamlit as st
import pandas as pd
import base64
import requests

st.title("Read CSV from GitHub")
a = st.text_input("Enter a")
b = st.text_input("Enter b")
c = st.text_input("Enter c")

if st.button("Upload to GitHub"):
    df = pd.DataFrame([{"a": a, "b": b, "c": c}])
    csv = df.to_csv(index=False)
    content = base64.b64encode(csv.encode()).decode()
    url = "https://api.github.com/repos/limfw/temp/contents/data2.csv"
    headers = {"Authorization": f"token {st.secrets['github']['token']}"}
    payload = {
        "message": "Add data.csv",
        "content": content,
        "branch": "main"
    }
    r = requests.put(url, headers=headers, json=payload)
    if r.status_code in [200, 201]:
        st.success("data Uploaded!")
    else:
        st.error("Failed to upload")
