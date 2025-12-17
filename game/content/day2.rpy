# -*- coding: utf-8 -*-
# Converted from 000001B3.lns

label day2:
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.5
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "（哔哔哔哔哔哔哔哔哔）"
    me "嗯……。"
    window hide
    show bg protagonist_room_morning at center with Radial(0.5)
    window show
    mother "[player_name]——！已经早上咯——快点起床——！！"
    "客厅里传来妈妈的声音。"
    me "……得去公司了。"
    stop sound fadeout 1.0
    "我慢慢爬出被窝后，又听到了母亲的声音。"
    mother "你在干什么呀~？"
    extend "\n你要是再磨磨蹭蹭的，上学可就要迟到咯~！"
    "嗯？"
    "我猛地站起身，往穿衣镜里一看——"
    stop music fadeout 0.5
    play music "lively_boys.ogg"
    play sound "fx/eureka.ogg"
    show 効果 remarkable at center with FadeWhite(0.5)
    "\n出现的竟然是一副看着笨笨的初中生模样！"
    extend "\n我依然还是初中生的模样！！"
    "梦还没醒。"
    extend "我好像在梦里醒了……！"
    window hide
    hide 効果 with dissolve
    window show
    me "好！！！"
    extend "\n今天我也要精神百倍地去上学！！！！！"
    play sound "fx/door_open.ogg"
    "（咔嚓！）"
    window hide
    pause 0.3
    window show
    mother "怎、怎么了？突然大喊大叫的。"
    extend "\n是身体不舒服吗？今天要不先不去学校了？"
    me "没有没有！没事的！！"
    "我满面笑容地向母亲表示我没事，\n母亲却带着一脸不安的表情回到了客厅。"
    "以前的母亲，总是会因为我一点点小事就担心不已啊。"
    extend "\n如今现实中的她已经对我冷淡许多了。"
    "不经意间，我感受到了自己的成长，也感受到了来自家人的爱。"
    "啊，糟糕。"
    extend "要是再沉浸在感伤当中，我真的就要迟到了。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label day2_1:
    play sound "fx/door_open.ogg"
    show bg residential_area at center with Radial(0.5)
    play music "going_to_school.ogg"
    window show
    me "哈啊~天气真好。"
    extend "\n我居然会开始期待起上学来，\n要是初中时代的时候就能这样想的话就好了。"
    "身体好轻盈……。"
    extend "\n世界仿佛以我为中心旋转着。"
    "我带着雀跃的心情跑了起来。"
    extend "\n这时——"
    window hide
    hide bg with dissolve
    return

label day2_1_tomo:
    show bg school_route at center with dissolve
    stop music fadeout 0.3
    window show
    unknown "[player_name]君，\n危险！！！"
    me "诶？"
    "（猛地一拉）"
    play sound "fx/wind_slash.ogg"
    me "呜哇！！！"
    play sound "fx/sudden_brake.ogg"
    "（急刹车声——！！！！）"
    $ renpy.transition(Quake(0, 100, 0.2, 0.065), layer='master')
    play sound "fx/fall_down.ogg"
    show bg sky with dissolve
    "事发突然，我完全没反应过来。"
    extend "\n有人拉住了我的袖子，而一辆卡车从我眼前驶过。"
    driver "好险，小鬼！！\n给我好好看红绿灯啊！！！"
    "我听着卡车司机骂骂咧咧的声音，呆呆地望向前方，只见红灯亮着。"
    window hide
    play music "emergency.ogg"
    show cg c10 at center with FadeWhite(0.5)
    window show
    tomo "呼~，差一点就……"
    extend "\n喂！[player_name]君！！\n过马路要看红绿灯呀！"
    "和我说话的，是友。"
    extend "\n被友拉住袖子倒下的我，\n此刻正以一种被他抱在怀里的姿势，倒在人行道上。"
    stop music fadeout 2.0
    show bg school_route
    "果然眼睛圆滚滚的，很可爱啊……。"
    extend "\n呆住的我近距离看着友，心里这么想着。"
    window hide
    hide cg with dissolve
    hide tomo with dissolve
    play music "going_to_school.ogg"
    show tomo 26 at top with dissolve
    window show
    tomo "真是的~。"
    extend "\n啊~还好你没事！"
    "友让我站了起来，确认绿灯亮起后，边走边对我说道。"
    me "对、对不起，友君。"
    extend "\n因为从早上开始就遇上了一些好事，我有些兴奋……。"
    show tomo 27 with dissolve
    tomo "好事？什么好事？"
    extend "\n啊，难道说~"
    show tomo 11 with dissolve
    play sound "fx/boing.ogg"
    extend "刚醒来的一发\n比平时的还要舒服吗？"
    me "一发？"
    show cg adult at center with FadeWhite(0.4)
    play sound "fx/wow2.ogg"
    extend "啊，就是说啊~。\n多巴胺不断分泌，情不自禁射了两发，不对，是三发~\n哎呀，年轻真好啊……"
    hide cg with Dissolve(0.2)
    play sound "fx/dash.ogg"
    extend "不对！！\n为什么每次都要聊这些话题啊，你这家伙……"
    show tomo 4 with dissolve
    tomo "有什么问题嘛！"
    show tomo 25 with dissolve
    extend "\n[player_name]君明明也挺喜欢这种话题的啊！。"
    me "也、也算不上太喜欢吧~。"
    show tomo 3 with dissolve
    tomo "我的朋友~。"
    show tomo 2 with dissolve
    extend "\n你知道吗？"
    extend "\n自己明明是变态，却不承认。\n没有什么比这样更丑陋了哦~"
    me "呜……。"
    show tomo 15 with dissolve
    play sound "fx/impact_japanese.ogg"
    tomo "男人全都是变态，这是常识！"
    show tomo 39 with dissolve
    extend "\n……嗯，好像小慎也这么说过。"
    me "你们两个应该多有点小孩该有的样子才对…。"
    show tomo 11 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tomo "人家本来就是小孩子嘛~小孩子对性的好奇心就是很强烈的嘛~"
    me "嘿。"
    extend "\n那么就让我来满足你对性的好奇心吧？"
    show tomo 28 with dissolve
    tomo "诶。"
    me "哎呀~你都说到这份上啦。"
    extend "\n作为友君的知心好友，我也想帮助你，"
    extend "\n不，是必须帮助你。"
    show tomo 18 with dissolve
    tomo "不、不是，可是……你看！"
    show tomo 19 with dissolve
    extend "那种事情可不能随便做，\n忍也这么说过……。"
    "哈哈哈。"
    extend "\n像这样，一旦真的被邀请做这种事就畏首畏尾起来，\n这点来说还是很像小孩子的。"
    me "那是针对陌生人、或者坏心眼的大人，\n只有对方是那种人的情况，才不能随便做，对吧？"
    extend "\n我们可是，你看，朋友嘛。所以说……。"
    play sound "fx/wind_slash.ogg"
    show cg adult at center with FadeWhite(0.4)
    "我牵起友的手。"
    tomo "不……不……"
    me "好不好嘛？"
    window hide
    hide tomo with dissolve
    hide cg with dissolve
    show tubasa 18 at top with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    window show
    tubasa "友、友君！！！"
    play sound "fx/boing.ogg"
    "友＆我" "哇！"
    "被突然从电线杆阴影里冒出来的翼吓了一跳，\n我们俩不约而同地叫出了声。"
    extend "\n这什么情况，他是怎么冒出来的……难道是有『任意门』吗？"
    window hide
    hide tubasa with dissolve
    show tomo 28 at topleft
    show tubasa 16 at topright with dissolve
    window show
    tubasa "[player_name]君！"
    extend "\n请、请不要说这种骗得友君\n团团转的话了！！"
    show tomo 29 with dissolve
    tomo "小、小翼。\n早、早上好……。"
    show tubasa 8 with dissolve
    tubasa "啊……那个……"
    show tubasa 3 with dissolve
    extend "早、早上好……。"
    "虽然他为了友的事鼓足干劲地冲了出来，\n但这股气势转眼间就萎缩下去了，"
    show tubasa 15 with dissolve
    "他又变回了平时那副畏畏缩缩的样子。"
    extend "\n居然认真到这种程度……。"
    extend "我是不是有点得意忘形了。"
    me "我、我是在开玩笑的！翼君。"
    extend "\n友也是，对不起！"
    extend "\n本来只是想顺着你说的来着，\n但好像玩笑开得过火了？"
    show tomo 20 with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    tomo "不对不对完全不对——！"
    show tomo 19 with dissolve
    extend "\n总觉得[player_name]君说的……语气好像很认真，感觉好羞耻啊……"
    show tubasa 14 with dissolve
    tubasa "……。"
    "友害羞地说道，而翼则露出一副复杂的表情\n看向了我这边。"
    hide tubasa with dissolve
    hide tomo with dissolve
    show tubasa 10 at top with dissolve
    "我对着翼耳语道。"
    me "~~~~~。"
    show tubasa 17 with dissolve
    tubasa "诶？"
    hide tubasa with dissolve
    show tomo 21 at top with dissolve
    tomo "嗯？[player_name]君，你跟翼说了什么？"
    me "秘~密~♪"
    show tomo 27 with dissolve
    tomo "诶~告诉我嘛！"
    me "不~行♪"
    show tomo 40 with dissolve
    tomo "呜！"
    me "等你抓住我，我再告诉你！"
    hide tomo with dissolve
    show tubasa 17 at topright
    show tomo 18 at topleft with dissolve
    play sound "fx/running.ogg"
    "我这么说着，就跑了起来。"
    hide tomo with dissolve
    play sound "fx/running.ogg"
    extend "\n友一边喊着『等等！』一边追了上来。当然了，翼也紧随其后。"
    play sound "fx/running.ogg"
    hide tubasa with dissolve
    extend "\n我一边感受着这种似曾相识的感觉，一边向着学校跑去。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label day2_1_sintarou:
    show bg school_route at center with dissolve
    stop music fadeout 0.3
    window show
    unknown "喂[player_name]君！！\n危险啊啊！！！"
    me "诶？"
    "（猛地一拉）"
    play sound "fx/wind_slash.ogg"
    me "呜哇！！！"
    play sound "fx/sudden_brake.ogg"
    "（急刹车声——！！！！）"
    $ renpy.transition(Quake(0, 100, 0.2, 0.065), layer='master')
    play sound "fx/fall_down.ogg"
    show bg sky with dissolve
    "事发突然，我完全没反应过来。"
    extend "\n有人拉住了我的袖子，而一辆卡车从我眼前驶过。"
    driver "好险，小鬼！！\n给我好好看红绿灯啊！！！"
    "我听着卡车司机骂骂咧咧的声音，呆呆地望向前方，只见红灯亮着。"
    window hide
    play music "emergency.ogg"
    show cg c24 at center with FadeWhite(0.5)
    window show
    sintarou "千、千钧一发——Safe！"
    extend "\n哎呀~不要一大早的就让我这样提心吊胆的啊[player_name]桑~。\n啊~真是可喜可贺可喜可贺。"
    "正在跟我说话的，是慎太郎。"
    extend "\n被慎太郎拉倒在地的我，\n被他抱在怀里，瘫倒在人行道上。"
    stop music fadeout 2.0
    show bg school_route
    "那双下垂眼和看起来软乎乎的脸颊，真让人安心啊……。"
    extend "\n呆住的我近距离看着慎太郎，心里这么想着。"
    window hide
    play music "going_to_school.ogg"
    hide sintarou with dissolve
    hide cg with dissolve
    show sintarou 11 at top with dissolve
    window show
    sintarou "哎呀呀，这种事情的话只在二次元的世界里就好了啊。"
    show sintarou 10 with dissolve
    extend "\n我还真是吓了一跳啊~。"
    "慎太郎把我扶了起来，绿灯亮起。一边走着，他一边说道。"
    me "抱、抱歉啊，慎太郎。"
    extend "\n因为从早上开始就遇上了一些好事，我有些兴奋……。"
    show sintarou 4 with dissolve
    sintarou "好事？什么什么？"
    extend "\n啊~难道说~你找到了，\n能证明自己内在其实是25岁的证据什么的？"
    me "那、那个还没……。"
    show sintarou 15 with dissolve
    sintarou "什么~嘛。那到底是什么啊？"
    me "没、没什么……只是，作为一个初中生，\n在今天也能和慎太郎你们一起度过快乐的校园生活什么的，"
    extend "\n让我实在是高兴得不得了啊。"
    show sintarou 14 with dissolve
    sintarou "……。"
    "慎太郎呆呆地看着我。"
    extend "\n怎么了，我说了什么奇怪的话吗？"
    show sintarou 9 with dissolve
    sintarou "哎呀~你这人设还真是做全套的啊~"
    me "诶？"
    show sintarou 20 with dissolve
    sintarou "你是要强调『当个初中生对现在的我来说是非日常体验』，对吧！"
    extend "\n就连咱这个老江湖，一大早都被你搞得有点懵了呀。"
    show sintarou 13 with dissolve
    sintarou "嘛，你的校园生活还长着呢，\n关于那件事，咱会慢慢替你验证的~。"
    me "还长着呢……吗。"
    "这生活，要持续到什么时候呢。"
    extend "\n真的，『还长着』吗……。"
    extend "\n忽然，脑海中闪过疑问。"
    "不，现在考虑这个也没意义。"
    "只要我展现真心的话，就会自然而然地表现得像大人。"
    extend "\n只要继续这样下去，就能让慎太郎相信我是个大人吧。"
    show sintarou 14 with dissolve
    sintarou "啊~那边是——！"
    window hide
    hide sintarou with dissolve
    show sintarou 7 at topleft with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    window show
    extend "\n喂——！小三朗——！！"
    "顺着慎太郎的视线看去，三朗正站在人行道的那头。"
    show saburo 12 at topright with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    saburo "呃！！"
    show saburo 15 with dissolve
    extend "\n一大早就遇见这个不像话的家伙啊……。"
    show sintarou 27 with dissolve
    sintarou "什么不像话的家伙嘛~。"
    show sintarou 27 with dissolve
    extend "\n小三朗见到咱也很高兴吧~？"
    show cg adult at center
    play sound "fx/wow2.ogg"
    show sintarou 12 with dissolve
    extend "咱们可是连彼此身上有多少颗痣都知道的关系呢~。"
    show saburo 25 with dissolve
    saburo "是啊……\n那天晚上我们还一起把角角落落都数遍了呢……真是火热的一晚。"
    hide cg with Dissolve(0.2)
    hide sintarou with Dissolve(0.2)
    hide saburo with Dissolve(0.2)
    show saburo 3 at topright with Dissolve(0.2)
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/dash.ogg"
    extend "\n不对，你这是在说什么鬼话啊！！！怎么可能有那种事啊你个白痴！！\n你的脑袋里面装的都是什么啊！"
    show sintarou 9 at topleft with dissolve
    sintarou "嘛，别那么害羞嘛，别害羞嘛。"
    show saburo 14 with dissolve
    saburo "才不是害羞！"
    show saburo 15 with dissolve
    extend "\n真是的……[player_surname]也是，一大清早的和这家伙一起上学有够受的吧。\n辛苦了。"
    me "没有那回事哦。"
    extend "\n拜他所赐，我一大清早就心情很愉快呢。"
    show sintarou 4 with dissolve
    sintarou "是吧~！"
    extend "\n刚才我们俩还说了悄悄话呢~。"
    show saburo 6 with dissolve
    saburo "悄悄话？"
    extend "\n是什么啊。"
    me "啊，不是……那是……。"
    show sintarou 12 with dissolve
    sintarou "是秘密所以肯定不会告诉你啦~。"
    show saburo 8 with dissolve
    saburo "唔……让人火大啊。"
    show sintarou 7 with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sintarou "喵——！\n难道说小三朗是在吃醋吗？？"
    show sintarou 12 with dissolve
    extend "\n安~啦！\n之后咱也会给三朗酱留出充足的『二人世界』时间的啦♪"
    show saburo 3 with dissolve
    saburo "我、我我我我我我才不要呢！"
    show saburo 15 with dissolve
    extend "\n唔……和这家伙在一起果然会让人变得奇怪！！"
    show saburo 11 with dissolve
    extend "\n我就先走了！\n回见！！"
    play sound "fx/running.ogg"
    hide saburo with dissolve
    "三朗慌慌张张地跑掉了。"
    extend "\n简直就像是夫妻相声一样啊。"
    hide sintarou with dissolve
    me "慎太郎，你真喜欢三朗啊。"
    window hide
    show sintarou 1 at top with dissolve
    window show
    sintarou "是啊~♪"
    extend "\n自从之前三朗酱来过我家的澡堂以后，\n咱就被他迷得神魂颠倒了呢~。"
    play sound "fx/eureka.ogg"
    me "在、在澡堂里做了什么！！？"
    extend "\n速速道来！！！"
    show sintarou 4 with dissolve
    sintarou "不~行♪"
    extend "\n这是咱和三朗酱之间的秘密哦~。"
    me "唔……是吗。"
    "唔……好不容易现实BL就在眼前，\n不告诉我细节简直太折磨人了。"
    "嗯~其实是，三朗君的身体超级色情之类的……？"
    extend "\n『脱下衣服以后会很厉害哦！！』之类的感觉？"
    show sintarou 25 with dissolve
    sintarou "所以啊，咱无论如何\n都想把那孩子拉进『这边』的世界！"
    me "拉进这边吗……厉害啊。"
    extend "\n我初中的时候，即便有心仪的男孩子，\n但想着『他肯定是直男』就放弃了啊~。"
    show sintarou 9 with dissolve
    sintarou "那孩子可是很有潜力的哦~。"
    show sintarou 13 with dissolve
    extend "\n再加把劲就能追到手了，\n今后咱也会继续努力的~！"
    me "如果真的追到了，之后会做什么呢？"
    show cg dark at center
    play sound "fx/shock.ogg"
    show sintarou 5 with dissolve
    sintarou "咱要把他身上的黑痣数量彻底数个遍！"
    "奥村慎太郎，可怕的孩子……。"
    hide cg with dissolve
    me "只有小孩子自己做这种事可不好！！"
    extend "\n如果真有那一天的话，我作为监护人一定也要在场吧！"
    show sintarou 1 with dissolve
    sintarou "嘛~前提是[player_name]君如果能证明自己其实是大人的话~"
    extend "\n咱很期待那一天哦~♪"
    me "当然，我一定会证明的！！"
    hide sintarou with dissolve
    "鼓足一整天的干劲后，我们一同向学校走去。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label day2_1_sinobu:
    show bg school_route at center with dissolve
    stop music fadeout 0.3
    window show
    unknown "[player_surname]君……！"
    me "诶？"
    "（猛地一拉）"
    play sound "fx/wind_slash.ogg"
    me "呜哇！！！"
    play sound "fx/sudden_brake.ogg"
    "（急刹车声——！！！！）"
    $ renpy.transition(Quake(0, 100, 0.2, 0.065), layer='master')
    play sound "fx/fall_down.ogg"
    show bg sky with dissolve
    "事发突然，我完全没反应过来。"
    extend "\n有人拉住了我的袖子，而一辆卡车从我眼前驶过。"
    driver "好险，小鬼！！\n给我好好看红绿灯啊！！！"
    "我听着卡车司机骂骂咧咧的声音，呆呆地望向前方，只见红灯亮着。"
    window hide
    play music "emergency.ogg"
    show cg c32 at center with FadeWhite(0.5)
    window show
    sinobu "哈啊……千钧一发。"
    extend "\n[player_surname]君，过马路看红绿灯这种规矩要好好遵守啊。"
    "和我搭话的，是忍。"
    extend "\n被忍拉着手倒下后，\n我被他抱在怀里，倒在人行道上。"
    stop music fadeout 2.0
    show bg school_route
    "果然，忍长得非常漂亮啊……像女孩子一样。"
    extend "\n呆住的我近距离看着忍，心里这么想着。"
    window hide
    hide cg with dissolve
    play music "going_to_school.ogg"
    show sinobu 2 at top with dissolve
    window show
    sinobu "你在发什么呆呢。"
    "忍把我扶了起来，看着绿灯亮起，边走边说道。"
    me "抱、抱歉，忍君。"
    extend "\n因为从早上开始就遇上了一些好事，我有些兴奋……。"
    show sinobu 3 with dissolve
    sinobu "……这样啊。"
    extend "\n兴奋得直接不看红绿灯就过马路很危险，可不要太飘飘然哦。"
    play sound "fx/boing.ogg"
    me "呜，你说得对……"
    extend "\n我会注意的。"
    show sinobu 5 with dissolve
    sinobu "……所以，发生了什么？"
    me "诶？"
    sinobu "发生了什么好事，让你兴奋得这么走神？"
    me "啊，不是……只是想到今天也能像这样和大家一起度过，\n就觉得很高兴。"
    show sinobu 23 with dissolve
    sinobu "……这样啊。"
    extend "\n结果因为太兴奋而被车撞到的话，可就本末倒置了呢。"
    extend "\n你能平安无事就好。"
    me "是……。"
    show sinobu 4 with dissolve
    sinobu "……。"
    me "……。"
    show cg sky at center with dissolve
    play sound "fx/triangle.ogg"
    "不、不行啊啊啊……话题完全无法进行下去。"
    extend "\n但是，我可不能气馁！"
    extend "\n好不容易能和如此可爱的男孩子一起上学。"
    extend "\n我一定要好好享受这段时光！！"
    window hide
    hide cg with dissolve
    hide sinobu with dissolve
    window show
    me "忍、忍君，你有不吃的东西吗？"
    show sinobu 3 at top with dissolve
    sinobu "没有。"
    me "那，你平常都看什么电视节目？"
    show sinobu 5 with dissolve
    sinobu "看MHK的『新闻7点钟』。"
    me "那、那你平时都是在哪里玩的呢~？"
    show sinobu 4 with dissolve
    sinobu "宝咲。"
    "咕唔……完全不知道该怎么展开话题啊！！"
    "但是，"
    play sound "fx/entrance.ogg"
    "我不会气馁！"
    play sound "fx/entrance.ogg"
    "我不会沮丧！"
    play sound "fx/entrance.ogg"
    "我不能哭啊~！！"
    show cg remarkable with Dissolve(0.2)
    play sound "fx/tadaa.ogg"
    extend "\n加油加油，[player_name]酱——！！！"
    window hide
    hide cg with Dissolve(0.2)
    hide sinobu with Dissolve(0.2)
    window show
    me "那、那你喜欢玩什么游戏呢？"
    show sinobu 2 at top with dissolve
    sinobu "……战斗类的。"
    me "……喜欢看什么动画？"
    show sinobu 8 with dissolve
    sinobu "……战斗类的。"
    "战斗类的啊……我也不太懂呢。"
    extend "\n话说回来，从我擅长的领域切入不就好了嘛！"
    me "那那那，喜欢看什么漫画？"
    show sinobu 6 with dissolve
    sinobu "……《东斗神拳》。"
    play sound "fx/eureka.ogg"
    "居然是《东斗神拳》啊！！！"
    extend "\n唔……虽然总听到这部作品是神作，但我没看过。"
    extend "\n可恶啊~，要是读过这部作品，就能和他有更多的话题了！！"
    me "你喜欢《东斗神拳》的什么地方呢？"
    show sinobu 11 with dissolve
    play sound "fx/sparkle.ogg"
    sinobu "登场人物个个都很热血帅气。"
    extend "\n男人们那种硬汉般的生存方式真是太棒了。"
    show sinobu 29 with dissolve
    extend "\n无论是我方，还是敌方，都不是一味地使用暴力，"
    extend "\n而是各自怀揣着信念，并赌上这份信念去战斗的啊。"
    me "哦、哦哦~！\n看来你很喜欢这部作品啊。"
    show sinobu 12 with dissolve
    sinobu "嗯。"
    extend "\n[player_surname]君也看过吗？"
    me "没、没有呢~……一直没找到机会，就没读过。"
    extend "\n啊，对了！下次可以借我看看吗？"
    extend "\n如、如果可以的话……。"
    show sinobu 26 with dissolve
    sinobu "可以哦。"
    extend "\n不过一口气读完27卷很困难，我会按顺序借给你的。"
    me "真的吗！？谢谢！"
    extend "\n好开心啊~！！终于可以读到那部名作了！"
    "太好了！这样一来就有了共同的爱好！！"
    extend "\n简直就像恋爱中的少女一样，不过我在意的不是这个。"
    extend "\n只要能和他友好相处，然后看到他各种各样的表情就可以了。"
    me "你是什么时候开始读《东斗神拳》的呢？"
    extend "\n是因为在朋友之间流行起来了吗？"
    show sinobu 3 with dissolve
    sinobu "不是。"
    extend "\n是因为我憧憬强大的男人，所以才开始读的。"
    me "强大的男人？"
    extend "\n但是，你现在也已经足够强了吧！"
    extend "\n空手道在县里也名列前茅吧？"
    show sinobu 4 with dissolve
    sinobu "现在还算可以……"
    extend "\n不过，以前很弱，"
    show sinobu 20 with dissolve
    extend "身心都是。"
    me "是吗。\n那你能变强真是太好了！"
    extend "\n就像梦想实现了的感觉吧？"
    show sinobu 22 with dissolve
    sinobu "怎么说呢……我还，不太清楚。"
    me "你是打算变得更强啊！"
    extend "\n真厉害~。"
    show sinobu 1 with dissolve
    sinobu "……关于我空手道水平的事是从友那里听说的吗？"
    me "嗯。"
    extend "\n昨天，在武道场里。"
    show sinobu 18 with dissolve
    sinobu "……这样啊。"
    "这样的忍，不知为何看起来很高兴。"
    hide sinobu with dissolve
    "我侧眼看着这样的他，感觉似乎和忍的关系稍微变好了些，\n于是心情愉快地向学校走去。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label day2_1_tubasa:
    show bg school_route at center with dissolve
    stop music fadeout 0.5
    play music "cute_silly.ogg"
    show tubasa 12 at top with dissolve
    window show
    tubasa "诶嘿嘿……昨晚能和友君通电话真是太好了啊。"
    show tubasa 34 with dissolve
    extend "\n呜~！睡意朦胧的友君也好可爱啊……。"
    show tubasa 4 with dissolve
    extend "\n不过话说回来，他真的好喜欢色色的话题啊。"
    extend "\n我可得继续努力学习，跟上友君的节奏才行啊。"
    show tubasa 11 with dissolve
    tubasa "如、如果这样的话，万一到了『那种时候』，\n说不定我就能好好辅助他了……诶嘿嘿……。"
    show cg adult at center
    show tubasa 4 with dissolve
    play sound "fx/sparkle.ogg"
    extend "哈啊……那种场面……友君的裸体……。"
    show tubasa 3 with dissolve
    extend "\n呜呜！光是想象就让人受不了了啊！！"
    show tubasa 11 with dissolve
    tubasa "之前偶然闻到的胯下的味道，也是那么的好闻，\n如果可以的话，真想啊呜一口把他吃掉呢♪"
    show cg dark
    play sound "fx/heartbeat.ogg"
    show tubasa 38 with dissolve
    extend "\n……干脆干脆，把他带回去，把他关起来好了……。"
    show tubasa 34 with dissolve
    extend "\n这样的话，友君就一辈子……开玩笑的啦……啊哈哈。"
    window hide
    hide tubasa with dissolve
    hide cg with dissolve
    $ renpy.transition(Quake(0, 100, 0.15, 0.069), layer='master')
    play sound "fx/shock.ogg"
    window show
    "刚才还高涨的心情瞬间冷却了。"
    extend "\n一大早的，我就看见了不该看的东西啊……。"
    "据说乖巧的孩子内心都是蕴藏着惊人能量的，\n但没、没想到竟然到了这种地步……。"
    "翼君，我之前太小看你对友的爱了……。"
    "他沉浸在妄想中，摇摇晃晃地走上了斑马线。"
    stop music fadeout 0.3
    me "翼君！！！\n危险——！！！！！"
    show tubasa 17 at top with dissolve
    tubasa "诶？"
    play sound "fx/wind_slash.ogg"
    "（猛地一拉）\n"
    show tubasa 8 with dissolve
    play sound "fx/fall_down.ogg"
    $ renpy.transition(Quake(0, 65, 0.1, 0.06), layer='master')
    hide tubasa with dissolve
    tubasa "呜哇！！！"
    show bg sky with dissolve
    play sound "fx/sudden_brake.ogg"
    extend "\n（急刹车声——！！！！）"
    "千钧一发。"
    extend "我拼尽全力拉住了翼的衣角，\n勉强防止了他与卡车相撞。"
    driver "好险，小鬼！！\n给我好好看红绿灯啊！！！"
    "抛下这句话，卡车就开走了。"
    extend "\n信号灯还是红的。"
    me "呼~好险啊……"
    extend "\n翼君，我知道你想事情想得很入迷，但是\n过马路之前要先看红绿灯啊。"
    window hide
    play music "emergency.ogg"
    show cg c41 at center with FadeWhite(0.5)
    window show
    tubasa "啊……咦……[player_name]君……？"
    "翼似乎还没反应过来发生了什么。"
    "被我拉倒在地的翼，\n此刻正以一种被我抱在怀里的姿势，倒在人行道上。"
    "乌黑的头发与白皙的皮肤形成鲜明的对比，好色情啊……。"
    extend "\n我还是第一次这么近距离地看他的脸，\n即便是正倒在地上，我还是不禁看得入迷了。"
    tubasa "我……啊！！！"
    "翼终于理解了现状，变回了平时那副纯真朴实的样子。"
    tubasa "对、对对对对不起！！！"
    extend "\n我、我，那个，我在发呆……！"
    extend "\n真、真的非常对不起！！"
    me "没、没关系的没关系的。\n比起那个，你能平安无事真是太好了。"
    extend "\n……。"
    "像这样看着，他果然好可爱啊。"
    extend "\n柔弱，时常警惕又战战兢兢的样子，\n就像小动物一样，让我不由自主地想去保护。"
    tubasa "那……那个……嗯……是不是该……。"
    me "啊！抱歉抱歉。"
    stop music fadeout 2.0
    show bg school_route
    "连我也跟着发呆是怎么回事！"
    "我放开了翼的手，扶他站了起来，然后迈开了脚步。"
    window hide
    hide cg with dissolve
    play music "going_to_school.ogg"
    show tubasa 9 at top with dissolve
    window show
    tubasa "真、真的是太感谢你了！！"
    extend "\n要是没有[player_name]君的话，我可能已经在车祸启示录的节目里出现了。"
    show tubasa 1 with dissolve
    extend "\n呜呜……我到底在干什么啊…。"
    me "不客气。"
    extend "\n下次在路边意淫的时候，还是克制一点吧。"
    show tubasa 19 with dissolve
    tubasa "诶诶？"
    me "不过，也没办法呢。\n毕竟对友君那么着迷啊……。"
    extend "\n哎呀~翼君意外地很闷骚呢！！\n居然会想那种事情~♪"
    show tubasa 8 with dissolve
    $ renpy.transition(Quake(0, 65, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    tubasa "诶、诶诶诶诶！？"
    extend "\n那个那个！！\n你、你到底在说什么啊！？"
    me "在过马路之前，你不是在自言自语吗。"
    show tubasa 22 with dissolve
    tubasa "不会吧……我说出来了吗……？"
    me "嗯。"
    show cg dark at center
    show tubasa 7 with dissolve
    play sound "fx/shock_big.ogg"
    tubasa "（受暴击！！！）"
    hide cg with dissolve
    show tubasa 3 with dissolve
    tubasa "呜呜呜，我想找个地缝钻进去。"
    "没、没想到竟然是无意识的……真是让人担心啊。"
    extend "\n恋爱，居然会让人这么盲目吗。"
    me "嘛嘛，别那么消沉啦！"
    extend "\n倒不如想，幸好听到的人是我！"
    extend "\n这样一来，我就能更好地支持你的恋爱了！"
    show tubasa 1 with dissolve
    tubasa "是这样吗……"
    me "没错！"
    extend "\n所以啊，来，打起精神吧！"
    show tubasa 22 with dissolve
    tubasa "好……好的……打起精神……"
    "嘴上这么说，翼还是很萎靡。"
    me "喂——，你说话的内容和语气完全不符啊~。"
    extend "\n……嗯？那是……友君和忍君！"
    window hide
    hide tubasa with dissolve
    show cg residential_area at center with dissolve
    show sinobu 12 at topright
    show tomo 12 at topleft with dissolve
    window show
    tubasa "啊，真的呢……"
    "两个人从拐角里走出来，正有说有笑地聊着天。"
    tubasa "呜呜……他们看起来好开心啊。"
    me "那两个人经常待在一起，关系果然很好吧？"
    window hide
    hide tomo with dissolve
    hide sinobu with dissolve
    hide cg with dissolve
    show tubasa 14 at top with dissolve
    window show
    tubasa "何止是关系好……那两个人可是青梅竹马啊。"
    extend "\n他们住在同一栋公寓里，而且两家人的关系也很好。"
    "原来如此……是这样啊。"
    extend "\n还有昨天的作哉。看来翼的恋爱道阻且长啊。"
    show tubasa 3 with dissolve
    tubasa "呜呜…怎么办啊……！"
    me "什么怎么办……"
    extend "\n好不容易见到了，不和他们搭个话怎么行呢！"
    show tubasa 20 with dissolve
    tubasa "可、可是，刚才说了，那两位是青梅竹马啊！"
    extend "\n肯定没有我这种人能插足的余地……。"
    me "正因如此，才更要去搭话啊！！"
    extend "\n所谓恋爱，最重要的就是如何缩短与对方的距离。"
    extend "\n像这样积极地搭话，\n能让你和友君的关系更加亲近的！！"
    show tubasa 9 with dissolve
    tubasa "……呜，嗯……说得对啊。"
    extend "\n那、那我去了！"
    me "好。"
    extend "\n加油哦，期待恋爱的少年！！"
    show tubasa 7 with dissolve
    tubasa "啊……这种事情请不要那么大声说啊……。"
    "说完，翼"
    play sound "fx/running.ogg"
    hide tubasa with dissolve
    "像是逃跑一般朝他们那边去了。"
    "从后面看去，看来是顺利加入到那两人之中了。"
    "眺望着少年们那其乐融融聊天的背影，\n虽是独自一人，我还是心情愉快地向学校走去了。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label day2_1_futago:
    show bg school_route at center with dissolve
    stop music fadeout 0.3
    window show
    unknown "[player_surname]！！"
    unknown "危险！！"
    me "诶？"
    "（猛地一拉）"
    play sound "fx/wind_slash.ogg"
    me "呜哇！！！"
    play sound "fx/sudden_brake.ogg"
    "（急刹车声——！！！！）"
    $ renpy.transition(Quake(0, 100, 0.2, 0.065), layer='master')
    play sound "fx/fall_down.ogg"
    show bg sky with dissolve
    "事发突然，我完全没反应过来。"
    extend "\n有人拉住了我的袖子，而一辆卡车从我眼前驶过。"
    driver "好险，小鬼！！\n给我好好看红绿灯啊！！！"
    "我听着卡车司机骂骂咧咧的声音，呆呆地望向前方，只见红灯亮着。"
    window hide
    play music "emergency.ogg"
    show cg c50 at center with FadeWhite(0.5)
    window show
    tuki "在想什么呢，[player_surname]。"
    extend "\n明明是红灯，你没有注意吗？"
    sora "不过，你没事真是太好了……。"
    extend "\n下次可要小心点哦。"
    "和我说话的，是月和空。"
    extend "\n被两人拉倒在地的我，此刻正被他们左抱右架地倒在人行道上。"
    stop music fadeout 2.0
    show bg school_route
    "虽然他们俩长得并不一样，但都是美男子……。"
    extend "\n呆住的我近距离看着两人，心里这么想着。"
    window hide
    hide cg with dissolve
    play music "going_to_school.ogg"
    show tuki 22 at topleft with dissolve
    window show
    tuki "真是的……[player_surname]君竟然会犯这种低级错误啊。"
    "月把我扶了起来。确认绿灯亮起后，他一边迈开步子，一边说道。"
    me "对、对不起，两位。"
    extend "\n因为从早上开始就遇上了一些好事，我有些兴奋……。"
    show sora 5 at topright with dissolve
    sora "我说你啊。"
    show sora 20 with dissolve
    extend "\n都已经不是小孩子了，可不要因为太兴奋，\n就做出出格的事哦。"
    me "对、对不起……。"
    extend "\n但、但是，初中生还算是小孩子吧？"
    show tuki 17 with dissolve
    tuki "你在胡说什么呢。"
    extend "\n只是现代日本对『成年』的界定比较晚而已，\n在战前的日本或者其他国家，像我们这个年纪，也已经算是大人了啊。"
    show sora 23 with dissolve
    sora "没错没错。"
    extend "\n为了不让我们的祖先大人蒙羞，\n我们得脚踏实地好好做人才行呢。"
    "噢、噢噢……多么懂事的孩子们啊……。"
    extend "\n我这个年纪的时候，完全没有这种自觉啊……。"
    me "你们两个人能这么自律，真的好厉害。"
    show tuki 6 with dissolve
    tuki "赤峰家的教育方针就是这样吧。"
    show sora 5 with dissolve
    sora "听说我们家算是历史悠久的名门，所以可能比较传统吧。"
    me "诶~这样啊。"
    extend "\n也就是说，你们家的房子也是从很久以前就一直保留着的吗？"
    show tuki 4 with dissolve
    tuki "是的。\n虽然随着时代的变迁，我们家的房子也做过几次改建，但基本还是木结构的老房子。"
    extend "\n也许这也是家规吧，我们在家里都是穿和服的。"
    show sora 26 with dissolve
    sora "和服很好哦~。"
    extend "\n穿起来宽松舒适让人很安心，还很暖和，\n而且可以配合体型进行调整，所以很耐穿！"
    show sora 11 with dissolve
    extend "\n大家都应该多穿穿和服的。"
    me "太厉害了。"
    extend "\n你们真的很珍视日本文化啊~。"
    extend "\n穿和服的话……"
    show cg adult at center with Dissolve(0.2)
    play sound "fx/sparkle.ogg"
    extend "该不会连内裤也是那种传统的『兜裆布』吧！"
    hide tuki
    hide sora
    "开玩笑的啦，怎么可能……"
    show tuki 5 at top
    hide cg with Dissolve(0.1)
    stop music fadeout 0.1
    play sound "fx/impact_japanese.ogg"
    tuki "是啊。"
    hide tuki with Dissolve(0.3)
    "诶？"
    play music "going_to_school.ogg"
    $ renpy.transition(Quake(0, 60, 0.1, 0.06), layer='master')
    play sound "fx/boing.ogg"
    me "诶诶诶诶诶诶诶诶！？！？！？！"
    extend "\n这、这这这是真的！？！？！？！"
    show tuki 9 at topleft with dissolve
    tuki "是真的。"
    extend "\n也不用那么吃惊吧。\n我们一直都是穿这个的哦。"
    show tuki 8 with dissolve
    extend "\n对吧，空。"
    show sora 14 at topright with dissolve
    sora "嗯、嗯。"
    extend "\n是这样没错……但是你这么直白地说出来，还是有点害羞啊……。"
    me "那、那个啊，这真的是出于好奇，\n绝没有什么下流的想法，还请不要误解，"
    extend "\n可、可以让我稍微看一下吗？"
    extend "\n毕、毕竟，我还没有亲眼见过兜裆布，想看看实物啊！！"
    "虽说完全没有觊觎之心是骗人的，但也的确很好奇。"
    show sora 8 with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    sora "不、不要啊！\n在路边给人看这种东西也太不像话了！！"
    me "那、那之后去厕所呢！！！"
    show tuki 1 with dissolve
    tuki "不用掩人耳目，可以在体育课换衣服的时候看嘛。"
    show tuki 6 with dissolve
    extend "\n既然你觉得那么稀奇的话，下次我借你一条怎么样？"
    extend "\n话虽如此，毕竟是穿别人的贴身衣物，\n再怎么说心里多少还是会有点抗拒吧。"
    me "不、不会的！！！\n倒不如说，那样更好呢！！！！！"
    show tuki 5 with dissolve
    tuki "是吗……"
    hide tuki with dissolve
    hide sora with dissolve
    show tuki 17 at top with dissolve
    extend "嗯？"
    "（盯……）"
    hide tuki with dissolve
    show sora 4 at topright with dissolve
    sora "怎么了？哥哥。"
    show tuki 1 at topleft with dissolve
    tuki "空，你看，[player_surname]君的眼睛。"
    show sora 4 with dissolve
    sora "嗯~？"
    hide tuki with dissolve
    hide sora with dissolve
    show sora 28 at top with dissolve
    extend "……啊。"
    hide sora with dissolve
    show sora 27 at topright
    show tuki 8 at topleft with dissolve
    tuki "[player_surname]君对于兜裆布的关心，好像不是单纯出于好奇吧？"
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.06), layer='master')
    "（咯噔！）"
    me "啊、啊哈哈哈！！"
    extend "\n才没那回事哦~？"
    extend "\n我也没什么企图哦~？"
    extend "\n没什么特别的啦~"
    show sora 29 with dissolve
    sora "语气不对劲。"
    show tuki 20 with dissolve
    tuki "太可疑了。"
    show cg dark at center with Dissolve(0.3)
    play sound "fx/shock.ogg"
    hide bg with dissolve
    hide tuki with dissolve
    "这、这是怎么回事！？"
    extend "\n糟糕……这样下去的话，好不容易能弄到少年刚脱下的兜裆布的机会，\n就要溜走了！！"
    extend "\n必须得想办法啊！！"
    show cg sky with dissolve
    play sound "fx/boing.ogg"
    me "啊，那个，是这样的！！"
    extend "\n因为我从来没见过兜裆布，"
    extend "\n一想到能借来、而且还能亲自穿在身上，\n所以我才会很期待，才兴奋起来了~！！"
    show bg remarkable at center
    show sora 28 at topright
    show tuki 7 at topleft
    tuki "……不。"
    sora "……不对。"
    hide cg with dissolve
    play sound "fx/impact_japanese.ogg"
    tuki_and_sora "你这眼神，是心怀不轨的眼神！！"
    play sound "fx/shock_big.ogg"
    "（受打击！！！）"
    "完、完全被看穿了。"
    extend "\n多么敏锐的洞察力啊……。"
    extend "\n小的诚惶诚恐，赤峰兄弟……。"
    window hide
    hide cg with dissolve
    hide tuki with dissolve
    hide sora with dissolve
    window show
    me "我、我认输了……。"
    extend "\n话说回来，你们两个，是怎么知道的？"
    show sora 11 at topright with dissolve
    sora "因为我们每天都在锻炼嘛。"
    me "锻炼？锻炼什么？"
    show tuki 9 at topleft with dissolve
    tuki "那个嘛……。"
    show cg sky at center with dissolve
    play sound "fx/chime.ogg"
    "（叮铃叮铃叮铃叮铃）"
    sora "啊！糟糕！！预备铃响了！"
    extend "\n你们俩，快点！"
    play sound "fx/running.ogg"
    "因为聊得太投入，我们上学要迟到了，便向学校跑去。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    hide cg with dissolve
    hide tuki with dissolve
    hide sora with dissolve
    return

