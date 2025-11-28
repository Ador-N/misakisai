# 游戏在此开始。

init -1:
    default persistent.seen_op = None
    default persistent.player_surname = "诹访部"
    default persistent.player_name = "翔平"

    default group_day1 = 0 # 服装/布置/料理/采购 = 1/2/3/4
    default group_day2 = 0 # 服装/布置/料理/采购 = 1/2/3/4
    default group_day3 = 0 # 服装/布置/料理/采购 = 1/2/3/4

    default target_day1 = ""
    default target_day2 = ""
    default target_day3 = ""

    default ending = ""

label splashscreen:
    call gymno_title
    if persistent.seen_op is None:
        $ persistent.seen_op = True
        call opening_animation
    return

label start:

label logic_day0:

    call day0
    call day0_1
    call day0_2
    call day0_3
    call day0_4

    call day0_normal
    call day0_normal_1

    $ day0_random_character = renpy.random.choice(["tomo", "tubasa", "sinobu", "sintarou", "tuki", "sora", "sakuya", "saburo"])

    call expression "day0_" + day0_random_character + "_before"

    python:
        ask_name_prompts = {
            "tomo": _("前辈～～！告诉我你叫什么名字嘛！"),
            "tubasa": _("那、那个……可以问一下你的名字吗……？"),
            "sinobu": _("名字？"),
            "tuki": _("报上名来。"),
            "sora": _("大哥哥，你叫什么名字呀？"),
            "sintarou": _("喂～那边超帅的大哥哥！告诉咱你的名字呗♪"),
            "sakuya": _("名字！叫什么？"),
            "saburo": _("喂～喂～能不能告诉咱你叫啥呀？")
        }

    window hide
    call screen input_name(ask_name_prompts[day0_random_character])
    $ player_surname, player_name = persistent.player_surname, persistent.player_name = _return
    window auto

    call expression "day0_" + day0_random_character + "_after"

label logic_day1:

    call day1
    call day1_1
    call day1_2

    menu (screen="choice_group"):
        "服装组":
            $ group_day1 = 1
            jump logic_day1_design
        "布置组":
            $ group_day1 = 2
            jump logic_day1_layout
        "料理组":
            $ group_day1 = 3
            jump logic_day1_cooking
        "采购组":
            $ group_day1 = 4
            jump logic_day1_supply
    
    label logic_day1_design:
        call day1_design
        menu:
            "离开教室":
                $ target_day1 = "tomo"
            "留在教室":
                $ target_day1 = "sintarou"
        call expression "day1_design_" + target_day1
        jump logic_day1_end
    
    label logic_day1_layout:
        call day1_layout
        menu:
            "离开教室":
                $ target_day1 = "sinobu"
            "留在教室":
                $ target_day1 = "tubasa"
        call expression "day1_layout_" + target_day1
        jump logic_day1_end
    
    label logic_day1_cooking:
        call day1_cooking
        menu:
            "让月留下":
                $ target_day1 = "tuki"
            "让空留下":
                $ target_day1 = "sora"
        call expression "day1_cooking_" + target_day1
        jump logic_day1_end
    
    label logic_day1_supply:
        call day1_supply
        menu:
            "去校舍后面":
                $ target_day1 = "sakuya"
            "去屋顶":
                $ target_day1 = "saburo"
        call expression "day1_supply_" + target_day1
        jump logic_day1_end
    
    label logic_day1_end:
        call day1_3
        call expression "day1_3_" + target_day1
        call day1_4
        call expression "day1_4_" + target_day1

label logic_day2:
    call day2
    call day2_1
    if target_day1 in ["tuki", "sora"]:
        call day2_1_futago
    else:
        call expression "day2_1_" + target_day1
    call day2_2

    menu (screen="choice_group"):
        "服装组":
            $ group_day2 = 1
            jump logic_day2_design
        "布置组":
            $ group_day2 = 2
            jump logic_day2_layout
        "料理组":
            $ group_day2 = 3
            jump logic_day2_cooking
        "采购组":
            $ group_day2 = 4
            jump logic_day2_supply
    
    label logic_day2_design:
        call day2_design
        if group_day1 == 1:
            menu:
                "让友试试领带":
                    $ target_day2 = "tomo"
                "让慎太郎试试领带":
                    $ target_day2 = "sintarou"
            if target_day1 != target_day2:
                jump day2_bad_end
            call expression "day2_design_" + target_day2
        else:
            call day2_design_self
        jump logic_day2_end

    label logic_day2_layout:
        call day2_layout
        if group_day1 == 2:
            menu:
                "特别是忍君":
                    $ target_day2 = "sinobu"
                "特别是翼君":
                    $ target_day2 = "tubasa"
            if target_day1 != target_day2:
                jump day2_bad_end
            call expression "day2_layout_" + target_day2
        else:
            call day2_layout_self
        jump logic_day2_end
    
    label logic_day2_cooking:
        call day2_cooking
        if group_day1 == 3:
            menu:
                "帮助月":
                    $ target_day2 = "tuki"
                "帮助空":
                    $ target_day2 = "sora"
            call expression "day2_cooking_" + target_day2
        else:
            call day2_cooking_self
        jump logic_day2_end
    
    label logic_day2_supply:
        call day2_supply
        if group_day1 == 4:
            menu:
                "跟着作哉":
                    $ target_day2 = "sakuya"
                "跟着三朗":
                    $ target_day2 = "saburo"
            if target_day1 != target_day2:
                jump day2_bad_end
            call expression "day2_supply_" + target_day2
        else:
            call day2_supply_self
            call day2_supply_self_1
            call day2_supply_self_2
        jump logic_day2_end

    label logic_day2_end:
        call day2_end

