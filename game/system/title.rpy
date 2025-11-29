# -*- coding: utf-8 -*-
# Converted from 00000001.lns

label title_screen:
    show cg s7 with Dissolve(0.7)
    return

label opening_animation:
    play music "reminiscence.ogg"
    show OP op1 at center with Radial(1.0)
    pause 0.5
    show OP op2 with Dissolve(0.3)
    pause 1.0
    show OP op3 with Dissolve(0.3)
    pause 2.5
    show OP op4 with FadeWhite(0.5)
    play sound "fx/cute2.ogg"
    show OP op5 with dissolve
    pause 1.0
    play sound "fx/wind.ogg"
    show OP op6 with FadeBlack(0.8)
    show OP op7 with dissolve
    show OP op8 with dissolve
    pause 1.5
    show OP op9 with DefocusWhite(0.8)
    pause 0.5
    show OP op10 with dissolve
    stop sound fadeout 2.0
    pause 2.5
    show OP op11 with Dissolve(0.8)
    pause 0.5
    show OP op12 with dissolve
    pause 1.5
    show OP op13 with dissolve
    play sound "fx/sparkle.ogg"
    show OP op14 with Radial(1.2)
    pause 2.5
    show OP op15 with dissolve
    play sound "fx/eureka.ogg"
    show OP op16 with dissolve
    pause 0.8
    play sound "fx/tadaa.ogg"
    show OP op17 with zoominout
    pause 0.8
    show OP op18 with dissolve
    pause 0.8
    show OP op19 with dissolve
    stop music fadeout 2.0
    pause 3.0
    hide OP with Dissolve(2.0)
    pause 0.6
    play music "school_festival.ogg"
    show cg s1 at center with Radial(0.3)
    pause 0.2
    show cg s2 with Radial(0.3)
    pause 0.2
    show cg s3 with Radial(0.3)
    pause 0.2
    show cg s4 with Radial(0.3)
    pause 0.5
    show cg s5 with Radial(0.7)
    pause 0.8
    show cg s6 with FadeWhite(0.7)
    pause 0.4
    return

label gymno_title:
    stop music fadeout 0.8
    show cg telop at center with Dissolve(0.8)
    pause 0.9
    hide cg with Dissolve(0.8)
    pause 0.8
    return