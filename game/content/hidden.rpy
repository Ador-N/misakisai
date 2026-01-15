# -*- coding: utf-8 -*-
# Converted from 0000025F.lns

label hidden:
    stop music fadeout 0.5
    hide cg with dissolve
    pause 0.5
    show bg cave at center with Radial(1.0)
    play music "fx/wind.ogg"
    window show
    "前方有座洞窟。"
    extend "\n要进去吗？"
    return

label hidden_1:
    stop music fadeout 1.0
    pause 0.4
    show bg dungeon with Radial(0.8)
    play music "nori_theme.ogg"
    pause 0.4
    show nori 14 at top with Dissolve(1.0)
    window show
    nori "哎呀，这隐居处竟然会有客人到来，真是稀奇……。"
    show nori 10 with dissolve
    nori "嗯？我还以为是谁呢，这不是当时遇见的那位先生吗。"
    show nori 12 with dissolve
    extend "\n竟然能再次寻到这里，你还真是个狂热的人啊。"
    show nori 15 with dissolve
    extend "\n话说回来，找到这个地方一定费了不少功夫吧。"
    extend "\n到底是怎么找到的呢……。"
    show nori 13 with dissolve
    nori "……原来如此。"
    extend "\n看看来，你已经被前几天的那场梦境给彻底俘虏了呢。"
    extend "\n而且还说什么一定要看那个梦的后续。"
    show nori 11 with dissolve
    nori "呵呵呵……你这人还真够下流的。"
    extend "\n竟然对还没成熟完全的少年们，燃起了这么高的热情。"
    show nori 12 with dissolve
    nori "话虽如此，我也能理解少年的魅力。"
    extend "\n这次，我就认可你寻访至此的这份努力，提供一些协助吧。"
    extend "\n请务必对我的这份慈悲心怀感激哦。"
    show nori 15 with dissolve
    nori "来吧，请再次许下心愿。"
    extend "\n为了那个……你最渴望与其相守的人。"
    hide nori with dissolve
    return

