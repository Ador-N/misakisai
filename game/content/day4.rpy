# -*- coding: utf-8 -*-
# Converted from 0000023D.lns

label day4:
    window show
    "就这样，我们用三天时间完成了执行委员的工作，"
    extend "\n之后的剩余时间，就与全班同学一起投入到各项准备中。"
    window hide
    show bg sky at center with Radial(0.8)
    play sound "fx/entrance.ogg"
    window show
    "然后，到了御咲祭当天——"
    window hide
    play sound "fx/crowd_noise.ogg"
    play music "school_festival.ogg"
    show bg school_building_full with FadeWhite(1.0)
    pause 0.6
    show bg hallway with Dissolve(1.0)
    pause 0.5
    play sound "fx/sparkle.ogg"
    show bg cafe with Radial(1.0)
    pause 0.4
    show tomo 13i at topright with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    window show
    tomo "好——大家！"
    extend "\n今天就玩个痛快吧！！！"
    show sintarou 4i at topleft with dissolve
    sintarou "这种时候，不如咱们拿出点气势，大家一起组个圆阵怎么样？"
    show sakuya 1i at top with dissolve
    sakuya "我才不要，丢死人了。"
    extend "\n不这么做也行的吧。"
    hide sintarou with dissolve
    show saburo 2i at topleft with dissolve
    saburo "事到如今你还害羞个什么劲儿啊。"
    show saburo 10i with dissolve
    extend "\n都围成『圆阵』了，那不正好把『引擎』发动起来吗？\n（注：『圆阵』读作Enjin，『引擎』读作Engine）"
    hide tomo with dissolve
    show tuki 18i at topright with dissolve
    tuki "说得对。\n大家毕竟是并肩作战到现在的战友。"
    show tuki 4i with dissolve
    extend "\n倒不如说，我们应该为此感到自豪。"
    hide sakuya with dissolve
    show sora 1i at top with dissolve
    sora "诶嘿嘿。\n有种正值青春的感觉呢。"
    hide tuki with dissolve
    show tubasa 4i at topright with dissolve
    tubasa "我、我还是第一次做这种事……。"
    hide saburo with dissolve
    show sinobu 20i at topleft with dissolve
    sinobu "……各位能稍微弯下腰的话就更好了。"
    hide sora with dissolve
    hide tubasa with dissolve
    hide sinobu with dissolve
    return

label day4_1:
    show tomo 17i at top with dissolve
    window show
    tomo "准备好咯——一、二！"
    window hide
    play sound "fx/impact.ogg"
    show cg c18 at center with Radial(0.6)
    window show
    everyone "『诶——诶——哦！！！』"
    window hide
    hide tomo with dissolve
    hide cg with dissolve
    hide bg with dissolve
    play sound "fx/crowd_noise.ogg"
    show bg cafe at center with Radial(0.8)
    show sora 3i at topleft with dissolve
    window show
    sora "让您久等了。\n这是您点的可乐和巧克力圣代。"
    show sora 11i with dissolve
    extend "\n请慢慢享用。"
    hide sora with dissolve
    show sintarou 1i at topright with dissolve
    sintarou "好嘞，欢迎光临~！"
    show sintarou 4i with dissolve
    extend "\n来，快请进快请进，坐这边。\n我现在就给您端凉水过来哦~。"
    hide sintarou with dissolve
    show sinobu 5i at topleft with dissolve
    sinobu "客人，非常抱歉，校内禁止吸烟。"
    show sinobu 3i with dissolve
    extend "\n吸烟区请出教学楼右转……。"
    hide sinobu with dissolve
    show tubasa 8i at topright with dissolve
    tubasa "呃，那个……一共是六百日元。"
    show tubasa 1i with dissolve
    extend "\n一、二、三……嗯，正好六百元。"
    show tubasa 9i with dissolve
    extend "\n谢、谢谢惠顾。欢迎下次再来。"
    hide tubasa with dissolve
    "嗯嗯，大家都做得很好啊……。"
    window hide
    window show
    customer1 "那个~不好意思。"
    extend "\n我点的是热咖啡……。"
    show tomo 28i at topright with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tomo "啊……非常抱歉！"
    show tomo 19i with dissolve
    extend "\n我现在马上给您换！！请稍等！！"
    hide tomo with dissolve
    show tuki 29i at topleft with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    tuki "……糟糕。芭菲上的巧克力酱撒得太多了。"
    show tuki 10i with dissolve
    extend "\n又失败了。没办法，只好由我来把它解决掉了。"
    hide tuki with dissolve
    show saburo 12i at topright with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    saburo "咦？"
    show saburo 11i with dissolve
    extend "\n这一单是送到哪张桌子上的来着？"
    hide saburo with dissolve
    show sakuya 6i at top with dissolve
    sakuya "喏。你点的奶油水果蛋糕。"
    play sound "fx/boing.ogg"
    customer2 "感、感觉态度有点差啊……？"
    window hide
    hide sakuya with dissolve
    window show
    "……嘛，凡事不可能一帆风顺。"
    "哎呀~我也想当个客人啊。"
    extend "\n有这么多可爱的少年来迎接的咖啡店……。"
    extend "\n全世界肯定找不出第二家了。"
    play sound "fx/impact_japanese.ogg"
    "全世界的正太控们！来这里集合吧！！"
    extend "\n就在这家今日限定的咖啡店里！！"
    window hide
    hide bg with dissolve
    play sound "fx/crowd_noise.ogg"
    show bg cafe at center with Dissolve(1.0)
    window show
    customer3 "呜呼……！\n满、满是正太的咖啡店……！"
    play sound "fx/sparkle.ogg"
    extend "\n我、我要把持不住了……！！"
    customer4 "快看。"
    extend "\n那个孩子超~可爱的啊。"
    play sound "fx/wow2.ogg"
    extend "小小的屁股好·棒·啊♪"
    customer5 "这杯乌龙茶……该不会不小心混进了少年的唾液吧……？"
    play sound "fx/eureka.ogg"
    extend "\n如果是的话那就太棒了！！！"
    window hide
    window show
    play sound "fx/triangle.ogg"
    "……。"
    "不用说，他们已经来了。"
    play sound "fx/crowd_noise.ogg"
    show sora 12i at topleft with dissolve
    sora "小慎，聚在那边的客人，"
    extend "\n感觉气场有些不对劲……？"
    show sintarou 27i at topright with dissolve
    sintarou "啊——那些人啊。"
    extend "\n虽然都是我家澡堂的常客，"
    show sintarou 1i with dissolve
    extend "不过稍微有点『那个』倾向，所以还是不要靠近他们比较好哦~。"
    hide sora with dissolve
    hide sintarou with dissolve
    show saburo 12i at top with dissolve
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    saburo "咿！那些家伙还是来了吗！！"
    show saburo 11i with dissolve
    extend "\n我、我去厨房帮忙了~……。"
    play sound "fx/running.ogg"
    hide saburo with dissolve
    show sora 13i at topleft
    show tuki 5i at topright with dissolve
    tuki "奥村家的澡堂明明是个舒适安稳的地方，\n不敢想象竟然会有那种客人出没啊。"
    show sintarou 16i at top with dissolve
    sintarou "哎呀，总会有点这样那样的原因啦，某些日子可就没那么安稳了。"
    show sintarou 13i with dissolve
    extend "\n嘛，这事跟你们两位没什么关系，别放在心上啦~。"
    window hide
    hide sora with dissolve
    hide sintarou with dissolve
    hide tuki with dissolve
    window show
    student1 "[player_name]君——。"
    extend "\n如果你有空的话，能替一下猫山，\n去招呼2号桌的客人点单吗？"
    me "了解。"
    "不对，能像这样和他们一起工作，本身不就是很难得的体验吗？"
    play sound "fx/explosion3.ogg"
    "哇哈哈哈，你们这些正太控肯定羡慕死我啦！"
    extend "\n现在的我可是御咲学园的学生！"
    extend "\n作为经营咖啡店的一份子，我会加油的！！"
    stop music fadeout 2.0
    window hide
    hide bg with dissolve
    play music "infiltration.ogg"
    show bg cafe at center with Dissolve(1.0)
    window show
    play sound "fx/eureka.ogg"
    customer3 "哦。你也是个气质相当质朴的少年呢。"
    customer4 "嗯~虽然看起来平平无奇，不过这种风格也挺有味道的，不错呢。"
    play sound "fx/sparkle.ogg"
    customer5 "我、我反倒是对这种类型的更有感觉啊！！"
    show cg dark at center with Dissolve(0.3)
    play sound "fx/ding.ogg"
    "喂喂，饶了我吧。"
    extend "\n我必须得听这些家伙点单吗……！"
    "醉翁之意不在酒，而在小正太对吧！"
    extend "\n身为正太控的我，居然会被同为正太控的人盯上……。"
    extend "\n唔……简直毛骨悚然。"
    stop sound fadeout 0.5
    window hide
    hide cg with dissolve
    window show
    me "欢、欢迎光临。"
    extend "\n请、请问要点些什么？"
    play sound "fx/eureka.ogg"
    customer3 "吼~[player_name]，这是你的名字吧。"
    extend "\n真是个好名字呢。"
    "男人看着我的名牌说道。"
    play sound "fx/sparkle.ogg"
    customer4 "哎呀~看上去还挺青涩啊~？"
    extend "\n长着张纯朴的脸蛋呢♪"
    play sound "fx/impact_japanese.ogg"
    customer5 "好香！！有股少年的味道！！"
    extend "\n哈啊~真让人把持不住！"
    play sound "fx/shock.ogg"
    "呜……不、不要这样。"
    extend "\n不要用那种眼神看我啊啊啊！！！"
    me "那、那个，请各位下单……。"
    customer4 "哎呀~别那么着急嘛~。"
    customer3 "来嘛来嘛，对客人可要多多服务一下哦！"
    stop music fadeout 1.0
    show cg remarkable at center with Dissolve(0.3)
    play sound "fx/wind_slash.ogg"
    "（拽）"
    "男人拉着我的胳膊。"
    play sound "fx/boing.ogg"
    me "咿……！"
    window hide
    hide bg with dissolve
    hide cg with dissolve
    return

label day4_1_tomo:
    show tomo 4i at top with dissolve
    window show
    tomo "[player_name]君，我们一起加油吧！"
    me "噢！"
    hide tomo with dissolve
    return

label day4_1_sintarou:
    show sintarou 7i at top with dissolve
    window show
    sintarou "[player_name]酱，今天咱们就轰轰烈烈地大干一场吧~！"
    me "噢！"
    hide sintarou with dissolve
    return

label end_tomo:
    show bg cafe at center with dissolve
    play music "tomo_theme.ogg"
    show tomo 15i at top with dissolve
    window show
    tomo "好，暂停！到此为止！！"
    me "友！"
    customer3 "怎、怎么会这样捏！"
    show tomo 10i with dissolve
    tomo "这位客人。\n对店员动手动脚是违反规则的哦~。"
    show tomo 38i with dissolve
    extend "\n规则就是规则，大家得好好遵守，才能好好享受学园祭嘛！"
    show tomo 16i with dissolve
    extend "\n快点，把手松开。"
    play sound "fx/boing.ogg"
    customer3 "呜……抱、抱歉了捏。"
    extend "\n有、有点兴奋过头，所以有点不守规矩了捏。"
    play sound "fx/cute3.ogg"
    customer5 "对不起呀。"
    extend "\n在这里我们还是绅士一点，姑且忍耐一下，记住可远观不可亵玩焉。"
    play sound "fx/sparkle.ogg"
    customer4 "正义感爆棚的男孩子也超级迷人呢♪"
    window hide
    hide tomo with dissolve
    window show
    "在友的帮助下，我总算从那尴尬的境地中脱身了。"
    "没想到在这种时候，竟然被一个初中生搭救了……。"
    extend "\n总感觉有点丢人啊……。"
    window hide
    show tomo 7i at top with dissolve
    window show
    tomo "[player_name]君，你没事吧？"
    me "嗯、嗯。多亏了你，得救了。"
    extend "\n谢谢你！"
    show tomo 2i with dissolve
    tomo "嘿嘿！没什么啦。"
    show tomo 23i with dissolve
    tomo "……。"
    show tomo 8i with dissolve
    tomo "那、那个啊，[player_name]君。"
    extend "\n今晚的后夜祭，你有和谁约好一起了吗？"
    me "诶？不，还没有安排。"
    show tomo 33i with dissolve
    tomo "这样啊！"
    extend "\n那要不，和我一起逛？"
    me "好啊，那其他人呢？"
    show tomo 35i with dissolve
    tomo "呜……那个……我觉得我们两个人就好……。"
    "啊。"
    me "嗯，可以啊！"
    extend "\n那我们就在鞋柜那边碰头吧。"
    show tomo 34i with dissolve
    tomo "嗯、嗯！谢谢！"
    show tomo 31i with dissolve
    extend "\n那我先回岗位去了！\n待会儿见！"
    window hide
    play sound "fx/running.ogg"
    hide tomo with dissolve
    window show
    "友，已经整理好心情了吗？"
    "……。"
    play sound "fx/heartbeat.ogg"
    show cg yellow at center with dissolve
    "呜……总觉得心跳加速了……。"
    "嘛、嘛，反正还不知道待会儿他会跟我谈些什么，\n没必要那么紧张……"
    "不行，好不容易又有了独处的机会。"
    extend "\n就算他没有主动开口，我也要自己把话挑明。"
    hide cg with dissolve
    hide bg with dissolve
    stop music fadeout 2.0
    "……毕竟这个梦，不知道会持续到什么时候……。"
    window hide
    show bg cafe at center with dissolve
    show tubasa 14i at top with dissolve
    window show
    tubasa "……。"
    window hide
    hide tubasa with dissolve
    hide bg with dissolve
    play sound "fx/crowd_noise.ogg"
    show bg school_building_evening_full at center with Dissolve(1.0)
    pause 0.4
    show bg cafe_evening with Radial(1.0)
    window show
    "咖啡店的营业时间差不多要结束了。"
    extend "\n剩下的活动，就是和友的后夜祭！"
    extend "\n我可不能迟到了。得赶紧收拾完。"
    window hide
    play music "tubasa_theme.ogg"
    show tubasa 1i at top with dissolve
    window show
    tubasa "那个，[player_name]君，打扰一下……。"
    "在我忙活的时候，翼叫住了我。"
    me "抱歉。\n我现在有个很重要的约会。"
    extend "\n有什么事能晚点再说吗？"
    show tubasa 20i with dissolve
    tubasa "啊，那个，必须是现在才行。"
    show tubasa 3i with dissolve
    extend "\n拜托了。……不会占用你太多时间的。"
    "翼表现出了前所未有的固执。我实在没法推托，只好跟着他走了。"
    hide tubasa with dissolve
    hide bg with dissolve
    "虽然已经大概猜到他要说什么了……。"
    window hide
    show bg school_backside_evening with Dissolve(1.0)
    window show
    "翼带我去的地方，是教学楼的后方。"
    show tubasa 21i at top with dissolve
    tubasa "[player_name]君。"
    extend "\n那个……那个……。"
    me "冷静点。没事的。"
    extend "\n无论翼君问什么，我都会坦诚回答。"
    show tubasa 22i with dissolve
    stop music fadeout 2.0
    tubasa "好、好的……那么，我就单刀直入地问了。"
    "翼深吸了一口气，然后缓缓开口。"
    play music "serious.ogg"
    show tubasa 1i with dissolve
    tubasa "……你对友君，是怎么想的？"
    "来了。"
    me "……。"
    show tubasa 23i with dissolve
    tubasa "请你，坦诚回答我。"
    me "……我喜欢他。"
    extend "\n不是作为普通朋友，而是超越了那种层面的感情。"
    show tubasa 21i with dissolve
    tubasa "！！"
    show tubasa 1i with dissolve
    extend "\n……果然是这样。"
    show tubasa 22i with dissolve
    stop music fadeout 2.0
    extend "\n……你打算把这份心意告诉友君吗？"
    "翼在每一句话之间夹杂的那段『停顿』，都显得格外沉重。"
    me "是的。"
    extend "\n我打算在后夜祭上告诉他。"
    show tubasa 14i with dissolve
    tubasa "唔……。"
    play music "fx/wind.ogg"
    show bg school_backside_night with Dissolve(0.8)
    show tubasa 24i with dissolve
    extend "\n……绝对……不行。"
    me "……。"
    hide tubasa with dissolve
    show tubasa 25i at top with dissolve
    play sound "fx/eureka.ogg"
    tubasa "像[player_name]君这样的人……我是绝对不会把友君交给你的……！"
    stop music fadeout 2.0
    me "……所以，你打算怎么办？"
    window hide
    play sound "fx/wind_slash.ogg"
    show cg c19 1 at center with DefocusBlack(0.3)
    play music "pinch.ogg"
    window show
    tubasa "我要让[player_name]君，再也没法从这里离开半步！"
    "说着，翼把手中拿着的绳子展示给我看。"
    play sound "fx/boing.ogg"
    "喂、喂喂，不会吧……。"
    extend "\n他打算用绳子给我绑个龟甲缚，然后邀请我进入SM的世界。"
    "然后呢，"
    play sound "fx/sparkle.ogg"
    show cg adult with Radial(0.5)
    "\n再来一句『比起友君，我要让你变成我的俘虏！』\n之类的……。"
    show cg c19 2 with DefocusBlack(0.3)
    play sound "fx/eureka.ogg"
    tubasa "（盯着）"
    "怎么可能啊——！！"
    play sound "fx/explosion3.ogg"
    extend "\n那完全是『狩猎者』的眼神……。"
    me "翼、翼君，冷静点。先冷静下来。"
    extend "\n就算用暴力解决，情况也不会好转的。"
    extend "\n不要去拖对方的后腿，\n用别的方法去守护友吧。"
    show cg c19 3 with Dissolve(0.3)
    tubasa "别的方法……？"
    me "翼君也很喜欢友吧？\n这份心意，我光是看着你的眼神就能明白了。"
    extend "\n既然如此，你就应该把这份感情传达给他，\n努力让友的心向你靠拢才对啊！"
    show cg c19 4 with Dissolve(0.3)
    tubasa "请、请不要说得那么简单！！"
    tubasa "[player_name]君说的没错，\n友君他是我最重要的……这世界上最重要的人！"
    extend "\n正因如此，如果告白之后被拒绝了……"
    extend "\n我……我……！"
    window hide
    hide cg with dissolve
    hide tubasa with dissolve
    show tubasa 29i at top with dissolve
    window show
    tubasa "而且……我觉得……"
    extend "\n友君也一定很喜欢[player_name]君。"
    show tubasa 24i with dissolve
    tubasa "所以……只要[player_name]君不向友君表白的话，\n友君就一定……。"
    me "翼君，这你就错了。"
    show tubasa 29i with dissolve
    tubasa "诶……？"
    me "我明白的。"
    extend "\n我能感觉到，那孩子真正在追求的是什么。"
    show tubasa 28i with dissolve
    play sound "fx/dash.ogg"
    tubasa "那请你跟我解释清楚！！"
    extend "\n友君看着我和别人时的眼神，怎么会\n和看着[player_name]君的眼神不一样。"
    extend "\n请你解释给我听啊！！"
    show tubasa 29i with dissolve
    tubasa "我……我是明白的啊。"
    extend "\n光是看着那种眼神……就感觉心都要被挖走了……！"
    me "那是……"
    extend "\n不，不对！"
    me "你忘了那天早上，我们贴着耳朵说的话了吗？"
    show tubasa 25i with dissolve
    tubasa "那又能说明什么！？"
    extend "\n在我看来，[player_name]君的行为根本就是自相矛盾！"
    me "……。"
    me "翼君。\n在这之后，我要去向友表白。"
    extend "\n然后，我也必须回应他的感情。这是我必须要做的事！"
    window hide
    play sound "fx/wind_slash.ogg"
    show cg c19 4 at center with DefocusWhite(0.5)
    window show
    tubasa "我不准！！我绝不允许你做这种事！！！"
    me "友他……并不会因为这样就从翼君你们身边消失了。"
    extend "\n所以，让我去吧。"
    tubasa "……不……要。"
    stop music fadeout 2.5
    me "拜托了……让我去吧。求你了。"
    window hide
    hide cg with dissolve
    hide tubasa with dissolve
    show tubasa 27i at top with dissolve
    window show
    tubasa "不……要……呜、呜呜呜呜呜呜呜呜哇啊啊啊啊……。"
    hide tubasa with Dissolve(1.0)
    play sound "fx/fall_down.ogg"
    "翼终于彻底崩溃，放声大哭起来。"
    "梦，终究会醒来。"
    extend "\n一切都会变为没发生过的样子。"
    extend "\n在那之前……"
    play music "serious.ogg"
    me "让我去传达我的心意吧。"
    extend "\n我这么任性，真的很抱歉。"
    "我抛下了蜷缩在地上抽泣的翼，径直朝着友所在的方向跑去。"
    play sound "fx/running.ogg"
    hide tubasa with dissolve
    hide bg with dissolve
    "居然把小孩子弄哭了，我真是个很过分的大人。"
    "…"
    window hide
    show bg gym_backside_night with Dissolve(0.8)
    window show
    "绕过教学楼的拐角处时，"
    show sinobu 4i at top with Dissolve(1.0)
    "我发现忍站在那里。"
    extend "\n刚才那些话，难道都被他听到了吗？"
    show sinobu 5i with dissolve
    sinobu "[player_name]……。"
    me "忍……你是怎么看我的？"
    show sinobu 3i with dissolve
    sinobu "……[player_name]，沿着自己决定的道路前进就好了。"
    extend "\n如果你这时候后悔，就只会让友感到不安和难过而已。"
    show sinobu 25i with dissolve
    sinobu "去吧。翼这边，有我在。"
    me "明白了。"
    extend "\n谢谢你，忍！"
    stop music fadeout 2.0
    play sound "fx/running.ogg"
    hide sinobu with dissolve
    hide bg with dissolve
    "我匆忙赶往与友约好的地点。"
    window hide
    play music "fx/night_insects.ogg"
    show bg gym_backside_night at center with Dissolve(0.8)
    show sinobu 4i at top with dissolve
    window show
    "…"
    show sinobu 22i with dissolve
    sinobu "其实我也很不甘心啊。"
    show sinobu 20i with dissolve
    extend "\n明明我最理解友，也最想守护他。"
    window hide
    hide sinobu with dissolve
    hide bg with dissolve
    window show
    "…"
    window hide
    show bg shoe_locker_night at center with Dissolve(0.8)
    window show
    "等我赶到鞋柜旁时，友已经在那里等着了。"
    show tomo 4i at top with dissolve
    tomo "喂——，[player_name]君——！"
    me "抱歉……我迟到了。"
    show tomo 10i with dissolve
    tomo "没事没事，别放在心上！"
    extend "\n我也是那种经常迟到的类型，\n所以对这种事挺宽容的哦。"
    show tomo 31i with dissolve
    extend "\n虽然也不是什么值得显摆的事情就是了，嘿嘿。"
    "友笑着说道。"
    show tomo 12i with dissolve
    tomo "那，我们走吧。"
    window hide
    hide tomo with dissolve
    show bg school_building_night with Dissolve(1.0)
    window show
    "等我们来到室外，夕阳已经落山了。\n但在照明与摊位灯光的映衬下，校园里的热闹气氛并未减弱。"
    extend "\n在这喧嚣之中，校园操场正中央，为了筹备御咲祭的篝火晚会，\n堆放柴火的工作正稳步推进着。"
    window hide
    show bg schoolyard_night with Dissolve(1.0)
    show tomo 6i at top with dissolve
    window show
    tomo "一直忙到现在，腿都酸了。"
    extend "\n我们找个地方坐会儿吧。"
    me "说得也是。"
    hide tomo with dissolve
    "这么说着，我们两人\n特意在操场深处人较少的一片草坪上坐了下来。"
    window hide
    show tomo 12i at top with dissolve
    window show
    me "这里既能清楚地看到篝火，又能安静地休息呢。"
    tomo "是啊……。"
    stop music fadeout 2.0
    hide tomo with dissolve
    "我们从远处眺望着，热闹非凡的学园祭盛况。"
    extend "\n就在这时——"
    window hide
    play sound "fx/fire.ogg"
    show bg campfire with Radial(0.5)
    window show
    "堆好的柴火终于被点燃了。"
    "鲜红的火焰熊熊燃烧着。"
    extend "\n真的好美啊……。"
    tomo "……真好啊，这种感觉。"
    extend "\n总觉得很平静。"
    me "嗯……。"
    stop sound fadeout 2.0
    window hide
    play music "good_atmosphere.ogg"
    show bg schoolyard_night with Dissolve(1.0)
    show tomo 33i at top with dissolve
    window show
    tomo "……那个，[player_name]君……"
    extend "\n我啊……[player_name]君在我身边的话，我就会觉得非常安心。"
    me "是吗……那还真是谢谢你了。"
    show tomo 35i with dissolve
    tomo "……我说啊，……那个……。"
    show tomo 36i with dissolve
    tomo "……我可以稍微撒一下娇吗……就一下下。"
    me "嗯……。"
    window hide
    show cg school_building_night at center with Dissolve(0.8)
    window show
    "友把头靠在了我的肩上。"
    extend "\n这举动，简直就像小孩子撒娇一样。"
    tomo "我啊……以前做了很多无礼的事，"
    extend "\n给身边的人添了不少麻烦。"
    tomo "那时候，各种讨厌的事和寂寞的心情全都堆积在一起，"
    extend "\n维系理智的那根弦『嘣』的一声就断了……"
    extend "\n所以才闯下了那样的祸。"
    tomo "虽然现在我已经把它牢牢地重新系好了，\n不会再断了。"
    tomo "但是……果然，我还是很弱小啊……"
    extend "\n总会不由自主地，感到很寂寞……。"
    me "那，果然还是和你父亲的事情有关吗？"
    window hide
    show cg school_building1_night with Dissolve(1.0)
    window show
    tomo "……嗯，是啊。"
    extend "\n母亲因为工作原因不常在家，\n所以我独处的时间就特别多。"
    tomo "忍察觉到了这一点，经常来家里陪我玩。"
    extend "\n可即便如此……我还是觉得好寂寞……。"
    tomo "……我喜欢有人陪着，"
    extend "\n所以不太想很早回家。"
    tomo "虽然也有弹钢琴来转移注意力的时候，"
    extend "\n……但一个人还是太冷清了。"
    show bg schoolyard1_night
    extend "\n所以，我才会在放学后在那儿弹琴，"
    extend "\n其实，我是在等谁能推门进来。"
    window hide
    hide cg with Dissolve(0.8)
    hide tomo with Dissolve(0.8)
    window show
    "原来如此。"
    extend "\n原来那场演奏，友是蕴含着这种心情在弹的啊……。"
    "友抬起脑袋，看着我。"
    extend "\n他面色通红，却区别于火光的颜色，能看出是羞赧的潮红。"
    window hide
    show tomo 34i at top with dissolve
    window show
    tomo "所以……[player_name]君。"
    extend "\n我当时，看到[player_name]君来到音乐室的时候，真的，真的好开心！"
    show tomo 35i with dissolve
    tomo "而且，[player_name]君和我待在一起的时候，\n我感觉很轻松……"
    extend "甚至有一种，内心被填满的感觉！"
    show tomo 29i with dissolve
    tomo "我、我！……[player_name]君，我可能，喜欢上了……你！"
    extend "\n不是作为朋友的那种……而是……更进一步的那种……。"
    "说完之后，友低下了头，又靠在了我的身上。"
    window hide
    show cg campfire_sparks at center with FadeWhite(0.8)
    window show
    tomo "[player_name]君……真的只是初中生吗？"
    me "诶？"
    tomo "总觉得……每次看着[player_name]君的时候，\n我都会有一种你根本不是同龄人的错觉。"
    tomo "成熟的男性……。"
    extend "\n对了，感觉就像是……像父亲一样……。"
    me "……友……。"
    tomo "所以……才想和你撒娇呢……。"
    extend "\n想被你摸摸头……想要一直和你待在一起。"
    me "……。"
    tomo "开玩笑啦！！"
    extend "啊、啊哈哈。\n不好意思，突然就说了一些奇怪的话……。"
    tomo "但是……这就是，我真实的心情。"
    extend "\n那时，在家里没能说出口的，真实的心情。"
    stop music fadeout 2.0
    me "友……谢谢你。"
    extend "\n谢谢你愿意这样仰慕我。"
    "我轻轻地摸了摸友的头。"
    window hide
    play music "reminiscence.ogg"
    show cg c20 1 with Radial(0.8)
    window show
    me "像这样摸摸头，心情会平静下来吗？"
    extend "\n还会觉得寂寞吗？"
    tomo "……嗯。好温暖……。"
    me "这样啊……。"
    me "友，我也……我也很喜欢你哦。是作为男孩子的那种喜欢。"
    me "……不过啊，友。"
    extend "\n我觉得你的这份心意，或许跟我的有点不同吧？"
    show cg campfire with Dissolve(1.0)
    tomo "诶……什么意思？"
    me "友现在，是在寻找一个可以代替父亲的可以撒娇的对象吧？"
    extend "\n确实，你对那个人的感情称为『喜欢』没错。"
    extend "\n但是，如果是作为男孩子之间的感情的话，就有一些不同了。"
    tomo "……。"
    me "我很尊敬创造了『森海友』这个生命的，你的父亲。"
    extend "\n因为他，才会有你这个如此可爱又出色的孩子。"
    "我再次温柔地把手放在友的头顶上。"
    me "在友的内心深处，有着父亲留给你的无数珍贵的宝物。"
    extend "\n所以，我是没办法也没资格代替你的父亲的。"
    me "你要试着去正视自己的内心，好好珍惜住在你心里的那个父亲。"
    extend "\n他一定，会一直守护着你。"
    window hide
    show cg c20 2 with FadeWhite(0.8)
    window show
    tomo "内心吗……。"
    "友把手轻轻按在自己的胸口上。"
    me "而且，在友的身边，已经有很多好朋友了，\n对你来说甚至都没有时间去感到寂寞了。"
    me "和你一起享受钢琴乐趣的是翼，"
    extend "\n保护你不受不良学生欺负的则是忍。"
    extend "\n万一你受伤了，月和空会担心你，"
    extend "\n你感到失落的时候，慎太郎则会逗你开心。"
    me "也许是最近我有点太出头了，\n所以你的眼里才只看到了我。"
    extend "\n不过，如果你试着把目光投向周围，\n也包括自己的内心在内，说不定会比以前感到更加心安吧。"
    me "大家都比你想的还要更关心你。"
    extend "\n所以，我觉得你想要的东西，其实已经得到了。"
    tomo "……。"
    show cg c20 3 with dissolve
    tomo "嗯……是啊……。"
    tomo "就算我再怎么消沉也没用！"
    extend "\n我要更加努力地成长才行！"
    extend "\n毕竟，我还有大家！！"
    tomo "谢谢你，[player_name]君。"
    extend "\n不知道从什么时候起，我好像变得越来越消极了。"
    extend "\n这一点都不像我。"
    extend "\n我得更积极一些才行！"
    me "嗯，这才是那个『森海友』嘛。"
    tomo "诶嘿嘿。"
    "友害羞地笑了笑，随后突然将脸贴近——"
    window hide
    show cg c20 4 with Radial(0.8)
    window show
    "（亲）"
    "……诶？"
    show cg c20 5 with Dissolve(0.8)
    tomo "嘿嘿。"
    extend "\n[player_name]君刚才说的作为男孩子的喜欢，\n……也就是，这个意思吧？"
    tomo "这个吻是回礼哦！"
    extend "\n谢谢你让我意识到了这么多重要的事情。"
    tomo "啊……但是，刚才的吻，与其说是回礼，不如说是本能……"
    extend "\n也许，我比[player_name]君想象的，还要更加喜欢[player_name]君哦？"
    me "啊哈哈，这下真是败给你了啊……。"
    me "我才是，非常谢谢你给我带来了这么多快乐。"
    window hide
    show cg moon_night with FadeWhite(0.8)
    window show
    "……这样一来，我终于回应了友的期待，也把自己的心意完整地传达给他了。"
    extend "\n御咲祭成功了，我也和友一起看到了这丛篝火。"
    extend "\n愿望全都实现了。……"
    window hide
    show cg campfire_sparks with Dissolve(0.8)
    window show
    "在这片燃烧的红炎之中，我的意识逐渐淡去……。"
    extend "\n……梦已经结束了。"
    window hide
    hide bg with Dissolve(0.8)
    hide tomo with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    window show
    "…"
    "梦的记忆是模糊的。"
    extend "\n在醒过来的同时，也会忘记这场梦。"
    extend "\n只留下甜美的回忆，其余的一切，都会被带往忘却的彼方。"
    stop music fadeout 4.0
    "好了……差不多该起来了。"
    window hide
    show tomo 34 at top with DefocusWhite(2.5)
    window show
    "友，我喜欢你哦。"
    window hide
    hide tomo with dissolve
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.6
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "（哔哔哔哔哔哔哔哔）"
    window hide
    show bg protagonist_room_morning at center with Radial(0.5)
    window show
    me "啊……已经早上了吗……？"
    extend "\n唔~感觉这一觉还没睡够啊……。"
    stop sound fadeout 0.5
    "我看向桌子，上面放着一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……"
    extend "啊，对对，是昨天回来的时候拿到的。"
    extend "\n那些孩子们，真可爱啊……。"
    me "……好！那天我一定要去好好享受！"
    play sound "fx/cute2.ogg"
    extend "\n然后在脑海里尽情幻想！！"
    window hide
    hide bg with dissolve
    stop music fadeout 0.5
    window show
    "御咲祭当天——"
    window hide
    play music "school_festival.ogg"
    play sound "fx/crowd_noise.ogg"
    show bg school_building_full at center with Radial(1.0)
    pause 0.6
    show bg hallway with Dissolve(1.0)
    window show
    me "我想想……记得说是二年一班和二班的咖啡店。"
    extend "\n唔？"
    play sound "fx/sliding_door.ogg"
    show bg cafe with dissolve
    extend "是这个吗？"
    "正当我站在店门口犹豫不决的时候，"
    extend "一名系着红色领带、戴着黄色名牌，\n左手手指上缠着创可贴的男孩子，从店里走了出来。"
    window hide
    play sound "fx/running.ogg"
    show tomo 33i at top with dissolve
    window show
    tomo "欢迎光临！"
    extend "请问是一位吗？"
    show tomo 34i with dissolve
    extend "\n请慢用。"
    window hide
    hide bg with FadeWhite(1.0)
    hide tomo with FadeWhite(1.0)
    pause 0.6
    show bg tomo_room_evening at center with Radial(0.7)
    pause 0.6
    show bg tomo_ed with Dissolve(0.8)
    pause 1.3
    stop music fadeout 1.5
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.8
    hide bg with dissolve
    return

