# -*- coding: utf-8 -*-
# Converted from 00000154.lns

label day0:
    show bg moon_night at center with Dissolve(2.0)
    play sound "train.ogg"
    pause 0.6
    show bg night_town with Dissolve(2.0)
    pause 1.0
    hide bg with Dissolve(1.0)
    play sound "train.ogg"
    show bg train_interior_night at center with FadeWhite(0.7)
    pause 0.5
    window show
    conductor "下一站『御咲』~『御咲』~。本站为终点站。"
    "与广播同步，列车缓缓减速，\n与站台并排停了下来。"
    extend "\n乘客们向同时打开的车门聚拢，我也跟了过去。"
    stop sound fadeout 1.0
    window hide
    hide bg with Dissolve(0.7)
    pause 0.5
    show bg telephone_pole_night with FadeWhite(0.5)
    play music "going_home.ogg"
    window show
    me "……呼，明明还不到六点，\n还以为能避开下班高峰的呢，没想到还挺拥挤的。"
    "从提前开暖气的车厢离开后，周围已经完全暗了下来。"
    extend "\n街道两旁的树木也渐渐染上了秋色。"
    "站在延伸至楼梯的队伍中，我漫不经心的望向对侧站台\n看到了一群等待电车的学生。"
    window hide
    play sound "fx/sparkle.ogg"
    show 少年たち c1 1 at center with Radial(0.5)
    pause 0.3
    show 少年たち c1 2 with Radial(0.5)
    window show
    me "啊，坐去梅咲的电车的话……"
    play sound "fx/boing.ogg"
    show cg remarkable at center with FadeWhite(0.5)
    "就能和那些可爱的中学生们一起回去了！！"
    "我在心中这样喊着。"
    "而我热切视线所注视的对象是……一群男孩子。"
    "没错，我是正太控。"
    window hide
    show cg telephone_pole_night with dissolve
    window show
    "正太控就是有正太郎情结，"
    extend "\n即对少年产生性冲动或恋爱感情的人。"
    extend "\n也就是喜欢小男孩的意思。"
    show cg c1 1 with FadeWhite(0.5)
    "从他们肩上背着的球拍包来看，他们是网球社的？"
    extend "\n不愧是必吃社团！可口的孩子很多啊。"
    show cg c1 2 with FadeWhite(0.5)
    "稍微远一点的地方，有群理着平头的孩子们，是棒球部吗？"
    extend "\n那样开心嬉闹的氛围真好啊，很可爱。"
    "唔~嗯，和那些孩子的话，就算是挤成沙丁鱼罐头我也会很乐意的……。"
    window hide
    hide bg with dissolve
    hide 少年たち with dissolve
    hide cg with dissolve
    return

label day0_1:
    show bg station_front_night at center with dissolve
    window show
    "刚出检票口，就看见一个少年在出口那边大声地叫着。"
    extend "\n这种时候他干什么呢？"
    window hide
    show tomo 1 at topright with dissolve
    window show
    boy1 "晚上好，我们是御咲学园！"
    extend "\n下周，我们将举办御咲祭，如果方便的话，请来看一看吧！\n我们将会有很多的节目，绝对不虚此行！"
    show tubasa 1 at topleft with dissolve
    boy2 "请，请来光顾……！"
    show tomo 2 with dissolve
    boy1 "翼君，再大声点！\n这样子路上的行人也听不到啊~！"
    show tubasa 2 with dissolve
    tubasa "啊，好的，友君……。"
    window hide
    show cg school_gate at center with Radial(0.5)
    window show
    "御咲学园是御咲这的一所中高一贯制的男校\n换句话说，这里是生活于御咲周边的我们这些正太控的圣地。"
    show cg school_building_full with FadeWhite(0.5)
    extend "\n顺带一提，我也是御咲学园的毕业生。"
    "御咲祭是御咲学园的文化祭……"
    hide tomo with dissolve
    hide tubasa with dissolve
    hide cg with dissolve
    extend "\n看样子，那些孩子手上还剩几张传单，\n发完前是回不去了。"
    "那么可爱的男孩子们都在努力的发放传单，\n不接受的人到底在想什么啊！正太控在干什么啊！\n真是的。"
    play sound "fx/eureka.ogg"
    "这时候，作为绅士的我，必须帮助这些可爱的学弟们！！"
    "趁机搭话什么的，才不是为了这种事。"
    extend "\n绝对。"
    extend "不是。"
    play sound "fx/boing.ogg"
    extend "一丝一毫都没……。"
    window hide
    pause 0.3
    window show
    play sound "fx/cute2.ogg"
    me "内，那个，不好意思！！  请给我一份传单吧！"
    show tubasa 3 at topleft with dissolve
    play sound "fx/cute.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    tubasa "咿！"
    "糟了。一上来就嘴瓢了，还大嗓门的喊了出来，反而吓到对方了。"
    show tomo 1 at topright with dissolve
    tomo "啊，好的！  请拿去请拿去！！  不止一份，要多少都行！"
    "被称为『友』的少年毫不畏惧地将传单递给了我。"
    play sound "fx/paper.ogg"
    tomo "请多多关照！！"
    show tomo 3 with dissolve
    extend "好了，翼君也来！"
    show tubasa 20 with dissolve
    tubasa "谢，谢谢……"
    "被称为『翼』的少年，不知道是因为害怕我，还是因为紧张，整个人都僵住了。"
    "这时候，我必须重整态势……"
    me "谢谢你。突然这么大声吓到你了，真是抱歉。"
    extend "\n其实，我是御咲学园的毕业生。"
    extend "\n怎么样？  在学校里过得开心吗？"
    "我用温柔的语气问道，翼这才恢复了冷静。"
    show tubasa 4 with dissolve
    tubasa "不，不，我们才是……！ 您原来是毕业生啊。"
    show tomo 4 with dissolve
    tomo "那您就是前辈呢！"
    extend "\n我超级享受校园生活的！"
    extend "\n对吧！  翼！"
    show tubasa 5 with dissolve
    tubasa "嗯，托你的福。"
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tomo "前辈~！ 请务必来参加御咲祭！！"
    extend "\n今年的御咲祭一定会很热闹的！"
    "友两眼放光，忙不迭地和我搭话。"
    me "真是令人怀念啊……  御咲篝火晚会还会举行吧？"
    show tomo 6 with dissolve
    tomo "当然了！  如果不举行篝火晚会，那怎么叫御咲祭呢。"
    me "那就好。"
    extend "\n祭典的最后，操场上的大火燃起来的感觉实在震撼，\n那是毕生难忘的回忆呢~。"
    "我不由得回忆起来。"
    me "话说回来，你们班的项目是什么呢？"
    show tomo 7 with dissolve
    tomo "那个！  我们班好像是……"
    show tomo 8 with dissolve
    play sound "fx/triangle.ogg"
    extend "\n…  什么来着？"
    "喂喂，你表现得那么兴奋，结果却忘了自己班的项目……"
    show tubasa 6 with dissolve
    tubasa "是咖啡厅。"
    extend "\n友君，昨天不是讨论过了吗？"
    show tomo 4 with dissolve
    tomo "啊，对了对了，咖啡厅！"
    tomo "我是二年一班，这孩子是二年二班，\n我们两班要开一个联合咖啡店！"
    extend "\n绝对会有美味的食物和饮品，"
    extend "\n请您一定要来哦！！"
    show tubasa 4 with dissolve
    tubasa "请，请多关照。"
    play sound "fx/impact.ogg"
    "哦哦！！！ 男孩子的邀请啊！！当然要去啊！！ 一定要去的啊！！！"
    window hide
    pause 0.3
    window show
    me "这样啊。我有空会去你那玩的。"
    extend "\n好好加油吧。"
    "我故作冷酷地离开了。"
    hide tomo with dissolve
    hide tubasa with dissolve
    "距离我成为社会人已经过去三年了……"
    extend "生活缺乏必要的滋润，\n也就是，缺少了「少年」的滋润！"
    extend "\n他们不可或缺，我要是少了他们，工作效率也会大幅下降。"
    extend "\n无论如何也要挤出时间去参加！"
    "我将干劲藏进心里，往家的方向走去。"
    extend "\n同时还用手摆出了胜利的姿势。"
    window hide
    hide bg with dissolve
    return

