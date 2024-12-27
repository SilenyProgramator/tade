def nacitani():
    basic.show_leds("""
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                """)
    basic.show_leds("""
                . . . . .
                . . . . .
                . # . # .
                . . . . .
                . . . . .
                """)
    basic.show_leds("""
                . . . . .
                . . . . .
                # . . . #
                . . . . .
                . . . . .
                """)
    basic.show_leds("""
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                """)
    basic.show_leds("""
                    . . . . .
                    . . . . .
                    . # . # .
                    . . . . .
                    . . . . .
                    """)
    basic.show_leds("""
                    . . . . .
                    . . . . .
                    # . . . #
                    . . . . .
                    . . . . .
                    """)
                
nacitani()

def on_button_pressed_a():
    basic.show_string("Hitler")
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    basic.show_string("Lenin")
input.on_button_pressed(Button.B, on_button_pressed_b)