label day2_1_sakuya:
    show bg school_route at center with dissolve
    stop music fadeout 0.3
    window show
    stop music
    unknown "喂！！！"
    me "诶？"
    "（猛地一拉）"
    play sound "fx/wind_slash.ogg"
    me "呜哇！！！"
    play sound "fx/sudden_brake.ogg"
    "（急刹车声——！！！！）"
    $ renpy.transition(Quake(0, 100, 0.2, 0.065), layer='master')
    play sound "fx/fall_down.ogg"
    show bg sky with dissolve
    "事发突然，我完全没反应过来。"
    extend "\n有人拉住了我的袖子，而一辆卡车从我眼前驶过。"
    driver "好险，小鬼！！\n给我好好看红绿灯啊！！！"
    "我听着卡车司机骂骂咧咧的声音，呆呆地望向前方，只见红灯亮着。"
    window hide
    play music "emergency.ogg"
    show cg c77 at center with FadeWhite(0.5)
    window show
    sakuya "你这家伙在想什么啊！！"
    extend "\n差点就要死掉了啊！！！"
    "正对我怒吼的人，是作哉。"
    "被作哉拉住袖子倒下的我，\n此刻正以一种被他抱在怀里的姿势，倒在人行道上。"
    stop music fadeout 2.0
    show bg school_route
    "生气时严肃的脸也很可爱啊……这种表情也让人欲罢不能啊……。"
    extend "\n呆住的我在近距离看着作哉时，这么想着。"
    window hide
    hide cg with dissolve
    hide sakuya with dissolve
    play music "going_to_school.ogg"
    show sakuya 20 at top with dissolve
    window show
    sakuya "真是的……一大早就让人提心吊胆的！"
    me "对、对不起，作哉君。"
    extend "\n早上有些开心的事情，就有点飘了……。"
    show sakuya 11 with dissolve
    sakuya "哈啊？很开心……？"
    extend "\n什么事这么开心啊？"
    me "不、不是……只是觉得，今天也能作为一名初中生，\n和大家一起过快乐的校园生活什么的，\n就觉得开心得不得了。"
    show sakuya 17 with dissolve
    sakuya "哈啊啊啊啊？？？\n就因为那种蠢理由差点被车撞了吗！"
    play sound "fx/dash.ogg"
    extend "\n你还是最好去检查一下脑子吧？？\n你这个笨蛋！！"
    play sound "fx/boing.ogg"
    me "呜……对不起……。"
    show sakuya 19 with dissolve
    sakuya "哼……。"
    show sakuya 20 with dissolve
    extend "\n……再说，你昨天都跟我说过吧。"
    me "诶？"
    show sakuya 4 with dissolve
    sakuya "说要和小翼一起玩。"
    me "啊，嗯。确实说过呢。"
    show sakuya 6 with dissolve
    sakuya "所以，你就别做让小翼伤心的事了。"
    me "……嗯，对不起。以后我会注意的。"
    extend "\n谢谢你关心我。"
    show sakuya 26 with dissolve
    sakuya "别误会了啊。"
    extend "\n我不过是怕小翼伤心才帮你一把而已。"
    me "啊……好的……。"
    show cg sky at center with dissolve
    sakuya "……。"
    me "……。"
    sakuya "……。"
    me "……。"
    window hide
    hide sakuya with dissolve
    hide cg with dissolve
    show sakuya 1 at top with dissolve
    window show
    play sound "fx/boing.ogg"
    sakuya "……为啥要沉默啊……搞得像我是什么坏人似的……。"
    "说完，作哉露出了有点过意不去的表情。"
    me "诶……没、没有！！\n作哉君并没有做错什么啊！"
    extend "\n是因为你的话深深触动了我，所以我才沉默的……！"
    extend "\n不如说，谢谢你骂我！"
    show sakuya 11 with dissolve
    sakuya "被骂了还谢我……你是抖M吗？"
    me "不不、不是那个意思啦！"
    extend "\n被你训斥，让我意识到了什么是正确的，\n你已经引导我走向了正确的道路，"
    extend "\n这种时候，一定要好好说声谢谢才行！"
    show sakuya 25 with dissolve
    sakuya "哼——嗯……这样啊。"
    "毕竟都这个年纪了，还被别人训斥什么的，确实很少见……。"
    hide sakuya with dissolve
    extend "\n再说了，被你这样帅气的正太训斥，\n"
    play sound "fx/sparkle.ogg"
    "在我们正太控圈子里，简直就是奖励啊！！！"
    window hide
    window show
    me "嗯，那边的是……喂——，翼君！"
    "我望向了前方，那是翼的身影。"
    show tubasa 2 at top with dissolve
    tubasa "诶……啊，[player_name]君。"
    extend "\n还有作哉君。"
    extend "\n早、早安……。"
    me "早上好~！"
    hide tubasa with dissolve
    show sakuya 19 at topleft with dissolve
    sakuya "……早。"
    show tubasa 19 at topright with dissolve
    tubasa "那个……总感觉，这组合有点罕见呢。"
    show sakuya 20 with dissolve
    sakuya "哈？你有意见吗？"
    show tubasa 21 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tubasa "诶！"
    extend "\n没、没有，我不是那个意思……。"
    me "也不用那么咄咄逼人吧……。"
    show sakuya 25 with dissolve
    sakuya "我才没找茬呢。"
    extend "\n你说是吧，一之濑？"
    show tubasa 1 with dissolve
    tubasa "那个……呃……。"
    show sakuya 16 with dissolve
    sakuya "切……一脸不满的样子。"
    extend "\n像你这种家伙，只要乖乖点头就行了。"
    extend "\n怎么个个都让人火大……。"
    show tubasa 15 with dissolve
    tubasa "是、是。"
    extend "\n对不起……。"
    me "作哉君，也没必要那么说吧？"
    extend "\n要是不对他温柔点，翼君会吓得缩成一团的哦。"
    show sakuya 19 with dissolve
    sakuya "无所谓。"
    show tubasa 2 with dissolve
    tubasa "那、那个……[player_name]君，请不要在意。"
    extend "\n我已经习惯了……。"
    me "但是……。"
    show tubasa 5 with dissolve
    tubasa "而且作哉君也不是什么坏人。"
    extend "\n虽然有时让人害怕，但也有温柔的时候……"
    show sakuya 20 with dissolve
    play sound "fx/boing.ogg"
    sakuya "喂、喂！！你说什么胡话呢！"
    extend "\n我可不记得对你温柔过！！"
    show tubasa 7 with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    tubasa "啊呜呜……对、对不起……！！"
    show sakuya 1 with dissolve
    sakuya "啊啊真是的……果然我应付不来这家伙……。"
    extend "\n我先走了。\n那就这样，[player_surname]！"
    me "诶，等等！"
    play sound "fx/running.ogg"
    hide sakuya with dissolve
    "作哉连头都没回，径直向学校走去。"
    window hide
    hide tubasa with dissolve
    show tubasa 2 at top with dissolve
    window show
    tubasa "走了呢……。"
    me "是啊……。"
    extend "\n话说回来，明明没必要那么冷淡的啊。"
    show tubasa 5 with dissolve
    tubasa "但是，别看作哉君现在那个样子，以前可是非常亲切的哦。"
    me "诶，是这样吗？"
    show tubasa 6 with dissolve
    tubasa "是的。"
    extend "\n……但是，有一天，突然就变冷淡了……。\n然后，就一直是现在这样了。"
    me "你知道是什么原因吗？"
    show tubasa 15 with dissolve
    tubasa "……不，我不太清楚。"
    extend "\n可能是因为我做了什么吧……"
    extend "\n作哉君也没有说什么，而且我清楚他本性是很温柔的，\n所以他现在这样，我其实也没关系的……。"
    me "这样啊……虽然有点在意，\n但既然翼君也觉得没问题的话，那就……。"
    show tubasa 4 with dissolve
    tubasa "嗯。所以，请不用担心。"
    "说完，翼露出了一个无力的笑容。"
    me "……嗯，我知道了。"
    hide tubasa with dissolve
    "我觉得继续说这个话题也不太好，\n于是切换了话题，和翼一起向学校走去。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label day2_1_saburo:
    show bg school_route at center with dissolve
    stop music fadeout 0.5
    play music "cute_silly.ogg"
    show saburo 12 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    window show
    saburo "唔诶……怎么可能有这种事……"
    show saburo 21 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    extend "\n不对不对，那种东西怎么可能进得去那种地方啊。"
    extend "\n呜呀！！竟然真的塞进去了！"
    show saburo 14 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/shock.ogg"
    extend "\n呜哇啊啊这怎么可能啊！！！"
    window hide
    hide saburo with dissolve
    window show
    "那个身影，是三朗君！"
    extend "\n他一边看着书，一边一个人自顾自地兴奋地喊着，\n不过因为封面包了书皮，不知道他在看什么书。"
    "我正想着要不要去跟他搭个话，\n就看到他沉迷在书里，摇摇晃晃地走上了斑马线。"
    stop music fadeout 0.3
    me "三朗君！！\n危险！！！！！"
    show saburo 24 at top with dissolve
    saburo "诶？"
    play sound "fx/wind_slash.ogg"
    "（猛地一拉）\n"
    show saburo 21 with dissolve
    play sound "fx/fall_down.ogg"
    $ renpy.transition(Quake(0, 65, 0.1, 0.06), layer='master')
    hide saburo with dissolve
    saburo "啊！！"
    show bg sky with dissolve
    play sound "fx/sudden_brake.ogg"
    "（急刹车声——！！！！）"
    "千钧一发。"
    extend "我用力地拉住了三朗的衣角，\n勉强防止了他与卡车相撞。"
    driver "好险，小鬼！！\n给我好好看红绿灯啊！！！"
    "抛下这句话，卡车就开走了。"
    extend "\n信号灯还是红的。"
    me "呼~真是好险……"
    extend "\n三朗君，读书固然是好事，但是\n过马路之前要先看红绿灯啊。"
    window hide
    play music "emergency.ogg"
    show cg c67 at center with FadeWhite(0.5)
    window show
    saburo "诶……诶……？"
    "三朗似乎还没反应过来发生了什么。"
    "他被我拉住后跌倒，最后被我抱在怀里，\n倒在人行道上。"
    "细软的头发、猫一样的眼睛，还有小虎牙……真的就像只猫一样。"
    extend "\n我还是第一次这么近距离地看他的脸，\n即便是正倒在地上，我还是不禁看得入迷了。"
    saburo "啊……！抱、抱歉[player_surname]！！"
    extend "\n我，一不小心看漫画看入迷了……。"
    "终于搞清楚情况的三朗，又回到了平常那副慌里慌张的样子。"
    me "没事没事。\n比起那个，你能平安无事真是万幸。"
    saburo "哦、哦哦……。"
    "眼看着三朗的脸就红了起来。"
    saburo "不、不好意思，那个……差不多能放开我了吧？"
    me "啊……抱歉抱歉。"
    stop music fadeout 2.0
    show bg school_route
    "我看三朗看得入迷，完全忘了自己还抱着他，\n听到他的话后我才放开了手，扶他站起身，然后迈起了步子。"
    window hide
    hide cg with dissolve
    play music "going_to_school.ogg"
    show saburo 11 at top with dissolve
    window show
    saburo "真的是对不住啦！\n下次我真的会注意，绝对不边走边看书了。"
    extend "\n要是[player_surname]不在的话，我现在可能已经去西天了。"
    me "真的是哦~。\n明明身手那么敏捷，就不要慢吞吞地『一边一边』啦。"
    extend "\n啊，这是你刚才看的漫画。"
    "我把三朗掉的书捡起来，递给他。"
    show saburo 23 with dissolve
    saburo "啊啊！！谢、谢谢……"
    show saburo 28 with dissolve
    extend "\n[player_surname]……你看过这里面的内容了吗？"
    me "咦？没看到哦。为什么这么问？"
    show saburo 2 with dissolve
    saburo "啊！！那就好！！"
    "正值青春期的男生一脸兴奋地读着，还把书藏起来不让人看见。"
    extend "\n好懂……实在是太好懂了啊，少年！！"
    play sound "fx/eureka.ogg"
    extend "\n刚才藏进包里的那些书，就是你的『圣经』吧！！！"
    show saburo 13 with dissolve
    saburo "比起这个，我得好好谢谢你啊。"
    extend "\n毕竟，[player_surname]可是我的救命恩人！"
    extend "\n对了！今天午饭我请你吧？"
    me "不用啦，我心领了。"
    extend "\n初中生说到底还是在啃老的年纪啊……。\n父母的钱，还是留给自己用吧。"
    show saburo 24 with dissolve
    saburo "哈啊？你在说啥呢？"
    me "啊——没事没事，是我自言自语。"
    extend "\n……啊！三朗君，快看那边！\n是你喜欢的御咲女子学园的学生们哦~。"
    show saburo 27 with dissolve
    saburo "哦——是耶。很可爱啊。"
    "咦……反应有点平淡啊。"
    extend "\n还以为你会表现得更感兴趣一点的……。"
    hide saburo with dissolve
    window hide
    show sintarou 4 at topleft with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    window show
    sintarou "早——啊！你们两个！"
    extend "\n干嘛要盯着女学生看啊~？\n这可不像你啊~。"
    "慎太郎突然出现，轻轻地把手搭在了我们的肩膀上。"
    me "啊，早啊，慎太郎君。"
    show saburo 14 at topright with dissolve
    saburo "糟了是你！！！"
    show sintarou 7 with dissolve
    sintarou "早啊，[player_name]酱！"
    show sintarou 17 with dissolve
    extend "\n还有，小三朗！\n『糟了是你』是什么鬼啊~。"
    extend "\n难得一早就能见到，就表现得开心点嘛~。"
    show saburo 3 with dissolve
    saburo "谁会开心啊！"
    show saburo 20 with dissolve
    extend "\n每次你出现，我就准没好事！！"
    show sintarou 29 with dissolve
    sintarou "太夸张了啦~。"
    extend "\n说起来，咱之前借你的漫画，你看过了吗？"
    show saburo 18 with dissolve
    saburo "那种低俗的漫画，我怎么可能看啊！！"
    extend "\n我今天就还给你！"
    show sintarou 27 with dissolve
    sintarou "哼哼——！！"
    extend "\n难得咱特意借给你的，怎么能这样嘛~三朗酱！"
    show saburo 8 with dissolve
    saburo "什么借给我，明明是你硬塞给我的！"
    extend "\n我可从~~~~来没说过要借你的漫画看哟。"
    show sintarou 29 with dissolve
    sintarou "哎呀不要这么说嘛~这可是咱的一番美意啊！"
    show sintarou 8 with dissolve
    play sound "fx/cute2.ogg"
    extend "\n……啊，那边的不是赤峰兄弟嘛！！"
    extend "\n那咱先走一步了！\n两位，再见啦~。"
    play sound "fx/running.ogg"
    hide sintarou with dissolve
    "慎太郎留下我们几个便跑远了。"
    extend "\n简直就像台风一样……。"
    me "原来你从慎太郎君那里借了漫画啊。"
    hide saburo with dissolve
    show saburo 18 at top with dissolve
    saburo "是那种内容很变态的漫画哟~。\n[player_surname]如果感兴趣的话，之后给你看看。"
    show saburo 14 with dissolve
    extend "\n是两个男人相爱的故事诶！！\n真————的是太扯了！"
    me "那，你刚才看得那么入迷的漫画就是？"
    show saburo 3 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    saburo "才、才不是啦！！！\n谁看入迷了啊！！！"
    show saburo 16 with dissolve
    extend "\n只是上学路上突然想起这本漫画，随便翻了两页而已……。"
    "Bingo！就是那种小黄书！！"
    extend "\n但是，没想到是BL漫画……真是出乎预料。"
    me "诶~能让人无视红绿灯的『随便翻翻』啊。"
    extend "\n啊！所以，你是被BL情节吸引住了，\n所以即便看到女孩子，也没什么反应的吧！！"
    "我一边坏笑着一边调戏着三朗。"
    show saburo 12 with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    saburo "什……！！？？\n怎么可能啊！！！！"
    extend "\n比起男人，我肯定更喜欢女人啊，这还用说吗！！！"
    me "嗯~~~~~。"
    show saburo 8 with dissolve
    saburo "唔……看来你不信我啊……。"
    extend "\n行啊，既然这样，我就证明给你看！！"
    play sound "fx/running.ogg"
    hide saburo with dissolve
    "这么说着，三朗便冲进了女学生中。"
    window hide
    show saburo 10 at top with dissolve
    window show
    saburo "各位小姐，那边的可爱小姐姐们！\n是御咲女子学园的学生们吧？"
    extend "\n我是御咲学园的，如果方便的话\n放学后要不要一起去喝杯茶呀？"
    window hide
    hide saburo with dissolve
    window show
    play sound "fx/cute3.ogg"
    girl1 "诶？你是御咲学园的？"
    extend "\n但我听说，那个学校里满地都是基佬情侣啊……。"
    play sound "fx/cute2.ogg"
    girl2 "诶~是那样吗！？"
    extend "\n那么，我们倒是有好多问题想问你呢！"
    play sound "fx/cute.ogg"
    girl3 "御咲学园里真的有这么猛的BL风暴吗？"
    extend "\n耽美世界是什么样的？你是攻？还是受？"
    play sound "fx/boing.ogg"
    girl2 "硬要说的话，感觉应该是受吧。"
    extend "\n但也可能是废柴攻吧？"
    play sound "fx/ding.ogg"
    show cg dark at center
    show saburo 21 at top with Dissolve(0.2)
    saburo "……。"
    show bg sky
    "被一群叽叽喳喳兴奋不已的女学生包围着，三朗只能呆呆地站在原地。"
    me "小三朗，你就老实回来吧。"
    hide cg with Dissolve(0.3)
    hide saburo with Dissolve(0.3)
    play sound "fx/shock.ogg"
    saburo "呜哇啊啊啊啊！！！！！\n不管走到哪里，全是Gay和Homo的话题啊啊啊啊啊！！！！"
    extend "\n我是不会承认这种事的啊啊啊啊啊！！！"
    play sound "fx/running.ogg"
    window hide
    hide bg with dissolve
    show bg school_route at center with dissolve
    window show
    "真可谓，悲也。"
    "我追赶着一溜烟逃跑的三朗，一起向着学校奔去。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label day2_2:
    pause 0.4
    show bg school_building_morning at center with dissolve
    play sound "fx/chime.ogg"
    pause 0.4
    play music "going_to_school.ogg"
    window show
    "上午的课很快结束了。"
    extend "\n嗯~。明明好不容易成了初中生，课程太短了，感觉有些意犹未尽啊。"
    show bg classroom with Dissolve(0.8)
    "大部分同学都回去了，只有执行委员们留了下来，聚在一起。"
    window hide
    show tomo 1 at topleft with dissolve
    window show
    tomo "哎呀，一天只上四节课的话，真是一眨眼就过去了啊~。"
    show tomo 24 with dissolve
    extend "\n真好啊~这种解放感！真是太棒了！"
    show saburo 2 at topright with dissolve
    saburo "我懂我懂！\n这感觉跟考试前那种缩短课时完全不一样啊~！"
    show saburo 17 with dissolve
    extend "\n因为现在完~全不用考虑学习的事嘛！"
    show saburo 7 with dissolve
    extend "\n要是能一直维持这种状态就好了呢~。"
    hide tomo with dissolve
    show sintarou 10 at topleft with dissolve
    sintarou "就是说啊~考试前的放学时间反而让人坐立不安呢。"
    show sintarou 16 with dissolve
    extend "\n一个人待着的时间又多，越想越容易把自己逼到死胡同里，\n好难受哦。"
    hide saburo with dissolve
    show sakuya 9 at topright with dissolve
    sakuya "说到底，\n学校学的这些东西，将来也没用啊！"
    show sakuya 8 with dissolve
    extend "\n特别是历史和古文！！根本没必要学嘛。\n真烦人。"
    hide sintarou with dissolve
    show tomo 26 at topleft with dissolve
    tomo "我同意技安说的！那玩意儿学了有什么用嘛！！"
    show tomo 27 with dissolve
    extend "\n教育部的那些老头老太太们,\n肯定是为了让我们受罪，\n才特意出那种难懂的题目吧。"
    hide sakuya with dissolve
    show saburo 25 at topright with dissolve
    saburo "唉~。\n真想快点变成自由的大人啊~。"
    hide tomo with dissolve
    show sintarou 17 at topleft with dissolve
    sintarou "我已经受够了被R-18束缚的生活啊……。"
    hide saburo with dissolve
    hide sintarou with dissolve
    "啊哈哈哈。我学生时代也这么想过。"
    "但是啊，年轻人们……等变成了大人，\n才会切身感受到，那些课程都会成为人生的养分啊~。"
    extend "\n等成了大人，想复习学生时代的课程可是很难的，\n所以，不趁现在好好学习掌握知识的话，以后可是会很困扰的哦~！！"
    "……这种话，你们现在肯定听不懂吧~。"
    window hide
    show tubasa 6 at top with dissolve
    window show
    tubasa "唉……虽然我有在认真听讲，\n也觉得自己有好好复习备考，"
    show tubasa 1 with dissolve
    extend "\n但为什么考试成绩总是提不上去呢……。"
    show sinobu 7 at topleft with dissolve
    sinobu "可能是归纳总结得不好吧……？"
    show sora 5 at topright with dissolve
    sora "如果在课本上做的标记太多，\n之后回顾的时候，就搞不清哪里是重点了。"
    show sora 34 with dissolve
    extend "\n根据重要程度的不同，改变做标记的方式也许会比较好！"
    hide sinobu with dissolve
    show tuki 5 at topleft with dissolve
    tuki "还有，不只要吸收知识，还要把学到的东西运用出来。"
    show tuki 4 with dissolve
    extend "\n这种练习，找个人互相出题考对方会很有效果。"
    show tuki 22 with dissolve
    extend "\n即使积累了知识，如果只是藏在肚子里，也不会知道学的怎么样的。\n学到的知识不应用的话就没有意义了。"
    show tubasa 7 with dissolve
    tubasa "呜呜……你说得对。"
    show tubasa 19 with dissolve
    extend "\n我上次考试把考试范围搞错了，\n结果考得很差……。"
    show sora 9 with dissolve
    sora "那、那还真是个严重的失误呢……。"
    hide tubasa with dissolve
    hide sora with dissolve
    hide tuki with dissolve
    "这样看来，学生也挺不容易的。"
    extend "\n每天被学习和社团活动追着跑，事情怎么做都做不完。"
    extend "\n不过从某种意义上来说，这也算是挺幸福的。"
    window hide
    show tomo 21 at top with dissolve
    window show
    tomo "啊，都这个时候啦！"
    show tomo 1 with dissolve
    extend "\n那就各自分组，开始工作吧——。"
    show tomo 12 with dissolve
    extend "\n今天没有时间限制，自由发挥就好——。"
    "喂喂，和昨天比起来，今天的安排还真是随便啊，委员长大人……。"
    hide tomo with dissolve
    "那么，今天去帮助哪个小组呢？"
    window hide
    show 班選択 choose_group_message at center with dissolve
    return