label day0_2:
    show bg sidewalk_night at center with dissolve
    window show
    me "『前辈』啊……"
    "我一边回想着和友还有翼的对话，一边露出了诡异的笑容。"
    "要是我今天回去的时间没有那么早，就不能和他们说话了。"
    extend "\n真走运！今天是我的幸运日吗？"
    "我一边这么想着，一边突然看向了前方，\n信号灯此时变成了红色。"
    extend "\n我不由得停在了人行横道和中央分隔带的交叉路口。"
    window hide
    pause 0.3
    window show
    boy3 "咖啡厅吗。到底会是什么样的呢？"
    window hide
    show sora 2 at Position(xpos=120, xanchor=0.0, yalign=0.0) with dissolve
    show sintarou 3 at Position(xpos=300, xanchor=0.0, yalign=0.0) with dissolve
    show tuki 1 at Position(xpos=-90, xanchor=0.0, yalign=0.0) with dissolve
    show sinobu 1 at Position(xpos=520, xanchor=0.0, yalign=0.0) with dissolve
    window show
    "我顺着声音看过去，发现有四名男生正站在原地。"
    extend "\n现在这个时间，应该是刚结束社团活动的御咲学园学生回家的时间吧。"
    "真是走运啊！今天真的很顺。"
    extend "\n机会难得，我决定听听他们的讨论。"
    window hide
    hide sora with dissolve
    hide sintarou with dissolve
    hide tuki with dissolve
    hide sinobu with dissolve
    show sintarou 1 at topright with dissolve
    window show
    boy4 "既然要开咖啡厅，就想要搞得轰轰烈烈啊！！"
    show sintarou 2 with dissolve
    extend "\n王道的话就是女仆咖啡厅，但再加一点小创意的话，\n短裤咖啡厅，体操服咖啡厅什么的也不错啊！"
    extend "\n就算维持学生制服的样子也没问题……。"
    show sora 1 at topleft with dissolve
    boy3 "不，不愧是慎酱，想法真厉害啊……。"
    show sora 3 with dissolve
    boy3 "我啊，想尝试一下店员的穿着\n时尚的衬衫和马甲，\n再系个领结的打扮啊。"
    show sintarou 1 with dissolve
    boy4 "哦哦~执事服吗！！空酱眼光不错！那也很棒啊！！"
    hide sora with dissolve
    hide sintarou with dissolve
    show sora 3 at topright with dissolve
    show sora 2 with dissolve
    sora "哥哥，你觉得怎么样？"
    show tuki 2 at topleft with dissolve
    boy5 "…………"
    show tuki 3 with dissolve
    play sound "fx/impact_japanese.ogg"
    extend "兜裆布咖啡厅。"
    show sora 4 with dissolve
    sora "嗯？抱歉我听不见。"
    hide sora with dissolve
    hide tuki with dissolve
    "嚯。他们也是御咲学园的学生吗。"
    extend "\n咖啡厅的话，和刚才那两人一样，都是二年一班和二班的学生吧？"
    "不过话说回来，每一个都各有魅力……。"
    extend "\n这下我更加期待了！！"
    window hide
    show sinobu 1 at top with dissolve
    window show
    boy6 "……"
    show sinobu 2 with dissolve
    extend "？"
    "我正喘着粗气，好像被察觉到了，\n于是沉默的少年把目光转向了我。"
    "哎呀……我是不是有点太兴奋了。"
    extend "\n啊……但是，那个娇小的男孩子也太可爱了吧。"
    hide sinobu with dissolve
    "我还没来得及多看他几眼，信号灯就变成了绿色，他们走了。"
    window hide
    hide bg with dissolve
    play sound "fx/crowd_noise.ogg"
    show bg shopping_street_night at center with dissolve
    window show
    "他们走过人行横道，进入了热闹的商业街。"
    "呼。兴奋过后，肚子也饿了啊。"
    extend "\n虽然还没到吃晚饭的时间，但是就算我回家了估计饭也还没做好，\n还是去吃个汉堡吧。"
    window hide
    hide bg with dissolve
    return

label day0_3:
    show bg food_shop_night at center with dissolve
    window show
    clerk "点汉堡的客人！让您久等了。"
    "我接过盘子，坐到位置上咬了一口汉堡。"
    window hide
    show sakuya 1 at top with dissolve
    window show
    boy7 "啊~啊，真是麻烦死了。\n为什么非得和一班一起搞什么咖啡店啊。"
    "坐在旁边的少年伸了一个懒腰嘟囔道。"
    hide sakuya with dissolve
    "这个时间段，无论去哪都会有少年。"
    play sound "fx/sparkle.ogg"
    extend "\n这就是正统的美少年黄金时间……"
    extend "\n不对，是天堂时间吧……！"
    show sakuya 6 at topleft
    show saburo 1 at Position(xalign=1.0, ypos=15, yanchor=0.0) with dissolve
    boy8 "嘛，算了算了！"
    extend "\n意味着今后就能和呆毛少年\n更近相处喽！"
    show sakuya 2 with dissolve
    boy7 "猫山……你这家伙真的是，不管讲多少遍都听不懂人话啊。"
    extend "\n你这不是猫而是鸡头吗，长点记性啊你这鸡脑袋！"
    play sound "fx/dash.ogg"
    extend "\n要是下次再敢说这种话，就别怪我不客气了。"
    show saburo 2 with dissolve
    nekoyama "又来了又来了，你就别害羞了作哉君！"
    show sakuya 3 with dissolve
    boy7 "呜……你，你才是，\n最近不是跟一班那变态猫嘴家伙关系很要好吗？"
    extend "\n两只猫的关系很好呢？很亲热啊。"
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    show saburo 3 with dissolve
    nekoyama "不！！！不，不是的！！才不是这样！！\n我们关系一点都不好啊！你，你在说什么啊！！\n白痴吗！！白痴！白痴白痴！！"
    "这人也太让人震惊了。"
    extend "又是他们的朋友啊"
    "话说回来，这男子学校御咲学园的学生居然会有这种对话……"
    "难道说，这是"
    play sound "fx/eureka.ogg"
    show cg adult at center with Dissolve(0.1)
    extend "……ＢＬ！！！？？？"
    play sound "fx/explosion2.ogg"
    "哇噢噢噢噢好厉害！！"
    extend "\n本以为都是二次元限定的事情，\n没想到这玩意真实存在啊！！！"
    "那我　就　得　去　参加　御咲大祭典了啊……！"
    extend "\n说不定，能有命运的邂逅呢。"
    "既然BL存在，那么大人和小孩，而且还是男人之间的禁断之爱\n也不是完全没有萌芽的可能性！！"
    hide sakuya with dissolve
    hide saburo with dissolve
    hide cg with dissolve
    "汉堡也吃了，为了不让别人怀疑\n还是早点回去，不然兴奋要表现出来了。"
    window hide
    hide bg with dissolve
    return

label day0_4:
    stop music fadeout 2.0
    play music "fx/night_insects.ogg"
    show bg residential_area_night at center with Dissolve(1.5)
    pause 0.3
    window show
    "我回到了人烟稀少的住宅区。"
    extend "已经离家很近了。"
    "哈啊……初中生真好啊。"
    extend "特别是二年级！"
    extend "\n现在回想起来，那时是最有活力的时候。"
    extend "\n也习惯了学校生活，也没有进入初高一贯的那种倦怠期。"
    me "啊~要是能回到那时候\n和刚才那些孩子们一起共度校园生活就好了。"
    "虽然是开玩笑。"
    extend "25岁的我却说出了幼稚的话。"
    unknown "我来实现你的愿望吧？"
    me "呜哇！？什么！！？"
    stop music fadeout 1.0
    window hide
    show nori 1 at top with Dissolve(1.0)
    window show
    "我回头看，有个带着帽子的男孩站在我身后。"
    window hide
    play sound "fx/wind.ogg"
    show nori c2 at center with FadeWhite(0.5)
    window show
    unknown "晚上好，下班回来的大哥哥。"
    unknown "最近气温突然降下来了呢。\n前不久的酷暑就像假的一样。"
    extend "\n这种季节的转变，好像会让人身体不适\n所以你要注意哦。"
    me "哈，哈啊？ 说，说的是呢。"
    extend "\n最近，我们公司感冒请假的人也很多呢。"
    "现在的日本，有多少孩子会主动和路边不认识的大人\n闲聊呢。"
    "至少，我从来没有见过这样的人，\n小时候也没干过这样的事。"
    extend "\n倒不如说，现在这个世道让人不安，\n应该被人嘱咐不要和不认识的人扯上关系才对。"
    unknown "大哥哥。这里不太方便，要不换个地方，\n稍微聊一会吧？"
    extend "\n去对面的公园怎么样。"
    me "诶，诶诶！？"
    window hide
    hide nori with Dissolve(1.5)
    hide bg with Dissolve(1.5)
    stop sound fadeout 1.0
    return

