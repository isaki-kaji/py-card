class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("原点")
        case Point(x=0, y=y):
            print(f"y={y}")
        case Point(x=x, y=0):
            print(f"x={x}")
        case Point():
            print("それ以外のどこか")
        case _:
            print("座標ではない")