label end_sintarou:
    show bg cafe at center with dissolve
    window show
    "（噔噔！！）"
    show sintarou 25i at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sintarou "你们三位——！OUT！！"
    me "慎太郎！"
    play sound "fx/cute.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.06), layer='master')
    customer3 "慎、慎太郎君！？"
    play music "sintarou_theme.ogg"
    show sintarou 17i with dissolve
    sintarou "我不是告诫过你们在咖啡店要自重吗！"
    extend "\n听好了，要是再敢对[player_name]动手动脚的话……"
    show cg remarkable at center with FadeWhite(0.4)
    play sound "fx/explosion3.ogg"
    extend "\n未来三个月，禁止踏进我家澡堂！！"
    hide cg with dissolve
    hide sintarou with dissolve
    play sound "fx/ding.ogg"
    customer3 "呜……抱、抱歉了捏。"
    extend "\n有、有点兴奋过头，所以有点不守规矩了捏。"
    customer5 "对不起呀。"
    extend "\n在这里我们还是绅士一点，姑且忍耐一下，记住可远观不可亵玩焉。"
    customer4 "对不起……。"
    stop sound fadeout 0.5
    show sintarou 29i at top with dissolve
    sintarou "嗯，很好。"
    show sintarou 19i with dissolve
    extend "\n我想你们心里应该清楚，不光是这一位，对其他的男孩子也绝对不准出手哦！"
    hide sintarou with dissolve
    "在慎太郎的帮助下，我总算摆脱了这个危机。"
    "没想到在这种时候，竟然被一个初中生搭救了……。"
    extend "\n总感觉有点丢人啊……。"
    window hide
    show sintarou 1i at top with dissolve
    window show
    sintarou "[player_name]，没事吧？"
    me "嗯、嗯。多亏了你，得救了。"
    extend "\n谢谢你！"
    show sintarou 4i with dissolve
    sintarou "不用客气~。"
    show sintarou 31i with dissolve
    sintarou "……。"
    show sintarou 18i with dissolve
    sintarou "话说，[player_name]。"
    extend "\n你今天有和谁约好一起逛后夜祭吗？"
    me "诶？不，还没有安排。"
    show sintarou 34i with dissolve
    sintarou "这样啊这样啊！"
    extend "\n那，你就和咱一起去吧！"
    me "好啊，那其他人呢？"
    show sintarou 23i with dissolve
    sintarou "这种事你就别多问啦！"
    show sintarou 30i with dissolve
    extend "\n而且，我还想和你谈谈咱俩的『秘密』。"
    me "啊……抱、抱歉。"
    extend "\n嗯，那就一起吧！"
    extend "\n那我们就在鞋柜那边碰头吧。"
    show sintarou 8i with dissolve
    sintarou "好！"
    show sintarou 33i with dissolve
    extend "\n那就待会儿见咯！！"
    window hide
    play sound "fx/running.ogg"
    hide sintarou with dissolve
    window show
    "除了『秘密』之外，慎太郎似乎还有其他想和我单独相处的理由。"
    "……。"
    play sound "fx/heartbeat.ogg"
    show cg orange at center with dissolve
    "呜……总觉得心跳加速了……。"
    "嘛、嘛，反正还不知道待会儿他会跟我谈些什么，\n没必要那么紧张……"
    "不行，好不容易又有了独处的机会。"
    extend "\n就算他没有主动开口，我也要自己把话挑明。"
    hide cg with dissolve
    hide bg with dissolve
    stop music fadeout 2.0
    "……毕竟这个梦，不知道会持续到什么时候……。"
    window hide
    play sound "fx/crowd_noise.ogg"
    show bg school_building_evening_full at center with Dissolve(1.0)
    pause 0.4
    show bg cafe_evening with Radial(1.0)
    window show
    "咖啡店的营业时间差不多要结束了。"
    extend "\n剩下的活动，就是和慎太郎的后夜祭！"
    extend "\n我可不能迟到了。得赶紧收拾完。"
    window hide
    play music "tomo_theme.ogg"
    play sound "fx/running.ogg"
    show tomo 4i at top with dissolve
    window show
    tomo "[player_name]君~！"
    "在我忙活的时候，友叫住了我。"
    me "是友啊……。怎么了？"
    show tomo 39i with dissolve
    tomo "我差点忘了，那之后，你和慎酱的约会怎么样呀~？"
    "友笑嘻嘻地问我。"
    me "什么怎么样……就是洗了个澡，然后在慎太郎的房间里睡了会儿而已。"
    show tomo 18i with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tomo "诶！！！"
    extend "\n不仅一起洗澡，还睡了一觉！！？"
    me "不、不是的，不是这样的！！"
    extend "\n是我一个人进去洗，结果因为泡太久头晕了，他才借地方给我休息一下啦！"
    show tomo 31i with dissolve
    tomo "啊哈哈哈~开玩笑啦！"
    extend "\n还有，后夜祭的时候你也要和慎酱一起『享受』吗？"
    me "诶！你怎么会知道……？"
    show tomo 25i with dissolve
    tomo "看你这么紧张，我就知道是这样啦~！"
    extend "\n[player_name]君的心情都写在脸上了哦！"
    me "真、真的吗……。"
    show tomo 2i with dissolve
    tomo "嗯！"
    extend "\n不过嘛，要是不知道你们俩的情况，顶多会觉得有点怪而已啦！"
    show tomo 6i with dissolve
    tomo "不过，没想到你连『享受』这两个字都亲口承认了……！"
    show tomo 13i with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    extend "\n多谢啦，我已经完全懂了！！"
    me "啊，不是啦！我可没有想那么多……。"
    show tomo 38i with dissolve
    tomo "唔……话说回来，我还真没想象过，\n那个碧池太郎慎酱，会和别人搞纯爱呢。"
    me "喂，这话你也没资格说吧。"
    show tomo 24i with dissolve
    tomo "是啊是啊。\n毕竟我最喜欢舒服的事情了呀！"
    show tomo 5i with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/dash.ogg"
    extend "\n不对，我有资格说！！"
    me "啊哈哈哈哈。"
    me "……呼。"
    extend "\n多亏了友的笨蛋属性，我感觉舒服多了。"
    extend "\n谢啦。"
    show tomo 38i with dissolve
    tomo "不用客气！"
    show tomo 28i with dissolve
    extend "\n嗯……？\n等等，你这根本就不是在夸我吧！！"
    me "是在夸是在夸啦！"
    extend "\n那我出发咯！"
    show tomo 4i with dissolve
    tomo "噢！"
    show tomo 17i with dissolve
    extend "\n直到最后一刻都要尽情享受『御咲祭』哦~！！"
    me "交给我吧！"
    extend "\n我这就去让你见识见识何为真正的男子汉！！"
    hide tomo with dissolve
    "虽然两人的对话多少有点牛头不对马嘴，但我确实从友那里得到了不少元气。\n我随即赶往和慎太郎约好的地点。"
    stop music fadeout 2.0
    window hide
    play sound "fx/running.ogg"
    hide bg with dissolve
    window show
    "…"
    play music "fx/night_insects.ogg"
    window hide
    show bg shoe_locker_night at center with dissolve
    window show
    "等我赶到鞋柜旁时，"
    show sintarou 31i at top with dissolve
    "慎太郎已经在那里等我了。"
    me "抱歉，等很久了吗？"
    show sintarou 22i with dissolve
    play sound "fx/sparkle.ogg"
    sintarou "没有，咱也是刚到！"
    show sintarou 29i with dissolve
    extend "\n……开个玩笑啦~这句话，咱一直想说一次试试看！！ "
    "慎太郎一如既往地打趣我。"
    show sintarou 4i with dissolve
    sintarou "那，咱们走吧！"
    window hide
    hide sintarou with dissolve
    show bg school_building_night with Dissolve(1.0)
    window show
    "等我们来到室外，夕阳已经落山了。\n但在照明与摊位灯光的映衬下，校园里的热闹气氛并未减弱。"
    extend "\n在这喧嚣之中，校园操场正中央，为了筹备御咲祭的篝火晚会，\n堆放柴火的工作正稳步推进着。"
    window hide
    show bg schoolyard_night with Dissolve(1.0)
    show sintarou 2i at top with dissolve
    window show
    sintarou "今天一整天都在干活呢，\n要不找个地方坐下来歇会儿吧~？"
    me "说得也是。"
    hide sintarou with dissolve
    "这么说着，我们两人\n特意在操场深处人较少的一片草坪上坐了下来。"
    window hide
    show sintarou 31i at top with dissolve
    window show
    me "这里既能清楚地看到篝火，又能安静地休息呢。"
    sintarou "是啊……。"
    stop music fadeout 2.0
    hide sintarou with dissolve
    "我们从远处眺望着，热闹非凡的学园祭盛况。"
    extend "\n就在这时——"
    window hide
    play sound "fx/fire.ogg"
    show bg campfire with Radial(0.5)
    window show
    "堆好的柴火终于被点燃了。"
    "鲜红的火焰熊熊燃烧着。"
    extend "\n真的好美啊……。"
    sintarou "怎么样？"
    extend "\n和你初中时看到的一样吗？"
    me "……啊啊。"
    extend "\n不过，这次身边有慎太郎陪着，这一点和当时不一样呢。"
    stop sound fadeout 2.0
    window hide
    play music "good_atmosphere.ogg"
    show bg schoolyard_night with Dissolve(1.0)
    show sintarou 31i at top with dissolve
    window show
    sintarou "这样啊……。"
    show sintarou 6i with dissolve
    sintarou "呐呐，你的职业是什么？"
    extend "\n实际上，是长什么样子？"
    show sintarou 4i with dissolve
    extend "\n一直住在御咲吗？"
    extend "\n有没有恋人？单身吗？是基吗？"
    play sound "fx/boing.ogg"
    me "等、等一下！你突然这么问，我会很为难的啦！"
    show sintarou 7i with dissolve
    sintarou "因为很在意啊~！"
    extend "\n像漫画或动画角色设定一样的人物就站在我眼前耶！！"
    extend "\n换谁都会被勾起好奇心吧！"
    me "喂喂，你是把我当成什么好玩的玩具了吗~？"
    show sintarou 11i with dissolve
    sintarou "当然不是那样啦！"
    show sintarou 13i with dissolve
    extend "\n只是单纯地，想要在最后多了解一些关于[player_name]的事情而已。"
    me "什么啊，突然这么严肃……。"
    show sintarou 18i with dissolve
    sintarou "因为……今天是最后一天了吧？"
    "诶？"
    show sintarou 20i with dissolve
    sintarou "[player_name]君吃的魔法糖，\n效果如果是回到初中生活度过学园祭的话，"
    extend "\n那么随着今天学园祭的结束，\n[player_name]君和我这样见面的机会，应该不会再有了吧？"
    me "……。"
    window hide
    show cg school_building1_night at center with Dissolve(0.8)
    window show
    "我顿时语塞了。"
    "虽然没有确凿的证据，但慎太郎所说的，恐怕正是真相。"
    show bg schoolyard1_night
    "要再也见不到慎太郎他们了吗……？"
    window hide
    hide cg with dissolve
    hide sintarou with dissolve
    window show
    me "说不定……是这样的。"
    show sintarou 30i at top with dissolve
    sintarou "啊，[player_name]自己对这种设定也不是很清楚呢。"
    extend "\n嘛，虽然完全是咱自己的推测啦！"
    show sintarou 8i with dissolve
    extend "\n……既然已经没时间了，那咱想问的事情就得问个清楚，\n传达的心意也必须说出口才行。"
    "连这种时候也是按照慎太郎的节奏来的。"
    extend "\n真是的，我这个人啊。"
    me "……说得也是。"
    extend "\n慎太郎，我也有话想告诉你。"
    show sintarou 18i with dissolve
    sintarou "什么？"
    extend "\n什么都可以说哦。"
    me "我……喜欢慎太郎。"
    extend "\n虽然你看起来总是一副吊儿郎当的样子，却总是在不知不觉间牵动着我的步调。"
    extend "\n在我软弱的时候，你会给予支持，一直陪伴在我身边。"
    stop music fadeout 2.0
    extend "\n这样的慎太郎魅力十足，我非常喜欢。"
    show sintarou 4i with dissolve
    sintarou "是嘛~。"
    window hide
    play music "reminiscence.ogg"
    show cg c30 1 at center with Radial(0.8)
    window show
    "听完我的告白，慎太郎轻轻地靠在了我的身上。"
    "那张脸颊，融入火焰的颜色之中难以分辨，但看上去像是泛红了。"
    sintarou "哼哼~♪"
    extend "\n[player_name]喜欢上咱了啊！"
    extend "\n咱也一样，非常喜欢[player_name]。"
    extend "\n这是咱第一次被别人打乱了节奏呢。"
    me "我一直都觉得自己是顺着慎太郎的节奏来的……。"
    sintarou "不不不~你这话可就不对了。"
    extend "\n还是说，这是在跟咱显摆什么『大人的力量』啊？"
    me "哈哈，现在已经不需要了吧。"
    sintarou "嘛，其实咱也是，打乱别人节奏的时候自己不会察觉到。"
    extend "\n在这点上，咱们俩搞不好真的很像呢！"
    "这么说来，其实在跟慎太郎坦白自己是大人之前，"
    extend "\n因为想法太合得来，我还真觉得过这是命中注定呢。"
    me "我大概也是感知到了这种共鸣，才忍不住对慎太郎坦白了身份吧~现在想想，真佩服那时的自己。"
    sintarou "原来如此啊~。听你这么说，我很高兴哦。"
    extend "\n虽然预先知道你即将消失这件事挺让人难受的，"
    extend "\n但正因如此，才能像这样提前做好准备嘛！"
    window hide
    show cg campfire with Dissolve(1.0)
    window show
    me "……慎太郎，真的很了不起啊。"
    extend "\n换作其他人，一定会因为寂寞而变得消沉，\n根本没法这么理性地面对呢。"
    sintarou "寂寞当然是会寂寞的啦~。"
    extend "\n这一点咱们彼此彼此，其实[player_name]也很困扰吧。"
    me "慎太郎在这方面也像个成熟的大人呢。"
    extend "\n想问什么就问，想说什么就说什么。\n这点其实是很重要的。"
    me "但是不知为何，一旦成了大人，\n有时候反而会觉得这种坦诚是一件很困难的事。"
    sintarou "是吗？"
    extend "\n……那么，趁着还是孩子，\n就把想做的事情都做了吧。"
    "慎太郎小声说着，随后突然将脸凑近——"
    window hide
    show cg c30 3 with Radial(0.8)
    window show
    "（亲）"
    "……诶？"
    show cg c30 2 with Dissolve(0.8)
    sintarou "嘿嘿嘿。"
    extend "\n[player_name]，为了以后不后悔，\n就趁现在，把那些事全都做个爽怎么样？"
    me "真是的……"
    extend "\n慎太郎到了最后关头还是那么『慎太郎』啊。"
    sintarou "当然！"
    extend "\n我就是我嘛！"
    window hide
    hide cg with Dissolve(0.8)
    hide sintarou with Dissolve(0.8)
    show sintarou 11i at top with dissolve
    window show
    sintarou "……啊——啊！"
    extend "\n本来还挺期待和『小大人』谈一场轰轰烈烈的恋爱呢，真可惜啊~！"
    me "『小大人』根本不是这个意思啦！！"
    extend "\n……不过，你说得对。我也好想一直和你待在一起啊。"
    extend "\n回归现实后，等待着我的又会是严酷的社会人生活啊……。"
    show sintarou 4i with dissolve
    sintarou "不过，大人的生活也很有意思吧？"
    extend "\n和孩子不同，行动要自由得多啊！"
    extend "\n还能尽情逛十八禁区域！"
    me "……确实。"
    extend "\n下次有机会，我会作为毕业生回御咲学园偷偷看你们的。"
    show sintarou 13i with dissolve
    sintarou "那可注意千万不要对学生出手，要是被捕就麻烦了呢~。"
    extend "\n最多也就在脑内妄想一下，然后自己解决啦。"
    show sintarou 8i with dissolve
    extend "\n啊，如果是对咱的话倒是无所谓！"
    show sintarou 35i with dissolve
    extend "\n还有，咱家的澡堂可一定记得要来哦！"
    me "交给我吧！！"
    extend "\n慎太郎你也要像个真正的初中生那样，给我好好学习哦。"
    extend "\n……那么，再见了。"
    show sintarou 33i with dissolve
    sintarou "嗯！拜拜！"
    extend "\n要保重哦！"
    window hide
    show cg moon_night at center with FadeWhite(0.8)
    window show
    "……这样一来，我终于向他表白了心意，也得到了慎太郎的答复。"
    extend "\n御咲祭成功了，我也和慎太郎一起看到了这丛篝火。"
    extend "\n愿望全都实现了。……"
    window hide
    show cg campfire_sparks with Dissolve(0.8)
    window show
    "在这片燃烧的红炎之中，我的意识逐渐淡去……。"
    extend "\n……梦已经结束了。"
    window hide
    hide bg with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    hide sintarou with Dissolve(0.8)
    window show
    "…"
    "梦的记忆是模糊的。"
    extend "\n在醒过来的同时，也会忘记这场梦。"
    extend "\n只留下甜美的回忆，其余的一切，都会被带往忘却的彼方。"
    stop music fadeout 4.0
    "好了……差不多该起来了。"
    window hide
    show sintarou 33 at top with DefocusWhite(2.5)
    window show
    "慎太郎，我喜欢你哦。"
    window hide
    hide sintarou with dissolve
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.6
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "（哔哔哔哔哔哔哔哔）"
    window hide
    show bg protagonist_room_morning at center with dissolve
    window show
    me "啊……已经早上了吗……？"
    extend "\n唔~感觉这一觉还没睡够啊……。"
    stop sound fadeout 0.5
    "我看向桌子，上面放着一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……"
    extend "啊，对对，是昨天回来的时候拿到的。"
    extend "\n那些孩子们，真可爱啊……。"
    me "……好！那天我一定要去好好享受！"
    play sound "fx/cute2.ogg"
    extend "\n然后在脑海里尽情幻想！！"
    window hide
    hide bg with dissolve
    stop music fadeout 0.5
    window show
    "御咲祭当天——"
    window hide
    play music "school_festival.ogg"
    play sound "fx/crowd_noise.ogg"
    show bg school_building_full at center with Radial(1.0)
    pause 0.4
    show bg hallway with Dissolve(1.0)
    window show
    me "我想想……记得说是二年一班和二班的咖啡店。"
    extend "\n唔？"
    play sound "fx/sliding_door.ogg"
    show bg cafe with dissolve
    extend "是这个吗？"
    "正当我站在店门口犹豫不决的时候，"
    extend "一名系着红色领带、戴着橘色名牌，\n右手手指上缠着创可贴的男孩子，从店里走了出来。"
    window hide
    play sound "fx/running.ogg"
    show sintarou 8i at top with dissolve
    window show
    sintarou "欢迎光临~！就一位吗？"
    show sintarou 34i with dissolve
    extend "\n来来，请进请进！请慢慢享受哦~！"
    window hide
    hide bg with Radial(1.0)
    hide sintarou with Radial(1.0)
    pause 0.6
    show bg hananoyu at center with Radial(0.7)
    pause 0.6
    show bg sintarou_ed with Dissolve(0.8)
    pause 1.3
    stop music fadeout 1.5
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.8
    hide bg with dissolve
    return

