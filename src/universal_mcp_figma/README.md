# Universal Mcp Figma MCP Server

An MCP Server for the Universal Mcp Figma API.

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.11+ (Recommended)
* [uv](https://github.com/astral-sh/uv) installed globally (`pip install uv`)

## 🛠️ Setup Instructions

Follow these steps to get the development environment up and running:

### 1. Sync Project Dependencies
Navigate to the project root directory (where `pyproject.toml` is located).
```bash
uv sync
```
This command uses `uv` to install all dependencies listed in `pyproject.toml` into a virtual environment (`.venv`) located in the project root.

### 2. Activate the Virtual Environment
Activating the virtual environment ensures that you are using the project's specific dependencies and Python interpreter.
- On **Linux/macOS**:
```bash
source .venv/bin/activate
```
- On **Windows**:
```bash
.venv\\Scripts\\activate
```

### 3. Start the MCP Inspector
Use the MCP CLI to start the application in development mode.
```bash
mcp dev src/universal_mcp_figma/mcp.py
```
The MCP inspector should now be running. Check the console output for the exact address and port.

## 🔌 Supported Integrations

- AgentR
- API Key (Coming Soon)
- OAuth (Coming Soon)

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Universal Mcp Figma API.

| Tool | Description |
|------|-------------|
| `get_file` | Retrieves file metadata and content from the API using the specified file key and optional query parameters. |
| `get_file_nodes` | Fetches node data for specified IDs from a file, supporting optional filters such as version, depth, geometry, and plugin data. |
| `get_images` | Retrieves image assets from a remote service for specified node IDs within a given file, with optional image format and export options. |
| `get_image_fills` | Retrieves image fill data for a given file key from the API. |
| `get_team_projects` | Retrieves the list of projects associated with a specified team. |
| `get_project_files` | Retrieves the list of files associated with a specified project, optionally filtered by branch data. |
| `get_file_versions` | Retrieves a paginated list of version history for a specified file. |
| `get_comments` | Retrieves comments for a specified file, optionally formatting the output as Markdown. |
| `post_comment` | Posts a comment to a specified file. |
| `delete_comment` | Deletes a specific comment from a file identified by its key and comment ID. |
| `get_comment_reactions` | Retrieves the reactions associated with a specific comment in a file. |
| `post_comment_reaction` | Posts a reaction emoji to a specific comment on a file. |
| `delete_comment_reaction` | Removes a specific emoji reaction from a comment in a file. |
| `get_me` | Retrieves information about the authenticated user from the API. |
| `get_team_components` | Retrieves a paginated list of components associated with a specified team. |
| `get_file_components` | Retrieves the component information for a specified file from the API. |
| `get_component` | Retrieves a component's details by its key from the API. |
| `get_team_component_sets` | Retrieves a paginated list of component sets for a specified team. |
| `get_file_component_sets` | Retrieves the list of component sets associated with a specific file key. |
| `get_component_set` | Retrieves a component set resource by its key from the server. |
| `get_team_styles` | Retrieves a list of styles for a specified team, with optional pagination controls. |
| `get_file_styles` | Retrieves the style definitions for a specified file from the API. |
| `get_style` | Retrieves a style resource identified by the given key from the API. |
| `post_webhook` | Registers a new webhook for a specified event type and team. |
| `get_webhook` | Retrieves the details of a specific webhook by its unique identifier. |
| `put_webhook` | Update an existing webhook's configuration with new settings such as event type, endpoint, passcode, status, or description. |
| `delete_webhook` | Deletes a webhook with the specified webhook ID. |
| `get_team_webhooks` | Retrieves the list of webhooks configured for a given team. |
| `get_webhook_requests` | Retrieves the list of requests for a specified webhook. |
| `get_activity_logs` | Retrieves activity logs from the API with optional filters for events, time range, limit, and order. |
| `get_payments` | Retrieves a list of payments based on the provided filter criteria. |
| `get_local_variables` | Retrieves the local variables associated with a specific file identified by file_key. |
| `get_published_variables` | Retrieves the published variables associated with a specified file key from the server. |
| `post_variables` | Posts or updates variable data for a specified file by sending a POST request to the variables endpoint. |
| `get_dev_resources` | Retrieves development resources for a specific file. |
| `post_dev_resources` | Submits developer resources to the API and returns the parsed JSON response. |
| `put_dev_resources` | Updates the development resources by sending a PUT request to the dev_resources endpoint. |
| `delete_dev_resource` | Deletes a specific development resource associated with a file. |

## 📁 Project Structure

The generated project has a standard layout:
```
.
├── src/                  # Source code directory
│   └── universal_mcp_figma/
│       ├── __init__.py
│       └── mcp.py        # Server is launched here
│       └── app.py        # Application tools are defined here
├── tests/                # Directory for project tests
├── .env                  # Environment variables (for local development)
├── pyproject.toml        # Project dependencies managed by uv
├── README.md             # This file
```

## 📝 License

This project is licensed under the MIT License.

---

_This project was generated using **MCP CLI** — Happy coding! 🚀_
