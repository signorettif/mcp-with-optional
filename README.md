# README

### Setup

```sh
git clone https://github.com/signorettif/mcp-with-optional.git
cd mcp-with-optional
uv sync
```

### Test using inspectors

```sh
npx @modelcontextprotocol/inspector uv run main.py
```

### Test using Cursor

1. Open `.cursor/mcp.json` file.
2. Amend `{path/to/main.py}` to actually point to your local main.py file
3. Reload Cursor and enable MCP server

#### Run commands

✅ Should work

```
call `add` using the following arguments:

{
"a":10
}
```

❌ Should NOT work and throw `Invalid type for parameter 'b' in tool add`

```
call `add` using the following arguments:

{
"a":10,
"b": 20
}
```