label day4_1_sinobu:
    show sinobu 26i at top with dissolve
    window show
    sinobu "[player_name]，加油哦。"
    me "噢！"
    hide sinobu with dissolve
    return

label day4_1_tubasa:
    show tubasa 4i at top with dissolve
    window show
    tubasa "[player_name]君，我们一起加油吧。"
    me "噢！"
    hide tubasa with dissolve
    return

label day4_1_tuki:
    show tuki 9i at top with dissolve
    window show
    tuki "[player_surname]，加油干吧。"
    me "噢！"
    hide tuki with dissolve
    return

label day4_1_sora:
    show sora 11i at top with dissolve
    window show
    sora "一起加油吧，[player_name]君！"
    me "噢！"
    hide sora with dissolve
    return

label day4_1_sakuya:
    show sakuya 5i at top with dissolve
    window show
    sakuya "[player_name]，你也给我好好努力啊！"
    me "噢！"
    hide sakuya with dissolve
    return

label day4_1_saburo:
    show saburo 10i at top with dissolve
    window show
    saburo "我来给你打气咯~[player_surname]！"
    me "噢！"
    hide saburo with dissolve
    return

label end_sinobu:
    show bg cafe at center with dissolve
    play music "sinobu_theme.ogg"
    show sinobu 3i at top with dissolve
    window show
    sinobu "到此为止了。"
    me "忍！"
    customer3 "怎，怎么会这样！"
    show sinobu 30i with dissolve
    sinobu "这位客人，本店禁止进行这样的行为。"
    extend "\n若您还打算继续这种行为的话，就请离开吧。"
    extend "\n请您把手放开。"
    play sound "fx/boing.ogg"
    customer3 "呜……抱，抱歉了捏。"
    extend "\n有，有点兴奋过头，所以有点不守规矩了捏。"
    play sound "fx/cute3.ogg"
    customer5 "对不起呀。"
    extend "\n这里还是绅士一点，姑且忍一忍，可远观不可亵玩焉。"
    play sound "fx/sparkle.ogg"
    customer4 "正义感强烈的男孩子真是棒呀♪"
    window hide
    hide sinobu with dissolve
    window show
    "在忍的帮助下，我总算是摆脱了困境。"
    "没想到在这种时候还能被初中生搭救……。"
    extend "\n总感觉有点丢人啊……。"
    window hide
    show sinobu 5i at top with dissolve
    window show
    sinobu "[player_name]，没事吧？"
    me "嗯，嗯嗯。得救了。"
    extend "\n谢谢你们！"
    show sinobu 4i with dissolve
    sinobu "不用客气。"
    show sinobu 15i with dissolve
    sinobu "……。"
    show sinobu 8i with dissolve
    sinobu "说起来，[player_name]君，\n你今天之后夜祭有安排吗？"
    me "诶？不，还没有安排。"
    show sinobu 31i with dissolve
    sinobu "对。"
    extend "\n那么，[player_name]我可以和你在一起吗？"
    me "好啊，其他人呢？"
    show sinobu 32i with dissolve
    sinobu "……我想和你独处一会…。"
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.07), layer='master')
    "什，什么啊啊啊啊啊！！！"
    me "诶，啊，是吗！？行行行可以啊！！"
    extend "\n那么，我们在鞋柜那碰头。"
    show sinobu 31i with dissolve
    sinobu "嗯……"
    show sinobu 33i with dissolve
    extend "\n那么，之后再见吧。"
    window hide
    play sound "fx/running.ogg"
    hide sinobu with dissolve
    window show
    "忍说的独处……难道是想要在之前回家路上的事的基础上进一步发展吗……？"
    "……。"
    play sound "fx/heartbeat.ogg"
    show cg green at center with dissolve
    "呜……总觉得心跳加速了……。"
    "嘛，嘛，也不知道会发展成什么样子，\n没必要那么紧张……"
    "不，好不容易又有了独处的机会。"
    extend "\n如果他没有主动提起的话，我也会主动开口。"
    hide cg with dissolve
    hide bg with dissolve
    stop music fadeout 2.0
    "……毕竟这个梦不知道会持续到什么时候……。"
    window hide
    play sound "fx/crowd_noise.ogg"
    show bg school_building_evening_full at center with Dissolve(1.0)
    pause 0.4
    show bg cafe_evening with Radial(1.0)
    window show
    "咖啡店的营业时间也差不多要结束了。"
    extend "\n剩下的活动，就是和忍在后夜祭上做些什么了！"
    extend "\n我可不能迟到了。得赶紧收拾完。"
    show tomo 23i at topright
    show tubasa 2i at topleft with dissolve
    tubasa "[player_name]君。"
    tomo "……。"
    "我还在勤恳地工作时，翼和友一起向我搭话了。"
    me "翼，还有友君……？ 什么事？"
    show tubasa 23i with dissolve
    tubasa "友君他，那个……"
    extend "\n[player_name]君，他有话要对你说。"
    show tomo 35i with dissolve
    tomo "……。"
    "……毕竟友是忍的青梅竹马。"
    extend "\n他一定从忍的样子看出\n接下来会发生什么了吧。"
    hide tomo with dissolve
    hide tubasa with dissolve
    play music "tomo_theme.ogg"
    show tomo 30i at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    tomo "……你要好好对待他哦！"
    show tomo 32i with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    extend "\n要是让他哭了我可饶不了你！！"
    show tomo 5i with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    extend "\n还有，忍做菜很烂，你要好好照顾他哦！"
    extend "\n还有还有……"
    hide tomo with dissolve
    show tomo 24i at topright with dissolve
    extend "祝你们幸福！！！"
    show tubasa 4i at topleft with dissolve
    tubasa "[player_name]君常常来布置组帮忙\n所以我很常有机会见到你们俩，"
    extend "\n我觉得你们一定会很顺利的。"
    me "……谢谢你们。"
    extend "\n我先走一步了！"
    show tomo 4i with dissolve
    tomo "好！"
    show tubasa 31i with dissolve
    tubasa "加油！"
    "得到了翼和友的鼓励，我急忙赶到了忍和我的约见地点。"
    stop music fadeout 1.0
    window hide
    play sound "fx/running.ogg"
    hide tomo with dissolve
    hide bg with dissolve
    hide tubasa with dissolve
    window show
    "…"
    play music "fx/night_insects.ogg"
    window hide
    show bg shoe_locker_night at center with dissolve
    window show
    "来到鞋柜前，发现忍早已在那里等我了。"
    extend "\n一见到忍的身影，我的脚步便停住了。"
    window hide
    show cg school_building_night at center with dissolve
    window show
    "是啊……这是一场不知何时会醒来的梦。"
    extend "\n说得更准确一点，也许梦在今天就结束了。"
    extend "\n但是，我应该把自己的心意说出来吗？"
    extend "\n这么做不会只是单纯地伤害到忍吗？"
    "可恶……居然在这种地方遇到了难题……。"
    window hide
    hide sinobu with dissolve
    hide cg with dissolve
    window show
    me "我，我到底……"
    show sinobu 26i at top with dissolve
    sinobu "[player_name]，你在这里呀。"
    "忍注意到了停下脚步的我，朝我这边走了过来。"
    show sinobu 22i with dissolve
    "原来你说的是在鞋柜见面，我还以为是在别的地方呢。"
    me "抱，抱歉！"
    extend "\n我本打算在鞋柜前等你……。"
    show sinobu 18i with dissolve
    sinobu "这样啊。\n不过，能在这里相遇真是太好了。"
    show sinobu 26i with dissolve
    extend "\n那我们出发吧。"
    window hide
    hide sinobu with dissolve
    show bg school_building_night with Dissolve(1.0)
    window show
    "我们来到外面，夕阳已经落山了。\n但余晖和摊位的灯光交相辉映，街上依然很热闹。"
    extend "\n在校园的正中央，大家为了御咲祭篝火晚会做准备，\n堆柴火的工作正在有序地进行。"
    window hide
    show bg schoolyard_night with Dissolve(1.0)
    show sinobu 22i at top with dissolve
    window show
    sinobu "今天一直都在工作，找个地方坐下来吧。"
    me "说的是。"
    hide sinobu with dissolve
    "这么说着，我们两人\n在远离操场的草坪上坐了下来。"
    window hide
    show sinobu 12i at top with dissolve
    window show
    me "在这里的话，就能清楚地看到火焰，可以好好休息了。"
    sinobu "说的也是……。"
    stop music fadeout 2.0
    hide sinobu with dissolve
    "远远眺望着，热闹非凡的学园祭的光景。"
    extend "\n然后"
    window hide
    play sound "fx/fire.ogg"
    show bg campfire with Radial(0.5)
    window show
    "终于点燃了柴火堆。"
    "熊熊燃烧着的鲜红火焰。"
    extend "\n真的好美啊……。"
    sinobu "真美啊……。"
    me "嗯……。"
    "不过比起眼前的景色，忍更美。"
    stop sound fadeout 2.0
    hide bg with Dissolve(0.3)
    "……说不出口。"
    window hide
    play music "good_atmosphere.ogg"
    show bg schoolyard_night at center with Dissolve(1.0)
    show sinobu 2i at top with dissolve
    window show
    sinobu "……[player_name]，怎么了？"
    me "……诶？"
    show sinobu 21i with dissolve
    sinobu "你一直在隐瞒着什么吧……"
    extend "与其说隐瞒，不如说是在思考吧。"
    me "嗯，嗯嗯……。"
    show sinobu 34i with dissolve
    sinobu "不想说的话就不用说了。"
    show sinobu 27i with dissolve
    extend "\n但是，如果方便的话，我想知道。"
    me "……嗯。"
    show sinobu 32i with dissolve
    sinobu "我，想更多的了解[player_name]君的事情，也更想和\n[player_name]君靠得近一点。"
    show sinobu 33i with dissolve
    sinobu "[player_name]君，我喜欢你。"
    me "忍……！"
    show sinobu 31i with dissolve
    sinobu "邀请你参加后夜祭，是因为我想传达这份感情。"
    extend "\n……一起回家的时候没说出口也是因为这个。"
    extend "\n那时，[player_name]说过我的笑容很漂亮，\n我真的非常高兴……。"
    "忍红着脸，低着头露出了微笑。"
    me "哎呀……被你听到了。"
    extend "\n忍……忍这么对我说，我也很高兴。\n真的十分感谢。"
    extend "\n……但是，我……。"
    show sinobu 34i with dissolve
    sinobu "[player_name]，冷静。"
    extend "\n我……[player_name]只要是你说的话，\n无论是什么都能接受。"
    me "忍…。"
    window hide
    show cg school_building1_night at center with Dissolve(0.8)
    window show
    me "我不能一直待在你的身边。"
    extend "\n可能过不了多久就会消失。也许，就是今天。"
    show bg schoolyard1_night
    extend "\n所以，这样的我不能回应你的心意…。"
    window hide
    hide cg with dissolve
    hide sinobu with dissolve
    show sinobu 18i at top with dissolve
    window show
    sinobu "[player_name]……哪怕真的如此，我也想表达出来。"
    show sinobu 21i with dissolve
    extend "\n这么说，不为什么未来的希冀"
    extend "\n而是为你伴我日夜冷暖的，[player_name]至今未变的心意"
    "……。"
    window hide
    show cg moon_night at center with Dissolve(2.0)
    window show
    sinobu "嘿嘿，今天我可以明白地说出来呢。"
    extend "\n『今晚月色真美。』"
    me "忍……我也喜欢你。"
    extend "\n现在的我比任何人都还要爱你。"
    sinobu "……嗯。\n谢谢你……好开心。"
    "这么说着，忍没有露出微笑，而是展露出最灿烂的笑容。"
    window hide
    show cg campfire with Dissolve(0.8)
    window show
    "我抱住了忍的头，让他靠在我身上。"
    me "呼……啊哈哈，感觉真是不可思议啊。"
    extend "\n最开始的时候，明明是我拼命想了解忍，\n现在却反而是忍拼命想要了解我。"
    sinobu "最开始的时候……[player_name]君是一个重视意志的人。"
    extend "\n然后，正如我所期待的那样，[player_name]君在我的灵魂深处，看到了我的真心。"
    extend "\n当然你也很关注我的外表啦。不过除此以外，你也看到了我的内在。"
    extend "\n我被这样的[player_name]君深深吸引住了。"
    sinobu "这就是……恋爱吧。"
    stop music fadeout 2.0
    "忍看着我说道。"
    extend "我也看向忍。"
    "他的脸颊还是一如既往的红。"
    extend "我脸上一定也是一样的吧。"
    window hide
    play music "reminiscence.ogg"
    show cg c38 1 with Radial(0.8)
    window show
    me "嗯……这就是恋爱啊。"
    sinobu "……。"
    me "……。"
    sinobu "……[player_name]，闭上眼睛。"
    me "嗯……。"
    window hide
    show cg c38 2 with Radial(0.8)
    window show
    "亲"
    "我感到了忍嘴唇传来的柔软触感。"
    show cg c38 3 with Dissolve(0.8)
    me "忍，真的变了呢。"
    sinobu "还不是因为你……。"
    sinobu "[player_name]刚说会马上消失，\n但我并不后悔。"
    extend "\n虽然会感到寂寞，但我绝对不会后悔，放心吧。"
    extend "\n因为我一直都很幸福。"
    me "嗯……谢谢你，忍。"
    extend "\n我也很幸福。"
    sinobu "啊……但是，《北O神拳》还没还呢，\n我们还没好好聊聊这件事真是遗憾。"
    me "啊~……这么说来还真是。"
    extend "\n但是没关系。\n如今，我与你已经比任何人都要了解彼此了。"
    sinobu "嗯……。"
    window hide
    show cg moon_night with FadeWhite(0.8)
    window show
    "……我回应了忍的心意，也传达了我的爱意。"
    extend "\n御咲祭也成功了，还和忍一起看完了这场火焰秀。"
    extend "\n愿望全都实现了。……"
    window hide
    show cg campfire_sparks with Dissolve(0.8)
    window show
    "在这片燃烧的红炎之中，我的意识逐渐淡去……。"
    extend "\n……梦已经结束了。"
    window hide
    hide bg with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    hide sinobu with Dissolve(0.8)
    window show
    "…"
    "梦的记忆是模糊的。"
    extend "\n在醒过来的同时，也会忘记这场梦。"
    extend "\n只留下甜美的回忆，其他的一切都被带去忘却的彼方而消散。"
    "我并不后悔。希望忍也一样。"
    stop music fadeout 4.0
    "好了……差不多该起来了。"
    window hide
    show sinobu 31 at top with DefocusWhite(2.5)
    window show
    "喜欢你，忍。"
    window hide
    hide sinobu with dissolve
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.6
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "哔哔哔哔哔哔哔哔"
    window hide
    show bg protagonist_room_morning at center with dissolve
    window show
    me "啊……已经早上了吗……？"
    extend "\n唔~我好像并没有睡多少啊……。"
    stop sound fadeout 0.5
    "我望向餐桌，上面放着一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……"
    extend "啊，对对对，昨天回来的时候拿到的。"
    extend "\n那些孩子们，真可爱啊……。"
    me "……好！那天我一定要去好好享受！"
    play sound "fx/cute2.ogg"
    extend "\n然后在脑海里尽情幻想！！"
    window hide
    hide bg with dissolve
    stop music fadeout 0.5
    window show
    "御咲祭当天ーーーーーー"
    window hide
    play music "school_festival.ogg"
    play sound "fx/crowd_noise.ogg"
    show bg school_building_full at center with Radial(1.0)
    pause 0.4
    show bg hallway with Dissolve(1.0)
    window show
    me "我想想……记得说是2年1班和2年2班的咖啡店。"
    extend "\n嗯？这里吗？"
    "正当我站在店门口犹豫不决的时候，"
    extend "\n三个与我差不多大的男生正在迷茫着，\n他们向店里的人打起了招呼。"
    window hide
    window show
    student_a "啊，喂~，我们来了。这里就是2年1，2班的咖啡馆吗？"
    show tubasa 4i at topright with dissolve
    unknown "啊，你，你好……"
    extend "\n是的，这里就是我们的咖啡馆。"
    extend "\n那个……如果您是要入店的话，请将乐器交给我保管。"
    student_b "哦，谢谢！"
    extend "\n这个不仅很重，还占地方，给你保管轻松多了！。"
    student_c "绝对不要摔了啊！！注意别弄掉了！！"
    "他们边这样说着，边被带着走过我身旁。"
    window hide
    play sound "fx/sliding_door.ogg"
    hide tubasa with dissolve
    window show
    "看来，肯定就是在这里！！"
    extend "\n我鼓起自信，意气风发地走向咖啡店的入口。"
    play sound "fx/sliding_door.ogg"
    show bg cafe with FadeWhite(0.5)
    "接着，一个戴绿色名牌的，打着红领带的男孩从店内走了出来。"
    window hide
    play sound "fx/running.ogg"
    show sinobu 26i at top with dissolve
    window show
    sinobu "欢迎光临，客人。"
    show sinobu 33i with dissolve
    extend "\n请问是一位吗？"
    show sinobu 31i with dissolve
    extend "\n请往这边走……请慢慢欣赏。"
    window hide
    hide bg with Radial(1.0)
    hide sinobu with Radial(1.0)
    pause 0.6
    show bg sidewalk_evening at center with Radial(0.7)
    pause 0.6
    show bg sinobu_ed with Dissolve(0.8)
    pause 1.3
    stop music fadeout 1.5
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.8
    hide bg with dissolve
    return

