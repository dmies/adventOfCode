def manhattan_distance(a, b=(0, 0)):
    x_value, y_value = a
    x_goal, y_goal = b
    return abs(x_value - x_goal) + abs(y_value - y_goal)