label day2_design:
    hide 班選択 with dissolve
    window show
    "去『服装组』看看吧！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "quiet_lunch.ogg"
    show tomo 1 at topleft with dissolve
    window show
    tomo "那么，[player_name]君，快收拾东西！"
    extend "\n小慎准备好了吗~？"
    show sintarou 1 at topright with dissolve
    sintarou "当然OK！"
    me "诶诶诶诶！？\n要、要回去了？"
    extend "委员的工作呢？"
    show tomo 2 with dissolve
    tomo "当然要做啦！"
    show sintarou 13 with dissolve
    sintarou "我们接下来就要去实地采购了哦。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    show bg shoe_locker with dissolve
    pause 0.5
    show bg school_route with dissolve
    pause 0.5
    show bg misaki_station with Dissolve(2.0)
    window show
    "我跟着友和慎太郎来到了御咲站。"
    me "喂喂，你们到底打算去哪啊？"
    window hide
    show sintarou 8 at topright with dissolve
    window show
    sintarou "毕竟像这种乡下小镇，\n东西都不太齐全嘛！"
    show sintarou 4 with dissolve
    extend "\n所以咱想去梅咲那边看看~。"
    show tomo 10 at topleft with dissolve
    tomo "那边是大城市，应该有很多好东西吧！"
    me "梅咲啊~……\n有公司的人在啊……。"
    show sintarou 15 with dissolve
    sintarou "公司？什么意思？"
    me "啊，不，是因为那里到处都是上班族，\n我这个小孩子在那里会紧张啊~！"
    show sintarou 9 with dissolve
    sintarou "嗯~？好可疑……"
    extend "你这家伙，莫非是在隐瞒什么吧？"
    "（咯噔！）"
    show tomo 25 with dissolve
    tomo "啊，我知道了！"
    extend "\n[player_name]君在和梅咲哪个上班族谈恋爱吧，绝对是！"
    show sintarou 6 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    sintarou "什么！！"
    extend "\n那可务必要让我们拜见一下啊！！"
    me "不、不是啦~！！！！"
    show sintarou 18 with dissolve
    sintarou "真是的~不用这么害羞嘛。"
    show tomo 4 with dissolve
    tomo "有什么关系嘛！介绍给我们吧~。"
    extend "\n我们会帮你保密的！"
    show sintarou 12 with dissolve
    sintarou "[player_name]君挺厉害的嘛！"
    extend "\n看起来这么单纯，结果居然在和大人交往什么的。"
    me "绝对不是——！！！"
    play sound "fx/dash.ogg"
    $ renpy.transition(Quake(0, 60, 0.15, 0.1), layer='master')
    extend "\n我感兴趣的，只有像你们这么可爱的少年啊！！！"
    stop music fadeout 0.5
    play sound "fx/ding.ogg"
    show bg dark
    show tomo 18
    show sintarou 14 with dissolve
    "……"
    play music "discovery.ogg"
    extend "\n诶……我、刚刚、说了什么……？"
    "等到我反应过来的时候，已经晚了。"
    extend "\n友和慎太郎盯着我，一言不发，愣在原地。"
    extend "\n甚至连周围的人，都用那种看可疑分子的眼光看着我。"
    stop sound fadeout 0.5
    window hide
    hide sintarou with dissolve
    hide tomo with dissolve
    hide bg with dissolve
    stop music fadeout 0.5
    show bg train_interior at center with dissolve
    play sound "train.ogg"
    show tomo 21 at topleft with dissolve
    window show
    tomo "啊，还有个空座位。"
    extend "\n[player_name]君，你坐吧。"
    me "诶？我不用了，"
    show sintarou 1 at topright with dissolve
    sintarou "不不~\n毕竟我们之中，精神上最『疲劳』的就是\n[player_name]酱了嘛，"
    extend "\n请坐。"
    me "呜……"
    hide sintarou with dissolve
    hide tomo with dissolve
    show bg train_interior_seat with dissolve
    "我无言以对，\n只能坐下了。"
    "就算他们再怎么早熟，我刚才的那句话果然还是太吓人了吧……。"
    "我感到一阵不安，抬起了一直低着的头，结果……"
    stop sound fadeout 0.5
    extend "\n映入眼帘的，是抓着吊环站立着的友和慎太郎的——"
    window hide
    play sound "fx/sparkle.ogg"
    show cg c9 at center with Radial(0.5)
    window show
    extend "裆、裆部……！！！"
    play music "bwv147.ogg"
    "神啊……"
    extend "这就是，世人仰望的喜悦啊——！！！"
    "啊……这飘渺的香味是……。"
    extend "\n受、受不……了了……！！"
    extend "\n不行……视线根本无法移开……。"
    "幸运的是，似乎没有谁注意到我下流的念头。"
    "为了不让周围的人察觉到我那青春期热血贲张的邪念，我极力让自己举止自然，"
    extend "\n在去梅咲的整段路程里，我都沉浸在幸福之中。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    hide cg with dissolve
    hide bg with dissolve
    stop music fadeout 0.5
    show bg umesaki at center with Radial(1.0)
    pause 0.5
    play music "umesaki.ogg"
    window show
    "走出梅咲站，映入眼帘的就是御咲所没有的高楼群。"
    window hide
    show bg umesaki_station_front with dissolve
    show sintarou 8 at topright with dissolve
    window show
    sintarou "哎呀~果然这里是大城市呢。"
    show tomo 10 at topleft with dissolve
    tomo "来到这种地方，总让人感觉很兴奋呢~。"
    extend "\n真羡慕住在这一带的人啊。"
    me "是吗~？\n我的话，如果要住，还是更喜欢像御咲那样沉稳安静的小镇呢。"
    extend "\n这种大城市人口多，车辆也多，\n吵吵闹闹的，一点都不安静。"
    show tomo 27 with dissolve
    tomo "诶~？[player_name]君这话就像大叔说的一样！"
    play sound "fx/boing.ogg"
    me "太失礼了！我也才25岁啊！！"
    show tomo 21
    show sintarou 14 with dissolve
    tomo_and_shin "哈？"
    me "不、不是，是那个，我是在说公司认识的一个人，才25岁，"
    extend "\n他当时就是这么对我说的啦~！"
    show sintarou 6 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    sintarou "噢噢噢！！！\n原来你真的谈恋爱了！！！"
    show sintarou 7 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    extend "\n快快快！！快跟我们详细说说！！！"
    show tomo 13 with dissolve
    tomo "有照片吗！？"
    extend "让我看看！！！"
    play sound "fx/explosion2.ogg"
    me "呜哇啊啊啊！！！不是的不是的！！"
    extend "\n都说了不是那样啊！！！！"
    "还是老样子，总被这两个人折腾得够呛……。"
    "我那因一时冲动而发热的大脑，现在一下子冷却了下来，突然想起了一件事。"
    me "对了。这也是那个人说过的，"
    extend "\n这一带治安不太好，要小心哦。"
    extend "\n尤其是像我们这样，既弱小又身怀巨款的小孩子，\n特别容易成为被抢劫的目标。"
    show tomo 2 with dissolve
    tomo "没问题啦！"
    extend "\n就算真的有，只要全力逃跑就冇问题啦！"
    show sintarou 2 with dissolve
    sintarou "而且，现在才刚过中午嘛~。"
    extend "\n人也很多，没事的啦~。"
    me "嗯……说的也是。"
    "天还这么亮，可能是我想太多了吧。"
    me "嗯，那我们就出发吧。"
    "我们走向附近的购物中心。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    hide bg with dissolve
    pause 0.3
    play sound "fx/crowd_noise.ogg"
    show bg shopping_mall_exterior at center with Radial(1.5)
    pause 0.5
    window show
    "走进购物中心，虽然是工作日的白天，但顾客依然很多。\n这里十分热闹，充满了活力。"
    window hide
    play sound "fx/crowd_noise.ogg"
    show bg shopping_mall_interior with Dissolve(2.0)
    show tomo 13 at topleft with dissolve
    window show
    tomo "哇哦~！情绪高涨~！！"
    show sintarou 8 at topright with dissolve
    sintarou "就是说啊！！好大啊~！"
    extend "\n反正还有时间，\n难得来一趟，等会儿我们顺便逛逛街吧！"
    show tomo 4 with dissolve
    tomo "赞成~！"
    extend "\n毕竟很少有机会能来梅咲，\n今天就好好享受吧♪"
    "虽然平时很稳重，但这种时候还是挺像小孩子的嘛。"
    "我不禁嘴角上扬。"
    me "那我们就速战速决，赶紧把工作搞定吧！"
    extend "\n去服装店，还有饰品店看看吧！"
    show cg remarkable at center
    play sound "fx/tadaa.ogg"
    show tomo 13
    show sintarou 7 with dissolve
    "友＆慎太郎" "好！！"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    hide bg with dissolve
    hide cg with dissolve
    stop music fadeout 1.0
    show bg shopping_mall at center with Dissolve(1.0)
    play music "umesaki2.ogg"
    show tomo 1 at topleft with dissolve
    window show
    tomo "我觉得小慎很适合穿这种休闲风的衣服~！"
    extend "\n你看你看。"
    show sintarou 1 at topright with dissolve
    sintarou "是——吗——？"
    extend "\n还不错呢~。"
    show sintarou 2 with dissolve
    extend "\n反倒是友亲，我觉得穿这个会很适合！\n啊，不过这种比较清纯的风格也挺适合你的~！"
    show tomo 24 with dissolve
    tomo "真的吗——！"
    extend "\n嗯嗯。下次挑战一下吧。"
    "友和慎太郎几乎都忘记了工作，\n在全身镜前拿着便服在身上比划，兴致勃勃地聊着。"
    "如果我还是大人的话，\n这样的衣服就可以直接买来送他们俩了……！"
    show tomo 28 with dissolve
    $ renpy.transition(Quake(30, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    tomo "……好贵。"
    show sintarou 17 with dissolve
    sintarou "光是……这件衬衫就一万日元啊……。"
    play sound "fx/boing.ogg"
    "什么！！？"
    extend "这可吓死人了！！"
    extend "\n现在的年轻人的衣服居然这么贵吗！"
    "一件衬衫就要花一万块，连我这个社会人都有点吃不消了。"
    extend "\n反过来说，幸好现在的我是个小孩……。"
    me "这、这毕竟是城市里的店嘛……"
    extend "\n稍微贵一点也是没办法的事……吧。"
    show tomo 26 with dissolve
    tomo "嗯……这样啊。"
    show sintarou 14 with dissolve
    sintarou "对了。\n顺便问问，服装费最多可以花多少？"
    show tomo 9 with dissolve
    tomo "五万日元……。"
    show sintarou 16 with dissolve
    sintarou "天、天呐……。"
    extend "嗯……。"
    show sintarou 19 with dissolve
    extend "\n既然这样，那我们就把这商场里的店铺全部逛一遍，\n努力找到便宜一点的吧！"
    show tomo 16 with dissolve
    tomo "了解！"
    me "要是在御咲周围的话，\n说不定能找到更便宜一些的店……。"
    show tomo 9
    show sintarou 16 with dissolve
    tomo_and_shin "不要那么说嘛……。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    hide bg with dissolve
    show bg shopping_mall_interior at center with Dissolve(1.5)
    show tomo 26 at topleft with dissolve
    window show
    tomo "大略逛了一圈，感觉最便宜也要四千日元啊……。"
    show sintarou 2 at topright with dissolve
    sintarou "看样子这家店的价位是最低的了，\n那就这家吧！"
    me "嗯？"
    extend "\n喂——！这边有均一价一千日元的区域哦。"
    show tomo 4 with dissolve
    tomo "干得漂亮！！[player_name]君！"
    show sintarou 8 with dissolve
    sintarou "噢~！"
    extend "\n虽然稍微有点缺乏视觉冲击力，但要是再搭配些其他服装的话，\n看起来应该会很不错！"
    show tomo 8 with dissolve
    tomo "嗯，我们两个班总共有72个人……。\n那个……那个……。"
    me "那样就不太够了。"
    extend "\n不过，没必要连后厨的衣服都准备，\n并且让两个轮班的人共用一套的话，只需要准备一半的数量就可以了吧。"
    show tomo 12 with dissolve
    tomo "话是这么说啦。"
    extend "\n但是难得有这个机会，我想让大家都穿上一样的衣服。"
    show tomo 1 with dissolve
    tomo "这样会感觉比较团结，而且还能作为实物留下来，"
    extend "\n最重要的是，这可以成为印象深刻的回忆，"
    show tomo 4 with dissolve
    extend "那样的话，我想大家一定会很开心的。"
    show sintarou 4 with dissolve
    sintarou "嗯嗯。"
    extend "\n如果大家都能穿一样的衣服的话，\n日后回忆起来，就会觉得『一班也好，二班也好，都很不错啊』。"
    show sintarou 20 with dissolve
    sintarou "而且，只有后厨的同学没有衣服穿的话，\n也有点太可怜了嘛。"
    "原来如此。"
    extend "\n睹物怀旧，也是触发回忆的契机啊。"
    me "……嗯，我知道了！"
    extend "\n作为二年一、二班的御咲祭执行委员的服装组的一员！！"
    extend "\n我会想办法让大家都能穿上统一的制服的！"
    show tomo 1
    show sintarou 8 with dissolve
    tomo_and_shin "嗯！"
    me "那么，接下来到外面去找找看吧。"
    extend "\n看样子这里已经没有更好的店了。"
    "我们离开了购物中心。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    hide bg with dissolve
    show bg downtown with Dissolve(1.0)
    window show
    "走了一阵子之后，慎太郎指了指什么东西。"
    window hide
    show sintarou 2 at topright with dissolve
    window show
    sintarou "呐呐！\n那里好像很不错啊？"
    show tomo 1 at topleft with dissolve
    tomo "真的！"
    extend "\n上面挂着好大的『500日元』的牌子！"
    extend "\n那里的话，应该能在预算内搞定全员的服装！"
    me "好！就去那家看看吧。"
    window hide
    hide sintarou with dissolve
    hide tomo with dissolve
    hide bg with dissolve
    show bg clothing_store with Dissolve(1.0)
    window show
    "店内的商品排列得毫无章法，完全没有统一感。"
    extend "\n但是，每一件单品的品味都不错。"
    extend "\n我有一种预感，在这家店里说不定能淘到什么宝贝。"
    window hide
    show sintarou 6 at topright with dissolve
    window show
    sintarou "呐呐！这个不挺好的吗？"
    "慎太郎高声一喊。他举起的，是一条没有任何花纹的、简约的红色领带。"
    show sintarou 4 with dissolve
    sintarou "现在也顾不上什么时尚啊华丽啊之类的了。"
    extend "\n简单就是最好的！"
    show tomo 4 at topleft with dissolve
    tomo "是啊。"
    extend "\n起初我太在意其他班级，只想着要展示『与众不同』。"
    extend "\n但是，重要的不是把外表弄得光鲜亮丽给其他人看，"
    me "而是我们，不对，是班上的大家，\n要如何把这次御咲祭变成美好的回忆留存下来，"
    extend "对吧？"
    show sintarou 1 with dissolve
    sintarou "嗯嗯。"
    show tomo 1 with dissolve
    tomo "是啊。"
    me "那么，就这么决定了！"
    extend "\n那么……。"
    hide sintarou with dissolve
    hide tomo with dissolve
    return

label day2_layout:
    hide 班選択 with dissolve
    window show
    "去『布置组』看看吧！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "quiet_lunch.ogg"
    show sinobu 26 at topleft with dissolve
    window show
    sinobu "那么，今天就去咖啡店实地考察一下吧。"
    show tubasa 13 at topright with dissolve
    tubasa "已经决定好去哪家店了吗？"
    show sinobu 12 with dissolve
    sinobu "嗯。"
    extend "\n昨天慎太郎给我推荐了一家不错的店，\n连地图都帮我准备好了，应该没问题。"
    me "让我看看地图。"
    extend "\n原来如此，是在车站的另一头啊。那一带我没怎么去过呢。"
    extend "\n『Mädchen Café』……还真是个少见的店名啊。"
    show tubasa 5 with dissolve
    tubasa "不、不过，总觉得名字听起来很时髦呢。"
    extend "\n究竟是什么样的地方呢……"
    show sinobu 23 with dissolve
    sinobu "慎太郎说『要做参考的话非这里莫属』，把那里夸上天了，我想应该是个不错的地方吧。"
    extend "\n那么，出发吧。"
    window hide
    hide sinobu with dissolve
    hide tubasa with dissolve
    stop music fadeout 2.0
    show bg school_route with dissolve
    pause 0.5
    show bg shopping_street with dissolve
    pause 0.5
    play music "fx/tsubame.ogg"
    show bg downtown with Dissolve(2.0)
    window show
    "我们跟着地图，来到了『Mädchen Café』的附近。"
    window hide
    show tubasa 10 at topright with dissolve
    window show
    tubasa "这一带的街景，看着很陌生呢……。"
    show sinobu 17 at topleft with dissolve
    sinobu "嗯。"
    extend "\n因为从车站下车后，我们一般只往御咲学园那个方向走。"
    me "看地图的话，确实是……这附近没错。"
    extend "\n但是，附近没有看到像咖啡店的建筑啊~。"
    "我环顾四周，只看到一排排狭窄的小楼。"
    show tubasa 2 with dissolve
    tubasa "要是早点问清楚店铺的外观就好了呢。"
    show sinobu 17 with dissolve
    sinobu "嗯……"
    show sinobu 9 with dissolve
    extend "啊，看那个。"
    "顺着忍手指的方向看去，只见大楼上挂着一块招牌。"
    show sinobu 2 with dissolve
    sinobu "『Mädchen Café』好像在那栋大楼的四楼。"
    show tubasa 19 with dissolve
    tubasa "真的诶。"
    extend "\n咦……可是，开在这种大楼里……？"
    "那栋大楼的外观实在令人不敢恭维。"
    me "看来，好像和我们想象的咖啡厅……\n很不一样呢……。"
    show sinobu 7 with dissolve
    sinobu "不过，肯定是这里没错了。"
    extend "\n总之先去看看吧。"
    show tubasa 3 with dissolve
    tubasa "这、这样真的没问题吗？"
    extend "\n万一，里面有可怕的人的话……。"
    me "没事的，翼君。"
    extend "\n不能以貌取人嘛。"
    extend "\n这种地方的居酒屋，出乎意料地是家不错的店呢。"
    show tubasa 21 with dissolve
    tubasa "居、居酒屋？"
    extend "\n你去过那种地方吗？"
    me "啊……被父亲带去吃过饭！"
    extend "\n毕竟那种店里，也是有卖软饮料的嘛！"
    extend "\n总、总之，先进去看看吧。"
    show sinobu 6 with dissolve
    play sound "fx/eureka.ogg"
    sinobu "万一有情况，就干掉他们。"
    show tubasa 7 with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tubasa "干、干掉什么啊啊啊！"
    extend "\n噫噫噫好可怕啊——。"
    me "都说没事啦！"
    extend "\n好，走吧。"
    hide sinobu with dissolve
    hide tubasa with dissolve
    play sound "fx/running.ogg"
    hide bg with dissolve
    "我拖着瑟瑟发抖的翼走进大楼，\n乘电梯上了四楼。"
    window hide
    play music "haunted_music_room.ogg"
    show bg meffen_cafe_hallway at center with Radial(1.0)
    pause 0.4
    window show
    "电梯门一开，映入眼帘的是一排排整齐的房门。"
    extend "\n这里难道是把酒店改建后使用的吗？"
    window hide
    show sinobu 5 at topleft with dissolve
    window show
    sinobu "『Mädchen Café』好像是最里面的那个房间。"
    show tubasa 8 at topright with dissolve
    tubasa "真、真的要去吗？！"
    show tubasa 7 with dissolve
    extend "\n算、算了吧~。"
    show tubasa 8 with dissolve
    extend "\n里面要是有恐怖的人该怎么办啊啊啊！"
    show sinobu 25 with dissolve
    sinobu "虽说如此，但总不能就这样回去吧。"
    play sound "fx/eureka.ogg"
    extend "\n没事的，如果有情况的话我会把他们打倒的。"
    show tubasa 7 with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tubasa "请不要说得那么轻巧啊啊啊啊。"
    "翼相当害怕，而忍则相当有攻击性。"
    extend "\n看来两人都是第一次来这种地方，所以都在警戒着吧。"
    extend "\n没办法了……这种时候，就由我来打头阵吧。"
    me "你们俩就在这里等着。"
    extend "\n我去看看情况。"
    show tubasa 17 with dissolve
    tubasa "但、但是，这样[player_name]君会有危险的！"
    show sinobu 6 with dissolve
    sinobu "就是啊。"
    extend "\n你能打倒他们吗？"
    me "哼哼！没问题的。"
    extend "\n这种时候，就该交给大人来处理♪"
    show tubasa 22
    show sinobu 27 with dissolve
    "翼＆忍" "……。"
    "我留下满脸讶异的两人，"
    hide sinobu with dissolve
    hide tubasa with dissolve
    play sound "fx/running.ogg"
    show bg dark with dissolve
    "径直走向里面的那扇门。"
    "哈哈。"
    extend "\n虽然从外观来看破烂不堪，但这毕竟是慎太郎介绍的店……。"
    extend "\n怎么可能是那种危险的地方嘛……！！"
    extend "\n肯定没有可怕的人……"
    extend "对吧——慎酱！！！"
    "要开喽……一、二、三！！"
    stop music fadeout 0.5
    play sound "fx/door_open.ogg"
    show bg remarkable with dissolve
    "（咔嚓！！）"
    "在打开门的瞬间，闯入我眼帘的竟然是——"
    window hide
    play music "maid_cafe.ogg"
    show bg meffen_cafe with Radial(1.5)
    pause 0.4
    window show
    play sound "fx/sparkle.ogg"
    unknown "欢迎回家，主人！！！"
    "发出这声娇滴滴的高亢欢呼的，是一群身穿女仆装的女孩子们。"
    play sound "fx/cute.ogg"
    me "诶？！？"
    "我不由得发出了惊慌失措的声音。"
    window hide
    show sinobu 25 at topleft with dissolve
    window show
    sinobu "[player_surname]君……？"
    show tubasa 21 at topright with dissolve
    tubasa "这、这到底是怎么回……。"
    "说起来……『Mädchen』在德语中的意思是『女仆』。"
    extend "\n也就是说，『Mädchen Café』是……"
    hide sinobu with dissolve
    hide tubasa with dissolve
    $ renpy.transition(Quake(0, 100, 0.1, 0.065), layer='master')
    play sound "fx/boing.ogg"
    extend "\n女仆咖啡厅啊啊啊！？？！"
    window hide
    window show
    clerk1 "哎呀，这身校服！是御咲学园的学生吧。"
    extend "\n稍微等一下哦！"
    clerk1 "店长~！！御咲学园的学生来了！"
    "女仆向店里的深处喊道。"
    manager "哦！终于来了吗~。"
    extend "\n可让我好等啊。"
    "紧接着，一位身穿管家服、看起来40多岁的男性出现了。"
    manager "呀呀，我都听慎太郎君说过了哦。"
    extend "\n你们打算在学园祭的时候开咖啡厅？"
    extend "\n不嫌弃敝店的话，就请尽情参观吧"
    me "啊，好的。那就拜托您了。"
    "我完全跟不上事态的发展，也没搞懂到底怎么回事，只能机械地随口应答。"
    manager "那么，今天要做一日店员的，是后面的两个人吗？"
    extend "\n我听说是——一个人考察我们店的布置和装潢，\n另外两个人要跟女仆们实际学习接待服务来着？"
    me "诶，啊啊，好的。那就拜托您了。"
    "我完全跟不上事态的发展，也没搞懂到底怎么回事，只能机械地随口应答。"
    clerk1 "那么，两位客人。"
    extend "\n请来这边换衣服吧♪"
    stop music fadeout 0.5
    show cg dark at center
    play sound "fx/triangle.ogg"
    show tubasa 17 at topright
    show sinobu 28 at topleft with dissolve
    "翼＆忍" "诶……？"
    hide sinobu with dissolve
    hide tubasa with dissolve
    hide cg with dissolve
    hide bg with dissolve
    "……"
    window hide
    show bg meffen_cafe at center with dissolve
    play music "quiet_lunch.ogg"
    window show
    "再次向店长打听后得知，他似乎和慎太郎关系很好。"
    extend "\n这次，听说我们在学园祭打算开咖啡店，\n他就主动提议如果不介意的话，可以来店里参考看看。"
    me "原来是这样啊。"
    extend "\n特意给您添麻烦，真是谢谢了。"
    manager "哪里哪里！"
    extend "\n我才应该这么说呢，因为我一直承蒙慎太郎君的关照啊。"
    extend "\n我也就只有这种时候能派上点用场，\n所以就厚着脸皮来多管闲事啦。"
    me "但是，真的没问题吗？"
    extend "\n初中生是不允许打工的吧……。"
    manager "这点没有问题！"
    extend "已经得到上面的许可了，\n算是『社会职业体验周』的一部分哦！"
    me "原来如此……。"
    "我们聊得正起劲时，"
    play sound "fx/cute.ogg"
    clerk2 "呀啊——！！两个人，都超级可爱啊~！"
    play sound "fx/cute2.ogg"
    clerk3 "小正太萌翻了呢~！受不了了啊！"
    manager "哦。"
    extend "\n看来是时候了。"
    "（心砰砰跳……）"
    "帘子的后面，站着打扮成女仆模样的两人。"
    stop music fadeout 0.5
    clerk1 "那么，现在开始介绍！"
    "帘子缓缓拉开……。"
    window hide
    show cg c33 1 at center with Radial(0.5)
    play sound "fx/sparkle.ogg"
    play music "lively_boys.ogg"
    window show
    manager "哦哦哦哦！！！"
    extend "\n太、太棒了！！！！"
    extend "\nNice正太！！！！"
    extend "Nice女装！！！！"
    sinobu "……呜……慎太郎那个混蛋……。"
    extend "\n我绝对要……宰了他……！！！"
    tubasa "这、这身打扮……羞死人了。"
    me "你、你们两个！实在是太可爱了！！！"
    extend "\n简直是最棒了！！！"
    extend "\n店长，相机！"
    extend "\n快拍下来吧！！"
    manager "当然啦！！！"
    extend "\n来来来，两位！看这边~。"
    extend "\n茄——子！"
    clerk2 "呀啊！！好萌~！！！"
    clerk3 "小正太，哈啊、哈啊！！！"
    sinobu "[player_surname]……咱们换换。"
    tubasa "我、我也想换。"
    extend "\n说到底，事情为什么会变成这样啊！"
    manager "想要学习待客之道，最好的办法就是在实际的咖啡店体验一番吧？"
    extend "\n要好好学习，之后再去教给班上的同学们哦。"
    window hide
    hide cg with dissolve
    window show
    me "……店长，原来你也喜欢这种事情吗？"
    manager "啊啊！倒不如说，这才是我的最爱！！"
    extend "\n但是，因为实际不能雇佣少年去工作，"
    extend "\n而市场需求量又大，所以只能勉为其难地让女孩子来了啊。"
    extend "\n不过，那些孩子们仔细看的话，也很可爱就是了。"
    me "男女通吃吗~。"
    extend "\n真有你的，店长。"
    manager "哎呀，如果不变得圆滑一点，\n可是没法在这个世道上混下去的啊。"
    "店长叹了一口气。"
    sinobu "你们两个，别在那里一脸悠哉地讨论什么处世之道啊……。"
    tubasa "是啊！也考虑一下我们的心情啊！"
    play sound "fx/sparkle.ogg"
    me "啊啊……真是可爱啊，你们两个！\n不管说什么都很可爱……"
    extend "不对，就算什么都不做，或者无论做什么，总之就是最棒的啊~！！！！"
    manager "女仆们。"
    extend "\n今天一天之内，\n要把这几个孩子，给我教育成出色的正太女仆！"
    play sound "fx/cute2.ogg"
    clerk "了解！！"
    "于是，御咲祭前的准备工作就这样开始了。"
    "虽然忍和翼看起来还是相当抗拒，"
    extend "\n但不知是因为明白了反抗也是徒劳的现状还是怎么的，\n慢慢地就顺从了。"
    window hide
    show cg c33 2 at center with Radial(0.5)
    window show
    clerk2 "忍君翼君，笑容要更多一点~！"
    tubasa_and_sinobu "……(强颜欢笑)。"
    clerk1 "嗯，做得不错。"
    extend "\n那么再来一次，从问候开始。"
    extend "\n来，预备——起！"
    show cg c33 1 with dissolve
    tubasa_and_sinobu "欢、欢迎回来，主人。"
    clerk1 "不行！声音再大一点！！"
    clerk2 "要将少年那美好的声音传达给主人啊！"
    extend "\n就像过去的阉伶那样！\n（注：『阉伶』指在童年时接受阉割手术的男性歌手，去势的目的是为了保持童声。）"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    show cg c33 2 with dissolve
    tubasa_and_sinobu "欢迎回来，主人！！"
    clerk1 "完美！太棒了！"
    clerk2 "太棒了！"
    window hide
    hide cg with dissolve
    window show
    sinobu "……咕。"
    tubasa "呜呜……。"
    me "你们俩~！"
    extend "\n再对我说一遍嘛~！！"
    window hide
    show cg c33 3 at center with FadeBlack(0.5)
    play sound "fx/eureka.ogg"
    window show
    tubasa_and_sinobu "（瞪）"
    me "啊……不是……。"
    extend "\n没、没事……。"
    "但是，那冰冷的视线，也让我欲罢不能啊……！！"
    window hide
    hide cg with dissolve
    hide bg with dissolve
    stop music fadeout 0.5
    show bg meffen_cafe_evening at center with dissolve
    play music "cute_silly.ogg"
    show tubasa 22 at topright
    show sinobu 19 at topleft with dissolve
    window show
    sinobu "……好累。"
    tubasa "我也是……。"
    "结束了女仆们地狱般严酷的特训，\n两人换回了校服。"
    me "辛苦了！"
    extend "\n真的非常努力了呢！这样一来，接待客人方面就没问题了。"
    extend "\n店长说，等会儿会请你们吃蛋糕套餐！"
    show sinobu 5 with dissolve
    sinobu "是吗……"
    extend "\n话说回来，[player_surname]君那边怎么样了？"
    me "啊。"
    extend "\n我跟店长请教了很多， 比如怎样的布局能让店铺显得更美观，\n还有必要的材料啊、菜单的绘制方法之类的。"
    extend "\n为了缓和气氛，BGM最好选择节奏慢一些的。"
    show tubasa 6 with dissolve
    tubasa "这样啊……"
    extend "\n总之今天的工作平安无事地结束了，太好了……。"
    me "哎呀……话说回来，\n刚才穿的女仆装真的很适合你们！"
    hide sinobu with dissolve
    hide tubasa with dissolve
    return

label day2_cooking:
    hide 班選択 with dissolve
    window show
    "要不要去『料理组』玩玩！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "twins_theme.ogg"
    window show
    me "那么，今天要做什么呢？"
    show tuki 9 at topleft with dissolve
    tuki "烹饪室被其他班级使用了，没法在那里做菜。"
    extend "\n所以，今天就在我们家开发新菜品吧。"
    me "哎，真的吗！？"
    extend "\n我也可以去你们的家吗！？"
    show sora 3 at topright with dissolve
    sora "当然可以。"
    extend "\n家里会有点乱，希望你不要太介意。"
    me "怎，怎么会！完全没问题！！！"
    extend "\n只要是男孩子住的地方，无论是什么样的地方都没关系！"
    show tuki 15 with dissolve
    tuki "哈哈哈，你还真是会说些有趣的话啊。"
    extend "\n食材应该已经由佣人买回来了。\n就这样直接过去吧。"
    show sora 14 with dissolve
    sora "明明都说好由我们去买，他们真是的！。\n总是把我们当成小孩子，总是这么爱管闲事。"
    "佣，佣人……？什么啊？"
    extend "\n这个词汇，我只在电视剧和漫画里听过。"
    show tuki 3 with dissolve
    tuki "毕竟他们从我俩小时候就一直照顾着我们。"
    extend "\n对他们来说，我俩还是小孩子吧。"
    extend "\n就连打扫道场，直到最近才肯让我们自己去做。"
    show sora 22 with dissolve
    sora "毕竟，道场是我们使用的，就要我们自己来打扫。"
    extend "\n带着感恩的心打扫，那一天的训练才能够结束。"
    "道场？训练？？"
    extend "\n完全跟不上话题啊。"
    "难道他们家像《难波 1/3》那样，家就是道场吗。"
    show cg school_building_morning at center with dissolve
    "不对，怎么可能有这种事啊。\n啊哈哈哈哈哈哈哈"
    window hide
    hide bg with dissolve
    hide tuki with dissolve
    hide sora with dissolve
    hide cg with dissolve
    window show
    "…"
    window hide
    stop music fadeout 0.5
    show bg akamine_house1 at center with FadeWhite(0.5)
    play sound "fx/impact.ogg"
    pause 0.8
    show bg akamine_house2 with FadeWhite(0.5)
    play sound "fx/impact.ogg"
    pause 0.8
    show bg akamine_house3 with Radial(0.8)
    play sound "fx/impact_japanese.ogg"
    pause 0.8
    window show
    play music "akamine_house.ogg"
    "然而，真的有这种事。"
    "这，这栋房子是怎么回事！"
    extend "\n居然有这么豪华的中庭……。"
    extend "\n就像是接待重要合作伙伴的高级和风餐厅！！"
    show sora 5 at topright with dissolve
    sora "[player_name]君，怎么了？\n你从刚才起就心神不宁的。"
    show tuki 16 at topleft with dissolve
    tuki "没事吧？"
    extend "\n如果这房间住得不舒服的话，我们会为你换一个的。"
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 60, 0.1, 0.06), layer='master')
    me "没，没事！请不必如此！！"
    extend "\n今，今天有幸能被招待到此地，\n真的是我的荣幸……非常感谢。"
    me "不好意思，现在才自我介绍。鄙人[player_surname][player_name]。\n今天请多多关照。"
    extend "\n那个，名片……"
    extend "等下？"
    play sound "fx/cute.ogg"
    $ renpy.transition(Quake(0, 60, 0.1, 0.06), layer='master')
    extend "没有！！在哪！？放到哪去了？"
    show sora 1 with dissolve
    sora "啊哈哈哈。\n[player_name]君，你怎么了？"
    extend "\n你是在模仿什么吗？"
    show tuki 15 with dissolve
    tuki "简直就像哪里新来的员工一样。"
    me "啊，啊哈哈……抱歉抱歉。"
    extend "\n因为我还是第一次来这种豪宅里，所以不自觉就紧张起来了…。"
    show sora 24 with dissolve
    sora "豪宅什么的，太夸张了。"
    extend "\n这里是你的朋友的家，不必客气，当成自己家就好。"
    window hide
    hide tuki with dissolve
    hide sora with dissolve
    play sound "fx/sliding_door.ogg"
    window show
    servant "请恕我打扰了。请用茶。"
    extend "\n[player_surname]君，一直以来月和空都承蒙您照顾。"
    extend "\n今后还请多多关照。"
    me "是，是！！  我，我才该说这些！"
    extend "\n一直以来，无论是眼睛、心灵还是在那方面，都承蒙他们关照了！！"
    servant "……？"
    show sora 1 at topright with dissolve
    sora "对吧？  他就是个有趣的人吧？"
    show tuki 4 at topleft with dissolve
    tuki "时不时就会说出些让人摸不着头脑的话，\n但气氛却会因此变得愉快。"
    servant "哦呵呵呵……是的呢。"
    extend "\n月，空，按你们嘱咐的，厨房现在可以使用了。"
    extend "\n我不在真的没问题吗？"
    show tuki 9 with dissolve
    tuki "啊啊……这可是学校的任务。"
    extend "\n课题就是不依靠家人的帮助，靠自己的力量完成。"
    extend "\n就由我们来完成吧。"
    servant "我明白了。"
    extend "\n如果还有什么问题，请随时叫我。\n那么，我就先告辞了。"
    play sound "fx/sliding_door.ogg"
    "佣人这么说着，便离开了房间。"
    hide tuki with dissolve
    hide sora with dissolve
    window hide
    show tuki 4 at top with dissolve
    window show
    tuki "好了。\n那我们赶紧去厨房制定菜单吧。"
    window hide
    hide tuki with dissolve
    hide sora with dissolve
    hide bg with dissolve
    play sound "fx/sliding_door.ogg"
    show bg akamine_kitchen at center with Radial(0.5)
    window show
    "赤峰家的厨房，与和风的宅邸并不相称，意外地很现代化。"
    show tuki 18 at topleft with dissolve
    tuki "这里是第二厨房。"
    extend "\n在有大量客人来拜访的时候，就用来辅助第一厨房。"
    extend "\n今天可以尽情使用这里，放心吧。"
    show sora 24 at topright with dissolve
    sora "我们平时并没有这么频繁地使用，\n所以没有好好地保养过。"
    extend "\n可能看起来不干净，还请见谅。"
    me "是，是吗……不，已经非常干净了！！"
    hide tuki with dissolve
    hide sora with dissolve
    extend "\n如果这样算脏的话，那我家厨房又算什么……。"
    "诚，诚惶诚恐，赤峰家主人……。"
    extend "\n这么大的房子，厨房却只有这么小。"
    extend "\n落差感好大啊……。"
    window hide
    show tuki 17 at topleft with dissolve
    window show
    tuki "如果我们因为准备菜谱时间拖得太久，或是把厨房弄脏了，\n而影响大家准备晚饭的时间就不好了。"
    show sora 11 at topright with dissolve
    sora "我们就在这间厨房里加油研究吧。"
    "我环视了一圈厨房，发现里头放着食材，还有几本烹饪书籍。"
    extend "\n是佣人准备的吗……。"
    extend "\n能事先计划好需要的东西，让佣人做好周全的准备……\n真不愧是住在这所豪宅里的人，他们真是管理的好手。"
    show sora 3 with dissolve
    sora "那就按照昨天说的，分头干活吧。"
    show tuki 4 with dissolve
    tuki "嗯。"
    "我们就这样分头开始了工作。"
    window hide
    hide tuki with dissolve
    hide sora with dissolve
    hide bg with dissolve
    show bg akamine_kitchen at center with dissolve
    window show
    "我参考烹饪书籍，和月一起做菜。"
    show tuki 8 at top with dissolve
    tuki "唔，照烧三明治，完成了。"
    show tuki 18 with dissolve
    extend "\n味道应该相当不错，[player_surname]愿意尝一下味道嘛？"
    "说着，月把三明治递给了我。"
    "（咽口水）"
    "是男孩子亲手做的……光是这个就已经很美味了！！！"
    hide tuki with dissolve
    "（大口咬）"
    extend "\n（嚼嚼）"
    "诶"
    "骗人的吧……竟然……"
    show cg remarkable at center with Dissolve(0.2)
    play sound "fx/tadaa.ogg"
    me "真，真好吃！！！！！！太好吃了吧！！！！"
    extend "\n面包里夹的照烧猪肉！"
    extend "\n到底用的什么调味料，才能这么好吃啊！？？"
    window hide
    hide cg with dissolve
    show tuki 6 at top with dissolve
    window show
    tuki "只是按照食谱做而已。"
    me "诶！骗人的吧？？"
    extend "\n能，能不能，把那本书给我看看。"
    "嗯……并没有什么特别的调味料。"
    extend "\n那么，就应该是猪肉本身很美味……？"
    me "月，这个，是用的高档的肉吗？"
    show tuki 5 with dissolve
    tuki "是高野黑猪。"
    extend "\n家里的佣人准备的。"
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 60, 0.1, 0.06), layer='master')
    me "高，高高高高野……！？！？"
    "喂喂喂等等！！"
    extend "\n区区一个照烧三明治，竟然用了这么好的肉！！！"
    me "喂，喂喂喂！！\n现在我们只是在做学园祭的菜品啊。"
    extend "\n要是买那种高价的肉，预算可就不够了哦！"
    show tuki 11 with dissolve
    tuki "……啊，是这样啊。"
    "所，所以说有钱人家的少爷真是……。"
    extend "\n不过话说回来，明明听说是要做学园祭的菜，\n却准备了这么贵的肉，佣人也太可怕了吧……。"
    me "算，算了，当天就用便宜的食材吧，\n今天就专心研究料理吧。"
    show tuki 17 with dissolve
    tuki "是啊，就这么办吧。"
    window hide
    hide tuki with dissolve
    show sora 10 at top with dissolve
    window show
    sora "哥哥！[player_name]君，快看快看！！"
    extend "\n我做好好吃的芭菲了哦！"
    "空一边喊着一边飞奔过来，然后把芭菲端了过来……"
    window hide
    play sound "fx/sparkle.ogg"
    show cg c51 at center with Radial(0.5)
    hide tuki
    hide sora
    window show
    me "那，那个，空啊……那个芭菲……。"
    sora "诶嘿嘿。"
    extend "\n把喜欢的点心全部装进去之后，就变成了这个样子了。"
    play sound "fx/ding.ogg"
    "非常……大……。"
    me "等，等等等等等等！！！"
    extend "\n能快乐地研究美食，这种心情非常棒！"
    extend "\n但，但是啊，月也说了，这些美食终究得在学园祭上制作！"
    extend "\n当天可做不了那么大的芭菲啊！！"
    stop sound fadeout 0.5
    hide cg with dissolve
    show sora 33 at top with dissolve
    play sound "fx/boing.ogg"
    sora "啊，是这样吗……。"
    me "总之啊，你们两个都想想接下来的事吧！！"
    extend "\n简单！快速！简易！"
    extend "\n之后为了教会大家做法，\n也为了当天可以制作，不遵守这个规则是行不通的。"
    hide sora with dissolve
    show tuki 17 at topleft with dissolve
    tuki "……确实是，[player_surname]君说的对。"
    extend "\n我们的想法太天真了。"
    show sora 13 at topright with dissolve
    sora "并不是只要我们觉得满意就可以了。"
    extend "\n[player_name]君的话我们记在心上了。再试一次吧。"
    hide tuki with dissolve
    hide sora with dissolve
    "说完，我们回到了各自的位置，重新开始开发。"
    window hide
    hide bg with dissolve
    show bg akamine_house1_evening at center with Dissolve(0.8)
    window show
    "过了几个小时，我们参考料理书，烹调料理，"
    extend "\n然后再以此为基础构思出新的菜单，制作出来，"
    extend "\n三人制作的料理，盛放在桌上。"
    window hide
    show bg akamine_kitchen with dissolve
    show sora 3 at topright with dissolve
    window show
    sora "哥哥做的三明治，看起来好好吃~！"
    show tuki 15 at topleft with dissolve
    tuki "空做的芭菲看起来也很好吃。"
    extend "\n你们做得真好。"
    me "嗯嗯！每个看起来都很不错。"
    extend "\n那么，我们现在开始试吃吧！"
    show sora 1 with dissolve
    sora "嗯！"
    extend "\n在做菜的时候，一直在看着很好吃的料理，\n肚子好饿。"
    extend "\n我开动了！"
    hide sora with dissolve
    hide tuki with dissolve
    "然后，我们开始吃试作品。"
    window hide
    show sora 3 at topright with dissolve
    window show
    sora "嗯，很好吃！"
    show sora 1 with dissolve
    extend "\n哥哥，这个照烧三明治，真的很好吃呢！！"
    show tuki 9 at topleft with dissolve
    tuki "是吗，那太好了。"
    extend "\n当天没法使用这种肉，\n所以我就试着在调味上下功夫。"
    show tuki 1 with dissolve
    extend "\n……嗯？这个汉堡是谁做的？"
    me "啊，是我做的。"
    show sora 26 with dissolve
    sora "哇啊~味道好香啊~。"
    extend "\n我开动了！"
    extend "\n……。"
    show sora 10 with dissolve
    play sound "fx/cute2.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    extend "\n嗯！这个也，非常的好吃！！"
    show tuki 4 with dissolve
    tuki "的确，非常的多汁，肉也很厚实，让人很有饱腹感。"
    extend "\n和那附近的快餐店的东西相比，美味多了。"
    "嘛，嘛，用了那么高级的肉，\n只要不是犯了什么大的错误的话，做出的东西肯定好吃的。"
    extend "\n但是，能这样看到你们两个人吃得这么开心，我非常高兴……。"
    extend "\n你们俩看起来也很好吃的样子啊……。"
    show sora 3 with dissolve
    sora "啊，对了！"
    extend "\n光我们几个人吃的话有点多，\n让妈妈，还有佣人们也尝尝吧。"
    show tuki 18 with dissolve
    tuki "是啊。"
    extend "\n毕竟都花了不少功夫，必须要向他们道谢才行。"
    "养育了这么孝顺的好孩子，父母也会高兴的。"
    extend "\n而且，双胞胎还是两位美男子……。"
    play sound "fx/sparkle.ogg"
    extend "\n赤峰家……太棒了！！"
    window hide
    hide tuki with dissolve
    hide sora with dissolve
    hide bg with dissolve
    show bg akamine_house1_evening at center with Dissolve(0.8)
    window show
    "点到为止地试吃过之后，剩下的就交给佣人们，然后我们就开始收拾了。"
    extend "\n月和我负责洗碗，空负责擦干并放入橱柜。"
    extend "\n佣人又想来给他们两人收拾，"
    extend "可月和空说优先准备其他人的晚饭。\n这次佣人老老实实放弃了。"
    window hide
    stop music fadeout 2.0
    show bg akamine_kitchen with dissolve
    show sora 13 at top with dissolve
    window show
    sora "……嗯，里面有个黑色的……？"
    window hide
    hide sora with dissolve
    hide bg with dissolve
    window show
    "……。"
    show bg remarkable at center with FadeWhite(0.5)
    $ renpy.transition(Quake(0, 100, 0.2, 0.06), layer='master')
    play sound "fx/explosion2.ogg"
    "呀啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！！！！！！！！！"
    "空大声的尖叫响彻整个厨房。"
    play music "emergency.ogg"
    show bg akamine_kitchen with FadeBlack(0.3)
    me "空，空！？"
    show tuki 12 at topleft with dissolve
    tuki "怎么了！？发生什么了！？"
    show sora 16 at topright with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sora "哥，哥哥！！"
    extend "\n碗，碗碗碗柜里有……大蜘蛛啊……！！"
    show sora 8 with dissolve
    extend "\n哇啊，哇啊啊啊啊啊它过来了啊啊啊啊啊！！！！！！！！"
    play sound "fx/running.ogg"
    hide sora with dissolve
    "空完全慌了，到处乱窜。"
    hide tuki with dissolve
    show tuki 12 at top with dissolve
    tuki "空！冷静点！！"
    show tuki 19 with dissolve
    extend "\n可恶的蜘蛛……"
    extend "\n让空遇上这种事情……罪该万死！！！"
    hide tuki with dissolve
    play sound "fx/wind_slash.ogg"
    "月边说边拿起旁边拖把，\n瞄准那个在厨房里四处移动的蜘蛛。"
    "可对手可不是一般的蜘蛛啊。"
    extend "\n是面对人类也不怕的勇猛果敢的蜘蛛，\n简直就像经历无数战争的大将一般。"
    return