label end_tubasa:
    show bg cafe at center with dissolve
    play music "tubasa_theme.ogg"
    show tubasa 16i at top with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    window show
    tubasa "客，客人！\n继续得寸进尺……是不行的！"
    me "翼！"
    customer3 "怎，怎么会这样！"
    show tubasa 24i with dissolve
    tubasa "那，那个……[player_name]君好像有点困扰，\n请你无论如何放开他。"
    show tubasa 18i with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    extend "\n再，再继续做奇怪的事的话，我就叫老师了哦！"
    play sound "fx/boing.ogg"
    customer3 "呜……抱，抱歉了捏。"
    extend "\n有，有点兴奋过头，所以有点不守规矩了捏。"
    play sound "fx/cute3.ogg"
    customer5 "对不起呀。"
    extend "\n这里还是绅士一点，姑且忍一忍，可远观不可亵玩焉。"
    play sound "fx/sparkle.ogg"
    customer4 "正义感强烈的男孩子真是棒呀♪"
    window hide
    hide tubasa with dissolve
    window show
    "在翼的帮助下，我总算是逃过了一劫。"
    "没想到在这种时候还能被初中生搭救……。"
    extend "\n总感觉有点丢人啊……。"
    window hide
    show tubasa 21i at top with dissolve
    window show
    tubasa "[player_name]君，没事吧……？"
    me "嗯，嗯嗯。得救了。"
    extend "\n谢谢你们！"
    show tubasa 12i with dissolve
    tubasa "没有，不客气。"
    show tubasa 14i with dissolve
    tubasa "……。"
    show tubasa 15i with dissolve
    tubasa "说，说起来，[player_name]君。"
    extend "\n关于之后的后夜祭，有什么预定吗？"
    me "诶？没，没什么……。"
    show tubasa 31i with dissolve
    tubasa "太，太好了。"
    extend "\n那个……如果可以的话，能和我一起逛吗？"
    me "可以啊……不过友君不去吗？"
    "我悄悄地对翼说道。"
    show tubasa 9i with dissolve
    tubasa "这，这次就算了！"
    show tubasa 37i with dissolve
    extend "\n[player_name]君和我两个人聊就好…。"
    me "……这样啊，我知道了。"
    extend "\n那么，我们在鞋柜那碰头。"
    show tubasa 36i with dissolve
    tubasa "嗯，谢谢你！"
    extend "\n那么，我就先回去了！\n回头见。"
    window hide
    play sound "fx/running.ogg"
    hide tubasa with dissolve
    window show
    "翼竟然不先找友说话，而是先找我。究竟是要说什么事呢？"
    "他俩难得一起当代表委员，明明这个好的机会……"
    extend "\n呃，这也不是我能决定的，啊。"
    "……。"
    play sound "fx/heartbeat.ogg"
    show cg blue at center with dissolve
    "呜……总觉得心跳加速了……。"
    "嘛，嘛，也不知道会发展成什么样子，\n没必要那么紧张……"
    "不，好不容易又有了独处的机会。"
    extend "\n如果他没有主动提起的话，我也会主动开口。"
    hide cg with dissolve
    hide bg with dissolve
    hide tubasa with dissolve
    stop music fadeout 2.0
    "……毕竟这个梦不知道会持续到什么时候……。"
    window hide
    play sound "fx/crowd_noise.ogg"
    show bg school_building_evening_full at center with Dissolve(1.0)
    pause 0.4
    show bg cafe_evening with Radial(1.0)
    window show
    "咖啡店的营业时间也差不多要结束了。"
    extend "\n剩下的活动，是和翼的后夜祭！"
    extend "\n我可不能迟到了。得赶紧收拾完。"
    window hide
    play music "serious.ogg"
    show sakuya 15i at top with dissolve
    window show
    sakuya "喂。"
    "在我努力干活的时候，作哉向我搭话了。"
    me "抱歉。\n我现在有点事。"
    extend "\n能稍微往后推一下吗？"
    show sakuya 10i with dissolve
    sakuya "我知道我知道。"
    extend "\n不会花太多时间的，跟我来。\n我有话和你说。"
    "这么说着，作哉强硬地拉走了我。"
    window hide
    hide sakuya with dissolve
    hide bg with dissolve
    show bg stairs_evening at center with Dissolve(1.0)
    stop music fadeout 2.0
    window show
    me "……所以，找我有什么事？"
    show sakuya 19i at top with dissolve
    sakuya "……。"
    "面对一脸奇妙的作哉，我加强了警戒。"
    show sakuya 7i with dissolve
    play music "sakuya_theme.ogg"
    sakuya "……抱歉啊。\n一直以来对你的态度都不好。"
    play sound "fx/boing.ogg"
    me "……诶？"
    "我本还抱着戒备，听到他意料之外的话，不由得发出了惊讶的声音。"
    show sakuya 10i with dissolve
    sakuya "昨天你对我说的那些话，回到家仔细思考了下，"
    extend "\n你说的并没有错。\n这点我可以承认。"
    extend "\n所以你也别太在意这些小细节啦。"
    me "……？\n小细节是？"
    show sakuya 6i with dissolve
    sakuya "……你，现在打算向一之濑告白对吧。"
    me "诶。"
    show sakuya 9i with dissolve
    sakuya "要是你突然顾虑到我的话我反而会很不爽的。"
    extend "\n你才是，不要擅自认定我的感情如何如何。\n那就再见啦。"
    hide sakuya with dissolve
    me "等，等等啊！"
    extend "\n我还没决定告白呢……。"
    "作哉准备离开的瞬间又回过头来。"
    window hide
    show sakuya 6i at top with dissolve
    window show
    sakuya "哈……？"
    me "的确，我喜欢那孩子。"
    extend "\n但是，我又不能强加这种感情给他。"
    extend "\n他明明心里想着友君，我可不想横刀夺爱。"
    extend "\n在确认他的感情之前，我是不会告白的。"
    show sakuya 16i with dissolve
    sakuya "……那算什么，逊爆了。"
    me "诶？"
    show sakuya 13i with dissolve
    sakuya "我就是在说你那明显吓到自保自全的怂样。"
    show sakuya 18i with dissolve
    extend "\n你表面上装得好像很尊重对方的意思，\n但你，不过是纯粹的没出息的胆小鬼。"
    me "……。"
    show sakuya 20i with dissolve
    sakuya "明明只是单纯地想装模作样地装明白人，"
    extend "\n一边说着『为了不后悔要坦率一点』，\n结果本人在告白前就老老实实地死心了，自己夹着尾巴逃走了，\n完全是前后矛盾的啊。"
    show sakuya 19i with dissolve
    sakuya "哈啊……是我看走眼了。"
    extend "\n我昨天到底是在想什么呢？"
    extend "\n我怎么就真的相信你这白痴的话了。"
    me "作，作哉……。"
    show sakuya 20i with dissolve
    sakuya "啊？"
    me "……是我错了呢。\n确实，一点都不合理。"
    extend "\n真拿你没办法啊，都这岁数了。"
    me "我会向你证明我是男子汉的。\n如果翼对我没那个意思的话，我也会强行让他关注到我。"
    extend "\n就算放弃，那也得在他完全拒绝我之后。"
    show sakuya 5i with dissolve
    sakuya "……你明白就好。"
    "听了我说的话，作哉笑了。"
    show sakuya 9i with dissolve
    sakuya "对，还有，要说不对的地方，还有一个。"
    show sakuya 20i with dissolve
    extend "\n恋爱和年龄没有关系。"
    extend "\n你这自命不凡的大人，自己也给自己设限了吧。"
    extend "\n明明不用受这种东西的束缚，随心所欲地去做就好了。"
    "……是这样吗。"
    me "作哉……谢谢。"
    show sakuya 8i with dissolve
    sakuya "怎，怎么了突然……真不好意思。"
    me "多亏作哉，我找回了自信。"
    extend "\n我想，我能放开心去面对了。"
    show sakuya 22i with dissolve
    sakuya "……那真是太好了。"
    play sound "fx/running.ogg"
    hide sakuya with dissolve
    "说完，作哉便回到了教学楼。"
    stop music fadeout 1.0
    window hide
    hide bg with dissolve
    window show
    "…"
    window hide
    play music "fx/night_insects.ogg"
    show bg shoe_locker_night at center with Dissolve(0.8)
    window show
    "到达鞋柜处，翼已经在那里等我了。"
    show tubasa 31i at top with dissolve
    tubasa "啊，[player_name]君。"
    me "抱歉抱歉！\n我来晚了。"
    show tubasa 4i with dissolve
    tubasa "没事的。"
    extend "\n我也是刚刚到。\n那我们走吧。"
    window hide
    hide tubasa with dissolve
    show bg school_building_night with Dissolve(1.0)
    window show
    "我们来到外面，夕阳已经落山了。\n但余晖和摊位的灯光交相辉映，街上依然很热闹。"
    extend "\n在校园的正中央，大家为了御咲祭篝火晚会做准备，\n堆柴火的工作正在有序地进行。"
    window hide
    show bg schoolyard_night with Dissolve(1.0)
    show tubasa 5i at top with dissolve
    window show
    tubasa "一直工作到现在，有点累了呢。"
    extend "\n要不要找个地方坐下来休息一下？"
    me "是啊。"
    hide tubasa with dissolve
    "这么说着，我们两人\n在远离操场的草坪上坐了下来。"
    window hide
    show tubasa 12i at top with dissolve
    window show
    me "在这里的话，就能清楚地看到火焰，可以好好休息了。"
    tubasa "是啊……"
    hide tubasa with dissolve
    "远远眺望着，热闹非凡的学园祭的光景。"
    extend "\n然后"
    window hide
    play sound "fx/fire.ogg"
    show bg campfire with Radial(0.5)
    window show
    "终于点燃了柴火堆。"
    "熊熊燃烧着的鲜红火焰。"
    extend "\n真的好美啊……。"
    tubasa "哇……好厉害……！"
    me "嗯……。"
    stop sound fadeout 2.0
    window hide
    play music "good_atmosphere.ogg"
    show bg schoolyard_night with Dissolve(1.0)
    show tubasa 5i at top with dissolve
    window show
    tubasa "[player_name]君能和我一起看到这个，真的太好了！。"
    me "不是和友君，而是和我吗？"
    show tubasa 31i with dissolve
    tubasa "是的。"
    extend "\n当然，就算和友在一起也很不错，\n但御咲祭的最后，\n[player_name]君和我在一起就好。"
    show tubasa 5i with dissolve
    tubasa "我受了你很多照顾。"
    me "照顾……？"
    show tubasa 12i with dissolve
    tubasa "嗯。\n[player_name]君教会了我怎么变得勇敢。"
    extend "\n我总是很胆小，总是逃避各种各样的事情，\n[player_name]君一直在背后助我一臂之力。"
    me "……。"
    show tubasa 35i with dissolve
    tubasa "所以，[player_name]君对我而言，是非常重要的人。"
    extend "\n能像这样在一起很开心，也很高兴。"
    extend "\n[player_name]君在我身边，我能更积极地面对各种事。"
    extend "\n准备祭典的这段日子，我觉得我有了些改变……。"
    me "……是吗。\n能听到你这么说，我也很开心。"
    show tubasa 36i with dissolve
    tubasa "太好了……。"
    stop music fadeout 2.0
    hide tubasa with dissolve
    "之后，我们沉默着，一起享受了后夜祭的景色。"
    window hide
    play music "reminiscence.ogg"
    show cg c46 1 at center with FadeWhite(0.8)
    window show
    me "翼。"
    tubasa "嗯。"
    me "我有话想告诉你。"
    tubasa "什么？"
    me "……其实啊，我很喜欢你。"
    show cg c46 2 with Dissolve(0.8)
    tubasa "诶……！"
    me "嘿嘿嘿。"
    extend "\n起初，我只是打算撮合你和友的，"
    extend "\n但不知不觉，两颗心便渐行渐近，无法停止，\n不知不觉中，我就爱上了你。"
    me "我当然知道，小翼爱着友君。"
    extend "\n可是，这次我想任性一回，我想传达这份感情。\n不然的话，我一定会后悔的。"
    extend "\n……抱歉突然说这些。"
    show cg c46 3 with Dissolve(0.8)
    tubasa "嗯…。"
    me "果，果然还是很为难啊！！"
    extend "\n当然，我并没有要阻碍翼恋爱的打算！"
    extend "\n只是想鼓起勇气面对翼而已……"
    tubasa "……那，那个！"
    me "嗯？"
    tubasa "那个……就是…。"
    "翼扭扭捏捏地思考着什么。"
    show cg campfire with Dissolve(0.8)
    "但他很快就抬起头看着我。"
    tubasa "……[player_name]君。"
    extend "\n可，可以……闭上眼睛吗？"
    me "诶？可以是…。"
    tubasa "……。"
    me "……。"
    window hide
    show cg c46 4 with Radial(0.8)
    window show
    "亲"
    "……诶？"
    me "翼，翼……？"
    show cg c46 1 with Dissolve(0.8)
    tubasa "那，那个……那个……我好开心。"
    extend "\n[player_name]君是这样在想的。"
    me "翼……。"
    show cg c46 3 with Dissolve(0.8)
    tubasa "还，还有就是，"
    extend "\n[player_name]君，正因为有你，我才能变得这么勇敢"
    extend "\n这算是证明，同时也是对你的谢礼……。"
    me "……谢谢你。\n能得到你的回应，我也很幸福。"
    extend "\n还给了我一个吻……。"
    tubasa "呜……请不要把这种事说得这么直白啊！"
    extend "\n我可是很害羞的，也很紧张的啊……。"
    show bg schoolyard1_night
    me "啊哈哈。\n但只要有这份勇气，就一定没问题的。"
    extend "\n以后也继续加油吧。\n我会永远支持翼的。"
    window hide
    hide tubasa with Dissolve(0.9)
    hide cg with Dissolve(0.9)
    show tubasa 36i at top with Dissolve(0.9)
    window show
    tubasa "好的……我会努力的！！"
    window hide
    show cg moon_night at center with FadeWhite(0.8)
    window show
    "……这样一来，我的想法也传达给了翼，而翼也接受了我的表白。"
    extend "\n御咲祭也顺利举办了，我还在翼的陪伴下见证了这场焰火表演。"
    extend "\n愿望全都实现了。……"
    window hide
    show cg campfire_sparks with Dissolve(0.8)
    window show
    "在这片燃烧的红炎之中，我的意识逐渐淡去……。"
    extend "\n……梦已经结束了。"
    window hide
    hide bg with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    hide tubasa with Dissolve(0.8)
    window show
    "…"
    "梦的记忆是模糊的。"
    extend "\n在醒过来的同时，也会忘记这场梦。"
    extend "\n只留下甜美的回忆，其他的一切都被带去忘却的彼方而消散。"
    stop music fadeout 4.0
    "好了……差不多该起来了。"
    window hide
    show tubasa 35i at top with DefocusWhite(2.5)
    window show
    "翼，祝你幸福。"
    window hide
    hide tubasa with dissolve
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.6
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "哔哔哔哔哔哔哔哔"
    window hide
    show bg protagonist_room_morning at center with dissolve
    window show
    me "啊……已经早上了吗……？"
    extend "\n唔~我好像并没有睡多少啊……。"
    stop sound fadeout 0.5
    "我望向餐桌，上面放着一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……"
    extend "啊，对对对，昨天回来的时候拿到的。"
    extend "\n那些孩子们，真可爱啊……。"
    me "……好！那天我一定要去好好享受！"
    play sound "fx/cute2.ogg"
    extend "\n然后在脑海里尽情幻想！！"
    window hide
    hide bg with dissolve
    stop music fadeout 0.5
    window show
    "御咲祭当天ーーーーーー"
    window hide
    play music "school_festival.ogg"
    play sound "fx/crowd_noise.ogg"
    show bg school_building_full at center with Radial(1.0)
    pause 0.4
    show bg hallway with Dissolve(1.0)
    window show
    me "我想想……记得说是2年1班和2年2班的咖啡店。"
    extend "\n嗯？这里吗？"
    "正当我站在店门口犹豫不决的时候，"
    extend "\n三个与我差不多大的男生正在迷茫着，\n他们向店里的人打起了招呼。"
    window hide
    window show
    student_a "啊，喂~，我们来了。这里就是2年1，2班的咖啡馆吗？"
    show sinobu 12i at topright with dissolve
    unknown "啊，前几天真是多谢了。"
    extend "\n嗯，这里是咖啡厅。\n要是有客人光临的话，会由身带绿色名牌的人来负责接待。"
    student_b "哦，谢谢！"
    extend "\n这个不仅很重，还占地方，给你保管轻松多了！。"
    student_c "绝对不要摔了啊！！注意别弄掉了！！"
    "说着，他们便跟着身带绿色名牌的人走了进去。"
    window hide
    play sound "fx/sliding_door.ogg"
    hide sinobu with dissolve
    window show
    "看来，肯定就是在这里！！"
    extend "\n我鼓起自信，意气风发地走向咖啡店的入口。"
    play sound "fx/sliding_door.ogg"
    show bg cafe with FadeWhite(0.5)
    "然后，身带蓝色名牌的红领带男走了出来。"
    window hide
    play sound "fx/running.ogg"
    show tubasa 9i at top with dissolve
    window show
    tubasa "欢迎光临，客人。"
    show tubasa 35i with dissolve
    extend "\n是，是一位吗？"
    show tubasa 36i with dissolve
    extend "\n请往这边走……请慢慢欣赏。"
    window hide
    hide bg with Radial(1.0)
    hide sinobu with Radial(1.0)
    hide tubasa with Radial(1.0)
    pause 0.6
    show bg park_bench at center with Radial(0.7)
    pause 0.6
    show bg tubasa_ed with Dissolve(0.8)
    pause 1.3
    stop music fadeout 1.5
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.8
    hide bg with dissolve
    return

label end_sora:
    show bg cafe at center
    show sora 17i at top with dissolve
    window show
    "空从背后抱住了我，支撑着我。"
    show sora 23i with dissolve
    sora "[player_name]君，别勉强了。"
    extend "\n哥哥，我带着[player_name]君去保健室，\n找个人来这里帮忙吧！"
    hide sora with dissolve
    show tuki 5i at topleft with dissolve
    tuki "知道了。"
    extend "\n我这边一有空就过去。"
    extend "\n[player_surname]君就拜托给你了。"
    show sora 10i at topright with dissolve
    sora "包在我身上！"
    hide tuki with dissolve
    hide sora with dissolve
    stop music fadeout 2.0
    show sora 2i at top with dissolve
    extend "\n来，[player_name]君，能站起来吗？"
    extend "\n我扶着你走。"
    "空将我的手搭在他的肩上，扶我走向了保健室。"
    window hide
    hide sora with dissolve
    hide bg with dissolve
    show bg school_building_night at center with Dissolve(1.0)
    play music "good_atmosphere.ogg"
    window show
    doctor "37度4分……有点发烧呢。"
    extend "\n而且，还伴有站立性眩晕……怎么办？"
    extend "\n要早退，回家休息吗？"
    me "不，不用了……！"
    extend "\n我没事。\n我再在留在这里休息一会，肯定能好的。"
    doctor "但是呢，与之前不一样，这次是有发热症状，"
    extend "\n不要勉强，还是好好休息比较好哦？"
    me "我不会勉强的。"
    extend "\n好不容易才努力到现在的，\n在御咲祭结束之前，我绝对不想回去……！！"
    "我来到这个世界，就是为了和大家一起享受学园祭。"
    extend "\n如果在这里就回家的话，那我的梦想可能就破灭了。"
    extend "\n我绝对不想在最后什么回忆都没留下的情况下结束！"
    teacher "是吗……"
    extend "\n你们毕竟是执行委员呢~我能理解你们的心情。"
    extend "\n那么，去里面的床上好好休息吧。"
    extend "\n只是，不要太过勉强自己哦？"
    me "谢，谢谢您！"
    sora "谢谢老师！"
    extend "\n那么[player_name]君，走吧"
    window hide
    show bg infirmary_night with Dissolve(0.8)
    window show
    "我跟上次一样，躺在床上……"
    extend "不过这次是作为病人。"
    me "空，虽然我跟老师那样说，但这次我的身体真的是有点不对劲。"
    extend "\n或许还是不要待在我身边比较好，\n而且咖啡厅那边也很忙，还是先去那边吧。"
    extend "\n等我睡一会恢复一下，就会马上赶过去。"
    show sora 5i at top with dissolve
    sora "你在说什么啊！\n之前你明明说过离开的话会是寂寞的！"
    show sora 24i with dissolve
    extend "\n……别勉强了，没事的。\n这次我也会待在你身边的。"
    show sora 2i with dissolve
    sora "而且，我们也已经一起努力了这么长的时间。"
    extend "\n直到学园祭结束为止，都和我在一起吧。"
    show sora 32i with dissolve
    extend "\n等哥哥也来了之后，我们三个人再一起行动吧？"
    me "空……谢谢你。\n空真的是太温柔了。"
    extend "\n空的这一点我非常喜欢哟。"
    show sora 30i with dissolve
    sora "诶嘿嘿……。"
    extend "\n昨天，[player_name]君跟我说的我的优点，\n我今后也会一直保持的哟。"
    show sora 32i with dissolve
    sora "与哥哥不一样的，专属于我我的『强大』，"
    extend "\n今后也会一直磨练下去。"
    show sora 31i with dissolve
    sora "……谢谢你教了我这些，真的非常感谢。"
    me "嗯。\n如果是空的话，一定可以变得更强。"
    extend "我相信你。"
    extend "\n你们两个人一起的话，\n你们的祖先一定可以放心把道场交给你们的。"
    show sora 10i with dissolve
    sora "嗯！\n我，会和哥哥一起加油的。"
    hide sora with dissolve
    window hide
    play sound "fx/sliding_door.ogg"
    window show
    tuki "打扰了。"
    "月的声音从帘子的另一边传来。"
    teacher "哎呀，是赤峰君的哥哥吗。"
    extend "\n你弟弟和[player_surname]正在里面的床上休息呢。"
    tuki "我知道了。连日来多有打扰。"
    extend "\n谢谢老师，我先告辞了。"
    "与老师打完招呼后，月也来到床边。"
    window hide
    show tuki 9i at topleft with dissolve
    window show
    tuki "还好，找到代班的人了。"
    extend "\n人手足够，不必担心。"
    extend "\n其他的人都拜托我传话给你，让我代为转达『请多保重。』。"
    me "这样啊……给你添麻烦了，抱歉。"
    show tuki 1i with dissolve
    tuki "不用道歉的。"
    extend "\n是因为努力到现在，身体太累了才导致不适了吧。"
    extend "\n工作那么辛苦，好好休息吧。"
    show sora 2i at topright with dissolve
    sora "哥哥说得没错。"
    extend "\n早点恢复健康吧。"
    me "嗯……谢谢。"
    show sora 32i with dissolve
    sora "不过话说回来，大家也都很认可你呢。"
    show tuki 4i with dissolve
    tuki "学园祭期间，一直在一起呢。"
    extend "\n没想到居然会发展成这样，真是命运的安排啊。"
    me "啊哈哈。也算是命运共同体吧。"
    "我们三人在一起的时候最开心了。"
    extend "\n我觉得这不是因为把他们俩当正太看待，"
    extend "\n而是纯粹地喜欢上了这两个人。"
    extend "\n真是对好兄弟啊。"
    window hide
    show cg school_building1_night at center with Dissolve(0.8)
    window show
    me "……哈啊~。"
    extend "\n不过话说回来，我更想逛学园祭，\n不想躺在保健室的床上啊……"
    extend "\n对两位来说很抱歉，但只要现在能恢复，我们还是可以去逛的。"
    me "要是能像『沉睡森林的美男』那样接个吻，\n然后突然精神百倍的奇迹就发生就好了啊。"
    stop music fadeout 3.0
    "月和空面面相觑。"
    window hide
    play music "twins_theme.ogg"
    show cg c57 1 with FadeWhite(0.8)
    window show
    tuki "这样的话……那要不实际试试看？"
    me "哎？"
    tuki "空，轮到你了。"
    sora "诶，诶！？\n我，我！？"
    tuki "要是非要在我和空之中选一个的话，[player_surname]君肯定会选你的，这一点我还是很清楚的。"
    extend "\n而且，一直以来[player_surname]君也常常照顾你。"
    extend "\n致谢的话不能像跟对家里人说的一样。"
    extend "\n要以亲吻作为回礼[player_surname]君才能打起精神来。"
    play sound "fx/boing.ogg"
    me "诶诶！！\n真，真的可以吗！？"
    extend "\n我只是随口说的而已，怎么会发展成这样……。"
    tuki "嗯。"
    extend "\n现在，[player_surname]君的眼睛告诉我，你并没有别的什么奇怪的意图。"
    extend "\n既然如此，我也没有拒绝的理由了……"
    extend "恐怕空也是。"
    extend "\n而且，我也想咱们三个人一起逛学园祭啊。"
    show cg c57 2 with Dissolve(0.8)
    sora "……嗯，是啊。"
    extend "我也是。"
    extend "\n我也想咱们三个人一起开心地逛学园祭啊！"
    extend "\n既然有发生这种奇迹的可能性，\n[player_name]君的kiss应该……！"
    me "空……。"
    tuki "……但是，我可不想你们嘴对嘴亲哦。"
    sora "我，我知道啦！！！"
    extend "\n那这样的话，[player_name]君……可以吗？"
    me "嗯，嗯。"
    show cg red with Dissolve(0.8)
    "空把脸凑近我，在我的耳边轻声说着。"
    sora "我，[player_name]君，我喜欢你。"
    extend "\n所以……快点好起来吧。"
    window hide
    show cg c57 3 with Radial(0.8)
    window show
    "亲"
    "当我用脸感受到空那柔软的嘴唇，我的身体真的就变得轻飘飘的了。"
    me "谢谢，空……。"
    extend "\n多亏有你，我感觉身体轻松了许多。"
    show cg c57 4 with Dissolve(0.8)
    sora "……嗯。"
    extend "\n那样的话，真是太好了。"
    "空羞红了脸，这么回应着我。"
    tuki "那是当然，"
    extend "\n空的吻这么的可爱……不灵验才怪！！"
    sora "哥，哥哥……！！要被老师听到了啦。\n真，真是的……。"
    me "啊哈哈哈。"
    window hide
    hide cg with dissolve
    hide sora with dissolve
    hide tuki with dissolve
    window show
    "就在这时，操场上响起了欢呼声。"
    show tuki 15i at topleft with dissolve
    tuki "嗯？"
    extend "\n你们两个，快看窗户那边。"
    show sora 3i at topright with dissolve
    sora "哇……御咲篝火，终于点燃了！！"
    window hide
    play sound "fx/fire.ogg"
    show cg campfire at center with Radial(0.5)
    window show
    "时隔10年，我再次看到了篝火，即便只是在室内观赏，也非常美丽而震撼。"
    extend "\n从保健室的角度看，很巧妙地避开了草木和小摊，"
    extend "\n某种意义上说，也许这里就是个很好的秘密观赏点。"
    sora "好漂亮……！"
    extend "\n无论怎样，能和你们两人这样一起度过，太好了。"
    extend "\n一定，会成为非常美妙的回忆……。"
    me "我也是这么想的。"
    extend "\n能和喜欢的两人在一起，真的太好了。"
    extend "\n月，空……谢谢你们在我身边。"
    stop sound fadeout 2.0
    window hide
    hide tuki with Dissolve(0.8)
    hide sora with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    show sora 26i at topright
    show tuki 4i at topleft with dissolve
    window show
    tuki "啊。"
    sora "诶嘿嘿……不用谢！"
    window hide
    show cg moon_night at center with FadeWhite(0.8)
    window show
    "……这样，御咲祭也成功了，也和两人一起看到这场焰火了。"
    extend "\n愿望实现了。……"
    show cg campfire_sparks with Dissolve(0.8)
    "在这片燃烧的红炎之中，我的意识逐渐淡去……。"
    extend "\n……梦已经结束了。"
    window hide
    hide bg with dissolve
    hide cg with dissolve
    hide tuki with dissolve
    hide sora with dissolve
    window show
    "…"
    "梦的记忆是模糊的。"
    extend "\n在醒过来的同时，也会忘记这场梦。"
    extend "\n只留下甜美的回忆，其他的一切都被带去忘却的彼方而消散。"
    stop music fadeout 4.0
    "好了……差不多该起来了。"
    window hide
    show sora 30 at topright
    show tuki 9 at topleft with DefocusWhite(2.5)
    window show
    "空，"
    extend "月，"
    extend "\n谢谢你们。"
    window hide
    hide sora with Dissolve(0.8)
    hide tuki with Dissolve(0.8)
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.6
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "哔哔哔哔哔哔哔哔"
    window hide
    show bg protagonist_room_morning at center with dissolve
    window show
    me "啊……已经早上了吗……？"
    extend "\n唔~我好像并没有睡多少啊……。"
    stop sound fadeout 0.5
    "我望向餐桌，上面放着一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……"
    extend "啊，对对对，昨天回来的时候拿到的。"
    extend "\n那些孩子们，真可爱啊……。"
    me "……好！那天我一定要去好好享受！"
    play sound "fx/cute2.ogg"
    extend "\n然后在脑海里尽情幻想！！"
    window hide
    hide bg with dissolve
    stop music fadeout 0.5
    window show
    "御咲祭当天ーーーーーー"
    window hide
    play music "school_festival.ogg"
    play sound "fx/crowd_noise.ogg"
    show bg school_building_full at center with Radial(1.0)
    pause 0.4
    show bg hallway with Dissolve(1.0)
    window show
    me "我想想……记得说是2年1班和2年2班的咖啡店。"
    extend "\n唔？"
    play sound "fx/sliding_door.ogg"
    show bg cafe with dissolve
    extend "是这个吗？"
    "我还在店门口犹豫的时候，一个挂着红色名签的男孩注意到了我。"
    show tuki 5i at topleft with dissolve
    tuki "空，有客人来了哦。"
    hide tuki with dissolve
    "说着，挂着同样颜色的名签的男孩，\n穿着散发香气的制服，从店里出来了。"
    window hide
    play sound "fx/running.ogg"
    show sora 30i at top with dissolve
    window show
    sora "啊，欢迎光临！"
    extend "您是一个人吗？"
    show sora 31i with dissolve
    extend "\n请随意，好好享受吧！"
    window hide
    hide bg with Radial(1.0)
    hide sora with Radial(1.0)
    pause 0.6
    show bg akamine_house3 at center with Radial(0.7)
    pause 0.6
    show bg sora_ed with Dissolve(0.8)
    pause 1.3
    stop music fadeout 1.5
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.8
    hide bg with dissolve
    return

