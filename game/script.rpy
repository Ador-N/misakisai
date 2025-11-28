## 游戏主逻辑脚本 ##########################################################

## 全局变量初始化 ##########################################################
init -1:
    default persistent.seen_op = None
    default persistent.seen_prelude = None
    default persistent.player_surname = "诹访部"
    default persistent.player_name = "翔平"

    default group_day1 = 0 # 服装/布置/料理/采购 = 1/2/3/4
    default group_day2 = 0 # 服装/布置/料理/采购 = 1/2/3/4
    default group_day3 = 0 # 服装/布置/料理/采购 = 1/2/3/4

    default target_day1 = ""
    default target_day2 = ""
    default target_day3 = ""

    default ending = ""
    default persistent.endings = set()
    default persistent.seen_single_ending = False
    default ask_name_prompts = {
        "tomo": _("学长～～！告诉我你叫什么名字嘛！"),
        "tubasa": _("那、那个……可以问一下你的名字吗……？"),
        "sinobu": _("名字？"),
        "tuki": _("报上名来。"),
        "sora": _("大哥哥，你叫什么名字呀？"),
        "sintarou": _("喂～那边超帅的大哥哥！告诉咱你的名字呗♪"),
        "sakuya": _("名字！叫什么？"),
        "saburo": _("喂～喂～能不能告诉咱你叫啥呀？")
    }

    default random_event_id = -1

## 合并持久化数据
## https://doc.renpy.cn/zh-CN/persistent.html#merging-persistent-data
init python:
    def merge_endings(old, new, current):
        current.update(old)
        current.update(new)
        return current
    renpy.register_persistent('endings', merge_endings)

## 开屏动画 ###############################################################
label splashscreen:
    call gymno_title from _call_gymno_title
    if persistent.seen_op is None:
        $ persistent.seen_op = True
        call opening_animation from _call_opening_animation
    return

## 游戏主流程 #############################################################
label start:

## 序幕 ############################################################
label logic_day0:

    if persistent.seen_prelude:
        menu:
            "观看序幕":
                pass
            "跳过序幕":
                jump logic_day0_name

    call day0 from _call_day0
    call day0_1 from _call_day0_1
    call day0_2 from _call_day0_2
    call day0_3 from _call_day0_3
    call day0_4 from _call_day0_4

    # 满足隐藏剧情条件
    if "bad" in persistent.endings and persistent.seen_single_ending:
        menu:
            "去":
                jump logic_day0_normal
            "不去":
                pass
        
        call day0_hidden from _call_day0_hidden
        call day0_hidden_1 from _call_day0_hidden_1

        menu:
            "帮助夕阳":
                $ ending = "yuuhi"
                call day0_hidden_yuuhi from _call_day0_hidden_yuuhi
            "帮助朔":
                $ ending = "nori"
                call day0_hidden_nori from _call_day0_hidden_nori

        jump logic_endgame
                
    

    label logic_day0_normal:

    call day0_normal from _call_day0_normal
    call day0_normal_1 from _call_day0_normal_1

    $ persistent.seen_prelude = True

    label logic_day0_name:

    $ day0_random_character = renpy.random.choice(["tomo", "tubasa", "sinobu", "sintarou", "tuki", "sora", "sakuya", "saburo"])

    call expression "day0_" + day0_random_character + "_before" from _call_expression

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

    call expression "day0_" + day0_random_character + "_after" from _call_expression_1

