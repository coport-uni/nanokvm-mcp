"""MCPB bundle entry point for the NanoKVM MCP server.

This thin wrapper exists so the bundle has a stable ``server/main.py``
entry point, as required by the MCPB manifest. The ``nanokvm_mcp``
package and its dependencies are vendored into ``server/lib`` and made
importable through the ``PYTHONPATH`` set in ``manifest.json``.
"""

from nanokvm_mcp.server import main

if __name__ == "__main__":
    main()
