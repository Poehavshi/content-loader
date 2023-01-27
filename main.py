import streamlit as st
import io


def main():
    st.title("Content loader")

    uploaded_file = st.file_uploader("Choose a video...", type=["mp4"])
    if uploaded_file is not None:
        with st.form("Upload file"):
            tags = st.text_input("Напиши теги через запятую:").split(',')
            g = io.BytesIO(uploaded_file.read())  # BytesIO Object
            temporary_location = "testout_simple.mp4"
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write("Saved!")
                with open(temporary_location, 'wb') as out:  # Open temporary file as bytes
                    out.write(g.read())  # Read bytes into file
                # close file
                out.close()
        st.write(tags)


if __name__ == '__main__':
    main()