## 第一天 ############################################################
label logic_day1:

    call day1 from _call_day1
    call day1_1 from _call_day1_1
    call day1_2 from _call_day1_2

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
        call day1_design from _call_day1_design
        menu:
            "离开教室":
                $ target_day1 = "tomo"
            "留在教室":
                $ target_day1 = "sintarou"
        call expression "day1_design_" + target_day1 from _call_expression_2
        jump logic_day1_end
    
    label logic_day1_layout:
        call day1_layout from _call_day1_layout
        menu:
            "离开教室":
                $ target_day1 = "sinobu"
            "留在教室":
                $ target_day1 = "tubasa"
        call expression "day1_layout_" + target_day1 from _call_expression_3
        jump logic_day1_end
    
    label logic_day1_cooking:
        call day1_cooking from _call_day1_cooking
        menu:
            "让月留下":
                $ target_day1 = "tuki"
            "让空留下":
                $ target_day1 = "sora"
        call expression "day1_cooking_" + target_day1 from _call_expression_4
        jump logic_day1_end
    
    label logic_day1_supply:
        call day1_supply from _call_day1_supply
        menu:
            "去校舍后面":
                $ target_day1 = "sakuya"
            "去屋顶":
                $ target_day1 = "saburo"
        call expression "day1_supply_" + target_day1 from _call_expression_5
        jump logic_day1_end
    
    label logic_day1_end:
        call day1_3 from _call_day1_3
        call expression "day1_3_" + target_day1 from _call_expression_6
        call day1_4 from _call_day1_4
        call expression "day1_4_" + target_day1 from _call_expression_7

## 第二天 ############################################################
label logic_day2:

    call day2 from _call_day2
    call day2_1 from _call_day2_1
    if target_day1 in ["tuki", "sora"]:
        call day2_1_futago from _call_day2_1_futago
    else:
        call expression "day2_1_" + target_day1 from _call_expression_8
    call day2_2 from _call_day2_2

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
        call day2_design from _call_day2_design
        if group_day1 == 1:
            menu:
                "让友试试领带":
                    $ target_day2 = "tomo"
                "让慎太郎试试领带":
                    $ target_day2 = "sintarou"
            if target_day1 != target_day2:
                jump logic_day2_bad_end
            call expression "day2_design_" + target_day2 from _call_expression_9
        else:
            call day2_design_self from _call_day2_design_self
        jump logic_day2_end

    label logic_day2_layout:
        call day2_layout from _call_day2_layout
        if group_day1 == 2:
            menu:
                "特别是忍君":
                    $ target_day2 = "sinobu"
                "特别是翼君":
                    $ target_day2 = "tubasa"
            if target_day1 != target_day2:
                jump logic_day2_bad_end
            call expression "day2_layout_" + target_day2 from _call_expression_10
        else:
            call day2_layout_self from _call_day2_layout_self
        jump logic_day2_end
    
    label logic_day2_cooking:
        call day2_cooking from _call_day2_cooking
        if group_day1 == 3:
            menu:
                "帮助月":
                    $ target_day2 = "tuki"
                "帮助空":
                    $ target_day2 = "sora"
            call expression "day2_cooking_" + target_day2 from _call_expression_11
        else:
            call day2_cooking_self from _call_day2_cooking_self
        jump logic_day2_end
    
    label logic_day2_supply:
        call day2_supply from _call_day2_supply
        if group_day1 == 4:
            menu:
                "跟着作哉":
                    $ target_day2 = "sakuya"
                "跟着三朗":
                    $ target_day2 = "saburo"
            if target_day1 != target_day2:
                jump logic_day2_bad_end
            call expression "day2_supply_" + target_day2 from _call_expression_12
        else:
            call day2_supply_self from _call_day2_supply_self
            call day2_supply_self_1 from _call_day2_supply_self_1
            call day2_supply_self_2 from _call_day2_supply_self_2
        jump logic_day2_end

    label logic_day2_bad_end:
        call day2_bad_end from _call_day2_bad_end
        $ ending = "bad"
        jump logic_endgame

    label logic_day2_end:
        call day2_end from _call_day2_end

