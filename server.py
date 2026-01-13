from mcp.server.fastmcp import FastMCP
import os

# Initialize the MCP server
server = FastMCP("My_Startup_Engine")

# Define the base project path to keep the AI focused
# Replace this with your actual project path
PROJECT_BASE_PATH = os.path.dirname(os.path.abspath(__file__))

@server.tool()
def list_project_files(sub_folder: str = ""):
    """
    List files specifically within the project directory.
    Use sub_folder to look into specific directories inside the project.
    """
    try:
        # Construct the full path securely
        target_path = os.path.join(PROJECT_BASE_PATH, sub_folder)
        files = os.listdir(target_path)
        return f"Files in project folder '{target_path}': " + ", ".join(files)
    except Exception as e:
        return f"Error accessing path: {str(e)}"

@server.tool()
def create_new_file(filename: str, content: str):
    """
    Create a new file in the project directory with the given content.
    This allows the AI to generate code or documentation.
    """
    try:
        file_path = os.path.join(PROJECT_BASE_PATH, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully created file: {filename}"
    except Exception as e:
        return f"Failed to create file: {str(e)}"

@server.tool()
def read_file_content(filename: str):
    """
    Read the content of a specific file in the project directory.
    This allows the AI to analyze existing code or notes.
    """
    try:
        file_path = os.path.join(PROJECT_BASE_PATH, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return f"Content of {filename}:\n\n{content}"
    except Exception as e:
        return f"Error reading file: {str(e)}"


if __name__ == "__main__":
    server.run()

