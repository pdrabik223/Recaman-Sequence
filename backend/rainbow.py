import math
from .color import Color
from .normalized_float import assert_normal


class RainbowConfigModel:

    def __init__(
        self,
        value_range: float,
        saturation: float = 1,
        brightness: float = 1,
        alpha: float = 1,
    ):

        self.value_range = assert_normal(value_range)
        self.saturation = assert_normal(saturation)
        self.brightness = assert_normal(brightness)
        self.alpha = assert_normal(alpha)


def rainbow(value: float, config: RainbowConfigModel) -> Color:
    """s
    Generate an RGB color tuple based on a position in a color range, creating a rainbow effect.
    Args:
        color (float): The current position in the color range.
        color_range (float): The total range of colors.
        brightness (float, optional): Brightness multiplier for the color. Defaults to 1.
        saturation (float, optional): Saturation value for the color. Defaults to 0.
    Returns:
        tuple: A tuple of three floats representing the RGB color.
    """

    value = assert_normal(value)
    third = value // (config.value_range / 3)

    if third == 0:
        offset_radians = value * math.pi / (config.value_range / 3) / 2

        return Color(
            math.cos(offset_radians) * config.brightness,
            math.sin(offset_radians) * config.brightness,
            config.saturation,
            config.alpha,
        )

    if third == 1:
        value -= config.value_range // 3
        offset_radians = value * math.pi / (config.value_range / 3) / 2
        return Color(
            config.saturation,
            math.cos(offset_radians) * config.brightness,
            math.sin(offset_radians) * config.brightness,
            config.alpha,
        )

    if third == 2:

        value -= 2 * config.value_range // 3
        offset_radians = value * math.pi / (config.value_range / 3) / 2
        return Color(
            math.sin(offset_radians) * config.brightness,
            config.saturation,
            math.cos(offset_radians) * config.brightness,
            config.alpha,
        )

    return Color(1, 0, 0)