label day0_normal_1:
    show bg protagonist_home_night at center with dissolve
    window show
    "呼。终于到家了。"
    play sound "fx/door_open.ogg"
    me "我回来了~。"
    window hide
    play music "nostalgia.ogg"
    show bg living_room_night with Radial(1.2)
    window show
    mother "哎呀，欢迎回来。"
    extend "今天回来得挺早的啊。"
    extend "\n离开饭还有一会儿，等会儿再叫你吧。"
    "厨房传来母亲的应答声。"
    me "哦。今天工作提前做完了。"
    "我在本地公司就职，并没有勉强自己一个人生活，\n而是把生活费交给家里，现在也依然住在家这边。"
    "走进厨房，从冰箱里拿出一瓶冰好的啤酒。"
    mother "哎呀哎呀，一回来就……完全像你爸爸了啊。"
    extend "\n这么年轻就摆出一副老成的样子，\n优秀的女性是不会接近你的哦。"
    me "好好。"
    "对母亲的忠告装作没听见。"
    "抱歉啊，母亲。我对优秀的女性没什么兴趣。"
    play sound "fx/impact_japanese.ogg"
    extend "\n倒是对优秀的少年很感兴趣！！"
    window hide
    hide bg with dissolve
    play sound "fx/door_open.ogg"
    show bg protagonist_room_night at center with dissolve
    window show
    me "呼~累死了。"
    play sound "fx/beer.ogg"
    "我走进自己的房间，坐在床上，喝起了啤酒。"
    me "咕哈~！"
    extend "\n下班后畅饮的啤酒真是太棒了！！"
    "碳酸渗透进疲惫的身体。"
    extend "好爽啊！"
    "话说回来，今天真是与少年结缘了啊～。"
    play sound "fx/paper.ogg"
    extend "\n我看了下友发来的传单。"
    "御咲学园吗……让我回想起了初中时代啊。"
    stop music fadeout 2.0
    "···\n···"
    window hide
    play music "reminiscence.ogg"
    show bg school_sepia with FadeWhite(2.0)
    window show
    "那个时候，我既没好好学习，也没谈过恋爱，\n真的就是只顾着玩了。"
    show bg mountain_sepia with FadeWhite(1.0)
    "跑到附近的森林里探险，骑自行车到邻镇去……。"
    extend "\n嗯嗯，果然最无忧无虑的初中二年级，就是玩得最开心的时候啊。"
    show bg classroom_sepia with FadeWhite(1.0)
    "嗯……我初中二年级时班上做了什么项目来着？"
    extend "\n……对了对了，鬼屋。"
    extend "\n我扮演了鬼，而且我还挺喜欢扮演鬼的，周围人都对我的扮相赞不绝口。"
    "不知道我自制的那个鬼面具，现在扔哪去了。"
    extend "\n嗯……估计早就扔了吧。"
    "然后是，后夜祭的篝火晚会……"
    window hide
    play sound "fx/fire.ogg"
    show bg campfire with Radial(1.0)
    window show
    extend "那真是漂亮啊。"
    extend "\n我现在都能清楚地回忆起来。"
    window hide
    stop sound fadeout 0.5
    show bg school_sepia
    window show
    "啊……好想再回到那个时候，想在学园祭上大闹一番。"
    "学园祭当天是挺开心的，\n但之前的准备时间也挺愉快的。"
    extend "\n在学园祭一星期前，学园会放掉下午的课程和社团活动。\n在放学后，直到天黑为止，我都会在学校和朋友们一起行动。"
    "今天，在我回到家之前，我看到的御咲学园的学生们，\n从明天开始，肯定会过上比平时更加开心的校园生活。"
    "啊……真棒啊~。"
    window hide
    show bg protagonist_room_night with FadeWhite(2.0)
    window show
    "···"
    "然后，和传单一起拿出的另一样东西。\n是那个谜之美少年给我的糖。"
    window hide
    stop music fadeout 2.0
    show 飴 c4 at center with dissolve
    window show
    "不管是什么愿望都可以实现的糖啊……。"
    "反正不过就是中二病发作的人恶作剧而已，\n刚好我手边缺点下酒菜，就吃了吧。"
    "我把糖扔进嘴里，咬碎，咽了下去。"
    extend "\n它的味道，难以形容，就像是随处可见的普通糖果。"
    window hide
    hide 飴 with dissolve
    window show
    me "哈哈……完全不搭啤酒啊。"
    "虽然现在的生活也不错，"
    extend "\n但是以前的小孩子的生活还是很棒的啊。"
    extend "\n那种快乐，如今再也不会感受到了。"
    "……糟了，今天醉得比平时快啊。"
    extend "\n一下子就睡着了。"
    "……现在想起来，刚刚吃的糖，不是什么毒品之类的危险东西吧。"
    extend "\n没问题的吧，御咲治安好，而且那孩子也还可爱。"
    "啊啊……今天要是能梦到初中时代就好了。"
    extend "\n那样的话"
    extend "……"
    extend "……"
    extend "……"
    hide bg with DefocusBlack(5.0)
    "Zzz"
    window hide
    return

label day0_tomo_before:
    show tomo 12 at top with DefocusBlack(2.5)
    window show
    "嗯……？ 请问您是……。"
    window hide
    show tomo 1 with dissolve
    return

label day0_tubasa_before:
    show tubasa 1 at top with DefocusBlack(2.5)
    window show
    "嗯……？ 请问您是……。"
    window hide
    show tubasa 3 with dissolve
    return

label day0_sinobu_before:
    show sinobu 4 at top with DefocusBlack(2.5)
    window show
    "嗯……？ 请问您是……。"
    window hide
    show sinobu 5 with dissolve
    return

label day0_tuki_before:
    show tuki 2 at top with DefocusBlack(2.5)
    window show
    "嗯……？ 请问您是……。"
    window hide
    show tuki 6 with dissolve
    return

label day0_sora_before:
    show sora 7 at top with DefocusBlack(2.5)
    window show
    "嗯……？ 请问您是……。"
    window hide
    show sora 2 with dissolve
    return

label day0_sintarou_before:
    show sintarou 3 at top with DefocusBlack(2.5)
    window show
    "嗯……？ 请问您是……。"
    window hide
    show sintarou 4 with dissolve
    return

label day0_saburo_before:
    show saburo 1 at top with DefocusBlack(2.5)
    window show
    "嗯……？ 请问您是……。"
    window hide
    show saburo 2 with dissolve
    return

label day0_sakuya_before:
    show sakuya 6 at top with DefocusBlack(2.5)
    window show
    "嗯……？ 请问您是……。"
    window hide
    show sakuya 4 with dissolve
    return

label day0_tomo_after:
    window show
    show tomo 4 with dissolve
    boy1 "真是谢谢你了！[player_surname][player_name]前辈！！"
    extend "\n那我走了！！"
    "等等……  你是……。"
    hide tomo with DefocusBlack(2.5)
    "Zzz"
    window hide
    return

label day0_tubasa_after:
    window show
    show tubasa 4 with dissolve
    boy2 "真是非常感谢。[player_surname][player_name]桑。"
    extend "\n那我就先走了……。"
    "等等……  你是……。"
    hide tubasa with DefocusBlack(2.5)
    "Zzz"
    window hide
    return

label day0_sinobu_after:
    window show
    show sinobu 3 with dissolve
    boy6 "我知道了，非常感谢，[player_surname][player_name]桑。"
    extend "\n那我走了。"
    "等等……  你是……。"
    hide sinobu with DefocusBlack(2.5)
    "Zzz"
    window hide
    return

label day0_tuki_after:
    window show
    show tuki 4 with dissolve
    boy5 "谢谢。[player_surname][player_name]桑。   是吧"
    extend "\n那我就先走了。"
    "等等……  你是……。"
    hide tuki with DefocusBlack(2.5)
    "Zzz"
    window hide
    return

label day0_sora_after:
    window show
    show sora 1 with dissolve
    boy3 "谢谢了。[player_surname][player_name]小哥。"
    extend "\n那么，再见。"
    "等等……  你是……。"
    hide sora with DefocusBlack(2.5)
    "Zzz"
    window hide
    return

label day0_sintarou_after:
    window show
    show sintarou 2 with dissolve
    boy4 "ＯＫ！[player_surname][player_name]再见！"
    extend "\n我不会把这东西用来做奇怪的事情的，请放心吧♪ 那么再见！"
    "等等……  你是……。"
    hide sintarou with DefocusBlack(2.5)
    "Zzz"
    window hide
    return

label day0_sakuya_after:
    window show
    show sakuya 5 with dissolve
    boy7 "您好。[player_surname][player_name]学长！"
    extend "\n那么，再见。"
    "等等……  你是……。"
    hide sakuya with DefocusBlack(2.5)
    "Zzz"
    window hide
    return

label day0_saburo_after:
    window show
    show saburo 5 with dissolve
    boy8 "谢谢，[player_surname][player_name]桑！"
    extend "\n那么，再见~！"
    "等等……  你是……。"
    hide saburo with DefocusBlack(2.5)
    "Zzz"
    window hide
    return

label day0_hidden:
    play music "fx/wind.ogg"
    show bg residential_area_night at center
    show nori 4 at top with dissolve
    window show
    me "等，等一下！ 你说的我跟不上啊。"
    extend "\n额…… 你究竟是哪来的小孩啊？"
    me "已经到晚饭时间了吧？"
    extend "\n不赶快回家的话，家里的人会担心的哦。"
    me "不然的话~"
    play sound "fx/boing.ogg"
    extend "你就会被像小哥这样有怪趣味的人，\n诱拐了哦~！"
    "我一边开玩笑地威胁一边想要摸他的头，"
    play sound "fx/wind_slash.ogg"
    hide nori with dissolve
    extend "\n少年却拒绝了，把我的手挥开了。"
    window hide
    show nori 5 at top with dissolve
    window show
    unknown "多谢您多余的担心。"
    show nori 6 with dissolve
    extend "\n但是，您管的有些太宽了哦，恶趣味的大哥哥。"
    play sound "fx/cute2.ogg"
    "哦哦，挺会说话的嘛。真是让人受不了。"
    show nori 4 with dissolve
    unknown "你不用在意我身边的事情。"
    extend "\n我只是想和小哥你说话而已。"
    me "虽然很不好意思拒绝你难得的邀请，\n但我现在只想回家好好休息。"
    extend "\n所以，不好意思了。"
    show nori 7 with Dissolve(0.8)
    unknown "……这样啊。"
    extend "\n那也没办法了呢。"
    me "嗯！能理解就好。"
    extend "\n那么，我先走了。"
    extend "\n虽然有点多管闲事，但我还是希望你能早点回家。"
    "说着，我从那孩子身边走开，继续前进。"
    window hide
    hide nori with dissolve
    stop music fadeout 0.5
    show cg telephone_pole_night at center with dissolve
    window show
    unknown "你打算去哪里呢？"
    extend "\n没办法了，只能用强硬的手段了哦。"
    me "诶？"
    window hide
    play sound "fx/wind_slash.ogg"
    show cg c89 with FadeWhite(0.5)
    play music "pinch.ogg"
    window show
    "这时，有什么东西缠住了我的身体。"
    play sound "fx/dash.ogg"
    extend "\n这，这是什么啊？！动弹不得！！！"
    "不是……绳子。"
    extend "\n又黏又滑，自己在扭动。"
    "触手……？"
    unknown "哎呀呀……虽然不想在住宅区使用这种方法。"
    extend "\n要是你乖乖吃下这颗含着安眠药的糖就好了……。"
    play sound "fx/fall_down.ogg"
    me "呜咕咕咕咕！！"
    "嘴被封住了，发不出声音。"
    unknown "就算你呼救也无济于事的哦。"
    extend "\n……很害怕吧。这表情真棒。"
    extend "\n明明肯吃糖，做着美梦就会结束了，\n真是作茧自缚呢。"
    unknown "虽然我不喜欢这种风险高的选择，\n但是能看到你这样的表情，也无所谓了。"
    extend "\n可惜我听不到悲鸣声……那就以后再说吧。"
    extend "\n那我就按照你所说的，回我的家吧。"
    "少年这样说着指向我，与此同时，张着更大口的触手，\n就像热吻一样交缠着我的舌头，钻进了我的口腔。"
    show cg remarkable with FadeWhite(0.5)
    me "嗯咕！？唔咕咕咕！？？！"
    "好恶心……咕啾咕啾的液体钻进了我的嘴里。"
    stop music fadeout 4.0
    me "嗯嗯……嗯唔…。"
    "渐渐地，我的意识开始模糊，视线也朦胧起来。"
    hide cg with DefocusBlack(5.0)
    hide nori with DefocusBlack(5.0)
    hide bg with DefocusBlack(5.0)
    pause 0.4
    "···。"
    window hide
    show bg residential_area_night at center with Radial(0.7)
    show nori 8 at top with Dissolve(0.7)
    window show
    unknown "晚安，大哥哥。"
    extend "\n我会换个地方，让你好好享受的。"
    window hide
    hide nori with Dissolve(0.9)
    hide bg with Dissolve(0.9)
    return

