from app.server.tools.sql_tools import list_tables, execute_sql_query
from app.server.tools.metadata_tools import describe_table
from app.server.tools.analytics_tools import top_customer, revenue_by_year

class MCPClient:

    def get_available_tools(self):
        return {
            "get_tables": list_tables,
            "get_table_schema": describe_table,
            "run_sql": execute_sql_query,
            "get_top_customers": top_customer,
            "get_revenue_by_year": revenue_by_year
        }
    
    def execute_tool(self, tool_name):

        if tool_name == "get_tables":
            return list_tables()
        
        elif tool_name == "get_table_schema":
            return describe_table()
        
        elif tool_name == "get_top_customers":
            return top_customer()
        
        elif tool_name == "get_revenue_by_year":
            return revenue_by_year()
        
        else:
            return {"error": "Tool not found"}