label end_tuki:
    show bg cafe at center
    show tuki 29i at top with dissolve
    window show
    "月抱住了我的身体，支撑着我。"
    show tuki 5i with dissolve
    tuki "[player_surname]，别勉强了。"
    extend "\n空，我带[player_surname]去保健室，你找个人来代一下班吧。"
    hide tuki with dissolve
    show sora 23i at topright with dissolve
    sora "知，知道了！"
    extend "\n我这边的工作做完也赶过去！"
    extend "\n[player_name]君，振作一点！！\n哥哥，之后就拜托你了！"
    stop music fadeout 2.0
    show tuki 17i at topleft with dissolve
    tuki "啊啊。"
    extend "\n[player_surname]，走吧。"
    "月说着，"
    play music "emergency.ogg"
    play sound "fx/sparkle.ogg"
    show cg remarkable at center with FadeWhite(0.5)
    extend "\n竟然将我公主抱了起来，就这样走出了教室。"
    play sound "fx/sliding_door.ogg"
    show cg hallway_evening with dissolve
    extend "\n这时我听到了其他学生们，还有在场的顾客们的欢呼声。"
    play sound "fx/boing.ogg"
    me "等，等一下，月……！"
    extend "\n这实在是太丢人了……！"
    tuki "现在是顾及这种事的时候吗！"
    extend "\n很快就到了，你就乖乖这样子别动。"
    me "呜呜……"
    "之后我依然受到了来自四面八方的视线洗礼，\n"
    stop music fadeout 2.0
    "十分羞耻的我闭上了眼睛，就这样被抱去了保健室。"
    window hide
    hide bg with dissolve
    hide tuki with dissolve
    hide cg with dissolve
    hide sora with dissolve
    show bg school_building_night at center with Dissolve(1.0)
    play music "good_atmosphere.ogg"
    window show
    doctor "37度4分……有点发烧呢。"
    extend "\n而且，还伴有站立性眩晕……怎么办？"
    extend "\n要早退，回家休息吗？"
    me "不，不用了……！"
    extend "\n我没事。\n我再在留在这里休息一会，肯定能好的。"
    doctor "但是呢，与之前不一样，这次是有发热症状，"
    extend "\n不要勉强，还是好好休息比较好哦？"
    me "我不会勉强的。"
    extend "\n好不容易才努力到现在的，\n在御咲祭结束之前，我绝对不想回去……！！"
    "我来到这个世界，就是为了和大家一起享受学园祭。"
    extend "\n如果在这里就回家的话，那我的梦想可能就破灭了。"
    extend "\n我绝对不想在最后什么回忆都没留下的情况下结束！"
    teacher "是吗……"
    extend "\n你们毕竟是执行委员呢~我能理解你们的心情。"
    extend "\n那么，去里面的床上好好休息吧。"
    extend "\n只是，不要太过勉强自己哦？"
    me "谢，谢谢您！"
    tuki "老师，真的非常感谢您。"
    extend "\n那么[player_surname]，走吧。"
    window hide
    show bg infirmary_night with Dissolve(0.8)
    window show
    "我跟上次一样，躺在床上……"
    extend "不过这次是作为病人。"
    me "月……虽然之前那样对你说过，但这次我的身体真的很难受。"
    extend "\n可能你别在这边陪着我比较好，\n而且咖啡厅也忙得不得了，你就去那里吧。"
    extend "\n等我睡一会恢复一下，就会马上赶过去。"
    show tuki 2i at top with dissolve
    tuki "这种时候就该只考虑自己的事情。"
    extend "\n而且，我的身体还很健壮的，"
    extend "\n我可不会因为一点小事就病倒，你就放心吧。"
    show tuki 5i with dissolve
    extend "\n在你身体好起来之前，我会一直陪在你身边。"
    me "月……谢谢你。"
    extend "\n月真的是坚强可靠……。"
    extend "\n我，最喜欢月这一点了。"
    show tuki 23i with dissolve
    tuki "突然说什么呢……！"
    show tuki 24i with dissolve
    extend "\n但是，既然你这么说，那我就欣然接受吧。"
    me "我也喜欢你这种害羞时可爱的样子。"
    show tuki 11i with dissolve
    tuki "！"
    show tuki 28i with dissolve
    extend "\n……我也喜欢你啊……整，整体上。"
    "月小声地说道。"
    me "啊哈哈。"
    extend "\n太好了呢~。"
    "要是平时的我，估计会高兴得跳起来。\n可现在的我，似乎没有那么大的体力了。"
    hide tuki with dissolve
    window hide
    play sound "fx/sliding_door.ogg"
    window show
    sora "失礼了。"
    "帘子的另一边，传来了空的声音。"
    doctor "啊呀，赤峰君的弟弟啊。"
    extend "\n你哥哥和[player_surname]正在里面的床上休息呢。"
    sora "我明白了。"
    extend "\n谢谢老师，我先告辞了。"
    "和医生说完后，空来到床边。"
    window hide
    show sora 3i at topright with dissolve
    window show
    sora "我找到人代班了。"
    extend "\n大家都待我向你转达『请保重。』"
    extend "\n大家都很担心你，要早点好起来呢。"
    me "这样啊……给你添麻烦了，抱歉。"
    show sora 1i with dissolve
    sora "没有必要道歉哦。"
    extend "\n[player_name]君一直以来都非常努力的在工作了。"
    extend "\n哪怕今天稍微休息一下，也不会有人说什么的。"
    show tuki 18i at topleft with dissolve
    tuki "没错。"
    extend "\n至少，我们最清楚你的努力。"
    extend "\n如果有人要责怪你，\n我会第一个站出来保护你的。"
    me "嗯……月要是能这么说的话，我就真的放心了。"
    show sora 32i with dissolve
    sora "不过话说回来，大家也都很认可你呢。"
    show tuki 4i with dissolve
    tuki "学园祭期间，一直在一起呢。"
    extend "\n没想到居然会发展成这样，真是命运的安排啊。"
    me "啊哈哈。也算是命运共同体吧。"
    "我们三人在一起的时候最开心了。"
    extend "\n这并不是因为我把两人当作正太来看待，\n而是纯粹地喜欢上了他们的为人。"
    extend "\n真是对好兄弟啊。"
    window hide
    show cg school_building1_night at center with Dissolve(0.8)
    window show
    me "……哈啊~。"
    extend "\n不过话说回来，我更想逛学园祭，\n不想躺在保健室的床上啊……"
    extend "\n对两位来说很抱歉，但只要现在能恢复，我们还是可以去逛的。"
    me "要是能像『沉睡森林的美男』那样接个吻，\n然后突然精神百倍的奇迹就发生就好了啊。"
    stop music fadeout 3.0
    "月和空面面相觑。"
    window hide
    play music "twins_theme.ogg"
    show cg c63 1 with FadeWhite(0.8)
    window show
    sora "……那要不试试看？"
    me "哎？"
    sora "刚才说过的，引起觉醒的奇迹之吻……。"
    extend "\n这种情况下，应该是治好感冒的吻吧。"
    extend "\n……如果是这样的话，亲吻的人应该是哥哥吧~。"
    tuki "什么啊，为什么是我啊……？"
    sora "因为，要是说到我和哥哥的话，\n[player_name]君会选哥哥吧。"
    extend "\n之前看哥哥的眼神也有点在意的样子！"
    extend "\n……哥哥也不是完全不情愿的吧？"
    play sound "fx/boing.ogg"
    me "诶！！\n真的吗！？"
    tuki "……。"
    me "我只是说着玩的而已，竟然发展成……。"
    sora "嗯。"
    extend "\n[player_name]君的眼睛告诉我，你现在并没有奇怪的想法。"
    extend "\n既然如此，我也没理由责备你……。"
    extend "\n况且我也想咱们三个人一起逛学园祭。"
    show cg c63 2 with Dissolve(0.8)
    tuki "……是啊。"
    extend "我的想法也和你们一样。"
    extend "\n既然有发生这种奇迹的可能性，\n[player_surname]君的kiss，我也很开心。"
    me "月……。"
    sora "……但是，得是亲在脸上！"
    extend "\n要是亲嘴的话我可饶不了你哦。"
    tuki "这，这点我还是知道的！"
    extend "\n那么，[player_surname]……准备好了吗？"
    me "嗯，嗯。"
    show cg red with Dissolve(0.8)
    "月把脸凑近我。"
    tuki "快点……振作起来吧。"
    window hide
    show cg c63 3 with Radial(0.8)
    window show
    "亲"
    "月柔软的嘴唇贴到我的脸上后，我感觉身体真的变轻了。"
    me "谢谢你，月。"
    extend "\n多亏有你，我感觉身体真的放松下来了。"
    show cg c63 4 with Dissolve(0.8)
    tuki "……嗯。"
    extend "\n那就好。"
    "月羞红了脸。"
    sora "啊，哥哥又脸红了~。"
    me "真的诶~好可爱♪"
    show cg c63 5 with dissolve
    tuki "喂，喂！！\n不要再提起这个了……。"
    sora "哈哈哈。"
    extend "\n……太好了，[player_name]君。"
    me "嗯。"
    extend "\n空谢谢你了。"
    sora "诶嘿嘿。"
    extend "\n不用客气！"
    window hide
    hide cg with dissolve
    hide sora with dissolve
    hide tuki with dissolve
    window show
    "就在这时，操场上响起了欢呼声。"
    show tuki 15i at topleft with dissolve
    tuki "嗯？"
    extend "\n你们两个，快看窗户那边。"
    show sora 3i at topright with dissolve
    sora "哇……御咲篝火，终于点燃了！！"
    window hide
    play sound "fx/fire.ogg"
    show cg campfire at center with Radial(0.5)
    window show
    "在室内也能够清晰地看到，时隔10年之后再次盛绽的焰火。"
    extend "\n从保健室的角度看，很巧妙地避开了草木和小摊，"
    extend "\n某种意义上说，也许这里就是个很好的秘密观赏点。"
    tuki "好美……。"
    extend "\n虽然是在保健室，但这段时光咱们能三个人一起度过，真好。"
    extend "\n这也肯定会成为我们美好的回忆。"
    me "我也是这么想的。"
    extend "\n能和喜欢的两人在一起，真的太好了。"
    extend "\n月，空……谢谢你们在我身边。"
    stop sound fadeout 2.0
    window hide
    hide tuki with Dissolve(0.8)
    hide sora with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    show sora 26i at topright
    show tuki 4i at topleft with dissolve
    window show
    tuki "啊。"
    sora "诶嘿嘿……不用谢！"
    window hide
    show cg moon_night at center with FadeWhite(0.8)
    window show
    "……这样，御咲祭也成功了，也和两人一起看到这场焰火了。"
    extend "\n愿望实现了。……"
    show cg campfire_sparks with Dissolve(0.8)
    "在这片燃烧的红炎之中，我的意识逐渐淡去……。"
    extend "\n……梦已经结束了。"
    window hide
    hide bg with dissolve
    hide cg with dissolve
    hide tuki with dissolve
    hide sora with dissolve
    window show
    "…"
    "梦的记忆是模糊的。"
    extend "\n在醒过来的同时，也会忘记这场梦。"
    extend "\n只留下甜美的回忆，其他的一切都被带去忘却的彼方而消散。"
    stop music fadeout 4.0
    "好了……差不多该起来了。"
    window hide
    show tuki 24 at topleft
    show sora 26 at topright with DefocusWhite(2.5)
    window show
    "月，"
    extend "空，"
    extend "\n谢谢你们。"
    window hide
    hide sora with Dissolve(0.8)
    hide tuki with Dissolve(0.8)
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.6
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "哔哔哔哔哔哔哔哔"
    window hide
    show bg protagonist_room_morning at center with dissolve
    window show
    me "啊……已经早上了吗……？"
    extend "\n唔~我好像并没有睡多少啊……。"
    stop sound fadeout 0.5
    "我望向餐桌，上面放着一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……"
    extend "啊，对对对，昨天回来的时候拿到的。"
    extend "\n那些孩子们，真可爱啊……。"
    me "……好！那天我一定要去好好享受！"
    play sound "fx/cute2.ogg"
    extend "\n然后在脑海里尽情幻想！！"
    window hide
    hide bg with dissolve
    stop music fadeout 0.5
    window show
    "御咲祭当天ーーーーーー"
    window hide
    play music "school_festival.ogg"
    play sound "fx/crowd_noise.ogg"
    show bg school_building_full at center with Radial(1.0)
    pause 0.4
    show bg hallway with Dissolve(1.0)
    window show
    me "我想想……记得说是2年1班和2年2班的咖啡店。"
    extend "\n唔？"
    play sound "fx/sliding_door.ogg"
    show bg cafe with dissolve
    extend "是这个吗？"
    "我还在店门口犹豫的时候，一个挂着红色名签的男孩注意到了我。"
    show sora 3i at topright with dissolve
    sora "哥哥，好像有客人来了，拜托你啦！"
    hide sora with dissolve
    "说着，挂着同样颜色的名签的男孩，\n穿着散发香气的制服，从店里出来了。"
    window hide
    play sound "fx/running.ogg"
    show tuki 24i at top with dissolve
    window show
    tuki "让您久等了。\n欢迎光临。"
    extend "您是一个人来吗？"
    show tuki 25i with dissolve
    extend "\n请慢慢享受吧。"
    window hide
    hide bg with Radial(1.0)
    hide tuki with Radial(1.0)
    pause 0.6
    show bg akamine_house1_evening at center with Radial(0.7)
    pause 0.6
    show bg tuki_ed with Dissolve(0.8)
    pause 1.3
    stop music fadeout 1.5
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.8
    hide bg with dissolve
    return

label end_futago:
    show bg cafe at center
    show tuki 29i at topleft
    show sora 17i at topright with dissolve
    window show
    "2人将我的身体抱在怀中，支撑着我。"
    show tuki 5i with dissolve
    tuki "[player_surname]别硬撑了。"
    show sora 23i with dissolve
    sora "就是啊。"
    extend "\n我们现在就把你送到保健室！"
    window hide
    hide tuki with dissolve
    hide sora with dissolve
    show sora 5i at topright with dissolve
    window show
    sora "忍同学！"
    show sinobu 9i at top with dissolve
    sinobu "怎么了？"
    show sinobu 28i with dissolve
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    extend "\n啊，[player_surname]君，没事吧……！？"
    show tuki 5i at topleft with dissolve
    tuki "看样子他好像是发烧了。"
    extend "\n不好意思[player_surname]君得跟我去保健室，得有人代班"
    extend "\n有谁可以帮忙代班吗？"
    show sinobu 7i with dissolve
    sinobu "嗯……我知道了。"
    extend "\n我也会告诉大家的……。"
    show sinobu 27i with dissolve
    extend "\n[player_surname]君，你好好休息。"
    me "谢，谢谢…。"
    play sound "fx/running.ogg"
    hide sinobu with dissolve
    "说完，忍就回到自己的岗位上了。"
    hide sora with dissolve
    hide tuki with dissolve
    show sora 22i at top with dissolve
    sora "好。\n那我们出发吧！"
    extend "\n[player_name]君，我们来撑着你，要好好的！"
    window hide
    stop music fadeout 2.0
    play sound "fx/sliding_door.ogg"
    show cg hallway_evening at center with dissolve
    window show
    "我把双手搭在月和空的肩上，被他们带到了保健室。"
    "周围有很多同学都在看着我们。"
    hide bg with dissolve
    hide tuki with dissolve
    hide cg with dissolve
    hide sora with dissolve
    play sound "fx/triangle.ogg"
    extend "\n我的样子，一定就像被囚禁的外星人一样吧……。"
    window hide
    show bg school_building_night at center with Dissolve(1.0)
    play music "good_atmosphere.ogg"
    window show
    doctor "37度4分……有点发烧呢。"
    extend "\n而且，还伴有站立性眩晕……怎么办？"
    extend "\n要早退，回家休息吗？"
    me "不，不用了……！"
    extend "\n我没事。\n我再在留在这里休息一会，肯定能好的。"
    teacher "但是，这次跟上次不一样，你发烧了，\n不要逞强了，好好休息吧？"
    me "我不会勉强的。"
    extend "\n好不容易才努力到现在的，\n在御咲祭结束之前，我绝对不想回去……！！"
    "我来到这个世界，就是为了和大家一起享受学园祭。"
    extend "\n如果在这里就回家的话，那我的梦想可能就破灭了。"
    extend "\n我绝对不想在最后什么回忆都没留下的情况下结束！"
    teacher "是吗……"
    extend "\n你们毕竟是执行委员呢~我能理解你们的心情。"
    extend "\n那么，去里面的床上好好休息吧。"
    extend "\n只是，不要太过勉强自己哦？"
    me "谢，谢谢您！"
    sora "太好了，[player_name]君。"
    tuki "那我们走吧。"
    window hide
    show bg infirmary_night with Dissolve(0.8)
    window show
    "我跟上次一样，躺在床上……"
    extend "不过这次是作为病人。"
    me "你们两个……这次我是真的身体不舒服。"
    extend "\n或许还是不要待在我身边比较好，\n而且咖啡厅那边也很忙，还是先去那边吧。"
    extend "\n等我睡一会恢复一下，就会马上赶过去。"
    show sora 5i at topright with dissolve
    sora "说什么胡话呢！"
    extend "\n你之前还说如果离开的话会寂寞！"
    show tuki 18i at topleft with dissolve
    tuki "不要逞强了。"
    extend "\n放心吧，我们会一直待在你身边，直到你恢复为止。"
    show sora 24i with dissolve
    sora "就是啊。"
    extend "\n而且，我们之前都那么努力。"
    show sora 26i with dissolve
    extend "\n在学园祭结束之前，咱们就一起过吧。"
    me "月，空……谢谢你们。\n你们俩真的太温柔了。"
    extend "\n我特别喜欢你们的这种性格。"
    extend "\n正因如此，和你们在一起，让我感觉很安心。"
    show sora 30i with dissolve
    sora "诶嘿嘿。\n我们才要说谢谢呢！"
    extend "\n我们也是，和你一样的感觉。"
    show tuki 24i with dissolve
    tuki "啊。\n只要我们三个人在一起，感觉就特别安心。"
    me "……你们能这么说，我真的好高兴。"
    "我这么说完，两人看着我露出了笑容。"
    show sora 32i with dissolve
    sora "不过话说回来，大家也都很认可你呢。"
    show tuki 4i with dissolve
    tuki "学园祭期间，一直在一起呢。"
    extend "\n没想到居然会发展成这样，真是命运的安排啊。"
    me "啊哈哈。也算是命运共同体吧。"
    "我们三人在一起的时候最开心了。"
    extend "\n这并不是因为我把两人当作正太来看待，\n而是纯粹地喜欢上了他们的为人。"
    extend "\n真是对好兄弟啊。"
    window hide
    show cg school_building1_night at center with Dissolve(0.8)
    window show
    me "……哈啊~。"
    extend "\n不过话说回来，我更想逛学园祭，\n不想躺在保健室的床上啊……"
    extend "\n对两位来说很抱歉，但只要现在能恢复，我们还是可以去逛的。"
    me "要是能像『沉睡森林的美男』那样接个吻，\n然后突然精神百倍的奇迹就发生就好了啊。"
    "月和空面面相觑。"
    hide cg with dissolve
    hide tuki with dissolve
    hide sora with dissolve
    show tuki 25i at topleft with dissolve
    tuki "空，这样可以吗？"
    show sora 30i at topright with dissolve
    sora "嗯。"
    extend "\n哥哥？"
    stop music fadeout 3.0
    show tuki 24i with dissolve
    tuki "我也没意见。"
    "两人似乎商量了些什么，然后看向我。"
    window hide
    play music "twins_theme.ogg"
    show cg c64 1 at center with FadeWhite(0.8)
    window show
    sora "[player_name]君，要试试吗？"
    me "哎？"
    tuki "就是你刚才说的那个，可以唤醒奇迹的接吻。"
    extend "\n不过，在这种情况下，应该是治愈感冒之吻。"
    me "诶？诶？？"
    sora "我们已经准备好亲你了哦。"
    tuki "啊啊。"
    extend "\n[player_surname]如果这个吻有可能让你恢复健康的话，\n我们没有理由拒绝。"
    sora "我们也最喜欢你了，[player_name]君！"
    play sound "fx/boing.ogg"
    me "真，真的吗！？"
    extend "\n我只是随口说的而已，怎么会发展成这样……。"
    tuki "正因如此。"
    extend "\n现在，[player_surname]君的眼神是纯粹的。"
    extend "\n所以，你就好好地\n接受我们的心意吧。"
    sora "当然，如果你不愿意的话我不会强求……。"
    play sound "fx/cute2.ogg"
    me "不不不！！不是，我怎么会不愿意！！"
    extend "\n我超高兴啊！！！"
    show cg red with Dissolve(0.8)
    extend "\n……我真是幸福啊。"
    "他们听到我的回答后，站到床的两端，然后把脸凑到我面前。"
    tuki_and_sora "快点打起精神来吧。"
    window hide
    show cg c64 2 with Radial(0.8)
    window show
    "亲"
    "得到脸颊两边那柔软的唇的触感，我的身体真的变得轻飘飘起来。"
    me "……感觉，身体真的变轻了…。"
    show cg c64 3 with Dissolve(0.8)
    sora "是吗……那真是太好了。"
    tuki "因为你确实将思念融入其中。"
    extend "\n而且貌似也确实传达到了，太好了。"
    me "谢谢你们两位。"
    window hide
    hide cg with dissolve
    hide sora with dissolve
    hide tuki with dissolve
    window show
    "这时，从学校操场那边传来了欢呼声。"
    show tuki 15i at topleft with dissolve
    tuki "嗯？"
    extend "\n你们两个，快看窗户那边。"
    show sora 3i at topright with dissolve
    sora "哇……御咲篝火，终于点燃了！！"
    window hide
    play sound "fx/fire.ogg"
    show cg campfire at center with Radial(0.5)
    window show
    "时隔10年，我再次看到了篝火，即便只是在室内观赏，也非常美丽而震撼。"
    extend "\n从保健室的角度看，很巧妙地避开了草木和小摊，"
    extend "\n某种意义上说，也许这里就是个很好的秘密观赏点。"
    sora "好漂亮……！"
    extend "\n无论怎样，能和你们两人这样一起度过，太好了。"
    extend "\n一定，会成为非常美妙的回忆……。"
    me "我也是这么想的。"
    extend "\n能和喜欢的两人在一起，真的太好了。"
    extend "\n月，空……感谢你们一直在我身边。"
    stop sound fadeout 2.0
    window hide
    hide tuki with Dissolve(0.8)
    hide sora with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    show sora 26i at topright
    show tuki 4i at topleft with dissolve
    window show
    tuki "啊。"
    sora "诶嘿嘿……不用谢！"
    window hide
    show cg moon_night at center with FadeWhite(0.8)
    window show
    "……这样，御咲祭也成功了，也和两人一起看到这场焰火了。"
    extend "\n愿望实现了。……"
    show cg campfire_sparks with Dissolve(0.8)
    "在这片燃烧的红炎之中，我的意识逐渐淡去……。"
    extend "\n……梦已经结束了。"
    window hide
    hide bg with dissolve
    hide cg with dissolve
    hide tuki with dissolve
    hide sora with dissolve
    window show
    "…"
    "梦的记忆是模糊的。"
    extend "\n在醒过来的同时，也会忘记这场梦。"
    extend "\n只留下甜美的回忆，其他的一切都被带去忘却的彼方而消散。"
    stop music fadeout 4.0
    "好了……差不多该起来了。"
    window hide
    show tuki 24 at topleft
    show sora 30 at topright with DefocusWhite(2.5)
    window show
    "月，"
    extend "空，"
    extend "谢谢你们。"
    window hide
    hide sora with Dissolve(0.8)
    hide tuki with Dissolve(0.8)
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.4
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "哔哔哔哔哔哔哔哔"
    window hide
    show bg protagonist_room_morning at center with dissolve
    window show
    me "啊……已经早上了吗……？"
    extend "\n唔~我好像并没有睡多少啊……。"
    stop sound fadeout 0.5
    "我望向餐桌，上面放着一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……"
    extend "啊，对对对，昨天回来的时候拿到的。"
    extend "\n那些孩子们，真可爱啊……。"
    me "……好！那天我一定要去好好享受！"
    play sound "fx/cute2.ogg"
    extend "\n然后在脑海里尽情幻想！！"
    window hide
    hide bg with dissolve
    stop music fadeout 0.5
    window show
    "御咲祭当天ーーーーーー"
    window hide
    play music "school_festival.ogg"
    play sound "fx/crowd_noise.ogg"
    show bg school_building_full at center with Radial(1.0)
    pause 0.4
    show bg hallway with Dissolve(1.0)
    window show
    me "我想想……记得说是2年1班和2年2班的咖啡店。"
    extend "\n唔？"
    play sound "fx/sliding_door.ogg"
    show bg cafe with dissolve
    extend "是这个吗？"
    "正当我在店门口感到迷茫时，两个散发着甜美香气，身着制服，身上挂着红色名牌的\n男生同时注意到了我，并走了过来。"
    window hide
    play sound "fx/running.ogg"
    show sora 3i at topright with dissolve
    window show
    sora "欢迎光临！请问是一个人吗？"
    window hide
    play sound "fx/running.ogg"
    show tuki 15i at topleft with dissolve
    window show
    tuki "请跟我来。"
    show tuki 25i
    show sora 31i with dissolve
    tuki_and_sora "请慢慢享受！"
    window hide
    hide bg with Radial(1.0)
    hide tuki with Radial(1.0)
    hide sora with Radial(1.0)
    pause 0.6
    show bg infirmary at center with Radial(0.7)
    pause 0.6
    show bg twins_ed with Dissolve(0.8)
    pause 1.3
    stop music fadeout 1.5
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.8
    hide bg with dissolve
    return

