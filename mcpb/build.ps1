# Build the Windows MCPB bundle for nanokvm-mcp.
#
# Vendors the nanokvm_mcp package and its dependencies as Windows wheels
# into server/lib, then validates and packs the bundle. The vendored
# lib/ and the resulting .mcpb are build artifacts and are gitignored;
# run this script to regenerate them. Requires Python 3.10+ and npx on
# PATH.

$ErrorActionPreference = "Stop"

$mcpbDir = $PSScriptRoot
$projectRoot = Split-Path $mcpbDir -Parent
$libDir = Join-Path $mcpbDir "server\lib"
$output = Join-Path $projectRoot "nanokvm-mcp.mcpb"

Write-Host "Cleaning previous vendored libraries..."
if (Test-Path $libDir) {
    Remove-Item $libDir -Recurse -Force
}

Write-Host "Vendoring nanokvm_mcp and dependencies into server/lib..."
python -m pip install --target $libDir $projectRoot --upgrade

Write-Host "Validating manifest..."
npx -y @anthropic-ai/mcpb validate (Join-Path $mcpbDir "manifest.json")

Write-Host "Packing bundle..."
npx -y @anthropic-ai/mcpb pack $mcpbDir $output

Write-Host "Done: $output"