label day0_normal:
    play music "nori_theme.ogg"
    show bg park_night at center with Dissolve(1.5)
    show nori 4 at top with Dissolve(0.9)
    window show
    "我被少年牵着，走到了公园里。"
    "这个少年仔细一看是个美少年啊。"
    "视线往下移，一边说着好冷啊，一边却穿着短裤！！"
    extend "\n毕竟孩子是风的子民啊！"
    play sound "fx/eureka.ogg"
    extend "Good！！"
    "被这样的小孩子搭话，说实话是非常开心的事，"
    extend "\n不过毕竟发展太快，一时无法理解。"
    "总之先冷静下来。深呼吸。"
    window hide
    pause 0.3
    window show
    me "……呼。所以，你找我有什么事吗？"
    show nori 3 with dissolve
    unknown "刚才，你嘀咕的愿望\n我打算帮你实现。"
    me "诶……？啊，嗯……诶？？"
    "我情不自禁地发出了怪叫。"
    "实现愿望？"
    extend "\n他到底在说什么？"
    "难道说，这就是这个年龄的必经之路「中二病」吗？"
    me "诶……你到底是从哪来的啊？"
    extend "\n不是快到晚饭时间了吗？\n再不快点回家的话，家里的人会担心的哦。"
    me "不然的话~"
    play sound "fx/boing.ogg"
    extend "你就会被像小哥这样有怪趣味的人，\n诱拐了哦~！"
    "我一边开玩笑地威胁一边想要摸他的头，"
    play sound "fx/wind_slash.ogg"
    hide nori with dissolve
    extend "\n少年却拒绝了，把我的手挥开了。"
    window hide
    show nori 5 at top with dissolve
    window show
    unknown "多谢您多余的担心。"
    show nori 6 with dissolve
    extend "\n但是，您管的有些太宽了哦，恶趣味的大哥哥。"
    play sound "fx/cute.ogg"
    "哦哦，挺会说话的嘛。真是让人受不了。"
    show nori 4 with dissolve
    unknown "回到刚才的话题吧。\n"
    window hide
    play sound "fx/battle3.ogg"
    show 飴 c3 at center with Radial(0.5)
    window show
    extend "我手上的这颗糖果，其实是一种魔法糖果哦。"
    unknown "吃了这种糖果的人，\n无论是什么样的愿望都能实现哦。"
    "我哑然无语地站在原地。"
    "你说是……魔法糖？"
    "少年手里的这个，\n是便利店或者超市的零食区卖的再普通不过的糖球。"
    unknown "看来您还不能相信我的话呢。"
    extend "这也在所难免。"
    extend "\n突然被一个素不相识的人搭话，\n要你相信他所说的这些话，这实在是太强人所难了啊。"
    "少年继续流畅地说道。"
    window hide
    hide 飴 with dissolve
    hide nori with dissolve
    show nori 1 at top with dissolve
    window show
    unknown "不过，还请稍微动动脑子想想。"
    extend "\n这位小哥，你至今为止的人生中，\n可曾有过像这样在路边被搭话，然后得到了能实现愿望的东西？"
    unknown "没有吧？"
    extend "\n这种，如同故事的开始一般的事。"
    me "是，是啊……。"
    "的确，突然眼前会出现一个谜之男子，"
    play sound "fx/knife.ogg"
    show cg dark at center with Dissolve(0.3)
    extend "\n然后说『戴上这眼镜的话~』，"
    play sound "fx/sparkle.ogg"
    show cg adult with FadeWhite(0.3)
    extend "『和我签订契约吧~』之类的，"
    hide cg with dissolve
    extend "\n这种唐突地搭话的桥段，在漫画和动画中经常看到，"
    "如今，在我面前发生的事，就相当于这些吗！？"
    show nori 5 with dissolve
    unknown "哼哼。这就要取决于你了哦。\n是否开启这段故事……。"
    extend "\n那么，我就此告辞了。"
    hide nori with dissolve
    me "啊，哎？\n结果，那糖果不给我吗？"
    show nori 2 at top with dissolve
    unknown "糖果，其实已经到你的口袋里了哦。"
    extend "\n那么，晚安。"
    extend "\n我祈祷你能看见美妙的梦。"
    "说完，少年融入了黑暗中。"
    window hide
    stop music fadeout 2.0
    hide nori with Dissolve(1.5)
    window show
    "我将手伸进裤兜，摸到了装有小块糖果的透明小袋。"
    me "完全没察觉……这孩子。。"
    "我回想起不久前还在身边的那名少年的面容。"
    extend "\n但是，那孩子很可爱啊。"
    show cg telephone_pole_night at center with Dissolve(0.6)
    "……不如说，我更想和他，多聊聊，\n这是我想去实现的愿望。。"
    window hide
    hide bg with Dissolve(1.0)
    hide cg with Dissolve(1.0)
    return