label day2_supply:
    hide 班選択 with dissolve
    window show
    "还是去『采购组』看看吧！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "discovery.ogg"
    show sakuya 15 at topleft with dissolve
    window show
    sakuya "好~那就回去吧。"
    show saburo 4 at topright with dissolve
    saburo "就是说啊。\n反正我们也找不到事情做。"
    $ renpy.transition(Quake(0, 40, 0.1, 0.1), layer='master')
    play sound "fx/cute.ogg"
    me "诶，等……等等！！"
    extend "\n那今天的委员会议就到此结束了吗？？"
    show saburo 5 with dissolve
    saburo "没错。\n毕竟我们也没什么事情要做嘛。"
    show sakuya 21 with dissolve
    sakuya "材料什么的，等到学园祭开始之前再弄不就好了。"
    me "话，话是这么说没错……但我们是不是再稍微聚一会儿？"
    extend "\n难得大家都聚在一起。"
    show sakuya 4 with dissolve
    sakuya "我们不是每天都有来学校嘛。"
    extend "\n你这句话只适用今天而已啦。"
    me "唔，话是这么说没错……话是这么说没错……！！"
    hide sakuya with dissolve
    hide saburo with dissolve
    play sound "fx/impact.ogg"
    "对我来说，每一天的校园生活都是很重要的！！"
    extend "\n机会难得，我一秒钟都不想浪费！！！"
    window hide
    window show
    me "好！！\n那么，大家一起去玩吧！！"
    show sakuya 11 at topleft
    show saburo 9 at topright with dissolve
    play sound "fx/boing.ogg"
    sakuya_and_saburo "诶……。"
    "呵……这反应在预料之内。"
    extend "\n我就知道会变成这样……！"
    play sound "fx/sparkle.ogg"
    me "我~！请~客~！！"
    show sakuya 23
    show saburo 4 with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/eureka.ogg"
    sakuya_and_saburo "真的假的！！？"
    "两人的眼睛一下子就亮了起来。"
    extend "\n我就知道……这两个家伙太现实了！"
    me "当然是真的！！"
    extend "\n要是有人想一起去的话，就抓住这根手指哦！"
    hide sakuya with dissolve
    hide saburo with dissolve
    stop music fadeout 0.5
    "……"
    extend "嗯？"
    window hide
    show sakuya 24 at topleft with dissolve
    window show
    sakuya "你在干什么啊，搞快点走吧。"
    show saburo 10 at topright with dissolve
    saburo "我们先去鞋柜了~！"
    play sound "fx/sliding_door.ogg"
    hide sakuya with dissolve
    hide saburo with dissolve
    "说完，两个人就走出了教室。"
    show bg dark with Dissolve(0.4)
    play sound "fx/triangle.ogg"
    me "……哈哈。"
    "我用另一只手温柔地抓住了自己的食指。"
    stop music fadeout 0.5
    window hide
    hide bg with dissolve
    show bg residential_area at center with Radial(0.8)
    play music "quiet_lunch.ogg"
    window show
    "我们离开学校，到御咲市内转悠。"
    show sakuya 5 at topleft with dissolve
    sakuya "那么~你们想去哪？"
    show saburo 4 at topright with dissolve
    saburo "游戏厅还是卡拉ＯＫ……还是去打保龄球？"
    "感觉就像是现在的孩子会玩的那些。"
    extend "\n现在的我完全成了宅男，\n对于那种类型的活动，已经没有什么兴趣了。"
    me "在安静的咖啡厅里悠闲地喝个咖啡，嗯~，怎么样？"
    "明知会被拒绝，我还是试着提议了一下。"
    show sakuya 10
    show saburo 20 with dissolve
    sakuya_and_saburo "……。"
    "啊，果然还是不行啊……。"
    extend "\n对于他们来说，那肯定很无聊吧~。"
    me "就，就是开玩笑啦！还是去别的地方吧……"
    show sakuya 9 with dissolve
    sakuya "没，没有！挺好的吧？"
    extend "\n安静的咖啡厅，嗯。"
    show saburo 17 with dissolve
    saburo "对，对啊！"
    extend "\n我们已经不是那种孩子了，\n偶尔也去那种适合大人的，安静的，放松的地方也挺好的。"
    "哦，意外的好感！"
    extend "\n哈哈……这两位是喜欢成熟的大人呢。"
    extend "\n那么，我就带你们去我的秘密咖啡店吧。"
    me "我知道一个好地方！"
    extend "\n那里虽然不大，但是安静且充满着成熟的感觉，\n二位一定会喜欢的~。"
    show sakuya 21 with dissolve
    sakuya "是，是吗！\n那我们就去那里吧。"
    me "OK！"
    "说定了！"
    "我马上前往我常去的咖啡店。"
    stop music fadeout 2.0
    window hide
    hide sakuya with dissolve
    hide saburo with dissolve
    hide bg with dissolve
    pause 0.4
    play music "fx/tsubame.ogg"
    show bg sky at center with FadeWhite(0.5)
    pause 0.6
    show bg western_cafe1 with Dissolve(1.0)
    window show
    "虽然是西式的，但有着些许古色古香的氛围的咖啡店……。"
    extend "\n刚进去，老板就用与店内气氛相符的稳重态度迎接了我们。"
    stop music fadeout 0.5
    window hide
    play music "adult_cafe.ogg"
    show bg western_cafe2 with Radial(1.3)
    window show
    boss "欢迎光临。"
    extend "\n请问有三位客人吗？"
    me "是的。\n今天带了两位小朋友过来哦。"
    extend "\n老板，麻烦给我上和往常一样的咖啡哦。"
    boss "……？"
    extend "\n恕我冒昧，客人是第一次来我们店吗？"
    "啊……对了。"
    extend "\n被熟悉店里的氛围所吸引，差点就用平常的语气说话了……！"
    me "啊，啊哈哈！！\n是这样的，真是失礼了！"
    extend "\n那个~我们就坐吧台边的位置吧。"
    "吧台边是我偏爱的位置。"
    extend "\n这里不仅能看见店里漂亮的内饰，也能看到外面的风景。"
    extend "\n是一个能让人忘记所有工作的治愈的空间。"
    window hide
    show sakuya 17 at topleft with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    window show
    sakuya "喂，喂！\n我们是不是跑错地方了？"
    extend "\n周围都是大人啊！"
    show saburo 8 at topright with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    saburo "不好……我开始紧张起来了。"
    extend "\n光是站在地板上，双腿就开始颤抖了。"
    me "你在说什么呢。"
    extend "\n不就是一直梦想着能在这里喝茶吗？"
    show saburo 16 with dissolve
    saburo "这，这个嘛……"
    hide sakuya with dissolve
    hide saburo with dissolve
    "我们刚就座，老板就走了过来。"
    shopkeeper "先请客人喝杯冷饮吧。"
    extend "\n平时来我们店的客人多半都比较年长，像你们这样的年轻人可不多见啊。\n我也是由衷感到高兴。"
    extend "\n今天请尽情享受本店的服务。"
    "可能是听到了我们的对话，店主补充道。"
    "说完，他将手巾和冰桶放在我们桌上，然后露出了和蔼的笑容。"
    extend "\n店主的这些小地方也体现了他为人善良的一面。"
    shopkeeper "话说，三位已经决定好点什么了吗？"
    me "我要一杯热的黑咖啡。"
    extend "\n你们两位呢？"
    show sakuya 12 at topleft with dissolve
    sakuya "那个，那个……我，我也要那个！"
    show saburo 23 at topright with dissolve
    saburo "那个那个！！"
    extend "\n这个！我要这个！！"
    "三朗指着菜单向老板点单。"
    hide sakuya with dissolve
    hide saburo with dissolve
    shopkeeper "好的，那您要的是大吉岭奶茶对吧？\n好的，我知道了。"
    extend "\n请您稍等片刻。"
    "老板说完后就进入店铺的后方。"
    window hide
    show saburo 12 at topright with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    window show
    saburo "大，『大吉岭茶』是什么东西……？"
    show sakuya 1 at topleft with dissolve
    sakuya "你，你这家伙，也不搞清楚就乱点单……。"
    me "大吉岭茶是一种红茶。"
    extend "\n虽然有点涩，但喝下去味道十分的醇厚。"
    show saburo 11 with dissolve
    saburo "涩，涩是什么东西……？"
    extend "\n喝的东西还有涩的吗？？"
    me "不，不是的，你误会了……。"
    extend "\n嗯……总之你喝喝看就知道了。"
    hide sakuya with dissolve
    hide saburo with dissolve
    "在我们聊天的过程中，老板端着我们的饮品走了出来。"
    window hide
    pause 0.3
    window show
    shopkeeper "久等了。"
    extend "\n这是黑咖啡……　　　　然后是大吉岭奶茶。"
    shopkeeper "……那么，请您慢慢享受。"
    "老板把饮品放在我们面前后，鞠躬示意后就离开了。"
    window hide
    show saburo 8 at top with dissolve
    window show
    saburo "诶……这，这是什么玩意儿。"
    extend "\n[player_surname]，这……这个怎么用啊。"
    "三朗拿着茶壶，呆呆地盯着杯子和茶壶。"
    extend "\n看来他以为喝的茶是直接泡好了端上来的"
    me "那是茶滤。这是为了把茶叶从茶水里过滤出来的。"
    extend "\n你看，就像这样放在茶杯上\n然后从上方把茶壶里的红茶倒进去。"
    window hide
    show cg c68 1 at center with Radial(0.5)
    window show
    saburo "哦哦……原来如此……"
    extend "\n哇好厉害啊！\n味道好香啊…。"
    "三朗闻着红茶的香气，一脸享受的样子……"
    play sound "fx/sparkle.ogg"
    extend "真是天真无邪啊！"
    "而作哉则是把脸凑到他点的黑咖啡上，\n闻了闻，然后一个人纠结着到底要不要喝。"
    sakuya "姆……咕噜……。"
    me "作哉，要加点牛奶和砂糖吗？"
    extend "\n不然这苦的话你喝不下去的吧。"
    play sound "fx/boing.ogg"
    sakuya "吵，吵死了！！"
    extend "\n又不是小孩子了，这点苦算什么！"
    "然后一口气把咖啡喝了下去。"
    show cg adult with FadeWhite(0.5)
    sakuya "呜……！！"
    extend "\n好苦……这，这种东西我绝对喝不下去的…。"
    "作哉被苦得忍不住流出了眼泪。"
    play sound "fx/entrance.ogg"
    "逞强的少年啊！"
    play sound "fx/entrance.ogg"
    extend "这个台词！！"
    play sound "fx/entrance.ogg"
    extend "这个表情！！！"
    play sound "fx/explosion2.ogg"
    extend "实在是棒啊作哉！！！！"
    show cg c68 2 with Dissolve(0.8)
    saburo "哎呀哎呀，穗海。\n你怎么了？真失礼。"
    extend "\n不要这么粗暴，要优雅地享受茶会的时光啊。"
    sakuya "吵死了~……既然这样，你喝喝看啊……。"
    saburo "我点的可是『大吉岭茶』~。"
    extend "\n啊~真好喝↑"
    sakuya "……[player_surname]君还好吗？\n明明这么苦……。"
    extend "\n这不是人类喝的饮料啊……。"
    me "没事没事！我每天都在喝啊。"
    extend "\n我要是早上不喝咖啡的话，一整天都会浑浑噩噩的。"
    "我喝了一口咖啡。"
    window hide
    hide cg with dissolve
    hide sakuya with dissolve
    hide saburo with dissolve
    window show
    me "嗯，真好喝。和平时的味道一样。"
    show saburo 24 at topright with dissolve
    saburo "[player_surname]。"
    show sakuya 10 at topleft with dissolve
    sakuya "好像很有大人风范啊……。"
    "桀桀桀，是吧是吧。"
    window hide
    hide sakuya with dissolve
    hide saburo with dissolve
    window show
    "我沉浸在优越感和两个少年的可爱之中，享受着在咖啡店的时光。"
    extend "\n话虽如此，他们两个好像还是不太习惯这个空间，\n不到一个小时就说要走，我们就离开了。"
    window hide
    stop music fadeout 2.0
    hide sakuya with Dissolve(0.9)
    hide saburo with Dissolve(0.9)
    hide bg with Dissolve(0.9)
    pause 0.4
    show bg residential_area at center with dissolve
    play music "quiet_lunch.ogg"
    show saburo 18 at topright
    show sakuya 1 at topleft with dissolve
    window show
    sakuya "呜啊啊啊啊……憋死了啊啊啊。"
    saburo "看来我们还没到去那种地方的年纪啊……。"
    me "啊哈哈。\n过不了多久应该就能习惯的！"
    extend "\n我刚开始的时候也是紧张得要死。"
    show sakuya 23 with dissolve
    sakuya "不过，你挺厉害的啊。\n在那种地方，也能泰然处之。"
    extend "\n……有点刮目相看了呢。"
    show saburo 25 with dissolve
    saburo "嗯嗯。\n完全融入了呢。"
    extend "\n真是成熟~很有大人风范呢。"
    me "是，是吗……谢谢夸奖。"
    show saburo 2 with dissolve
    saburo "而且，还是你请的客。"
    extend "\n[player_surname]，多谢多谢。"
    show sakuya 24 with dissolve
    sakuya "多谢招待。"
    me "哈哈……哪里哪里，不用谢。"
    "虽然嘴上在虚张声势，但我的钱包早就已经空空如也了。"
    "初中的时候，钱包里就那么空啊……。"
    extend "\n不过，能够得到他们的认可，这钱花得也很值吧？"
    me "那么，接下来怎么办？"
    show sakuya 5 with dissolve
    sakuya "我还有别的地方要去，先走了。"
    show saburo 5 with dissolve
    saburo "我也是。"
    extend "\n那今天就先到这里解散吧？\n感觉你们都有想做的事情呢！"
    "呜……时候到了啊。"
    extend "\n如果可以的话，我还想和他们在一起待得久一点啊……！！"
    hide saburo with dissolve
    hide sakuya with dissolve
    return

