from typing import Annotated

from mcp.server.fastmcp import FastMCP
from pydantic import Field


def add(
    a: Annotated[
        int,
        Field(description="First number to add"),
    ],
    b: Annotated[
        int | None,
        Field(description="Optional second number to add"),
    ] = None,
) -> int:
    if b is None:
        b = 0
    return a + b


if __name__ == "__main__":
    mcp = FastMCP("Optional")
    mcp.add_tool(add)
    mcp.run(transport="stdio")
