def mouve_gyver(self):
    x_position, y_position = self.gyverposition[0]

    if self.direction == "Left":
        new_position = (x_position - MOVE_INCREMENT, y_position)
    elif self.direction == "Right":
        new_position = (x_position + MOVE_INCREMENT, y_position)
    elif self.direction == "Down":
        new_position = (x_position, y_position + MOVE_INCREMENT)
    elif self.direction == "Up":
        new_position = (x_position, y_position - MOVE_INCREMENT)