label day2_design_tomo:
    show bg clothing_store at center
    stop music fadeout 0.5
    window show
    me "作为尝试，友君，你试着戴戴看吧。"
    window hide
    play music "tomo_theme.ogg"
    show tomo 18 at top with dissolve
    window show
    tomo "诶，我吗？"
    show tomo 31 with dissolve
    extend "\n可、可是我，不会系领带啊……啊哈哈。"
    me "那我来帮你系吧。"
    "话音刚落，我就扒下了友的立领校服，把手绕到了他的脖子上。"
    "我在系领带的时候，友或许是因这突然的近距离接触而感到惊讶，一直低着头。"
    window hide
    show cg c11 at center with Radial(0.5)
    window show
    me "这样就好啦！"
    extend "\n嗯，很适合你！\n对吧？慎太郎。"
    sintarou "那当然！"
    extend "咱已经完美地用手机拍下来了哟！\n友亲，很适合你哦~。"
    tomo "谢、谢谢……。"
    extend "\n我这还是第一次系领带，所以有点害羞……。"
    me "毕竟你还是个孩子嘛。"
    extend "\n等你出社会了，就算不想系也会被逼着系的，\n趁现在练习习惯一下比较好哦。"
    tomo "唔~……"
    extend "\n[player_name]君有时候会把我们当小孩子看呢。"
    extend "\n就连碎碎念都像大叔一样。"
    me "啊哈哈，这也是听那个上班族说的~现学现卖啦。"
    window hide
    hide cg with dissolve
    hide sintarou with dissolve
    hide tomo with dissolve
    show tomo 27 at topleft
    show sintarou 15 at topright with dissolve
    window show
    sintarou "话说回来……虽然找到了合适的，\n但是会有72条的库存吗？"
    show tomo 21 with dissolve
    tomo "这么说来……。"
    me "我、我去问问店员！"
    "我拿着领带走向收银台，询问了店员。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    play sound "fx/boing.ogg"
    window show
    clerk "72条吗？！"
    extend "\n哎呀~你能买这么多我是很高兴啦，\n但没那么多库存啊……。"
    me "那、那样的话……"
    extend "\n周五之前能进货吗？"
    show tomo 20 at top with dissolve
    tomo "拜托您了！这是学园祭要用的服装，真的很需要！！"
    clerk "嗯~……我先跟供货商联系一下吧。"
    extend "\n能稍微等一会儿吗？"
    me "好的，谢谢您。"
    hide tomo with dissolve
    "店员走进了储藏间，开始打电话。"
    "说起来，我也好久没有被人用对待小孩子的语气说话了啊……"
    extend "\n正当我这么想的时候，慎太郎突然跳了起来。"
    window hide
    show sintarou 21 at topright with dissolve
    $ renpy.transition(Quake(40, 0, 0.15, 0.1), layer='master')
    play sound "fx/cute3.ogg"
    window show
    sintarou "啊……！！！\n糟糕了……怎么办啊。"
    show tomo 28 at topleft with dissolve
    tomo "怎么了？慎酱。"
    show sintarou 16 with dissolve
    sintarou "刚才在购物中心上厕所的时候，\n好像把书包忘在那了……。"
    show tomo 18 with dissolve
    tomo "哇真的诶！慎酱你两手空空嘛！！"
    extend "\n为什么之前没注意到啊。"
    show sintarou 10 with dissolve
    sintarou "咱这就冲刺去那边拿回来，\n要是店员打完电话了，你们就在这儿等等咱吧~。"
    me "知道啦。要小心哦。"
    play sound "fx/running.ogg"
    hide sintarou with dissolve
    "说完之后，慎太郎朝着购物中心跑去。"
    hide tomo with dissolve
    show tomo 12 at top with dissolve
    tomo "店员的电话好像还要打一会儿，\n我去外面的自动贩卖机买点果汁来。"
    extend "\n[player_name]君有什么想喝的吗？"
    me "我就不用了。"
    extend "\n要是让小孩子帮我跑腿，我会过意不去的。"
    show tomo 24 with dissolve
    tomo "这算什么。我们谁跟谁嘛！"
    play sound "fx/running.ogg"
    hide tomo with dissolve
    "友笑着这么说道，走出了店门。"
    "与此同时，店员也打完了电话，从储藏间走了出来。"
    window hide
    window show
    clerk "久等了。"
    extend "\n是72条吧？"
    extend "\n供货商说周五就能送过来，\n应该能赶上学园祭。太好了呢。"
    me "是吗！！\n真的非常感谢！"
    extend "\n给您添麻烦了。"
    clerk "哪里哪里。"
    extend "\n那就麻烦你在这张纸上写下代表人的姓名和收货地址。"
    extend "\n带笔了吗？"
    stop music fadeout 1.0
    "我正打算从包里拿出笔来，视线无意间扫向前方，"
    show bg downtown with FadeWhite(0.5)
    show tomo 5 at top with dissolve
    "\n透过窗户，我看到了友，以及两个像是大学生模样的陌生男子。"
    extend "\n他们好像在争吵些什么。发生什么事了吗？"
    hide tomo with dissolve
    hide bg with dissolve
    me "不好意思！我稍微离开一下！"
    window hide
    play sound "fx/running.ogg"
    show bg downtown at center with dissolve
    play music "hurry_up.ogg"
    window show
    "我急忙跑到外面，躲在他们的视野死角里窥探着情况。"
    window hide
    show tomo 5 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    window show
    tomo "还、还给我！我的钱包！！"
    boy_a "我看看我看看……切，装的钱可真少啊。"
    boy_b "毕竟是个初中小鬼。"
    extend "\n嗯……？那个信封是什么？拿过来。"
    "男子一把夺过了友口袋里的信封。"
    show tomo 18 with dissolve
    tomo "啊，那是……！不、不行！！！"
    extend "\n那些钱，是大家很重要的服装费！！！"
    show tomo 30 with dissolve
    extend "住手！！还给我！！！"
    boy_b "服装费？那是什么？"
    extend "\n初中生带着这种巨款到处乱晃可是不行的哟。"
    extend "\n所以说，这笔钱就先由哥哥们替你保管啦。"
    "友从口袋中掏出手机，\n按了几下，把屏幕怼到两人面前。"
    show tomo 32 with dissolve
    tomo "还给我！！！不、不然我就报警了！！"
    boy_b "啊？从刚才开始就叽叽歪歪的烦死了。"
    extend "\n看来在事情变麻烦之前，先让你闭嘴吧。"
    "说着，男子举起拳头。"
    show tomo 30 with dissolve
    tomo "噫……！"
    me "住手！！！！！"
    window hide
    play sound "fx/wind_slash.ogg"
    show cg c12 1 at center with FadeWhite(0.5)
    hide tomo with dissolve
    window show
    "（咚）"
    play sound "fx/dash.ogg"
    $ renpy.transition(Quake(0, 200, 0.1, 0.065), layer='master')
    extend "\n我飞奔而出，别开男子的手臂，躲开了拳头。"
    boy_b "什！？你是谁啊！"
    boy_a "什么啊，是朋友啊？"
    extend "\n跑到这种偏僻巷子里来，你个小鬼想干嘛啊？"
    me "喂，把钱还给我。"
    show cg c12 2 with dissolve
    extend "\n不然的话，哥哥我就要惩罚你了哦！"
    play sound "fx/punch2.ogg"
    "我顺势扭住了刚才别开的那只手的手腕。"
    man2 "呜！？"
    "趁着男人痛得失去平衡向前栽倒之际，\n我用单手加上全身的体重，锁住了他的手腕。"
    play sound "fx/boing.ogg"
    man2 "好疼疼疼疼疼疼！！！投降！我投降！！"
    man1 "你这混蛋……区区初中生小鬼少给我得意忘形啊！"
    play sound "fx/wind_slash.ogg"
    "另一个男人向我挥来的拳头，被我空出来的手给格挡开了。"
    extend "\n我顺势扭过他的手腕施加体重，那男人便跪倒在地。"
    me "还真是懂礼貌啊，两个人居然都这么干脆地从我正前方攻过来。"
    extend "\n两人夹击的话我还不敢说，但你们这样进攻的话，\n真让我省了不少心呢。"
    me "很遗憾，从我初中开始就像野孩子一样东跑西跑了，\n唯独对体力一直很有自信呢。"
    extend "\n而且，这七年来一直都在练习合气道。"
    extend "\n区区小混混，我可不会输给你们啊。"
    window hide
    hide cg with dissolve
    show tomo 5 at top with dissolve
    window show
    tomo "把我们的服装费还给我！！！！！"
    "友朝着那两个失去平衡的男人，狠狠地给了一记猛撞。"
    hide tomo with dissolve
    $ renpy.transition(Quake(50, 100, 0.2, 0.065), layer='master')
    play sound "fx/dash.ogg"
    male1_and_2 "咕啊啊！！"
    "男人们一边哀嚎着，一边被撞飞了出去。"
    extend "\n没过多久，察觉到骚动的人们聚集了过来。"
    male1 "喂、喂，糟了。赶紧逃吧。"
    male2 "切。一群臭小鬼！给我记住！！"
    play sound "fx/running.ogg"
    stop music fadeout 1.0
    "留下这句狠话后，他们推开看热闹的人们，消失不见了。"
    me "……真是的，所以我才讨厌城里啊。"
    "我捡起那两个家伙弄掉的友的钱包和信封，如此喃喃自语。"
    me "友，没事吧？没受伤吧？"
    window hide
    play music "tomo_theme.ogg"
    show tomo 29 at top with dissolve
    window show
    tomo "嗯、嗯，没事。"
    show tomo 18 with dissolve
    extend "\n……话说回来，[player_name]君真厉害啊！\n竟然一个人就干掉他们了啊。"
    me "不是啦，也不算是干掉他们吧。"
    extend "\n只是引导他们攻击后，顺势按住他们，让他们动弹不得而已。"
    show tomo 12 with dissolve
    tomo "那种不带暴力攻击性的战斗方式，冷静又帅气哦！"
    show tomo 33 with dissolve
    extend "\n谢谢你，[player_name]君。"
    extend "\n要是[player_name]君不在的话，他们肯定就得逞了。"
    me "不客气。"
    extend "\n不过友也勇敢地反击到了最后啊。"
    extend "\n并且，最后给对方致命一击的也是友哦。"
    extend "\n虽然还只是个孩子，却相当有胆量啊。"
    show tomo 31 with dissolve
    tomo "这、这样吗……？"
    extend "\n总之我当时满脑子只想着一定要守住服装费，就一股脑地冲上去了……。"
    me "了不起哦，真棒。"
    extend "\n真不愧是我的友君。"
    "我这么说着，摸了摸友的头。"
    show tomo 33 with dissolve
    tomo "嗯、嗯。"
    show tomo 34 with dissolve
    extend "\n……嘿嘿。"
    "友低着头变得满脸通红。"
    me "你在害羞个什么劲啊~。"
    extend "\n啊，对了，买果汁给你作为奖励吧。"
    show tomo 29 with dissolve
    tomo "诶，不用了！不用的！"
    me "拿着拿着。这种时候就别客气啦！"
    "我这么说着，半强硬地问出了友想喝什么，\n买了果汁，然后回到店里。"
    stop music fadeout 0.5
    window hide
    hide tomo with dissolve
    hide bg with dissolve
    show bg clothing_store at center with Dissolve(1.0)
    play music "umesaki.ogg"
    window show
    "和店员办完手续正在喝果汁的时候，慎太郎也回来了。"
    window hide
    play sound "fx/running.ogg"
    show sintarou 17 at topright with dissolve
    window show
    sintarou "久等了——！！"
    extend "\n哎呀，真是不好意思。\n我居然也会不小心~。"
    me "包没事就好。"
    extend "\n里面的东西也都在吧？"
    show sintarou 13 with dissolve
    sintarou "嗯，没事的！"
    extend "\n话说咱的书都留在学校了，所以包里没什么。"
    show tomo 25 at topleft with dissolve
    tomo "反过来说，要是有陌生人看到了慎酱包里的东西，\n估计会吓得都不敢下手偷吧。"
    me "里面到底装了什么啊……。"
    window hide
    hide sintarou with Dissolve(0.9)
    hide tomo with Dissolve(0.9)
    hide bg with Dissolve(0.9)
    stop music fadeout 0.5
    show bg umesaki_station_front_night at center with Dissolve(1.0)
    window show
    "就这样，总算结束了服装组的我们，踏上了回家的路。"
    extend "\n夕阳完全落下，街道上的灯光，让这个城市变得更加繁华。"
    "我们从梅咲站，和周围的上班族一起挤上了电车。"
    window hide
    play sound "train.ogg"
    show bg train_interior_night with Dissolve(1.5)
    window show
    me "呜哇……这个时间的电车果然很拥挤啊……。"
    "下班回家的各位，今天的工作辛苦了！……那啥的。"
    extend "\n要是我没有变回孩子的话，\n恐怕也是这群筋疲力尽的上班族的一员了吧。"
    "车门关上，电车开始行进。"
    extend "\n但是，刚开始加速的瞬间，电车突然紧急停车了。"
    me "哎呀。"
    "没抓牢扶手的我，因为电车的惯性向前倒去。"
    extend "\n下意识地，我把手伸向了前面的物体。"
    stop sound fadeout 0.5
    play sound "fx/cute.ogg"
    "（捏~）"
    window hide
    play music "cute_silly.ogg"
    show tomo 18 at top with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    window show
    tomo "呜呀！？"
    show tomo 20 with dissolve
    extend "\n喂、喂，[player_name]君！"
    extend "\n你、你在摸哪里啊！"
    me "呜哇！抱、抱歉！！"
    extend "\n我不是那个意思……。"
    hide tomo with dissolve
    show tomo 35 at topleft
    show sintarou 7 at topright with dissolve
    sintarou "哦~\n难不成是痴汉Play？！"
    show sintarou 9 with dissolve
    extend "\n[player_name]酱也相当大胆啊~。"
    me "所以说不是啦！"
    extend "\n只是碰巧啦！碰巧（Tamatama）！！"
    show sintarou 12 with dissolve
    sintarou "只是碰巧碰到了蛋蛋（Tama）吗？"
    play sound "fx/triangle.ogg"
    "真无聊……。"
    hide tomo with dissolve
    hide sintarou with dissolve
    "虽然刚才那确实是偶然……但我内心已经兴奋起来了。"
    extend "\n我盯着刚才碰到了那里的手掌，凑近鼻子闻了闻味道。"
    play sound "fx/sparkle.ogg"
    show cg adult at center with dissolve
    me "（好香啊……。）"
    "在这种满员电车上，这种事太棒了！！！"
    window hide
    hide tomo with dissolve
    hide cg with dissolve
    show tomo 9 at topleft with dissolve
    window show
    tomo "……。"
    show sintarou 14 at topright with dissolve
    sintarou "怎么了？小友，你怎么把腰弯成那样啊。"
    extend "\n是不是闹肚子了？"
    show tomo 20 with dissolve
    tomo "没、没什么！！"
    hide tomo with dissolve
    hide sintarou with dissolve
    conductor "诶~非常抱歉，让您久等了。"
    extend "\n刚才有下车的乘客的行李与车体发生了接触，\n导致列车紧急停车。"
    extend "\n现在即将重新发车。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    window show
    conductor "下一站~宝咲，宝咲站到了。下一站是终点御咲站。"
    window hide
    show bg train_interior_night at center with dissolve
    show tomo 23 at topleft with dissolve
    window show
    tomo "那个，我就在这里下车了。"
    show tomo 19 with dissolve
    extend "\n[player_name]君，慎酱，再见了。"
    me "哦。"
    show sintarou 8 at topright with dissolve
    sintarou "小友，再见~！"
    hide tomo with dissolve
    play sound "fx/running.ogg"
    "电车到达宝咲站后，友就下车了。"
    window hide
    hide sintarou with dissolve
    hide bg with dissolve
    play sound "train.ogg"
    window show
    "电车再次朝终点开去。"
    window hide
    show bg train_interior_night at center with dissolve
    show sintarou 27 at top with dissolve
    window show
    sintarou "小友的样子，总感觉怪怪的呢。"
    me "嗯……是怎么了呢。大概是累了吧。"
    "确实，友比平时要安静许多，这虽让我有些在意，"
    extend "\n但我想他应该是走了一整天，又被不良少年缠上，所以累了吧。"
    stop sound fadeout 2.0
    show cg misaki_station_night at center with Dissolve(0.7)
    extend "\n在御咲站和慎太郎分别后，我就直接回家了。"
    window hide
    hide bg with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    hide sintarou with Dissolve(0.8)
    pause 0.4
    show bg living_room_night at center with Radial(1.0)
    play music "nostalgia.ogg"
    window show
    play sound "fx/door_open.ogg"
    me "我回来了~。"
    mother "欢迎回来~。"
    extend "\n今天回来得有点晚啊。"
    me "嗯。"
    extend "\n我去了趟梅咲，去采购学园祭要用的东西了。"
    mother "哎呀，是这样啊~。"
    extend "\n不过，那一带晚上很危险的，可不能在那里待到太晚哦？"
    me "我知道啦。又不是第一次去了。"
    extend "\n呼~今天也好开心啊。"
    play sound "fx/beer.ogg"
    "我慢条斯理地从冰箱里取出罐装啤酒，打开了拉环。"
    "（噗——嘶）"
    mother "等、等一下！！[player_name]！？\n为什么要喝啤酒啊！！"
    extend "\n你，还是未成年人吧！"
    play sound "fx/boing.ogg"
    me "啊！！"
    "糟了！！下意识地就按平时的习惯……。"
    me "啊、啊哈哈。\n抱歉抱歉。"
    extend "我搞错了，以为这是果汁啊。\n啊哈哈哈。"
    "我干笑着掩饰了过去。"
    mother "真是的……"
    extend "\n真担心你将来也像爸爸一样，\n变成那种一回家就非得喝啤酒的酒鬼呢。"
    extend "\n我可不要啊~↑"
    me "会、会那样吗~\n啊哈哈哈……。"
    "总、总算蒙混过去了。好险好险。"
    "在学校里，也得注意别说漏嘴了啊……。"
    return

label day2_design_sintarou:
    show bg clothing_store at center
    stop music fadeout 0.5
    window show
    me "作为尝试，慎太郎，你试着戴戴看吧。"
    window hide
    play music "sintarou_theme.ogg"
    show sintarou 14 at top with dissolve
    window show
    sintarou "咱来戴——？"
    show sintarou 11 with dissolve
    extend "\n是可以啦，\n不过，咱不知道该怎么系领带耶——。"
    me "那我来帮你系吧。"
    "话音刚落，我就把手绕到了慎太郎的脖子上。"
    window hide
    show cg c25 at center with Radial(0.5)
    window show
    sintarou "哦……[player_name]酱真是的，突然变得这么大胆呢♪"
    me "别说傻话了，乖乖待着别动。"
    tomo "咻咻——！！"
    "真是的，这两个家伙……。"
    me "这样就OK了！\n嗯，很适合你！"
    extend "\n对吧？友君。"
    tomo "嗯！\n这种松松垮垮的系法很有小慎的风格！"
    extend "\n很适合你哦！！"
    sintarou "多谢啦~。"
    extend "\n虽然咱也给别人系过领带，\n但这还是第一次有人帮咱系呢~。\n呐哈哈哈！"
    tomo "唔咿呦~！\n小慎说的好成熟的样子♪"
    sintarou "话说回来，这样子还真是新鲜啊。"
    extend "\n因为制服不是西装外套，\n所以也没有系领带的机会。"
    me "毕竟你还是个孩子嘛。"
    extend "\n等你出社会了，就算不想系也会被逼着系的，\n趁现在练习习惯一下比较好哦。"
    window hide
    hide cg with dissolve
    hide tomo with dissolve
    hide sintarou with dissolve
    show tomo 27 at topleft with dissolve
    window show
    tomo "唔~……"
    extend "\n[player_name]君有时候会把我们当小孩子看呢。"
    extend "\n就连碎碎念都像大叔一样。"
    me "啊哈哈，这也是听那个上班族说的~现学现卖啦。"
    show sintarou 15 at topright with dissolve
    sintarou "话说回来……虽然找到了合适的，"
    extend "\n但是会有72条的库存吗？"
    show tomo 21 with dissolve
    tomo "这么说来……。"
    me "我、我去问问店员！"
    "我拿着领带走向收银台，询问了店员。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    play sound "fx/boing.ogg"
    window show
    clerk "72条吗？！"
    extend "\n哎呀~你能买这么多我是很高兴啦，"
    extend "\n但没那么多库存啊……。"
    me "那、那样的话……"
    extend "\n周五之前能进货吗？"
    show sintarou 26 at top with dissolve
    sintarou "这个无论如何都得用在文化祭的服装上啊~！"
    clerk "嗯~……我先跟供货商联系一下吧。"
    extend "\n能稍微等一会儿吗？"
    me "好的，谢谢您。"
    hide sintarou with dissolve
    "店员走进了储藏间，开始打电话。"
    "说起来，我也好久没有被人用对待小孩子的语气说话了啊……"
    extend "\n正当我这么想的时候，友突然跳了起来。"
    window hide
    show tomo 28 at topleft with dissolve
    $ renpy.transition(Quake(40, 0, 0.15, 0.1), layer='master')
    play sound "fx/cute3.ogg"
    window show
    tomo "……诶！！！"
    extend "\n完蛋了！！！"
    show sintarou 14 at topright with dissolve
    sintarou "怎么了，友亲。"
    show tomo 18 with dissolve
    tomo "刚才在购物中心上厕所的时候，\n好像把书包忘在那了……。"
    show sintarou 32 with dissolve
    sintarou "真的~。我现在才注意到，友两手空空的！"
    extend "\n怎么到现在才发现啊。"
    show tomo 20 with dissolve
    tomo "抱歉！我现在马上去拿，你们在这里等我。\n如果店员的电话打完了，你们就在这里等我！"
    me "知道了。要小心哦。"
    play sound "fx/running.ogg"
    hide tomo with dissolve
    "说完，友就朝着购物中心的方向跑去了。"
    window hide
    hide sintarou with dissolve
    show sintarou 11 at top with dissolve
    window show
    sintarou "真是的~友亲真是冒冒失失的啊~。"
    me "是啊。"
    extend "\n店员的电话好像还要打一会儿，\n我去外面的自动贩卖机买点果汁来。"
    extend "\n慎太郎，有什么想喝的吗？"
    show sintarou 29 with dissolve
    sintarou "我就不用了啦~。"
    extend "\n今天也没带多少钱出来。"
    me "一两瓶果汁而已，很便宜的啦。这点小钱我还是请得起的。"
    extend "\n小孩子家家的，用不着跟我客气哦？"
    show sintarou 9 with dissolve
    play sound "fx/eureka.ogg"
    sintarou "……嚯~。"
    "慎太郎露出了某种意味深长的坏笑。"
    me "怎、怎么了？"
    show sintarou 13 with dissolve
    sintarou "哎呀~只是觉得今天那个分数一直在涨啊！"
    me "分数？是指什么？"
    show sintarou 2 with dissolve
    sintarou "『内在是25岁大叔』的可信度分数哦~。"
    extend "\n虽然还没有『决定性的一击』，但从早上开始就一直有蛛丝马迹！"
    me "啊啊，事实上，如果内在是25岁的话，就算没有刻意去表现，\n只要老老实实做自己，成熟的感觉自然就出来了。"
    show sintarou 20 with dissolve
    sintarou "原来如此啊~。"
    show sintarou 23 with dissolve
    extend "\n但是，和友亲在一起的时候还是克制一下比较好！"
    extend "\n我在某种意义上可是被吓了一跳哦~虽然姑且是帮你糊弄过去了。"
    show sintarou 30 with dissolve
    extend "\n这件事，还是不要对大家说比较好吧？"
    me "嗯！！你帮了大忙了……谢谢！"
    extend "\n让不相干的人知道了的话就不好了。"
    extend "\n毕竟这种事，就算本人没有那个意思，\n也会因为一点小事就传开的。"
    show sintarou 17 with dissolve
    sintarou "这说的完全就是今天面对友亲时的[player_name]酱嘛！"
    show sintarou 29 with dissolve
    extend "\n不过~我觉得无论是友亲还是大家，都不会轻易相信这种事啦~。"
    me "呜……无地自容……。"
    "确实啊……就算说只要老实做自己，但在除了和慎太郎独处的时候以外，\n还是必须得注意才行啊。"
    extend "\n竟然被一个小孩子说教了……。"
    show sintarou 31 with dissolve
    sintarou "说起来，\n咱也曾有过那样思考这一类事情的时期呢。"
    me "诶？"
    show sintarou 13 with dissolve
    sintarou "嗯喵，就是害怕流言蜚语传开的时期~。"
    show sintarou 12 with dissolve
    extend "\n我们有无法轻易说出口的事情吧？同志啊。"
    "『正太控』这三个字浮现于脑海。"
    "确实，这件事是绝对不能暴露的。"
    extend "\n像我这种人，要是被别人知道居然用那种眼光看待少年， 简直就是社会性死亡！"
    extend "\n昨天能和慎太郎达成共识，真的算得上是幸运了。"
    show sintarou 18 with dissolve
    sintarou "就算对自己来说再普通，但终究是少数派嘛。"
    extend "\n不过~站在对方的立场想的话，发现自己成了正太控的XP，\n会想把咱们认定为『有害』的心情，倒也不是不能理解啦~。"
    "原来如此。"
    extend "\n慎太郎是身为正太的正太控……正因为被自己的喜好对象所包围，\n所以对于暴露这件事，他比我还要敏感。"
    "朋友也许会变得不再是朋友，周围的人也许会变成敌人。"
    extend "\n对于还不懂『区别』与『歧视』差别的孩子们来说，这是常有的事。"
    me "不过，从慎太郎现在的言行来看，很难想象竟然是这样的人。"
    show sintarou 31 with dissolve
    sintarou "因为现在的我已经是初中生了嘛。"
    show sintarou 29 with dissolve
    extend "\n总觉得~事事都要在意别人的眼光，变得好麻烦啊~。\n那种畏畏缩缩的时期，可以说早就和小学一起毕业了！"
    show sintarou 2 with dissolve
    extend "\n所以就当作御咲学园的入学纪念，试着出柜了！！"
    show sintarou 1 with dissolve
    sintarou "结果非常成功，我才终于能像现在这样自由地生活。"
    extend "\n不过，最重要的是大家的包容啦。"
    show sintarou 3 with dissolve
    extend "\n嘛，不过这跟[player_name]酱的情况大不相同，\n所以你也可以像我一样随便暴露哦！"
    "……初中生，可能比我想象的还要成熟。"
    extend "\n无论是藏在内心的烦恼，还是对外在世界的包容力，都比我想象的要强得多。"
    show sintarou 15 with dissolve
    sintarou "哈~说着说着就口渴了。"
    extend "\n『浓可尔比思苏打』，拜托啦！"
    me "诶？你在说什么？"
    show sintarou 4 with dissolve
    sintarou "刚才不是说好的嘛——！说要请我喝饮料。"
    extend "\n既然是成年人，一两瓶饮料而已，也不算什么吧？"
    "慎太郎淘气地笑着。"
    me "哈哈，真有你的啊~。"
    extend "\n知道了，稍等一下。"
    extend "\n店员如果回来的话，就拜托你代替我应付一下咯。"
    show sintarou 1 with dissolve
    sintarou "了解~。"
    "听到回答后，我走出了店门。"
    window hide
    hide sintarou with dissolve
    hide bg with dissolve
    play sound "fx/running.ogg"
    show bg downtown at center with dissolve
    window show
    "嗯嗯嗯……打开钱包后才发现，"
    extend "\n现在的我，身上的钱连初中时代的水平都没有。"
    extend "\n一个月就五百块，请朋友喝饮料说实话还真有点吃紧！！"
    "可是，这也是为了证明自己是大人！"
    extend "\n绝不能舍弃大人的尊严啊，[player_surname][player_name]！！"
    extend "\n这点小钱，根本不痛不痒！！"
    window hide
    play sound "fx/running.ogg"
    show bg clothing_store with dissolve
    show sintarou 8 at top with dissolve
    window show
    sintarou "回来啦~感谢感谢！"
    me "没事没事。\n作为大人，这是理所当然的。"
    show sintarou 9 with dissolve
    sintarou "嚯嚯~你还真会说话啊！"
    show sintarou 14 with dissolve
    extend "\n啊嘞？[player_name]酱没给自己买喝的吗？"
    me "我、我只是买果汁来打发时间，\n反正我的喉咙又不干，所以不需要啦！！"
    extend "\n而且我也没那么想喝饮料！"
    extend "\n因为我是大人嘛！！呼哈哈。"
    show sintarou 20 with dissolve
    sintarou "是吗？"
    show sintarou 9 with dissolve
    extend "\n虽说内心是大人，但身体可是小孩子哦，\n所以其实你其实很渴吧~？"
    show sintarou 5 with dissolve
    extend "\n好啦好啦，你就老实说嘛~。"
    "慎太郎说着，把手中的饮料罐子朝我递了过来。"
    "（咕咚……）"
    "我不禁咽了咽口水。"
    me "这可不行！！大人是不能被这种程度的诱惑给……。"
    show cg adult at center
    play sound "fx/sparkle.ogg"
    show sintarou 22 with dissolve
    sintarou "咱的浓郁可尔必思苏打，你不想喝吗？"
    window hide
    hide sintarou with dissolve
    hide bg with dissolve
    hide cg with dissolve
    window show
    "…"
    window hide
    window show
    play sound "fx/wow2.ogg"
    "（咕噜咕噜……）"
    window hide
    show bg clothing_store at center
    show sintarou 9 at top with Radial(0.5)
    window show
    sintarou "呀哈哈~[player_name]酱身体还是很诚实的嘛~！"
    show sintarou 1 with dissolve
    extend "\n尽管喝个够吧~。"
    "可恶……我岂不是变成五指山下的孙悟空了吗。明明我是个大人来着！！"
    show sintarou 4 with dissolve
    sintarou "不过，我和[player_name]酱之间的秘密只有我们两个人知道。我对着这瓶可尔必思起誓绝对不会说出去，你就放心吧。"
    me "还真是随便的誓言啊……。"
    show sintarou 31 with dissolve
    sintarou "男人就不要在意那些小细节啦！"
    show sintarou 2 with dissolve
    sintarou "啊，对了。刚才下单的手续已经办好了哟！"
    show sintarou 1 with dissolve
    extend "\n店员说周五之前肯定能送到。"
    extend "\n太好了！[player_name]酱！"
    me "那真是太好了。"
    extend "\n这样一来，今天的任务也就顺利完成了。"
    hide sintarou with dissolve
    "呼……今天一整天，都被慎太郎牵着鼻子走了啊。"
    stop music fadeout 0.5
    extend "\n他这个人飘忽不定，让人捉摸不透。"
    extend "哪怕是对于身为大人的我来说，也是如此。"
    "正因如此，他才让我如此着迷，\n以至于我都想向他吐露心声了。"
    play music "umesaki.ogg"
    "正当我这么想着的时候，友回来了。"
    window hide
    play sound "fx/running.ogg"
    show tomo 20 at topleft with dissolve
    window show
    tomo "久等了~！！！"
    show tomo 9 with dissolve
    extend "\n抱歉抱歉！\n一不小心就发了会儿呆。"
    show sintarou 4 at topright with dissolve
    sintarou "毕竟到了厕所，不知不觉就想『放松』一下，这种事也是常有的呢~"
    show sintarou 5 with dissolve
    play sound "fx/cute.ogg"
    extend "\n我偶尔也会偷偷来一发。"
    show tomo 15 with dissolve
    tomo "嗯嗯！"
    show tomo 11 with dissolve
    play sound "fx/cute2.ogg"
    extend "\n啊，不过，不注意气味的话，被其他人发现就麻烦了。"
    "刚一回来就聊这个。"
    show sintarou 3
    show tomo 12 with dissolve
    extend "这两个人果然是臭味相投呢。"
    me "能找到书包真是太好了呢。"
    extend "\n里面的东西也都在吧？"
    show tomo 10 with dissolve
    tomo "嗯，没事的！"
    extend "\n毕竟那个东西也好好的在里面。"
    "从拉开的拉链的缝隙中，"
    play sound "fx/triangle.ogg"
    extend "看到类似电摩棒的东西，不知该说什么。"
    show sintarou 8 with dissolve
    sintarou "我们这边也是顺利订购到领带了~。"
    show tomo 4 with dissolve
    tomo "那真是太好了！那，差不多该回去了吧。"
    window hide
    hide sintarou with Dissolve(0.9)
    hide tomo with Dissolve(0.9)
    hide bg with Dissolve(0.9)
    stop music fadeout 0.5
    show bg umesaki_station_front_night with Dissolve(2.0)
    window show
    "就这样，总算结束了服装组的我们，踏上了回家的路。"
    extend "\n夕阳完全落下，街道上的灯光，让这个城市变得更加繁华。"
    "我们从梅咲站，和周围的上班族一起挤上了电车。"
    window hide
    play sound "train.ogg"
    show bg train_interior_night with Dissolve(1.5)
    window show
    me "呜哇……这个时间的电车果然很拥挤啊……。"
    "下班回家的各位，今天的工作辛苦了！……那啥的。"
    extend "\n要是我没有变回孩子的话，\n恐怕也是这群筋疲力尽的上班族的一员了吧。"
    "车门关上，电车开始行进。"
    extend "\n但是，刚开始加速的瞬间，电车突然紧急停车了。"
    me "哎呀。"
    "没抓牢扶手的我，因为电车的惯性向前倒去。"
    extend "\n下意识地，我把手伸向了前面的物体。"
    stop sound fadeout 0.5
    play sound "fx/cute.ogg"
    "（捏~）"
    window hide
    play music "cute_silly.ogg"
    show sintarou 32 at top with dissolve
    $ renpy.transition(Quake(60, 0, 0.1, 0.15), layer='master')
    window show
    sintarou "……那个，[player_name]桑。"
    extend "\n您的小手手碰到我了哟~。"
    "慎太郎在我耳边轻语道。"
    me "呜哇！抱、抱歉！！"
    extend "\n我不是那个意思……。"
    show sintarou 9 with dissolve
    sintarou "哼哼嗯。\n虽说要诚实面对欲望，但这未免也太大胆了点啊。"
    show sintarou 12 with dissolve
    extend "\n啊，这行为也是在打算证明自己是大人吗？"
    extend "\n可信度在蹭蹭往上涨呢。"
    me "不、不是的……不是那个意思………。"
    show sintarou 30 with dissolve
    sintarou "但是啊……[player_name]桑，"
    extend "\n在之前的电车上，你一直盯着我们的那里看吧。"
    play sound "fx/shock_big.ogg"
    "被、被发现了啊啊啊啊啊！！！！！"
    "我低着头，感觉后背一凉，流了一身冷汗。"
    extend "\n脸好烫。这什么情况，超难为情啊！"
    extend "\n被痴汉的一方居然搞起了言语羞辱，这算哪门子的Play啊！！"
    me "那、那那那是……"
    show sintarou 18 with dissolve
    sintarou "没~事。"
    extend "\n包括这件事，我都会对友保密的呦♪"
    show sintarou 12 with dissolve
    extend "\n真是的，[player_name]桑还真是可爱啊~。"
    window hide
    hide sintarou with dissolve
    show sintarou 31 at topright
    show tomo 12 at topleft with dissolve
    window show
    tomo "嗯？你们说啥呢？"
    "慎太郎把脸从我耳边移开，回答道。"
    show sintarou 29 with dissolve
    sintarou "[player_name]酱说想把友亲头上的呆毛给拔掉。"
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    show tomo 5 with dissolve
    tomo "什、什么！！"
    me "我才没说那种话——！！"
    "真是的……对上慎太郎这家伙，可真是没辙了啊。"
    hide sintarou with dissolve
    hide tomo with dissolve
    "虽然刚才那确实是偶然……但我内心已经兴奋起来了。"
    "我盯着刚才碰到了那里的手掌，凑近鼻子闻了闻味道。"
    play sound "fx/sparkle.ogg"
    show cg adult at center with dissolve
    me "（好香啊……。）"
    "在这种满员电车上，这种事太棒了！！！"
    window hide
    hide cg with dissolve
    show sintarou 20 at topright with dissolve
    window show
    sintarou "看来这种时候，"
    extend "\n就算长大成人也是不会变的呢~。"
    show tomo 27 at topleft with dissolve
    tomo "诶——！你们在说什么呀~？"
    hide sintarou with dissolve
    hide tomo with dissolve
    conductor "诶~非常抱歉，让您久等了。"
    extend "\n刚才有下车的乘客的行李与车体发生了接触，\n导致列车紧急停车。"
    extend "\n现在即将重新发车。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    window show
    conductor "下一站~宝咲，宝咲站到了。下一站是终点御咲站。"
    window hide
    show bg train_interior_night at center with dissolve
    show tomo 12 at topleft with dissolve
    window show
    tomo "那，我就在这站下啦。"
    show sintarou 8 at topright with dissolve
    sintarou "好！友亲，明天见~。"
    me "辛苦啦。路上小心啊~。"
    show tomo 4 with dissolve
    tomo "嗯，拜拜！明天见！"
    hide tomo with dissolve
    play sound "fx/running.ogg"
    "电车到达宝咲站后，友就下车了。"
    window hide
    hide sintarou with dissolve
    hide bg with dissolve
    play music "fx/train.ogg"
    show bg train_interior_night at center with dissolve
    window show
    "电车再次朝终点开去。"
    "我环视车内，发现乘客已经所剩无几。"
    window hide
    show sintarou 8 at top with dissolve
    window show
    sintarou "难得有空位，我们坐吧。"
    me "嗯，好。"
    window hide
    hide sintarou with dissolve
    show bg train_night with dissolve
    window show
    "正好有两个并排的空位，于是我们坐了下去。"
    "我无意间向前一看，注意到了坐在前面的熟人。"
    extend "\n我下意识站起身去打招呼。"
    window hide
    show cg remarkable at center with dissolve
    window show
    me "进藤先生，好久不见！"
    extend "\n您最近可好？"
    "男人一脸茫然地回应道。"
    play sound "fx/boing.ogg"
    man "诶？你、你是哪位啊？"
    me "我是在吉蒙（Gymno）股份公司任职的[player_surname]啊！"
    extend "\n前些日子的那笔交易，真是承蒙您关照了。"
    me "哎呀~没想到能在这里遇到您！"
    extend "\n我记得您的府上是在四国那边吧。"
    extend "\n既然如此，今天又是为何会来到这边呢？"
    man "你、你到底在胡说什么啊？！"
    extend "\n别开玩笑了！"
    me "诶？可是……。"
    show cg dark with Dissolve(0.3)
    play sound "fx/ding.ogg"
    extend "\n啊……。"
    "搞砸了——我瞬间意识到了这一点。"
    extend "\n我又一次忘记了自己现在的模样。"
    "同时，我注意到周围投射过来的视线非常扎人。"
    show bg train_interior_night with dissolve
    "那也难怪。"
    stop sound fadeout 0.5
    extend "\n在旁人看来，我不过是个奇怪的孩子罢了。"
    window hide
    hide cg with dissolve
    show sintarou 29 at top with dissolve
    window show
    sintarou "……那个，[player_name]君。"
    extend "\n总之，先坐下来吧。"
    "慎太郎把手搭在我的肩膀上，对我说道。"
    play sound "fx/dash.ogg"
    "呜哇啊啊啊！！\n又搞砸了啊啊啊！！"
    hide sintarou with dissolve
    "……。"
    me "如果地上有洞……我真想钻进去啊。"
    window hide
    show sintarou 30 at top with dissolve
    window show
    sintarou "好啦好啦！"
    extend "\n打起精神来嘛~[player_name]桑。"
    "慎太郎一边说着，一边抚摸着我的头。"
    "然而，我却忍受不了车内沉闷尴尬的氛围，"
    stop sound fadeout 2.0
    play sound "fx/running.ogg"
    hide sintarou with dissolve
    hide bg with dissolve
    extend "\n刚到车站，就立刻飞奔了出去。"
    window hide
    play music "fx/night_insects.ogg"
    show bg misaki_station_night at center with Dissolve(1.5)
    play sound "fx/running.ogg"
    show sintarou 16 at top with dissolve
    window show
    sintarou "[player_name]！等等~！"
    extend "\n不用跑得那么急啦~！"
    "慎太郎拼命地追了上来。"
    "我，停下了脚步。"
    me "哈啊……哈啊……"
    extend "\n我，今后该何去何从啊……？"
    extend "\n顶着这副模样，接下来的生活还能继续下去吗……？"
    show sintarou 26 with dissolve
    sintarou "没事的啦，[player_name]。"
    extend "\n咱会陪在你身边，罩着你的啦！"
    "慎太郎摆出了拳击的架势。"
    me "慎太郎……。"
    window hide
    stop music fadeout 0.5
    play music "good_scene.ogg"
    show cg c26 at center with Radial(0.5)
    window show
    sintarou "因为知道这个秘密的人，就只有咱一个嘛。"
    extend "\n这样的话，能帮到[player_name]的唯一人选，\n不就只有咱了吗！"
    extend "对吧？"
    sintarou "咱啊，会试着努力去相信[player_name]说的话的哟。"
    extend "\n那样的话，就算[player_name]像刚才那样搞砸了，我也能马上帮你解围！"
    extend "\n刚才那个人，也是你上班时的熟人吧？"
    window hide
    hide cg with dissolve
    hide sintarou with dissolve
    window show
    me "……谢谢你，慎太郎。"
    extend "\n听到你这么说，我感觉被拯救了一样。"
    me "嗯……！\n我也，一定会让慎太郎相信我的！！"
    extend "\n会让你相信，我的内在真的是一个25岁的男人！！"
    show sintarou 7 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sintarou "哦！就是这种气势，就是这种气势！！"
    show sintarou 4 with dissolve
    extend "\n我很期待哦♪"
    hide sintarou with dissolve
    "被慎太郎一边说着『乖啦乖啦』一边摸头安抚，我终于恢复了平静。"
    extend "\n之后我和慎太郎道别，各自回了家。"
    stop music fadeout 1.5
    hide bg with dissolve
    "我真是……赢不了慎太郎啊……。"
    window hide
    pause 0.4
    show bg living_room_night at center with Radial(0.9)
    play music "nostalgia.ogg"
    window show
    play sound "fx/door_open.ogg"
    me "我回来了~。"
    mother "欢迎回来~。"
    extend "\n今天回来得有点晚啊。"
    me "嗯。"
    extend "\n我去了趟梅咲，去采购学园祭要用的东西了。"
    mother "哎呀，是这样啊~。"
    extend "\n不过，那一带晚上很危险的，可不能在那里待到太晚哦？"
    me "我知道啦。又不是第一次去了。"
    extend "\n呼~今天也好开心啊。"
    "我缓缓地正打算从冰箱里拿出一罐啤酒。"
    play sound "fx/boing.ogg"
    "……哎呀，好险好险。就是这种下意识的习惯不行啊……。"
    mother "回来就直奔冰箱，和你爸爸一模一样呢。"
    extend "\n真担心你将来也像爸爸一样，\n变成那种一回家就非得喝啤酒的酒鬼呢。"
    extend "\n我可不要啊~↑"
    me "会、会那样吗~\n啊哈哈哈……。"
    "在学校里，也得注意别再出洋相或者说漏嘴了啊……。"
    return

