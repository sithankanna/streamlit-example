import streamlit as st


def main():
    upload()  # The upload functionality will be shown first
    chat_bot()  # Then, the chat bot will be displayed below


def upload():
    st.title("Upload Documents")

    jd_file = st.file_uploader("Upload a JD", type=["pdf"])
    cv_file = st.file_uploader("Upload your CV", type=["pdf"])

    if jd_file:
        st.write("You've uploaded Document 1!")
    if cv_file:
        st.write("You've uploaded Document 2!")

    st.write("---")  # Add a separator between sections


def chat_bot():
    st.title("Echo Bot")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"Echo: {prompt}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
