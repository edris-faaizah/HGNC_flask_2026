from flask import Flask, request, render_template
import logging
from typing import Dict, Any, Optional

from hgnc_gene_data_collector.data_collector import settings
from hgnc_gene_data_collector.data_collector.models.data_search import search_gene
from hgnc_gene_data_collector.data_collector.models.txt_to_dict import convert_txt_to_dict
from hgnc_gene_data_collector.data_collector.logger import setup_logging

# Application Factory
# ---------------------------------
# use csv.dictreader to read the file and turn it into a list of dictionaries

def create_app() -> Flask:
    """
    Creates and configures Flask application
    """

    #create flask instance
    app: Flask = Flask(__name__)

    # setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Initialising Flask application via factory")

    # Load data
    DATA_FILE = settings.DATA_FILE
    logger.info(f"Loading data from {DATA_FILE}")

    try:
        # Store data inside app config to avoid global state
        # ✅ This is important for testing and flexibility
        app.config["DATA"] = convert_txt_to_dict(DATA_FILE)           #recheck this
        logger.info("Data loaded successfully")

    except Exception:
        logger.exception("Failed to load data")
        raise

    # Routes
    # --------------------------

    @app.route("/")
    def home() -> str:
        """
        Home page route
        """
        logger.debug("Rendering homepage")
        return render_template("index.html")

    @app.route("/search", methods=["POST"])
    def search() -> str:
        """
        Search route to handle search requests
        """
        try:
            query: str = request.form.get("query", "").strip()
            logger.debug(f"Received search query: {query}")

            if not query:
                logger.warning("Empty search query received")
                return render_template("index.html",
                output_text_1="No query identified.",
                output_text_2 = ""
                )


            query_result: Optional[Dict[str, Any]] = search_gene(query, app.config["DATA"]) #pass in the dataset

            if query_result is None:
                logger.info(f"No results found for query: {query}")
                return render_template("index.html",
                output_text_1=f"Error: {query} not found",
                output_text_2 = ""
                )
                
            logger.info(f"Info found for: {query}")
            
            output_text_1 : str = f"Info for {query}"
            output_text_2 = query_result

            return render_template("index.html",
            output_text_1 = output_text_1 ,
            output_text_2 = output_text_2
            )
                
        except KeyError as e:
            logger.warning(f"Missing expected data field: {e}")
            return render_template(
                "index.html",
                output_text_1=f"Error: missing data field {str(e)}",
                output_text_2=""
            )

        except Exception as e:
            logger.exception("Unexpected error during search")
            return render_template(
                "index.html",
                output_text_1=f"Error: {str(e)}",
                output_text_2=""
            ) 

    return app

app: Flask = create_app()

# -------------------------------------------------------------------
# Entry point (local development only)
# -------------------------------------------------------------------
if __name__ == "__main__":
    logging.getLogger(__name__).info("Running Flask app")
    app.run()