# 游戏在此开始。

init -1:
    define persistent.seen_op = None
    define player_surname = "诹访部"
    define player_name = "翔平"

label start:

    call gymno_title

    if persistent.seen_op is None:
        $ persistent.seen_op = True
        call opening_animation
        call title_screen
    else:
        call title_screen
        call title_music_loop
        call start_game
    
    jump day0_start

    return
