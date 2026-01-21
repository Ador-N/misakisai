# -*- coding: utf-8 -*-
# Converted from 0000028A.lns

label event00:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg rooftop with dissolve
    show tomo 12 at topleft
    show tubasa 5 at topright with dissolve
    show tomo 38 with dissolve
    window show
    play sound "fx/eureka.ogg"
    tomo "翼君你其实，"
    extend "很好色对吧！"
    show tubasa 20 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tubasa "你突然在乱说些什么呀！"
    show tomo 3 with dissolve
    tomo "听说男孩子『那种事情』做多了，"
    extend "体毛就会很浓密哦。"
    show tubasa 10 with dissolve
    tubasa "哈、哈啊……。"
    show tomo 39 with dissolve
    tomo "……"
    extend "说起来，"
    extend "翼君的眉毛是真的很粗啊。"
    show tubasa 37 with dissolve
    tubasa "是、是这样吗……？"
    show tomo 2 with dissolve
    play sound "fx/impact_japanese.ogg"
    tomo "所以呀，"
    extend "肯定是这么回事啦！"
    show tubasa 7 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tubasa "这、这根本毫无关联吧！！"
    window hide
    hide tomo
    hide tubasa
    with dissolve
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event01:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg classroom with dissolve
    show sinobu 2 at top with dissolve
    window show
    sinobu "友，下节课要换教室了……。"
    hide sinobu with dissolve
    show tomo 3 at top with dissolve
    tomo "……Zzz……Zzz"
    hide tomo with dissolve
    show sinobu 4 at top with dissolve
    sinobu "诶，居然睡着了……。"
    show sinobu 22 with dissolve
    extend "\n真是的，睡得还挺香啊……。"
    hide sinobu with dissolve
    show tomo 31 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tomo "啊……啊嗯……那里那里哦哦哦……。"
    extend "\n电摩棒好舒服……唔呜呜。"
    hide sinobu
    hide tomo
    with dissolve
    show tomo 31 at topleft
    show sinobu 19 at topright with dissolve
    sinobu "……。"
    play sound "fx/punch2.ogg"
    show cg remarkable at top with FadeWhite(0.5)
    "（咻啪！）"
    hide tomo
    hide sinobu
    hide cg
    with dissolve
    show sinobu 6 at topright
    show tomo 20 at topleft with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tomo "呜呀！！"
    sinobu "别在学校里发情啊。"
    window hide
    hide sinobu
    hide tomo
    with dissolve
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event02:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg washroom with dissolve
    show sintarou 3 at topright
    show tuki 17 at topleft
    show sora 2 at top with dissolve
    show sintarou 1 with dissolve
    window show
    sintarou "哎呀~月的身材还是一如既往的好啊。\n肌肉相当结实，真棒啊~。"
    show tuki 1 with dissolve
    tuki "啊，多谢夸奖。"
    show sora 34 with dissolve
    sora "那是当然的，哥哥可是剑道部的王牌主将呢！"
    extend "\n他每天都在坚持锻炼肌肉哦。"
    show sintarou 12 with dissolve
    sintarou "既然如此……"
    play sound "fx/eureka.ogg"
    extend "想必晚上也会很激烈吧~。"
    extend "\n哎呀~真想偷窥一次啊。"
    show sora 15 with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sora "你、你你你你在胡说什么呢，真是的！\n怎么可能会有那种事……"
    show tuki 29 with dissolve
    play sound "fx/impact.ogg"
    tuki "嗯……你是怎么知道的，奥村。"
    extend "\n难道说，你偷窥过……？"
    play sound "fx/explosion2.ogg"
    show cg hallway at center with FadeWhite(0.5)
    hide bg
    hide sintarou
    hide tuki
    hide sora
    $ renpy.transition(Quake(0, 70, 0.15, 0.1), layer='master')
    sora "喂！哥、哥哥啊啊啊啊！！"
    window hide
    hide tuki
    hide cg
    hide sora
    hide sintarou
    with dissolve
    show bg washroom at center
    show sintarou 31 at top with dissolve
    window show
    sintarou "（贼笑）"
    window hide
    hide sintarou
    hide tuki
    hide sora
    with dissolve
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event03:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg classroom with dissolve
    show sintarou 25 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    window show
    sintarou "那么，各位！！"
    extend "\n说到夜晚的伴侣，你想到的是什么！！？"
    window hide
    hide sintarou with dissolve
    show bg remarkable
    show tomo 13 at top with dissolve
    play sound "fx/impact.ogg"
    window show
    tomo "飞机杯！"
    window hide
    show sintarou 7 at topright with dissolve
    play sound "fx/impact.ogg"
    window show
    sintarou "自慰器！！"
    window hide
    show tuki 7 at topleft with dissolve
    play sound "fx/impact_japanese.ogg"
    window show
    tuki "空的○○○！！！"
    window hide
    hide sintarou
    hide tomo
    hide tuki
    with dissolve
    show bg classroom
    show tomo 21 at top with dissolve
    window show
    play sound "fx/boing.ogg"
    tomo "老师！"
    extend "\n请问○○○也能算作伴侣吗？"
    show sintarou 9 at topright with dissolve
    play sound "fx/triangle.ogg"
    sintarou "唔。"
    extend "\n是个相当深奥的难题呐……。"
    show tuki 18 at topleft with dissolve
    play sound "fx/eureka.ogg"
    tuki "你们俩还在依赖玩具，还是太嫩了啊。"
    window hide
    hide sintarou
    hide tomo
    hide tuki
    with dissolve
    show sora 7 at topleft with dissolve
    window show
    sora "……今天是扔可燃垃圾的日子吧？"
    extend "\n得去准备三个特大号垃圾袋才行……。"
    show sinobu 7 at topright with dissolve
    sinobu "我也来帮忙。"
    window hide
    hide sora
    hide sinobu
    with dissolve
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event04:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg cafeteria with dissolve
    show tomo 12 at topright
    show tubasa 5 at topleft with dissolve
    show tomo 3 with dissolve
    window show
    tomo "（咕嘟……咕嘟……）"
    show tomo 4 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    extend "\n噗哈——！！\n可乐真好喝呀☆"
    show tubasa 11 with dissolve
    tubasa "（友君今天也很可爱呢……。）"
    show tomo 1 with dissolve
    tomo "啊，翼君也想喝一口吗~？"
    show tubasa 8 with dissolve
    tubasa "诶？那个……这个……。"
    hide tomo
    hide tubasa
    with dissolve
    play sound "fx/sparkle.ogg"
    show cg blue at center
    show tubasa 24 at top with Radial(0.5)
    tubasa "（啊！！这是能和友君间接接吻的机会！！"
    show tubasa 7 with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    extend "\n但、但是我又喝不了碳酸饮料……。"
    show tubasa 6 with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    extend "\n呜、呜呜呜……怎么办怎么办。"
    show tubasa 29 with dissolve
    extend "\n……不行，我也是个男人。"
    show tubasa 16 with dissolve
    extend "只要去做……"
    play sound "fx/impact.ogg"
    extend "就一定能做到！！）"
    window hide
    hide cg
    hide tubasa
    with dissolve
    show tubasa 18 at top with dissolve
    play sound "fx/eureka.ogg"
    window show
    tubasa "那、那我就开动了！！"
    show tubasa 7 with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/dash.ogg"
    extend "\n呜！？"
    hide tomo
    hide tubasa
    with dissolve
    show tubasa 9 at topleft with dissolve
    tubasa "噗……咳咳！"
    show tomo 18 at topright with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tomo "翼、翼君，你没事吧！？"
    window hide
    hide tomo
    hide tubasa
    with dissolve
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event05:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg school_backside with dissolve
    show sora 8 at top with dissolve
    window show
    sora "……。"
    window hide
    play sound "fx/boing.ogg"
    show cg c102 at center with Radial(0.5)
    window show
    "（嗡……嗡……）"
    window hide
    hide cg
    hide sora
    with dissolve
    show sora 9 at top with dissolve
    $ renpy.transition(Quake(30, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    window show
    sora "呜呜呜……有虫子在飞来飞去，没法过去啊啊啊……。"
    window hide
    hide sora with dissolve
    show bg gym_backside with dissolve
    show tubasa 7 at top with dissolve
    $ renpy.transition(Quake(30, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    window show
    tubasa "……。"
    window hide
    pause 0.4
    window show
    sora "啊……对面也有同样遭遇的人……！"
    extend "\n嗯嗯，我懂的。虫子这种东西真的很恐怖呢……。"
    window hide
    pause 0.4
    window show
    show tubasa 19 with dissolve
    tubasa "……"
    show tubasa 16 with dissolve
    play sound "fx/eureka.ogg"
    extend "嘿！！"
    play sound "fx/running.ogg"
    window hide
    hide tubasa with dissolve
    window show
    sora "呜、呜哇，那孩子是打算穿过去啊！"
    extend "\n真有勇气啊……。"
    window hide
    show bg school_backside with dissolve
    show sora 8 at top with dissolve
    window show
    sora "诶……那是！？"
    extend "\n等、等等，虫子们飞过来了！！？"
    extend "\n那、那孩子朝这边冲过来了，也就是说……！！"
    window hide
    play sound "fx/boing.ogg"
    show cg c102 at center with Radial(0.5)
    window show
    "（嗡~嗡~！！！！）"
    window hide
    hide cg
    hide tubasa
    hide sora
    with dissolve
    show cg remarkable at center
    show tubasa 7 at topright
    show sora 16 at topleft with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    window show
    sora "为什么会变成这样啊啊啊！！！"
    tubasa "对、对不起啊啊啊啊！！！"
    window hide
    hide sora
    hide tubasa
    hide cg
    with dissolve
    play sound "fx/running.ogg"
    pause 0.6
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event06:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg classroom with dissolve
    show tomo 12 at topleft
    show sintarou 3 at topright with dissolve
    show sintarou 29 with dissolve
    window show
    sintarou "我昨晚，认真学习了来着~。"
    show tomo 3 with dissolve
    tomo "诶~。\n光是听到慎酱会学习这一点，就很让人吃惊了。"
    show sintarou 23 with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sintarou "你这家伙，若无其事地说了很过分的话啊……。"
    show sintarou 16 with dissolve
    sintarou "然后呢，学到一半遇到了不认识的汉字就去翻字典。"
    show sintarou 4 with dissolve
    extend "\n结果翻着翻着，就开始不停地查起各种色情的词了。"
    show tomo 11 with dissolve
    play sound "fx/eureka.ogg"
    tomo "啊~确实确实！"
    play sound "fx/cute.ogg"
    extend "\n比如阴○啊，"
    play sound "fx/cute2.ogg"
    extend "勃○啊，"
    play sound "fx/wow2.ogg"
    extend "射○啊，"
    extend "这类词语对吧？"
    show sintarou 5 with dissolve
    play sound "fx/cute2.ogg"
    sintarou "没错没错♪"
    show sintarou 29 with dissolve
    extend "\n然后，就变得越来越兴奋，\n最后完全没法集中注意力，直接进入飞机杯咻咻的时间。"
    show tomo 6 with dissolve
    tomo "对对对，我太懂了~！"
    extend "\n我的话，就不是咻咻，而是嗡嗡呢~。"
    window hide
    hide tomo
    hide sintarou
    hide bg
    with dissolve
    show bg classroom at center
    show sora 12 at top with Dissolve(0.8)
    window show
    sintarou "嗡嗡是什么声音啊~。"
    tomo "当然是电摩啦！"
    window hide
    show sora 20 with dissolve
    play sound "fx/triangle.ogg"
    window show
    sora "……"
    extend "是该吐槽，还是不该吐槽呢……。"
    window hide
    hide sora with dissolve
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event07:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg schoolyard with dissolve
    show tomo 12 at topleft
    show tubasa 5 at topright with dissolve
    show tomo 21 with dissolve
    window show
    tomo "感觉咱们学校，各种地方都很老派啊。"
    extend "\n制服是诘襟，泳衣是三角裤。"
    show tomo 24 with dissolve
    extend "\n不过，我倒觉得这种穿起来更舒服！"
    show tubasa 4 with dissolve
    tubasa "确实呢。"
    extend "\n我也觉得，这种款式的……看着挺不错的……。"
    show tubasa 11 with dissolve
    play sound "fx/cute2.ogg"
    extend "\n仅限友君的话。"
    window hide
    hide tomo
    hide tubasa
    with dissolve
    show sintarou 9 at top with dissolve
    window show
    play sound "fx/eureka.ogg"
    sintarou "我们学校的泳裤之所以采用这种三角裤，\n是因为校长大人有这方面的特殊癖好哟。"
    show tomo 28 at topleft
    show tubasa 17 at topright with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tubasa "奥、奥村君！"
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tomo "慎酱，这是真的吗！？"
    show sintarou 8 with dissolve
    sintarou "嗯！"
    extend "\n校长以前来过我家的澡堂，\n那时咱就听说了很多『内幕』~。"
    show tomo 11 with dissolve
    play sound "fx/cute2.ogg"
    tomo "快、快给我详细讲讲！！！"
    play sound "fx/sparkle.ogg"
    show 効果ＣＧ adult at center with FadeWhite(0.5)
    sintarou "哎呀呀~。"
    extend "\n当时咱体贴地问了句『要不要帮您搓个背呀？』"
    extend "结果一来二去的，\n气氛越洗越火热呢。"
    play sound "fx/impact_japanese.ogg"
    tomo "唔噢噢噢噢！！不愧是慎酱！手艺高超啊~♪"
    sintarou "然后，是校长先彻底放飞自我，\n直接朝咱扑了过来哟。"
    play sound "fx/cute3.ogg"
    tubasa "……啊呜啊呜。"
    hide 効果ＣＧ
    hide tomo
    hide tubasa
    hide sintarou
    with dissolve
    show tomo 6 at top with dissolve
    tomo "好厉害~。我们的校长还真行啊……。"
    show tomo 11 with dissolve
    play sound "fx/wow2.ogg"
    extend "\n然后呢然后呢，后来怎么样了！？"
    hide tomo
    hide tubasa
    with dissolve
    show tomo 25 at topleft
    show tubasa 3 at topright with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tubasa "友、友君！这种故事不能听下去啦！！"
    extend "\n友君会变脏的呜呜呜呜！！"
    show sintarou 29 at top with dissolve
    sintarou "没事没事，一之濑同学。\n他已经脏得不能再脏了哦？"
    show tubasa 7 with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tubasa "总之就是不可以——！！！"
    window hide
    hide tomo
    hide tubasa
    hide sintarou
    with dissolve
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event08:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg cafeteria with dissolve
    show tuki 1 at topleft
    show sora 2 at topright with dissolve
    show sora 26 with dissolve
    window show
    sora "最近车站前新开了一家看起来很好吃的芭菲店哦~。"
    show sora 14 with dissolve
    extend "\n但是，店面装修得太豪华了，总觉得不太好意思进去啊。"
    show tuki 5 with dissolve
    tuki "这样啊。"
    show sora 25 with dissolve
    sora "这种时候就会不禁想『如果我是女孩子就好了』。"
    extend "\n毕竟男生一个人进那种店，果然还是会不好意思啊。"
    show tuki 3 with dissolve
    tuki "……。"
    hide tuki
    hide sora
    with dissolve
    play sound "fx/sparkle.ogg"
    show cg adult at center
    show tuki 4 at top with Radial(0.5)
    extend "如果空是女生的话，现在一定连孩子都有了吧……。"
    hide tuki
    hide sora
    hide cg
    with dissolve
    show sora 17 at top with dissolve
    play sound "fx/dash.ogg"
    sora "变——————态！！！"
    hide sora with dissolve
    play sound "fx/shock.ogg"
    show cg dark at center
    show tuki 13 at top with Dissolve(0.3)
    tuki "（受打击！）"
    hide sora
    hide tuki
    hide cg
    with dissolve
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label event09:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg classroom with dissolve
    show saburo 1 at top with dissolve
    show saburo 5 with dissolve
    window show
    saburo "穗海~"
    hide sakuya
    hide saburo
    with dissolve
    show sakuya 19 at top with dissolve
    sakuya "……Zzz……Zzz"
    hide sakuya with dissolve
    show saburo 4 at top with dissolve
    saburo "诶，怎么睡着了啊~？"
    extend "\n我肚子饿了，一起去食堂吧~↑"
    hide saburo with dissolve
    show saburo 1 at topright
    show sakuya 25 at topleft with dissolve
    sakuya "嗯……啊，知道了……等一下……。"
    window hide
    hide saburo
    hide sakuya
    with dissolve
    show sakuya 19 at top with dissolve
    window show
    play sound "fx/boing.ogg"
    sakuya "（嗯……？下半身感觉不对劲……。）"
    play sound "fx/sparkle.ogg"
    show cg adult at center
    show sakuya 32 with Radial(0.5)
    sakuya "……啊。"
    window hide
    hide sakuya
    hide cg
    with dissolve
    show saburo 5 at topright with dissolve
    window show
    saburo "嗯？怎么了~穗海。"
    show sakuya 12 at topleft with dissolve
    sakuya "……我还是算了。你自己去吧。"
    show saburo 8 with dissolve
    saburo "哈啊？搞什么啊！"
    extend "\n快点走啊~。"
    show sakuya 27 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/dash.ogg"
    sakuya "吵死了笨蛋！呆子！！废物！！！"
    show saburo 3 with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    saburo "嘴好毒！！好可怕！！"
    window hide
    hide saburo
    hide sakuya
    with dissolve
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event10:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg classroom with dissolve
    show tomo 12 at topleft
    show sinobu 1 at topright with dissolve
    show tomo 7 with dissolve
    window show
    tomo "忍~。"
    extend "\n能教教我这道题怎么做吗？"
    show sinobu 7 with dissolve
    sinobu "嗯，可以啊。"
    extend "\n我看看……这里要把右边的项进行移项，然后代入求根公式……。"
    window hide
    play music "fx/footsteps.ogg"
    hide tomo
    hide sinobu
    hide bg
    with dissolve
    window show
    "…"
    window hide
    stop music fadeout 1.0
    show bg classroom at center with dissolve
    show sinobu 2 at topright with dissolve
    window show
    sinobu "……所以结果是0.721。"
    show tomo 24 at topleft with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tomo "原来如此！！非常感谢！"
    play sound "fx/running.ogg"
    hide tomo with dissolve
    window hide
    hide sinobu with dissolve
    show sinobu 22 at top with dissolve
    window show
    sinobu "（友上次期末考试不及格，是不是重新认识到了学习的重要性呢？"
    show sinobu 21 with dissolve
    extend "\n难得见他这么用功，\n我得尽可能多帮帮他才行。）"
    window hide
    hide sinobu with dissolve
    show tomo 39 at topright with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    window show
    tomo "这样一来，终于能进那个神秘里站了呢，老板。"
    show sintarou 13 at topleft with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sintarou "干得漂亮友亲！！"
    extend "\n最近那些网站不光是会隐藏链接，\n搞这种登录问题的情况也越来越多了啊。"
    extend "\n真是麻烦啊。"
    show tomo 31 with dissolve
    tomo "不过~正是因为有这种重重阻碍，\n成功潜入时的那种成就感才更强烈，里面的内容也更有看头了呢~。"
    show sintarou 12 with dissolve
    sintarou "没错没错！"
    extend "\n你也懂行了啊！！"
    extend "\n友亲，免许皆传！"
    window hide
    hide tomo
    hide sintarou
    with dissolve
    show sinobu 13 at top with dissolve
    window show
    play sound "fx/triangle.ogg"
    sinobu "……。"
    hide sinobu with dissolve
    show tomo 31 at topright
    show sintarou 12 at topleft with dissolve
    show sinobu 25 at top with dissolve
    show cg dark at center
    play sound "fx/impact.ogg"
    sinobu "你们两个……跟我去楼顶一趟。"
    show tomo 30
    show sintarou 21 with dissolve
    play sound "fx/cute2.ogg"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    "友＆慎太郎" "咿！！？"
    window hide
    hide tomo
    hide sinobu
    hide sintarou
    hide cg
    with dissolve
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event11:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg c103 with Radial(0.5)
    play sound "fx/tadaa.ogg"
    window show
    tomo "铛铛——！"
    sora "友君，你的头发是怎么回事！"
    extend "\n变得好直！"
    tomo "哼哼~。"
    extend "\n隔壁班有个带了卷发棒的家伙，\n我刚才借来用了一下！"
    extend "\n很厉害吧！"
    sintarou "嚯~。"
    extend "\n只是把头发拉直而已，感觉整个人的形象都变了！"
    window hide
    hide bg with dissolve
    pause 0.5
    play music "fx/rain.ogg"
    show bg rain at center with FadeWhite(0.6)
    window show
    sora "啊，开始下雨了。"
    extend "\n而且，雨势还挺大的。"
    sintarou "真的呢~。"
    extend "\n不过，肯定是阵雨啦。"
    extend "\n毕竟天气预报说今天一整天都是晴天。"
    window hide
    stop music fadeout 1.0
    hide bg with Dissolve(0.6)
    window show
    "…"
    window hide
    play sound "fx/tsubame.ogg"
    show bg sky at center with Radial(0.5)
    pause 0.6
    stop sound fadeout 1.0
    show bg classroom with dissolve
    show sora 2 at topright with dissolve
    window show
    sora "天气放晴了呢……。"
    show sintarou 31 at topleft with dissolve
    sintarou "是啊~。"
    extend "\n不过……。"
    show sora 20
    show sintarou 16 with dissolve
    sora "结果还是……"
    sintarou "恢复原状……。"
    window hide
    hide sora
    hide sintarou
    with dissolve
    show tomo 9 at top with Dissolve(0.8)
    play sound "fx/triangle.ogg"
    window show
    tomo "呜呜呜……。"
    window hide
    hide sora
    hide sintarou
    hide tomo
    with Dissolve(0.7)
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event12:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg hallway with dissolve
    show tomo 12 at top with dissolve
    window show
    tomo "~♪"
    hide tomo with dissolve
    show saburo 20 at top with Dissolve(0.75)
    saburo "（好在意……。"
    extend "\n无论如何都很在意……！）"
    play sound "fx/eureka.ogg"
    show cg c104 1 at center with FadeWhite(0.5)
    saburo "（那家伙的呆毛！从以前开始就一直很在意！"
    extend "\n怎么说呢，好想……好想摸一摸，又想揪一下……！"
    extend "\n这样盯着看的话，"
    play sound "fx/sparkle.ogg"
    show cg c104 2 with Radial(0.65)
    extend "还会忍不住想要扑上去！！"
    extend "\n这股冲动，是怎么回事啊……！）"
    play sound "fx/boing.ogg"
    saburo "（啊，不行不行……我在想什么啊！"
    extend "\n那家伙是穗海的心上人啊！！"
    extend "\n敢对他出手的话，"
    play sound "fx/knife.ogg"
    extend "那可是要被锯断脑袋、开膛破肚的重罪啊！"
    play sound "fx/explosion2.ogg"
    extend "\n给我压住，压制住我的本能！！！给我忍住啊啊啊啊！！！！）"
    window hide
    hide cg
    hide saburo
    with dissolve
    show sakuya 26 at topleft with dissolve
    window show
    sakuya "喂，猫山……你从刚才开始就喘得厉害啊。"
    extend "\n怎么了？"
    show saburo 14 at topright with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    saburo "穗、穗海……我会忍住的……。"
    extend "\n绝不会背叛我们的友情……！"
    show sakuya 11 with dissolve
    sakuya "啊？"
    window hide
    hide saburo
    hide sakuya
    with dissolve
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event13:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg hallway with dissolve
    show sakuya 20 at topleft
    show tomo 28 at topright with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/dash.ogg"
    window show
    "（咚）"
    show sakuya 6 with dissolve
    sakuya "好痛。"
    show tomo 7 with dissolve
    tomo "啊，对、对不起。"
    show sakuya 2 with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sakuya "你这笨蛋！"
    extend "\n眼睛长哪去了！走路不看路吗！！"
    extend "\n都是因为你，害我肩膀都撞疼了！\n赶紧把医药费交出来！！"
    show tomo 5 with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tomo "我、我不是道过歉了吗！"
    extend "\n你才是，我要告你诽谤，让你赔我精神损失费，你这家伙！"
    show sakuya 20 with dissolve
    sakuya "切……你这种家伙有什么名誉可言啊！！"
    show sakuya 2 with dissolve
    extend "\n既然你这个态度，那我们法庭见！"
    extend "\n记得找个好律师啊混蛋！！"
    window hide
    hide sakuya
    hide tomo
    with dissolve
    window show
    play sound "fx/wind_slash.ogg"
    sinobu "……那就不必了。"
    window hide
    play sound "fx/impact.ogg"
    show cg c105 at center with FadeWhite(0.5)
    window show
    "（啪嚓！）"
    play sound "fx/entrance.ogg"
    "『铁·"
    play sound "fx/entrance.ogg"
    extend "拳·"
    play sound "fx/entrance.ogg"
    extend "制·"
    play sound "fx/entrance.ogg"
    extend "裁！！！』」"
    play sound "fx/impact_japanese.ogg"
    window hide
    hide tomo
    hide cg
    hide sakuya
    with dissolve
    show sinobu 24 at top with dissolve
    window show
    sinobu "判决已下。"
    extend "\n现在宣布闭庭。"
    window hide
    hide sinobu with dissolve
    window show
    play sound "fx/ding.ogg"
    sakuya "呜呜呜……。"
    show tomo 26 at topright with dissolve
    tomo "这……这样会不会太可怜了……。"
    window hide
    stop sound fadeout 1.0
    hide tomo with dissolve
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event14:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg hallway with dissolve
    show tubasa 31 at top with dissolve
    window show
    tubasa "啊……是友君。"
    window hide
    play sound "fx/sparkle.ogg"
    show cg c34 2 at center with Radial(0.5)
    window show
    tubasa "在他身边的是，绫濑君……"
    extend "\n……真好啊，绫濑君。"
    extend "\n总是能和友君待在一起……。"
    window hide
    hide bg
    hide tubasa
    hide cg
    with dissolve
    play sound "fx/heartbeat.ogg"
    show bg dark at center
    show tubasa 38 at top with Dissolve(0.9)
    window show
    tubasa "………………………。"
    stop sound fadeout 1.0
    show bg hallway
    play sound "fx/triangle.ogg"
    show tubasa 21 with dissolve
    tubasa "咦、咦……糟糕，我真是的。\n刚才好像在想很不好的事……。"
    extend "\n啊呜呜呜呜……以后得多注意才行……。"
    window hide
    hide tubasa with Dissolve(0.7)
    stop music fadeout 1.0
    hide bg with Dissolve(0.8)
    return

label event15:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg classroom with dissolve
    show sintarou 3 at topright
    show tomo 12 at topleft
    show sora 2 at top with dissolve
    show tomo 21 with dissolve
    window show
    tomo "说起来，空你们几个的生日是什么时候来着~？"
    show sora 26 with dissolve
    sora "是6月9日哦。\n我们不仅是双胞胎，还刚好是双子座呢。"
    show sora 3 with dissolve
    extend "\n而且6和9的数字形状还是正对的哦~。"
    window hide
    hide sintarou
    hide tomo
    hide sora
    with dissolve
    show tomo 15 at topleft with dissolve
    window show
    tomo "6和……"
    show sintarou 19 at topright with dissolve
    sintarou "9……。"
    show cg remarkable at center
    show sintarou 6
    show tomo 13 with dissolve
    play sound "fx/tadaa.ogg"
    tomo_and_shin "69！！！"
    play sound "fx/wow2.ogg"
    show cg adult
    show tomo 17
    show sintarou 7 with dissolve
    tomo_and_shin "69，69，69~♪"
    window hide
    hide sintarou
    hide tomo
    hide cg
    with dissolve
    show tuki 2 at topleft
    show sora 15 at topright with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    window show
    sora "哥、哥哥！快想想办法啊~！！"
    show tuki 9 with dissolve
    tuki "啊，回家以后试试吧。"
    show sora 16 with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    sora "笨蛋啊啊啊啊啊啊啊啊啊啊啊！！！！！！"
    window hide
    hide sora
    hide tuki
    with Dissolve(0.7)
    stop music fadeout 1.0
    hide bg with Dissolve(0.7)
    return

label event16:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg washroom with dissolve
    show sakuya 12 at top with dissolve
    window show
    sakuya "……真是的，上个厕所也太久了吧。"
    extend "\n我也想上，能不能快点啊……。"
    hide sakuya with dissolve
    play sound "fx/door_open.ogg"
    "（咔嚓）"
    window hide
    show tomo 6 at top with dissolve
    window show
    tomo "……呼。清爽了！"
    hide tomo with dissolve
    show sakuya 8 at topright with dissolve
    sakuya "呃，是你啊……。"
    show tomo 28 at topleft with dissolve
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    tomo "呃！技安！！"
    show tomo 31 with dissolve
    extend "\n我、我先走一步了~！"
    hide tomo
    hide sakuya
    with dissolve
    show sakuya 19 at top with dissolve
    sakuya "……虽然不太想用这家伙刚用过的隔间，但也没办法……。"
    window hide
    hide sakuya with dissolve
    play sound "fx/door_open.ogg"
    show bg private_toilet with Radial(0.5)
    window show
    sakuya "嗯……？"
    extend "\n这股味道……还有这张纸巾的湿度……。"
    show bg dark
    show sakuya 29 at top with dissolve
    play sound "fx/shock.ogg"
    sakuya "那家伙刚才绝对！绝对做了！！"
    window hide
    hide sakuya with dissolve
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event17:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg pool with dissolve
    show saburo 16m at top with dissolve
    window show
    saburo "唉……我最讨厌游泳课了……。"
    extend "\n我们猫山家的人，世世代代都不擅长应付水和狗啊……。"
    show saburo 15m with dissolve
    extend "\n呜呜呜……。"
    hide saburo with dissolve
    show sakuya 31m at top with dissolve
    sakuya "……。"
    hide saburo
    hide sakuya
    with dissolve
    show saburo 12m at topright
    show sakuya 37m at topleft with dissolve
    $ renpy.transition(Quake(30, 0, 0.1, 0.15), layer='master')
    play sound "fx/dash.ogg"
    sakuya "看招。"
    $ renpy.transition(Quake(0, 80, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    saburo "喵啊！！！"
    hide saburo with dissolve
    play sound "fx/dive.ogg"
    "（啪！）"
    hide sakuya with dissolve
    window hide
    show sakuya 3m at top with dissolve
    window show
    sakuya "诶~。\n明明是只猫却擅长狗刨啊。"
    play sound "FX/可愛い2.ogg"
    saburo "你、你！！我一定要收拾你啊啊啊！！！"
    window hide
    hide sakuya with dissolve
    stop music fadeout 1.0
    hide bg with dissolve
    return

label event18:
    show bg school_building_full at center with Radial(0.8)
    play music "yonkoma.ogg"
    pause 0.6
    show bg classroom with dissolve
    show tomo 12 at topleft
    show sinobu 2 at top
    show sintarou 3 at topright with dissolve
    show sintarou 4 with dissolve
    window show
    sintarou "忍同学~。"
    extend "\n我想拍一张你的照片，双手比出『耶』的手势来一张嘛~。"
    show tomo 4 with dissolve
    tomo "忍~要有笑容！笑容啊~！！"
    show sinobu 27 with dissolve
    sinobu "……。"
    window hide
    play sound "fx/sparkle.ogg"
    show cg c106 1 at center with Radial(0.7)
    window show
    tomo "忍，笑得再灿烂一点！"
    extend "\n来嘛，笑一个笑一个！"
    extend "\n你只要肯做就一定能行的！"
    sintarou "嘴巴能不能再张开一点点？"
    show cg c106 2 with Dissolve(0.7)
    extend "\n对对，就是这种感觉！"
    sinobu "……。"
    play sound "fx/eureka.ogg"
    tomo "啊！！\n忍的头顶上方，出现『电摩战队城市英雄』的玩偶了！！！"
    sinobu "？"
    window hide
    hide tomo
    hide sinobu
    hide sintarou
    hide cg
    hide bg
    with dissolve
    window show
    "（咔嚓）"
    window hide
    show bg classroom at center with Dissolve(0.6)
    show tomo 8 at topleft
    show sintarou 23 at topright with dissolve
    window show
    play sound "fx/triangle.ogg"
    sintarou "这、这是……。"
    tomo "拍、拍到不得了的东西了……。"
    show sinobu 2 at top with dissolve
    sinobu "怎么回事……？"
    window hide
    hide tomo
    hide sinobu
    hide sintarou
    with Dissolve(0.7)
    stop music fadeout 1.0
    hide bg with Dissolve(0.8)
    return