"""
Logging configuration for the HGNC Gene Data Collector (Defensive version?).
- centralised logging
- safe file handling
- defensive programming
- logger naming conventions

"""
import os
from pathlib import Path

"""
this didnt work: wanted the log inside my repo, but this makes
handler log in /home/ubuntu/.hgnc_gene_data_collector.log
# Step 1: DEfine default log file
home_dir = os.path.expanduser("~/repos/HGNC_flask_2026")
DEFAULT_LOG = os.path.join(home_dir, ".hgnc_gene_data_collector.log")

LOG_FILE = DEFAULT_LOG

# Step 2: Normalise path (defensiuve step)
LOG_FILE = os.path.abspath(os.path.expanduser(LOG_FILE))
"""

# HGNC_flask_2026/
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# HGNC_flask_2026/hgnc_gene_data_collector.log
LOG_FILE = PROJECT_ROOT / "hgnc_gene_data_collector.log"

# Step 3: ENsure directory exists
log_dir = os.path.dirname(LOG_FILE)
if log_dir:
    os.makedirs(log_dir, exist_ok=True)

#Step 4: Logging configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    # --------------------------------------------------
    # FORMATTERS
    # --------------------------------------------------
    "formatters": {
        "standard": {
            "format": (
                "%(asctime)s | %(levelname)s | %(name)s | "
                "%(filename)s:%(lineno)d | %(message)s"
            )
        }
    },

    # --------------------------------------------------
    # HANDLERS
    # --------------------------------------------------
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": LOG_FILE,
        },
    },

    "loggers": {
        "hgnc_gene_data_collector": {

            # The logging level for this specific logger
            # DEBUG = capture EVERYTHING (lowest threshold)
            # Helps when you want deep visibility into this component
            "level": "DEBUG",

            # Handlers define *where* the logs go:
            # - "console" → terminal/stdout (human-readable, immediate)
            # - "file"    → persistent storage for later analysis
            #
            # Multiple handlers = same message sent to multiple destinations
            "handlers": ["console", "file"],

            # propagate controls whether logs "bubble up" to parent loggers
            #
            # False (recommended here):
            # - prevents duplicate log entries
            # - ensures this logger is self-contained
            # - useful when you explicitly define handlers for this logger
            #
            # True would:
            # - pass logs to parent/root loggers as well
            # - can cause duplicate messages if those loggers use the same handlers
            #
            # NOTE (important in real systems):
            # - This can be intentionally overridden when your code is used as a library
            # - e.g. if hgnc_gene_data_collector is imported into a larger application (CLI, web app)
            #   the parent application may want to control logging centrally
            # - In that case, setting propagate=True allows integration into the host app’s logging

            "propagate": False
        },
    },

    # --------------------------------------------------
    # ROOT LOGGER
    # --------------------------------------------------
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"],
    }
}

# Setup data directory path
DATA_DIR = Path(__file__).resolve().parent.parent / "hgnc_data"

# Setup data file
DATA_FILE = os.path.join(DATA_DIR, f"hgnc_complete_set.txt")