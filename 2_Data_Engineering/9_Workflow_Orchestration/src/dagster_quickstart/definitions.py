"""
definitions.py — Dagster Definitions entry-point for the Weather Pipeline.

All assets are discovered automatically from the `assets` module and
registered with Dagster. This file is referenced in pyproject.toml
under [tool.dagster] -> module_name.
"""

from dagster import Definitions, load_assets_from_modules

from . import assets

# Discover every @asset-decorated function from assets.py
all_assets = load_assets_from_modules([assets])

# The Definitions object is the single source of truth Dagster loads
defs = Definitions(assets=all_assets)
