# -*- coding: utf-8 -*-
# Converted from 0000025F.lns

label hidden:
    stop music fadeout 0.5
    hide cg with dissolve
    pause 0.5
    show bg 洞窟 at center with Dissolve(1.0)
    play music "FX/風.ogg"
    window show
    "前方有个洞窟。"
    extend "\n要进去吗？"
    return

label hidden_1:
    stop music fadeout 1.0
    pause 0.4
    show bg 地下牢 with Dissolve(0.8)
    play music "朔.ogg"
    pause 0.4
    show nori 14 at top with Dissolve(1.0)
    window show
    nori "哎呀，这隐居处竟然会有客人到来，真是稀奇…。"
    show nori 10 with dissolve
    nori "嗯？我还以为是谁呢，这不是当时遇见的那位吗。"
    show nori 12 with dissolve
    extend "\n竟然又会来这里，你还真是个狂热的人啊。"
    show nori 15 with dissolve
    extend "\n话说回来，找到这个地方一定费了不少功夫吧。"
    extend "\n到底是怎么找到的呢……。"
    show nori 13 with dissolve
    nori "……原来如此。"
    extend "\n看样子你已经被前几天看到的梦给俘虏了呢。"
    extend "\n而且还说什么一定要看那个梦的后续。"
    show nori 11 with dissolve
    nori "呵呵呵……你这人还真够下流的。"
    extend "\n竟然对还没成熟完全的少年们，燃起了这么大的热情。"
    show nori 12 with dissolve
    nori "话虽如此，我也知道少年的魅力。"
    extend "\n这次就认可你到达这里的这份努力，提供一些协助吧。"
    extend "\n请好好感谢我的温柔吧。"
    show nori 15 with dissolve
    nori "来，现在请再次许愿。"
    extend "\n许愿你最想在一起的人……。"
    hide nori with dissolve
    return

label hidden_tomo:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "Gymnopedies-No1.ogg"
    show bg ホテル at center with Dissolve(2.0)
    show tomo 20h at top with dissolve
    play sound "FX/可愛い.ogg"
    window show
    tomo "哈欠！！！"
    show tomo 8h with dissolve
    extend "\n……嗯啊……因为裸睡，可能感冒了……。"
    extend "\n暖气开大点……。"
    tomo "都，都怪你昨晚做那么荒唐的事，\n害我没来得及穿衣服就直接累得睡着了，"
    extend "\n要是真的感冒了，可要负起责任哦~。"
    show tomo 31h with dissolve
    tomo "……虽然这么说，但说实话我也很起劲……"
    show tomo 23h with dissolve
    extend "\n因为你，真的很厉害嘛……真的……各个方面都很厉害……。"
    show tomo 33h with dissolve
    tomo "果，果然是爱的力量吗？"
    show tomo 23h with dissolve
    extend "\n你，你看，我们……都，都是恋人了……。"
    show tomo 28h with dissolve
    play sound "FX/ビヨン.ogg"
    tomo "呃，糟糕……我自己说出来以后感觉超难为情的……！！"
    show tomo 34h with dissolve
    extend "\n呜哇，恋人，恋人啊！！"
    extend "\n好厉害啊……我居然会有恋人！"
    show tomo 36h with dissolve
    tomo "如果忍他们知道的话，肯定会大吃一惊吧。"
    extend "\n嗯……"
    extend "\n看来还是暂时保密比较好……嗯。"
    show tomo 23h with dissolve
    tomo "……。"
    show tomo 35h with dissolve
    tomo "……。"
    show tomo 23h with dissolve
    tomo "……我说，现在还有……时间吧？"
    show tomo 36h with dissolve
    tomo "……那，那接下来……再做一次吧？"
    show tomo 35h with dissolve
    play sound "FX/ビヨン.ogg"
    tomo "呜呜呜呜……我知道的！！我自己也知道！！！"
    extend "\n自己是大清早开始就性欲高涨的家伙啊\n这种事情我再清楚不过了！"
    show tomo 36h with dissolve
    tomo "可，可是……这样和你说话，\n我又会想起昨晚的事情……那个……"
    extend "\n心情又会变得兴奋起来……。"
    window hide
    show cg c94 at center with Dissolve(0.8)
    window show
    tomo "这，这也没办法吧！！\n毕竟我还没有发育完全，还是个毛头小子！"
    extend "\n倒不如说，这不正是年轻健康的证据吗？\n是啊！这没什么好奇怪的！！"
    extend "哼！你有意见吗？！"
    tomo "……所以……我就说你没意见了吧？"
    tomo "……总之，虽然我是个笨蛋，\n不过今后也请多多关照了！"
    window hide
    stop music fadeout 0.8
    hide tomo with dissolve
    hide cg with dissolve
    hide bg with dissolve
    return

