import streamlit as st

from app.client.orchestrator import process_user_query

st.title("SQL MCP - Streamlit Interface")

st.set_page_config(page_title="SQL MCP", page_icon=":bar_chart:", layout="wide")

## User input
user_query = st.text_input("Ask a question about your database or request an analysis:")

## Button to submit the query
if st.button("Submit"):

    with st.spinner("Processing your query..."):
        
        llm_response, tool_result = process_user_query(user_query)

        ## AI response
        st.subheader("AI Response:")
        st.write(llm_response)

        ## Tool result
        st.subheader("Tool Result:")
        st.write(tool_result)