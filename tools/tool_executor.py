from tools.file_tools import (
    list_files,
    read_file,
    write_file,
)


TOOL_MAP = {
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file,
}


def execute_tool(tool_name: str, arguments: dict):

    if tool_name not in TOOL_MAP:
        raise ValueError(f"Unknown tool: {tool_name}")

    tool = TOOL_MAP[tool_name]

    return tool(**arguments)