label hidden_tubasa:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "Gymnopedies-No1.ogg"
    show bg ホテル at center with Dissolve(2.0)
    show tubasa 2h at top with dissolve
    window show
    tubasa "啊……早，早上好。"
    show tubasa 37h with dissolve
    extend "\n……那个，你睡得还行吗？"
    show tubasa 19h with dissolve
    tubasa "今，今天天气好像不错，\n不如出去走走。"
    show tubasa 2h with dissolve
    extend "\n可，可是现在是稍微有点凉的季节，\n还是穿得暖和一点比较好哦。"
    show tubasa 33h with dissolve
    play sound "FX/ビヨン.ogg"
    tubasa "……诶……啊……啊……我……我……我没穿衣服？"
    extend "\n诶……？为，为什么？？"
    extend "\n诶……诶诶诶诶诶诶诶？？？"
    extend "\n话说，这到底是哪儿，现在是什么时候，我又是谁……。"
    show tubasa 21h with dissolve
    tubasa "啊啊啊啊啊啊！ 对，对不起……。"
    extend "\n我……那个……！\n"
    show tubasa 19h with dissolve
    "我现在还是有点混乱……。"
    extend "\n我，我要做一下深呼吸……！"
    show tubasa 9h with dissolve
    tubasa "吸……呼……吸……呼……。"
    show tubasa 6h with dissolve
    tubasa "啊……从昨晚起我就一直很亢奋，根本没法冷静……。"
    show tubasa 1h with dissolve
    extend "\n……说起来，我还完全没有现实感，还不知道这是不是真的……。"
    extend "\n对，对不起……。"
    show tubasa 17h with dissolve
    play sound "FX/可愛い.ogg"
    tubasa "啊……那个，不对，不是这样的。"
    extend "\n我绝对不是讨厌！"
    extend "\n那个……只是有点跟不上事情的发展，或者说……"
    show tubasa 1h with dissolve
    extend "\n没想到……我居然能和你这样优秀的人在一起……。"
    show tubasa 37h with dissolve
    tubasa "我居然会对你产生这样的感情，我自己也觉得意外……。"
    show tubasa 19h with dissolve
    extend "\n啊……我，我说这些话，是不是很失礼啊。"
    extend "\n但，但是，我绝对不是讨厌……！"
    show tubasa 3h with dissolve
    tubasa "我，我最喜欢你了……。"
    extend "\n所以，昨天晚上才……。\n但是，对于那样的我，我还是有点不敢相信……那个……。"
    show tubasa 36h with dissolve
    tubasa "……一定是因为，和你成为恋人，我实在是太开心了，\n兴奋过头，所以才不知道说什么……。"
    show tubasa 35h with dissolve
    tubasa "但，但是……看着这样醒着的你，\n我觉得稍微冷静下来了点……。"
    show tubasa 6h with dissolve
    extend "\n夜晚的话，果然……会想些有的没的……。\n结果，从那以后我一整晚都没睡……"
    window hide
    show cg c96 at center with Dissolve(0.7)
    window show
    tubasa "呼啊……一放松下来就感觉一下子就要睡着了……。"
    tubasa "抱歉……再让我躺一会儿……可以吗？"
    extend "\n就一会儿……而已……所以……Zzz"
    tubasa "……最……喜欢了……。"
    window hide
    stop music fadeout 0.7
    hide cg with dissolve
    hide bg with dissolve
    hide tubasa with dissolve
    return