label hidden_tomo:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "gymnopedies_no1.ogg"
    show bg hotel at center with Radial(2.0)
    show tomo 20h at top with dissolve
    play sound "fx/cute.ogg"
    $ renpy.transition(Quake(0, 30, 0.1, 0.15), layer='master')
    window show
    tomo "阿——嚏！！！"
    show tomo 8h with dissolve
    extend "\n……嗯啊……昨晚光着身子就睡着了，可能有点感冒了……。"
    extend "\n得把暖气开大点……。"
    tomo "都、都怪你啦！昨晚玩得那么过火，\n害得我连穿衣服的力气都没有，直接累得睡死过去了。"
    extend "\n要是真的感冒了，你可要负起责任哦~。"
    show tomo 31h with dissolve
    tomo "……虽然这么说，但说实话我也很起劲……。"
    show tomo 23h with dissolve
    extend "\n因为你，真的很厉害嘛……真的……各个方面都很厉害……。"
    show tomo 33h with dissolve
    tomo "果、果然是爱的力量吗？"
    show tomo 23h with dissolve
    extend "\n你、你看，我们……已经是、是恋人了对吧……。"
    show tomo 28h with dissolve
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 30, 0.1, 0.15), layer='master')
    tomo "哇，糟糕……自己说出这种话来感觉超级羞耻的……！！"
    show tomo 34h with dissolve
    extend "\n『恋人』什么的，居然真的是恋人啊！！"
    extend "\n好厉害啊……我居然会有恋人！"
    show tomo 36h with dissolve
    tomo "如果忍他们知道的话，肯定会大吃一惊吧。"
    extend "\n嗯……。"
    extend "\n果然，暂时还是先保密比较好……嗯。"
    show tomo 23h with dissolve
    tomo "……。"
    show tomo 35h with dissolve
    tomo "……。"
    show tomo 23h with dissolve
    tomo "……我说，现在还有……时间吧？"
    show tomo 36h with dissolve
    tomo "……那、那我们就……再来做一次，好吗？"
    show tomo 35h with dissolve
    $ renpy.transition(Quake(0, 30, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tomo "呜呜呜呜……我知道的！！我自己也知道！！！"
    extend "\n自己是一大清早就性欲高涨的家伙啊，\n这种事情我再清楚不过了！"
    show tomo 36h with dissolve
    tomo "可、可是……这样和你说话，\n又会忍不住想起昨晚的事……那个……"
    extend "\n情绪一下子就又高涨起来了嘛……。"
    window hide
    show cg c94 at center with Radial(0.8)
    window show
    tomo "这、这也没办法吧！！\n毕竟我还是个正值青春期的毛头小子啊！"
    extend "\n倒不如说，这不正是年轻健康的证明吗？\n没错！这是很正常的生理现象！！"
    extend "哼！你有意见吗？！"
    tomo "……所以……既然没意见，那就开始咯？"
    tomo "……总之，虽然我是个笨蛋，\n但从今往后，也请多多关照啦！"
    window hide
    stop music fadeout 0.8
    hide tomo with Dissolve(1.0)
    hide cg with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    return

label hidden_tubasa:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "gymnopedies_no1.ogg"
    show bg hotel at center with Radial(2.0)
    show tubasa 2h at top with dissolve
    window show
    tubasa "啊……早、早上好。"
    show tubasa 37h with dissolve
    extend "\n……那个，你睡得还好吗？"
    show tubasa 19h with dissolve
    tubasa "今、今天天气好像不错，\n能一起出去走走就好了呢。"
    show tubasa 2h with dissolve
    extend "\n可、可是现在是稍微有点凉的季节，\n出门的话还是穿得暖和一点比较好哦。"
    show tubasa 33h with dissolve
    $ renpy.transition(Quake(0, 30, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tubasa "……诶……啊……啊……我、我……我没穿衣服……？"
    extend "\n诶……？为、为什么？？"
    extend "\n诶……诶诶诶诶诶诶诶？？？"
    extend "\n话说，这到底是哪儿，现在是什么时候，我又是谁……。"
    show tubasa 21h with dissolve
    tubasa "啊哇哇哇哇！对、对不起……。"
    extend "\n我……那个……！"
    show tubasa 19h with dissolve
    extend "果然，脑子里还是乱糟糟的……。"
    extend "\n我、我要做一下深呼吸……呼……！"
    show tubasa 9h with dissolve
    tubasa "吸——……呼——……吸——……呼——……。"
    show tubasa 6h with dissolve
    tubasa "啊……自从昨晚做了那种事之后，一直没法冷静下来……。"
    show tubasa 1h with dissolve
    extend "\n……或者该说，直到现在我都没有什么现实感，不敢相信这一切是真的……。"
    extend "\n对、对不起……。"
    show tubasa 17h with dissolve
    $ renpy.transition(Quake(0, 30, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tubasa "不、不是的，请不要误会。"
    extend "\n我绝对不是因为讨厌才会这样的！"
    extend "\n那个……只是有点跟不上事情的发展，或者说心跳已经快到要控制不住了……。"
    show tubasa 1h with dissolve
    extend "\n没想到……我居然能和你这样优秀的人在一起……。"
    show tubasa 37h with dissolve
    tubasa "我居然会对你产生这样的感情，连我自己都觉得很意外……。"
    show tubasa 19h with dissolve
    extend "\n啊……我、我这样说，是不是很失礼啊。"
    extend "\n但、但是，我绝对不是讨厌……！"
    show tubasa 3h with dissolve
    tubasa "我、我最喜欢你了……。"
    extend "\n所以，昨天晚上才……。\n可是一想到那样的自己，就还是觉得有点不敢相信……那个……。"
    show tubasa 36h with dissolve
    tubasa "……一定是因为，和你成为恋人，我实在是太开心了，\n一直处于亢奋状态，连话都不会说了……。"
    show tubasa 35h with dissolve
    tubasa "但、但是……看着这样醒过来的你，\n我觉得稍微冷静下来了点……。"
    show tubasa 6h with dissolve
    extend "\n晚上的话，果然……会想些有的没的……。\n结果，从那以后我一整晚都没睡……"
    window hide
    show cg c96 at center with Radial(0.7)
    window show
    tubasa "呼啊……一旦放松下来，困意就一下子全涌上来……了……。"
    tubasa "抱歉……再让我躺一会儿……可以吗？"
    extend "\n就一会儿……而已……所以……Zzz"
    tubasa "……最……喜欢你了……。"
    window hide
    stop music fadeout 0.7
    hide cg with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    hide tubasa with Dissolve(1.0)
    return

label hidden_sinobu:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "gymnopedies_no1.ogg"
    show bg hotel at center with Radial(2.0)
    show sinobu 5h at top with dissolve
    window show
    sinobu "啊……早……。"
    show sinobu 13h with dissolve
    sinobu "……那个……怎么说呢……\n昨晚，多有怠慢了……。"
    show sinobu 15h with dissolve
    sinobu "那时，真是让你看见了不像样子的一面。\n说实话，连我自己都感到很惊讶……。"
    show sinobu 16h with dissolve
    extend "\n光是去回想，就觉得羞耻得脑袋快炸了……。"
    show sinobu 32h with dissolve
    sinobu "但是……我一点都不讨厌哦。"
    extend "\n……如果可以的话，我还想再……呜。"
    show sinobu 17h with dissolve
    sinobu "对、对了。"
    extend "\n那个……我们是恋人这件事，\n希望你能先瞒着大家……。"
    extend "\n在我对这种状况稍微习惯一点之前……拜托了。"
    show sinobu 13h with dissolve
    sinobu "如果现在被人知道我们是恋人，\n我的脑子一定会坏掉的吧……实在是太羞耻了。"
    show sinobu 6h with dissolve
    play sound "fx/eureka.ogg"
    sinobu "还有，我想你应该清楚，\n昨晚的事，也绝对不能说出去。"
    show sinobu 33h with dissolve
    extend "\n不仅是因为觉得羞耻……主要是……。"
    extend "\n那种事，我想把它当成只属于我们两个人的回忆。"
    show sinobu 31h with dissolve
    sinobu "这个……约好了，不能破坏约定哦。"
    window hide
    show cg c95 at center with Radial(0.7)
    window show
    sinobu "那个……我说啊……。"
    sinobu "……。"
    sinobu "……那个……。"
    sinobu "……。"
    sinobu "……果、果然……还是……没什么……。"
    sinobu "……。"
    sinobu "……哈啊……我，原来，是这样的一个人啊……。"
    extend "\n这样子，就不能告诉友了啊……。"
    window hide
    stop music fadeout 0.8
    hide cg with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    hide sinobu with Dissolve(1.0)
    return

label hidden_tuki:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "gymnopedies_no1.ogg"
    show bg hotel at center with Radial(2.0)
    show tuki 5h at top with dissolve
    window show
    tuki "……你醒了啊……。"
    show tuki 23h with dissolve
    extend "\n那个……怎么说呢……。"
    extend "\n昨晚的事，那是……那个……。"
    show tuki 22h with dissolve
    tuki "……嗯，算了。"
    show tuki 26h with dissolve
    extend "\n比起这个，你听我说。"
    extend "\n从早上开始，我其实就做过很蠢的事了哦。"
    show tuki 3h with dissolve
    tuki "我有种坏习惯，每当发生什么令人高兴或幸福的事，\n就会下意识地怀疑这究竟是不是现实。"
    extend "\n今天早上也是这样……。\n当我睁开眼看到你，想起昨晚的事，我就怀疑自己还在梦中。"
    show tuki 2h with dissolve
    tuki "为了确认，我去浴室用冷水浇头，那冰凉的触感是真实的。"
    extend "\n接着，我又回来触碰了还在熟睡中的你。"
    extend "\n那触感，也是真实的。"
    extend "\n直到那一刻，我才终于敢相信，这一切并非梦境。"
    show tuki 10h with dissolve
    tuki "连我自己都觉得，刚才那副手忙脚乱的样子真是丢人啊……。"
    show tuki 28h with dissolve
    tuki "不过……能像这样和你结合，\n而不是做梦，真是太好了……。"
    show tuki 2h with dissolve
    extend "\n……关于我们的事，近期也得找机会告诉空才行。"
    show tuki 16h with dissolve
    tuki "说实话，要把这件事告诉他，我多少会有点内疚。\n但我必须郑重地向他说明。"
    show tuki 25h with dissolve
    extend "\n不过……我想一定没问题的。\n空那孩子，会祝福我们的。"
    show tuki 20h with dissolve
    $ renpy.transition(Quake(0, 30, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tuki "至于其他人……还是暂时保密吧。"
    extend "\n特别是奥村和森海，绝对不能告诉他们。"
    extend "\n他们肯定会嘲笑我们的。"
    window hide
    show cg c99 at center with Radial(0.7)
    window show
    tuki "……呐，你还困吗……？"
    tuki "如果已经醒了的话，那个……怎么说呢。"
    extend "\n昨晚的触感，一直在我脑海中挥之不去……。"
    tuki "所以……那个……要不要再来一次？就一次。"
    tuki "这一次，我想更直接地……感受你……。"
    window hide
    stop music fadeout 0.7
    hide cg with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    hide tuki with Dissolve(1.0)
    return

label hidden_sora:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "gymnopedies_no1.ogg"
    show bg hotel at center with Radial(2.0)
    show sora 18h at top with dissolve
    window show
    sora "嗯……诶……已经……早上啦。"
    show sora 13h with dissolve
    $ renpy.transition(Quake(0, 30, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sora "哇！！"
    extend "\n我们昨天就那样睡着了啊……。"
    extend "\n难怪会有点冷。"
    show sora 14h with dissolve
    extend "\n那个……唔，重来一遍，早安。"
    show sora 1h with dissolve
    sora "啊哈哈，总感觉好难为情啊。"
    extend "\n这种时候应该说什么才好呢。"
    extend "\n感觉好不可思议啊……。"
    show sora 30h with dissolve
    sora "没想到我居然会交到恋人……"
    extend "\n要是哥哥知道了，肯定会非常惊讶的吧……。"
    extend "\n就连我自己都无法想象，\n居然会出现一位比哥哥更令我心动的人……。"
    show sora 32h with dissolve
    sora "真是的，我这样不行啊。\n到现在为止，我还是没法脱离哥哥啊。"
    show sora 1h with dissolve
    extend "\n说出这种话，会让你觉得不安吗？\n啊哈哈。"
    show sora 32h with dissolve
    sora "不过，请放心。现在我能好好地说出来了。\n我最喜欢的人，就是你。"
    show sora 18h with dissolve
    extend "\n啊，怎么办……一说出这种话，感觉脸……好烫……。"
    window hide
    show cg c98 at center with Radial(0.7)
    window show
    sora "真不好意思啊……我，现在肯定脸红了吧？"
    extend "\n……不、不要在意。\n我想大概很快就会恢复原状的……。"
    sora "那个，红晕已经消退了吗……？"
    extend "\n真的很抱歉。我真是太没有男子气概了……。"
    sora "……不过，这正是我喜欢你的证明……。"
    extend "\n如果你能接受这样的我，我会非常……高兴的。"
    sora "因为，我喜欢你。"
    extend "\n这世界上我最……最喜欢你了！"
    window hide
    stop music fadeout 0.8
    hide cg with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    hide sora with Dissolve(1.0)
    return

label hidden_sakuya:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "gymnopedies_no1.ogg"
    show bg hotel at center with Radial(2.0)
    show sakuya 10h at top with dissolve
    window show
    sakuya "……嗯，早啊。"
    show sakuya 20h with dissolve
    extend "\n……你、你在看什么啊……。"
    extend "\n话说，你打算睡到什么时候？"
    extend "\n我一个人真的好无聊啊。"
    show sakuya 32h with dissolve
    sakuya "嘛、嘛……大致上的理由我也明白。"
    extend "\n毕竟昨天晚上折腾到很晚……那个，发生了那种事嘛……。"
    extend "\n可、可是，要说累的话我也一样累啊……。"
    show sakuya 1h with dissolve
    extend "\n哈啊……为什么会变成这样呢……。"
    show sakuya 9h with dissolve
    sakuya "我、我知道的哦！"
    extend "\n你肯定又想说『因为我们是恋人』之类的话吧！"
    extend "\n那、那种难为情的事情，没必要每次都特意强调吧！"
    show sakuya 10h with dissolve
    sakuya "……然后呢，接下来打算怎么办？好像还有一点时间。"
    show sakuya 20h with dissolve
    $ renpy.transition(Quake(0, 30, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    extend "\n……话、话说衣服！我的衣服被你丢到哪里去了啊！"
    extend "\n你这家伙居然擅自把衣服收起来了，\n害得我起床之后只能一直这样。"
    show sakuya 8h with dissolve
    sakuya "……真是的，够了！\n我不管了，我现在就去睡回笼觉了！！"
    show sakuya 19h with dissolve
    sakuya "……。"
    show sakuya 7h with dissolve
    sakuya "……那个……我说啊，虽然只能说出这种程度的话……。\n但我，那个……姑且先说明白，我……并不讨厌你。"
    extend "\n这一点你可别误会了。"
    show sakuya 36h with dissolve
    play sound "fx/dash.ogg"
    extend "\n换、换句话说就是那个。讨厌的反义词！明白了吗？"
    window hide
    show cg c101 at center with Radial(0.7)
    window show
    sakuya "……你也赶紧……给我进被窝里来。"
    extend "\n我一个人……太冷了。"
    extend "\n真、真是的！我就是那种不擅长甜言蜜语的类型啦！！"
    extend "\n我会用行动来证明的，别废话了赶紧过来！"
    sakuya "…………因为我喜欢你。"
    window hide
    stop music fadeout 0.8
    hide cg with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    hide sakuya with Dissolve(1.0)
    return

label hidden_saburo:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "gymnopedies_no1.ogg"
    show bg hotel at center with Radial(2.0)
    show saburo 31h at top with dissolve
    $ renpy.transition(Quake(0, 30, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    window show
    saburo "阿嚏！！！！"
    show saburo 16h with dissolve
    extend "\n嗯~……嗯……？这里是……咦？"
    extend "\n话说，为什么我会裸着……？嗯……？呃……。"
    extend "\n我记得昨天是和那家伙去了那个地方，然后晚上……。"
    show saburo 18h with dissolve
    saburo "……。"
    show saburo 31h with dissolve
    saburo "……。"
    show saburo 12h with dissolve
    play sound "fx/cute2.ogg"
    saburo "……！！！！"
    show saburo 3h with dissolve
    $ renpy.transition(Quake(0, 30, 0.1, 0.15), layer='master')
    play sound "fx/explosion2.ogg"
    saburo "哇……哇……哇啊啊啊！！"
    extend "\n我、我，我做了什么啊！！！"
    extend "\n……到底还是踏足了『这边』的世界啊……。"
    show saburo 15h with dissolve
    play sound "fx/triangle.ogg"
    saburo "真的吗……？不是吧……？昨晚难道不是我在做梦吗？"
    extend "\n难道全都是现实……？"
    extend "\n……但、但是，那真实的触感……。"
    extend "\n现在都还清晰记得……果然那些都是……。"
    show saburo 3h with dissolve
    $ renpy.transition(Quake(0, 30, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    saburo "咦！哇啊啊啊！？"
    extend "\n你、你这家伙居然已经醒了吗！！"
    extend "\n我就说这么大个被窝里只有我一个人，还在纳闷呢！！"
    show saburo 11h with dissolve
    saburo "话说……为什么你也裸着啊……。"
    extend "\n……嘛、嘛，虽然大概能猜到理由是什么就是了……。"
    show saburo 15h with dissolve
    extend "\n我们，真的做了那种事啊……。"
    extend "\n……哈啊……。"
    show saburo 33h with dissolve
    saburo "啊……不、不是的！我绝对不是讨厌哦！"
    extend "\n因、因为我自己也承认了啊……。"
    extend "\n该叫什么呢？情侣吧？还是恋人？\n反正就是那种关系啊……。"
    show saburo 31h with dissolve
    saburo "所以……我觉得昨晚能那样做也不错……。"
    show saburo 22h with dissolve
    extend "\n刚才那个，我也不是真的讨厌，\n别、别误会了啊！"
    window hide
    show cg c100 at center with Radial(0.7)
    window show
    saburo "……倒不如说，反而是因为回想起来……\n结果搞得我又起反应了啊……。"
    extend "\n你、你懂的吧？"
    extend "\n看到我到现在还没从床上起来，你就该明白是怎么回事了吧！！"
    saburo "……那就，再来一次吧……。"
    extend "\n那个……毕竟我是真的喜、喜欢你的，\n……从现在开始，我要用行动好好表达出来！！！！"
    extend "\n快点来啦，笨蛋！！！"
    window hide
    stop music fadeout 0.8
    hide cg with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    hide saburo with Dissolve(1.0)
    return

label hidden_sintarou:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "gymnopedies_no1.ogg"
    show bg hotel at center with Radial(2.0)
    show sintarou 11h at top with dissolve
    window show
    sintarou "呜嗯……"
    extend "\n已经早上了吗。好快啊。"
    extend "\n话说，总觉得没怎么睡啊。"
    extend "\n……嘛，实际上，咱完全睡不着啊。"
    show sintarou 22h with dissolve
    sintarou "啊，哎呀，咱们两个就这么光着身子睡了啊。"
    extend "\n床单都这么乱糟糟了，\n真是邋遢。"
    show sintarou 29h with dissolve
    sintarou "还不是因为，某人在床上来回闹腾，\n才会变成这样的啊。"
    extend "\n哎呀呀~昨晚咱这边也是累得够呛啊。"
    show sintarou 34h with dissolve
    sintarou "嘛！不过那种感觉，倒是相当~相当不错呢♪"
    show sintarou 31h with dissolve
    sintarou "当然，其中也有技巧和气氛的因素在，"
    show sintarou 34h with dissolve
    extend "\n不过要是说点稍微肉麻的话……"
    extend "\n说白了，不就是所谓的爱的力量吗？"
    show sintarou 33h with dissolve
    sintarou "嘿嘿♪"
    extend "\n不管怎样，咱们还是新婚小夫妻嘛！"
    show sintarou 20h with dissolve
    sintarou "……话说回来，没想到咱还能交到恋人，\n真的完全没想到呢……。"
    extend "\n哎呀~人生这种东西，还真是不知道下一秒会发生什么呐……。"
    show sintarou 29h with dissolve
    sintarou "要是把咱这样的家伙留在身边啊~"
    extend "\n往后准让你操心得够呛哟。"
    show sintarou 33h with dissolve
    extend "\n不过嘛……既然已经是你的恋人了，作为伴侣，咱也会拼命努力，\n争取不给你增加负担的。"
    window hide
    show cg c97 at center with Radial(0.7)
    window show
    sintarou "哼哼♪"
    extend "\n所以，接下来打算怎么办？"
    extend "\n时间还有很多，得悠闲又充实地度过才行呐。"
    sintarou "……对咱来说的话，还是不想离开这个床呢……吧。"
    "诶嘿嘿……就是这么回事。"
    sintarou "……那个。"
    extend "\n你居然如此爱着这样的咱，\n真的是，感激不尽啊。"
    window hide
    stop music fadeout 0.8
    hide cg with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    hide sintarou with Dissolve(1.0)
    return

label hidden_note:
    stop music fadeout 0.5
    play music "fx/cave_ambience.ogg"
    show bg cave_space2 with dissolve
    window show
    "洞里只有一本摊开的，字迹未干的笔记本。\n（点击以隐藏对话框）"
    window hide
    pause
    stop music fadeout 0.5
    hide bg with Dissolve(0.8)
    return

label hidden_nori:
    show nori 10 at top with dissolve
    window show
    nori "请许下与你付出的努力相匹配的愿望。"
    extend "\n若是不付出相应的代价，那过于强烈的欲望，只会引导你走向毁灭。"
    hide nori with dissolve
    return