label day4_1_futago:
    show bg cafe at center with dissolve
    play music "twins_theme.ogg"
    show sora 22i at topright
    show tuki 2i at topleft with dissolve
    window show
    tuki "不好意思，到此结束。"
    sora "[player_name]君！！趁现在到这边来！"
    me "你们两个！"
    customer3 "怎，怎么会这样！"
    show sora 28i
    show tuki 5i with dissolve
    tuki "就算是客人，也不能做出这种无礼的行为。"
    sora "我们是不欢迎不遵守规则的人来的。"
    play sound "fx/boing.ogg"
    customer3 "呜……抱，抱歉了捏。"
    extend "\n有，有点兴奋过头，所以有点不守规矩了捏。"
    play sound "fx/cute3.ogg"
    customer5 "对不起呀。"
    extend "\n这里还是绅士一点，姑且忍一忍，可远观不可亵玩焉。"
    play sound "fx/sparkle.ogg"
    customer4 "正义感强烈的男孩子真是棒呀♪"
    window hide
    hide tuki with dissolve
    hide sora with dissolve
    window show
    "有了月和空的帮助，我顺利地度过了这一关。"
    "没想到在这种时候还能被初中生搭救……。"
    extend "\n总感觉有点丢人啊……。"
    window hide
    show tuki 6i at topleft with dissolve
    window show
    tuki "[player_surname]，你没事吧？"
    me "嗯，嗯嗯。得救了。"
    extend "\n谢谢你们！"
    show sora 2i at topright with dissolve
    sora "不客气。"
    show sora 5i with dissolve
    extend "\n不过话说回来，[player_name]君。"
    extend "\n我今天就觉得你的脸色很差啊？"
    me "诶……有吗？"
    "可能是专注于活动而没有注意到，\n说起来，感觉今天身体莫名地沉重……。"
    "呜……意识到之后，就开始难受起来了……。"
    stop music fadeout 5.0
    show tuki 16i with dissolve
    tuki "喂，[player_surname]！没事吧？\n你怎么左摇右摆的？"
    me "没事，没事……！\n稍，稍微休息一下，马上就……。"
    window hide
    hide tuki with dissolve
    hide sora with dissolve
    play music "serious.ogg"
    window show
    "我软弱地瘫坐在休息室的椅子上。"
    "不妙啊……最近是不是太拼导致身体出问题了……？"
    extend "\n剧烈的环境变化会带来很大的精神压力啊。"
    extend "\n梦里居然还能这么真实，真是可笑……。"
    show sora 4i at topright with dissolve
    sora "[player_name]君，让我看看。"
    "空一边说着，一边把手放在我的额头上。"
    show sora 22i with dissolve
    sora "……果然发烧了，哥哥！"
    show tuki 15i at topleft with dissolve
    tuki "嗯。"
    extend "\n[player_surname]，现在就带你去医务室吧。"
    me "都，都说了没事的！"
    extend "\n这点小烧……上班可不能请假啊……。"
    "虽然我虚张声势地想站起身来，但实在是使不上力。"
    extend "\n看来孩子的体力和大人之间还是有着相当大的差距。"
    play sound "fx/boing.ogg"
    me "呜…。"
    hide tuki with dissolve
    hide sora with dissolve
    hide bg with dissolve
    play sound "fx/fall_down.ogg"
    "视野开始摇晃，我失去了平衡。"
    "……啾"
    window hide
    return

label end_saburo:
    show bg cafe at center with dissolve
    play music "saburo_theme.ogg"
    show saburo 33i me at top with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    window show
    saburo "别，别闹了你们！！够了！"
    me "三朗！"
    customer3 "怎，怎么了！"
    extend "\n嗯……？"
    extend "总感觉在哪里见过你……。"
    show saburo 33i me with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    saburo "可，可能是你的错觉……。"
    extend "不对，一定是错觉……！"
    extend "\n好，好了，现在立刻放开[player_surname]君的手~！"
    extend "\n不然的话，我就要找老师说，让他把你们赶走了哦……！？"
    play sound "fx/boing.ogg"
    customer3 "呜……抱，抱歉了捏。"
    extend "\n有，有点兴奋过头，所以有点不守规矩了捏。"
    play sound "fx/cute3.ogg"
    customer5 "对不起呀。"
    extend "\n这里还是绅士一点，姑且忍一忍，可远观不可亵玩焉。"
    play sound "fx/sparkle.ogg"
    customer4 "正义感强烈的男孩子真是棒呀♪"
    window hide
    hide saburo with dissolve
    window show
    "三朗救了我一命，我总算是挺过了这次危机。"
    "没想到这种场合下救我的居然是初中生……。"
    extend "\n总感觉有点丢人啊……。"
    window hide
    show saburo 17i me at top with dissolve
    window show
    saburo "[player_surname]，你没事吧？"
    me "啊，嗯，得救了，谢谢！"
    extend "\n不过话说回来，三朗你原来戴着眼镜来着？"
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    show saburo 8i with dissolve
    saburo "没，没有，不过戴上也没关系吧。"
    extend "\n不用在意。"
    me "是，是这样啊。"
    show saburo 28i with dissolve
    saburo "比起这个，[player_surname]。"
    extend "\n今天后夜祭你有事吗？"
    me "诶？不，还没有安排。"
    show saburo 29i with dissolve
    saburo "这样啊！"
    extend "\n那要不跟我一起逛？"
    me "好啊，其他人呢？"
    show saburo 26i with dissolve
    saburo "呜……那个……那个，就是。"
    extend "\n两个人的话，那个……那个……。"
    show saburo 28i with dissolve
    extend "\n不对，你明明懂我的意思的吧！\n你不是内心已经是大人了吗！"
    me "啊……嗯，可以啊！"
    extend "\n那就在鞋柜那碰头吧。"
    show saburo 30i with dissolve
    saburo "哦，行。"
    extend "\n那我就回去工作了。"
    window hide
    play sound "fx/running.ogg"
    hide saburo with dissolve
    window show
    "三朗要跟我单独在一起，该不会有什么重要的事吧？"
    "……。"
    play sound "fx/heartbeat.ogg"
    show cg light-blue at center with dissolve
    "难不成……呃，我怎么心跳加速了！"
    extend "\n不过，按这个展开，应该是那种经典的那种情节吧……那个……。"
    "……嘛，稍微期待一下也行。"
    hide cg with dissolve
    hide bg with dissolve
    stop music fadeout 2.0
    "……毕竟这个梦不知道会持续到什么时候……。"
    window hide
    play sound "fx/crowd_noise.ogg"
    show bg school_building_evening_full at center with Dissolve(1.0)
    pause 0.4
    show bg cafe_evening with Radial(1.0)
    window show
    "咖啡店的营业时间也差不多要结束了。"
    extend "\n剩下的活动，就是和三朗一起的后夜祭！"
    extend "\n因为不能迟到，所以我赶紧收拾东西。"
    play sound "fx/sliding_door.ogg"
    window hide
    show bg hallway_evening with dissolve
    play music "sintarou_theme.ogg"
    show sintarou 1i at top with dissolve
    window show
    sintarou "哟，[player_name]酱！"
    extend "\n看你这么着急是要去哪？"
    "我正准备去换鞋时，慎太郎过来说话了。"
    me "那个……我在等三朗。"
    show sintarou 18i with dissolve
    sintarou "哼嗯。"
    extend "\n三朗酱果然是这样啊。"
    me "“果然是这样”是什么意思？"
    show sintarou 29i with dissolve
    sintarou "这还不能说。"
    extend "\n你迟早会知道的！"
    me "唔~？"
    extend "\n我有点搞不懂啊。"
    show sintarou 31i with dissolve
    sintarou "没事没事，不用介意！"
    show sintarou 30i with dissolve
    extend "\n比起这个，[player_name]君你到底是用了什么手法，\n才能把三朗引到这边来的？"
    extend "\n你也教教我，那个技术吧~。"
    me "诶，嗯……什么引到这边来呀，我只是稍稍辅助了他一下而已哦。"
    show sintarou 28i with dissolve
    sintarou "辅助？？那是什么？"
    me "就像合气道一样，如果从这边强行加上了力量，\n反而对手也会用力，身体会僵硬的。"
    extend "\n所以，要顺着对手力量的方向，加以利用。"
    me "就三朗来说，他自身其实也向着这边，所以"
    extend "\n也没必要改变他。"
    me "而是让他自己承认自己的不同，并面对它。"
    show sintarou 35i with dissolve
    sintarou "……嗯。"
    extend "虽然感觉有点难，但总的来说\n就是不强行把他拉过来，而是在他背后轻轻地推他一把。"
    extend "\n咱完全没有学习过这种方法。"
    show sintarou 23i with dissolve
    extend "\n原来是要借力啊……。"
    show sintarou 30i with dissolve
    sintarou "是啊。"
    extend "\n所以三朗酱他也是朝着[player_name]君的方向去的。"
    show sintarou 20i with dissolve
    extend "\n咱也是从像[player_name]这样的人中学到了好多东西呢。"
    me "慎太郎君，怎么了？"
    show sintarou 8i with dissolve
    sintarou "哎呀抱歉！"
    extend "\n没什么，自说自话！"
    show sintarou 9i with dissolve
    extend "\n不过啊，[player_name]酱看起来真的很有大人样啊！"
    extend "\n难道说内在是25岁左右的大人了吗？"
    play sound "fx/boing.ogg"
    "咿，咿咕！"
    me "怎，怎么可能呢！"
    extend "\n这种奇怪的话，只在梦里说就够了。"
    show sintarou 1i with dissolve
    sintarou "啊哈哈！"
    extend "说得也是。"
    extend "\n那我就回大部队了。"
    extend "\n拜拜！三朗酱可就拜托你了！！"
    me "……嗯，我知道了。"
    window hide
    hide sintarou with dissolve
    hide bg with dissolve
    stop music fadeout 0.5
    window show
    "…"
    window hide
    play music "fx/night_insects.ogg"
    show bg shoe_locker_night at center with Dissolve(0.8)
    window show
    "和慎太郎分开后，我便回到鞋柜前，三朗已经在那里等着了。"
    show saburo 1i at top with dissolve
    saburo "啊，[player_surname]！你来得好晚啊~。"
    me "抱歉抱歉！"
    extend "\n稍微和慎太郎聊了几句。"
    show saburo 6i with dissolve
    saburo "和他？"
    show saburo 10i with dissolve
    extend "\n……算了。先出发吧。"
    extend "\n外面也相当热闹呢！"
    window hide
    hide saburo with dissolve
    show bg school_building_night with Dissolve(1.0)
    window show
    "我们来到外面，夕阳已经落山了。\n但余晖和摊位的灯光交相辉映，街上依然很热闹。"
    extend "\n在校园的正中央，大家为了御咲祭篝火晚会做准备，\n堆柴火的工作正在有序地进行。"
    window hide
    show bg schoolyard_night with Dissolve(1.0)
    show saburo 11i at top with dissolve
    window show
    saburo "虽然我想去很多地方，但一直工作太累了~。"
    extend "\n稍微找个地方坐下休息一下吧？"
    me "说的是。"
    hide saburo with dissolve
    "这么说着，我们两人\n在远离操场的草坪上坐了下来。"
    window hide
    show saburo 1i at top with dissolve
    window show
    me "在这里的话，就能清楚地看到火焰，可以好好休息了。"
    saburo "是啊……。"
    hide saburo with dissolve
    "远远眺望着，热闹非凡的学园祭的光景。"
    extend "\n然后"
    window hide
    play sound "fx/fire.ogg"
    show bg campfire with Radial(0.5)
    window show
    "终于点燃了柴火堆。"
    "熊熊燃烧着的鲜红火焰。"
    extend "\n真的好美啊……。"
    saburo "……真好啊，这种感觉。"
    extend "\n好安心啊……。"
    me "是啊……。"
    stop sound fadeout 2.0
    window hide
    play music "good_atmosphere.ogg"
    show bg schoolyard_night with Dissolve(1.0)
    show saburo 26i at top with dissolve
    window show
    saburo "……呐，[player_surname]。"
    extend "\n[player_surname]，你现在在谈恋爱吗？"
    "三朗唐突的提问，让我不由得心跳加速。"
    me "诶？怎，怎么了？？这么突然。"
    show saburo 31i with dissolve
    saburo "别，别管了回答我啊~！"
    extend "\n谈了吗？"
    me "嗯，嗯~。"
    extend "\n怎么说呢……"
    extend "确实有点被那个人吸引了，\n但这也算是恋爱吗……"
    extend "\n友情和恋爱感情之间的界限好难分啊。"
    show saburo 4i with dissolve
    saburo "难道不应该更加凭直觉吗？"
    me "啊哈哈，是啊。"
    extend "\n大概，就这样吧。"
    show saburo 9i with dissolve
    saburo "什么啊那是~。"
    extend "\n光是说这些，又回答得相当随便呢。"
    me "恋爱这种东西，每个人都不太一样，不是很复杂吗？"
    extend "\n所以，三朗君怎么样了呢？"
    extend "\n现在，恋爱了吗？"
    show saburo 26i with dissolve
    saburo "唔……我，我……那个……。"
    "三朗含糊其辞。"
    me "看你的反应，肯定是有了吧。"
    show saburo 31i with dissolve
    stop music fadeout 2.0
    saburo "……对。"
    extend "\n大概，这就是这种感情吧。"
    me "……对象，是谁？"
    window hide
    show cg school_building_night at center with Dissolve(1.0)
    window show
    saburo "……。"
    play music "good_scene.ogg"
    extend "\n……[player_name]，是你。"
    extend "\n我！喜，喜欢上你了！！！"
    extend "\n不知不觉，变得喜欢你到无法自拔！！"
    saburo "那个……不是朋友之间的感情，而是更加需要的，更加想珍惜的……。"
    extend "\n所，所以，想要好好，直面自己的感情\n趁现在，想要告诉你……！！"
    saburo "啊，那，那个！并，并不是希望得到你的答复！！"
    extend "\n我只是单纯想要吐露出来而已！"
    extend "\n应该说，[player_surname]君你的话，我想应该会理解我的……\n不，就算我这样的家伙说出口，也只会让你觉得恶心吧……。"
    window hide
    show cg school_building1_night with Dissolve(1.0)
    window show
    me "……谢谢你，三朗。"
    extend "\n你能这样对我说，我很开心哦。"
    saburo "呜，嗯……。"
    "三朗的脸，涌现了在火焰的映衬下也相当醒目的红潮。"
    me "……三朗，来我这边一点。"
    saburo "诶。"
    extend "\n这，这么羞耻……。"
    me "那，我去你那边。"
    window hide
    show cg c74 1 with FadeWhite(0.8)
    window show
    "说着，我靠近三朗，就这样抱住了他。"
    saburo "什！！"
    extend "\n等……[player_surname]！！！"
    extend "\n在这种地方做这种事……！"
    me "没关系的。"
    extend "\n最后的最后，让我这样一会儿。"
    extend "\n这样，就会很舒服很幸福。"
    show cg campfire with Dissolve(1.0)
    saburo "很舒服，很幸福……。"
    extend "\n那，那个，[player_surname]。"
    extend "\n想变得更幸福吗……？"
    me "嗯？嗯……来吧。"
    saburo "那么……能请你闭上眼睛吗？"
    "我听话地闭上了眼睛。"
    window hide
    show cg c74 2 with Radial(0.8)
    window show
    "亲"
    me "三朗……。"
    show cg c74 3 with Dissolve(0.8)
    saburo "嘿嘿……我试试。"
    extend "\n没关系的吧？我也喜欢你。"
    extend "\n怎么样，幸福吗？"
    me "嗯……很幸福。"
    window hide
    show cg moon_night with FadeWhite(0.8)
    window show
    "……这样就听到了三朗诚实的心声，得到了最棒的幸福。"
    extend "\n御咲祭成功举办了，还和三朗一起看到了这焰火。"
    extend "\n愿望全都实现了。……"
    window hide
    show cg campfire_sparks with Dissolve(0.8)
    window show
    "在这片燃烧的红炎之中，我的意识逐渐淡去……。"
    extend "\n……梦已经结束了。"
    window hide
    hide bg with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    hide saburo with Dissolve(0.8)
    window show
    "…"
    "梦的记忆是模糊的。"
    extend "\n在醒过来的同时，也会忘记这场梦。"
    extend "\n只留下甜美的回忆，其他的一切都被带去忘却的彼方而消散。"
    stop music fadeout 4.0
    "好了……差不多该起来了。"
    window hide
    show saburo 30 at top with DefocusWhite(2.5)
    window show
    "三朗，我喜欢你。"
    window hide
    hide saburo with dissolve
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.6
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "哔哔哔哔哔哔哔哔"
    window hide
    show bg protagonist_room_morning at center with Radial(0.5)
    window show
    me "啊……已经早上了吗……？"
    extend "\n唔~我好像并没有睡多少啊……。"
    stop sound fadeout 0.5
    "我望向餐桌，上面放着一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……"
    extend "啊，对对对，昨天回来的时候拿到的。"
    extend "\n那些孩子们，真可爱啊……。"
    me "……好！那天我一定要去好好享受！"
    play sound "fx/cute2.ogg"
    extend "\n然后在脑海里尽情幻想！！"
    window hide
    hide bg with dissolve
    stop music fadeout 0.5
    window show
    "御咲祭当天ーーーーーー"
    window hide
    play music "school_festival.ogg"
    play sound "fx/crowd_noise.ogg"
    show bg school_building_full at center with Radial(1.0)
    pause 0.6
    show bg hallway with Dissolve(1.0)
    window show
    me "我想想……记得说是2年1班和2年2班的咖啡店。"
    extend "\n唔？"
    play sound "fx/sliding_door.ogg"
    show bg cafe with dissolve
    extend "是这个吗？"
    "正当我站在店门口犹豫不决的时候，"
    extend "\n戴水蓝色名牌的红领带男孩从店里走了出来。"
    window hide
    play sound "fx/running.ogg"
    show saburo 29i at top with dissolve
    window show
    saburo "欢迎光临ーー！"
    extend "\n这位客人，您是一个人来的吗？"
    show saburo 30i with dissolve
    extend "\n请在店里慢慢逛吧！"
    window hide
    hide bg with Radial(1.0)
    hide saburo with Radial(1.0)
    pause 0.6
    show bg game_center2 at center with Radial(0.7)
    pause 0.6
    show bg saburou_ed with Dissolve(0.8)
    pause 1.3
    stop music fadeout 1.5
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.8
    hide bg with dissolve
    return

