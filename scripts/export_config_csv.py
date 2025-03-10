"""Exports layer configuration as a CSV file."""

# Hack to import from qgreenland
import os, sys  # noqa: E401
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.insert(0, PARENT_DIR)

if __name__ == '__main__':
    from qgreenland.util.config.config import (
        init_config,
        get_config,
    )
    from qgreenland.util.config.export import export_config_csv

    init_config()
    export_config_csv(get_config())