label hidden_sinobu:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "Gymnopedies-No1.ogg"
    show bg ホテル at center with Dissolve(2.0)
    show sinobu 5h at top with dissolve
    window show
    sinobu "啊，早……。"
    show sinobu 13h with dissolve
    sinobu "……那个……怎么说呢……\n昨晚真是失礼了……。"
    show sinobu 15h with dissolve
    sinobu "那时，真是让你看见了不像样子的一面。\n连我自己都感到惊讶……。"
    show sinobu 16h with dissolve
    extend "\n光是回想起来，就觉得羞耻得脑袋快炸了……。"
    show sinobu 32h with dissolve
    sinobu "但是……我一点都不讨厌啊。"
    extend "\n……如果可以的话，我还想再……呜呜。"
    show sinobu 17h with dissolve
    sinobu "对，对了。"
    extend "\n那个……我们是恋人这件事，\n希望你能继续瞒着大家……。"
    extend "\n在我完全适应这个环境之前……拜托你了。"
    show sinobu 13h with dissolve
    sinobu "如果现在被人知道了我们是恋人，\n那样我的脑袋一定会崩坏的吧……实在是太过羞耻了。"
    show sinobu 6h with dissolve
    play sound "FX/ひらめき！.ogg"
    sinobu "还有，我想你应该知道，\n昨晚的事，也绝对不能说出去。"
    show sinobu 33h with dissolve
    extend "\n虽然，这也是一件很羞耻的事……但是……"
    extend "\n我想，那件事，是只属于我们两个人的秘密。"
    show sinobu 31h with dissolve
    sinobu "这个……约好了，不能破坏约定哦。"
    window hide
    show cg c95 at center with Dissolve(0.7)
    window show
    sinobu "那个……我说啊…。"
    sinobu "……。"
    sinobu "……那个……。"
    sinobu "……。"
    sinobu "……果，果然……还是……没什么……。"
    sinobu "……。"
    sinobu "……哈啊……我，原来，是这样的一个人啊……"
    extend "\n这样子，就不能告诉友了啊……。"
    window hide
    stop music fadeout 0.8
    hide cg with dissolve
    hide bg with dissolve
    hide sinobu with dissolve
    return

label hidden_tuki:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "Gymnopedies-No1.ogg"
    show bg ホテル at center with Dissolve(2.0)
    show tuki 5h at top with dissolve
    window show
    tuki "……你醒了啊……。"
    show tuki 23h with dissolve
    extend "\n那个……怎么说呢……。"
    extend "\n昨晚，是那个……那个……。"
    show tuki 22h with dissolve
    tuki "……嗯，算了。"
    show tuki 26h with dissolve
    extend "\n比起这个，你听我说。"
    extend "\n从早上开始，我其实就做了很蠢的事了哦。"
    show tuki 3h with dissolve
    tuki "我有，每当发生什么令人高兴或幸福的事，\n就怀疑是不是在做梦的毛病。"
    extend "\n今天早上也是这样……。\n我醒来后，看到你，想起昨晚的事，我就怀疑是梦。"
    show tuki 2h with dissolve
    tuki "在浴室里，用水浇头后，身体感受到的真实感触。"
    extend "\n接着，是睡着的你的身体。"
    extend "\n那感触，也是真实的。"
    extend "\n然后，我第一次认识到这是现实。"
    show tuki 10h with dissolve
    tuki "连我都有点慌张了，真是丢人啊…。"
    show tuki 28h with dissolve
    tuki "不过……能和你在一起，\n而不是做梦，真是太好了…。"
    show tuki 2h with dissolve
    extend "\n……得快点告诉空才行。"
    show tuki 16h with dissolve
    tuki "说实话，要将这件事告诉他，我多少有点内疚，\n可必须要告诉他才行。"
    show tuki 25h with dissolve
    extend "\n不过……一定没事的。\n空会祝福我们的。"
    show tuki 20h with dissolve
    play sound "FX/ビヨン.ogg"
    tuki "其他人……暂时保密。"
    extend "\n特别是奥村和森海，绝对不能告诉他们。"
    extend "\n他们一定会嘲笑我们的。"
    window hide
    show cg c99 at center with Dissolve(0.7)
    window show
    tuki "……呐，你还没睡醒么……？"
    tuki "如果不是的话，那个……怎么说呢。"
    extend "\n昨晚的触感，一直在我脑海中挥之不去…。"
    tuki "所以……那个……要不要再来一次？"
    tuki "这次，我想直接感受到你…。"
    window hide
    stop music fadeout 0.7
    hide cg with dissolve
    hide bg with dissolve
    hide tuki with dissolve
    return