label day0_hidden_1:
    window show
    "···"
    window hide
    show bg dungeon at center with DefocusWhite(2.4)
    play music "fx/cave_ambience.ogg"
    window show
    me "嗯……这里是……？"
    "不知从何处传来的滴水声，唤醒了我鲜明的意识。"
    extend "\n周围昏暗一片，只有一根小小的蜡烛散发着光芒。"
    extend "\n这潮湿的空气，令人感到不快。"
    "这里是，什么地方……？"
    extend "\n我应该是从车站步行回家的……。"
    extend "\n是的……在那里，被那名神秘的少年搭话了……！"
    "……嗯？"
    window hide
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 60, 0.15, 0.1), layer='master')
    window show
    me "这是什么！！？？"
    "我被捆绑在椅子上，手脚都被固定住了。"
    extend "\n并且，捆绑着我的，毫无疑问是触手。"
    me "触手……。"
    extend "这不是梦吗……？"
    unknown "什么嘛。已经醒了吗？"
    "神秘的少年从黑暗深处现出身影。"
    stop music fadeout 0.5
    window hide
    play music "nori_theme.ogg"
    show nori 9 at top with Dissolve(0.9)
    window show
    unknown "果然，这些孩子的体液对于成人来说效果太差了。"
    extend "\n这样的话，就会留下更多的多余记忆呢。"
    extend "\n要是再继续下去，事后处理就麻烦了。\n得赶紧开始实验。"
    window hide
    hide nori with dissolve
    play sound "fx/dash.ogg"
    window show
    me "你，你！！！\n是你对我做了那种事吗？！"
    extend "\n这是怎么回事！什么情况啊！！"
    play sound "fx/wow2.ogg"
    me "难道说，你是想拍捆绑系的素人AV吗！？"
    extend "\n你是靠自己幼小的外表来钓男孩子的狩猎者吗！！？"
    extend "\n虽然这话有些自说自话，但我的身体可没那么漂亮！"
    play sound "fx/eureka.ogg"
    me "嗯？这么说来，你还有其他工作人员吗？"
    extend "\n咦？相机呢！？没有相机啊！！"
    extend "\n难道说，要用隐藏摄像头来拍摄吗？？"
    extend "\n觉得被拍摄的羞耻感很棒吗！！？"
    show nori 10 at top with dissolve
    unknown "你在说什么呢。"
    extend "\n才刚醒过来而已，倒是挺有精神的嘛。"
    play sound "fx/boing.ogg"
    me "听好了啊！你所做的事情可是严重的犯罪啊！！"
    extend "\n就算是孩子，犯了罪也会被送入少年管教所的！"
    extend "\n要是再继续做下去的话，你也会变成那个样子的哦！！"
    extend "\n现在的话，还有补救的机会，所以马上放了我！"
    show nori 11 with dissolve
    unknown "你真是能说会道呢。"
    extend "\n我不是说过不用担心我吗。"
    "少年并没有被我说的话所动摇，反而用着轻蔑的表情对我笑着。"
    play sound "fx/triangle.ogg"
    extend "\n虽然很不甘心，但我被他吸引了！！"
    show nori 12 with dissolve
    unknown "请放心。\n我不会做取人性命那种粗暴的事。"
    extend "\n等实验结束之后，我会消除记忆，让你回家的。"
    extend "\n在那之前，我会让你作为实验对象协助我……。"
    me "你，你在说什么……"
    show nori 9 with dissolve
    unknown "你现在有想要实现的梦想吗？"
    extend "\n有想要实现的世界吗？"
    extend "\n请想象着这些，许愿吧。"
    me "想要实现……？"
    extend "实现……？"
    show nori 13 with dissolve
    unknown "只要抱有欲望和强大的执念，就会成为能量。"
    show nori 11 with dissolve
    extend "\n那么，请闭上眼睛……想象吧。"
    extend "\n就好像是你为了消除这一天的疲劳，\n躺到了床上，开始期待着接下来会做的梦一样！"
    "这孩子在说什么……？"
    play sound "fx/cute3.ogg"
    extend "\n我完全听不懂。"
    window hide
    hide nori with dissolve
    window show
    "已经无所谓了……随便怎样都好。"
    "反正只要想象着想要做的梦然后睡着就行了。"
    extend "\n这样的话应该就会没事了吧。"
    extend "\n想要做的梦……"
    play sound "fx/sparkle.ogg"
    show cg adult at center with FadeWhite(0.5)
    extend "果然还是跟可爱的小男孩卿卿我我的梦啊……。"
    "……嗯，很顺利。快要睡着了啊~。"
    extend "\n虽然手脚被束缚着有些违和感……。"
    window hide
    hide cg with dissolve
    hide nori with dissolve
    hide bg with dissolve
    play sound "fx/wind_slash.ogg"
    window show
    "呜ーーーーーー嗯"
    "嗯，这机械声是哪来的？"
    extend "\n啊~这个，是某种实验来着。"
    extend "\n他说不会做危险的实验，肯定没问题吧。"
    extend "\n嗯……睡吧……。"
    stop music fadeout 4.0
    "·"
    pause 1.0
    "·"
    pause 1.0
    "·"
    pause 1.0
    play sound "fx/eureka.ogg"
    show bg remarkable at center with FadeWhite(0.5)
    unknown "幻象火焰！！！！！！！！！"
    window hide
    play sound "fx/battle3.ogg"
    show bg campfire_sparks with FadeWhite(0.4)
    pause 0.6
    play sound "fx/phantom_fire.ogg"
    show bg phantom_fire with Radial(0.4)
    window show
    "砰啊啊啊啊啊啊啊啊啊！！！！！！"
    window hide
    show bg dungeon at center with FadeBlack(0.2)
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 60, 0.15, 0.1), layer='master')
    window show
    me "呜哇！！ 什么！？！？"
    extend "\n喂！！声音太大了我睡不着啊！！！"
    show nori 14 at top with dissolve
    unknown "这个声音，不是我弄的。"
    extend "\n话说回来，那个声音……来了啊。"
    hide nori with dissolve
    "橙色头发的少年从漫天尘土中现身。"
    window hide
    show yuuhi 1 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    play music "pinch.ogg"
    window show
    unknown "呀，朔！！！！\n你又在干坏事了！！"
    extend "\n现在马上把人给我放开！！"
    hide yuuhi with dissolve
    show nori 15 at topleft with dissolve
    nori "欢迎你，炎之魔法师 夕阳。"
    extend "\n每次都是这样，你的鼻子真是像狗一样灵呢。"
    extend "\n还是说……你忘不掉那天被触手吞没，\n烙印在身上的快感？"
    show yuuhi 2 at topright with dissolve
    yuuhi "这……怎么可能嘛，你个恶趣味的家伙！！！"
    show yuuhi 3 with dissolve
    extend "\n而且你的行为总是那么大胆！！"
    extend "\n你这小孩居然向大人搭讪，还把人拘禁起来，自顾自在那里唧唧歪歪！"
    show nori 16 with dissolve
    nori "哎呀，你明明早就发现了，却故意不救他，\n还利用他来寻找我的藏身处……"
    extend "\n居然为了满足私欲，就让你庇护的普通市民陷入恐慌，\n真是有够冷酷的啊。"
    show yuuhi 4 with dissolve
    yuuhi "切！！你以为我想找到你家吗！"
    extend "\n我只是因为火焰魔法在住宅区不能用……仅此而已！"
    show yuuhi 5 with dissolve
    extend "\n你再稍微动一下脑子啊，你这下流混蛋！！"
    show nori 17 with dissolve
    nori "唔……。"
    "至此，朔那从容的表情第一次阴沉下来。"
    show yuuhi 6 with dissolve
    yuuhi "那边的小哥。\n你再稍微在那里等一会儿！"
    extend "\n我现在就去把这下流混蛋给打趴，然后救你！！"
    window hide
    play sound "fx/running.ogg"
    hide yuuhi with dissolve
    hide nori with dissolve
    show nori 10 at top with dissolve
    window show
    nori "现在比起实验，应该优先对付夕阳……"
    extend "\n你那强烈正义感的内心，看上去应该很有能量。"
    extend "\n那我当然不能错过。"
    show nori 11 with dissolve
    extend "\n……而且，我好想再看到你沉溺于快乐而露出一副哭丧脸啊！"
    window hide
    play sound "fx/impact.ogg"
    show cg c90 at center with FadeWhite(0.5)
    window show
    "说完，"
    play sound "fx/battle1.ogg"
    "朔拿出几把小刀，向夕阳扔了过去。"
    play sound "fx/battle2.ogg"
    show cg c90 with FadeWhite(0.5)
    extend "\n朔的触手与小刀纷至沓来，战斗一触即发，"
    play sound "fx/battle4.ogg"
    show cg c90 with Radial(0.5)
    extend "夕阳便释放火焰魔法与之缠斗。"
    "这…难道不是做梦吗……。"
    extend "\n比起我那些逼真的梦，眼前这景象，才更像是场梦一样"
    me "……我换一个积极点的想法吧。"
    extend "\n他们肯定都很喜欢我，喜欢到无法自拔\n然后为了我展开了激烈的争夺…啊哈哈。"
    play sound "fx/boing.ogg"
    extend "\n我…真是个罪孽深重的男人啊……啊哈哈哈……"
    play sound "fx/tadaa.ogg"
    me "加油啊。你们俩都加油啊。"
    extend "\n然后把我的心偷走吧。"
    extend "\n要是一起偷走我的心也没问题啊~。"
    window hide
    hide cg with dissolve
    hide yuuhi with dissolve
    hide nori with dissolve
    show nori 16 at top with dissolve
    window show
    nori "『一起偷走』……？"
    extend "\n是啊……\n再这样下去也没有办法解决，看来还是把大哥哥拿出来用"
    show nori 12 with dissolve
    extend "\n才能处于有利的局面。"
    me "诶？"
    "朔对我的话有所反应，打量着我，露出了下流的笑容。"
    hide nori with dissolve
    play sound "fx/wind_slash.ogg"
    extend "\n然后，束缚住我的触手开始移动，把我带到了朔的面前。"
    window hide
    play sound "fx/knife.ogg"
    show cg c91 1 at center with FadeWhite(0.5)
    window show
    "咔嚓"
    "朔将刀刃抵在了我的脖子上。"
    me "诶……那，那个，朔先生……。"
    extend "\n不，刚才你不是说…不会做什么危险的事吗……。"
    nori "啊……对不起。"
    extend "\n由于有人来碍事，所以不得不撤回刚才的发言。"
    extend "\n既然我已经挥舞着刀，就不用说危不危险什么的了。"
    extend "\n如果要恨的话，就恨那个魔术师吧。"
    me "啊，好的……这样啊…。"
    play sound "fx/dash.ogg"
    yuuhi "啊！！ 你这家伙，这种说法也太脏了吧！"
    extend "\n这种时候应该多动动脑子，你不觉得羞耻吗！！"
    extend "\n真是受不了……一边考虑解救人质一边战斗真是麻烦，\n我最不擅长动脑了…。"
    show cg c91 2 with dissolve
    nori "头脑不应该是用来戴帽子的……是用来思考的，夕阳。"
    extend "\n好了，用你那软弱的脑袋打破这个状况吧！"
    extend "\n还是说要老老实实地落到我手里，成为快乐的俘虏呢？"
    stop music fadeout 2.5
    extend "\n自诩正义的伙伴真是太可笑了……淫荡的魔术师君。"
    window hide
    hide nori with dissolve
    hide cg with dissolve
    show yuuhi 7 at topleft with dissolve
    play music "hurry_up.ogg"
    window show
    yuuhi "唔……！！"
    extend "\n你这家伙，不也是经常露出显眼的破绽吗？"
    extend "\n难道你就很适合演反派吗？"
    show nori 14 at topright with dissolve
    nori "……真是以自我为中心的低劣想法呢。"
    extend "\n对于我们的正义而言，你才是反派哦，夕阳。"
    show yuuhi 8 with dissolve
    yuuhi "说到底，你什么意思啊！从刚才开始就一直在说些下流的话！！"
    extend "\n你脑子里都是那种东西吗！你这，下流无耻惹事精！！"
    show nori 18 with dissolve
    play sound "fx/boing.ogg"
    nori "少，少废话！"
    show yuuhi 5 with dissolve
    yuuhi "你看，一有什么不顺心的事，\n就用一句「少废话」打发过去……。"
    show nori 17 with dissolve
    play sound "fx/boing.ogg"
    nori "吵死了！！"
    show yuuhi 4 with dissolve
    yuuhi "不就是换个说法而已嘛！"
    extend "\n总是用这种粗暴的手段，总有一天会露出马脚的哟~？"
    window hide
    hide nori with dissolve
    hide yuuhi with dissolve
    window show
    "我被两个人丢在一边，争吵持续着。"
    "……嗯，"
    play sound "fx/eureka.ogg"
    extend "你们两个，干脆结婚不就完了么！！"
    extend "\n我一边期待着BL展开，一边想着接下来该怎么做。"
    hide nori with dissolve
    hide yuuhi with dissolve
    return

