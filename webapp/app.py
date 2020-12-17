import talisker.requests

# Packages
from canonicalwebteam.flask_base.app import FlaskBase
from canonicalwebteam.discourse import (
    Docs,
    DiscourseAPI,
    DocParser,
)
from flask import render_template

# Rename your project below
app = FlaskBase(
    __name__,
    "dqlite.io",
    template_folder="../templates",
    static_folder="../static",
    template_404="404.html",
    template_500="500.html",
)
session = talisker.requests.get_session()

docs_url_prefix = "/docs"
discourse_docs = Docs(
    parser=DocParser(
        api=DiscourseAPI(
            base_url="https://discourse.dqlite.io/",
            session=session,
        ),
        index_topic_id=34,
        url_prefix=docs_url_prefix,
    ),
    document_template="docs/document.html",
    url_prefix=docs_url_prefix,
)
discourse_docs.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")