label hidden_sora:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "Gymnopedies-No1.ogg"
    show bg ホテル at center with Dissolve(2.0)
    show sora 18h at top with dissolve
    window show
    sora "嗯……诶……已经……早上啦。"
    show sora 13h with dissolve
    play sound "FX/可愛い.ogg"
    sora "哇！！"
    extend "\n我们昨天就那样睡着了啊……。"
    extend "\n难怪会有点冷。"
    show sora 14h with dissolve
    extend "\n那个……那个，早安。"
    show sora 1h with dissolve
    sora "啊哈哈，总感觉有点难为情啊。"
    extend "\n这种时候应该说什么才好呢。"
    extend "\n真厉害啊……。"
    show sora 30h with dissolve
    sora "没想到我居然会交到恋人……"
    extend "\n要是哥哥知道了，肯定会非常惊讶的吧……"
    extend "\n就连我自己都无法想象，\n居然会出现一位比哥哥还要令我心动的人……。"
    show sora 32h with dissolve
    sora "真是的，我这样不行啊。\n到现在为止，我依然无法脱离哥哥。"
    show sora 1h with dissolve
    extend "\n说出这种话，可能会让你不安吗？\n啊哈哈。"
    show sora 32h with dissolve
    sora "不过，放心吧。现在我能好好地说出来了。\n我最喜欢的人，就是你。"
    show sora 18h with dissolve
    extend "\n啊，怎么办……说出这种话后，我的脸……好热……。"
    window hide
    show cg c98 at center with Dissolve(0.7)
    window show
    sora "真不好意思啊……我，现在肯定脸红了吧？"
    extend "\n……不，不要在意。\n我估计很快就会恢复了……。"
    sora "这红脸是不是已经消了……？"
    extend "\n实在是抱歉了。我真是太没男子气概了……"
    sora "……不过，这个就是我喜欢你的证据……。"
    extend "\n你要是能接受，我会很高兴的。"
    sora "因为，我喜欢你。"
    extend "\n这世上我最....喜欢你了！"
    window hide
    stop music fadeout 0.8
    hide cg with dissolve
    hide bg with dissolve
    hide sora with dissolve
    return

