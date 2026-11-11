import os
import sys
import types
from pathlib import Path

# Identify backend directory
BASE_DIR = Path(__file__).resolve().parent.parent  # backend directory
PARENT_DIR = BASE_DIR.parent                      # repository root if cloned together

for path in [str(BASE_DIR), str(PARENT_DIR)]:
    if path not in sys.path:
        sys.path.insert(0, path)

# If 'backend' package cannot be imported directly (e.g., when root is backend/),
# construct the module alias so all internal imports resolve seamlessly.
try:
    import backend.app.main
except ImportError:
    import app
    backend_pkg = types.ModuleType("backend")
    backend_pkg.app = app
    sys.modules["backend"] = backend_pkg
    sys.modules["backend.app"] = app

from backend.app.main import app
