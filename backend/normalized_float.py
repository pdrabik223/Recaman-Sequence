# Normalized float, assures that value is in range <0,1>
def assert_normal(value: float) -> float:
    if value > 1:
        return 1
    elif value < 0:
        return 0
    return value