label day0_hidden_nori:
    show bg dungeon at center
    stop music fadeout 0.5
    play music "infiltration.ogg"
    window show
    me "夕，夕阳君，你冷静一下。"
    extend "\n这次，朔君是在做某种实验，\n虽然形式上是这样，但其实我只是在帮他忙。"
    window hide
    show yuuhi 3 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    window show
    yuuhi "哎！？"
    extend "\n可，可是，他强行把你带来这里啊……。"
    play sound "fx/impact.ogg"
    show cg remarkable at center with FadeWhite(0.5)
    me "能被这样的美少年监禁，求之不得！！！！！"
    play sound "fx/impact.ogg"
    "求之不得！！！\n"
    pause 0.5
    play sound "fx/impact.ogg"
    "求之不得！\n"
    pause 0.5
    play sound "fx/impact.ogg"
    "求之不得……。"
    window hide
    hide cg with dissolve
    hide yuuhi with dissolve
    window show
    play sound "fx/triangle.ogg"
    "……。"
    "我豁出去的喊声在地下室里回响。"
    me "唔……"
    extend "嘛，就只是这样而已，所以我没事的。"
    extend "\n所以，请放心吧。"
    window hide
    show yuuhi 7 at topleft with dissolve
    window show
    yuuhi "但，但是……"
    show nori 15 at topright with dissolve
    nori "呵呵……哥哥你这话说得太好了。"
    show nori 11 with dissolve
    extend "\n哎呀？\n那边那个自称为正义魔术师的，看来是无法接受吧。"
    me "……朔，能把耳朵靠过来吗？"
    hide nori with dissolve
    hide yuuhi with dissolve
    show nori 12 at top with dissolve
    nori "可以。有什么事吗？"
    "朔把耳朵凑了过来。"
    play sound "fx/cute2.ogg"
    extend "\n他的头发有一股香味。"
    window hide
    hide nori with dissolve
    show yuuhi 1 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    window show
    yuuhi "喂，喂！你们在干什么！！"
    hide yuuhi with dissolve
    show nori 14 at top with dissolve
    play sound "fx/knife.ogg"
    nori "请不要动。"
    extend "还是说无论我怎么处置这男人，你都无所谓了？"
    hide nori with dissolve
    show yuuhi 2 at top with dissolve
    yuuhi "呜……。"
    window hide
    hide yuuhi with dissolve
    hide nori with dissolve
    window show
    me "事已至此，只有将夕阳抓去，进行实验了。"
    extend "\n我刚刚想出一个好办法。"
    show nori 12 at top with dissolve
    nori "哦……好吧。"
    extend "\n如果实验成功的话，就奖励你好喝的红茶。"
    extend "\n那么，能说一下你的妙计吗？。"
    hide nori with dissolve
    "（窃窃私语声）"
    window hide
    show yuuhi 1 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    window show
    yuuhi "喂，你们在干什么！！"
    hide yuuhi with dissolve
    show nori 11 at top with dissolve
    nori "哎呀……失礼了。"
    extend "\n他想回去的理由太令人感动了，\n我一时没控制住，凑过去听了一下……。"
    show nori 9 with dissolve
    nori "实验对象就去寻找其他人吧。"
    extend "\n虽然有点不甘心，但是这次我就放弃吧。"
    extend "\n大哥哥，你可以去夕阳那里了。"
    extend "\n夕阳，把这孩子带回家吧。"
    hide yuuhi with dissolve
    hide nori with dissolve
    hide bg with dissolve
    play sound "fx/fall_down.ogg"
    "说完，束缚着我身体的触手就放开了我。"
    window hide
    show bg dungeon at center with dissolve
    show yuuhi 3 at top with dissolve
    window show
    yuuhi "诶……"
    show yuuhi 1 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    extend "哈，哈！？这，这是怎么回事啊！！"
    extend "\n因为这次的人质很可怜，所以想把人换掉吗？"
    me "至少这次你把我救出去了，这不挺好的嘛。"
    extend "\n夕阳君也和我一起赶快离开这儿，\n对朔君的惩罚，就留到下次再做吧！"
    extend "\n好了，快走吧！！把我带出去。"
    show yuuhi 3 with dissolve
    yuuhi "不，可，可是……。"
    me "快点快点！"
    hide yuuhi with dissolve
    "我强行拉住夕阳的双手，让他背对着我。"
    "然后，大喊道。"
    stop music fadeout 0.5
    show cg remarkable at center with FadeWhite(0.5)
    me "朔，就是现在！！"
    window hide
    play sound "fx/wind_slash.ogg"
    show cg c89 with FadeWhite(0.5)
    window show
    "咻噜噜噜噜！！！"
    "触手捉住了背向这边，手被控制的夕阳。"
    window hide
    play sound "fx/impact_japanese.ogg"
    show cg c93 1 with FadeWhite(0.5)
    play music "hurry_up.ogg"
    window show
    play sound "fx/boing.ogg"
    yuuhi "哇啊！？！？什么情况啊！？！？"
    extend "\n快放开我啦！！！可恶啊！！\n你们竟然骗了我啊！！！！"
    nori "哼……居然会中这种战术，你果然蠢。"
    extend "\n好不容易抓到的实验对象，怎么能就这么放了他呢。"
    extend "\n还是说，你以为我真的被他感动，改变主意？"
    extend "\n好了，大哥哥，要怎么折磨这个魔术师呢？"
    me "折磨……玩弄他如何？"
    nori "当然。"
    extend "\n你看看……他那狼狈的样子。"
    extend "\n要好好利用这好不容易才得到的机会。"
    extend "\n在我动手之前，我想把这个优先权交给出谋者的您。"
    me "唔，嗯……"
    "我看着夕阳被触手束缚的样子。"
    "确实，这个光景我妄想过无数次。"
    extend "\n但是，一来到眼前，就令人意外地动弹不得。"
    extend "\n而且，这个孩子是为了救我才来到这里的。"
    extend "\n要我做这种恩将仇报的事吗……。"
    nori "大哥哥，人类谁都有黑心。"
    extend "\n在这种情况下，不需要被罪恶感折磨哦。"
    extend "\n大哥哥你其实也想这么做吧……？"
    play sound "fx/cute3.ogg"
    "唔……。"
    "朔的挑衅让我几乎要答应了。"
    window hide
    hide yuuhi with dissolve
    hide cg with dissolve
    show nori 15 at top with dissolve
    window show
    nori "那么我告诉你一件好事。"
    extend "\n其实……那个魔术师，\n穿着很不得了的内裤哦。"
    play sound "fx/explosion2.ogg"
    me "很，很很很很不得了的内裤！！？！\n那是什么东西啊！！？"
    extend "\n话说为什么朔你知道啊！？"
    show nori 16 with dissolve
    nori "别，别在意这种小事！"
    show nori 12 with dissolve
    extend "\n什么样的内裤，请用你自己的眼睛去确认。"
    extend "\n好了，只要你下命令的话，触手就会按你说的行动。"
    me "呜咕……呜呜呜呜呜……。"
    show nori 9 with dissolve
    nori "还是快点决定比较好……这段时间不会永远持续下去。"
    extend "\n对他来说，你已经变成叛徒了。"
    extend "\n他可能会把你牵扯进来，然后进行反击。"
    me "呜嗯咕呜呜呜呜呜呜……。"
    play sound "fx/cute2.ogg"
    extend "\n对，对不起！夕阳君！！！"
    extend "\n能把那条短裤脱下来，让我看看你穿的是什么内裤吗？"
    show nori 11 with dissolve
    nori "没错，夕阳。"
    extend "\n哥哥似乎对你那色情的内裤很感兴趣哦。"
    window hide
    show cg c93 1 at center with FadeWhite(0.5)
    window show
    play sound "fx/boing.ogg"
    yuuhi "你，你们在说什么啊，这群变态！！！！"
    extend "\n快放开我！！"
    extend "\n再，再继续下去的话……！"
    nori "继续下去，是指？"
    extend "\n用魔法进行反击的话，大哥哥也会被波及的。"
    extend "\n作为自己遭背叛的报复，让一般人受伤这种事，\n正义的伙伴是不能做的对吧？"
    "听到这话后，夕阳气馁地垂下了头。"
    show cg c93 2 with dissolve
    yuuhi "呜呜呜呜……我知道了，我知道了啦！"
    extend "\n是我多管闲事了……。"
    extend "\n我向你道歉，所以真的请你停下来……！！"
    nori "大哥哥，你打算怎么做？"
    me "唔，嗯……也是呢。"
    extend "\n那让我稍微看一下！"
    play sound "fx/dash.ogg"
    extend "\n拜托了！？ 仅此而已，仅此而已！！"
    nori "……真是拼命呢。你的罪恶感呢？"
    play sound "fx/cute.ogg"
    me "吵，吵吵吵吵死了！！\n人类一失去可以得到的东西，就会突然开始珍惜！"
    play sound "fx/sparkle.ogg"
    extend "\n这么梦幻的，触手×正太的场景……\n除了好好享用，还能怎么办呢！？"
    play sound "fx/wind_slash.ogg"
    show cg c89 with FadeWhite(0.5)
    me "来吧，触手君！！"
    stop music fadeout 2.0
    play sound "fx/explosion3.ogg"
    extend "\n只是一会儿就好，把短裤给我脱下来！！！"
    window hide
    show cg c93 3 with Radial(0.5)
    window show
    "偷瞄"
    play music "bwv147.ogg"
    show cg adult with FadeWhite(0.5)
    "……。"
    "黑色比基尼真是吓人一跳……。"
    extend "\n多谢款待！！"
    hide cg with dissolve
    hide yuuhi with dissolve
    hide nori with dissolve
    hide bg with dissolve
    "下一刻，我突然喷鼻血了。"
    stop music fadeout 3.0
    play sound "fx/fall_down.ogg"
    nori "诶！？"
    window hide
    show bg dungeon at center with dissolve
    show yuuhi 1 at top with dissolve
    window show
    play sound "fx/eureka.ogg"
    yuuhi "……就是现在！"
    play sound "fx/phantom_fire.ogg"
    show cg phantom_fire at center with FadeWhite(0.5)
    "趁朔的注意力都集中在我身上的时候，夕阳烧断了缠绕在自己身上的触手。"
    window hide
    hide cg with FadeWhite(0.5)
    hide yuuhi with FadeWhite(0.5)
    show yuuhi 11 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    window show
    yuuhi "可恶~我明明是正义的伙伴啊~！！！！\n好不容易来救你，结果却被人质反咬一口~！！！"
    extend "\n你们给我记住哦~！！！"
    play sound "fx/running.ogg"
    hide yuuhi with dissolve
    "获得自由的夕阳一边抹着眼泪一边溜走了。"
    window hide
    show nori 16 at top with dissolve
    window show
    nori "……。"
    me "……。"
    hide nori with dissolve
    "朔暂时消失在黑暗中，拿来了茶壶和茶杯，\n然后递给我卫生纸。"
    window hide
    play music "going_home.ogg"
    show nori 14 at top with dissolve
    window show
    nori "……没事吧？"
    me "啊……嗯。谢谢。"
    extend "\n对不起，好不容易抓到的夕阳君还是让他逃跑了……。"
    show nori 10 with dissolve
    nori "没事……反正他本来就是个碍事的人。"
    extend "\n而且，大哥哥身上隐藏着非比寻常的能量。"
    show nori 12 with dissolve
    extend "\n夕阳的插曲让我知道了有这回事，也不算亏。"
    extend "\n喝完红茶休息一下后，再重新开始实验吧。"
    me "……嗯！"
    window hide
    hide nori with dissolve
    window show
    "我享受完和朔的优雅的下午茶后，再次被要求坐在椅子上"
    hide bg with dissolve
    stop music fadeout 3.0
    extend "\n和刚才一样，我闭上眼，\n开始在脑海中描绘自己想实现的愿望。"
    window hide
    window show
    "···。"
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
    me "啊……已经早上了啊……？"
    extend "\n嗯~总觉得没睡够呢…。"
    stop sound fadeout 0.5
    "我一边嘀咕着一边起床，看向桌子，\n上面放了一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……啊，对对，是昨天回去的时候拿到的。"
    extend "\n那些小家伙们，真的好可爱啊……。"
    play sound "fx/triangle.ogg"
    me "……不过仔细想想，下周要出差啊。"
    extend "\n这下可去不了了……沮丧…。"
    "我不禁低下头，看到了垃圾桶。"
    play sound "fx/boing.ogg"
    me "咦？我流鼻血了吗？？"
    "垃圾桶里放着沾了血的纸巾。"
    "我做好了去公司的准备，像平常一样出门扔垃圾。"
    window hide
    hide bg with dissolve
    play sound "fx/door_open.ogg"
    show bg sky at center with Radial(0.7)
    window show
    me "好！今天也要加油！！"
    window hide
    stop music fadeout 1.0
    hide bg with FadeWhite(1.0)
    pause 0.6
    show bg dungeon at center with Radial(0.7)
    pause 0.6
    show bg saku_ed with Dissolve(0.8)
    pause 1.3
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.5
    hide bg with dissolve
    return

