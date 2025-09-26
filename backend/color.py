def assert_normal(value: float) -> float:
    if value > 1:
        return 1
    elif value < 0:
        return 0
    return value


class Color:
    def __init__(self, red: float, green: float, blue: float, alpha: float = 1):

        self.red = assert_normal(red)
        self.green = assert_normal(green)
        self.blue = assert_normal(blue)
        self.alpha = assert_normal(alpha)

    def from_hex_str(value: str) -> "Color":

        value = value.lstrip("#")
        values = tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))
        return Color(*values, 1)