label end_sakuya:
    show bg cafe at center with dissolve
    play music "sakuya_theme.ogg"
    show sakuya 18i at top with dissolve
    window show
    play sound "fx/dash.ogg"
    sakuya "喂，你们。别再用那恶心的手碰他。"
    me "作哉君！"
    customer3 "怎，怎么会这样！"
    show sakuya 13i with dissolve
    sakuya "啊？什么玩意啊。"
    extend "\n从刚才开始就一直散发着恶心的气氛。"
    extend "\n如果你再敢不正经的话。"
    show sakuya 3i with dissolve
    extend "\n你那丑陋的脸，会扭曲得更加难看的哦。"
    play sound "fx/boing.ogg"
    customer3 "抱歉抱歉捏。"
    extend "\n有，有点兴奋过头，所以有点不守规矩了捏。"
    play sound "fx/cute3.ogg"
    customer5 "对不起呀。"
    extend "\n这里还是绅士一点，姑且忍一忍，可远观不可亵玩焉。"
    play sound "fx/sparkle.ogg"
    customer4 "哎呀~……粗犷的男人好棒♪"
    window hide
    hide sakuya with dissolve
    window show
    "在作哉的帮助下，我得以从那种场合中逃了出来。"
    "没想到在这种时候还能被初中生搭救……。"
    extend "\n总感觉有点丢人啊……。"
    window hide
    show sakuya 10i at top with dissolve
    window show
    sakuya "喂，怎么了？"
    me "嗯，嗯嗯。得救了。"
    extend "\n谢谢你们！"
    show sakuya 25i with dissolve
    sakuya "我并不是想帮你哦。"
    extend "\n只是想让那些恶心的家伙们受到一句骂声的洗礼而已。"
    extend "\n啊~心情舒畅多了。\n麻烦的工作中的休息时间变得愉快起来了呢！"
    me "这，这样啊……。"
    show sakuya 15i with dissolve
    sakuya "比起这个……你今天，"
    extend "\n今天后夜祭有空吗？"
    me "诶？那个，没什么。"
    show sakuya 14i with dissolve
    sakuya "我就知道~你朋友很少嘛！"
    extend "\n那就陪我去后夜祭吧。"
    play sound "fx/cute.ogg"
    me "啊！！作，作哉君要和我两人单独参加后夜祭吗！？"
    show sakuya 29i with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sakuya "你，你个笨蛋！！！才不是啦！！！"
    extend "\n是小翼说无论如何都要和你待在一起……。"
    show sakuya 36i with dissolve
    play sound "fx/dash.ogg"
    extend "\n话说回来，你没有拒绝的权利！\n所以一定要来！"
    me "嗯，嗯，我一定会来的！\n我也想见小翼……。"
    extend "\n那就在鞋柜那碰头吧。"
    show sakuya 9i with dissolve
    sakuya "哼！"
    extend "\n那我就先回自己负责的地方去了。"
    extend "\n回头见！"
    window hide
    play sound "fx/running.ogg"
    hide sakuya with dissolve
    window show
    "虽然作哉是为了小翼才邀请我的，但他居然主动邀请了我……！"
    "……。"
    show cg purple at center with dissolve
    "我是因为很期待学园祭，才来到这梦中的世界。"
    extend "\n没想到后夜祭的时候，还能和他在一起。"
    "所以我想尽量陪在他身边……"
    extend "想帮助他。"
    hide cg with dissolve
    hide bg with dissolve
    stop music fadeout 2.0
    "……毕竟这个梦不知道会持续到什么时候……。"
    window hide
    play sound "fx/crowd_noise.ogg"
    show bg school_building_evening_full at center with Dissolve(1.0)
    pause 0.4
    show bg cafe_evening with Radial(1.0)
    window show
    "咖啡店的营业时间也差不多要结束了。"
    extend "\n接下来的活动，就是和作哉一起参加后夜祭！"
    extend "\n不能迟到，于是我赶紧收拾完东西，朝大门走去。"
    window hide
    hide bg with dissolve
    window show
    "…"
    window hide
    play music "fx/night_insects.ogg"
    show bg shoe_locker_night at center with Dissolve(0.8)
    window show
    "我走到鞋柜前，发现作哉已经在那儿等着了。"
    me "作哉君，久等了！"
    show sakuya 6i at top with dissolve
    sakuya "久等了！"
    show sakuya 25i with dissolve
    extend "\n……那，走吧。"
    window hide
    hide sakuya with dissolve
    show bg school_building_night with Dissolve(1.0)
    window show
    "我们来到外面，夕阳已经落山了。\n但余晖和摊位的灯光交相辉映，街上依然很热闹。"
    extend "\n在校园的正中央，大家为了御咲祭篝火晚会做准备，\n堆柴火的工作正在有序地进行。"
    "我们趁着人少的时候，叫上翼来到了教学楼后方。"
    window hide
    show bg school_backside_night with Dissolve(1.0)
    show tsubasa 1 at top with dissolve
    window show
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play music "fx/cute.ogg"
    tsubasa "汪汪！"
    hide tsubasa with dissolve
    show tsubasa 4 at topright
    show sakuya 23i at topleft with dissolve
    sakuya "小翼，今天可是学园祭。"
    extend "\n我就破例带你在校园里转转吧。"
    extend "\n可别胡闹，要安静哦。"
    show tsubasa 2 with dissolve
    tsubasa "汪！"
    window hide
    hide sakuya with dissolve
    hide tsubasa with dissolve
    show bg schoolyard_night with dissolve
    window show
    "我们一回到校园，就故意坐在了人少的\n运动场内侧的草坪上。"
    window hide
    window show
    sakuya "这里可以清楚地看到焰火，应该能好好放松一下了。"
    show tsubasa 3 at topright
    show sakuya 23i at topleft with dissolve
    sakuya "是啊。"
    show sakuya 24i with dissolve
    extend "\n真是太好了呢，小翼。"
    extend "\n从现在开始，你就可以看到巨大的焰火了哦~。"
    show tsubasa 5 with dissolve
    tsubasa "呜嗯？"
    "小翼似乎听不懂我们在说什么，歪着脑袋。"
    hide sakuya with dissolve
    hide tsubasa with dissolve
    "远远眺望着，热闹非凡的学园祭的光景。"
    extend "\n然后"
    window hide
    play sound "fx/fire.ogg"
    show bg campfire with Radial(0.5)
    window show
    "终于点燃了柴火堆。"
    "熊熊燃烧着的鲜红火焰。"
    extend "\n真的好美啊……。"
    sakuya "快看，小翼！"
    extend "\n好壮观的焰火啊~！！"
    tsubasa "汪汪！"
    me "啊哈哈。"
    extend "\n他好像在说『真漂亮！』"
    sakuya "是啊，一定就是这样。"
    stop sound fadeout 2.0
    window hide
    play music "good_atmosphere.ogg"
    show bg schoolyard_night with dissolve
    show sakuya 31i at top with dissolve
    window show
    sakuya "……我说啊，[player_surname]。"
    extend "\n我要把所有事情都告诉你。"
    me "诶，什么事？"
    show sakuya 32i with dissolve
    sakuya "就是……关于之前岔开话题的一之濑的事…。"
    me "啊，是这件事啊！"
    extend "\n嗯，我想听。"
    extend "\n我想多了解你一些，然后助你一臂之力。"
    show sakuya 2i with dissolve
    play sound "fx/boing.ogg"
    sakuya "白，白痴！！\n别说这种丢人的话啊！"
    extend "\n这样会很难开口的。"
    me "啊哈哈，抱歉抱歉。"
    window hide
    show cg school_building_night at center with Dissolve(0.8)
    window show
    sakuya "……是我以前养过的狗，明明是条狗，却很胆小，\n外出的时候总是怯生生，一直提心吊胆的。"
    extend "\n所以，之前也说过了，我觉得让它待在家里比较好，\n除了散步以外都把它关在室内。"
    sakuya "不知道为什么……这一点和一之濑重叠了。"
    extend "\n每次看到一之濑，我就会想起它，然后回忆起它的死亡，\n很难受，很讨厌……所以我尽可能地冷淡对待一之濑。"
    extend "\n我觉得这样很对不起一之濑，他没有任何错……。"
    "确实，会变成这样吧……。"
    sakuya "之前还能正常地对待他。"
    extend "\n甚至到了想见他，并且喜欢他的程度。"
    extend "\n所以，对一之濑来说，我应该是突然变了一个人吧。"
    extend "\n但是，我已经被束缚住了，完全无法坦率地行动。"
    me "这种伤，只能等待时间来治愈了吧。"
    sakuya "是啊。"
    extend "\n我真是够弱小的。"
    extend "\n也许比起他，比起一之濑，我才是真正的弱小……。"
    window hide
    show cg school_building1_night with Dissolve(1.0)
    window show
    me "没有这回事。"
    extend "这种创伤无论对谁而言，都是强大的敌人。"
    extend "\n作哉不是软弱，而是温柔。"
    extend "\n虽然因为温柔而变得冷淡有点奇怪，\n但反过来讲，作哉应该可以依靠翼的力量吧？"
    sakuya "他的力量……？"
    me "嗯。"
    extend "\n翼知道作哉的本质是温柔的，\n所以他说了就算作哉冷淡对待自己也没关系。"
    extend "\n只不过他担心自己是不是做了什么错事。"
    sakuya "是吗……这样啊。"
    extend "\n他看起来弱不禁风，其实意外地强呢。"
    extend "\n这方面或许和你很像……。"
    me "等你不再因此难过了，能坦率一点的话，\n我认为你向他说明清楚比较好。"
    extend "\n还要跟他说『对不起』哦。"
    show bg schoolyard1_night
    sakuya "是啊……。"
    window hide
    hide cg with Dissolve(0.7)
    hide sakuya with Dissolve(0.7)
    show tsubasa 1 at top with dissolve
    window show
    tsubasa "汪汪！"
    me "瞧，小翼又在鼓励你了。"
    extend "\n最近作哉哥哥经常变得很消沉，\n小翼也很困扰呢~。"
    show tsubasa 6 with dissolve
    tsubasa "呜~。"
    hide tsubasa with dissolve
    show tsubasa 5 at topright
    show sakuya 22i at topleft with dissolve
    sakuya "啊哈哈，抱歉抱歉。\n没问题的，小翼。"
    extend "\n我有小翼……"
    show sakuya 33i with dissolve
    extend "而且[player_surname]君也在旁边陪伴我。"
    show sakuya 35i with dissolve
    extend "\n啊~下次说不定还会向你介绍名叫一之濑的哥哥呢~。"
    me "感觉就像母子一样呢。"
    extend "\n作哉是妈妈，而小翼是孩子。"
    extend "\n我应该可以当爸爸吧。"
    extend "\n真好呢~真想和你们住在一起。"
    show sakuya 26i with dissolve
    sakuya "哈，哈！？\n又说这种无聊的话……！"
    extend "\n妄想也该有点分寸……"
    show tsubasa 4 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tsubasa "汪汪！"
    me "但是，小翼好像很同意哦。"
    show tsubasa 2 with dissolve
    tsubasa "汪！"
    show sakuya 29i with dissolve
    sakuya "呜……那，那怎么可能！！"
    extend "\n为什么我要和你……。"
    extend "\n而且，我可是男的！！！\n我当妈妈太奇怪了吧！"
    me "那我当妈妈好了。"
    extend "\n哎呀，亲爱的……领带歪了哦。"
    show sakuya 8i with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sakuya "哇，哇啊啊啊啊……不要这样太恶心了！！"
    me "小翼，最近作哉很冷淡呢……"
    extend "\n难道他出轨了吗……？"
    hide tsubasa with dissolve
    hide sakuya with dissolve
    show tsubasa 5 at top with dissolve
    tubasa "呜~……。"
    me "支持我的人只有小翼呢。"
    extend "\n呜呜……。"
    show tsubasa 6 with dissolve
    tubasa "呜……"
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    show tsubasa 1 with dissolve
    extend "\n汪汪！"
    hide tsubasa with dissolve
    show tsubasa 5 at topright
    show sakuya 12i at topleft with dissolve
    sakuya "呜……抱歉。"
    extend "\n我不会出轨的，所以请原谅我吧。"
    show sakuya 36i with dissolve
    extend "\n我怎么可能在有小翼的情况下出轨呢。"
    show tsubasa 2 with dissolve
    tsubasa "汪！"
    window hide
    show cg school_building1_night at center with dissolve
    window show
    me "噗……"
    extend "啊哈哈！"
    sakuya "啊哈哈哈。"
    "我们被这闹剧逗得忍不住笑了出来。"
    window hide
    hide sakuya with dissolve
    hide tsubasa with dissolve
    hide cg with dissolve
    show sakuya 35i at topleft with dissolve
    window show
    sakuya "哈哈太无聊了吧。"
    extend "\n对吧，翼？"
    show tsubasa 5 at topright with dissolve
    tubasa "汪？"
    show sakuya 33i with dissolve
    sakuya "翼♪"
    show tsubasa 1 with dissolve
    tubasa "汪汪♪"
    show sakuya 28i with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sakuya "诶嘿嘿。"
    extend "\n翼~♪"
    show tsubasa 2 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tubasa "汪汪汪♪"
    play sound "fx/sparkle.ogg"
    show cg adult at center with FadeWhite(0.5)
    "你，你们怎么回事啊……也太可爱了吧……！！"
    extend "\n但是，这真的要人命啊……。"
    window hide
    hide cg with dissolve
    hide tsubasa with dissolve
    hide sakuya with dissolve
    show sakuya 33i at top with dissolve
    window show
    sakuya "……的确，养小翼需要钱啊~。"
    extend "\n组成一家人什么的，如果是为了可爱的小翼，倒也不错。"
    extend "\n这样的话，我来当妈妈好了。"
    me "诶？是，是吗？"
    show sakuya 14i with dissolve
    sakuya "嗯。"
    extend "\n我会尽力照顾好小翼。\n你就好好挣钱，让我们过上好日子。"
    extend "\n这可是重要的资金来源，拜托你了。"
    me "怎么，怎么，感觉是妻管严的典范嘛~。"
    extend "\n根本就是个骑在丈夫头上的妻子吗。"
    extend "\n可怜的老公连藏点私房钱都不得安生吧…。"
    show sakuya 24i with dissolve
    sakuya "那些都是小翼的抚养费！！"
    me "喂喂，我可不是ATM啊~。"
    show sakuya 23i with dissolve
    play sound "fx/boing.ogg"
    sakuya "诶，是吗？"
    me "啊哈哈。\n真是个对丈夫严厉，对孩子却温柔的贤母啊。"
    hide sakuya with dissolve
    show tsubasa 3 at topright with dissolve
    tubasa "汪！汪！"
    stop music fadeout 2.0
    show sakuya 31i at topleft with dissolve
    sakuya "嗯？"
    show sakuya 7i with dissolve
    extend "\n诶…。"
    me "怎么了？"
    sakuya "……。"
    window hide
    play music "reminiscence.ogg"
    show cg c83 1 at center with FadeWhite(0.8)
    window show
    sakuya "喂，你，给我把眼睛闭上！"
    me "诶……为什么？"
    sakuya "没，没事！快点闭上！"
    extend "\n你要是敢睁开眼睛我可不饶你！！"
    "怎么回事啊……。"
    extend "\n我听话地闭上了眼睛。"
    hide cg with dissolve
    hide bg with dissolve
    hide sakuya with dissolve
    hide tsubasa with dissolve
    sakuya "……嘴巴给我闭上！！"
    play sound "fx/boing.ogg"
    "诶诶诶！！？"
    extend "这这这这是怎么回事！？！？！"
    window hide
    show cg c83 2 at center with Radial(0.7)
    window show
    "亲"
    "……诶？"
    me "作，作哉……？"
    show cg purple with FadeWhite(0.5)
    sakuya "那，那个……小翼他……"
    show bg schoolyard1_night at center
    show tsubasa 5 at topright
    show sakuya 10i at topleft
    extend "小翼说他无论如何都想和[player_surname]君接吻！"
    extend "\n所以……刚才那个吻，不是我，而是小翼哦！"
    extend "\n不要误会了，笨蛋！！！"
    hide cg with dissolve
    me "哼~。"
    extend "\n小翼，你真的这么想？"
    tsubasa "呜~。"
    me "我就知道~不可能嘛~。"
    extend "\n这么说起来，刚才我听了那个故事之后突然想到，\n小翼这个名字，是作哉你取的吧。"
    show sakuya 17i with dissolve
    sakuya "诶……是的，我早说过，这是他原本的名字…。"
    me "骗人~！"
    extend "\n居然骗自己的丈夫，你这个坏女人~！！"
    extend "\n看我这样惩罚你！"
    window hide
    show cg c83 3 at center with Radial(0.7)
    window show
    "我这样说着，一把抱住了作哉。"
    sakuya "什……！！"
    extend "\n这，这个……有点……不，不行的……！！！"
    me "拜托了。"
    extend "\n再让我抱一会……。"
    sakuya "……。"
    tsubasa "汪！"
    sakuya "！"
    extend "\n……。"
    window hide
    show cg moon_night with FadeWhite(0.8)
    window show
    "能感觉到，作哉的手臂环抱着我的背。"
    "……能感受到作哉变得诚实，这真是太好了。"
    extend "\n御咲祭也顺利成功了，我见证了作哉和小翼一起欣赏的火焰。"
    extend "\n愿望全都实现了。……"
    window hide
    show cg campfire_sparks with Dissolve(0.8)
    window show
    "在这片燃烧的红炎之中，我的意识逐渐淡去……。"
    extend "\n……梦已经结束了。"
    window hide
    hide bg with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    hide tsubasa with Dissolve(0.8)
    hide sakuya with Dissolve(0.8)
    window show
    "…"
    "梦的记忆是模糊的。"
    extend "\n在醒过来的同时，也会忘记这场梦。"
    extend "\n只留下甜美的回忆，其他的一切都被带去忘却的彼方而消散。"
    stop music fadeout 4.0
    "好了……差不多该起来了。"
    window hide
    show sakuya 35 at top with DefocusWhite(2.5)
    window show
    "作哉，我喜欢你。"
    window hide
    hide sakuya with dissolve
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.6
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "哔哔哔哔哔哔哔哔"
    window hide
    show bg protagonist_room_morning at center with Radial(0.5)
    window show
    me "啊……已经早上了吗……？"
    extend "\n唔~我好像并没有睡多少啊……。"
    stop sound fadeout 0.5
    "我望向餐桌，上面放着一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……"
    extend "啊，对对对，昨天回来的时候拿到的。"
    extend "\n那些孩子们，真可爱啊……。"
    me "……好！那天我一定要去好好享受！"
    play sound "fx/cute2.ogg"
    extend "\n然后在脑海里尽情幻想！！"
    window hide
    hide bg with dissolve
    stop music fadeout 0.5
    window show
    "御咲祭当天ーーーーーー"
    window hide
    play music "school_festival.ogg"
    play sound "fx/crowd_noise.ogg"
    show bg school_building_full at center with Radial(1.0)
    pause 0.6
    show bg hallway with Dissolve(1.0)
    window show
    me "我想想……记得说是2年1班和2年2班的咖啡店。"
    extend "\n唔？"
    play sound "fx/sliding_door.ogg"
    show bg cafe with dissolve
    extend "是这个吗？"
    "正当我站在店门口犹豫不决的时候，"
    extend "\n一位戴着紫色名牌，系着红色领带的男生从店里走了出来。"
    window hide
    play sound "fx/running.ogg"
    show sakuya 23i at top with dissolve
    window show
    sakuya "欢迎。"
    show sakuya 15i with dissolve
    extend "\n客人，你是一个人逛学园祭的吗？"
    show sakuya 35i with dissolve
    extend "\n……嘛，我们会好好招待你的，你就放轻松吧！"
    window hide
    hide bg with FadeWhite(1.0)
    hide sakuya with FadeWhite(1.0)
    pause 0.6
    show bg school_backside at center with Radial(0.7)
    pause 0.6
    show bg sakuya_ed with Dissolve(0.8)
    pause 1.3
    stop music fadeout 1.5
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.8
    hide bg with dissolve
    return