label day0_hidden_yuuhi:
    show bg dungeon at center
    stop music fadeout 0.5
    play music "infiltration.ogg"
    show cg c91 2 at center with Dissolve(0.8)
    window show
    me "夕，夕阳……！\n你能不能想想办法让我离开这里！！"
    extend "\n虽然被美少年囚禁，坦白说我求之不得，\n不过再这样下去生活也会受到妨碍！"
    play sound "fx/boing.ogg"
    yuuhi "啊，啊，是啊！！\n现在可不是争执的时候。"
    extend "\n喂，朔！快把人质放了！！"
    nori "你有什么资格说我？"
    extend "\n你才是，被选中的人。"
    extend "\n是要服从我，还是要反抗……"
    extend "\n要是回答有误，哥哥的脸就要被染得通红了哦。"
    play sound "fx/knife.ogg"
    "说完，朔把刀架在我的脖子上。"
    me "咿……。"
    window hide
    hide cg with dissolve
    show yuuhi 1 at topleft with dissolve
    window show
    yuuhi "喂，住手！！"
    show nori 12 at topright with dissolve
    nori "那你要怎么做呢？"
    extend "\n不过，都有人质要挟你了，结果已经注定了。"
    extend "\n来吧，用你的嘴巴，说一句让我满意的话，投降吧。"
    show yuuhi 2 with dissolve
    yuuhi "呜……。"
    window hide
    hide yuuhi with dissolve
    hide nori with dissolve
    window show
    me "嗯……。"
    "为了尽可能与刀保持距离，我不由自主地看向了朔。"
    window hide
    show nori 18 at top with dissolve
    play sound "fx/cute3.ogg"
    $ renpy.transition(Quake(30, 0, 0.1, 0.15), layer='master')
    window show
    "（微微颤抖）"
    hide nori with dissolve
    "……嗯？"
    "我的喘息声传到了朔的耳中，他似乎有了些许反应。"
    extend "\n但又不能把目光从夕阳身上移开，只能假装平静。"
    "难道说，这孩子……。"
    stop music fadeout 2.0
    play sound "fx/eureka.ogg"
    extend "\n豁出去了，赌一把……！！"
    "我使劲地把脸靠近朔的耳边"
    play sound "fx/sparkle.ogg"
    show cg adult at center with dissolve
    me "呼~~~~~~……。"
    window hide
    hide cg with dissolve
    show nori 20 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    window show
    nori "呜……啊！？"
    "朔的身体抖动了一下，手里的小刀掉了下来，"
    play sound "fx/wind_slash.ogg"
    extend "\n刚好插进正下方触手本体里，受了伤的触手这才放开了我。"
    extend "\n我立刻从背后抱住了朔的身体。"
    play sound "fx/fall_down.ogg"
    window hide
    hide nori with dissolve
    play music "hurry_up.ogg"
    window show
    play sound "fx/cute2.ogg"
    me "嘿嘿嘿~抓到你了♪"
    extend "\n朔君……这么小的年纪，就浑身透着暴露气息，这身体也太色情了吧？"
    show nori 19 at top with dissolve
    nori "呜……闭嘴！！\n可恶，竟敢……！！！"
    $ renpy.transition(Quake(0, 60, 0.15, 0.1), layer='master')
    play sound "fx/dash.ogg"
    show nori 20 with dissolve
    extend "\n放开我！！！快，快放开我！！！\n否则的话，我就要将你大卸八块了！！！"
    hide nori with dissolve
    "虽然嘴上说得那么吓人，可终究是个孩子……"
    extend "\n他不可能是成人的我的对手。"
    window hide
    window show
    me "夕阳君，就是现在！"
    extend "\n封住朔的行动！！"
    show yuuhi 13 at top with dissolve
    yuuhi "你，你还挺能干的嘛！！超帅哦！"
    show yuuhi 7 with dissolve
    extend "\n那个，能捆绑的东西……\n啊，用这个触手的残肢来吧……"
    hide yuuhi with dissolve
    "夕阳被突如其来的发展搞得目瞪口呆，\n听到我的声音才回过神来，捡起被小刀切下的触手，绑住了朔的两只手腕。"
    window hide
    play sound "fx/wind_slash.ogg"
    show cg c92 1 at center with FadeWhite(0.5)
    window show
    nori "快，快住手！你，你这！！"
    play sound "fx/boing.ogg"
    extend "\n喂，触手们！！！\n赶快阻止这些家伙！！！"
    yuuhi "哎呀！既然没有了人质，那我就按自己喜欢的来咯。"
    play sound "fx/eureka.ogg"
    extend "\n幻影火焰！！"
    window hide
    play sound "fx/battle3.ogg"
    show cg campfire_sparks with FadeWhite(0.4)
    pause 0.6
    play sound "fx/phantom_fire.ogg"
    show cg phantom_fire with Radial(0.4)
    window show
    "轰轰轰轰轰轰轰"
    "伴随着刺耳的轰鸣声，夕阳释放出了火焰，将触手烧得一干二净。"
    yuuhi "好耶！这样一来他就动不了了吧！"
    extend "\n嘿嘿，真是个惨不忍睹的反派啊~！"
    show cg c92 1 with Dissolve(0.7)
    "朔被夕阳固定住，摆出大喊万岁的姿势，不甘心地瞪着我。"
    "这种高贵又有尊严的美少年的这种表情，非常有魅力。"
    play sound "fx/triangle.ogg"
    extend "\n……话说，我好像意外地和朔君的兴趣很合得来啊。"
    "好了，那我就从夕阳君那，包含朔君在内的事开始来问问吧。"
    window hide
    hide cg with dissolve
    hide yuuhi with dissolve
    hide nori with dissolve
    window show
    me "夕阳君，我有很多事想问你……。"
    show yuuhi 12 at top with dissolve
    yuuhi "嗯？好。"
    stop music fadeout 3.0
    window hide
    hide yuuhi with dissolve
    hide bg with dissolve
    window show
    "···"
    window hide
    play music "fx/cave_ambience.ogg"
    show bg dungeon at center with dissolve
    window show
    me "那个，整理一下的话，"
    extend "\n就是，操纵火焰，守护世界和平的见习魔术师，夕阳君，\n和企图征服世界的『Wolf‘s』成员，朔君，是吧？？？"
    extend "\n这，这种漫画般的剧情……。"
    show yuuhi 13 at top with dissolve
    yuuhi "是真的啊！"
    extend "\n我刚才的战斗也让你看过了，要再给你看一次吗？"
    window hide
    play sound "fx/explosion1.ogg"
    show cg phantom_fire at center with Radial(0.5)
    window show
    "说着，夕阳在手掌上变出了一团小火焰。"
    yuuhi "这种事，一般人是办不到的吧？"
    "确实……一点符咒也没有，火焰就这么凭空出现。"
    window hide
    hide cg with dissolve
    hide yuuhi with dissolve
    window show
    me "啊啊……"
    extend "\n这世上还有太多太多我不知道的事了……。"
    show yuuhi 14 at top with dissolve
    yuuhi "就是啊！"
    extend "\n这世上没有不可能的事！"
    me "我好像在什么地方听过这句话……是你现学现卖？"
    show yuuhi 1 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    yuuhi "才不是！！这是我的原创！"
    show yuuhi 9 with dissolve
    extend "\n好！任务也顺利完成了，我们回去吧！！"
    me "啊，等一下！"
    extend "\n你打算就这么把被绑着的朔扔在这里不管吗？"
    window hide
    show cg c92 2 at center with Dissolve(0.8)
    window show
    "我们看向羞耻感压过了抵抗之心，此时垂头丧气地朔。"
    yuuhi "啊，让他保持现在这个状态也可以。"
    extend "\n反正他一定会想办法逃出来的。"
    extend "\n他执着起来可是很可怕的……。"
    window hide
    hide cg with dissolve
    hide yuuhi with dissolve
    window show
    me "是，是么……"
    extend "\n那，那我还有一件事想确认！\n可以去吗？"
    show yuuhi 14 at top with dissolve
    yuuhi "嗯？这个嘛，也可以吧。"
    play sound "fx/running.ogg"
    hide yuuhi with dissolve
    "听到这句话，我靠近朔。"
    window hide
    show cg c92 2 at center with Dissolve(0.8)
    window show
    nori "……还有什么事？"
    me "没什么，只是很少见到毫无防备的美少年，"
    stop music fadeout 0.5
    play sound "fx/tadaa.ogg"
    show cg remarkable with FadeWhite(0.5)
    extend "\n所以想拜见一下你的内裤！"
    play sound "fx/dash.ogg"
    "夕阳＆朔" "什……！！"
    window hide
    play music "hurry_up.ogg"
    show cg c92 1 with FadeWhite(0.5)
    window show
    me "不是挺好的嘛~♪"
    extend "\n我可是被你监禁的人哦？"
    extend "\n向我道歉，不是合情合理的事情吗？？"
    play sound "fx/boing.ogg"
    nori "你在说什么傻话……！"
    play sound "fx/triangle.ogg"
    yuuhi "什么合情合理啊……。"
    me "啊，不是不是。"
    extend "\n如果把这幅狼狈的样子拍下来，\n我想这孩子就不会再伤害我了♪”"
    yuuhi "原，原来如此……？"
    nori "谁，谁会盯上你这种人啊……！！"
    extend "\n我已经不想再看到你的脸了！"
    me "诶~别说这种话~？"
    extend "\n只要不危害到我，我当然很欢迎你啦~。"
    extend "\n呐呐，来见我嘛~。"
    play sound "fx/dash.ogg"
    nori "吵死了！！你给我乖乖消失！"
    "我无视了朔的话，伸手去摸他的裤子。"
    play sound "fx/sparkle.ogg"
    show cg adult at center with FadeWhite(0.5)
    me "那么~我很期待你会穿什么样的内裤呢~！"
    extend "\n如果是你的话，穿什么内裤都能萌到我哦~。"
    extend "\n是意外稚嫩的三角裤？还是调皮的平角内裤？\n还是年轻人喜欢的拳击短裤？还是，还是"
    play sound "fx/wow2.ogg"
    extend "变态比基尼？？"
    window hide
    hide cg with dissolve
    hide yuuhi with dissolve
    show yuuhi 11 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    window show
    yuuhi "别，别说变态啦！！"
    me "诶？"
    show yuuhi 10 with dissolve
    stop music fadeout 0.5
    yuuhi "啊，不是，没什么……。"
    window hide
    show cg c92 2 at center with dissolve
    window show
    nori "如果能做到的话，就试试吧……。"
    me "咦，咦……？为什么突然这么强硬？？"
    extend "\n你再表现得更讨厌一点啊。"
    "这时，朔一脸快要哭出来的表情，颤抖着用几乎听不见的声音说道。"
    play sound "fx/impact.ogg"
    show cg c92 3 with FadeWhite(0.5)
    nori "我，我……不穿内裤……"
    extend "\n所以……更进一步的事情……"
    show cg remarkable with Dissolve(0.2)
    play sound "fx/explosion2.ogg"
    extend "\n如果想让这个游戏变成十八禁的话，就做试试看！！！！！"
    hide cg with Dissolve(0.8)
    hide bg with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    hide yuuhi with Dissolve(0.8)
    hide nori with Dissolve(0.8)
    window hide
    window show
    "···。"
    window hide
    show bg residential_area_night at center with Dissolve(0.8)
    play music "going_home.ogg"
    window show
    "就这样，我们逃离了朔，顺利地来到了外面。"
    me "夕阳君，今天真是谢谢你了。"
    show yuuhi 6 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    yuuhi "哦！"
    extend "\n不过，能够顺利逃出来，也有你的功劳。"
    show yuuhi 4 with dissolve
    extend "\n真亏你能发现那家伙耳朵很敏感呢~。"
    extend "\n下次再打的话，我也会这么做。"
    me "明明在床上打就好了。"
    show yuuhi 3 with dissolve
    play sound "fx/boing.ogg"
    yuuhi "啥？？"
    me "啊，没什么……"
    extend "\n今后世界的和平也拜托你了！夕阳君。"
    extend "\n偶尔也来见见我吧。\n像你这样的少年，随时都欢迎！！"
    show yuuhi 8 with dissolve
    yuuhi "唔~嗯……被你这么一说，我更难开口了……"
    show yuuhi 14 with dissolve
    extend "\n如果又发生了什么，随时都可以来找我！我会赶来帮助你的。"
    play sound "fx/eureka.ogg"
    extend "\n就交给我这位炎之魔法师 夕阳吧！！"
    me "就算我陷入欲求不满足的状态也行吗？"
    show yuuhi 8 with dissolve
    yuuhi "这，这种事要靠自己解决啊……！"
    me "自称正义的伙伴真是可爱啊。"
    show yuuhi 1 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    yuuhi "你说什么~！！"
    me "啊哈哈哈。"
    window hide
    show cg night_town at center with Dissolve(0.7)
    window show
    "谈笑了一会儿，夕阳又离开去了别的地方。"
    extend "\n为了守护世界的和平，巡逻是必不可少的。"
    "就这样，我那宛如梦境般的奇妙体验拉下了帷幕。"
    window hide
    stop music fadeout 1.0
    hide bg with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    hide yuuhi with Dissolve(0.8)
    window show
    "···。"
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
    me "嗯啊~真是美好的清晨啊！！"
    extend "\n新一天的开始，希望的早晨……让人想要欢呼雀跃啊~！"
    extend "\n说起来，昨天的事，真的是现实吗……。\n是不是我又做了超现实的梦啊…。"
    stop sound fadeout 0.5
    "我一边嘟囔着一边起身，看向了桌面上，\n那里放着一张传单。"
    play sound "fx/paper.ogg"
    me "嗯？这是……"
    extend "啊，对了对了，是我昨天回去的时候拿到的。"
    extend "\n那些小家伙们，真的好可爱啊……。"
    play sound "fx/triangle.ogg"
    me "……不过仔细想想，下周要出差啊。"
    extend "\n这下可去不了了……沮丧…。"
    me "现在先老老实实地面对现实吧。"
    extend "\n就算是做梦，只要想着少年们给了我力量就行了！"
    "我洗了个澡，做好上班的准备，就如往常一样离开了家。"
    window hide
    hide bg with dissolve
    play sound "fx/door_open.ogg"
    show bg sky at center with Radial(0.7)
    window show
    me "好！今天也要加油！！"
    window hide
    stop music fadeout 1.0
    hide bg with FadeWhite(1.0)
    pause 0.6
    show bg phantom_fire at center with Radial(0.7)
    pause 0.6
    show bg yuuhi_ed with Dissolve(0.8)
    pause 1.3
    hide bg with dissolve
    pause 0.5
    show bg credits at center with dissolve
    pause 0.5
    hide bg with dissolve
    return