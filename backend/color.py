from normalized_float import assert_normal


class Color:
    def __init__(self, red: float, green: float, blue: float, alpha: float = 1):

        self.red = assert_normal(red)
        self.green = assert_normal(green)
        self.blue = assert_normal(blue)
        self.alpha = assert_normal(alpha)
