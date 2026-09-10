"""
This file defines how logging is activated for this project
Loading configuration from settings.py and applied when explicitly requested

HOW IT WORKS:
- call setup function ONCE at start of application
    from HGNC_flask_2026.hgnc_gene_data_collector.logger import setup_logging
    setup_logging()
- only apply configuration here, do not create loggers or define handlers here
- It is best practice to initialise logging at the root of your installable package
(e.g. SeqKitSTP) so all modules inherit consistent behaviour
     logger = logging.getLogger(__name__)

"""

import logging.config

from hgnc_gene_data_collector.settings import LOGGING_CONFIG


# --------------------------------------------------
# LOGGING ACTIVATION FUNCTION
# --------------------------------------------------
def setup_logging():
    """
    Apply the logging configuration.

    This should be called ONCE at application startup.

    After this:
    ✔ Logging is globally configured
    ✔ All modules can use logging.getLogger()s
    ✔ Hierarchical inheritance works automatically
    """

    logging.config.dictConfig(LOGGING_CONFIG)