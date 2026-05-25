## Register tools and expose them via MCP

from fastmcp import FastMCP

from app.server.tools.analytics_tools import top_customer, revenue_by_year
from app.server.tools.metadata_tools import describe_table
from app.server.tools.sql_tools import list_tables, execute_sql_query

## Initialize the MCP instance
mcp = FastMCP("Enterprise SQL MCP", "A powerful SQL assistant for database management and analytics.")

## Register tools with the MCP instance
@mcp.tool()
def get_tables():
    """Get a list of all tables in the database."""
    return list_tables()

@mcp.tool()
def get_table_schema(table_name: str):
    """Get the schema information for a specific table."""
    return describe_table(table_name)

@mcp.tool()
def run_sql(query: str):
    """Execute a custom SQL query."""
    return execute_sql_query(query)

@mcp.tool()
def get_top_customers():
    """Get the top customers by revenue."""
    return top_customer()

@mcp.tool()
def get_revenue_by_year():
    """Get the total revenue by year."""
    return revenue_by_year()

if __name__ == "__main__":
    mcp.run()