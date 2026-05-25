## Control all the ai workflow

from app.client.mcp_client import MCPClient
from app.client.groq_client import ask_groq

client= MCPClient()

def process_user_query(user_query: str):

    query_lower = user_query.lower()

    ## Simple rule based routing to determine which tool to use based on keywords in the user query
    if "table" in query_lower:
        result = client.execute_tool("get_tables")
    
    elif "customer" in query_lower:
        result = client.execute_tool("get_top_customers")

    elif "revenue" in query_lower:
        result = client.execute_tool("get_revenue_by_year")

    else:
        result = "No relevant tool found for the query. Please try asking about tables, customers, or revenue."

    ## Prompt for llm
    final_prompt = f"""The user asked: "{user_query}"
The system executed the following tool and got this result: {result}
Based on the user's query and the tool result, provide a concise and informative response to the user. If the tool result is relevant to the user's query, use it to enhance your response.
If the tool result is not relevant, just answer the user's query based on your knowledge without mentioning the tool result.
"""

    llm_response = ask_groq(final_prompt)

    return llm_response, result
    