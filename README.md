# Local File Management MCP Server

A Model Context Protocol (MCP) server implementation that provides file system operations (list, read, write) within a local project directory. Built with FastMCP as a personal project for exploring the Model Context Protocol.

## Overview

This server exposes three tools to MCP clients:
- List files in the project directory
- Read file contents
- Write new files

All operations are scoped to the project directory where the server is located.

## Prerequisites

- Python 3.14+ (or compatible version)
- pip

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mcp
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install fastmcp
   ```

## Usage

### Running the Server

```bash
python server.py
```

Or with the virtual environment:

```bash
./venv/bin/python server.py
```

### Available Tools

#### `list_project_files`
Lists files in the project directory.

**Parameters:**
- `sub_folder` (optional): Subdirectory path relative to project root

**Returns:** String listing files in the specified path

#### `read_file_content`
Reads the contents of a file in the project directory.

**Parameters:**
- `filename` (required): File path relative to project root

**Returns:** File contents as a string

#### `create_new_file`
Creates a new file in the project directory.

**Parameters:**
- `filename` (required): File path relative to project root
- `content` (required): Content to write to the file

**Returns:** Success or error message

## Project Structure

```
mcp/
├── server.py          # MCP server implementation
├── mission.txt        # Project notes
├── README.md          # This file
└── venv/              # Virtual environment (not tracked in git)
```

## Security

File operations are restricted to the project base directory. The server uses standard path validation to prevent directory traversal. Error handling is implemented for all file operations.

## Configuration

The project base path is set to the directory containing `server.py`. To change this, modify `PROJECT_BASE_PATH` in `server.py`:

```python
PROJECT_BASE_PATH = os.path.dirname(os.path.abspath(__file__))
```

## Integration

Compatible with MCP clients such as Claude Desktop and other MCP-compatible tools.

## License

[Add your license here]