label end_sirou:
    play sound "fx/crowd_noise.ogg"
    show bg cafe at center with dissolve
    show sirou 2 at top with dissolve
    window show
    sirou "……[player_name]桑？"
    "我朝旁边一看，居然看到了四朗。"
    extend "\n他来我们咖啡厅了吗……！！"
    window hide
    hide sirou with dissolve
    window show
    play sound "fx/cute2.ogg"
    customer3 "哎呀，除了店员之外，还发现了可爱的正太！"
    extend "\n我，我也要来点一杯茶在那边坐下来！"
    "那个男人这么说着，松开了我的手，朝四朗伸出了手。"
    window hide
    play sound "fx/explosion3.ogg"
    show cg remarkable at center with FadeWhite(0.5)
    play music "hurry_up.ogg"
    window show
    me "等一下！！"
    "我挺身护住了四朗。"
    play sound "fx/dash.ogg"
    customer3 "怎，怎么了！"
    extend "\n客人您是点茶喝吗！？"
    play sound "fx/eureka.ogg"
    me "啊啊……？客人……请不要得寸进尺哦。"
    extend "\n听说最近的年轻人，发起火来可是很恐怖的哦~。"
    extend "\n你听说过『暴躁的青少年』这个词吗？"
    extend "\n你还是适可而止比较好吧？"
    window hide
    hide cg with dissolve
    window show
    play sound "fx/boing.ogg"
    customer3 "呜……抱，抱歉了捏。"
    extend "\n有，有点兴奋过头，所以有点不守规矩了捏。"
    play sound "fx/cute3.ogg"
    customer5 "对不起呀。"
    extend "\n这里还是绅士一点，姑且忍一忍，可远观不可亵玩焉。"
    play sound "fx/cute.ogg"
    customer4 "对不起…。"
    me "明白的话就赶紧走吧！"
    extend "\n那么，请点单吧！"
    window hide
    play sound "fx/sparkle.ogg"
    show sirou 10 at top with dissolve
    window show
    sirou "[player_name]桑，好帅……！！"
    play sound "fx/impact_japanese.ogg"
    "呼……成功了！！"
    extend "\n我不能在四朗面前出丑！"
    stop music fadeout 2.0
    play sound "fx/running.ogg"
    hide sirou with dissolve
    hide bg with dissolve
    "我成功地逃脱了那个男人，走向了四朗。"
    window hide
    show bg cafe at center with dissolve
    play music "siro_theme.ogg"
    window show
    me "呀，好久不见。"
    show sirou 4 at top with dissolve
    sirou "好久不见，[player_name]桑！"
    extend "\n刚才的那个，帅呆了哦！！"
    show sirou 15 with dissolve
    extend "\n再次救了我，谢谢你！"
    me "不不不……我只是做了应该做的。"
    extend "\n但是，你这么说，我很开心。"
    show sirou 11 with dissolve
    play sound "fx/sparkle.ogg"
    sirou "真好啊……我如果升到初中的话，就会增加体力变强，\n就算被坏家伙抓住了，也能像你那样制裁他们！"
    me "啊哈哈，没问题。\n在四朗君被抓之前，我会去干掉那些家伙的！"
    show sirou 12 with dissolve
    sirou "诶~！！\n那么，总觉得好像只有我在出糗的样子。"
    show sirou 13 with dissolve
    extend "\n……啊，对了！"
    extend "\n[player_name]桑，你之后有事吗？"
    me "那个……没有，再过10分钟就休息了。"
    extend "\n怎么了？"
    show sirou 4 with dissolve
    sirou "可以的话，和我一起逛学园祭吧！"
    show sirou 14 with dissolve
    extend "\n虽然我本来是想带朋友来的，\n但是，那孩子因为感冒，没办法来了……。"
    extend "\n我，现在孤身一人。"
    play sound "fx/explosion2.ogg"
    "呜噢噢噢噢噢噢！！正太向我发出邀请了啊啊啊啊啊！！！"
    me "这，这样啊。"
    extend "\nOK！如果我没事的话，就一起去吧。"
    show sirou 15 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sirou "太好啦！！"
    extend "\n那我先去教室等你啦！"
    play sound "fx/running.ogg"
    hide sirou with dissolve
    show cg remarkable at center with Dissolve(0.2)
    play sound "fx/tadaa.ogg"
    "太好啦！！"
    extend "\n没想到居然能和四朗一起逛学园祭！！！"
    hide sirou with dissolve
    hide cg with dissolve
    hide bg with dissolve
    stop music fadeout 2.0
    "我兴奋得之后完全没法工作。"
    window hide
    play sound "fx/crowd_noise.ogg"
    show bg school_building_evening_full at center with Dissolve(1.0)
    pause 0.4
    show bg hallway_evening with Dissolve(0.8)
    window show
    me "让你久等了，四郎君。"
    show sirou 3 at top with dissolve
    sirou "啊，[player_name]桑！工作辛苦了！！"
    extend "\n那赶紧走吧～！"
    play sound "fx/running.ogg"
    hide sirou with dissolve
    "四朗拉着我的手，开心地走了起来。"
    play sound "fx/sparkle.ogg"
    show cg adult at center with FadeWhite(0.5)
    extend "\n这幅景象，简直就像我梦中见到的弟弟一样。"
    window hide
    hide cg with dissolve
    window show
    me "四郎，不用那么急匆匆的，店不会跑掉的。"
    play music "siro_theme.ogg"
    show sirou 9 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sirou "因为~我想逛遍所有店铺呀~！"
    extend "\n不赶紧点，一下就结束啦！"
    "哈哈，小孩子真是活力满满啊！"
    extend "\n已经完全变成了哥哥的我，兴冲冲地指向了店铺。"
    window hide
    hide sirou with dissolve
    window show
    me "啊！喂，四郎。"
    extend "\n那个鬼屋怎么样？"
    show sirou 14 at top with dissolve
    $ renpy.transition(Quake(30, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    sirou "诶……鬼，鬼屋吗……？"
    extend "\n这，这有点……。"
    "哦？难道说，这家伙是那种害怕恐怖的东西吗？"
    play sound "fx/eureka.ogg"
    "……我咧嘴一笑"
    me "咦？刚才，不是说要征服所有的店铺的吗！"
    extend "\n那就要好好地参观一下鬼屋了呢。"
    extend "\n男子汉大丈夫可不能反悔哦？"
    show sirou 1 with dissolve
    sirou "呜呜呜呜……"
    show sirou 17 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    extend "我，我知道了！我们走吧！！"
    extend "\n我可不怕鬼怪什么的！！"
    stop music fadeout 2.0
    play sound "fx/sliding_door.ogg"
    hide bg with dissolve
    hide sirou with dissolve
    "听到我这么一说，四朗就逞强似地进入了鬼屋。"
    window hide
    pause 0.4
    play music "haunted_music_room.ogg"
    show bg dark at center with dissolve
    window show
    play sound "fx/boing.ogg"
    sirou "咿呀啊啊啊啊啊啊啊啊！！！\n这，这是人头啊啊啊啊！！！！"
    play sound "fx/cute3.ogg"
    sirou "呜哇啊啊啊啊！！！！"
    extend "\n为什么这是只毛茸茸的手啊啊啊啊啊！！！？"
    play sound "fx/shock.ogg"
    sirou "不要啊啊啊啊啊！！\n我想回家啊啊啊啊啊啊！！！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    pause 0.4
    play music "siro_theme.ogg"
    show bg school_building_evening at center with Radial(0.7)
    pause 0.4
    show bg hallway_evening with Dissolve(0.7)
    show sirou 16 at top with dissolve
    window show
    sirou "嗝……嗝……。"
    show sirou 1 with dissolve
    extend "\n呜呜呜呜……好害怕啊啊啊……。"
    window hide
    hide sirou with dissolve
    window show
    "在鬼屋的出口处，四朗哭了出来。"
    "那么一眼假的鬼居然能把他吓成这样，\n这家伙真是相当的胆小啊……。"
    extend "\n看到他这样的反应，运营人员应该会相当满足吧。"
    me "好了好了。"
    extend "\n四朗，已经没事了，放心吧。"
    show sirou 16 at top with dissolve
    sirou "呜呜……嗝……。"
    show sirou 17 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    extend "\n真是的[player_name]桑你欺负人！"
    extend "\n为什么把我一个人丢在后面，自己先走啊！！"
    "我虽然表面上是等走得慢的四朗，但其实是在观察他害怕的样子。"
    extend "\n这种事情我绝对不可能说出来。"
    me "那么……毕，毕竟！\n刚才四朗不是说想要变得更强吗。"
    extend "\n所以，才给予了你考验……。"
    show sirou 1 with dissolve
    sirou "呜呜……是这样啊……。\n那就好……。"
    show sirou 6 with dissolve
    play sound "fx/sparkle.ogg"
    extend "\n居然能为我着想到这个地步，果然很温柔啊。"
    extend "\n但是，想变强什么的，等我成为中学生之后再说吧……。"
    "虽然对把我的谎言当真的四朗君多少有点罪恶感，\n但总之能处理好这个场面真是太好了。"
    show sirou 9 with dissolve
    sirou "嗯……！"
    extend "\n占用你的时间真是对不起！已经不要紧了！！"
    show sirou 15 with dissolve
    extend "\n那么，重新振作，去逛其他地方吧！"
    "四朗擦干眼泪，气势十足地站了起来。"
    window hide
    show cg school_building_evening at center with Dissolve(0.7)
    window show
    "之后，我们按照之前的宣言，逛遍了所有的学校内的摊位。"
    extend "\n到了最后关头，我实在是不行了，两膝都在颤抖，但是\n相对的，四朗还是一副精神满满的样子。"
    "不愧是小学生……"
    play sound "fx/impact.ogg"
    stop music fadeout 2.5
    extend "深不见底的体力，真是可怕啊……。"
    window hide
    hide bg with dissolve
    hide sirou with dissolve
    hide cg with dissolve
    play music "fx/night_insects.ogg"
    show bg school_building_night at center with Dissolve(1.0)
    pause 0.5
    show bg shoe_locker_night with dissolve
    show sirou 15 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    window show
    sirou "[player_name]桑，今天真的非常开心呢~！"
    extend "\n真的非常感谢你能陪我玩到这么晚！！"
    me "没，没事……四朗能开心就好。"
    show sirou 13 with dissolve
    sirou "在逛学园祭的时候，太阳就基本落山了呢。"
    extend "\n接下来终于要举办后夜祭了吧。"
    me "后夜祭……"
    extend "\n对了，四朗！\n如果不介意的话，后夜祭也一起来吧"
    window hide
    hide sirou with dissolve
    stop music fadeout 0.5
    show sirou 10 at top with dissolve
    play sound "fx/eureka.ogg"
    window show
    sirou "嗯！？"
    extend "\n那边站着的……"
    play music "lively_boys.ogg"
    show sirou 18 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    sirou "穗海学长！！！"
    play sound "fx/running.ogg"
    hide sirou with dissolve
    "四朗无视了我所说的，直接跑了过去。"
    extend "\n我顺着他的视线一看，发现作哉和三朗站在那里。"
    window hide
    show sakuya 15i at topleft with dissolve
    window show
    sakuya "哦！这不是四朗嘛。"
    extend "\n怎么，你来了啊。"
    show sirou 15 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sirou "那是当然的！"
    extend "\n我当然也去学长工作的咖啡店看了看。"
    show sirou 14 with dissolve
    extend "\n但是没能找到学长，真是可惜……。"
    show saburo 33i at topright with dissolve
    play sound "fx/boing.ogg"
    saburo "喂喂。"
    extend "\n是无视了哥哥的存在吗？"
    show sirou 8 with dissolve
    sirou "直到刚才，[player_name]桑在和我一起逛学园祭。"
    extend "\n本来是想去和穗海学长一起逛的，\n但我想你肯定有工作在身，所以就没有找你！"
    show sirou 6 with dissolve
    extend "诶嘿嘿。"
    show sakuya 23i with dissolve
    sakuya "诶~是这样啊。谢谢你这么为我着想。"
    show sakuya 11i with dissolve
    play sound "fx/triangle.ogg"
    extend "\n话说，那边那个看着被击溃的人就是『[player_name]桑吗？"
    show saburo 18i with dissolve
    saburo "你……是有多折腾我们啊。"
    show sirou 9 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sirou "我才没有折腾呢~！"
    extend "\n我们只是愉快地逛学园祭而已！！"
    hide sirou with dissolve
    hide sakuya with dissolve
    hide saburo with dissolve
    "说完，四朗走到了我的面前。"
    window hide
    play sound "fx/sparkle.ogg"
    show cg c87 at center with FadeWhite(0.8)
    window show
    sirou "[player_name]桑！"
    extend "\n后面我要和穗海学长一起去参加后夜祭，所以先告辞了！！"
    extend "\n谢谢你陪我逛那么久！\n那下次见！"
    window hide
    play sound "fx/running.ogg"
    hide cg with Dissolve(0.7)
    window show
    "四朗说完后，再次抛下我，渐行渐远。"
    extend "\n然后，三个人就这样一同离开了校园。"
    window hide
    show cg school_building_night at center with dissolve
    play sound "fx/ding.ogg"
    window show
    "……。"
    me "诚实的孩子……从某种意义上来说，真是残酷啊……。"
    extend "\n啊哈哈。"
    "果然，我适合远远地眺望少年呢。"
    extend "\n好了，老老实实地回到原来的世界吧。"
    stop music fadeout 3.0
    stop sound fadeout 0.5
    hide bg with dissolve
    hide cg with dissolve
    "喂，快醒醒啊。\n到早上了啊。"
    window hide
    window show
    "…。"
    window hide
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.6
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "哔哔哔哔哔哔哔哔"
    window hide
    show bg protagonist_room_morning at center with Radial(0.5)
    window show
    me "啊……已经早上了吗……？"
    extend "\n唔~我好像并没有睡多少啊……。"
    stop sound fadeout 0.5
    "我望向餐桌，上面放着一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……"
    extend "啊，对对对，昨天回来的时候拿到的。"
    extend "\n那些孩子们，真可爱啊……。"
    play sound "fx/triangle.ogg"
    me "……不过仔细想想，下周还要出差。"
    extend "\n这次实在没办法推掉了……哎……。"
    me "还是老老实实地，面对现实吧。"
    extend "\n呜……腿怎么这么酸痛。"
    extend "\n昨天有走那么远吗？"
    "我稍微做了下伸展，然后做好了上班的准备，和往常一样出门了。"
    window hide
    hide bg with dissolve
    play sound "fx/door_open.ogg"
    show bg sky at center with Radial(0.7)
    window show
    me "好嘞！ 今天也加油干一天！！！"
    window hide
    stop music fadeout 1.0
    hide bg with FadeWhite(1.0)
    pause 0.6
    show bg intersection at center with Radial(0.7)
    pause 0.6
    show bg sirou_ed with Dissolve(0.8)
    pause 1.3
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.5
    hide bg with dissolve
    return

label end_all:
    show bg cafe at center with dissolve
    window show
    "可恶……太得意忘形了啊……！！"
    extend "\n我猛地挣脱对方的手，开始反击。"
    window hide
    play sound "fx/explosion3.ogg"
    show cg remarkable at center with FadeWhite(0.5)
    play music "hurry_up.ogg"
    window show
    play sound "fx/dash.ogg"
    customer3 "怎，怎么会这样！"
    me "客人……不要太得意忘形了。"
    extend "\n听说最近的年轻人，发起火来可是很恐怖的哦~。"
    extend "\n你听说过『暴躁的青少年』这个词吗？"
    extend "\n你还是适可而止比较好吧？"
    window hide
    hide cg with dissolve
    window show
    play sound "fx/boing.ogg"
    customer3 "呜……抱，抱歉了捏。"
    extend "\n有，有点兴奋过头，所以有点不守规矩了捏。"
    play sound "fx/cute3.ogg"
    customer5 "对不起呀。"
    extend "\n这里还是绅士一点，姑且忍一忍，可远观不可亵玩焉。"
    play sound "fx/sparkle.ogg"
    customer4 "好帅啊♪"
    window hide
    window show
    me "……那么，请点菜！"
    "真是的，这么没礼貌的家伙竟然是我的同类……"
    play sound "fx/eureka.ogg"
    extend "\n同为正太控的我好羞耻啊！！"
    stop music fadeout 2.0
    play sound "fx/running.ogg"
    hide bg with dissolve
    "点完菜后，我回到厨房，等待其他工作人员点单。"
    window hide
    play sound "fx/crowd_noise.ogg"
    show bg cafe at center with dissolve
    play music "afternoon_class.ogg"
    show sintarou 29i at top with dissolve
    window show
    sintarou "哎呀~不好意思啊，[player_name]亲。"
    extend "\n待会我也会好好警告他们的。"
    me "嗯……那就拜托了。"
    extend "\n我也已经警告他们了，应该没问题吧……。"
    hide sintarou with dissolve
    show saburo 2i at top with dissolve
    saburo "真是胆大包天啊！"
    extend "\n哎呀~ 说得好！！"
    show saburo 7i with dissolve
    extend "\n这样一来，我也可以安心工作啦~。"
    me "嗯？ 话说回来，三朗和他们是什么关系？"
    show saburo 33i with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    saburo "怎，怎么可能有什么关系啊！！"
    extend "\n我才不认识那种恶心的团伙呢！"
    hide saburo with dissolve
    show saburo 26i at topright
    show sintarou 29i at topleft with dissolve
    sintarou "算啦算啦[player_name]亲。"
    extend "\n还是请你别去问他了，就随他去吧。"
    me "和慎太郎君都认识的熟人……？"
    extend "\n你不说我还真挺在意的…。"
    hide sintarou with dissolve
    hide saburo with dissolve
    show sora 26i at top with dissolve
    sora "不过，没想到竟然会有这么多的客人来，\n真是出乎我的意料啊~！"
    show sora 11i with dissolve
    extend "我好开心~！！"
    me "这也是多亏了大家的齐心协力才有了今天的成果。"
    show sora 10i with dissolve
    sora "是啊！我们的努力都是有价值的。"
    hide sora with dissolve
    show tubasa 4i at topright with dissolve
    tubasa "我也渐渐地习惯做招待客人的工作了呢…。"
    show sinobu 26i at topleft with dissolve
    sinobu "好像是呢。"
    show sinobu 24i with dissolve
    extend "\n而且好像也不会弄错一千元和一万元的钞票了。"
    show tuki 18i at top with dissolve
    tuki "我也终于能做好甜点的盛盘了哦。"
    show tuki 15i with dissolve
    extend "\n像这样去体验新事物果然还是很重要呢。"
    extend "\n这样才能发现新事物，独立思考，学习到新的东西。"
    me "不愧是你！！"
    extend "\n年轻的时候学习能力就是强啊~！"
    window hide
    hide tubasa with dissolve
    hide sinobu with dissolve
    hide tuki with dissolve
    window show
    "…"
    window hide
    show tomo 28i at topright with dissolve
    window show
    tomo "咦？！不会吧！"
    extend "\n我好像又点错单了……？"
    show tomo 24i with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    extend "\n对，对不起！！\n我马上就去换！！"
    play sound "fx/running.ogg"
    hide tomo with dissolve
    show sakuya 15i at topleft with dissolve
    play sound "fx/boing.ogg"
    sakuya "这个不是法式咖啡，而是拿铁咖啡吗……？"
    show sakuya 27i with dissolve
    play sound "fx/dash.ogg"
    extend "\n这些东西都是一样的吧，反正都是咖啡！！"
    window hide
    hide sakuya with dissolve
    window show
    "…"
    show tubasa 19i at topleft
    show sinobu 16i at topright with dissolve
    play sound "fx/triangle.ogg"
    sinobu "有的人好像完全没进步呢。"
    tubasa "啊哈哈…。"
    me "……学习能力因人而异。"
    extend "\n让我们用长远的目光，温柔地守护他们的成长吧…。"
    stop music fadeout 1.0
    window hide
    hide tubasa with dissolve
    hide sinobu with dissolve
    hide bg with dissolve
    play sound "fx/crowd_noise.ogg"
    show bg school_building_evening_full at center with Dissolve(1.0)
    pause 0.4
    show bg cafe_evening with Radial(1.0)
    window show
    "咖啡店的营业时间也差不多要结束了。"
    extend "\n剩下的活动只有后夜祭了。"
    show tomo 13i at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    tomo "御咲祭执行委员，集合啦~！"
    hide tomo with dissolve
    "嗯？什么？"
    window hide
    play music "going_home.ogg"
    show tomo 12i at top with dissolve
    window show
    tomo "真的辛苦大家了！"
    show tomo 4i with dissolve
    extend "\n当然，虽然也多亏了班上同学们的帮忙，\n但是咱们执行委员作为核心，才让御咲祭得以顺利举办！！"
    show tomo 17i with dissolve
    extend "\n老师给我们每人奖励了一瓶果汁，现在来发吧~！"
    hide tomo with dissolve
    show saburo 9i at topleft with dissolve
    saburo "什么~是橘子汁。"
    extend "\n不管怎样，不如大吃一顿烤肉吧~。"
    show sakuya 25i at topright with dissolve
    sakuya "对啊。待会我来跟老师求求看吧。"
    show sintarou 13i at top with dissolve
    sintarou "那么，要在这里干杯庆祝一下吗？"
    hide sintarou with dissolve
    hide saburo with dissolve
    hide sakuya with dissolve
    me "稍等一下。"
    extend "\n虽然在这里庆祝也行，但既然要庆祝，\n不如大家一起看御咲祭篝火晚会，庆祝一番吧。"
    show sintarou 8i at top with dissolve
    sintarou "御咲祭篝火晚会吗……"
    extend "好主意！"
    show sora 3i at topright with dissolve
    sora "赞成~！那样更有庆祝的感觉。"
    show tuki 15i at topleft with dissolve
    tuki "那我也赞成。"
    hide sintarou with dissolve
    hide sora with dissolve
    hide tuki with dissolve
    show tubasa 31i at topright
    show sinobu 18i at topleft with dissolve
    tubasa "我也觉得，大家一起肯定更开心…。"
    sinobu "嗯，"
    extend "\n我也这么觉得。"
    show tomo 1i at top with dissolve
    tomo "……是啊！"
    "好不容易都这么努力了，就一直坚持到最后吧！"
    extend "\n那大家就一起去操场，Let's go！！"
    stop music fadeout 2.0
    window hide
    hide tomo with dissolve
    hide tubasa with dissolve
    hide sinobu with dissolve
    hide bg with Dissolve(1.0)
    play music "fx/night_insects.ogg"
    show bg school_building_night at center with Dissolve(1.0)
    window show
    "我们来到外面，夕阳已经落山了。\n但余晖和摊位的灯光交相辉映，街上依然很热闹。"
    "在校园的正中央，大家为了御咲祭篝火晚会做准备，\n堆柴火的工作正在有序地进行。"
    window hide
    show bg schoolyard_night with dissolve
    window show
    me "一直工作脚都酸了。"
    extend "\n找个地方歇会儿吧。"
    "这么说着，我们两人\n在远离操场的草坪上坐了下来。"
    window hide
    show tuki 9i at topleft
    show sora 2i at topright with dissolve
    window show
    sora "这里的话，御咲焰火应该也很好看吧。"
    tuki "是啊。"
    hide sora with dissolve
    hide tuki with dissolve
    "远远眺望着，热闹非凡的学园祭的光景。"
    extend "\n然后"
    stop music fadeout 0.5
    window hide
    play music "going_home.ogg"
    play sound "fx/fire.ogg"
    show cg campfire at center with Radial(0.5)
    window show
    "终于点燃了柴火堆。"
    "熊熊燃烧着的鲜红火焰。"
    extend "\n真的好美啊……。"
    window hide
    window show
    tubasa "……感觉好浪漫啊。"
    tomo "是啊~。"
    extend "\n要是拍电影的话，背景就是这焰火，然后就吻一下两下吧。"
    play sound "fx/cute2.ogg"
    tubasa "是，是这样吗！？"
    extend "\n友，友友……如果你觉得我可以的话……那个…。"
    play sound "fx/boing.ogg"
    extend "\n嗯……好，好痛好痛好痛！！"
    extend "\n忍，忍君，不要拉我脸蛋~……！"
    stop sound fadeout 1.0
    window hide
    hide cg with dissolve
    show tubasa 7i at topright
    show sinobu 6i at topleft with dissolve
    window show
    sinobu "这种事只有你们两人的时候再做。"
    show sintarou 12i at top with dissolve
    "慎太郎　我倒是无所谓啊，"
    show sintarou 13i with dissolve
    extend "\n不如说，你们这么做才更会让我们兴奋起来♪"
    hide sintarou with dissolve
    hide tubasa with dissolve
    hide sinobu with dissolve
    show tuki 9i at topleft
    show sora 4i at topright with dissolve
    tuki "空，你听见了没？"
    extend "\n向着焰火，然后一边转身一边接吻好像是固定的套路。"
    show sora 20i with dissolve
    sora "这种事，我没听人说过，也没问过，更没有做过。"
    show sora 4i with dissolve
    extend "\n咦？"
    extend "\n对了，穗海和猫山呢？"
    me "刚才他们往操场的摊位那边过去了。"
    extend "\n啊，正好回来了。"
    window hide
    hide tuki with dissolve
    hide sora with dissolve
    play sound "fx/running.ogg"
    show sakuya 24i at topleft
    show saburo 10i at topright with dissolve
    window show
    saburo "哟~我回来了~！"
    extend "\n难得出来一趟，就想着买点果汁的下酒菜~！"
    sakuya "炸鸡，炒面，土豆还有章鱼烧！"
    extend "\n给我们买了好多呢~。"
    me "『给我们买了好多』，不是你们自己买的吗？"
    show sakuya 4i with dissolve
    sakuya "怎么会是我们买的啊！"
    show sakuya 21i with dissolve
    extend "\n是老师的好意呀。"
    show saburo 17i with dissolve
    saburo "我就说了，要一起过来的。"
    extend "\n这家伙，真的好小气啊~。"
    show saburo 19i with dissolve
    extend "\n不过嘛，我也是兴致勃勃地去交涉的！"
    "真是不屈不挠……。将来，可能要成为大人物。"
    play sound "fx/dash.ogg"
    extend "\n但是，我懂我懂。老师你其实也懂吧！！"
    extend "\n这么可爱的两个学生央求你，你怎么能拒绝呢。"
    hide sakuya with dissolve
    hide saburo with dissolve
    show tomo 4i at topleft with dissolve
    tomo "厉害，Nice~！！"
    show tomo 2i with dissolve
    extend "\n那我们就心怀感激地收下了！"
    show sinobu 12i at topright with dissolve
    sinobu "之后，我们也得去跟老师道谢。"
    me "嗯。"
    extend "\n总之，执行委员都到齐了。"
    stop music fadeout 3.0
    extend "\n就让我们举杯，共同庆祝2年1班和2年2班合办的咖啡店取得成功吧。"
    extend "\n那么，有请两个代表来带头干杯吧。"
    window hide
    hide sinobu with dissolve
    hide tomo with dissolve
    show tomo 17i at top with dissolve
    play music "school_festival.ogg"
    window show
    tomo "好！"
    show tomo 13i with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    extend "\n各位~大家杯子都装了果汁吧~？"
    everyone "是的~。"
    hide tomo with dissolve
    show tubasa 9i at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tubasa "那……干杯！！"
    window hide
    play sound "fx/sparkle.ogg"
    show cg remarkable at center with Radial(0.5)
    window show
    everyone "干杯！！！"
    window hide
    show cg school_building1_night with dissolve
    window show
    "咕嘟咕嘟咕嘟！"
    show bg schoolyard1_night at center
    me "嗯！真好喝！！"
    extend "\n劳动之后喝的饮料为什么能让人这么舒服。"
    extend "\n简直就像下班后的啤酒一样！"
    window hide
    hide cg with Dissolve(0.7)
    hide tubasa with Dissolve(0.7)
    show sintarou 20i at top with dissolve
    window show
    sintarou "你在说啥老头子一样的话啊。"
    extend "\n对我们来说还早吧。"
    window hide
    hide sintarou with dissolve
    show saburo 2i at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    window show
    saburo "嚼嚼……"
    extend "\n我……嚼嚼……"
    show saburo 13i with dissolve
    extend "章鱼烧……嚼嚼……"
    extend "\n……虽然……"
    show saburo 20i with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/dash.ogg"
    extend "嚼嚼嚼嚼……吵闹……"
    show saburo 7i with dissolve
    $ renpy.transition(Quake(30, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    extend "嚼嚼……"
    show saburo 17i with dissolve
    extend "\n这个……嚼嚼……"
    hide saburo with dissolve
    show tubasa 8i at topright
    show saburo 10i at topleft with dissolve
    play sound "fx/cute2.ogg"
    saburo "做得相当……嚼嚼……好吃！"
    show tubasa 7i
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tubasa "呐，猫山同学！"
    extend "\n你一边吃一边说话，我都听不清楚你在说什么，\n而且吃的东西到处乱飞……！！"
    window hide
    hide tubasa with dissolve
    hide saburo with dissolve
    show tomo 31i at top with dissolve
    window show
    tomo "看起来真好吃~！！"
    extend "\n我也来一份~！"
    show tomo 18i with dissolve
    play sound "fx/triangle.ogg"
    extend "\n……诶？？我的份呢？"
    hide tomo with dissolve
    show sakuya 3i at topleft
    show tomo 28i at topright with dissolve
    sakuya "嘿！"
    extend "\n这可轮不到你来吃！！"
    show sakuya 24i with dissolve
    extend "\n啊~绝品啊，这章鱼烧。"
    show tomo 5i with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tomo "技，技安！！！"
    extend "\n把那章鱼烧给我~！！"
    hide tomo with dissolve
    hide sakuya with dissolve
    play sound "fx/wind_slash.ogg"
    "作哉和友"
    play sound "fx/eureka.ogg"
    "开始你争我抢起来"
    play sound "fx/explosion2.ogg"
    "。"
    window hide
    show sinobu 26i at top with dissolve
    window show
    sinobu "……焰火，真是漂亮呢。"
    show sora 2i at topleft with dissolve
    sora "嗯，让人感觉心平气和。"
    show tuki 9i at topright with dissolve
    tuki "劳顿之后的疲惫也缓解了。"
    hide tuki with dissolve
    hide sora with dissolve
    hide sinobu with dissolve
    play sound "fx/sparkle.ogg"
    show tuki 4i at topright
    show sora 32i at topleft
    show sinobu 18i at top with dissolve
    "忍＆月＆空" "（陶醉……）"
    hide tuki with dissolve
    hide sora with dissolve
    hide sinobu with dissolve
    "就这样，在热闹非凡的后夜祭中，我们开了一场小小的庆功宴。"
    "……。"
    window hide
    show cg c88 1 at center with Radial(0.5)
    window show
    "友，"
    show cg c88 2 with Radial(0.5)
    extend "友，"
    show cg c88 3 with Radial(0.5)
    extend "翼，"
    show cg c88 4 with Radial(0.5)
    extend "月，"
    show cg c88 5 with Radial(0.5)
    extend "空，"
    show cg c88 6 with Radial(0.5)
    extend "忍，"
    show cg c88 7 with Radial(0.5)
    extend "作哉，"
    show cg c88 8 with Radial(0.5)
    extend "三朗，"
    extend "慎太郎"
    window hide
    show cg moon_night with FadeWhite(0.8)
    window show
    "……在这个梦幻的世界中，能和大家搞好关系，实在是太好了。"
    extend "\n御咲祭也圆满成功了，也和大家一起看了这焰火。"
    extend "\n愿望全都实现了。……"
    window hide
    show cg campfire_sparks with Dissolve(0.8)
    window show
    "在这片燃烧的红炎之中，我的意识逐渐淡去……。"
    extend "\n……梦已经结束了。"
    "梦的记忆是模糊的。"
    extend "\n在醒过来的同时，也会忘记这场梦。"
    extend "\n只留下甜美的回忆，其他的一切都被带去忘却的彼方而消散。"
    stop music fadeout 4.0
    "好了……差不多该起来了。"
    window hide
    hide tubasa with dissolve
    hide sinobu with dissolve
    hide sora with dissolve
    hide cg with dissolve
    hide bg with dissolve
    hide tuki with dissolve
    pause 0.6
    window show
    "…。"
    window hide
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.6
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "哔哔哔哔哔哔哔哔"
    window hide
    show bg protagonist_room_morning at center with dissolve
    window show
    me "啊……已经早上了吗……？"
    extend "\n唔~我好像并没有睡多少啊……。"
    stop sound fadeout 0.5
    "我望向餐桌，上面放着一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……"
    extend "啊，对对对，昨天回来的时候拿到的。"
    extend "\n那些孩子们，真可爱啊……。"
    me "……好！那天我一定要去好好享受！"
    play sound "fx/cute2.ogg"
    extend "\n然后在脑海里尽情幻想！！"
    window hide
    hide bg with dissolve
    stop music fadeout 0.5
    window show
    "御咲祭当天ーーーーーー"
    window hide
    play music "quiet_lunch.ogg"
    play sound "fx/crowd_noise.ogg"
    show bg school_building_full at center with Radial(1.0)
    pause 0.4
    show bg hallway with Dissolve(1.0)
    window show
    me "我想想……记得说是2年1班和2年2班的咖啡店。"
    extend "\n唔？"
    play sound "fx/sliding_door.ogg"
    show bg cafe with dissolve
    extend "是这个吗？"
    "正当我站在店门口犹豫不决的时候，"
    extend "穿着红领带的男孩从店里走了出来。"
    window hide
    show cg adult at center with FadeWhite(0.8)
    window show
    unknown "欢迎光临。"
    extend "您是一个人来吗？"
    extend "\n请往这边走……请尽情享受吧。"
    window hide
    hide bg with Radial(1.0)
    hide cg with Radial(1.0)
    pause 0.6
    show bg cafe_evening at center with Radial(0.7)
    pause 0.6
    show bg alled with Dissolve(0.8)
    pause 1.3
    stop music fadeout 1.5
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.8
    hide bg with dissolve
    return