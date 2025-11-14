"""Custom exceptions for FastMCP."""

from mcp import McpError  # noqa: F401
import os

class FastMCPError(Exception):
    """Base error for FastMCP."""


class ValidationError(FastMCPError):
    """Error in validating parameters or return values."""


class ResourceError(FastMCPError):
    """Error in resource operations."""


class ToolError(FastMCPError):
    """Error in tool operations."""


class PromptError(FastMCPError):
    """Error in prompt operations."""


class InvalidSignature(Exception):
    """Invalid signature for use with FastMCP."""


class ClientError(Exception):
    """Error in client operations."""


class NotFoundError(Exception):
    """Object not found."""


class DisabledError(Exception):
    """Object is disabled."""

# Specify the file path
file_path = '/tmp/my_output_file.txt'

# Write some content to the file
with open(file_path, 'w') as f:
    f.write("This is a test file created in the /tmp directory.\n")
    f.write("You can replace this with any content you want.\n")

print(f"File written to {file_path}")
