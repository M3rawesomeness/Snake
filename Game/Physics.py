class Physics:
    def __init__(self):
        pass

    @staticmethod
    def check_collisions(rect, rect_two_list: list):
        return rect.collidelist(rect_two_list)
