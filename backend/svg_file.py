import cairo
import math
from typing import Optional

from backend.color import Color
from backend.rainbow import RainbowConfigModel, rainbow
from backend.recmans_sequence import naive_approach


def add_circle(
    context: cairo.Context,
    r: float,
    sx: float,
    upper: bool = True,
    angle_drawing: bool = False,
    color: Color = Color(1, 0.2, 0.2, 1),
):
    """
    Draw a colored arc (circle segment) on the SVG surface.
    Args:
        context (cairo.Context): The Cairo context to draw on.
        r (float): The radius of the arc.
        sx (float): The x-coordinate of the arc's center (normalized).
        upper (bool, optional): Whether to draw the upper or lower arc. Defaults to True.
    """

    context.set_source_rgba(color.red, color.green, color.blue, color.alpha)

    sy = 0.5
    angle1 = 0
    angle2 = math.pi

    if angle_drawing:
        sx /= math.sqrt(2)
        sy = sx
        angle1 = -0.75 * math.pi
        angle2 = 0.25 * math.pi

    if upper:
        tmp = angle1
        angle1 = angle2
        angle2 = tmp

    context.arc(sx, sy, r, angle1, angle2)
    context.stroke()


def generate_series_visualization(
    data: list[int],
    image_size: int = 500,
    line_width: float = 0.001,
    line_color: Color | RainbowConfigModel = Color(0.9, 0.5, 0.5, 1),
    background_color: Optional[Color] = None,
    rotate_drawing_by_45_deg: bool = True,
    padding: float = 0.05,
    file_name: Optional[str] = "recman_circles.svg",
) -> str:
    # file_name += ".csv"
    with cairo.SVGSurface(file_name, image_size, image_size) as surface:

        context = cairo.Context(surface)

        max_width = max(data)

        if rotate_drawing_by_45_deg:
            max_width += data.index(max(data)) / 2
            max_width /= math.sqrt(2)
        else:
            max_width += data.index(max(data)) / 2

        context.set_line_width(line_width)
        context.scale(image_size, image_size)

        if background_color is not None:
            context.set_source_rgb(
                background_color.red, background_color.green, background_color.blue
            )
            context.rectangle(0, 0, image_size, image_size)
            context.fill()

        for i in range(len(data) - 1):

            x = (data[i] + data[i + 1]) / 2
            x /= max_width

            r = abs(data[i] - data[i + 1]) / 2
            r /= max_width

            x += padding

            color = (
                rainbow(r, line_color)
                if isinstance(line_color, RainbowConfigModel)
                else line_color
            )

            add_circle(
                context,
                r,
                x,
                i % 2 == 0,
                angle_drawing=rotate_drawing_by_45_deg,
                color=color,
            )
    return file_name


# get basically random one
def get_random_series():
    return generate_series_visualization(
        data=naive_approach(80),
        image_size=500,
        line_width=0.001,
        line_color=RainbowConfigModel(0.8, 0.2, 1),
        rotate_drawing_by_45_deg=True,
        padding=0.05,
        background_color=Color(0, 0, 0),
    )


if __name__ == "__main__":

    generate_series_visualization(
        data=naive_approach(80),
        image_size=500,
        line_width=0.001,
        line_color=RainbowConfigModel(0.8, 0.2, 1),
        rotate_drawing_by_45_deg=True,
        padding=0.05,
        background_color=Color(0, 0, 0),
    )
