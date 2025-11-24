# -*- coding: utf-8 -*-
# Converted from 00000001.lns

label title_screen:
    show s7 with Dissolve(0.7)
    return

label opening_animation:
    play music "回想.ogg"
    show op1 with Dissolve(1.0)
    pause 0.5
    show op2 with Dissolve(0.3)
    pause 1.0
    show op3 with Dissolve(0.3)
    pause 2.5
    show op4 with fade
    play sound "FX/可愛い2.ogg"
    show op5 with dissolve
    pause 1.0
    play sound "FX/風.ogg"
    show op6 with Dissolve(0.8)
    show op7 with dissolve
    show op8 with dissolve
    pause 1.5
    show op9 with Dissolve(0.8)
    pause 0.5
    show op10 with dissolve
    stop sound fadeout 2.0
    pause 2.5
    show op11 with Dissolve(0.8)
    pause 0.5
    show op12 with dissolve
    pause 1.5
    show op13 with dissolve
    play sound "FX/キラキラ.ogg"
    show op14 with Dissolve(1.2)
    pause 2.5
    show op15 with dissolve
    play sound "FX/ひらめき！.ogg"
    show op16 with dissolve
    pause 0.8
    play sound "FX/ジャジャーン.ogg"
    show op17 with lm_flash
    pause 0.8
    show op18 with dissolve
    pause 0.8
    show op19 with dissolve
    stop music fadeout 2.0
    pause 3.0
    hide op
    pause 0.6
    play music "学祭だ！.ogg"
    show s1 with Dissolve(0.3)
    pause 0.2
    show s2 with Dissolve(0.3)
    pause 0.2
    show s3 with Dissolve(0.3)
    pause 0.2
    show s4 with Dissolve(0.3)
    pause 0.5
    show s5 with Dissolve(0.7)
    pause 0.8
    show s6 with Dissolve(0.7)
    pause 0.4
    return

label gymno_title:
    stop music fadeout 0.8
    show テロップ with Dissolve(0.8)
    pause 0.9
    hide テロップ with Dissolve(0.8)
    pause 0.8
    return

label title_music_loop:
    play music "学祭だ！.ogg"
    return

label start_game:
    stop music fadeout 2.0
    scene black with fade
    pause 0.75
    return