label logic_day3:
    call day3
    call day3_1
    
    $ day3_temp_target = target_day2 if target_day2 != "" else target_day1
    if day3_temp_target in ["tomo", "sinobu"]:
        call day3_1_tomo_sinobu
    elif day3_temp_target in ["saburo", "sakuya", "tubasa"]:
        call day3_1_saburo_sakuya_tubasa
    elif day3_temp_target in ["sintarou", "tuki", "sora"]:
        call day3_1_sintarou_tuki_sora

    if target_day2 in ["tuki", "sora"]:
        call expression "day3_2_futago"
    if target_day2 != "":
        call expression "day3_2_" + target_day2
    call day3_3
    if target_day2 == target_day1:
        call expression "day3_3_" + target_day2
    call day3_4

    menu (screen="choice_group"):
        "服装组":
            $ group_day3 = 1
            jump logic_day3_design
        "布置组":
            $ group_day3 = 2
            jump logic_day3_layout
        "料理组":
            $ group_day3 = 3
            jump logic_day3_cooking
        "采购组":
            $ group_day3 = 4
            jump logic_day3_supply
    
    label logic_day3_design:
        if 1 != group_day1 != group_day2 != 1:
            call day3_design_sirou
            jump logic_day3_sirou

        call day3_design
        $ target_day3 = target_day2
        if target_day3 not in ["tomo", "sintarou"]:
            menu:
                "黄色":
                    $ target_day3 = "tomo"
                "橙色":
                    $ target_day3 = "sintarou"

        call expression "day3_design_" + target_day3
        if target_day3 == target_day2:
            call expression "day3_design_2_" + target_day3
        else:
            call day3_design_2_self
        jump logic_day4
        

    label logic_day3_layout:
        if 2 != group_day1 != group_day2 != 2:
            call day3_layout_sirou
            jump logic_day3_sirou

        call day3_layout

        $ target_day3 = target_day2
        if target_day3 not in ["sinobu", "tubasa"]:
            menu:
                "帮助忍":
                    $ target_day3 = "sinobu"
                "帮助翼":
                    $ target_day3 = "tubasa"

        if target_day3 == "sinobu":
            call day3_layout_sinobu
            if group_day2 == 2:
                call day3_layout_sinobu_2
            else:
                call day3_layout_sinobu_2_noday2
            call day3_layout_2
            if target_day2 == "sinobu":
                call day3_layout_2_sinobu

        elif target_day3 == "tubasa":
            call day3_layout_tubasa
            if target_day2 == "tubasa":
                call day3_layout_tubasa_2
            elif group_day2 == 2:
                call day3_layout_tubasa_2_noinroute
            else:
                call day3_layout_tubasa_2_noday2
            call day3_layout_2
            if target_day2 == "tubasa":
                call day3_layout_2_tubasa
        
        jump logic_day4
        

    label logic_day3_cooking:
        if 3 != group_day1 != group_day2 != 3:
            call day3_cooking_sirou
            jump logic_day3_sirou
        if target_day2 not in ["tuki", "sora"]:
            call day3_cooking_all
            jump logic_day4
        
        call day3_cooking
        menu:
            "让月来做":
                $ target_day3 = "tuki"
            "让空来做":
                $ target_day3 = "sora"
        call expression "day3_cooking_" + target_day3
        jump logic_day4

    label logic_day3_supply:
        if 4 != group_day1 != group_day2 != 4:
            call day3_supply_sirou
            jump logic_day3_sirou

        call day3_supply
        if target_day2 in ["sakuya", "saburo"]:
            $ target_day3 = target_day2
            call expression "day3_supply_" + target_day3
            call day3_supply_2
            call expression "day3_supply_2_" + target_day3
        else:
            call day3_supply_self

        jump logic_day4

label logic_day3_sirou:
    call day3_sirou
    $ target_day3 = "sirou"
    jump logic_day4

label logic_day4:

    # 计算最终结局
    if target_day1 == target_day2 == target_day3 != "":
        $ ending = target_day3
    elif group_day1 == group_day2 == group_day3 == 3:
        $ ending = "futago"
    elif group_day1 != group_day2 != group_day3 != group_day1:
        $ ending = "sirou"
    else:
        $ ending = "all"
    
    call day4
    call day4_1
    if ending not in ["all", "sirou"]:
        call expression "day4_1_" + ending
    call expression "end_" + ending

    return
