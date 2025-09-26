from flask import Flask, make_response, render_template, request, send_file

from backend.color import Color, assert_normal
from backend.rainbow import RainbowConfigModel
from backend.recmans_sequence import naive_approach
from backend.svg_file import generate_series_visualization

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


def parse_input(data: dict):
    sequence_length = data.get("sequence_length", 80)
    image_size = data.get("image_size", 100)
    line_width = assert_normal(data.get("line_width", 0.001))
    use_rainbow_color = data.get("use_rainbow_color", True)
    line_color = Color.from_hex_str(data.get("line_color", "#aa0e0e"))
    use_background_color = data.get("use_background_color", False)
    background_color = Color.from_hex_str(data.get("background_color", "#000000"))
    padding = assert_normal(data.get("padding", 0.001))
    rotate_visualization = data.get("rotate_visualization", False)
    saturation = assert_normal(data.get("saturation", 1))
    brightness = assert_normal(data.get("brightness", 1))
    alpha = assert_normal(data.get("alpha", 1))

    background_color = background_color if use_background_color else None

    line_color = (
        line_color
        if not use_rainbow_color
        else RainbowConfigModel(saturation, brightness, alpha)
    )

    if sequence_length > 10000:
        sequence_length = 10000

    if image_size > 20000:
        image_size = 20000

    return (
        sequence_length,
        image_size,
        line_width,
        line_color,
        background_color,
        padding,
        rotate_visualization,
    )


@app.route("/svg_file_download", methods=["GET", "POST"])
def svg_file_download():

    (
        sequence_length,
        image_size,
        line_width,
        line_color,
        background_color,
        padding,
        rotate_visualization,
    ) = parse_input(request.json)

    data = naive_approach(sequence_length)

    path = "static/assets/recman_circles.svg"

    generate_series_visualization(
        data,
        file_name=path,
        image_size=image_size,
        line_color=line_color,
        line_width=line_width,
        background_color=background_color,
        rotate_drawing_by_45_deg=rotate_visualization,
        padding=padding,
    )

    return send_file(path)


if __name__ == "__main__":
    app.run(debug=True)
