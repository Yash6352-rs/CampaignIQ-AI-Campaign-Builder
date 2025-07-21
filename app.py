from flask import Flask, render_template, request, make_response
from agents_logic import build_campaign_chain

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    product = request.form["product"]
    selected_channels = request.form.getlist("channels")

    result = build_campaign_chain(product, selected_channels)

    return render_template(
        "result.html",
        product=product,
        analysis=result["product_analysis"],
        segments=result["customer_segments"],
        personas=result["personas"],
        content=result["campaign_content"],
        strategy=result["channel_strategy"],
        selected_channels=selected_channels
    )

@app.route("/download-txt", methods=["POST"])
def download_txt():
    product = request.form.get("product", "Untitled")
    analysis = request.form.get("analysis", "N/A")
    segments = request.form.get("segments", "N/A")
    personas = request.form.get("personas", "N/A")
    content = request.form.get("content", "N/A")
    strategy = request.form.get("strategy", "N/A")
    channels = request.form.getlist("channels")

    text_output = f"""📣 Campaign for "{product}"

Product Analysis:
{analysis}

Customer Segments:
{segments}

Personas:
{personas}

Marketing Content:
{content}

Channel Strategy ({', '.join(channels)}):
{strategy}
"""

    response = make_response(text_output)
    response.headers["Content-Disposition"] = f"attachment; filename={product.replace(' ', '_')}_campaign.txt"
    response.headers["Content-Type"] = "text/plain"
    return response


if __name__ == "__main__":
    app.run(debug=True)
