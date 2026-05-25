## Problem statement:
1. How an mcp server exposes the tools/resources
2. How an MCP client discovers and invokes it
3. How can an LLM interact with mcp capabilities dynamically
4. How can a UI orchestrate the app

## Title: Enterprise MCP Assistant

## Objective: 
Modular AI application with the lifecycle as following:

### User -> Streamlit -> MCP Client -> MCP Server -> LLM -> UI
                                            |
                                        Data source

### Questions:
1. Show top 5 products by revenue
2. Generate sales trend

## MCP Core idea:
1. Client: Sends user request to interact with the tool. Calling tools, selecting tools, orchestrating requests
2. Server: Exposes the capability of the tool. returning outputs
3. Tool: Performs operations/executions. SQL exection, schema reading, analysis '


## Level 1: Hardcorded functions
in this project: User query-> selecting tools -> execute tools -> pass results to groq -> generate the business summary

## Level 2: Capstone: Fully autonomous sql agent
NLP User query -> Converted to equivalent SQL -> MCP server to run -> result will be passed to groq -> generate the business summary

# .env file should contain this without white spaces
- GROQ_API_KEY=
- AZURE_SQL_SERVER=
- AZURE_SQL_DATABASE=
- AZURE_SQL_USERNAME=
- AZURE_SQL_PASSWORD=

# RUN THE CODE
1. Start the mcp server: python -m app.server.mcp_server

2. Run the streamlit app: python -m streamlit run app/streamlit_app.py