## 第三天 ############################################################
label logic_day3:

    call day3 from _call_day3
    call day3_1 from _call_day3_1
    
    $ day3_temp_target = target_day2 if target_day2 != "" else target_day1
    if day3_temp_target in ["tomo", "sinobu"]:
        call day3_1_tomo_sinobu from _call_day3_1_tomo_sinobu
    elif day3_temp_target in ["saburo", "sakuya", "tubasa"]:
        call day3_1_saburo_sakuya_tubasa from _call_day3_1_saburo_sakuya_tubasa
    elif day3_temp_target in ["sintarou", "tuki", "sora"]:
        call day3_1_sintarou_tuki_sora from _call_day3_1_sintarou_tuki_sora

    call logic_random_event from _call_logic_random_event

    if target_day2 in ["tuki", "sora"]:
        call expression "day3_2_futago" from _call_expression_13
    if target_day2 != "":
        call expression "day3_2_" + target_day2 from _call_expression_14
    call day3_3 from _call_day3_3
    if target_day2 == target_day1:
        call expression "day3_3_" + target_day2 from _call_expression_15
    call day3_4 from _call_day3_4

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
            call day3_design_sirou from _call_day3_design_sirou
            jump logic_day3_sirou

        call day3_design from _call_day3_design
        $ target_day3 = target_day2
        if target_day3 not in ["tomo", "sintarou"]:
            menu:
                "黄色":
                    $ target_day3 = "tomo"
                "橙色":
                    $ target_day3 = "sintarou"

        call expression "day3_design_" + target_day3 from _call_expression_16
        if target_day3 == target_day2:
            call expression "day3_design_2_" + target_day3 from _call_expression_17
        else:
            call day3_design_2_self from _call_day3_design_2_self
        jump logic_day4
        

    label logic_day3_layout:
        if 2 != group_day1 != group_day2 != 2:
            call day3_layout_sirou from _call_day3_layout_sirou
            jump logic_day3_sirou

        call day3_layout from _call_day3_layout

        $ target_day3 = target_day2
        if target_day3 not in ["sinobu", "tubasa"]:
            menu:
                "帮助忍":
                    $ target_day3 = "sinobu"
                "帮助翼":
                    $ target_day3 = "tubasa"

        if target_day3 == "sinobu":
            call day3_layout_sinobu from _call_day3_layout_sinobu
            if group_day2 == 2:
                call day3_layout_sinobu_2 from _call_day3_layout_sinobu_2
            else:
                call day3_layout_sinobu_2_noday2 from _call_day3_layout_sinobu_2_noday2
            call day3_layout_2 from _call_day3_layout_2
            if target_day2 == "sinobu":
                call day3_layout_2_sinobu from _call_day3_layout_2_sinobu

        elif target_day3 == "tubasa":
            call day3_layout_tubasa from _call_day3_layout_tubasa
            if target_day2 == "tubasa":
                call day3_layout_tubasa_2 from _call_day3_layout_tubasa_2
            elif group_day2 == 2:
                call day3_layout_tubasa_2_noinroute from _call_day3_layout_tubasa_2_noinroute
            else:
                call day3_layout_tubasa_2_noday2 from _call_day3_layout_tubasa_2_noday2
            call day3_layout_2 from _call_day3_layout_2_1
            if target_day2 == "tubasa":
                call day3_layout_2_tubasa from _call_day3_layout_2_tubasa
        
        jump logic_day4
        

    label logic_day3_cooking:
        if 3 != group_day1 != group_day2 != 3:
            call day3_cooking_sirou from _call_day3_cooking_sirou
            jump logic_day3_sirou
        if target_day2 not in ["tuki", "sora"]:
            call day3_cooking_all from _call_day3_cooking_all
            jump logic_day4
        
        call day3_cooking from _call_day3_cooking
        menu:
            "让月来做":
                $ target_day3 = "tuki"
            "让空来做":
                $ target_day3 = "sora"
        call expression "day3_cooking_" + target_day3 from _call_expression_18
        jump logic_day4

    label logic_day3_supply:
        if 4 != group_day1 != group_day2 != 4:
            call day3_supply_sirou from _call_day3_supply_sirou
            jump logic_day3_sirou

        call day3_supply from _call_day3_supply
        if target_day2 in ["sakuya", "saburo"]:
            $ target_day3 = target_day2
            call expression "day3_supply_" + target_day3 from _call_expression_19
            call day3_supply_2 from _call_day3_supply_2
            call expression "day3_supply_2_" + target_day3 from _call_expression_20
        else:
            call day3_supply_self from _call_day3_supply_self

        jump logic_day4

label logic_day3_sirou:
    call day3_sirou from _call_day3_sirou
    $ target_day3 = "sirou"
    jump logic_day4

