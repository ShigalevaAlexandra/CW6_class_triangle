class TriangleChecker:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths

    def is_triangle(self):
        if all(isinstance(side_length, (int, float)) for side_length in self.side_lengths):
            if all(side_length > 0 for side_length in self.side_lengths):
                sort_side_lengths = sorted(self.side_lengths)

                if sort_side_lengths[0] + sort_side_lengths[1] > sort_side_lengths[2]:
                    return "Ура, можно построить треугольник!"

                return "Жаль, но из этого треугольник не сделать."

            return "С отрицательными числами ничего не выйдет!"

        return "Нужно вводить только числа!"