label hidden_sakuya:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "Gymnopedies-No1.ogg"
    show bg ホテル at center with Dissolve(2.0)
    show sakuya 10h at top with dissolve
    window show
    sakuya "……嗯，早上好。"
    show sakuya 20h with dissolve
    extend "\n……你，你在看什么呢……。"
    extend "\n话说，你要睡到什么时候啊？"
    extend "\n不过真的好无聊啊。"
    show sakuya 32h with dissolve
    sakuya "嘛，嘛……大致上理由我明白。"
    extend "\n昨天晚上也到很晚……那个，是那个……。"
    extend "\n但，但是，要是那样的话我也……。"
    show sakuya 1h with dissolve
    extend "\n哈啊……为什么会变成这样呢……。"
    show sakuya 9h with dissolve
    sakuya "我，我知道的哦！"
    extend "\n因为是恋人所以想说这些吧！"
    extend "\n那，那种羞耻的事情，没必要一一说出来吧！"
    show sakuya 10h with dissolve
    sakuya "……然后，接下来打算怎么做？好像还有一点时间。"
    show sakuya 20h with dissolve
    play sound "FX/ビヨン.ogg"
    extend "\n……话，话说衣服！衣服放哪了啊！"
    extend "\n擅自跑到别的地方去了，\n害得我起床之后都一直这样了。"
    show sakuya 8h with dissolve
    sakuya "……真是的，够了！\n我现在就去睡回笼觉！！"
    show sakuya 19h with dissolve
    sakuya "……。"
    show sakuya 7h with dissolve
    sakuya "……那个……那个啊，我能说的就只有这些了，但，\n……姑且，那啥……我，对你没有讨厌啊。"
    extend "\n这一点你可别误会了。"
    show sakuya 36h with dissolve
    play sound "FX/ダッ！.ogg"
    extend "\n换，换句话说就是那个。讨厌的反义词！明白了吗？"
    window hide
    show cg c101 at center with Dissolve(0.7)
    window show
    sakuya "……你也进来吧……进被窝里。"
    extend "\n只有你一个人……太冷了。"
    extend "\n真，真是的！我嘴太笨了啊！！"
    extend "\n我会以态度来证明的，别废话赶紧过来！"
    sakuya "…………因为我喜欢你。"
    window hide
    stop music fadeout 0.8
    hide cg with dissolve
    hide bg with dissolve
    hide sakuya with dissolve
    return

label hidden_saburo:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "Gymnopedies-No1.ogg"
    show bg ホテル at center with Dissolve(2.0)
    show saburo 31h at top with dissolve
    play sound "FX/ビヨン.ogg"
    window show
    saburo "啊切！！！！"
    show saburo 16h with dissolve
    extend "\n嗯~……嗯……？这里是……咦？"
    extend "\n话说，为什么我会裸着……？嗯……？呃……。"
    extend "\n昨天是和那家伙去的那里，然后晚上……。"
    show saburo 18h with dissolve
    saburo "……。"
    show saburo 31h with dissolve
    saburo "……。"
    show saburo 12h with dissolve
    play sound "FX/可愛い2.ogg"
    saburo "……！！！！"
    show saburo 3h with dissolve
    play sound "FX/爆発２.ogg"
    saburo "哇……哇……哇啊啊啊！！"
    extend "\n我，我，做了什么啊！！！"
    extend "\n……终于踏足了这个世界啊……。"
    show saburo 15h with dissolve
    saburo "真的吗……？真的吗……？那不是梦吗？"
    extend "\n是现实吗……？"
    extend "\n……但，但是，那真实的触感……。"
    extend "\n现在都还清晰记得……果然那是……。"
    show saburo 3h with dissolve
    play sound "FX/ビヨン.ogg"
    saburo "咦！哇啊啊啊！？"
    extend "\n自己是怎么起的啊！！"
    extend "\n孤零零地在大床上！！"
    show saburo 11h with dissolve
    saburo "话说……为什么我也裸着啊……。"
    extend "\n……嘛，嘛，大体的理由可以想象出……啊……。"
    show saburo 15h with dissolve
    extend "\n我们，真的做了啊……。"
    extend "\n……哈啊……。"
    show saburo 33h with dissolve
    saburo "啊……不，不是的！我绝对不是讨厌！"
    extend "\n因，因为我自己也承认了啊……"
    extend "\n那个啥？是情侣吧？还是还是恋人吧？\n要变成那种关系啊……。"
    show saburo 31h with dissolve
    saburo "所以……我觉得昨晚做那件事也不错……"
    show saburo 22h with dissolve
    extend "\n刚才那个，我也不是真的讨厌，\n别，别误会了啊！"
    window hide
    show cg c100 at center with Dissolve(0.7)
    window show
    saburo "……倒不如说，反倒是回想起来才发现\n不知不觉都变成那种关系了啊……。"
    extend "\n这，你懂的吧？"
    extend "\n就从你看到我还没离开这张床的状态，懂了吗！"
    saburo "……那就，再来一次吧……。"
    extend "\n那个……我是，喜，喜欢你的，\n……从现在开始，我要好好表达出来！！！！"
    extend "\n快点来，笨蛋！！！"
    window hide
    stop music fadeout 0.8
    hide cg with dissolve
    hide bg with dissolve
    hide saburo with dissolve
    return

