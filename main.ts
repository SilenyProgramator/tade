function nacitani() {
    basic.showLeds(`
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                `)
    basic.showLeds(`
                . . . . .
                . . . . .
                . # . # .
                . . . . .
                . . . . .
                `)
    basic.showLeds(`
                . . . . .
                . . . . .
                # . . . #
                . . . . .
                . . . . .
                `)
    basic.showLeds(`
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                `)
    basic.showLeds(`
                    . . . . .
                    . . . . .
                    . # . # .
                    . . . . .
                    . . . . .
                    `)
    basic.showLeds(`
                    . . . . .
                    . . . . .
                    # . . . #
                    . . . . .
                    . . . . .
                    `)
}

nacitani()
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("Hitler")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("Lenin")
})