## 御咲祭当天 ##########################################################
label logic_day4:

    # 计算最终结局
    if target_day1 == target_day2 == target_day3 != "":
        $ ending = target_day3
        $ persistent.seen_single_ending = True
    elif group_day1 == group_day2 == group_day3 == 3:
        $ ending = "futago"
    elif group_day1 != group_day2 != group_day3 != group_day1:
        $ ending = "sirou"
    else:
        $ ending = "all"
    
    call day4 from _call_day4
    call day4_1 from _call_day4_1
    if ending not in ["all", "sirou"]:
        call expression "day4_1_" + ending from _call_expression_21
    call expression "end_" + ending from _call_expression_22

label logic_endgame:

    $ persistent.endings.add(ending)

    return

## 首页？？？选项 ##########################################################
label logic_hidden:

    call hidden from _call_hidden

    menu:
        "进入":
            pass
        "不进入":
            return
    
    if not ("yuuhi" in persistent.endings or "nori" in persistent.endings):
        call hidden_note from _call_hidden_note
        return

    call hidden_1 from _call_hidden_1

    label logic_hidden_choice:
    menu (screen="choice_group"):
        "服装组":
            jump logic_hidden_design
        "布置组":
            jump logic_hidden_layout
        "料理组":
            jump logic_hidden_cooking
        "采购组":
            jump logic_hidden_supply
    
    label logic_hidden_design:
        if not ("tomo" in persistent.endings or "sintarou" in persistent.endings):
            jump logic_hidden_retry
        menu:
            "友" if "tomo" in persistent.endings:
                window hide
                call hidden_tomo from _call_hidden_tomo
                return
            "????" if "tomo" not in persistent.endings:
                jump logic_hidden_retry
            "慎太郎" if "sintarou" in persistent.endings:
                window hide
                call hidden_sintarou from _call_hidden_sintarou
                return
            "????" if "sintarou" not in persistent.endings:
                jump logic_hidden_retry
    
    label logic_hidden_layout:
        if not ("sinobu" in persistent.endings or "tubasa" in persistent.endings):
            jump logic_hidden_retry
        menu:
            "忍" if "sinobu" in persistent.endings:
                window hide
                call hidden_sinobu from _call_hidden_sinobu
                return
            "????" if "sinobu" not in persistent.endings:
                jump logic_hidden_retry
            "翼" if "tubasa" in persistent.endings:
                window hide
                call hidden_tubasa from _call_hidden_tubasa
                return
            "????" if "tubasa" not in persistent.endings:
                jump logic_hidden_retry
    
    label logic_hidden_cooking:
        if not ("tuki" in persistent.endings or "sora" in persistent.endings):
            jump logic_hidden_retry
        menu:
            "月" if "tuki" in persistent.endings:
                window hide
                call hidden_tuki from _call_hidden_tuki
                return
            "????" if "tuki" not in persistent.endings:
                jump logic_hidden_retry
            "空" if "sora" in persistent.endings:
                window hide
                call hidden_sora from _call_hidden_sora
                return
            "????" if "sora" not in persistent.endings:
                jump logic_hidden_retry
    
    label logic_hidden_supply:
        if not ("sakuya" in persistent.endings or "saburo" in persistent.endings):
            jump logic_hidden_retry
        menu:
            "作哉" if "sakuya" in persistent.endings:
                window hide
                call hidden_sakuya from _call_hidden_sakuya
                return
            "????" if "sakuya" not in persistent.endings:
                jump logic_hidden_retry
            "三朗" if "saburo" in persistent.endings:
                window hide
                call hidden_saburo from _call_hidden_saburo
                return
            "????" if "saburo" not in persistent.endings:
                jump logic_hidden_retry

    label logic_hidden_retry:
        call hidden_nori from _call_hidden_nori
        jump logic_hidden_choice

    return

## 随机事件逻辑 ##########################################################

label logic_random_event:
    python:
        random_event_id_old = random_event_id
        while random_event_id_old == random_event_id:
            random_event_id = renpy.random.randint(0, 18)
    
    call expression "random_event_" + str(random_event_id) from _call_expression_23
