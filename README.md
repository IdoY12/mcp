# Local File Management MCP Server

A Model Context Protocol (MCP) server that provides file system operations (list, read, write) within a local project directory. Built with FastMCP.

## Prerequisites

- Python 3.10+
- `fastmcp` package

## Installation

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies: You can install the core package directly:
```bash
pip install fastmcp
```

Or install all project dependencies from the requirements file:
```bash
pip install -r requirements.txt
```

## Configuration

The server operates within the directory containing `server.py`. To change the base path, modify `PROJECT_BASE_PATH` in `server.py`:

```python
PROJECT_BASE_PATH = os.path.dirname(os.path.abspath(__file__))
```

## Integration with Claude Desktop

Add this server to your Claude Desktop configuration file (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "mcp-file-server": {
      "command": "/path/to/your/venv/bin/python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

Replace `/path/to/your/venv/bin/python` with the absolute path to your Python interpreter, and `/path/to/server.py` with the absolute path to `server.py`.

**Configuration file locations:**
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

## Available Tools

| Tool | Description |
|------|-------------|
| `list_project_files` | List files in the project directory (optional `sub_folder` parameter) |
| `read_file_content` | Read contents of a file (`filename` parameter) |
| `create_new_file` | Create a new file (`filename` and `content` parameters) |

All operations are scoped to the project directory. File operations include standard path validation and error handling.
