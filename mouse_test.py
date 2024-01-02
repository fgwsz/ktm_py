from ktm import mouse

m=mouse.Mouse()
print(m.current_position())
m.move_up()
print(m.current_position())
m.move_down()
print(m.current_position())
m.move_left()
print(m.current_position())
m.move_right()
print(m.current_position())
