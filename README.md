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

## Integration with Claude

### Method 1: Claude Desktop App

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

**After editing the config file, restart Claude Desktop completely for changes to take effect.**

### Method 2: Claude Code Extension in VS Code

If you're using the Claude Code extension in VS Code, you need to configure the MCP server through the Claude Code CLI first:

**Prerequisites:**
- Install the [Claude Code extension](https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-code) in VS Code
- Install Claude Code CLI (follow the installation guide at [code.claude.com](https://code.claude.com))

**Configuration Steps:**

1. Open your terminal and configure the MCP server using the Claude Code CLI:
```bash
claude mcp add mcp-file-server
```

When prompted, provide:
- **Command**: `/path/to/your/venv/bin/python`
- **Arguments**: `/path/to/server.py`

Alternatively, you can manually edit the Claude Code settings file:

2. Open the Claude Code settings file:
   - macOS/Linux: `~/.claude/settings.json`
   - Windows: `%USERPROFILE%\.claude\settings.json`

3. Add your MCP server configuration under the `mcpServers` section:
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

4. Restart VS Code completely (`Cmd/Ctrl+Shift+P` → "Developer: Reload Window")

5. Open the Claude Code extension panel in VS Code and verify the MCP server is connected:
   - Type `/mcp` in the Claude Code chat to see the server status
   - The server should show as "connected" with available tools

**Note:** The Claude Code extension shares settings with the CLI through `~/.claude/settings.json`, so MCP servers configured via CLI will automatically be available in the VS Code extension.

**Finding your Python path:**
```bash
which python  # On macOS/Linux
where python  # On Windows
```

## Available Tools

| Tool | Description |
|------|-------------|
| `list_project_files` | List files in the project directory (optional `sub_folder` parameter) |
| `read_file_content` | Read contents of a file (`filename` parameter) |
| `create_new_file` | Create a new file (`filename` and `content` parameters) |

All operations are scoped to the project directory. File operations include standard path validation and error handling.