label day2_end:
    window show
    "在那之后，加上回家的父亲，\n我们又像昨天一样，全家聚在一起吃晚饭。"
    "真是幸福呢。"
    extend "\n以后也想一直在这个世界生活下去。"
    "这种想法，比昨天更加坚定了。"
    extend "\n我这么觉得。"
    window hide
    hide bg with Dissolve(1.0)
    play sound "fx/door_open.ogg"
    show bg protagonist_room_night at center with Dissolve(1.0)
    window show
    "回到自己的房间后，我躺在床上。"
    "这真是个幸福的世界啊。"
    extend "\n我想让大家幸福，想让大家都露出更多的笑容。"
    extend "\n为此，"
    me "我会尽全力面对挑战，一定要让御咲祭取得成功！"
    "在那之前，请让我做个好梦吧，神啊。"
    extend "\n话说回来……"
    me "呼啊~……。"
    stop music fadeout 2.0
    "小孩子也太容易睡着了吧。"
    extend "\n如果是平时，我肯定还得再醒一会儿，\n看会儿电视，玩会儿电脑，打会儿手枪！！"
    extend "\n本来还想再享受一下独处时光。"
    "……既然是在梦里，就忍耐一下吧。"
    "闭上眼睛，慢慢沉入梦乡……。"
    hide bg with DefocusBlack(5.0)
    "Zzz"
    window hide
    return

label day2_layout_tubasa:
    show bg meffen_cafe_evening at center
    stop music fadeout 0.5
    window show
    me "尤其是翼！"
    extend "\n虽说看起来绝对不是女孩子，\n但身为男孩子被强行换上女装的感觉简直绝了！！"
    extend "\n这绝对是受宅男欢迎的！"
    window hide
    play music "tubasa_theme.ogg"
    show tubasa 8 at topright with dissolve
    window show
    tubasa "这，这是什么评价……！"
    show sinobu 10 at topleft with dissolve
    sinobu "完全搞不懂是在夸人还是在损人呢。"
    "这时，我小声地对翼说。"
    me "要是看到那副样子，友一定会很开心的。"
    hide tubasa with dissolve
    hide sinobu with dissolve
    show tubasa 21 at top with dissolve
    tubasa "啊……"
    me "之后我把照片发给你哦。"
    show tubasa 3 with dissolve
    tubasa "……不，不过，那种……太难为情了啦…。"
    "翼下意识红了脸。"
    window hide
    hide tubasa with dissolve
    show sinobu 2 at topleft with dissolve
    window show
    sinobu "……没事啦。"
    extend "\n友看到那种照片不会有什么的。"
    show tubasa 8 at topright with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tubasa "忍，忍君！！？你听到了吗！？"
    show sinobu 11 with dissolve
    sinobu "嘿嘿。"
    me "你看，青梅都这么说了，！！"
    extend "\n呐！还是发给他看看吧。"
    show tubasa 7 with dissolve
    tubasa "我，我才不要。"
    show sinobu 12 with dissolve
    sinobu "他反而会高兴的。"
    extend "\n友好像也挺在意翼的。"
    show tubasa 21 with dissolve
    tubasa "诶！？"
    me "是这样吗？"
    show sinobu 23 with dissolve
    sinobu "嗯。"
    extend "\n他经常提起翼呢。\n说翼很可爱，很治愈。"
    show tubasa 12 with dissolve
    play sound "fx/sparkle.ogg"
    tubasa "友，友君……。"
    "翼听到了忍的话，脸变得更红了。"
    show tubasa 23 with dissolve
    tubasa "……我，我知道啦。"
    extend "\n之后……我会发给他的……！"
    window hide
    hide tubasa with dissolve
    hide sinobu with dissolve
    window show
    clerk2 "看起来很高兴呢！"
    extend "\n好了，三份蛋糕套餐，拿好了哦~。"
    clerk3 "真是让人忍不住啊~！\n少年们欢闹的样子……身体和心灵都得到了治愈~！！"
    extend "\n呐，店长！"
    play sound "fx/cute2.ogg"
    manager "啊。\n一定要好好地记在心里。"
    extend "\n这种机会可不多见啊……！！"
    "旁人看来，我们俩应该是在谈论恋爱话题吧\n就像是女高中生一样。"
    extend "\n不过，一旦开始恋爱，无论男人还是女人都会兴奋得\n难以自持，情不自禁地欢呼雀跃起来。"
    "我们一边吃着蛋糕，翼一边发送了彩信。"
    window hide
    hide bg with Dissolve(0.7)
    pause 0.3
    stop music fadeout 0.5
    show bg evening at center with Dissolve(0.9)
    play music "quiet_lunch.ogg"
    pause 0.6
    show bg meffen_cafe_evening with Dissolve(0.8)
    show tubasa 1 at topright with dissolve
    window show
    tubasa "……一直没有……回信过来……。"
    show sinobu 9 at topleft with dissolve
    sinobu "服装组的工作还没做完吗？"
    me "肯定是这样了。"
    extend "\n耐心等待吧，翼同学。"
    show tubasa 22 with dissolve
    tubasa "是，是啊。"
    me "话说回来，这蛋糕真好吃啊。"
    extend "\n……嗯？忍。\n你的脸蛋上粘了奶油哦。"
    extend "\n让我来帮你擦掉吧。"
    show sinobu 6 with dissolve
    sinobu "别把我当成小孩子啊。"
    play sound "fx/dash.ogg"
    $ renpy.transition(Quake(0, 60, 0.13, 0.06), layer='master')
    "啪嚓"
    "愉快地度过了一段时光后，我们结束了蛋糕的品尝，\n向照顾我们的店长小姐和女仆们表达了感谢，然后离开了店里。"
    window hide
    stop music fadeout 0.5
    hide tubasa with dissolve
    hide sinobu with dissolve
    hide bg with dissolve
    play music "fx/tsubame.ogg"
    show bg downtown_evening at center with Radial(0.5)
    show sinobu 26 at topleft with dissolve
    window show
    sinobu "今天的活儿也做完了，就在这里解散吧。"
    extend "\n辛苦了，明天见。"
    me "哦。"
    show tubasa 5 at topright with dissolve
    tubasa "好的，辛苦了。"
    extend "\n明天见……。"
    window hide
    play sound "fx/running.ogg"
    hide sinobu with dissolve
    window show
    "就这样，今天的布置组的工作，平安地完成了。"
    extend "\n那我也回家吧。"
    window hide
    hide tubasa with dissolve
    show tubasa 30 at top with dissolve
    window show
    tubasa "那个……[player_name]君。"
    extend "\n你还有时间吗……？"
    me "诶？嗯，有吧。"
    "翼看起来非常不安，就像是在寻求帮助一般。"
    me "……去对面的公园吧，就我们俩聊聊。"
    show tubasa 22 with dissolve
    tubasa "这，这样就帮大忙了。"
    stop music fadeout 0.5
    window hide
    hide tubasa with Dissolve(0.8)
    play music "tubasa_theme.ogg"
    show bg park_bench with Dissolve(2.0)
    pause 0.3
    window show
    me "所以，怎么了？"
    show tubasa 15 at top with dissolve
    tubasa "我还没收到……友君发来的回信。"
    extend "\n从那之后已经过去不少时间了。\n服装班的工作一定也已经结束了。"
    extend "\n可……。"
    me "他只是偶然漏掉了你的信息吧。"
    extend "\n过一会就会察觉到并回信的。"
    show tubasa 1 with dissolve
    tubasa "友君回信的速度一向很快。"
    extend "\n所以我觉得他很少会漏掉我的信息。"
    me "嗯~那难道说，他把手机忘在了家里吗！"
    extend "\n如果真是这样，那等他回家后肯定会……。"
    show tubasa 20 with dissolve
    tubasa "今天早上，我看见友君在摆弄手机。"
    extend "\n所以应该不会是忘在了家里……。"
    me "唔，唔嗯……。"
    show tubasa 21 with dissolve
    tubasa "……怎么办啊……我……。"
    extend "\n给他看了那样的照片……如果，被他讨厌了的话……。"
    "翼的眼睛里，浮现出泪水。"
    me "没，没事的！"
    extend "\n你看，忍不也说友不会讨厌的吗。"
    show tubasa 27 with dissolve
    tubasa "但是……但是……。"
    me "再等等吧。"
    extend "\n没事的！"
    extend "\n所以，好了……别哭了。"
    "我看到翼哭泣的样子，就再也忍不下去了，想要抱住他。"
    extend "\n但是，翼拒绝了我，粗暴地擦干眼泪，看向我这边。"
    play sound "fx/cute.ogg"
    $ renpy.transition(Quake(60, 0, 0.1, 0.15), layer='master')
    show tubasa 18 with dissolve
    tubasa "我，我才没有哭呢！"
    extend "\n只，只是夕阳有点耀眼……那个……。"
    stop music fadeout 1.5
    show tubasa 27 with dissolve
    extend "\n呜呜……呜呜……。"
    window hide
    play music "good_atmosphere.ogg"
    show cg evening at center with Dissolve(0.7)
    window show
    "……他真的很喜欢友君啊……。"
    extend "\n不然的话，不会哭得这么伤心的。"
    extend "\n但是，他还是隐瞒了这件事，果然他也是个男孩子。"
    me "没事没事。"
    extend "\n你很喜欢友君吧？"
    extend "\n那就得相信他才行，对吧？"
    window hide
    hide cg with Dissolve(0.6)
    hide tubasa with Dissolve(0.6)
    show tubasa 26 at top with dissolve
    window show
    tubasa "呜呜，呜呜……。"
    me "好了，别哭哭啼啼的！"
    extend "\n相信友君吧！"
    extend "\n一味地往坏处想的话，事情可不会因此就好转哦。"
    show tubasa 20 with dissolve
    tubasa "……嗯……是……这样啊。"
    extend "\n我也得相信……得相信友君才行！"
    show tubasa 23 with dissolve
    extend "\n那，那个，我去厕所洗把脸。"
    extend "\n对不起，你等我一下。"
    window hide
    play sound "fx/running.ogg"
    hide tubasa with dissolve
    window show
    "翼边说边跑向厕所。"
    "真是个好孩子啊。"
    show cg adult at center with dissolve
    extend "\n真想和他谈恋爱，好好疼爱他……。"
    stop music fadeout 0.3
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(50, 50, 0.07, 0.06), layer='master')
    "……我脑子有病吗。"
    extend "\n我到底在想什么啊！！"
    extend "\n只是看到一个哭泣的男孩，就兴奋起来了……。"
    window hide
    play music "tubasa_theme.ogg"
    show cg blue
    show tubasa 31 at top with Dissolve(0.2)
    window show
    "翼不仅长得可爱，而且还是个让人想要疼爱的孩子。"
    extend "\n但是，即便如此，我也不能对翼抱有爱意……。"
    me "不行不行！"
    extend "\n而且我可是翼的朋友。"
    window hide
    hide tubasa with dissolve
    hide cg with dissolve
    window show
    "我一边自言自语，一边思考着这些，翼回来了。"
    window hide
    show cg c42 1 at center with Radial(0.5)
    window show
    tubasa "[player_name]君！友给我回信息了！！"
    extend "\n[player_name]君说的没错，友只是刚好没看到而已。"
    tubasa "友说我穿这套衣服很适合，很可爱……！"
    extend "\n太好了……真是太好了……。"
    me "……是，是吗~太好了！"
    extend "\n你看，凡事不要那么悲观嘛。"
    show cg c42 2 with dissolve
    tubasa "嗯……真的。"
    extend "\n[player_name]君说得没错。"
    tubasa "……总感觉，[player_name]君一直在给我加油打气……。"
    extend "\n要是我一个人的话，说不定早就被不安击溃了。"
    extend "\n真的非常感谢。\n这份恩情我一定会还的。"
    me "不用谢啦。\n我只是喜欢才做这种事的！"
    extend "\n比起这个，以后也继续加油吧。"
    extend "\n翼的恋爱，道阻且长呢~！"
    show cg c42 1 with dissolve
    tubasa "好的！"
    extend "\n但是，[player_name]君在的话，就一定没问题的。"
    "看到翼的笑容，我感觉一阵内疚。"
    "对啊……我这种人是不能干涉初中生恋爱的。"
    extend "\n我最终只能作为局外人去守望他们。"
    window hide
    hide cg with Dissolve(0.8)
    window show
    "……。"
    extend "\n但是，"
    window hide
    show tubasa 36 at top with dissolve
    window show
    tubasa "那么，回去吧，[player_name]君。"
    show cg evening at center with dissolve
    "看到这样的笑容，让我觉得自己的想法动摇了。"
    extend "\n这种感觉"
    stop music fadeout 1.0
    window hide
    hide tubasa with Dissolve(1.0)
    hide cg with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    pause 0.4
    show bg living_room_night at center with Radial(1.0)
    play music "nostalgia.ogg"
    window show
    me "我回来了~。"
    mother "欢迎回来~。"
    extend "\n今天回来的有点晚啊。"
    me "嗯。"
    extend "\n御咲站往学校反方向走了一段，在咖啡店参观了一下。"
    mother "哦，是这样啊。"
    extend "\n不过那里晚上很危险的，不要玩到太晚哦。"
    me "我知道。毕竟我已经不是第一次去了。"
    extend "\n呼~今天也好开心啊。"
    play sound "fx/beer.ogg"
    "我慢慢地从冰箱里取出罐装啤酒，打开了盖子。"
    "噗。"
    mother "喂，等一下！！[player_name]！？\n为什么要喝啤酒！！"
    extend "\n你，还是未成年人吧！。"
    play sound "fx/boing.ogg"
    me "啊！！"
    "糟了！！不小心就养成平时的习惯了……。"
    me "啊，啊哈哈。\n抱歉抱歉。"
    extend "我搞错了，以为这是果汁。\n啊哈哈哈。"
    "我干笑着掩饰过去了。"
    mother "真是的……"
    extend "\n你将来也想成为爸爸那样的\n一回家就开瓶大口喝啤酒的酒鬼吗？"
    extend "\n我可不要啊~"
    me "会，会那样吗~\n啊哈哈哈……。"
    "总，总算蒙混过去了。好险好险。"
    "在学校里说话也要注意点才好……。"
    return

label day2_layout_sinobu:
    stop music fadeout 0.5
    window show
    me "忍君，像个女孩子一样可爱呢！"
    extend "\n哎呀~真是让我大饱眼福了！！"
    window hide
    play music "sinobu_theme.ogg"
    show sinobu 4 at top with dissolve
    window show
    sinobu "……。"
    me "我之前就有这样的感觉~。"
    extend "\n看起来也不像男孩子，女装一定很适合你！"
    show sinobu 27 with dissolve
    sinobu "……。"
    me "那个……忍君？"
    show sinobu 4 with dissolve
    sinobu "……。"
    show sinobu 30 with dissolve
    stop music fadeout 0.5
    play sound "fx/wind_slash.ogg"
    extend "\n……就算你这么说，我也不会高兴的。"
    "说完，忍背过了身。"
    hide sinobu with dissolve
    show tubasa 17 at topright with dissolve
    tubasa "忍，忍君？"
    show sinobu 20 at topleft with dissolve
    sinobu "……总觉得今天好累啊。"
    extend "\n不好意思，我先回去了。"
    extend "\n明天见。"
    me "诶！"
    extend "\n那个……忍君！！"
    play sound "fx/running.ogg"
    hide sinobu with dissolve
    "好像没听到我的声音，忍离开了咖啡店。"
    "难道惹他生气了？"
    extend "\n不会吧……这种时候，应该脸红害羞才对吧……。"
    "面对预料外的事态，我开始心急如焚。"
    "刚刚我说的话有那么糟糕吗？"
    extend "\n快想想快想想……。"
    hide tubasa with dissolve
    hide bg with dissolve
    "啊……"
    window hide
    show bg gym_backside at center
    show tomo 31 at top with FadeWhite(1.0)
    window show
    tomo "你看\n忍受欢迎也是可以理解的吧~。"
    extend "\n他乍一看就像个女孩子一样……"
    show tomo 7 with dissolve
    extend "啊，不过，\n他本人非常在意这件事，还是不说为妙。"
    window hide
    stop sound fadeout 0.5
    hide bg with FadeWhite(1.0)
    hide tomo with FadeWhite(1.0)
    play music "serious.ogg"
    show bg meffen_cafe_evening at center with dissolve
    $ renpy.transition(Quake(0, 100, 0.1, 0.065), layer='master')
    play sound "fx/break.ogg"
    window show
    "搞砸了……。"
    extend "\n我到底做了什么啊……！"
    window hide
    show tubasa 23 at top with dissolve
    window show
    tubasa "忍君，到底怎么了呢……。"
    me "怎么办……我……并不是那个意思……。"
    "就是啊……昨天不是才说过吗！"
    extend "\n男生被人说像女孩子会高兴吗？"
    extend "\n更何况，忍自己还对这种说法非常介意！！"
    me "我去追忍。"
    show tubasa 21 with dissolve
    tubasa "诶！？"
    me "翼，不必担心，在这里享受下午茶吧。"
    extend "\n另外……记得取消我们点的套餐。"
    extend "\n那么，我先走了！"
    show tubasa 8 with dissolve
    tubasa "诶诶……啊啊……好的，我知道了。"
    window hide
    hide tubasa with dissolve
    hide bg with dissolve
    play sound "fx/door_open.ogg"
    show bg meffen_cafe_hallway at center with dissolve
    pause 0.4
    play sound "fx/running.ogg"
    show bg downtown_evening with FadeBlack(0.5)
    window show
    "我离开咖啡店，顺着来路跑了起来。"
    "25岁了，为什么还不能考虑到对方的心情……。"
    extend "\n忍……抱歉，对不起！"
    "我忘我地奔跑着，在视野的一角，一个男孩映入眼帘。"
    window hide
    stop music fadeout 0.5
    play sound "fx/running.ogg"
    show bg park_walkway with FadeWhite(0.5)
    pause 0.3
    window show
    me "忍！！！"
    show sinobu 5 at top with Dissolve(0.8)
    sinobu "[player_surname]君……"
    "忍转过头来。"
    me "哈啊……哈啊……还好你没有离我太远……。"
    show sinobu 20 with dissolve
    sinobu "……你是特意跑过来的吗？"
    me "是的……。"
    me "我！"
    extend "\n说了些伤害忍的话……"
    extend "\n做了一些没有分寸的事……"
    extend "\n所以我想向你道歉……！"
    me "真的……真的很抱歉！！！！"
    "我深深地低下头。"
    show sinobu 3 with dissolve
    sinobu "……。"
    extend "\n[player_surname]君，抬起头来。"
    extend "\n我其实……并没有生气。"
    me "但是……对不起！！"
    extend "\n我应该要更多地考虑忍的心情后再行动。"
    extend "\n好好地思考一下，这种事情……"
    show sinobu 1 with dissolve
    sinobu "……。"
    me "只是……那是我最真实的感想。"
    extend "\n虽然希望不要产生误解，不过比喻有点不恰当……"
    extend "\n并不是想捉弄，或者瞧不起忍的意思，而是看到忍穿着女仆装，\n我真的被打动了。"
    show sinobu 3 with dissolve
    sinobu "……。"
    extend "\n那么，你就试试换种说法。告诉我，"
    extend "\n[player_surname]君对我所抱有的感情是什么样的。"
    "……。"
    window hide
    hide sinobu with dissolve
    play music "good_scene.ogg"
    show bg evening with dissolve
    window show
    me "……忍你很了不起哦……。"
    extend "\n学习也很优秀，空手道也很厉害，容貌……不对，\n做事认真又老实，也深得大家的信任。"
    extend "\n这样的忍，即使穿上女仆装也是那么的威风凛凛……"
    sinobu "……。"
    me "真是太棒了……。"
    "……。"
    window hide
    show bg park_walkway with dissolve
    show sinobu 21 at top with dissolve
    window show
    sinobu "呵呵……这句话听起来倒还可以。"
    me "忍……。"
    "看到忍的微笑，我的紧张也缓和了。"
    show sinobu 34 with dissolve
    sinobu "我所憧憬的，是坚强，正直，坚韧，\n守护重要的人……。"
    extend "\n为了成为那样的人，我正在以自己的方式努力。"
    show sinobu 20 with dissolve
    sinobu "可是，只要照镜子，映入眼帘的就不是理想中的自己。"
    extend "\n所以……我实在不想去关注自己的容貌。"
    show sinobu 27 with dissolve
    sinobu "所以……刚才我一气之下就离开了。"
    extend "\n平时的话还能勉强控制，但今天实在是……"
    "就算他人觉得好看，自己也未必会喜欢。"
    extend "\n反之亦然……。"
    me "忍。"
    extend "无论你的外表如何，\n我都看得到，你拥有一颗和理想中一样纯洁的灵魂。"
    show sinobu 18 with dissolve
    sinobu "……谢谢你。"
    extend "\n我还是第一次听到有人这样对我说。"
    show sinobu 34 with dissolve
    sinobu "[player_surname]君觉得我是那样的人。"
    extend "\n所以，我已经不生气也不伤心了。"
    show sinobu 29 with dissolve
    extend "\n只觉得，非常开心。"
    me "……你居然能够如此轻易地原谅对方，\n真了不起啊，忍。"
    extend "\n就算是我赶到的时候，你也是强忍着心中的怒火，\n努力让自己保持平静吧。"
    show sinobu 28 with dissolve
    sinobu "！"
    show sinobu 20 with dissolve
    sinobu "……而且，当时我对自己无法原谅对方而感到焦躁。"
    extend "\n但如果原谅了对方，说不定我还是会无法原谅那样自己……。"
    show sinobu 26 with dissolve
    extend "\n[player_surname]君巧妙地化解了我们的困境。"
    show sinobu 15 with dissolve
    sinobu "所以说……。"
    "忍含糊其辞。"
    me "嗯？  怎么了？"
    show sinobu 13 with dissolve
    sinobu "[player_surname]君的话，那样子说我的话，就是那个……"
    stop music fadeout 2.0
    me "嗯"
    show sinobu 14 with dissolve
    sinobu "……说我“可爱”其实也可以的……。"
    extend "\n那个……通过刚才的，我也明白你是什么意思了。"
    me "忍……！！"
    window hide
    play sound "fx/cute.ogg"
    show cg c33 at center with FadeWhite(0.5)
    play music "sinobu_theme.ogg"
    window show
    "我不禁抱住了忍。"
    me "你啊~你真是一个好孩子啊！！"
    extend "\n好乖好乖！！！"
    sinobu "诶……等一下，不要贴得太紧！"
    extend "\n停，停下来……喂！不要摸我头啊。[player_name]。"
    "在我心中挣扎的忍可爱极了，让我忍不住想要抱紧他。"
    window hide
    hide sinobu with dissolve
    hide cg with dissolve
    show sinobu 15 at top with dissolve
    window show
    sinobu "真是的！"
    extend "\n……那我们就回刚才的咖啡厅吧。"
    extend "\n我们丢下了一之濑同学，\n也得向店里的工作人员道个谢。"
    "忍终于被我放开了，他说道。"
    me "嗯，就这么办！"
    extend "\n……啊，我和忍的蛋糕套餐，\n取消掉了。"
    show sinobu 21 with dissolve
    sinobu "没事的，不必在意。"
    extend "\n真是的……你虽然急忙地追赶我，\n但还挺冷静呢。"
    extend "\n呵呵……。"
    "啊，笑了。"
    "虽然不至于大笑，但微笑的他更可爱了。"
    extend "\n我想多看看他……但是，又不想让别人看到。"
    play sound "fx/boing.ogg"
    "哎，我在想什么呢。我自以为了不起吗。"
    show sinobu 1 with dissolve
    sinobu "……[player_name]？"
    play sound "fx/cute.ogg"
    me "呀！？"
    show sinobu 9 with dissolve
    sinobu "怎么了……？突然不说话。"
    extend "\n我不是在挖苦你，别因此伤心哦。"
    me "啊？啊，嗯！"
    extend "\n我才是，让你为我操心了。"
    extend "\n我只是稍微想了一下事情。"
    show sinobu 12 with dissolve
    sinobu "……这样啊。"
    extend "\n那么，走吧。"
    window hide
    hide sinobu with dissolve
    show bg evening with dissolve
    window show
    "我俩说着，往「美馨儿咖啡」走去了。"
    "……他不追问这一点也挺好的。"
    extend "\n和忍在一起，能平静下来呢……。"
    "怀着甜蜜的心情，我和忍回到咖啡店，"
    hide bg with dissolve
    stop music fadeout 2.0
    extend "\n在那里和等待着我的翼汇合，完成了布置组今天的任务。"
    window hide
    pause 0.4
    show bg living_room_night at center with Radial(1.0)
    play music "nostalgia.ogg"
    window show
    play sound "fx/door_open.ogg"
    me "我回来了~。"
    mother "欢迎回来~。"
    extend "\n今天回来的有点晚啊。"
    me "嗯。"
    extend "\n御咲站往学校反方向走了一段，在咖啡店参观了一下。"
    mother "哦，是这样啊。"
    extend "\n不过那里晚上很危险的，不要玩到太晚哦。"
    me "我知道。毕竟我已经不是第一次去了。"
    extend "\n呼~今天也好开心啊。"
    play sound "fx/beer.ogg"
    "我慢慢地从冰箱里取出罐装啤酒，打开了盖子。"
    "噗。"
    mother "喂，等一下！！[player_name]！？\n为什么要喝啤酒！！"
    extend "\n你，还是未成年人吧！。"
    play sound "fx/boing.ogg"
    me "啊！！"
    "糟了！！不小心就养成平时的习惯了……。"
    me "啊，啊哈哈。\n抱歉抱歉。"
    extend "我搞错了，以为这是果汁。\n啊哈哈哈。"
    "我干笑着掩饰过去了。"
    mother "真是的……"
    extend "\n你将来也想成为爸爸那样的\n一回家就开瓶大口喝啤酒的酒鬼吗？"
    extend "\n我可不要啊~"
    me "会，会那样吗~\n啊哈哈哈……。"
    "总，总算蒙混过去了。好险好险。"
    "在学校里说话也要注意点才好……。"
    return