label hidden_sintarou:
    stop music fadeout 0.5
    hide bg with dissolve
    play music "Gymnopedies-No1.ogg"
    show bg ホテル at center with Dissolve(2.0)
    show sintarou 11h at top with dissolve
    window show
    sintarou "呜嗯……"
    extend "\n早上了吗。好快啊。"
    extend "\n话说，总觉得没怎么睡啊。"
    extend "\n……嘛，实际上，我完全睡不着啊。"
    show sintarou 22h with dissolve
    sintarou "啊，哎呀，我们光着身子睡了啊。"
    extend "\n床单都这么乱糟糟了，\n真是邋遢。"
    show sintarou 29h with dissolve
    sintarou "还不是因为，某位在床上来回闹腾\n才会变成这样的啊。"
    extend "\n哎呀呀，我昨晚也很不得了的哦。"
    show sintarou 34h with dissolve
    sintarou "嘛！但结果还是相当不错哦♪"
    show sintarou 31h with dissolve
    sintarou "当然，其中也有技巧和气氛的因素在，"
    show sintarou 34h with dissolve
    extend "\n虽说有点不妥，但还是说一下，"
    extend "\n……说白了，这不就是所谓的爱的力量吗？"
    show sintarou 33h with dissolve
    sintarou "嘿嘿♪"
    extend "\n不管怎样，我们还是新婚小夫妻嘛！"
    show sintarou 20h with dissolve
    sintarou "……话说回来，没想到我还能交到恋人，\n真的完全没想到呢……。"
    extend "\n哎呀~人生这种东西，真的是什么都有可能发生呢……。"
    show sintarou 29h with dissolve
    sintarou "要是把咱这样的家伙留在身边啊～"
    extend "\n往后准让你操心得够呛哟。"
    show sintarou 33h with dissolve
    extend "\n不过嘛……既然当了你恋人，作为恋人的咱，肯定会努力\n不让咱的恋人受到负担的。"
    window hide
    show cg c97 at center with Dissolve(0.7)
    window show
    sintarou "哼哼♪"
    extend "\n所以，接下来怎么办？"
    extend "\n时间还有很多，我想悠闲又有意义地度过哦。"
    sintarou "……对我来说，还是不想离开这个床呢……吧。"
    "诶嘿嘿……就是这么回事。"
    sintarou "……那啥啊。"
    extend "\n你居然如此爱着这样的我，\n真是感激不尽啊。"
    window hide
    stop music fadeout 0.8
    hide cg with dissolve
    hide bg with dissolve
    hide sintarou with dissolve
    return

label hidden_note:
    stop music fadeout 0.5
    play music "FX/洞窟.ogg"
    show bg 洞窟（空間） with dissolve
    window show
    "洞里只有一本摊开的，字迹未干的笔记本。「按空格可隐藏对话框」"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label hidden_nori:
    show nori 10 at top with dissolve
    window show
    "\n毫无代价的欲望太过强烈，只会毁了你自己。"
    hide nori with dissolve
    return