label day2_cooking_tuki:
    show bg akamine_kitchen at center
    window show
    me "月，我来助你一臂之力！！"
    "我把书桌上的烹饪书卷起来，站在月的身旁。"
    window hide
    show tuki 19 at top with dissolve
    window show
    tuki "你快和空一起逃！！"
    extend "\n这里我一个人想办法……！"
    me "你在说什么呢！\n在战场上丢下少年，正太控听到后都要傻眼了！"
    extend "\n不管月说什么，我都要和你战斗到底。"
    extend "\n空已经出去了，你不用担心！！"
    show tuki 17 with dissolve
    tuki "是吗……\n那你就好好表现表现吧。"
    window hide
    show cg remarkable at center with dissolve
    window show
    tuki "正如你所见，对方不仅反应迅速，对声响也很敏感。"
    extend "\n慢慢将敌人逼到绝路的战法是行不通的"
    me "原来如此。\n也就是说必须一击必杀吗。"
    window hide
    hide tuki with dissolve
    hide cg with dissolve
    show tuki 8 at top with dissolve
    window show
    tuki "是的。"
    extend "\n但是，敌方只有一只，我方有两个人……必须要利用这优势。"
    extend "\n这里就采取前后夹击吧。\n我从右侧，[player_surname]君在左侧，数到3的同时发动攻击。"
    me "明白！！\n动作可不要慢了哦！"
    show tuki 18 with dissolve
    tuki "哼……真会说。"
    show tuki 7 with dissolve
    extend "\n那我要上了。\n一，二"
    stop music fadeout 0.5
    play sound "fx/wind_slash.ogg"
    hide bg with Dissolve(0.2)
    hide tuki with Dissolve(0.2)
    tuki "3！！！！"
    show cg remarkable at center with FadeWhite(0.5)
    $ renpy.transition(Quake(0, 70, 0.2, 0.06), layer='master')
    play sound "fx/punch.ogg"
    "啪嚓"
    "！？！？"
    play music "discovery.ogg"
    window hide
    show cg c60 with zoominout
    window show
    "被干掉的人是我。"
    "由于我手短，没能提前一步冲出去。"
    extend "\n留有退路的敌人迅速躲开了攻击，\n月的拖把向冲出去的我袭来。"
    me "咕嘿……好，好臭啊…。"
    tuki "对，对不起！！"
    extend "\n可恶……武器不同，时机也差了点。"
    stop music fadeout 2.0
    me "呜呜……这样下去的话，就算攻击了也会被躲开啊。\n到底该怎么做……。"
    show bg akamine_kitchen at center
    extend "\n我们，难道赢不了他吗……？"
    window hide
    hide cg with dissolve
    show tuki 18 at top with dissolve
    play music "japanebattle.ogg"
    window show
    tuki "我可不喜欢当窝囊废。"
    extend "\n无论身处什么状况，都要与对手对抗到底。"
    extend "\n如果时机不对，就攻击到时机对为止！"
    me "……噢！"
    extend "\n不愧是月，很男子汉，很帅气啊！"
    show tuki 7 with dissolve
    tuki "那种话等胜利后再说！"
    extend "\n要上了哦！\n一，二"
    play sound "fx/wind_slash.ogg"
    show cg remarkable at center with FadeWhite(0.5)
    hide bg
    hide tuki
    hide sora
    tuki "三！！！"
    $ renpy.transition(Quake(0, 70, 0.2, 0.06), layer='master')
    play sound "fx/punch2.ogg"
    "扑咚"
    show bg akamine_kitchen at center
    "月用拖把堵住了敌人逃跑的退路，\n但敌人迅速地迂回逃走了。"
    hide tuki with FadeWhite(0.5)
    hide cg with FadeWhite(0.5)
    me "可恶~太狡猾了……！！！"
    show tuki 19 at top with dissolve
    tuki "还没结束……还没放弃！"
    extend "\n我是赤峰家的长子！我一定会击败敌人的！！"
    hide tuki with dissolve
    window hide
    window show
    play sound "fx/sliding_door.ogg"
    "嘎啦"
    sora "哥哥！"
    "朝着声音的方向看去，"
    window hide
    play sound "fx/running.ogg"
    show sora 23 at topright with dissolve
    window show
    extend "是手拿着棒状的袋子的空。"
    show tuki 12 at topleft with dissolve
    tuki "空！？"
    extend "\n我不是让你先走吗！\n为什么要回来啊！？"
    show sora 10 with dissolve
    sora "是为了和哥哥一起战斗，一起前进！！\n"
    window hide
    play sound "fx/wind_slash.ogg"
    show cg c48 1 at center with FadeWhite(0.5)
    window show
    extend "把这个，收下！！"
    play sound "fx/impact_japanese.ogg"
    show cg c48 2 with FadeWhite(0.5)
    tuki "这是……。"
    extend "\n空，感谢你！"
    extend "\n正好我想要这个呢！！"
    "月接住了的东西，"
    extend "是一把竹刀！"
    play sound "fx/boing.ogg"
    me "不应该拿杀虫剂吗！？\n为什么是竹刀！！？"
    sora "赤峰家代代都是武士。"
    extend "\n手持长刀，将自身流派发展到极致的先祖们创立了道场，\n将其命名为赤峰道场，将剑术传承到了后世。"
    extend "\n当背负着赤峰之名的我们面对敌人时，手上要拿着刀！"
    tuki "没错，模拟刀的竹刀，能让我们发挥出最大的力量。"
    extend "\n手持武士刀的武士，就像他的刀锋一样，用刀背保护同伴，\n刀刃则只面向敌人，而且必胜无疑。"
    extend "\n这就是赤峰家流武士的信念！！"
    hide bg
    hide tuki
    hide sora
    tuki "[player_surname]，你给我把拖把拿过来……。\n这样东西正好适合当武器。"
    extend "\n上！\n呜哦哦哦！！！"
    show cg remarkable with Radial(0.5)
    play sound "fx/explosion2.ogg"
    "我和拿着竹刀的月，气势汹汹地攻击蜘蛛！"
    $ renpy.transition(Quake(0, 70, 0.2, 0.06), layer='master')
    play sound "fx/dash.ogg"
    "虽然蜘蛛勉强避开了拖把，但最终还是成了月竹刀下的亡魂。"
    window hide
    play sound "fx/sparkle.ogg"
    show cg c52 with Dissolve(2.0)
    window show
    tuki "……你可别怪我。"
    extend "\n我有自己的必须保护的人。"
    "……那个，这是什么电视剧吗？"
    stop music fadeout 2.0
    window hide
    hide bg with Dissolve(1.5)
    hide sora with Dissolve(1.5)
    hide cg with Dissolve(1.5)
    hide tuki with Dissolve(1.5)
    show bg akamine_kitchen at center with dissolve
    play music "twins_theme.ogg"
    show tuki 4 at top with dissolve
    window show
    tuki "[player_surname]，我得好好感谢你的帮助。"
    extend "\n多亏了你，我们才能成功获胜。"
    me "不，不是的，说到底击败对方的还是月……。"
    show tuki 18 with dissolve
    tuki "别因为结果而忽略了过程。"
    extend "\n没有那些帮助者，就不会有胜利的结局。"
    extend "\n别因为自己的表现而妄自菲薄。"
    show tuki 4 with dissolve
    tuki "[player_surname]我对你刮目相看了哦。"
    "……呃，我们，刚才不还在考虑菜单吗……。"
    extend "\n这是什么气氛，仿佛刚刚经历了赌上性命的决斗一样！？"
    hide tuki with dissolve
    window hide
    show sora 3 at topright with dissolve
    window show
    sora "对了！\n[player_name]君，要不要到我们道场练习？"
    extend "\n一定会变得比现在更加强大的！！"
    show tuki 15 at topleft with dissolve
    tuki "嗯，这个建议不错。"
    extend "\n让我们一同锻炼身心吧。"
    me "啊，哈哈……不是的~感谢你的邀请，但是，\n我已经在别的道场练习了……！"
    extend "\n我觉得，赤峰道场对我来档次有些太高了~。"
    show tuki 6 with dissolve
    tuki "嚯嚯，哪一个道场？"
    extend "\n从刚才你的动作来看，应该不只是空手道吧？"
    show sora 4 with dissolve
    sora "这附近的道场，也只有我家的剑道场了呢~。"
    extend "\n你的动作到底是从哪里学来的啊，我很想知道……。"
    "诶……为什么话题突然就变成这个样子了？？"
    play sound "fx/cute.ogg"
    $ renpy.transition(Quake(0, 80, 0.15, 0.1), layer='master')
    extend "\n这，这个，不是在说如何消灭蜘蛛的吗！？"
    extend "\n对方是蜘蛛，而舞台就是厨房对吧！！？"
    return

label day2_cooking_sora:
    show bg akamine_kitchen at center
    window show
    me "空，冷静一下！"
    extend "\n这里就交给月，总之我们先离开这里！"
    "我抓住了正在四处逃窜的空，然后拉着他的手走出了厨房。"
    play sound "fx/running.ogg"
    stop music fadeout 0.5
    window hide
    hide bg with dissolve
    play music "fx/tsubame.ogg"
    show bg akamine_house2_evening with dissolve
    window show
    sora "……呜呜……呜呜。"
    "虽然空已经恢复冷静了，但是身体却还在轻微地颤抖。"
    "虽然不合时宜，但是我看着空这副模样，突然觉得他好可爱。"
    "为了让空冷静下来，我温柔地抱住空，然后轻轻地抚摸他的后背。"
    extend "\n然后，空的颤抖也逐渐平息了，没过多久，就冷静下来了。"
    window hide
    show sora 9 at top with dissolve
    window show
    sora "呜哇……好可怕……。"
    me "好了好了，已经没事了。"
    extend "\n这里的话你大可放心的哦。"
    show sora 20 with dissolve
    sora "呜呜……对不起，让你看见我这副丢人的样子了。"
    extend "\n我，我实在是害怕蜘蛛啊……。"
    me "那也是没办法的啊。"
    extend "\n虽然我对虫子没什么感觉，但是，刚才那样的话我也会被吓到的啊。"
    show sora 18 with dissolve
    sora "哈啊……呼……。"
    show sora 33 with dissolve
    extend "\n唔嗯……已经冷静不少了……。"
    me "话说回来，哭得这么厉害的空君也很可爱啊~。"
    extend "\n没想到你居然会慌张成这样。"
    show sora 27 with dissolve
    sora "真是的！别，别嘲笑我了。"
    extend "\n因为，我还是第一次看到这么大的东西呢……。"
    play sound "fx/cute2.ogg"
    "这句台词，是不是有点下流？"
    show sora 25 with dissolve
    sora "……不过，还是谢谢你救了我。"
    me "没事没事，不用客气。"
    extend "\n拯救可爱的小男生，可是身为正太控的我理所应当要做的事！"
    show sora 14 with dissolve
    sora "你在说什么啊……。"
    me "嗯……月君的情况也挺让人在意的。"
    extend "\n……他没事吧？"
    stop music fadeout 0.5
    window hide
    play music "fx/wind.ogg"
    show cg akamine_kitchen_red at center with FadeWhite(0.5)
    window show
    show sora 23 with dissolve
    sora "啊，对了！"
    extend "哥哥还在厨房里……。"
    show sora 18 with dissolve
    extend "\n怎，怎么办啊……虽然很担心他，但回去之后又……。\n呜呜……。"
    show sora 13 with dissolve
    sora "……。"
    show sora 22 with dissolve
    stop music fadeout 0.5
    window hide
    hide cg with FadeWhite(0.5)
    window show
    sora "……不对！"
    play music "japanebattle.ogg"
    extend "\n哥哥正在战斗，身为弟弟的我怎么可以逃跑！"
    show sora 17 with dissolve
    extend "\n不能给赤峰家的二少爷丢脸！"
    hide sora with dissolve
    play sound "fx/wind_slash.ogg"
    "这么说着，空气势十足地站起身来。"
    window hide
    show sora 22 at top with dissolve
    window show
    sora "[player_name]君就在这里等我吧！"
    extend "\n我去救他回来！"
    me "诶，诶诶？！"
    extend "\n但是，究竟该怎么……？"
    play sound "fx/running.ogg"
    hide sora with dissolve
    "空没有回答我的问题，而是朝着厨房走去。"
    me "喂，我也要一起去！！"
    play sound "fx/running.ogg"
    window hide
    hide bg with dissolve
    show bg akamine_kitchen at center with dissolve
    show tuki 19 at top with Dissolve(0.8)
    window show
    tuki "可恶，挺能干的嘛……\n用不惯的拖把是打不倒那家伙的……。"
    extend "\n但是，要是放跑这家伙的话，空会再次陷入危险……。"
    extend "\n这种时候要是有那个就好了……！"
    hide tuki with dissolve
    play sound "fx/fall_down.ogg"
    show sora 23 at topright with dissolve
    sora "哥哥！"
    show tuki 12 at topleft with dissolve
    tuki "空！？"
    extend "\n我不是让你先走吗！\n为什么要回来啊！？"
    show sora 10 with dissolve
    sora "是为了和哥哥一起战斗，一起前进！！"
    window hide
    play sound "fx/wind_slash.ogg"
    show cg c48 1 at center with FadeWhite(0.5)
    window show
    extend "把这个，收下！！"
    play sound "fx/impact_japanese.ogg"
    show cg c48 2 with FadeWhite(0.5)
    tuki "这个是……。"
    extend "\n空，感谢你！"
    extend "\n正好我想要这个呢！！"
    "月接住了的东西，"
    extend "是一把竹刀！"
    play sound "fx/boing.ogg"
    me "不应该拿杀虫剂吗！？\n为什么是竹刀！！？"
    sora "赤峰家代代都是武士。"
    extend "\n手持长刀，将自身流派发展到极致的先祖们创立了道场，\n将其命名为赤峰道场，将剑术传承到了后世。"
    extend "\n当背负着赤峰之名的我们面对敌人时，手上要拿着刀！"
    tuki "没错，模拟刀的竹刀，能让我们发挥出最大的力量。"
    extend "\n手持武士刀的武士，就像他的刀锋一样，用刀背保护同伴，\n刀刃则只面向敌人，而且必胜无疑。"
    extend "\n这就是赤峰家流武士的信念！！"
    tuki "呜哦哦哦哦！！！！！"
    show cg remarkable with Radial(0.5)
    play sound "fx/explosion2.ogg"
    "月握着竹刀，气势汹汹地向蜘蛛刺去！"
    window hide
    play sound "fx/sparkle.ogg"
    show cg c52 with Dissolve(2.0)
    window show
    tuki "……你可别怪我。"
    extend "\n我有自己的必须保护的人。"
    "……那个，这是什么电视剧吗？"
    stop music fadeout 2.0
    window hide
    hide bg with Dissolve(1.5)
    hide sora with Dissolve(1.5)
    hide cg with Dissolve(1.5)
    hide tuki with Dissolve(1.5)
    show bg akamine_kitchen at center with dissolve
    play music "twins_theme.ogg"
    show sora 24 at topright
    show tuki 9 at topleft with dissolve
    window show
    tuki "空，谢谢你。"
    extend "\n多亏了你，我们才能成功获胜。"
    show sora 32 with dissolve
    sora "没事……我相信哥哥一定能赢。"
    "……呃，我们，刚才不还在考虑菜单吗……。"
    extend "\n这是什么气氛，仿佛刚刚经历了赌上性命的决斗一样！？"
    show sora 3 with dissolve
    sora "我能够帮上哥哥的忙，[player_name]君也帮了大忙了。"
    extend "\n[player_name]君不在的话，我一定会慌张失措，\n不可能冷静地做出那样的判断的。"
    show tuki 18 with dissolve
    tuki "是这样啊……[player_surname]君，非常感谢。"
    extend "\n谢谢你帮助了空，也顺便救了我。"
    me "没，没有啦~我什么都没做……。"
    show tuki 15 with dissolve
    tuki "没那回事。"
    extend "\n要是你不在的话，我或许会输掉这场战斗。"
    extend "\n这是在场所有人的胜利。"
    play sound "fx/cute.ogg"
    $ renpy.transition(Quake(0, 80, 0.15, 0.1), layer='master')
    "所，所以说，这个是关于杀死蜘蛛的话题吧！？"
    extend "\n对方是蜘蛛，而舞台就是厨房对吧！！？"
    return

label day2_supply_sakuya:
    stop music fadeout 0.5
    window show
    me "作哉君！\n我也能和你一起去吗？"
    window hide
    play music "sakuya_theme.ogg"
    show sakuya 10 at top with dissolve
    window show
    sakuya "嗯？可以是可以……。"
    show sakuya 5 with dissolve
    extend "\n不，嗯……不如说，你跟着来吧。\n有很多事想教给你。"
    "『有很多事想教给你』……？"
    show cg adult at center with FadeWhite(0.5)
    play sound "fx/wow2.ogg"
    extend "\n很多事……难道说，这个带刺的现代少年，\n要带我这个单纯的、不懂那些不堪之事的人见识大人的世界吗！？"
    "这，这真是，令人浮想联翩啊！！！"
    hide saburo with dissolve
    hide cg with dissolve
    hide sakuya with dissolve
    me "那，那就这么决定了！！"
    extend "\n那三朗君！明天见了！！！"
    show saburo 6 at top with dissolve
    saburo "诶~好像很起劲呢。"
    extend "\n如果你们两个要玩的话，我也想和你们一起玩啦……。"
    show saburo 5 with dissolve
    extend "\n不，今天就算了！！\n那么，再见啦~！"
    play sound "fx/running.ogg"
    hide saburo with dissolve
    "我和三朗道别后，和作哉一起动了起来。"
    window hide
    hide bg with dissolve
    show bg residential_area at center with dissolve
    show sakuya 19 at top with dissolve
    window show
    sakuya "呼……那家伙回去了啊。"
    extend "\n太好了。"
    play sound "fx/cute2.ogg"
    "嗯，嗯嗯，就是说啊！！"
    extend "不是两人单独在一起的话就不太妙了！！！"
    me "那，那，你们到底要去哪儿啊？"
    show sakuya 5 with dissolve
    sakuya "宠物店。\n去买小翼的饵食。"
    me "诶？"
    show sakuya 23 with dissolve
    sakuya "诶？"
    show cg dark at center with Dissolve(0.2)
    play sound "fx/triangle.ogg"
    "……。"
    window hide
    hide cg with dissolve
    hide sakuya with dissolve
    window show
    me "……啊，啊~原来如此。"
    extend "\n作哉君，真的是非常喜欢小翼啊。"
    show sakuya 25 at top with dissolve
    sakuya "那还用说。"
    extend "\n小翼是我喜欢的狗狗……我当然会想要好好疼爱他。"
    "说的也是啊……这终究只是一场妄想……但是我还是想再梦下去啊！！"
    play sound "fx/explosion2.ogg"
    extend "\n啊啊，作哉深爱着的小翼，我好嫉妒你啊！！！"
    me "啊哈哈。"
    extend "\n这么一说，就像是在说一之濑翼一样啊。"
    show cg remarkable at center with FadeWhite(0.5)
    play sound "fx/punch2.ogg"
    "啪！！！"
    window hide
    hide cg with dissolve
    hide sakuya with dissolve
    show sakuya 27 at top with dissolve
    window show
    sakuya "看我不把你打飞！！"
    me "……你已经打过了……。"
    show sakuya 19 with dissolve
    sakuya "哼！自作自受。"
    me "……呜呜……。"
    extend "\n我说啊，作哉。"
    extend "\n为什么你会把翼当成眼中钉呢？"
    show sakuya 6 with dissolve
    sakuya "……我可没有。"
    me "骗人。"
    extend "\n因为你在面对其他男孩的时候，态度明显就不一样。"
    show sakuya 30 with dissolve
    sakuya "……烦死了……你什么都不知道。"
    me "诶？"
    show sakuya 26 with dissolve
    sakuya "不，不，没什么！！"
    show sakuya 20 with dissolve
    sakuya "总之，我才没有把他当成眼中钉！"
    extend "\n这个……该怎么说呢，我也不知道。\n就自然地就变成那样了！"
    show sakuya 1 with dissolve
    extend "所以，我也没办法啊！"
    me "自然……什么意思？"
    show sakuya 2 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sakuya "啊真是的，麻烦死了！！"
    extend "\n随便你怎么说吧。"
    extend "\n这个话题已经结束了！"
    extend "\n敢再提我就揍你！！"
    show cg sky at center with dissolve
    "作哉强行结束了对话，并且之后再也没有提过这个话题。"
    "呜呜……这个话题是禁忌么。"
    extend "\n谈吐自然而然的冷淡，并不是代表作哉就是个虐待狂。\n可怜的翼依然对他的责难不明所以……。"
    "一边想着这些事，一边到了宠物店。"
    window hide
    stop music fadeout 2.0
    hide sakuya with dissolve
    hide cg with dissolve
    hide bg with dissolve
    play sound "fx/crowd_noise.ogg"
    show bg pet_shop at center with dissolve
    window show
    "一进到店里，笼子里的各种动物映入眼帘。"
    extend "\n有点独特的味道啊……。"
    extend "\n对于不怎么和动物打交道的我来说很新鲜。"
    "作哉熟门熟路地走进了店内。"
    extend "\n跟着他走进了放有狗食的地方。"
    window hide
    window show
    me "诶~。各种各样的啊。"
    show sakuya 5 at top with dissolve
    sakuya "对。"
    extend "\n当然要认真阅读包装袋上的说明，\n最好也去网上查一下，看看是出于什么目的制作的。"
    extend "\n不然有可能对狗的身体不好。"
    me "原来是这样啊……"
    extend "\n我啊，会综合考虑包装袋的可爱程度和名气，来选让狗狗开心的肉食。"
    show sakuya 12 with dissolve
    sakuya "这样做的话，营养不均衡，狗狗会生病的。"
    show sakuya 5 with dissolve
    extend "\n接着，给小翼买这款狗粮……"
    extend "\n对了，去看看新的项圈吧。"
    me "都做到这份上了，你还不如把小翼养在家里呢。"
    hide sakuya with dissolve
    "（抖）"
    "作哉听到我的话后停了下来。"
    extend "\n……咦？我说了什么不该说的话吗？？"
    window hide
    play sound "fx/crowd_noise.ogg"
    show sakuya 7 at top with dissolve
    window show
    sakuya "……是啊。"
    play sound "fx/running.ogg"
    hide sakuya with dissolve
    "作哉说完后，又向其他地方走去。"
    "我有些在意作哉的反应，"
    extend "\n但是一直缠着他的话，他应该会讨厌的，\n于是决定去笼子里看看小狗和小猫。"
    window hide
    hide bg with dissolve
    play sound "fx/sparkle.ogg"
    show bg adult at center with Radial(0.5)
    play music "cute_silly.ogg"
    window show
    "汪汪！"
    extend "\n喵喵！"
    play sound "fx/cute.ogg"
    me "呜哇~……好可爱啊！"
    "那里有很多的小狗和小猫。"
    "虽然我对动物没什么兴趣，但是可爱的东西还是很可爱的！！"
    extend "\n而且不仅是人，为什么无论什么动物幼年时期都会这么可爱呢？"
    play sound "fx/cute3.ogg"
    me "毛茸茸的~。"
    extend "\n啊哈哈，这只小猫睡得真香~。"
    extend "\n嗯？这只小猫真精神啊~。"
    "同样的狗狗，性格也是不一样的。"
    me "要是能早点找到一个好饲主就好了。"
    window hide
    show bg pet_shop with dissolve
    show sakuya 5 at top with dissolve
    window show
    sakuya "哦，你在这里啊。"
    "我对着笼子一个人自言自语的时候，\n买完东西的作哉提着塑料袋过来了。"
    stop music fadeout 5.0
    show sakuya 21 with dissolve
    sakuya "这些小狗真的都好可爱啊…。"
    me "嗯，看着它们就感觉好安心~。"
    show sakuya 22 with dissolve
    sakuya "……我家以前养的狗，也是从这个笼子里出来的。"
    me "啊，原来是这样。"
    window hide
    play music "good_atmosphere.ogg"
    show cg c78 at center with FadeWhite(0.5)
    window show
    sakuya "它还很健康的时候，总是像这些孩子一样闹腾。"
    extend "\n我因此放下心来，没有注意到它的异样。"
    extend "\n……我可从没想过，它会因为生病去世。\n它当时明明才7岁啊。"
    me "……。"
    sakuya "归根结底，这都是我的错。"
    extend "\n都是因为我用半吊子的知识抚养它，所以它才会生病……。"
    extend "\n所以，虽然这不能算是补偿，"
    extend "但是为了防止这种情况再次发生，\n我就想让小翼很健康地长大……。"
    "作哉说到这里，双眼开始泛起泪光。"
    extend "\n我并不知道该对他说些什么。"
    extend "\n只能呆呆地看着他。"
    hide cg with dissolve
    hide sakuya with dissolve
    show sakuya 7 at top with dissolve
    sakuya "……啊，抱，抱歉！"
    extend "\n我有些太阴沉了。"
    extend "\n我先出门了，\n你看着那些家伙，直到你心满意足吧。"
    play sound "fx/running.ogg"
    hide sakuya with dissolve
    "说完，作哉小跑着离开了店里。"
    extend "\n我本想给他点独自思考的时间，\n但看着作哉的样子，我实在是无法在原地呆下去，就追了上去。"
    window hide
    play sound "fx/running.ogg"
    hide bg with dissolve
    show bg residential_area_evening at center with Dissolve(0.8)
    window show
    "作哉站在店的前面。"
    me "作哉……没事吧？"
    show sakuya 24 at top with dissolve
    sakuya "嗯……哦，已经出来了。"
    extend "\n我有点……抱歉啊。你难得被可爱的动物治愈了。"
    extend "\n一回想起来，我就停不住嘴了。\n哈哈…。"
    "作哉的脸上虽然在笑着，但声音却有些鼻音。"
    show sakuya 26 with dissolve
    sakuya "……嘛，顺带一提，让我再多说一句，"
    extend "\n我的家人也因为过于溺爱的爱犬过世了，受到了很大的打击，\n以至于说再也不想养狗了。"
    show sakuya 21 with dissolve
    sakuya "所以，我才会在教学楼的后面偷偷地养小翼。"
    me "……原来如此，是这样啊。"
    extend "\n难不成是因为我说了‘你还不如把小翼养在家里呢’，你就想起这件事来了……？"
    show sakuya 25 with dissolve
    sakuya "不不，才没这种事啦。"
    extend "\n你没有那么大的影响力，所以不用放在心上。"
    "……。"
    me "……作哉。"
    extend "\n能不能也让我帮忙照顾小翼呢？"
    show sakuya 31 with dissolve
    sakuya "哎……。"
    me "我……怎么说呢，\n看到作哉那么努力地照顾小翼的样子，我非常感动。"
    hide sakuya with dissolve
    window hide
    window show
    me "我完全不懂怎么照顾动物，\n对于照顾小翼来说，我可能帮不上什么忙。"
    extend "\n但是，对于作哉你，我应该能帮上一些忙。"
    extend "\n所以，即使是间接地帮助，我也想帮着照顾小翼。"
    me "我可以和你一起闲聊小翼的事，"
    extend "\n或者是在你想起过去的时候听听你讲讲，"
    extend "\n也可以直接和小翼玩。"
    extend "\n我想多少帮上一些忙……可以吗？"
    sakuya "……。\n"
    window hide
    show sakuya 25 at top with dissolve
    window show
    extend "怎么可能不行啊。"
    "作哉稍微思考了一下，然后这么说。"
    show sakuya 6 with dissolve
    sakuya "说，说起来！\n就算你没有说，我本来就是这么打算的！！"
    extend "\n所以我一开始也说了，我会教你很多。"
    extend "\n……来，这个。"
    "作哉递过一个塑料袋，里面装着狗粮。"
    show sakuya 10 with dissolve
    sakuya "这是很适合小翼的狗粮。"
    extend "\n给我记好了，以后就你来买了哦。"
    extend "\n要是搞错了，可不饶你哦。"
    me "啊哈哈，交给我吧！"
    extend "\n只是跑个腿而已，小事一桩。"
    show sakuya 20 with dissolve
    sakuya "而且，动物相关知识，我会亲自教你的，\n所以不只是对我而言，对小翼也是有很大帮助的！"
    extend "\n……知道了吗？"
    me "嗯，我知道了。"
    extend "\n我会努力记住的，请多关照。"
    extend "\n我们一起努力照顾小翼吧！"
    show sakuya 23 with dissolve
    sakuya "对。"
    extend "\n……"
    show sakuya 22 with dissolve
    extend "谢谢。"
    me "诶？"
    show sakuya 26 with dissolve
    sakuya "没事！"
    extend "\n好了，回家吧！！"
    show cg evening at center with dissolve
    "作哉的「谢谢」声音太小，以至于我下意识地反问了一句，\n不过他的话确实传进了我的耳中。"
    "虽然态度有点傲，但其实他本质还是很温柔的。"
    extend "\n我一边对一之濑翼说的话产生共鸣，一边踏上了回家的路。"
    stop music fadeout 1.5
    window hide
    hide sakuya with Dissolve(1.0)
    hide cg with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    pause 0.4
    show bg living_room_night at center with Radial(1.0)
    play music "nostalgia.ogg"
    window show
    play sound "fx/door_open.ogg"
    me "我回来了~。"
    mother "欢迎回来~。"
    extend "\n今天回来的有点晚啊。"
    me "嗯。"
    extend "\n我今天跟朋友出去玩了哦。"
    mother "哦，是这样啊。"
    extend "\n也别忘记写作业啊。"
    me "知道啦，我都这么大个人了。"
    extend "\n呼~今天也好开心啊。"
    play sound "fx/beer.ogg"
    "我慢慢地从冰箱里取出罐装啤酒，打开了盖子。"
    "噗。"
    mother "喂，等一下！！[player_name]！？"
    play sound "fx/boing.ogg"
    extend "为什么还要喝啤酒！！"
    extend "\n你，还是未成年人吧！。"
    me "啊！！"
    "糟了！！不小心就养成平时的习惯了……。"
    me "啊，啊哈哈。\n抱歉抱歉。"
    extend "我搞错了，以为这是果汁。\n啊哈哈哈。"
    "我干笑着掩饰过去了。"
    mother "真是的……"
    extend "\n你将来也想成为爸爸那样的\n一回家就开瓶大口喝啤酒的酒鬼吗？"
    extend "\n我可不要啊~"
    me "会，会那样吗~\n啊哈哈哈……。"
    "总，总算蒙混过去了。好险好险。"
    "在学校里说话也要注意点才好……。"
    return

label day2_supply_saburo:
    stop music fadeout 0.5
    window show
    me "三朗！\n我能和你一起去吗？"
    window hide
    play music "saburo_theme.ogg"
    show saburo 24 at top with dissolve
    window show
    saburo "诶……唔~好倒是好，"
    show saburo 19 with dissolve
    extend "\n不过这一次，[player_surname]君可能要硬硬的哦？"
    "三朗露出了大胆的笑容。"
    "能让我硬硬的地方？"
    extend "\n到底是要带我去哪里啊？"
    me "嗯，没关系的。"
    extend "\n只要是和三朗君在一起的话，去哪里都可以♪"
    show saburo 8 with dissolve
    saburo "那是什么……感觉怪恶心的。"
    hide saburo with dissolve
    show saburo 1 at topright with dissolve
    extend "\n那么穗海，我就和[player_surname]先走了。\n明天见。"
    show sakuya 5 at topleft with dissolve
    sakuya "哦，明天见。"
    "我与作哉分别，和三朗一起走。"
    window hide
    hide bg with dissolve
    hide saburo with dissolve
    hide sakuya with dissolve
    show bg downtown at center with dissolve
    window show
    me "所以，我们要去哪里？"
    show saburo 25 at top with dissolve
    saburo "去看黄书！"
    extend "\n因为我最近都没怎么去呢~。\n搞不好，最近有新刊出来了！！"
    "原来如此，是这样啊……。"
    extend "\n一定是被我那朴素的外表所骗了，\n觉得我是天真无邪的同龄少年吧。"
    play sound "fx/eureka.ogg"
    show cg remarkable at center with Dissolve(0.2)
    "天真啊……我可是25岁了啊！！"
    extend "\n黄段子和下流梗什么的早就已经听腻了！"
    window hide
    hide saburo with dissolve
    hide cg with dissolve
    window show
    me "嗯……？但是，我们还是未成年人啊。"
    extend "\n而且还是穿着制服，\n去成人商店没问题吗？"
    show saburo 2 at top with dissolve
    saburo "店本身又不是十八禁，没关系的！"
    extend "\n店员的检查也很宽松，我们又不买，\n没什么好担心的。"
    me "是，是吗……"
    show saburo 1 with dissolve
    saburo "哦！"
    show cg sky at center with dissolve
    extend "\n……到，到了。"
    extend "\n快，进去吧~！"
    play sound "fx/running.ogg"
    hide saburo with dissolve
    hide cg with dissolve
    hide saburo with dissolve
    hide bg with dissolve
    stop music fadeout 0.5
    "到达目的地后，三朗意气扬扬地走进了店里。"
    window hide
    play music "infiltration.ogg"
    show bg bookstore at center with Dissolve(1.0)
    window show
    "店里氛围和一般的书店不同，\n放置着一些小众的漫画和成人向杂志。"
    "三朗在那里面若无事地走了进去。"
    extend "\n然后，他拿起了一本书，一边淫荡地笑着一边开始站着看了起来。"
    "真是的，果然是男生啊……。"
    extend "\n我一边注意着三朗的股间反应，一边开始寻找自己喜欢的书。"
    "这种地方，也没有那种东西吗……"
    extend "\n就在我感到有些沮丧的时候，"
    play sound "fx/cute2.ogg"
    me "哦！这里也有啊！"
    "那里有我经常看的书。"
    extend "\n我一拿到书，就立刻走向三朗那里。"
    window hide
    window show
    me "三朗！"
    extend "\n你看这个♪"
    play sound "fx/paper.ogg"
    show cg remarkable at center with Dissolve(0.4)
    "我一边说一边把书翻到bl内容给三朗看。"
    stop music fadeout 2.0
    extend "\n当然，是挑了没到十八禁的页数。"
    window hide
    play music "hurry_up.ogg"
    play sound "fx/boing.ogg"
    show cg c69 with zoominout
    window show
    saburo "你，你你你你干什么！！\n这，这这这是什么玩意啊！！！！"
    extend "\n这种的……这，这种的……"
    "三朗好像受到的刺激太强了一样，脸变得通红。"
    extend "\n但是，和他说的话相反，他的眼睛没有离开本子。"
    me "三朗……我觉得……"
    extend "\n你其实对这种东西也有兴趣吧？"
    "我笑嘻嘻地问道。"
    saburo "才，才没有……！"
    extend "\n我更喜欢这种性感大姐姐……。"
    "三朗一边语无伦次地回答，一边盯着自己手上的书。"
    saburo "呜呜……。"
    window hide
    hide cg with dissolve
    play sound "fx/fall_down.ogg"
    window show
    "突然，三朗按住大腿蹲了下去。"
    me "哎呀呀~？ 三朗君，怎么了？"
    "我故意这么询问。"
    show saburo 11 at top with dissolve
    saburo "没，没什么……！\n没什么……！！"
    extend "\n总之，把那本书给我收起来。"
    extend "\n求你了……！！"
    "三朗满脸通红，含着泪水低着头\n我感觉做的有些过头了，就按照他说的把书放回了书架。"
    "再这样下去，我的两腿之间就要变得精神了。"
    window hide
    stop music fadeout 2.0
    hide bg with dissolve
    hide saburo with dissolve
    hide saburo with dissolve
    play music "afternoon_class.ogg"
    show bg bookstore at center with Dissolve(1.0)
    show saburo 16 at top with dissolve
    window show
    "当我回到三朗身边时，他正神情诡秘地站着。"
    show saburo 15 with dissolve
    saburo "那个……[player_surname]君比，比其他家伙稍微成熟一些的吧？"
    extend "\n所以我想问问你……。"
    extend "\n男的会对男的产生性欲，这是怎么一回事……？"
    extend "\n一般来说，不可能发生这种事吧……？？"
    me "哎，不……也不是不可能。"
    extend "\n只是，确实不怎么常见……"
    extend "毕竟属于少数派，\n可能有人觉得是身体出现异常，或是精神有问题，\n但其实是很正常的。"
    show saburo 22 with dissolve
    saburo "……这样啊。"
    extend "\n[player_surname]君说的话我就相信吧。"
    extend "\n虽然你可能觉得我很变态，但这件事你千万不要告诉别人。"
    extend "\n拜托了……！"
    stop music fadeout 2.0
    me "嗯，嗯。"
    "被三朗的气势压倒了。"
    play music "good_scene.ogg"
    show saburo 26 with dissolve
    saburo "……我最近啊，有点不对劲。"
    extend "\n就算看到女人，也没啥感觉……"
    extend "\n就像刚才[player_surname]拿过来的书本一样……"
    extend "那种类型的，\n才更能够激起我的兴趣，怎么说呢……那个……。"
    me "……。"
    "三朗的表情，十分严肃认真。"
    extend "\n他可能是因为自己可能是异常而感到不安。"
    extend "\n我后悔自己轻率的决定，而捉弄了三朗。"
    me "三朗君……如果你愿意的话，我就陪你聊一聊。"
    extend "\n这样的话，也能减少你心里的负担吧？"
    show saburo 27 with dissolve
    saburo "[player_surname]，谢谢你……。"
    extend "\n我，应该没有问题吧。\n其实，挺正常的。"
    me "嗯，你说的没错。\n这并不是什么可羞耻的事情。"
    extend "\n这就是，三朗君内心真实一面的体现，\n三朗君你自己，也要好好接受才行啊。"
    show saburo 1 with dissolve
    saburo "是吗……是啊，嗯。"
    "三朗盯着自己的胸口，然后又看向了前方。"
    me "好！\n总之，先离开这里吧。"
    extend "\n换个环境更好的地方说话吧。"
    show saburo 2 with dissolve
    saburo "哦哦。"
    window hide
    stop music fadeout 2.0
    hide saburo with dissolve
    hide bg with dissolve
    hide saburo with dissolve
    play music "good_atmosphere.ogg"
    show bg evening at center with Radial(0.6)
    pause 0.5
    show bg downtown_evening with Dissolve(1.0)
    show saburo 15 at top with dissolve
    window show
    saburo "哈啊……为什么事情会变成这样啊~……。"
    extend "\n不，我明白……大致上的原因还是知道的。"
    me "每个人的喜好各不相同。"
    extend "\n既不是被迫接受，也不是强迫他人。"
    extend "\n即使周围的人都喜欢女人，只有你自己喜欢男人，那也没问题。"
    extend "\n堂堂正正地去面对就好了。"
    show saburo 16 with dissolve
    saburo "你，你这话说着简单！……"
    extend "\n我自己，想保持正常人的想法！\n我可不想走上同性恋这条不归路！！"
    extend "\n我要用气势恢复成正常的想法！"
    me "哎呀哎呀……刚才的决心，原来是这个方向啊。"
    extend "\n这边风景一样绚烂哦~。\n啊，对了！慎太郎也是哦！！"
    show saburo 3 with dissolve
    saburo "那，那家伙在，我更不干了！"
    show saburo 9 with dissolve
    extend "\n话说回来……这又是怎么回事？\n你也是……那种类型的？"
    me "不，哎呀……严格来说的话……。"
    show saburo 21 with dissolve
    saburo "呜哇~真的吗！？"
    extend "\n奥村也好，穗海也好，我也是，\n我的周围，净是些同性恋吗！"
    me "诶？！作哉也是这样吗？？"
    hide saburo with Dissolve(0.3)
    hide bg with Dissolve(0.3)
    play sound "fx/sparkle.ogg"
    show cg adult at center
    show sakuya 5 at topleft
    show 共 tomo 12 at topright with Radial(0.5)
    saburo "咦？你不知道吗？"
    extend "\n那家伙，迷恋上了班里的卷毛小鬼头哦！"
    "真，真真真真的吗！！！！！"
    me "是，是这样吗！！！！\n我可不知道啊……。"
    show bg downtown_evening at center
    extend "\n哎~那个孩子啊~……。\n总觉得挺意外的……。"
    window hide
    hide cg with Radial(0.5)
    hide sakuya with Radial(0.5)
    hide 共 with Radial(0.5)
    show saburo 2 at top with dissolve
    window show
    saburo "对吧？"
    extend "\n反正那方面是个人的自由，我也没什么说的。"
    me "什么嘛。\n你明明知道那是个人的自由吧。"
    extend "\n如果是那样的话，你现在就去接受它不就行了吗。"
    show saburo 3 with dissolve
    saburo "那，那是两码事！！！"
    me "什么两码事？"
    show saburo 16 with dissolve
    saburo "那，那是……。"
    show saburo 14 with dissolve
    extend "\n总之！！！是两码事！！！"
    extend "\n啊~够~了啊，这个话题到此为止！！"
    extend "\n刚才对不起了，突然变得那么正经！"
    "三朗噗地一下转过头去，开始走起来。"
    window hide
    hide saburo with dissolve
    window show
    "正如慎太郎所说的那样，只是「还差一步」。"
    extend "\n正处在无法确定对于自己对同性爱的兴趣，以及提起自己身为少数派的勇气的两难境地啊。"
    "但是，这个孩子的情况的话，与其说是被拉拢……。"
    window hide
    show saburo 6 at top with dissolve
    window show
    saburo "喂－[player_surname]！\n你在干啥呢！回家了！！"
    "走在前面的三朗转过头来叫了我一声。"
    me "哦！现在就去！！"
    "然后我就跑了过去，和三朗一起各回各家了。"
    stop music fadeout 0.5
    window hide
    hide cg with Dissolve(0.8)
    hide bg with Dissolve(0.8)
    hide saburo with Dissolve(0.8)
    pause 0.4
    show bg living_room_night at center with Dissolve(1.0)
    play music "nostalgia.ogg"
    window show
    play sound "fx/door_open.ogg"
    me "我回来了~。"
    mother "欢迎回来~。"
    extend "\n今天回来的有点晚啊。"
    me "嗯。"
    extend "\n我今天跟朋友出去玩了哦。"
    mother "哦，是这样啊。"
    extend "\n也别忘记写作业啊。"
    me "知道啦，我都这么大个人了。"
    extend "\n呼~今天也好开心啊。"
    play sound "fx/beer.ogg"
    "我慢慢地从冰箱里取出罐装啤酒，打开了盖子。"
    "噗。"
    mother "喂，等一下！！[player_name]！？\n为什么要喝啤酒！！"
    extend "\n你，还是未成年人吧！。"
    play sound "fx/boing.ogg"
    me "啊！！"
    "糟了！！不小心就养成平时的习惯了……。"
    me "啊，啊哈哈。\n抱歉抱歉。"
    extend "我搞错了，以为这是果汁。\n啊哈哈哈。"
    "我干笑着掩饰过去了。"
    mother "真是的……"
    extend "\n你将来也想成为爸爸那样的\n一回家就开瓶大口喝啤酒的酒鬼吗？"
    extend "\n我可不要啊~"
    me "会，会那样吗~\n啊哈哈哈……。"
    "总，总算蒙混过去了。好险好险。"
    "在学校里说话也要注意点才好……。"
    return

label day2_cooking_self:
    hide tuki with dissolve
    hide sora with dissolve
    window show
    "就在我心里吐槽的时候，佣人先生走进了厨房。"
    window hide
    play sound "fx/sliding_door.ogg"
    window show
    servant "三位，有什么事吗？\n我好像，听到很大的声音了……。"
    show tuki 18 at topleft with dissolve
    tuki "啊。\n厨房里出现了一只大蜘蛛，我们已经处理好了。"
    servant "啊呀啊呀……那空一定受了不少罪吧。\n没事吧？"
    extend "\n一会儿我给你端温热的茶来。"
    show sora 1 at topright with dissolve
    sora "谢谢。"
    show sora 3 with dissolve
    extend "\n对了，我们的手艺怎么样？"
    extend "\n我有点想知道母亲和其他的佣人怎么看。"
    servant "嗯，非常好。"
    extend "\n大家吃得很开心，觉得非常美味。"
    extend "\n到时候也请你们像今天一样努力。"
    extend "\n那我先去端茶了。"
    play sound "fx/sliding_door.ogg"
    "佣人先生说着，再次离开了厨房。"
    window hide
    hide tuki with dissolve
    hide sora with dissolve
    show sora 11 at topright with dissolve
    window show
    sora "太好了！哥哥，[player_name]君。"
    show tuki 9 at topleft with dissolve
    tuki "是啊。"
    me "嗯"
    show cg red at center with dissolve
    "……这就是赤峰家的家风吧。"
    extend "\n我觉得自己明白了他俩早上说的那句话。"
    "家里还有其他的人什么的，真是个奇怪的家啊。"
    extend "\n不过，在这个奇怪的家里，大家却能互相理解。"
    extend "\n我感受到了和自己家里不同的，别样的家的温暖。"
    window hide
    hide sora with dissolve
    hide tuki with dissolve
    hide cg with dissolve
    show tuki 15 at topleft with dissolve
    window show
    tuki "对了，[player_surname]。"
    extend "\n作为感谢你的帮助，今晚就在家里做晚饭给你吃吧。"
    show sora 3 at topright with dissolve
    sora "啊~说得对！"
    extend "\n[player_name]君，你一定要留下来吃晚饭哦！！"
    me "嗯~……\n抱歉，你们这么热情邀请我，我很高兴，不过这次就不用了。"
    extend "\n因为妈妈正在家里等我回去吃饭。"
    show sora 1 with dissolve
    sora "这样啊……那，没办法了。"
    extend "\n[player_name]君，你能够考虑到母亲的心情，真不简单。"
    me "啊哈哈，是吗？"
    extend "\n硬要说的话，可能是因为我想念自己的家了。"
    extend "\n最近这段时间，我很开心能和家人一起吃饭。"
    show tuki 8 with dissolve
    tuki "你才来没几个小时，就开始想家了？"
    extend "\n看来你还是太小了呢。"
    me "不，不好意思！"
    extend "\n别看我这样，其实我比你们大十岁哦！"
    show sora 34 with dissolve
    sora "你的意思是，你精神年龄很大吗？"
    extend "\n毕竟你在关键时刻总是很可靠的，所以这倒也说不定……。"
    me "关键时刻……你们是想说，平时我看上去就是个小孩吗……？"
    show tuki 1
    show sora 4 with dissolve
    tuki_and_sora "嗯。"
    play sound "fx/shock.ogg"
    "失落！！"
    show tuki 4 with dissolve
    tuki "总之，不用那么在意。"
    extend "\n因为我们的成长才刚刚开始。"
    me "哎，哎呀……过25岁后，代谢就会变差，\n记忆力和理解力也会逐渐衰退啊……。"
    show sora 26 with dissolve
    sora "啊哈哈哈！\n[player_name]君，你在说什么呢？"
    extend "\n果然很有趣呢！"
    hide tuki with dissolve
    hide sora with dissolve
    "就这样，虽然在途中经历了一场战斗，但还是成功开发出了料理，\n"
    hide bg with dissolve
    stop music fadeout 2.0
    "顺利完成了第二天的料理组的工作。"
    window hide
    pause 0.4
    show bg living_room_night at center with Radial(1.0)
    play music "nostalgia.ogg"
    window show
    play sound "fx/door_open.ogg"
    me "我回来了~。"
    mother "欢迎回来~。"
    extend "\n今天回来的有点晚啊。"
    me "嗯。"
    extend "\n我在朋友家里开发咖啡店的菜单。"
    mother "哦，是这样啊。"
    extend "\n居然特地把厨房借给你们，真是亲切呢。\n你们有好好遵守规矩吧？"
    me "没事啦，又不是小孩子了。"
    extend "\n呼~今天也好开心啊。"
    play sound "fx/beer.ogg"
    "我慢慢地从冰箱里取出罐装啤酒，打开了盖子。"
    "噗。"
    mother "喂，等一下！！[player_name]！？\n为什么要喝啤酒！！"
    extend "\n你，还是未成年人吧！。"
    play sound "fx/boing.ogg"
    me "啊！！"
    "糟了！！不小心就养成平时的习惯了……。"
    me "啊，啊哈哈。\n抱歉抱歉。"
    extend "我搞错了，以为这是果汁。\n啊哈哈哈。"
    "我干笑着掩饰过去了。"
    mother "真是的……"
    extend "\n你将来也想成为爸爸那样的\n一回家就开瓶大口喝啤酒的酒鬼吗？"
    extend "\n我可不要啊~"
    me "会，会那样吗~\n啊哈哈哈……。"
    "总，总算蒙混过去了。好险好险。"
    "在学校里说话也要注意点才好……。"
    return

label day2_design_self:
    show bg clothing_store at center
    window show
    me "你们都去试试看嘛。"
    window hide
    show tomo 8 at topleft with dissolve
    window show
    tomo "嗯~……"
    extend "\n但是，我连领带怎么系都不知道啊……。"
    show sintarou 23 at topright with dissolve
    sintarou "我也是……。"
    me "啊啊，你们都是穿学生服，所以还没有系领带的机会啊。"
    extend "\n那么，我来系一下吧。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    pause 0.3
    window show
    me "……嗯，大概这样吧？"
    show sintarou 8 at topright
    show tomo 1 at topleft with dissolve
    tomo "哦~！！很不错嘛！"
    sintarou "嗯嗯！很适合你呢[player_name]酱！"
    extend "\n而且，打领带的动作很熟练呢。"
    show sintarou 4 with dissolve
    extend "\n下次也教教咱怎么打领带吧~。"
    show tomo 4 with dissolve
    tomo "也教教我也教教我~！"
    extend "\n这样的话，穿便服的时候也可以戴领带了。"
    me "嗯，可以啊。"
    extend "\n下次，我再仔细地手把手教你们。"
    hide tomo with dissolve
    hide sintarou with dissolve
    show sintarou 12 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sintarou "哇哦……那个说法，很色吧？"
    me "嗯~？"
    extend "\n这样的话，就把你们分别叫到房间里，\n一对一指导。"
    show sintarou 29 with dissolve
    sintarou "哇哦♪，真期待啊。"
    hide sintarou with dissolve
    show tomo 38 at topleft with dissolve
    play sound "fx/eureka.ogg"
    tomo "那样也不错，但这里就干脆来个3P如何？"
    show sintarou 9 at topright with dissolve
    sintarou "3P啊……"
    show sintarou 5 with dissolve
    play sound "fx/cute.ogg"
    extend "\n按照我们这个阵容来看，感觉会是很不得了的事情啊~。"
    show tomo 2 with dissolve
    tomo "说得对~。"
    show tomo 11 with dissolve
    play sound "fx/cute2.ogg"
    extend "\n特别是，[player_name]感觉会做非常不得了的事情啊~。"
    play sound "fx/boing.ogg"
    me "为，为什么一定要我啊……。"
    extend "\n其他人先不说，和我比起来你们俩也没差多少啊。"
    hide sintarou with dissolve
    hide tomo with dissolve
    show sintarou 15 at top with dissolve
    sintarou "诶……？"
    show cg adult at center
    play sound "fx/sparkle.ogg"
    show sintarou 22 with dissolve
    extend "其，其实，\n连怎么生小孩我都不知道哦。"
    hide sintarou with dissolve
    show sintarou 23 at topright
    show tomo 22 at topleft with dissolve
    tomo "小慎。"
    play sound "fx/sparkle.ogg"
    extend "记得是，\n是天女从天而降把小孩送到人间的哦。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    hide cg with dissolve
    play sound "fx/ding.ogg"
    window show
    me "……。"
    "多么明显的睁眼说瞎话。"
    extend "\n这么一看，不管现在怎么说装成熟，\n我都能明白这两个人和「初」完全不搭边了……。"
    stop sound fadeout 0.5
    window hide
    show cg umesaki at center with Dissolve(0.7)
    window show
    "总算是找到了合适的领带的我们，订了两个班的量，\n顺利地完成了今天的服装班的工作。"
    stop music fadeout 2.0
    window hide
    hide bg with Dissolve(0.9)
    hide tomo with Dissolve(0.9)
    hide sintarou with Dissolve(0.9)
    hide cg with Dissolve(0.9)
    pause 0.4
    show bg living_room_night at center with Radial(0.8)
    play music "nostalgia.ogg"
    window show
    play sound "fx/door_open.ogg"
    me "我回来了~。"
    mother "欢迎回来~。"
    extend "\n学园祭的准备工作做的怎么样了？"
    me "嗯。"
    extend "\n然后去梅咲买学园祭要用的东西了。"
    mother "哦，是这样啊。"
    extend "\n不过那里晚上很危险的，不要玩到太晚哦。"
    me "我知道。毕竟我已经不是第一次去了。"
    extend "\n呼~今天也好开心啊。"
    play sound "fx/beer.ogg"
    "我慢慢地从冰箱里取出罐装啤酒，打开了盖子。"
    "噗。"
    mother "喂，等一下！！[player_name]！？\n为什么要喝啤酒！！"
    extend "\n你，还是未成年人吧！。"
    play sound "fx/boing.ogg"
    me "啊！！"
    "糟了！！不小心就养成平时的习惯了……。"
    me "啊，啊哈哈。\n抱歉抱歉。"
    extend "我搞错了，以为这是果汁。\n啊哈哈哈。"
    "我干笑着掩饰过去了。"
    mother "真是的……"
    extend "\n你将来也想成为爸爸那样的\n一回家就开瓶大口喝啤酒的酒鬼吗？"
    extend "\n我可不要啊~"
    me "会，会那样吗~\n啊哈哈哈……。"
    "总，总算蒙混过去了。好险好险。"
    "在学校里说话也要注意点才好……。"
    return

label day2_layout_self:
    show bg meffen_cafe_evening at center
    show sinobu 4 at top with dissolve
    window show
    sinobu "嗯嗯。"
    extend "\n那样的话，[player_surname]君也穿一下试试看吧。"
    show sinobu 11 with dissolve
    play sound "fx/eureka.ogg"
    extend "\n会是一次很好的尝试。"
    hide sinobu with dissolve
    hide tubasa with dissolve
    show sinobu 12 at topleft
    show tubasa 18 at topright with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tubasa "是，是啊。"
    extend "\n明明我们都穿了，[player_name]君不穿的话，可就太狡猾了"
    me "不，不是啦~毕竟！我可是只负责观赏的啊！！"
    hide sinobu with dissolve
    hide tubasa with dissolve
    show sinobu 10 at top with dissolve
    sinobu "你在说什么莫名其妙的话……"
    show sinobu 9 with dissolve
    extend "\n抱歉，能打扰一下吗？"
    window hide
    hide sinobu with dissolve
    window show
    "忍说完后，把女仆叫了过来。"
    stop music fadeout 2.0
    show sinobu 7 at top with dissolve
    sinobu "他说也想试试女仆装…。"
    play sound "fx/boing.ogg"
    me "等！  忍！  ？"
    play music "lively_boys.ogg"
    play sound "fx/sparkle.ogg"
    clerk2 "哎呀♪  是这样吗？"
    clerk1 "呜呼呼，ok！☆"
    play sound "fx/eureka.ogg"
    extend "\n即便你这样的朴素系男生，只要交给我们，\n就能变成心~动的正太女仆哦~！"
    play sound "fx/wind_slash.ogg"
    show cg remarkable at center with FadeWhite(0.5)
    "这么说着，女仆小姐们从两边把我抬了起来。"
    play sound "fx/dash.ogg"
    "什……什么啊力气竟然这么大！！？"
    window hide
    hide cg with Dissolve(0.3)
    hide sinobu with Dissolve(0.3)
    hide tubasa with Dissolve(0.3)
    window show
    me "那个！诶！？ 为什么？ ！！"
    play sound "fx/cute.ogg"
    clerk2 "不用那么害羞啦~。"
    play sound "fx/cute2.ogg"
    clerk1 "交给我们吧♪"
    play sound "fx/ding.ogg"
    show cg dark at center with dissolve
    "嘶嘶嘶嘶嘶……"
    "我非常丢脸地被女仆二人组拖进了里面的房间。"
    window hide
    hide cg with dissolve
    show sinobu 11 at topleft with dissolve
    window show
    stop sound fadeout 0.5
    sinobu "呵。"
    show tubasa 4 at topright with dissolve
    tubasa "诶嘿嘿。这是看到我们的样子笑出来的惩罚呢。"
    window hide
    show cg meffen_cafe_hallway at center with Dissolve(0.7)
    window show
    "就这样，我被迫换上了一副无论怎么看都不适合我的女仆打扮，\n还要遭受难以言喻的屈辱。"
    play sound "fx/dash.ogg"
    "到底谁会获利呢……。"
    window hide
    show cg downtown_evening with Dissolve(0.7)
    window show
    "一边想着这样的事情，一边结束了在「美馨儿咖啡」的参观，\n我们完成了布置组的工作。"
    window hide
    stop music fadeout 2.0
    hide bg with Dissolve(0.9)
    hide cg with Dissolve(0.9)
    hide tubasa with Dissolve(0.9)
    hide sinobu with Dissolve(0.9)
    pause 0.4
    show bg living_room_night at center with Radial(1.0)
    play music "nostalgia.ogg"
    window show
    play sound "fx/door_open.ogg"
    me "我回来了~。"
    mother "欢迎回来~。"
    extend "\n今天回来的有点晚啊。"
    me "嗯。"
    extend "\n御咲站往学校反方向走了一段，在咖啡店参观了一下。"
    mother "哦，是这样啊。"
    extend "\n不过那里晚上很危险的，不要玩到太晚哦。"
    me "我知道。毕竟我已经不是第一次去了。"
    extend "\n呼~今天也好开心啊。"
    play sound "fx/beer.ogg"
    "我慢慢地从冰箱里取出罐装啤酒，打开了盖子。"
    "噗。"
    mother "喂，等一下！！[player_name]！？\n为什么要喝啤酒！！"
    extend "\n你，还是未成年人吧！。"
    play sound "fx/boing.ogg"
    me "啊！！"
    "糟了！！不小心就养成平时的习惯了……。"
    me "啊，啊哈哈。\n抱歉抱歉。"
    extend "我搞错了，以为这是果汁。\n啊哈哈哈。"
    "我干笑着掩饰过去了。"
    mother "真是的……"
    extend "\n你将来也想成为爸爸那样的\n一回家就开瓶大口喝啤酒的酒鬼吗？"
    extend "\n我可不要啊~"
    me "会，会那样吗~\n啊哈哈哈……。"
    "总，总算蒙混过去了。好险好险。"
    "在学校里说话也要注意点才好……。"
    return

label day2_supply_self:
    window show
    me "三朗！\n我能和你一起去吗？"
    window hide
    show saburo 7 at top with dissolve
    window show
    saburo "唔~真是抱歉呢，[player_surname]。\n这次，我想一个人去别的地方看看。"
    show saburo 4 with dissolve
    extend "\n所以，下次再一起玩吧！"
    window hide
    hide saburo with dissolve
    window show
    play sound "fx/shock.ogg"
    me "（失落！）"
    extend "\n那，那么，就去作哉同学的那里……。"
    show sakuya 19 at top with dissolve
    sakuya "不行。"
    extend "\n因为我也想一个人行动，所以别跟着来。"
    return

label day2_supply_self_1:
    hide sakuya with dissolve
    hide saburo with dissolve
    window show
    play sound "fx/shock_big.ogg"
    me "（失落失落！）"
    window hide
    show saburo 2 at top with dissolve
    window show
    saburo "啊哈哈。别在意，[player_surname]。"
    extend "\n那么，你们两位，明天再见啦~。"
    window hide
    play sound "fx/running.ogg"
    hide saburo with dissolve
    show sakuya 5 at top with dissolve
    window show
    sakuya "行，那我先走了。"
    extend "\n我也走了。"
    show sakuya 15 with dissolve
    extend "\n你别傻站着了，快回去吧。"
    window hide
    play sound "fx/running.ogg"
    hide sakuya with dissolve
    window show
    play sound "fx/ding.ogg"
    "呼……"
    "我独自伫立，身旁的风无情地吹过。"
    "话说回来，居然两个人都单独想去某个地方，\n到底是什么地方呢……？"
    stop music fadeout 2.0
    show cg sky at center with dissolve
    "哈啊……。"
    extend "\n早知道，第一天就该跟他们更亲近些的。"
    stop sound fadeout 0.5
    extend "\n呼呼……。"
    hide cg with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    "就这样，我今天一天的校园生活悲惨地拉下了帷幕。"
    window hide
    pause 0.4
    show bg living_room_night at center with Radial(0.9)
    play music "nostalgia.ogg"
    window show
    play sound "fx/door_open.ogg"
    me "我回来了~。"
    mother "欢迎回来~。"
    extend "\n今天回来的有点晚啊。"
    me "嗯。"
    extend "\n我今天跟朋友出去玩了哦。"
    mother "哦，是这样啊。"
    extend "\n也别忘记写作业啊。"
    me "知道啦，我都这么大个人了。"
    extend "\n呼~今天也好开心啊。"
    play sound "fx/beer.ogg"
    "我慢慢地从冰箱里取出罐装啤酒，打开了盖子。"
    "噗。"
    mother "喂，等一下！！[player_name]！？"
    play sound "fx/boing.ogg"
    extend "为什么还要喝啤酒！！"
    extend "\n你，还是未成年人吧！。"
    me "啊！！"
    "糟了！！不小心就养成平时的习惯了……。"
    me "啊，啊哈哈。\n抱歉抱歉。"
    extend "我搞错了，以为这是果汁。\n啊哈哈哈。"
    "我干笑着掩饰过去了。"
    mother "真是的……"
    extend "\n你将来也想成为爸爸那样的\n一回家就开瓶大口喝啤酒的酒鬼吗？"
    extend "\n我可不要啊~"
    me "会，会那样吗~\n啊哈哈哈……。"
    "总，总算蒙混过去了。好险好险。"
    "在学校里说话也要注意点才好……。"
    return

label day2_supply_self_2:
    window show
    me "作哉君！\n我也能和你一起去吗？"
    window hide
    show sakuya 19 at top with dissolve
    window show
    sakuya "啊~……不好意思，[player_surname]。\n这次我想一个人去行动。"
    show sakuya 5 with dissolve
    extend "\n所以，我们下次再见"
    window hide
    hide sakuya with dissolve
    window show
    play sound "fx/shock.ogg"
    me "（失落！）"
    extend "\n那，那么，三朗君要一起来吗……。（这句话应该是翔平说的）"
    show saburo 7 at top with dissolve
    saburo "抱歉，我也想一个人去。"
    return

label day2_bad_end:
    stop music fadeout 0.3
    hide bg with Dissolve(0.2)
    play sound "fx/break.ogg"
    window show
    "咔嚓！！"
    window hide
    play music "fx/wind.ogg"
    window show
    me "什么！？？"
    "到底发生了什么！？！！"
    extend "\n虽然我睁着眼睛，但是眼前却一片漆黑！！？"
    window hide
    play sound "fx/wind_slash.ogg"
    show bg cave_space at center with dissolve
    play sound "fx/running.ogg"
    show yuuhi 13 at top with dissolve
    window show
    unknown "好，这下就能把人救出来了！"
    extend "\n喂，你！没事吧？"
    "声音传来的同时，一位橙色头发的少年出现在我的眼前。"
    me "诶……你，你是……？"
    extend "\n我刚才还和他们在一起……。"
    play sound "fx/boing.ogg"
    extend "\n诶……诶？？为什么？？？"
    show yuuhi 14 with dissolve
    unknown "也难怪你会混乱。\n你到刚才为止都还处于被梦境迷惑的状态。"
    show yuuhi 6 with dissolve
    extend "\n但是，已经没事了！\n因为我已经让你清醒过来了！！"
    window hide
    hide yuuhi with dissolve
    window show
    "梦境……"
    play sound "fx/eureka.ogg"
    extend "对，是我的梦！！"
    extend "\n我那快乐又幸福的梦，就是被你强行夺走了吗！？"
    play sound "fx/explosion2.ogg"
    extend "\n也就是说……我再也无法见到那梦境了吗！？"
    window hide
    play sound "fx/shock_big.ogg"
    window show
    me "怎，怎么可以这样啊啊啊啊啊！！\n你都对我做了什么啊啊啊啊！！"
    extend "\n好不容易……好不容易，"
    extend "才有了梦境里的学园生活……。"
    show yuuhi 3 at top with dissolve
    unknown "你，你为什么会那么失望啊。"
    extend "\n你这不正是得救了吗？"
    extend "\n真是个让人搞不清情况的家伙啊……。"
    play sound "fx/dash.ogg"
    me "因，因为……如果就那样的话，\n说不定还能跟他们发生更加更加色情的事啊！"
    extend "\n呜呜呜呜呜……。"
    hide yuuhi with dissolve
    "就是啊。"
    extend "\n将来要是能和他们变得更加亲密的话，说不定……！！"
    "事已至此……事已至此……！！！"
    window hide
    pause 0.4
    window show
    me "……呵呵呵呵。"
    extend "\n呵哈哈哈哈！！"
    show yuuhi 8 at top with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    unknown "什，什么啊？？\n你又突然笑起来，真让人不舒服……。"
    extend "\n难道说，你还没有睡醒吗？"
    me "没……托你的福，我意识已经清醒不少了。"
    extend "\n所以，我现在知道应该怎么做选择了！"
    show yuuhi 3 with dissolve
    unknown "什，什么啊，你这是。"
    me "没能和那些可爱的男孩子们亲密贴贴，"
    play sound "fx/impact_japanese.ogg"
    extend "\n我要和你贴到爽！！！！"
    play sound "fx/wind_slash.ogg"
    hide bg with dissolve
    hide yuuhi with dissolve
    "我勇敢地向眼前的小子飞扑过去。"
    window hide
    show bg cave_space at center
    show yuuhi 2 at top with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    window show
    unknown "呜，呜哇！！？为啥啊！？"
    extend "\n我明明是好心救了你，你为啥要袭击我啊……！？！？"
    show yuuhi 1 with dissolve
    play sound "fx/eureka.ogg"
    extend "\n可恶……既然如此，那就让你吃点苦头！"
    stop music fadeout 0.3
    window hide
    play sound "fx/battle3.ogg"
    show cg campfire_sparks at center with FadeWhite(0.4)
    window show
    yuuhi "幻象火焰！！！"
    window hide
    play sound "fx/phantom_fire.ogg"
    show cg phantom_fire with Radial(0.4)
    window show
    "砰！！！"
    window hide
    hide yuuhi with dissolve
    hide nori with dissolve
    hide bg with dissolve
    hide cg with dissolve
    window show
    "…"
    window hide
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.6
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "哔哔哔哔哔哔哔哔哔"
    window hide
    show bg protagonist_room_morning at center with Radial(0.5)
    window show
    me "啊……已经天亮了啊……？"
    extend "\n唔~总觉得好像没有睡觉呢……。"
    stop sound fadeout 0.5
    "我一边自言自语一边起床，看向桌子上面，\n上面放着一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……啊，对哦对哦，昨天回来的时候拿到的。"
    extend "\n那些正太们，真的好可爱啊……。"
    play sound "fx/triangle.ogg"
    me "……不过仔细一想，下周要去出差啊。"
    extend "\n这下子是逃不掉了啊……唉……。"
    me "嗯……身体莫名有股焦味啊。\n难道是妈妈做饭又失败了吗？"
    hide bg with dissolve
    "我洗了个澡，做好前往公司的准备，和往常一样出门了。"
    window hide
    play sound "fx/door_open.ogg"
    show bg sky at center with Radial(0.7)
    window show
    me "好嘞！ 今天也要加油啊！！"
    window hide
    stop music fadeout 1.0
    hide bg with FadeWhite(1.0)
    pause 0.6
    show bg dark at center with Radial(0.7)
    pause 0.6
    show bg baded with Dissolve(0.8)
    pause 1.3
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.5
    hide bg with dissolve
    return