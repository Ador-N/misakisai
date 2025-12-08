# -*- coding: utf-8 -*-
# Converted from 00000182.lns

label day1:
    window show
    "···"
    window hide
    pause 0.5
    window show
    "嗯……。"
    extend "\n怎么回事……我没有洗澡就睡着了吗……？"
    "而且，感觉头好晕……。"
    extend "\n我，趴在什么上面？"
    "……桌子？"
    "可是，我记得，自己应该是睡在床上……。"
    unknown "咦？[player_name]君睡着了？"
    extend "\n喂、喂[player_name]君！快起来~。"
    "少年那舒心的声音传入耳中。"
    unknown "啊哈哈，完全睡着了呢~。"
    unknown "难道说，身体不舒服吗？"
    play music "fx/heartbeat.ogg"
    "有人靠近了我。"
    unknown "[player_name]"
    "那孩子的手触碰着我的肩膀。"
    extend "\n我为了看清楚对方的脸，强行抬起昏沉的头，站起身子。"
    "咔嚓\n"
    stop music fadeout 1.0
    play sound "fx/wind_slash.ogg"
    show bg classroom at center with Radial(0.5)
    "铛！！！"
    play sound "fx/dash.ogg"
    $ renpy.transition(Quake(0, 200, 0.1, 0.065), layer='master')
    play music "emergency.ogg"
    boy1 "好疼啊啊啊！！"
    extend "\n别、别突然站起来啊[player_name]君……！！"
    "伴随着一道闷响，翻江倒海般的头痛传来。"
    extend "\n但是，我还是被似曾相识的少年的声音吸引了注意力。"
    "我确认了声音的主人，那正是……。"
    window hide
    play sound "fx/entrance.ogg"
    show tomo c5 1 at center with DefocusWhite(0.5)
    window show
    "昨晚在车站前给我传单的那位少年。"
    "看起来他的下巴受到重创，正在痛苦地呻吟。"
    "我的头痛很快消散，头脑清醒了些，但仍感到混乱。"
    "这里是……教室？从外面的光线来看，是白天吗？为什么我会在这里？"
    extend "\n完全搞不清状况，让我感到了另一种意义上的头痛。"
    "忽然，想起自己刚刚用头撞了人。"
    me "抱、抱歉！你、你没事吧？"
    "嗯……？"
    extend "\n我的声音……似乎比平时……细了一些？"
    "而且，总觉得这个教室，我好像在哪里见过……。"
    "既不是大学的讲堂，也不是高中的教室……"
    extend "\n是御咲学园中等部的教室！！"
    hide tomo with Dissolve(0.3)
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 50, 0.15, 0.1), layer='master')
    me "诶、诶诶诶诶诶诶诶诶！！？？！？"
    extend "\n这是怎么回事啊！？"
    extend "\n这、这是做梦？这是在做梦吗？？？"
    "我不禁大声喊了出来。"
    show tomo c5 2 at center with dissolve
    boy1 "[player_name]君，你是睡糊涂了吗~？"
    extend "\n真是的~我明明作为代表那么努力地在组织大家！"
    boy1 "我现在稍微能理解，训斥上课睡觉的同学时，\n老师的心情了。\n好痛啊……。"
    "少年一边揉着下巴一边说道。"
    window hide
    hide tomo with dissolve
    show sakuya 4 at topleft with dissolve
    window show
    boy7 "你在说什么啊！"
    extend "\n完全没进展的原因不就是因为你一直絮絮叨叨的嘛。"
    extend "\n那样肯定会想睡觉的啊。"
    show saburo 4 at topright with dissolve
    boy8 "好了好了。"
    extend "\n不过话说回来，咖啡店啊~。"
    extend "\n去当客人倒还好，\n但要从经营的角度考虑的话，应该相当辛苦吧。"
    hide sakuya with dissolve
    show sintarou 4 at topleft with dissolve
    boy4 "没事没事！"
    extend "\n三酱的服装咱会特别量身定制，\n如果遇到什么困难，咱也会全力支援你的♪"
    show saburo 3 with dissolve
    play sound "fx/dash.ogg"
    boy8 "为什么啊！"
    extend "\n话说为什么已经决定让我当服务员了啊！！"
    extend "\n我绝对不要做那种工作！"
    "身后传来喧闹声。"
    hide saburo with dissolve
    hide sintarou with dissolve
    show sora 5 at topright with dissolve
    boy3 "[player_name]君没事吧？"
    extend "\n真的是身体不舒服吗？"
    show tuki 4 at topleft with dissolve
    boy5 "如果是那样的话，尽管开口说。"
    extend "\n我会把你背到保健室去。"
    "坐在旁边的两人温柔地说道。"
    hide sora with dissolve
    hide tuki with dissolve
    show tubasa 7 at top with dissolve
    boy2 "那、那个……那个……。"
    "独自站在讲台上的少年不知所措。"
    extend "\n他旁边的空位，应该就是来叫醒我的少年的吧。"
    hide tubasa with dissolve
    "仔细看下来，这间教室里\n似乎都是昨晚遇到的御咲学园的学生。"
    extend "\n再看前排的位置，正是那个身材娇小的男孩子。"
    window hide
    show sinobu 3 at topright with dissolve
    window show
    boy6 "友。\n总之先休息一下，\n十分钟后继续开会怎么样？"
    show tomo 9 at topleft with dissolve
    tomo "唔……嗯……。"
    "对哦。这个少年叫『友』来着。"
    me "抱、抱歉啊，友。\n之后我会认真听你讲话的。"
    show tomo 10 with dissolve
    tomo "完全没关系，不用在意。"
    extend "\n比起这个，如果真的身体不舒服，\n不用顾虑，随时可以提出来哦！"
    hide tomo with dissolve
    hide sinobu with dissolve
    show tomo 1 at top with dissolve
    tomo "那么，现在休息十分钟。"
    window hide
    hide tomo with dissolve
    hide bg with dissolve
    return

label day1_1:
    play sound "fx/sliding_door.ogg"
    show bg hallway at center with dissolve
    window show
    "装作平静的样子走出教室，\n外面果然是我初中时所在的御咲学园的走廊。"
    extend "\n也就是说，厕所在这边……！"
    window hide
    stop music fadeout 0.5
    play sound "fx/running.ogg"
    hide bg with dissolve
    show bg washroom at center with dissolve
    window show
    play music "discovery.ogg"
    "教室里的孩子，对我都像对待同级生一样。"
    extend "\n这样的话，也就是说……。"
    "去洗手间照镜子，镜中反射出的是……"
    "……。"
    window hide
    play sound "fx/boing.ogg"
    show 俺 c6 at center with zoominout
    window show
    "一个既不可爱也不帅气，但也不难看的"
    extend "\n土里土气的家伙正看着我。"
    "我果然变回了初中生。"
    extend "\n虽然稍微好看了些，但当时确实是长这样……。"
    "但是，到底为什么呢……？"
    extend "\n昨晚我……"
    "啊，对了……我想要变回初中生。"
    extend "\n然后，就拿到了能实现愿望的糖果……。"
    "可，就这样实现了吗……骗人的吧？"
    window hide
    hide 俺 with dissolve
    window show
    "想着怎么可能会有这种事，我试着拉了下脸颊。\n"
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(200, 0, 0.5, 0.5), layer='master')
    pause 0.5
    $ renpy.transition(Quake(-100, 0, 0.25, 0.5), layer='master')
    extend "拍了几巴掌。"
    play sound "fx/dash.ogg"
    $ renpy.transition(Quake(200, 0, 0.1, 0.065), layer='master')
    extend "\n又敲了敲脑袋。"
    play sound "fx/punch2.ogg"
    $ renpy.transition(Quake(0, 200, 0.1, 0.065), layer='master')
    "……好疼。这不是梦……吗？"
    "不，但是这种事在现实里绝不可能发生吧。"
    extend "\n虽然我的想象力很丰富，每天都会做五彩斑斓的梦，"
    extend "\n但我的梦还没有真实到能感受到疼痛和重量的程度啊！"
    "嗯？对了……既然变回了初中生，"
    play sound "fx/eureka.ogg"
    extend "难道连那里也……！"
    window hide
    play sound "fx/door_open.ogg"
    show bg private_toilet with FadeWhite(0.5)
    window show
    "如今我的那个东西完全变成了在林中奔跑的长毛象。"
    extend "\n但是，在那时还只是个可爱的小象。"
    "虽然我对自己没有性欲，\n但是少年的好奇心蠢蠢欲动，所以这并不是什么大问题！"
    "我脱下了裤子。"
    play sound "fx/sparkle.ogg"
    extend "\n……对啊，那时候还穿着三角裤啊……。"
    extend "\n不对，现在不是感伤的时候！问题是下面！！"
    "我刚把手放在内裤上，"
    stop music fadeout 0.5
    play sound "fx/triangle.ogg"
    unknown "呜哦……好洁白的内裤！"
    unknown "和翼一样呢！"
    "！！？"
    "伴随声音，我感觉到了上方的视线。"
    play music "lively_boys.ogg"
    show bg remarkable with Dissolve(0.2)
    me "你、你们在干什么啊！！"
    "我抬起头，看到从旁边隔间探出头的猫嘴少年和友。"
    "竟然偷窥别人的隔间，这些人也太大胆了！"
    extend "\n……虽然这么想，但我在初中的时候也做过这种事。"
    extend "\n难免有怀念的感觉……"
    play sound "fx/door_open.ogg"
    show bg washroom with FadeWhite(0.5)
    "我整理好裤子走到了外面，那两人开始聊天。"
    window hide
    show sintarou 9 at topright with dissolve
    window show
    boy4 "哎呀~我听到厕所隔间传来很涩的娇喘声，本来以为听错了，\n就探头一看！"
    show tomo 10 at topleft with dissolve
    tomo "原来如此~是这么回事啊。"
    extend "\n[player_name]君，你是开会时实在忍不住想涩涩\n所以就跑来这里了啊！"
    extend "\n没错没错……嗯，男人的话肯定会有这种时候！"
    "两人靠了过来。"
    show sintarou 1 with dissolve
    boy4 "虽然外表很纯良，但意外的好色啊[player_name]酱。"
    play sound "fx/wow2.ogg"
    show bg adult
    show sintarou 5 with dissolve
    extend "\n我看看啊，这里就让我们为你两肋插刀\n来帮帮你吧…。"
    show tomo 11 with dissolve
    tomo "别不好意思啦，放松交给我们就好~。"
    extend "\n没事没事，我们都是男人嘛。"
    me "什、什什什么！"
    "这、这和我的初中时完全不一样啊！"
    extend "\n现在的孩子已经这么前卫了吗……！"
    extend "\n这成何体统……！！！"
    "拜托了！梦啊，千万不要醒来啊！！"
    play sound "fx/explosion3.ogg"
    extend "\n就算弄脏了被子也没关系的，所以千万不要醒来啊啊啊！！！"
    show bg washroom with dissolve
    "（砰！）\n"
    play sound "fx/punch.ogg"
    $ renpy.transition(Quake(0, 100, 0.1, 0.065), layer='master')
    tomo "啊！？"
    hide tomo with dissolve
    "（砰！）\n"
    play sound "fx/punch2.ogg"
    $ renpy.transition(Quake(0, 100, 0.1, 0.065), layer='master')
    boy4 "呜！！"
    hide sintarou with dissolve
    boy6 "在公共场所，不要做这种蠢事。"
    "倒在地上的两个人的对面，\n"
    play sound "fx/impact_japanese.ogg"
    window hide
    show sinobu c7 1 at center with Radial(0.5)
    window show
    extend "那个身材纤细的少年出现了。"
    extend "\n他的双拳紧握，蓄势待发"
    show sinobu c7 2 with dissolve
    boy6 "没事吧？[player_surname]君。"
    extend "\n以后要注意别被这两个人带坏了哦。"
    me "……嗯。"
    "梦境是自由的天地。"
    extend "\n能意识到自己在做梦的清醒梦，就是这种自由的极致。"
    extend "\n无论是凌空飞行、施展魔法，还是拯救世界，甚至犯下罪行，在梦中，一切都随心所欲。"
    "自己就是这梦境的支配者，谁也不能妨碍我，亦或是惩罚我。"
    extend "\n如果这一切就是那种梦境的话，我就要推倒眼前这个娇小可爱的少年，\n扒掉裤子让他露出内裤，然后尽情调教！！"
    "但是，这次有点……不，是相当不一样。"
    extend "\n如果我在此出手，感觉那个少年会立刻一拳击中我的要害，然后我就真的永远\n陷入长眠了。"
    extend "\n从他释放的杀气中感觉得到。"
    window hide
    stop music fadeout 1.0
    hide sinobu with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    return

label day1_2:
    show bg classroom at center with dissolve
    play music "cute_silly.ogg"
    window show
    "和三人一起回到教室后，站在讲台上的孩子走了过来。"
    show tubasa 8 at topright with dissolve
    boy2 "友、友同学。\n你的头上有个很大的肿包……。"
    show tomo 9 at topleft with dissolve
    tomo "没、没事的，不用在意……。"
    "友开朗地回应了他，然后说继续刚才关于御咲祭的讨论。"
    hide tubasa with dissolve
    hide tomo with dissolve
    "唔，话说回来，能梦见如此真实的梦，\n是不是和昨晚的戴帽子的短裤少年有关系呢。"
    stop music fadeout 2.0
    extend "\n如果是这样，那孩子还真是送了我不得了的东西呢。"
    extend "\n如果不会影响到现实中的我就好。"
    play music "school_festival.ogg"
    "……好，这样就干脆在这个奇妙的梦境世界里\n尽情享受吧！"
    "现在的我[player_surname][player_name]是初中二年生！"
    extend "\n身体是孩子，头脑是大人！"
    extend "\n就像某位名侦探一样，带着外挂，轻松攻略吧！"
    "···"
    window hide
    show bg school_building_morning with dissolve
    window show
    "我稍微观察了一阵后，总算是搞明白了状况。"
    extend "\n我们好像是二年级一班和二班的御咲祭执行委员。"
    "因此，放学后我们得聚在一块，在各班代表的主持下，\n一起讨论并决定大致流程，再进行各种准备。"
    extend "\n然后，就是执行委员和各班学生一起进行筹备，差不多是这种感觉。"
    "接着，关于委员会的成员……"
    "一班的代表是，\n"
    window hide
    show bg yellow
    show tomo at top with dissolve
    window show
    extend "被我撞到过头，又因为偷窥厕所隔间被敲了铁锤的森海友。"
    "他那圆圆的卷发也是他的萌点。"
    extend "\n看上去开朗风趣，\n从刚才的事情来看，应该是个喜欢开黄腔的人。"
    hide tomo with dissolve
    show bg classroom with dissolve
    show tomo 12 at topleft with dissolve
    show tomo 2 with dissolve
    "他作为代表，虽然兴致勃勃地站在讲台上，\n但是总感觉他不太擅长组织，并不适合当领导者。"
    hide tomo with dissolve
    "然后，在他身旁\n"
    window hide
    show bg blue
    show tubasa at top with dissolve
    window show
    extend "站着的是二班的代表一之濑翼。"
    "黑色的头发和粗粗的眉毛，给人一种单纯的感觉。"
    extend "\n与友完全相反，他是个内向且胆小的人，一举一动就像个小动物一样。"
    "因为这样的性格，所以我觉得他也不太适合当负责人。"
    "虽然不了解他是个什么样的人，\n但是……\n"
    hide tubasa with dissolve
    show bg classroom with dissolve
    show tubasa 5 at topright with dissolve
    show tubasa 11 with dissolve
    "他对友投去的炙热目光中，似乎藏着某种复杂的情愫啊。"
    hide tubasa with dissolve
    "然后是，一班的执行委员，"
    "坐在我面前的，\n"
    window hide
    show bg green
    show sinobu at top with dissolve
    window show
    extend "是刚才打过照面的绫濑忍君。"
    "中性化的脸庞，加上娇小而纤细的身材，怎么看都像女孩子。"
    "冷静又成熟，话也很少，所以并不清楚他在想什么，不过……\n肯定讨厌开黄腔。"
    extend "至少这一点我是知道的。必须注意才行。"
    hide sinobu with dissolve
    show bg classroom with dissolve
    show sinobu 4 at topleft with dissolve
    "作为友的青梅竹马，是阻止他胡闹乱来的角色吗。"
    extend "\n话说回来，在厕所里那铁拳制裁的威力……到底是从哪来的啊？"
    hide sinobu with dissolve
    "然后是首先担心我的心地善良的双胞胎，坐在旁边的赤峰月君"
    window hide
    show bg red
    show tuki at topleft with dissolve
    window show
    extend "和空君。"
    window hide
    show sora at topright with dissolve
    window show
    extend "\n双胞胎在同一班上可真是少见。"
    "身材高大，体格健壮，气质凛然的就是哥哥月。"
    extend "\n和朋友们比起来他显得很沉稳，而且我也感觉得出来他有很强的体力。"
    "而相对的，弟弟空则身材苗条，有着一双圆溜溜的大眼睛。"
    extend "\n他所散发出的气质温暖柔和，看起来很会照顾人。"
    "……以上就是我对他们的第一印象，"
    hide tuki with dissolve
    hide sora with dissolve
    show bg classroom with dissolve
    show tuki 5 at topleft with dissolve
    tuki "森海！\n我提的『兜裆布咖啡厅』为什么被无视了啊……？"
    show sora 6 at topright with dissolve
    sora "哥哥你闭嘴。"
    "看来还有这样意外的一面啊。"
    extend "与忍和友的关系很像。"
    hide sora with dissolve
    hide tuki with dissolve
    "然后是二班的执行委员，"
    "坐在里面的位置上一脸不耐烦的，\n"
    window hide
    show bg purple
    show sakuya at top with dissolve
    window show
    extend "是穗海作哉。"
    "柔顺的直发配着张桀骜不驯的脸，典型的人气王配置啊。"
    extend "\n在讨论中，他明显地很不耐烦，还对友冷嘲热讽，\n给人的印象是浑身带刺。"
    hide sakuya with dissolve
    show bg classroom with dissolve
    show sakuya 6 at topleft with dissolve
    "尤其是看到友和翼在一起的时候，那种尖锐感就更加强烈了。"
    "这、这难道就是，昨晚在汉堡店听说的那个……"
    extend "\n现实中的BL吗……！"
    extend "\n居然能亲眼看见……真是期待今后的发展啊！！"
    "另一个人，\n"
    hide sakuya with dissolve
    window hide
    show bg light-blue
    show saburo at top with dissolve
    window show
    extend "是坐他旁边的猫山三朗。"
    "特征是虎牙，说着一口流利的关西腔。"
    extend "\n他给人的印象是既调皮又大度。"
    extend "\n他和作哉关系很好，感觉既能和作哉一起插科打诨，也能安抚他。"
    hide saburo with dissolve
    show bg classroom with dissolve
    show sintarou 1 at topleft with dissolve
    show saburo 3 at topright with dissolve
    "但是，对旁边的奥村慎太郎却毫无招架之力，每次他说点什么，都吓得惊慌失措，差点叫出声来。"
    extend "\n这、这也是BL吗……？！"
    "对了，一班的委员还有一人。"
    hide saburo with dissolve
    hide sintarou with dissolve
    extend "\n就是和友一起偷窥隔间的，\n"
    window hide
    show bg orange
    show sintarou at top with dissolve
    window show
    extend "奥村慎太郎，通称『慎酱』。"
    "他的特征是猫唇，以及由此说话时带有的独特腔调。"
    extend "\n性格是……对性的好奇心旺盛得相当变态的人。"
    hide sintarou with dissolve
    show bg classroom with dissolve
    show sintarou 9 at topleft with dissolve
    extend "\n一听到色情的话题立马就扑过来，并且，自己也会挑起那类话题。"
    "就像高中时的我一样……说不定，还要超过当时的我。"
    extend "\n真是令人生畏的孩子啊。"
    hide sintarou with dissolve
    "以上的八人，包括我共九人，就是一班和二班的御咲祭执行委员。"
    window hide
    show tomo 13 at topleft with dissolve
    window show
    tomo "好！"
    extend "\n那么，主题就是融合咖啡店！！\n日式西式中式，和洋折衷，融合各种风格，不受拘束，\n随心所欲！！那么开始进行吧！"
    show sintarou 7 at topright with dissolve
    sintarou "好耶！！"
    "结果，内容还是什么都没决定啊……。"
    extend "\n初中生对学园祭的讨论就这种程度啊。"
    extend "\n这样安排得粗略一点可能反而会比较好吧。"
    me "嗯，这样挺好的。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    show bg blackboard with dissolve
    show tubasa 2 at top with dissolve
    window show
    tubasa "那、那么，现在开始分组。"
    extend "\n①『服装组』，②『布置组』，③『料理组』，④『采购组』\n一共分为四个组。"
    show tubasa 12 with dissolve
    tubasa "①『服装组』，负责确定咖啡店店员要穿着的服装，\n在预算范围内，进行服装的采购，或者制作。"
    show tubasa 3 with dissolve
    extend "\n②『布置组』，决定要借哪间教室来作为咖啡店，\n考虑店内的构造，物品的配置、设计等。"
    show tubasa 10 with dissolve
    tubasa "③『料理组』，负责考虑咖啡店要提供的料理，\n实际制作出来，确定最终的菜单。"
    show tubasa 13 with dissolve
    extend "\n④『采购组』，为『布置组』和『料理组』，\n采购需要的材料。"
    window hide
    hide tubasa with dissolve
    show bg classroom with dissolve
    show sakuya 3 at topleft with dissolve
    window show
    sakuya "总之，我不想和那个呆毛一组！"
    show tomo 5 at topright with dissolve
    $ renpy.transition(Quake(0, 65, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tomo "你说啥！！\n那是我该说的话吧，你这技安！"
    hide sakuya with dissolve
    hide tomo with dissolve
    show sinobu 6 at topleft with dissolve
    sinobu "……除了『料理组』以外。"
    show sora 1 at topright with dissolve
    sora "忍、忍同学，姑且还算有自觉呢…。"
    hide sinobu with dissolve
    show tuki 6 at topleft with dissolve
    tuki "和空一组就好。"
    show sora 4 with dissolve
    sora "……。"
    show tuki 1 with dissolve
    tuki "……。"
    show sora 7 with dissolve
    sora "……。"
    show tuki 7
    play sound "fx/dash.ogg"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    tuki "想和空一组……！！"
    show sora 8 with dissolve
    sora "我、我知道啦！知道啦！……真是的。"
    hide sora with dissolve
    hide tuki with dissolve
    show sintarou 8 at topleft with dissolve
    sintarou "嗯~咱还是去设计服装好了。"
    show saburo 6 at topright with dissolve
    saburo "我就去买东西的组好了。"
    extend "\n感觉不怎么用动脑子！"
    hide sintarou with dissolve
    hide saburo with dissolve
    show tubasa 1 at topleft with dissolve
    tubasa "那、那我怎么办……。"
    show tubasa 14 with dissolve
    "翼扭扭捏捏地向一旁的友投去求助的目光。"
    show tomo 4 at topright with dissolve
    tomo "那，我也想和慎酱去服装组！"
    show tubasa 7 with dissolve
    play sound "fx/shock.ogg"
    tubasa "（受打击！！！）"
    "翼，你也太好懂了吧……！"
    extend "\n友也太罪孽深重了啊。"
    hide tubasa with dissolve
    hide tomo with dissolve
    me "每组都正好有两个人，我就作为临时帮手，随时给各组帮忙吧。"
    window hide
    show tomo 1 at top with dissolve
    window show
    tomo "OK！事情终于可以有进展了~。"
    show tomo 3 with dissolve
    tomo "那么，就开始分组讨论吧！"
    extend "\n现在是两点半，那就定在接下来的两个小时——也就是到四点半吧！\n就算在那之前讨论完了，也不许擅自回家哦。"
    extend "\n之后我们会把每组讨论的情况告诉老师。"
    show tomo 12 with dissolve
    tomo "那么[player_name]君，你今天帮哪个组？"
    hide tomo with dissolve
    window hide
    show 班選択 choose_group_message at center with dissolve
    return

label day1_design:
    hide 班選択 with dissolve
    window show
    me "我去『服装组』！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg dark at center with dissolve
    play music "infiltration.ogg"
    show tomo 3 at top with dissolve
    window show
    tomo "诶，御咲祭只剩不到一周了，\n没有时间可以浪费了。"
    show tomo 15 with dissolve
    tomo "那么，聚集在这里的我们是『服装组』……"
    extend "\n为两个班的学生准备服装，得花费相当多的金钱和时间吧。"
    show tomo 16 with dissolve
    tomo "因此，接下来需要慎重且迅速地推进话题。"
    extend "\n那么……"
    stop music fadeout 0.5
    hide tomo with dissolve
    show bg classroom with Radial(0.5)
    play music "hurry_up.ogg"
    show tomo 13 at topleft with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    extend "二位，究竟要选择怎样的服饰比较好呢~！？！？"
    show sintarou 7 at topright with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sintarou "我我我！"
    extend "\n我认为服装是决定店铺印象的关键所在，\n所以这里必须要搞得超级华丽才行！！"
    show tomo 17 with dissolve
    tomo "就是~啊~！！"
    extend "\n必须要跟其他班级有明显的区别才行！"
    show tomo 11 with dissolve
    tomo "既然要华丽，那不如就选之前小慎给我们的，\n那个色情的服饰让全员都穿上怎么样？"
    show sintarou 5 with dissolve
    sintarou "猫耳+比基尼+蝴蝶领结的那个？"
    extend "\n不错啊不错啊~！"
    show sintarou 11 with dissolve
    extend "\n不过，要想把那些都凑齐，可是要花不少钱的喔~。"
    show sintarou 10 with dissolve
    sintarou "话说回来，如果真的选了那样的服饰的话，\n我认识的那些家伙绝对会来咖啡店而且赖着不走的。"
    extend "\n不过不管选怎样的服饰，他们也许都会赖着不走！"
    show tomo 18 with dissolve
    tomo "慎酱认识的那些家伙，是澡堂传言中的常客？"
    extend "\n哇~他们真的会来啊！"
    show tomo 25 with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    extend "\n讨厌~怎么办，我要被性骚扰了吗？好可怕~~~~！"
    show sintarou 9 with dissolve
    sintarou "虽然你这么说，但其实你很感兴趣吧！！"
    show tomo 19 with dissolve
    tomo "才没有，完全没有！！"
    extend "\n我已经从那种事毕业了啊！"
    show sintarou 12 with dissolve
    sintarou "你嘴上这么说~♪"
    show sintarou 13 with dissolve
    extend "\n不过嘛，我会提醒他们自重一点，\n应该不会出什么事的吧。"
    show tomo 8 with dissolve
    tomo "哼，哼~嗯……。"
    show sintarou 5 with dissolve
    play sound "fx/eureka.ogg"
    sintarou "啊~你刚才很失望吧！！"
    extend "\n果然友才是淫乱少年呢~！"
    show tomo 20 with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tomo "才不是，我可没有！！"
    extend "\n请不要把我和慎酱混为一谈~！"
    me "……。"
    hide tomo with dissolve
    hide sintarou with dissolve
    play sound "fx/ding.ogg"
    "这、这是什么啊……完全无法融入对话。"
    "我心目中的初中男生\n应该是更加纯洁的，清纯的，硬派的，无瑕的少年！！"
    extend "\n初中时，都是些不知道大人世界的小男孩，\n但从刚才厕所里的事来看，现在的中学生似乎已经变得如此开放了吗！？"
    stop sound fadeout 0.5
    "但是，这样也挺好的……"
    extend "可能。"
    window hide
    show sintarou 4 at topright with dissolve
    window show
    sintarou "说起来，电摩君还好吗？"
    show tomo 2 at topleft with dissolve
    tomo "很好很好！好着呢！！"
    extend "\n今天早上也是一直都在哔哔叫！"
    extend "\n说起来，慎酱的飞机杯酱还好吗？"
    show sintarou 1 with dissolve
    sintarou "超级好！"
    extend "\n昨晚也给他灌了一堆精液。"
    hide sintarou with dissolve
    hide tomo with dissolve
    play sound "fx/boing.ogg"
    "电、电摩棒……？！"
    extend "飞、飞机杯！？！？"
    extend "\n冷、冷静点。默数质数。"
    "没错，这一定是听错了！"
    extend "\n或许是最近年轻人喜欢的简称，刚好和那些重合了而已。"
    window hide
    show tomo 7 at topleft with dissolve
    window show
    tomo "但是最近震动越来越弱了呢。"
    extend "\n是不是快寿终正寝了啊~？该考虑买新的了啊。"
    show sintarou 11 at topright with dissolve
    sintarou "我也快用完润滑液了。"
    extend "\n下次再买点吧。"
    hide tomo with dissolve
    hide sintarou with dissolve
    play sound "fx/shock_big.ogg"
    "是成人玩具啊啊啊！！\n这完全是指成人玩具吧！！"
    extend "\n我上高中那会儿，都还只是靠少年周刊里的擦边球来解决……\n自己真是没出息啊！！！！"
    "嗯？不对，等等……这不正是机会吗？"
    extend "\n可以让我走上另一条我没能选择的道路了！！"
    play sound "fx/sparkle.ogg"
    show cg adult at center with Radial(0.5)
    "好，初中生[player_surname][player_name]！"
    extend "\n和这些孩子们一起飞向粉色世界吧！！"
    window hide
    hide cg with dissolve
    window show
    me "……你们两个，现在要是把身体交给机器和道具的话，\n之后就无法被真人满足了哦？"
    show tomo 21 at topleft with dissolve
    tomo "诶……？"
    show sintarou 14 at topright with dissolve
    sintarou "[player_name]桑……？"
    me "即使不依赖什么道具，能让我们变得更加\n舒服的东西就在身边不是吗！"
    me "没错，就是我们自己！"
    extend "\n虽然这么说，也不是要自己来慰抚自己！"
    extend "\n而是让别人来代劳的意思。"
    me "也就是说，用自己的身体去慰藉他人，用他人的身体去慰藉自己。"
    extend "\n这才是最棒的快感哦。"
    show tomo 3
    show sintarou 15 with dissolve
    tomo_and_shin "哦哦…"
    me "怎么样？有兴趣吗？"
    extend "\n有兴趣体验最棒快感的人，就抓住这根手指！！"
    show tomo 17
    show sintarou 6 with dissolve
    tomo_and_shin "我！！我！！"
    play sound "fx/eureka.ogg"
    me "好！"
    extend "\n那大家！跟着我！！"
    extend "\n让我们一同感受最棒的快感！！"
    play sound "fx/tadaa.ogg"
    show bg remarkable
    show tomo 13
    show sintarou 7 with dissolve
    tomo_and_shin "哦哦哦！！！"
    window hide
    stop music fadeout 0.5
    show bg classroom with dissolve
    window show
    sinobu "烦死了。"
    play sound "fx/punch.ogg"
    $ renpy.transition(Quake(100, 0, 0.1, 0.065), layer='master')
    "咚！\n"
    hide tomo with dissolve
    play sound "fx/punch2.ogg"
    $ renpy.transition(Quake(100, 0, 0.1, 0.065), layer='master')
    "砰！！\n"
    hide sintarou with dissolve
    play sound "fx/punch3.ogg"
    $ renpy.transition(Quake(0, 500, 0.1, 0.065), layer='master')
    "砰砰！！"
    window hide
    play sound "fx/impact.ogg"
    show sinobu c7 1 at center with FadeWhite(0.5)
    window show
    play sound "fx/entrance.ogg"
    extend "现在还是白天，"
    play sound "fx/entrance.ogg"
    extend "这里是教室，"
    play sound "fx/entrance.ogg"
    extend "身为委员正在工作的时候……"
    show sinobu c7 3 with FadeWhite(0.5)
    play sound "fx/impact_japanese.ogg"
    extend "T·P·O！（行为举止要注意场合！）"
    window hide
    hide sinobu with dissolve
    show sinobu 4 at top with dissolve
    window show
    sinobu "以上。"
    "友＆慎＆我" "好、好的……抱歉，忍老师。"
    "忍保持着在洗手间释放的杀气，"
    hide sinobu with dissolve
    "就这样离开了。"
    window hide
    play sound "fx/triangle.ogg"
    show tomo 9 at top with dissolve
    window show
    tomo "那、那么，我们重整一下精神，\n来讨论关于服装的事情吧。"
    stop sound fadeout 0.5
    window hide
    hide tomo with dissolve
    hide bg with dissolve
    play music "quiet_lunch.ogg"
    show bg classroom at center with dissolve
    window show
    "之后，我们开始认真讨论，\n有关预算的事情，决定实际去店里之后再考虑，"
    extend "\n总之，我们先各自把服装的设计画在了素描簿上。"
    window hide
    show sintarou 8 at topright with dissolve
    window show
    sintarou "[player_name]这是什么画啊~。"
    extend "\n从头顶长出手来了啊！"
    show tomo 4 at topleft with dissolve
    tomo "真的啊~。好厉害。在某种意义上是艺术啊。"
    me "别、别管我啊！！"
    extend "\n我从以前开始就没什么画画的天分。"
    "被嘲弄的我，\n转而对友和慎太郎的画提出评价和意见。"
    show tomo 12
    show sintarou 3 with dissolve
    "不愧是有创意的年轻人们的画。"
    extend "\n虽然有些地方不太现实，但不管哪个都很新颖。"
    "而且，"
    play sound "fx/sparkle.ogg"
    show bg adult
    show tomo 13
    show sintarou 7 with dissolve
    "充满活力的少年的姿态，真是一饱眼福啊……。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    hide bg with dissolve
    show bg school_building_evening at center with Dissolve(1.0)
    window show
    "过了一会儿，快到四点的时候，"
    extend "\n在我们想完了所有方案后，小组活动成了单纯的涂鸦大会。"
    "我环顾四周，发现其他小组也基本完成了手头上的工作，正在各自休息。"
    window hide
    show bg classroom_evening with Dissolve(0.8)
    show tomo 3 at topleft with dissolve
    window show
    tomo "呼……"
    show tomo 12 with dissolve
    extend "\n我能稍微离开一下吗？"
    extend "\n反正事情都进展得很顺利，就趁现在休息一下吧。"
    show sintarou 13 at topright with dissolve
    sintarou "好啊。"
    extend "\n那我们明天再开始正式的活动！"
    "那么，我该做什么呢……？"
    hide tomo with dissolve
    hide sintarou with dissolve
    return

label day1_layout:
    hide 班選択 with dissolve
    window show
    me "去『布置组』看看吧！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "fx/footsteps.ogg"
    show sinobu 4 at topleft with dissolve
    window show
    sinobu "……"
    show tubasa 1 at topright with dissolve
    tubasa "……"
    me "……。"
    show sinobu 7 with dissolve
    sinobu "……"
    show tubasa 14 with dissolve
    tubasa "……"
    me "……。"
    play music "fx/ding.ogg"
    show cg dark at center with Dissolve(0.3)
    "一片令人窒息的沉默……！！！"
    extend "\n别的小组都那么热闹，\n这个组的成员为什么这么沉默啊！？"
    "这样下去根本没法工作，而且精神上也倍感煎熬。"
    extend "\n快点……快想点话题……！"
    window hide
    stop music fadeout 0.5
    hide cg with dissolve
    hide sinobu with dissolve
    hide tubasa with dissolve
    play music "discovery.ogg"
    window show
    me "呃，哎呀~今天天气真好啊！"
    me "话、话说回来，教数学的滑子老师不是前不久结婚了吗~？"
    extend "\n没想到那位滑子老师居然也结婚了啊~。"
    window hide
    show tubasa 21 at topright with dissolve
    window show
    tubasa "咦……？"
    show sinobu 5 at topleft with dissolve
    sinobu "之前……我记得那位老师不是一直都被称作『知名爱妻狂』嘛。"
    extend "\n他在开学典礼上还秀了一番恩爱呢。"
    play sound "fx/boing.ogg"
    "不、不好！！"
    extend "\n怎么能提十年前的八卦话题啊！！"
    "我看看我看看……有没有能跨越世代的话题……"
    me "你知道御咲祭的七大不可思议吗？"
    extend "\n校舍后面的室外厕所，封锁在最里面的隔间里……"
    show tubasa 20 with dissolve
    tubasa "那里有厕所？"
    show sinobu 2 with dissolve
    sinobu "没有。"
    play sound "fx/cute3.ogg"
    me "诶，那里没了！？为什么啊！？"
    show sinobu 23 with dissolve
    sinobu "我怎么知道。"
    extend "\n从刚才起，你说的话就有点不符合时代，真是奇怪。"
    "呜……就算变成同龄的样子，还是没有共同话题……！"
    extend "\n这就是年龄代沟吗！！"
    "虽然我曾对这梦境世界兴奋不已，但没想到事情会这么麻烦……。"
    me "那个……"
    show sinobu 24 with dissolve
    sinobu "什么？还有什么事吗？"
    me "呃……没什么事……。"
    show tubasa 22 with dissolve
    tubasa "……"
    show sinobu 7 with dissolve
    "……。"
    play sound "fx/ding.ogg"
    show cg dark at center with Dissolve(0.3)
    "沉默再次降临。"
    "诶，是我选错了组吗？"
    extend "\n……不对！！"
    extend "不管在什么情况下，\n只要能跟可爱的少年们一起工作，我就能克服任何困难！！"
    window hide
    stop sound fadeout 0.5
    stop music fadeout 2.5
    hide cg with dissolve
    hide sinobu with dissolve
    hide tubasa with dissolve
    show sinobu 4 at topleft with dissolve
    window show
    sinobu "……"
    show tubasa 1 at topright with dissolve
    tubasa "……"
    hide sinobu with dissolve
    hide tubasa with dissolve
    "果然还是很难熬啊……谁来救救我……。"
    window hide
    show sinobu 23 at top with dissolve
    window show
    sinobu "嗯，决定了。"
    me "诶，决定什么？"
    play music "quiet_lunch.ogg"
    show sinobu 7 with dissolve
    sinobu "我考虑了一下布置组的工作。"
    me "是、是啊。"
    extend "\n你有什么好主意吗？"
    show sinobu 3 with dissolve
    sinobu "实际去店里参观考察之后再做考虑。"
    me "诶、诶诶诶诶诶！！"
    extend "\n那今天的讨论要怎么办？"
    show sinobu 23 with dissolve
    sinobu "没法讨论。"
    extend "\n没办法啊，不清楚的事就是怎么思考也没用。"
    show sinobu 3 with dissolve
    extend "\n不满意的话，[player_surname]，你来提个主意好了。"
    me "呜……。"
    hide sinobu with dissolve
    show tubasa 19 at topright with dissolve
    tubasa "我、我也赞成，忍的意见。"
    extend "\n我们都没去过咖啡店，\n不知道该怎么设计布局。"
    show sinobu 23 at topleft with dissolve
    sinobu "那么，我们待会儿问问慎太郎有没有什么好的店。"
    show sinobu 2 with dissolve
    extend "\n然后，明天去考察，看看是什么感觉。"
    me "那、那至少也得考虑下\n给顾客坐的桌椅的数量。"
    extend "\n这样就结束讨论的话，剩下的时间就浪费了。"
    show sinobu 3 with dissolve
    sinobu "这个也不行。"
    extend "\n因为我们连要申请哪个教室都不知道。"
    me "诶？不是用这间教室吗？"
    show tubasa 13 with dissolve
    tubasa "根据店铺的规模不同，教室也会不同。"
    show tubasa 6 with dissolve
    extend "\n我们是两个班合开一家店，而且还要用到火，\n所以普通的教室不行。"
    me "原、原来是这样啊。"
    "我初中时都是听从执行委员的指挥，\n所以完全不了解情况……。"
    me "那么，我们什么时候能选教室？"
    show sinobu 24 with dissolve
    sinobu "后天开始。"
    extend "\n因为决定权在负责的海老师手里，我们要直接去找他谈，争取把教室拿下来。"
    show tubasa 21 with dissolve
    tubasa "不然的话，班上的同学会很困扰的……。"
    me "原来如此……。"
    show sinobu 23 with dissolve
    sinobu "眼下也没什么能做的了，虽然时间还早，但今天就先解散。"
    extend "\n正式的工作从明天开始。\n你们有意见吗？"
    show tubasa 6 with dissolve
    tubasa "没有。"
    me "唔……。"
    "这、这孩子真是坚定啊……。"
    window hide
    hide sinobu with dissolve
    hide tubasa with dissolve
    show tubasa 14 at top with dissolve
    window show
    tubasa "……"
    "翼偷偷瞄了一眼旁边的人。"
    extend "\n他从刚才开始好像就无法集中注意力了。"
    "这个小组……能好好完成工作吗？"
    hide tubasa with dissolve
    me "那个……你们对『要开一间什么样的咖啡厅』有想法吗？"
    stop music fadeout 1.5
    show tubasa 30 at topright with dissolve
    tubasa "……"
    show sinobu 25 at topleft with dissolve
    sinobu "那种事随便怎样都行吧。"
    extend "\n今天的讨论到此结束。"
    "不行……他不明白。"
    play music "hurry_up.ogg"
    me "你们两个不对吧，这可不行啊。"
    extend "\n我们可是代表两个班级的执行委员，\n得更有责任感，更积极地去思考才行！"
    me "光是完成交代的任务可不够。"
    extend "\n必须自己思考想要什么样的店铺，\n然后朝着这个目标好好地努力！"
    extend "\n如果一直是这样的态度，可是打造不出好的咖啡店的哦。"
    show sinobu 27 with dissolve
    sinobu "……"
    show tubasa 22 with dissolve
    tubasa "嗯……。"
    me "好啦好啦，说话啊。"
    extend "\n好好地把自己的想法传达出来！"
    show sinobu 14 with dissolve
    sinobu "……嗯。"
    show tubasa 20 with dissolve
    tubasa "……好的。"
    play sound "fx/eureka.ogg"
    me "再大声点！"
    show tubasa 9
    show sinobu 6 with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    "友＆忍" "嗯！"
    me "很好！"
    extend "\n那么，我再问一次，想要什么样的咖啡店？"
    show sinobu 17 with dissolve
    sinobu "……一间能够安静地读书的咖啡店吧……。"
    show tubasa 4 with dissolve
    tubasa "这样的话，BGM就不要流行音乐，而是古典音乐吧。"
    show tubasa 23 with dissolve
    tubasa "我的话……我想……"
    show tubasa 4 with dissolve
    extend "\n开一家『即便独自一人进去也不会犹豫』的咖啡店。"
    show sinobu 21 with dissolve
    sinobu "要实现一之濑同学的愿望的话，是需要吧台的呢。"
    me "嗯嗯！"
    extend "\n好啦，这样讨论的话，就能想出接近理想的方案，\n而且大家思考的干劲也就上来了吧？"
    me "顺带一提，我是希望能做成一家老少皆宜的咖啡店。"
    extend "\n为此，我们需要设置几个隔间，\n最好是能做出西式和日式两种风格。"
    show tubasa 31 with dissolve
    tubasa "这样的话，就需要去学艺室借榻榻米了呢。"
    show sinobu 7 with dissolve
    sinobu "隔间的话，用布帘围起来就可以了吧。"
    extend "\n不过搬榻榻米光靠我们几个肯定人手不够，\n所以得讨论集体协作的事了。"
    me "对对！！"
    extend "\n很好！你们俩都挺有干劲的嘛！！\n从明天开始也要保持这个势头加油哦！"
    extend "\n今天的作业就是想象一下你们各自理想中的咖啡厅！"
    show tubasa 31 with dissolve
    tubasa "我明白了。"
    show tubasa 4 with dissolve
    extend "\n话说回来，[player_name]君……总感觉好像老师一样。"
    show sinobu 22 with dissolve
    sinobu "是啊。"
    extend "\n而且还是个热血老师。"
    play sound "fx/dash.ogg"
    "咯噔"
    me "啊、啊哈哈哈！\n太期待学园祭了，我有些兴奋过头了呢~。"
    extend "\n抱歉，我有些得意忘形了~明明我也是和你们一样十五岁！"
    show tubasa 13 with dissolve
    tubasa "咦……？"
    show sinobu 5 with dissolve
    sinobu "我们的学年应该是十三或者十四岁才对……。"
    stop music fadeout 1.5
    play sound "fx/boing.ogg"
    me "啊，不、不对！搞错了！！\n对！！我是十四岁啦！！"
    extend "\n我有些兴奋过头，连自己几岁都搞错了。\n真讨厌~啊哈哈哈。"
    show sinobu 2 with dissolve
    sinobu "……"
    play music "quiet_lunch.ogg"
    show sinobu 23 with dissolve
    sinobu "那差不多告一段落了，\n我还有点事，可以稍微离开一下吗？"
    extend "\n大概三十分钟就能回来了。"
    show tubasa 5 with dissolve
    tubasa "好、好的。\n反正也没别的事要讨论了……"
    extend "\n那接下来就先自由活动吧。"
    me "好，就这么办吧。"
    show sinobu 12 with dissolve
    sinobu "嗯。一会儿见。"
    play sound "fx/sliding_door.ogg"
    hide sinobu with dissolve
    "说完，忍就离开了教室。"
    "自由活动……我应该做什么呢？"
    hide tubasa with dissolve
    return

label day1_cooking:
    hide 班選択 with dissolve
    window show
    me "我去『料理组』看看！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "twins_theme.ogg"
    show sora 3 at topright with dissolve
    window show
    sora "好，既然我们是『料理组』，"
    extend "\n那就先来讨论一下，要制定什么样的菜单吧。"
    show tuki 9 at topleft with dissolve
    tuki "空喜欢甜食，对这方面也很了解，甜点类就交给空吧。"
    extend "\n[player_surname]就和我一起考虑主食的菜单吧。"
    me "嗯，好的。"
    "虽说我是被双胞胎这少见的属性吸引，才选择了这个小组，但……"
    extend "\n真到了讨论的时候，刚才那股气势不知跑哪去了，反倒莫名紧张起来。"
    show sora 12 with dissolve
    sora "甜食吗。"
    extend "\n唔~……我是很喜欢，\n但进蛋糕店总觉得很不好意思，\n所以其实也没吃过多少次呢。"
    show tuki 5 with dissolve
    tuki "为什么会害羞呢？"
    extend "\n品尝喜欢的东西，还在意周围人的眼光干嘛？"
    show sora 13 with dissolve
    sora "因、因为……那种店里全是女孩子，\n我一个男生进去，会显得格格不入啊。"
    show tuki 4 with dissolve
    tuki "什么嘛，原来是这样啊。"
    extend "\n空，你放心吧。"
    extend "\n像你这般可爱、漂亮又清纯的话，\n就算是在那种地方，也不会让人觉得奇怪的。"
    show sora 14 with dissolve
    sora "什、什么嘛……感觉开心不起来。"
    show tuki 12 with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tuki "为、为什么啊。\n我这不是在夸你嘛？"
    show sora 27 with dissolve
    sora "因、因为，这不像是该对男孩子说的话啊。"
    show sora 5 with dissolve
    extend "\n你说是吧？[player_name]君。"
    me "嗯、嗯。"
    show tuki 7 with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/dash.ogg"
    tuki "才不会。\n这些话说给男生听也是可以的。"
    extend "特别是对空这样有魅力的人来说！！"
    extend "\n是吧，[player_surname]？"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    me "噢，嗯。"
    show tuki 1
    show sora 4 with dissolve
    "别、别两个人都盯着我啊……！"
    extend "\n现在的我，可完全没心思去应付你们小情侣的打情骂俏啊啊啊啊！！"
    show sora 2 with dissolve
    sora "话说回来，甜品啊。"
    extend "\n嗯……果然还是少不了芭菲呢！"
    extend "\n我一直很想试着亲手做一次巧克力香蕉芭菲看看。"
    extend "\n其他的还有什么呢……。"
    show tuki 9 with dissolve
    tuki "说起咖啡厅的主食，\n果然还是三明治和吐司之类的面包为主流啊。"
    extend "\n不过，森海说还会加入加入日式和中式风格，\n该如何安排才好呢……"
    show sora 3 with dissolve
    sora "[player_name]君，你有什么喜欢的甜点吗？"
    show tuki 15 with dissolve
    tuki "[player_surname]，关于其他的菜品，你有什么主意吗？"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    me "哦、哦……"
    show tuki 16
    show sora 21 with dissolve
    tuki_and_sora "……？"
    "空和月面面相觑。"
    show sora 5 with dissolve
    sora "[player_name]君，你的身体还是不舒服吗？"
    extend "\n真的不要紧吗？没有发烧吧？"
    show tuki 6 with dissolve
    tuki "我刚才也说过吧，这种时候不用客气，直接说出来。"
    extend "\n不然的话，不只是你，还会影响到周围的人啊。"
    me "没、没问题的！"
    extend "\n你看~我这不是好好的嘛，精神得很！！"
    "为了不让二人担心，我摆出展示肌肉的姿势，拼命表现出我很健康的样子。"
    play sound "fx/eureka.ogg"
    "没错！"
    extend "\n只要看着他们俩，跟往常一样进行些危险的想象，"
    extend "\n紧张感一定很快就会缓解的！"
    hide sora with dissolve
    hide tuki with dissolve
    show sora 21 at top with dissolve
    sora "虽然我也想卖蛋糕，不过手工制作实在太辛苦了。"
    extend "\n到底该怎么做才好呢？"
    "赤峰空君……"
    window hide
    play sound "fx/sparkle.ogg"
    show cg c47 1 at center with dissolve
    window show
    extend "说到底，这孩子最棒的还是这副温柔的神情。"
    extend "\n光是看着那平静的面容，就能治愈心灵了。"
    "还有，这线条纤细而优美的身体。"
    extend "\n但是，这也不意味着他是弱不禁风的。"
    extend "\n柔韧的肌肉也恰到好处地附着在骨骼之上。"
    extend "\n这简直是集青春期少年的特质于一身的，极具魅力的体型啊。"
    "哈、哈……。"
    window hide
    hide sora with dissolve
    hide cg with dissolve
    show tuki 3 at top with dissolve
    window show
    tuki "该不该推出一些米饭或者面类主食呢……"
    extend "\n不过这样做似乎很费功夫，而且跟学校食堂没什么两样了……。"
    "赤峰月君……"
    window hide
    play sound "fx/sparkle.ogg"
    show cg c47 2 at center with dissolve
    window show
    extend "与气质柔和的空君相对，这张凛然的面容真是格外帅气。"
    extend "\n但正因他是这般硬汉，\n一旦沦为受方之时，究竟会露出怎样的表情——\n难道只有我一个人在意这点吗！？"
    "更何况，不管怎么说，这副锻炼得来的肌肉体格简直太美妙了。"
    extend "\n那结实壮硕的身体，手感一定很不错吧。"
    extend "\n虽说我比他年长，但真想被他抱一次啊……。"
    hide cg with dissolve
    hide tuki with dissolve
    hide bg with dissolve
    stop music fadeout 2.0
    "呼……哈啊……"
    window hide
    show bg classroom at center with dissolve
    show sora 19 at topright with dissolve
    window show
    sora "那、那个……[player_name]君？"
    show tuki 16 at topleft with dissolve
    tuki "从刚才开始，你的喘气声就很粗哦。\n怎么了？"
    me "啊……。"
    play sound "fx/boing.ogg"
    "呜！！糟了！"
    extend "\n这次，反倒是露出本性了……！"
    show sora 22 with dissolve
    play music "discovery.ogg"
    sora "果然身体不舒服吧！！\n我们去医务室吧！"
    show tuki 6 with dissolve
    tuki "是啊。"
    extend "\n[player_surname]这家伙相当倔呢，就算硬拖也要把他带过去。"
    me "不、不是的，不是这样的，你们两个！\n这、这是有原因的……"
    show sora 23 with dissolve
    sora "少啰嗦！"
    extend "\n来，哥哥。你架住那边的肩膀。"
    show tuki 17 with dissolve
    tuki "我明白了。"
    extend "\n要站起来咯，一、二、三！"
    "就这样，我在空和月的左右搀扶下，被『押送』到了医务室。"
    stop music fadeout 0.5
    window hide
    play sound "fx/sliding_door.ogg"
    hide sora with dissolve
    hide tuki with dissolve
    hide bg with dissolve
    play music "quiet_lunch.ogg"
    show cg school_building_morning at center with Radial(0.5)
    show bg infirmary with dissolve
    window show
    teacher "嗯。"
    extend "\n体温和脉搏都很正常。\n喉咙好像也没有肿起来，应该没什么问题。"
    extend "\n不过，你还是躺一会儿，等没有不舒服的感觉了再回教室。"
    show tuki 15 at topleft with dissolve
    tuki "我明白了。"
    extend "\n非常感谢您。"
    show sora 22 at topright with dissolve
    sora "好了，[player_name]君。"
    extend "\n到这边的床上来吧~。"
    "彻底被当成病号对待了……再加上这突如其来的展开让我身心俱疲，"
    extend "\n我已经连反驳的力气都没了，只好乖乖地躺到了床上。"
    "啊~感觉就像在翘课一样，简直就像是漫画情节。"
    extend "\n以前的我还很老实，做不出这种事情啊~。"
    window hide
    hide cg with dissolve
    hide tuki with dissolve
    hide sora with dissolve
    show sora 5 at topright with dissolve
    window show
    sora "你是从什么时候开始觉得不舒服的呢？"
    extend "\n最近天气变冷了吧。"
    extend "\n是不是因为这个，身体才有点不舒服呀？"
    show tuki 5 at topleft with dissolve
    tuki "要喝点什么吗？"
    extend "\n我可以把室温再调高一点。"
    extend "\n有能帮上忙的地方的话，尽管说。"
    "啊，不过，这样就挺好的……。"
    extend "\n能被两个少年这样温柔对待，\n我还真是幸福啊……。"
    me "谢谢你们。\n但是，我真的没事，不用担心。"
    extend "\n你们的好意我心领了。"
    show sora 4 with dissolve
    sora "是吗……\n那就好。"
    extend "\n哥哥，料理组的讨论要怎么办？"
    show tuki 4 with dissolve
    tuki "嗯，我看我们留在这里也帮不上什么忙，\n况且还有老师在照看。"
    extend "\n不如我们先回教室，继续讨论吧。"
    me "欸。"
    show sora 21 with dissolve
    sora "说得也是。"
    extend "毕竟离御咲祭也没剩多少时间了，\n那就先去推进一下我们两个能做的工作吧。"
    me "等……！"
    hide sora with dissolve
    hide tuki with dissolve
    play sound "fx/shock.ogg"
    "等、等一下！！"
    extend "\n既然那样的话，我也要回教室……！"
    extend "\n要是没有你们俩陪在身边，这样根本就毫无意义啊！！"
    "不过，就算我现在说要回教室，他们两个肯定也会拦着我的吧。"
    "那么……"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    me "咳、咳咳！！"
    extend "\n请、请等一下……。"
    extend "\n要是你们俩都不在，\n我……一寂寞，感觉感冒都要加重了……。"
    "感什么冒啊。"
    extend "\n我是兔子吗。"
    extend "\n都25岁的人了，还这么丢人现眼……。"
    "但是！！"
    play sound "fx/dash.ogg"
    "面对这种天大的甜头，我怎么能眼睁睁看着它结束！！"
    show sora 19 at topright with dissolve
    sora "唔、唔……"
    extend "\n那么，是不是留一个人在这里比较好……？"
    show tuki 2 at topleft with dissolve
    tuki "行吧。\n那另一个人回教室继续工作。"
    extend "\n毕竟，我们也不能在这里讨论工作的事。"
    hide tuki with dissolve
    hide sora with dissolve
    return

label day1_supply:
    hide 班選択 with dissolve
    window show
    me "我去『采购组』！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    show sakuya 19 at topleft
    show saburo 18 at topright with dissolve
    window show
    play sound "fx/ding.ogg"
    saburo "好困……。"
    sakuya "好无聊……。"
    me "……。"
    stop sound fadeout 0.5
    show saburo 6 with dissolve
    play music "discovery.ogg"
    saburo "我说，咱们虽说是采购组，但这也没啥好讨论的吧？"
    extend "\n说白了，不就是负责把材料弄来就行了吗？"
    show sakuya 1 with dissolve
    sakuya "就是说啊~。"
    extend "\n真是的……那个笨蛋班长，安排得也太烂了吧。"
    extend "\n我们留在这根本没意义啊。"
    me "嘛、好啦好啦，别这么说嘛。"
    extend "\n你看~……比如！\n我们可以先讨论一下去哪家店采购比较好呀？"
    show saburo 9 with dissolve
    saburo "那更是得等对面的指示才行啊~。\n毕竟咱们连要买啥都不知道呢。"
    show sakuya 11 with dissolve
    sakuya "你这家伙，是个笨蛋吧~。"
    hide sakuya with dissolve
    hide saburo with dissolve
    window hide
    $ renpy.transition(Quake(0, 50, 0.1, 0.1), layer='master')
    play sound "fx/punch2.ogg"
    window show
    "（受打击！！）"
    "呜……现在的孩子，嘴巴还真是毒啊……。"
    window hide
    show saburo 17 at topright with dissolve
    window show
    saburo "怎么办呢~穗海。\n要不要去跟班长抗议一下，让他放咱们早点回去？"
    show sakuya 1 at topleft with dissolve
    sakuya "别了，真要那么干的话，\n肯定又得跟那个笨蛋吵起来，只会变得更麻烦。"
    show sakuya 15 with dissolve
    extend "\n我们自己随便找点乐子打发时间好了。"
    show saburo 4 with dissolve
    saburo "说的也是。"
    "这么说着，两人离开了座位。"
    play sound "fx/running.ogg"
    hide saburo with dissolve
    hide sakuya with dissolve
    me "诶？等、等等？"
    play sound "fx/sliding_door.ogg"
    stop music fadeout 2.0
    hide bg with dissolve
    "我的声音根本没能叫住他们，两人就这样走出了教室。"
    show bg classroom at center with dissolve
    play sound "fx/ding.ogg"
    me "………………。"
    "诶……难道我就这样落单了吗！！？"
    extend "\n明明好不容易回到了初中时代，本该和身边的少年们打得火热，\n享受愉快的校园生活才对，结果开局就是这副鬼样子啊！？！？"
    stop sound fadeout 0.5
    "怎么能让这梦幻般的机会化为泡影！！"
    $ renpy.transition(Quake(0, 50, 0.1, 0.06), layer='master')
    play sound "fx/dash.ogg"
    "咣当"
    play music "cute_silly.ogg"
    "我猛地站起身，大家被吓了一跳，纷纷转头看向我。"
    show tomo 28 at topleft with dissolve
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    tomo "怎、怎么了？[player_name]你突然站起来干嘛！！？"
    extend "\n是不是又想去厕所了！？？"
    show sintarou 29 at topright with dissolve
    sintarou "年轻真好啊~。"
    me "不、不是！！"
    extend "\n我去找一下作哉君和三朗君…。"
    show tomo 21 with dissolve
    tomo "诶？"
    show tomo 5 with dissolve
    play sound "fx/cute2.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    extend "\n啊！！那两个家伙，不知不觉就不见了！！！"
    extend "\n真是的，那帮不良~……。"
    show sintarou 17 with dissolve
    sintarou "难道说，[player_name]酱被孤立了？"
    extend "\n哎呀呀~好可怜啊……。"
    me "那个，你们知道他们俩可能会去哪里吗？"
    show sintarou 19 with dissolve
    sintarou "嗯~如果是三酱的话，应该是在楼顶悠闲地睡午觉吧？"
    show tomo 26 with dissolve
    tomo "技安应该是在教学楼后面。"
    extend "\n他们俩经常在那里打打闹闹的……。"
    me "这样啊。谢谢你们！"
    extend "\n我去看看。"
    show tomo 3
    show sintarou 1 with dissolve
    tomo_and_shin "慢走哦。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    play sound "fx/sliding_door.ogg"
    show bg hallway with dissolve
    window show
    "那么，走出教室后，我去哪里好呢……"
    return

label day1_design_tomo:
    window show
    "跟着友去看看！"
    extend "\n说不定会发生像刚刚那样的有趣的事情。"
    me "那我也先离开一下。"
    "跟慎太郎说完后，我跟着友来到走廊。"
    window hide
    show tubasa 14 at top with dissolve
    window show
    tubasa "……"
    window hide
    hide tubasa with dissolve
    hide bg with dissolve
    play sound "fx/sliding_door.ogg"
    show bg hallway_evening at center with dissolve
    window show
    "跟随着友走在顶楼的走廊上。"
    "他要去哪里呢？前面有什么东西吗。"
    stop music fadeout 0.5
    "来到走廊尽头，我看到友把手放在门上，\n门上挂着「音乐教室」的门牌。"
    window hide
    play music "tomo_theme.ogg"
    show tomo 18 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    window show
    tomo "哇！[player_name]君，你在尾随我吗？"
    me "啊哈哈。"
    extend "\n友君你要去哪里，我有些好奇。"
    show tomo 11 with dissolve
    play sound "fx/boing.ogg"
    tomo "哎呀哎呀，[player_name]君，你才这么点年纪就喜欢跟踪别人啦？"
    extend "\n真是未来可期呢~。"
    "将来岌岌可危的是你们俩才对……。"
    show tomo 2 with dissolve
    tomo "开个玩笑啦！"
    show tomo 12 with dissolve
    extend "\n[player_name]君要不要也来听听看我的钢琴演奏呢？"
    window hide
    hide tomo with dissolve
    hide bg with dissolve
    play sound "fx/sliding_door.ogg"
    show bg music_room_evening at center with dissolve
    window show
    "（叮铃铃）"
    "音乐教室和平常的教室不一样，没有课桌\n只有靠墙排列的椅子。"
    extend "\n可能因为这样，才会让人感觉十分宽敞。"
    "音乐教室啊……。"
    extend "\n虽然平时除了上课之外没怎么接触过，但是墙上贴的音乐家的肖像画给我留下了深刻的印象。"
    extend "\n哈哈……我也只知道贝多芬而已。"
    me "好怀念啊……。"
    window hide
    show tomo 21 at top with dissolve
    window show
    tomo "怀念？怀念什么？"
    me "没，没什么！"
    extend "\n对了，原来友君会弹钢琴啊。"
    extend "\n有些意外呢~。"
    show tomo 2 with dissolve
    tomo "诶嘿~！这种话我经常会听到呢。"
    extend "\n一天不弹一次我就不舒服呢~。"
    show tomo 7 with dissolve
    extend "\n虽然我家也有钢琴，\n不过因为要准备学园祭，所以回去的时间会比较晚，没时间弹。"
    show tomo 12 with dissolve
    tomo "那么，唔，该弹什么呢。"
    show tomo 10 with dissolve
    extend "\n……好，就弹那个吧！"
    show cg yellow at center with dissolve
    "刚才还在开玩笑的少年\n究竟会弹出多么有趣而又美妙的曲子呢。我有些期待"
    stop music fadeout 2.0
    extend "\n比如超高速『踩到猫』之类的吗。"
    extend "那个相当厉害呢。"
    "友将手指放在琴键上，按了下去。\n"
    window hide
    hide cg with dissolve
    hide bg with dissolve
    hide tomo with dissolve
    play music "gymnopedie.ogg"
    pause 0.5
    show cg c8 at center with Radial(2.0)
    window show
    extend "……。"
    "……"
    extend "……诶？"
    "这，这真是令人惊讶啊……。"
    extend "\n没想到他居然能弹奏出这种曲子啊！"
    "好厉害啊……。"
    extend "\n虽然对音乐一窍不通的我没法表达清楚，\n但能够让听者觉得美妙的演奏，一定称得上是优秀的演奏。"
    "嗯~这种曲子，好像在什么地方听过啊……。"
    extend "\n是在电视广告里播放的吗？"
    extend "虽然不知道曲名。"
    "哈啊……真是令人平静啊。心情也舒畅了许多。"
    extend "\n仿佛连工作的疲倦都一扫而空了。"
    extend "\n话说，现在是初中生啊。"
    "真想永远听他演奏下去啊。"
    "弹奏着钢琴的友，与平时判若两人，\n表情威风凛凛，手指动作也十分华丽。"
    "仿佛身处梦境中，又进入了更为美妙的梦境一般。"
    window hide
    show bg music_room_evening at center
    stop music fadeout 3.0
    hide cg with Dissolve(1.3)
    hide tomo with Dissolve(1.3)
    show tomo 3 at top with dissolve
    window show
    tomo "呼……"
    play music "tomo_theme.ogg"
    show tomo 12 with dissolve
    extend "怎么样？"
    "弹奏完之后，友又变回了平时那和蔼的表情。"
    "我一边拍着手，一边靠近友。"
    me "哎呀……真的很棒啊。"
    extend "\n好久都没有被感动过了。谢谢。"
    extend "\n都让人想录下来做成开车的BGM了。"
    show tomo 6 with dissolve
    tomo "开，开车……还早着呢。"
    show tomo 4 with dissolve
    extend "\n但是，谢谢你的收听！"
    show tomo 10 with dissolve
    extend "\n刚才的曲子，是萨蒂作曲的『Gymnopedies』。"
    extend "\n是我很喜欢的一首曲子~。"
    tomo "顺带一提，『Gymnopedies』的意思是，\n『裸体少年们的节日』哦。"
    play sound "fx/sparkle.ogg"
    show tomo 11 with dissolve
    extend "\n[player_name]君很喜欢这种题材吧？"
    "友露出小恶魔般的笑容说到。"
    me "没，没那种事哦！"
    extend "\n我是很健全的……。"
    show tomo 2 with dissolve
    tomo "骗人~！！"
    extend "\n刚才在教室，聊色色的事聊得那么起劲！"
    tomo "而且，"
    show tomo 11 with dissolve
    play sound "fx/boing.ogg"
    extend "在厕所的时候也完全没有抵抗。"
    me "呜咕……"
    extend "对，对了。\n小友你是为什么开始学钢琴的？"
    extend "\n你以前上过钢琴课吗？"
    show tomo 1 with dissolve
    tomo "没有。"
    extend "\n一直都是妈妈教我的。"
    me "哦～原来妈妈还会弹钢琴啊，那很了不起啊~。"
    show tomo 4 with dissolve
    tomo "嗯！妈妈就是钢琴老师！"
    show tomo 10 with dissolve
    extend "\n弹得很好，还去了维也纳，\n还参加了那里的管弦乐团的钢琴协奏曲演出哦！"
    extend "\n深受那边有名的指挥的信赖呢~。"
    play sound "fx/cute.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.09), layer='master')
    me "嘿，嘿~！好厉害啊！！！维也纳吗！！"
    extend "\n而且，管弦乐团！？钢琴协奏曲！"
    extend "\n指挥啊~！嗯~！"
    hide tomo with dissolve
    "中学生说出这种厉害的词语，我不由得有些退缩。"
    extend "\n都25岁了，还真是羞愧……。"
    me "顺便问一下，你父亲是做什么的？"
    window hide
    show tomo 22 at top with dissolve
    window show
    tomo "嗯~。父亲吗。"
    extend "\n如果是有名大公司的社长……真好啊。"
    "如果是……？"
    extend "实际上是小企业的普通员工吗。"
    show tomo 21 with dissolve
    tomo "嗯……？"
    stop music fadeout 2.0
    hide tomo with dissolve
    show tomo 4 at topright with dissolve
    extend "翼 ！！"
    extend "\n别站在门口，进来嘛！"
    "我一回头，"
    show tubasa 1 at topleft with Dissolve(0.8)
    "发现翼偷偷站在了门口。"
    hide tubasa with dissolve
    hide tomo with dissolve
    window hide
    play music "tubasa_theme.ogg"
    show tubasa 3 at topleft with dissolve
    window show
    tubasa "那，那个……打扰了…。"
    "翼小声说着，靠近我。"
    show tomo 1 at topright with dissolve
    tomo "翼的小组也在休息？"
    extend "\n怎么样？讨论的顺利吗？"
    show tubasa 5 with dissolve
    tubasa "嗯，嗯。还行吧。"
    show tubasa 1 with dissolve
    "翼来回看了看友和我，然后露出了复杂的表情。"
    "哦，他是在担心我们俩的关系吧。"
    "察觉到这点的我，便主动向翼搭话。"
    me "你也知道了吗？友会弹钢琴。"
    show tubasa 2 with dissolve
    tubasa "嗯，嗯。"
    extend "\n我一开始也是听了刚才的『Gymnopedies』……"
    show tubasa 12 with dissolve
    extend "那时候真是吓了我一大跳啊。"
    me "也是啊。"
    extend "我也被吓了一跳呢。"
    extend "\n哎呀~真是，人不可貌相呢。"
    show tomo 6 with dissolve
    tomo "你这是在夸我还是在损我啊~？？"
    me "当然是在夸你了！"
    extend "\n友君，谢谢你让我聆听了这么美妙的音乐。"
    extend "\n不仅是音乐，你弹奏的样子也非常华丽哦。"
    extend "\n下次再让我欣赏一下吧。"
    show tomo 8 with dissolve
    tomo "你，你这么夸我，我都有点害羞了……。"
    show tomo 23 with dissolve
    extend "\n不，不用谢……。"
    show tubasa 14 with dissolve
    tubasa "……"
    show tomo 24 with dissolve
    tomo "哎呀，在这休息得似乎有点久了呢。"
    extend "\n弹了一曲后终于清爽多了，回教室吧！"
    play sound "fx/sliding_door.ogg"
    hide tomo with dissolve
    "说完，友从音乐教室里出来了。"
    window hide
    hide tubasa with dissolve
    show tubasa 15 at top with dissolve
    window show
    tubasa "[player_name]君……对友君是…。"
    me "诶？"
    show tubasa 8 with dissolve
    tubasa "没，没什么！"
    show tubasa 4 with dissolve
    extend "\n我，我们也一起去！"
    "真是的……这个孩子也太好懂了。"
    me "翼……你真的喜欢友君呢。"
    show tubasa 8 with dissolve
    $ renpy.transition(Quake(0, 65, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tubasa "诶！？"
    extend "你，你在说什么"
    me "嗯，我知道的。"
    extend "\n就算是从我这个大人角度来看，那个孩子也非常有魅力。"
    show tubasa 2 with dissolve
    tubasa "这，这是……什么意思？"
    me "这个嘛~秘密♪"
    show tubasa 7 with dissolve
    $ renpy.transition(Quake(0, 65, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    tubasa "诶诶诶诶！"
    extend "\n请，请告诉我，[player_name]君！！"
    me "不行♪"
    tomo "你们两个在干什么呢~？？"
    extend "\n赶紧走吧！"
    window hide
    hide tubasa with dissolve
    window show
    "我从正摸着耳朵的翼身边溜出来，朝门口走去，正好遇到了回来叫我们的友。"
    "翼看着我们走远，更加焦急地跟了上来，\n我们就这样悠闲地离开了音乐教室。"
    window hide
    stop music fadeout 0.5
    hide bg with Dissolve(0.8)
    return

label day1_design_sintarou:
    show bg classroom_evening at center
    window show
    "连动起来都觉得没劲，还是留在教室吧。"
    "我再次凝视着放在我桌上的画。"
    extend "\n先不说我，慎太郎画得比友好太多了。"
    stop music fadeout 0.5
    me "慎太郎你很擅长画画呢！"
    extend "\n你喜欢这类的东西？"
    window hide
    play music "sintarou_theme.ogg"
    show sintarou 1 at top with dissolve
    window show
    sintarou "算是吧~。"
    extend "\n咱非常喜欢动漫和漫画呢。"
    me "是这样啊！！\n我也经常看这类的！"
    extend "\n知道『魔法少女小袁』吗？"
    "『魔法少女小袁』，是一部在部分群体中很有人气的深夜动画。"
    extend "\n……如果是『魔法少年』的话，在我心中的评价会更高。"
    show sintarou 4 with dissolve
    sintarou "知道知道！！那个超有趣的～！\n很在意之后的展开哦～。"
    show sintarou 25 with dissolve
    play sound "fx/dash.ogg"
    extend "\n关于那个Q太郎。"
    "哦！没想到他也看啊！！"
    extend "\n不过，像这样能聊到共同话题真是令人高兴。"
    extend "\n看来我和这孩子兴趣相仿啊！"
    show sintarou 12 with dissolve
    sintarou "想看朔和夕阳变得更乱七八糟啊！"
    "嗯？还在画吗~。看起来很享受啊。"
    extend "\n我看看，他画的到底是什么？"
    "……诶。"
    me "慎，慎太郎，那个角色是……。"
    window hide
    show cg c22 at center with dissolve
    window show
    sintarou "这个？"
    extend "\n嗯~……就算是你，[player_name]估计也不知道吧？"
    extend "\n这是漫画《见习魔术师的任务！》里的角色。"
    play sound "fx/eureka.ogg"
    me "！！！"
    extend "\n我知道！！当然我知道啊！！！我全集都有收藏！"
    extend "\n我可是真爱粉！"
    window hide
    hide cg with dissolve
    hide sintarou with dissolve
    show sintarou 6 at top with dissolve
    window show
    play sound "fx/cute2.ogg"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    sintarou "真的吗！！没想到[player_name]酱居然也在看啊啊啊！！！完全没想到！"
    extend "\n既然这样，你早说嘛~！"
    me "因，因为那个是……\n毕竟它是成人向，内容也很那个。"
    extend "\n难道说，慎太郎你喜欢这种类型的？"
    show sintarou 7 with dissolve
    sintarou "当然喜欢！简直是我最喜欢的！"
    extend "\n像刚才说的《魔法少女小袁》，我觉得如果是魔法少年就好了！"
    play sound "fx/explosion3.ogg"
    "他居然也跟我有同样的想法！！"
    "这家伙……居然是个正太控啊！"
    extend "\n真，真是岂有此理！！！！"
    show sintarou 9 with dissolve
    sintarou "没想到在这里能遇到志同道合的朋友……！"
    show sintarou 8 with dissolve
    extend "\n朋友们都不是正太控，所以没法和他们提起，\n从今以后，我们就一起尽情聊正太萌的话题吧！！"
    me "嗯，正有此意！"
    "在现实中遇到正太控朋友，简直就像中了头奖一样，\n我们不禁热情地握了手。"
    show sintarou 27 with dissolve
    sintarou "《见习魔法师》的作者画风不太稳定呢。"
    extend "\n初期和现在的画风变化好大。"
    me "确实。\n初期的画里阴影很多，现在却变得很清爽了。"
    extend "\n毕竟每个人对画风的喜好都是不一样的，\n正因如此，可能这样能迎合更多人的喜好吧。"
    show sintarou 15 with dissolve
    sintarou "原来是这样~。"
    extend "\n如果手里有全集的话，就能在其中发现自己喜欢的画风，像这样吗？"
    me "对对！！"
    extend "顺带一提，我是属于初期党的！\n因为整体色调偏暗，所以正太的肌肤才会显得更加白皙。"
    show sintarou 1 with dissolve
    sintarou "诶~我是更喜欢现在这个~。"
    show sintarou 2 with dissolve
    extend "\n因为初期的画风太混乱了，现在的画风更好阅读。"
    extend "\n虽然阴暗的氛围和SM风格稍微差了一点。"
    me "说到阅读性，那个作者的用词也是相当有趣呢。"
    extend "\n就算没有错，但表达方式很奇怪，可能有些难读懂。"
    show sintarou 17 with dissolve
    sintarou "啊~我懂。"
    extend "\n实际上，错别字和缺字也是屡见不鲜，在色情场景出现更是令人扫兴。"
    me "嗯嗯！"
    extend "\n说起来，色情场景里也是有着触手，机械之类的，比较特殊呢。"
    extend "\n虽然作者是喜欢V形线，所以着重于夕阳的V字比基尼，\n但我对竞赛的泳装不是特别感兴趣……。"
    show sintarou 25 with dissolve
    play sound "fx/dash.ogg"
    $ renpy.transition(Quake(0, 60, 0.1, 0.09), layer='master')
    sintarou "你根本就不懂啊！！"
    extend "披风下的比基尼，那个才好啊！"
    "好热……！好热血啊！！！"
    extend "\n初中生就能说出这么专业的话了……！！"
    "这不就是披着孩子皮的大人嘛。"
    extend "\n等等，我就是这样的啊。"
    me "初中生却能说出这么多话，真是吓我一跳。"
    extend "\n慎太郎君不像是孩子呢。"
    show sintarou 4 with dissolve
    sintarou "呼呼~彼此彼此吧~。"
    extend "所谓小大人吧？"
    extend "\n[player_name]你才是，内心其实已经30岁了吧~？"
    show sintarou 9 with dissolve
    extend "\n那种「初中生外皮的大人」在同人志上也有过哦~"
    me "真，真失礼！！"
    extend "\n我才25啊！！"
    "『小大人』也不是那个意思啊！"
    show sintarou 14 with dissolve
    sintarou "咦？25？"
    play sound "fx/boing.ogg"
    "啊"
    extend "\n不妙！！！"
    me "只是开玩笑啦~♪"
    extend "\n啊，啊哈哈！\n开玩笑啦~。"
    show sintarou 18 with dissolve
    sintarou "呼~嗯。"
    extend "这个玩笑也太无聊了。"
    show sintarou 2 with dissolve
    sintarou "不过，真的发生了那种事的话就有趣了呢。"
    extend "\n外表是孩子！头脑是大人！就像某位名侦探一样。"
    show sintarou 13 with dissolve
    extend "\n话说，那个孩子也很可爱呢！眼镜正太万岁！！"
    extend "\n那种长相，还什么都懂，真是让人受不了！"
    play sound "fx/cute2.ogg"
    "哇哦又说了一样的话！！"
    extend "\n这是命运吗！？！？"
    "……我俩这么心有灵犀，所以讲实话也没关系吧？"
    play sound "fx/sparkle.ogg"
    show cg orange at center
    show sintarou 3 with dissolve
    extend "我觉得，慎太郎一定能理解我，相信我。"
    "话说，难道慎太郎其实跟我一样，是个成年人？"
    "说到底，为什么我要将这件事保密呢？"
    extend "\n毕竟再怎么写实，这都是梦。"
    "哼！管他呢！"
    hide cg with dissolve
    hide sintarou with dissolve
    me "慎太郎，和我去一趟厕所！"
    extend "\n我有秘密要跟你说！！"
    show sintarou 12 at top with dissolve
    sintarou "嗯~？又要去厕所做那种事？"
    extend "\n你真是的[player_name]酱~"
    me "行，行啦！！"
    "我硬是把闹腾的慎太郎带离教室，走向厕所。"
    window hide
    play sound "fx/running.ogg"
    hide sintarou with dissolve
    hide bg with dissolve
    stop music fadeout 0.5
    show bg washroom at center with dissolve
    show sintarou 3 at top with dissolve
    window show
    "进到厕所后，我慢慢开始说起实话。"
    me "慎太郎……"
    extend "其实我啊，虽然外表是初中生，但真实年龄是25岁。"
    extend "\n准确来说，就只有外表变回初中生了……。"
    show sintarou 28 with dissolve
    sintarou "……"
    "慎太郎什么也没说，摆出一副异常认真的表情听着。"
    extend "\n他是不是在思考什么？"
    me "然，然后，刚才跟你聊天时，我突然想到，"
    extend "\n难道说，慎太郎也跟我一样，实际是成年人……。"
    "话说到一半，慎太郎终于开口了。"
    show sintarou 24 with dissolve
    sintarou "不对。"
    me "诶"
    show sintarou 19 with dissolve
    sintarou "很遗憾，我真的是十四岁。"
    extend "\n并不是什么成年人。"
    me "这，这样啊……也是。"
    show sintarou 18 with dissolve
    sintarou "所以，[player_name]关于你说的"
    extend "你有证据吗？"
    me "证，证据……？"
    show sintarou 29 with dissolve
    sintarou "嗯。[player_name]能证明你心里是个大人的证据。"
    extend "\n这种事突然说出来，我想谁都不会相信的。"
    "慎太郎所说的话，完全是正确的。"
    extend "\n这种事，怎么可能让人轻易相信。我很清楚。"
    "即便如此，我认为慎太郎和其他人不同，他能接受我。"
    me "证据嘛……。"
    "我失去了依靠，我的目光迷茫地飘浮在半空中。"
    extend "\n脑子一片空白。"
    "虽然我一直认为这只是梦，"
    extend "\n但没人相信这件事，给我带来了这么大的打击……。"
    window hide
    show sintarou 9 with dissolve
    window show
    sintarou "啊，我先说好了，"
    play sound "fx/wow2.ogg"
    extend "不可以做爱。"
    "是啊，不可以做爱……做爱。"
    play music "sintarou_theme.ogg"
    play sound "fx/boing.ogg"
    me "呃，啥？"
    "慎太郎出人意料的发言让我吃了一惊。"
    show sintarou 12 with dissolve
    sintarou "不是~，我本以为[player_name]你会说「用身体证明！！」或者什么的，\n然后顺势带入那种感觉里呢~。"
    show sintarou 13 with dissolve
    sintarou "但是很抱歉，色情的技巧并不能证明什么哦。"
    extend "\n因为也有技巧堪比大人一样的小孩子啊♪"
    "慎太郎得意洋洋地拍了拍自己的胸膛。"
    "没，没想到他会这么想……！我竟然……！！"
    extend "\n该死……不仅外表，连思维也要变得年轻灵活才行！！"
    "不，还没完……。还没完，现在开始思考！"
    extend "我还很年轻！！"
    me "呵，呵呵~！\n那就让我看看你的技巧吧！"
    extend "\n不然的话，就说明根本没有这样的小孩子，\n而我就要用我的技巧来证明自己个大人哦。"
    show sintarou 21 with dissolve
    sintarou "唔！你真敢说啊！！"
    show sintarou 23 with dissolve
    extend "\n真是的，没办法了啊……。"
    "慎太郎这么说着，把手放在了衬衫的纽扣上。"
    play music "fx/cute2.ogg"
    extend "\n这，这是要来真的啊……！！？"
    show sintarou 4 with dissolve
    sintarou "开玩笑的~♪"
    extend "\n才不会让你得逞呢，这位客官。"
    "慎太郎把手停在了纽扣上，然后微微一笑。"
    show sintarou 1 with dissolve
    sintarou "这样的话，不管是哪边，[player_name]都会如愿，"
    show sintarou 2 with dissolve
    extend "\n不如，从现在开始，咱要认真地观察[player_name]\n，判断你内心是否真的是大人！"
    me "诶……也就是说，你相信我说的话了？"
    show sintarou 13 with dissolve
    sintarou "嘛~啊~。"
    extend "\n虽然没有完全肯定，但[player_name]看起来不擅长说谎，\n我认为可能性不是0啊~。"
    show sintarou 2 with dissolve
    sintarou "而且！咱啊，很喜欢这种像是漫画一样的展开呢！"
    "原来如此啊。"
    extend "\n作为一成不变的校园的调味料，享受一下这种展开吧。"
    show sintarou 1 with dissolve
    sintarou "好了~话也说完了，差不多该回教室了吧！"
    hide sintarou with dissolve
    "我突然看了看手表，指针指着四点二十五分。"
    extend "\n已经这么晚了啊。"
    show cg orange at center with Dissolve(0.8)
    "总觉得，时间过得很快。"
    extend "\n不知道是不是慎太郎气场的问题"
    extend "\n和这孩子一起，时间过得飞快啊。"
    "我总觉得，拥有着不可思议魅力的慎太郎，非常的可靠。"
    extend "\n就算他的内心并不是成年人，但只要他能相信我的话，我就很开心了。"
    window hide
    hide cg with dissolve
    show sintarou 17 at top with dissolve
    window show
    sintarou "呜唉~回到家里，澡堂的工作还在等着我啊~。"
    extend "\n今天要干那个，还有打扫澡堂也好麻烦啊~。"
    "慎太郎自言自语道。"
    me "啊，这么说来，刚才和友君聊过天，听说\n慎太郎的家里是开澡堂的。"
    extend "\n真厉害啊~。"
    show sintarou 16 with dissolve
    sintarou "也没什么大不了的啦~毕竟很破旧。\n现在就只有老主顾会来。"
    extend "\n如果方便的话，[player_name]酱也来一趟吧。"
    show sintarou 4 with dissolve
    extend "\n我会好好款待你的哦~。"
    me "款待？是什么样的款待？"
    show sintarou 2 with dissolve
    sintarou "会准备点心之类的啦~。"
    extend "\n这样做客人也会很高兴的啦~。"
    me "是这样啊。"
    extend "\n那，今天就去一趟吧！"
    "都还没分开，就有点恋恋不舍了！"
    extend "\n啊，如果顺利的话，说不定还会给我洗背什么的！！"
    show sintarou 23 with dissolve
    sintarou "啊，今天不行。"
    me "诶？为什么？"
    show sintarou 16 with dissolve
    sintarou "不，不是啦~那个~……"
    show sintarou 29 with dissolve
    extend "总之，今天不行！"
    extend "\n明天来明天来！！要不然就是后天！"
    me "嗯，嗯。知道了。"
    hide sintarou with dissolve
    "这还真是出乎意料啊。到底是为什么呢……？"
    extend "\n和他说的那个是不是有什么关系呢。"
    "我托着下巴思考着，这时正要出厕所的慎太郎回过头。"
    window hide
    play sound "fx/sparkle.ogg"
    show cg c23 at center with Radial(0.5)
    window show
    show sintarou 18 at top with dissolve
    sintarou "[player_name]大哥哥！"
    show sintarou 4 with dissolve
    extend "\n我啊，对小孩外表下的大人技术很感兴趣，\n也想看看大人在小孩的身体中能变的多下流呢♪"
    "说着，他解开衬衫的一颗扣子给我看，\n然后轻快地走出厕所。"
    play sound "fx/running.ogg"
    hide sintarou with dissolve
    hide cg with dissolve
    "这，这……"
    extend "不论如何绝对要让你相信我……！！"
    extend "\n作为正太控一定要努力！！！"
    "我将秘密的决心藏于心中，跟着慎太郎回到了教室。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label day1_layout_sinobu:
    window show
    "难得的自由活动时间，就去逛逛令人怀念的学校吧。"
    me "我出去逛逛。"
    window hide
    show tubasa 5 at top with dissolve
    window show
    tubasa "好的，我明白了。"
    extend "\n四点半之前回来哦。"
    me "知道了知道了。"
    hide bg with dissolve
    hide tubasa with dissolve
    play sound "fx/sliding_door.ogg"
    "我这么对翼说后，离开了教室。"
    window hide
    show bg hallway at center with dissolve
    window show
    "来到走廊上，环视四周。"
    extend "\n其他班级好像也在为御咲祭做准备。"
    "大家都很期待学园祭吧。"
    extend "\n感觉整个学校都团结起来了。"
    window hide
    stop music fadeout 1.0
    play sound "fx/running.ogg"
    show bg schoolyard with dissolve
    play music "tsubame.ogg"
    window show
    "我走出校舍，看向外面。"
    me "那边是体育馆。"
    extend "\n诶？那个旁边的房子……是干什么用的？"
    "那里有一座像小号体育馆一样的建筑。"
    me "唔……不行，想不起来了。"
    extend "\n去看看吧。"
    show bg gym_backside with FadeWhite(0.5)
    "我很在意那栋建筑是什么，走过去看……"
    window hide
    play sound "fx/wind_slash.ogg"
    show cg c31 at center with Radial(0.5)
    play music "sinobu_theme.ogg"
    window show
    sinobu "力道太弱！"
    extend "\n这样接下来的突刺会弱掉的！"
    sinobu "对，让动作更漂亮。\n然后，用力突刺！"
    extend "\n还是不够。再来一次！"
    first_year "是！"
    "那里有忍和一个像一年级的学生。"
    extend "\n从铺着模仿榻榻米的垫子这点来看，这里应该是武道场。"
    sinobu "嗯。\n虽然比刚才要好点了，但还不够。"
    extend "\n我来示范一下，你好好看。"
    first_year "是！"
    show cg remarkable with FadeWhite(0.5)
    play sound "fx/wind_slash.ogg"
    "咻啪！"
    "好快……！"
    "移动重心也不会晃动的身体。"
    extend "\n以最短距离笔直打出的锐利突刺。"
    extend "\n难以想象从这样娇小的肉体中会释放出这样让人震惊的力量。"
    "即使是外行人，也能看出他的实力有多强。"
    me "这样就理解了在厕所时为什么……。"
    window hide
    hide cg with dissolve
    window show
    "我一个人在点头的时候，"
    show tomo 4 at top with dissolve
    tomo "[player_name]君！\n你在干嘛？"
    me "哇！"
    "我回头一看，友正站在那里。"
    show tomo 12 with dissolve
    tomo "嗯？你在看空手道社的自主训练吗？"
    extend "\n因为忍也在吧。"
    extend "\n毕竟一年级的说想要找前辈陪练啊。"
    me "是这样啊。"
    extend "\n居然特地抽空陪学弟练习，真是温柔呢。"
    show tomo 6 with dissolve
    tomo "毕竟忍的空手道在县内可是顶级水平啊~。"
    extend "\n不只是学弟，前辈们也都很追捧他，\n早上和放学后，社团活动之外的空闲时间他也都会去陪他们练习。"
    me "诶~！！"
    extend "\n那他应该很受学弟欢迎吧！"
    show tomo 38 with dissolve
    tomo "没错没错！\n一年级的经常来他教室。"
    extend "\n情人节的时候，他大概收到了有三十盒左右的巧克力！"
    play sound "fx/eureka.ogg"
    me "诶！？？三十盒！？"
    show tomo 25 with dissolve
    tomo "当然是全部都出自男同学手啦！"
    extend "毕竟我们可是男校。"
    play sound "fx/explosion2.ogg"
    "什，什什什什什什什什么！"
    "什么情况！\n现在的御咲学园，男人给男人送巧克力已经真么普遍了吗！？"
    extend "\n太羡慕了……简直就像天堂一样……！"
    show tomo 8 with dissolve
    tomo "[player_name]……口水快滴下来了。"
    me "哈……！"
    extend "\n不是，这真是太厉害了！！"
    "忍也是，还有这所学校也太厉害了吧。"
    show tomo 10 with dissolve
    tomo "还有~！"
    extend "\n忍还经常被高等部的前辈告白。"
    "好，好厉害！！"
    extend "\n这不就像是BL游戏的世界吗！！！"
    extend "\n现在这都成家常便饭了吗！"
    extend "\n我中学的时候可没这些事啊！"
    show tomo 31 with dissolve
    tomo "不过\n忍这么受欢迎我也能理解~。"
    extend "\n乍一看，就长得像个女孩子……"
    show tomo 7 with dissolve
    extend "不过\n其实他本人很在意这个的，所以你还是少说点比较好。"
    me "嗯，嗯嗯！！"
    "确实，他长得这么漂亮……。"
    extend "\n而且还是县内数一数二的武道家，\n被这种反差吸引而为之着迷也是可以理解的。"
    show tomo 11 with dissolve
    play sound "fx/boing.ogg"
    tomo "咦~？"
    extend "\n[player_name]君也是，难道说，\n也喜欢上忍了吗？"
    me "你，你你你你说什么呢……！"
    show tomo 24 with dissolve
    tomo "没有没有~我们学校，\n以前就是有很多这样的，\n不用害羞的！"
    me "诶，什么意思……？"
    show tomo 38 with dissolve
    tomo "就是有很多同志！"
    play sound "fx/cute2.ogg"
    "什，什么啊啊啊啊啊啊啊！！！！"
    me "这，这怎么可能啊！！"
    extend "\n我完全不知道有这回事啊！"
    show tomo 27 with dissolve
    tomo "那是……"
    extend "\n只是偶然和[player_name]你没有缘吧？"
    play sound "fx/shock.ogg"
    "冲击！！！"
    me "怎……么能……。"
    extend "\n我想变……回初中生……。"
    show tomo 26 with dissolve
    tomo "[player_name]君啊，别灰心。"
    extend "\n我们现在正是初中生活最精彩的部分。"
    window hide
    hide tomo with dissolve
    show sinobu 23 at topright with Dissolve(0.8)
    window show
    sinobu "……你们从刚才开始就在说什么啊？"
    "我向声音传来的武道场看去，不知何时忍已经来到了我的身边。"
    extend "\n他汗流浃背，微微喘气的样子显得格外性感。"
    show tomo 17 at topleft with dissolve
    tomo "哦！忍~练习辛苦了！！"
    me "……你，你好！忍。"
    extend "\n已经结束练习了吗？"
    show sinobu 2 with dissolve
    sinobu "嗯。"
    extend "\n友和[player_surname]君怎么会在这里？"
    me "因为是自由活动时间，所以我们出来散散步。"
    show tomo 10 with dissolve
    tomo "我也差不多~。"
    me "不过话说回来，忍！\n你真的很帅啊！！"
    extend "\n我从没见过你那样的动作！"
    hide tomo with dissolve
    hide sinobu with dissolve
    show sinobu 22 at top with dissolve
    sinobu "……谢谢。"
    extend "\n但我还有很多不足之处啊。"
    me "别谦虚了~。"
    extend "\n我也有学过一点武术，\n但完全敌不过你啊。"
    show sinobu 12 with dissolve
    sinobu "这样啊。"
    extend "\n既然如此，下次我们就一起练习吧。"
    me "好！那就拜托你了。"
    hide sinobu with dissolve
    show sinobu 12 at topright
    show tomo 6 at topleft with dissolve
    tomo "通过武术加深感情……不错啊~。"
    hide tomo with dissolve
    hide sinobu with dissolve
    play sound "fx/vibrate.ogg"
    "嗡嗡嗡嗡"
    "就在这时，友的手机响了。"
    stop sound fadeout 1.0
    tomo "喂，你好~慎酱？"
    extend "\n啊，抱歉抱歉！我马上回去了！"
    "哔"
    show tomo 40 at top with dissolve
    tomo "慎酱叫我马上回去。"
    show tomo 1 with dissolve
    extend "\n那么，我就先一步回教室了。"
    extend "\n待会儿见！"
    play sound "fx/running.ogg"
    hide tomo with dissolve
    "这么说完，友便跑向了我们来时的方向。"
    window hide
    show sinobu 4 at top with dissolve
    window show
    sinobu "……所以，你们刚才在聊什么？"
    me "嗯，那个~是关于忍你很受欢迎的事……。"
    show sinobu 10 with dissolve
    sinobu "……是吗。"
    extend "\n真是的，友真是个大嘴巴啊。"
    me "啊哈哈哈。"
    extend "\n我是不是不应该去听啊……？"
    show sinobu 4 with dissolve
    sinobu "也没什么啦。毕竟也是实话。"
    extend "\n而且能受到欢迎也是件值得高兴的事。"
    show sinobu 20 with dissolve
    sinobu "……那个啊，[player_surname]君。"
    extend "\n说实话，我是想早点结束小组讨论的，\n因为刚才那个后辈在等我。"
    extend "\n……抱歉，擅自把时间按我的需要安排。"
    me "诶，没事！完全没问题的。"
    extend "\n我知道忍很重视后辈的事。"
    extend "\n而且，我们已经把能商量的事都商量完了，所以不用担心。\n不用在意的。"
    show sinobu 27 with dissolve
    sinobu "……嗯，谢谢。"
    extend "\n从明天开始，为了不给你们添麻烦，放学后的训练我就不去了。"
    "忍这么说着，他刚才在教室里表现出的冷淡的态度完全消失，\n取而代之的是感到抱歉的消沉情绪。"
    play sound "fx/sparkle.ogg"
    "这……从某种意义上，也是反差萌！"
    show sinobu 12 with dissolve
    sinobu "那么，差不多该回去了。不能迟到。"
    me "啊，啊啊，是啊！"
    hide sinobu with dissolve
    "我一边注意着别被他发现我的想法，\n一边和忍一起回到了教室。"
    stop music fadeout 0.5
    window hide
    hide sinobu with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    return

label day1_layout_tubasa:
    stop music fadeout 1.0
    window show
    "对对！"
    extend "\n我要留在教室里，想问这孩子一些事呢~♪"
    play music "tubasa_theme.ogg"
    me "翼同学！"
    window hide
    show cg c39 2 at center with dissolve
    window show
    tubasa "嗯，嗯。"
    hide bg with dissolve
    extend "\n什么事？"
    me "你从刚才开始就一直心神不宁的，\n是有什么在意的事吗？"
    show cg c39 1 with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tubasa "诶？"
    extend "\n那个，没，没没没没什么！！"
    "呼呼，真是个好懂的孩子啊！"
    extend "\n大概，这孩子很在意和自己一起站在讲台的森海友吧。"
    play sound "fx/sparkle.ogg"
    extend "\n这就是现实中的BL！！！美妙的青春啊！！"
    play sound "fx/eureka.ogg"
    "好！！\n作为御咲学园的毕业生，为了后辈也得帮一把！！"
    extend "\n毕竟，这可是近距离观看少年们的恋爱故事的好机会♪"
    me "喂喂，难得的自由活动时间，\n要不要去散个步？"
    tubasa "诶……但，但是我……"
    "翼再次看向了友。"
    "原来如此……是因为在意他到一刻都离不开他啊！！！"
    show bg classroom at center
    "既然如此……我就把嘴贴到了翼的耳边"
    window hide
    hide cg with dissolve
    window show
    me "翼同学……你喜欢森海友同学对吧？"
    show tubasa 18 at top with dissolve
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    tubasa "什！什什什什！？！？！？"
    extend "\n[player_name]君！？！"
    me "关于那个，我有话要对你说~"
    extend "\n喂！你愿意和我一起去吗？"
    window hide
    hide tubasa with dissolve
    hide bg with dissolve
    play sound "fx/sliding_door.ogg"
    show bg hallway at center with dissolve
    window show
    "翼无从抵抗，只能跟在我后面。"
    "眼前，可爱的少年陷入爱情的困扰。"
    extend "\n这怎么能不插一脚呢！不，是一定得插一脚！！"
    window hide
    stop music fadeout 0.5
    play sound "fx/running.ogg"
    hide bg with dissolve
    show bg stairs at center with dissolve
    play music "discovery.ogg"
    window show
    me "好……就在这附近吧？"
    show tubasa 20 at top with dissolve
    tubasa "那，那个……刚才你说的到底...！！"
    me "不是啦~我只是看着你们俩，就隐约这么觉得了。"
    show tubasa 3 with dissolve
    play sound "fx/shock.ogg"
    tubasa "不是吧……你怎么会发现的……。"
    show tubasa 18 with dissolve
    extend "\n啊！！不，不是的！！"
    extend "\n因，因为都是男生，所以绝对不会有那种事情……！！\n对吧？你看……诶，内个！"
    me "哼哼。\n就算都是男生，和能否恋爱也没有关系。"
    extend "\n倒不如说，最近国内的同性恋者似乎增加了。"
    show tubasa 3 with dissolve
    tubasa "我，我并不是！\n同，同性恋什么的……！"
    extend "\n那，那那那那那那！！"
    me "原~来如此。"
    extend "\n也就是说，你和森海友君无关性别，\n而是喜欢上了他本人吧。"
    play sound "fx/cute3.ogg"
    "噗！！"
    "翼的脸就像着了火一样红。"
    show tubasa 33 with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.065), layer='master')
    play sound "fx/boing.ogg"
    tubasa "阿哇，阿哇哇哇哇哇……！"
    me "契机是什么呢？"
    extend "\n什么时候开始喜欢上的呢？"
    show tubasa 7 with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.065), layer='master')
    play sound "fx/boing.ogg"
    tubasa "契，契契契契契机……？！\n从，从从从什么时候开始的！？\n喜……喜欢……！？"
    "翼，像个坏掉的人偶一样，不断地重复着这句话。"
    me "所以呢所以呢！"
    extend "\n翼君你，想传达自己的心意吗？"
    show tubasa 33 with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.065), layer='master')
    play sound "fx/boing.ogg"
    tubasa "心意……！？！？"
    extend "\n心心心心心……！传传传传传……？！"
    "他慌慌张张的样子实在是太可爱了，我不禁捉弄了他一下。"
    me "啊哈哈哈抱歉抱歉。"
    extend "\n好像稍微捉弄过头了。"
    show tubasa 9 with dissolve
    tubasa "哈啊哈啊哈啊……捉弄……唔……？"
    stop music fadeout 1.0
    me "话题跳得太快了对吧？"
    extend "\n翼的反应实在是太有趣了，所以，一不小心就"
    play music "tubasa_theme.ogg"
    show tubasa 3 with dissolve
    tubasa "呜，呜呜呜呜……好过分，[player_name]君……。"
    me "抱歉啦！"
    extend "\n总之你放心吧。\n我会把这件事保密的。"
    "……话虽如此，看翼这个样子，估计已经有不少人注意到了。"
    show tubasa 20 with dissolve
    tubasa "秘，秘密什么的，我还没……\n承认我喜欢友君呢……。"
    me "呼~。\n那就算友君跟其他人交往了你也无所谓呀~。"
    extend "\n啊！说不定我开始喜欢上友君了！\n等下就去告白吧~！"
    show tubasa 7 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tubasa "哇啊啊啊啊！！\n不行不行！！绝对不行！！！"
    me "啊哈哈哈！"
    extend "\n瞧，你明明都有这种反应了，\n难道不打算承认自己喜欢他吗？"
    show tubasa 19 with dissolve
    tubasa "呜，呜呜……这……。"
    me "如果没有特别的感情，应该不会有这种反应吧？"
    show tubasa 1 with dissolve
    tubasa "呜呜……可是，就算喜欢……"
    extend "\n我这种又土又胆小又笨的人，\n根本不可能受到对方的青睐……肯定也不会进展顺利……。"
    me "哦，真是从一开始就特别消极啊。"
    extend "\n翼同学，我打算帮助你们。"
    show tubasa 23 with dissolve
    tubasa "帮助……？"
    me "啊！也就是所谓的爱情的丘比特！"
    extend "\n为了让你的心意传达给友，我会帮助你的！"
    show tubasa 8 with dissolve
    tubasa "爱，爱情……！？"
    extend "\n啾啾啾啾啾啾啾啾，丘比特~？"
    me "怎么样？"
    extend "\n作为一个男人，要努力一下吗？"
    show tubasa 7 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tubasa "不，不行不行不行。"
    extend "\n这种事我做不到！"
    me "比想象中还要消极啊……"
    extend "\n既然这么喜欢友，\n那就更加积极一点啊。"
    show tubasa 30 with dissolve
    tubasa "因为……因为……。\n我……就算维持现状也无所谓啊。"
    extend "\n即便不能结合，只要能作为要好的朋友，我就……"
    me "可是翼。"
    extend "\n照这样发展下去，就像我刚刚说的，\n友说不定有一天会和别人交往的。"
    extend "\n翼，到时候你能作为朋友为他送上祝福吗？"
    show tubasa 3 with dissolve
    tubasa "那，那样我做不到啊……"
    extend "\n我绝对不允许友和其他人交往什么的……。"
    me "对吧？"
    extend "\n我也没说马上就要告白啊。"
    extend "\n所以，才要慢慢的做好准备，\n好让翼君能将自己的心意传达给友君。"
    show tubasa 23 with dissolve
    tubasa "传达心意的准备…。"
    me "平时不做好准备，\n等友君被别人抢走的时候，可就没法抵抗了。"
    show tubasa 6 with dissolve
    tubasa "呜呜……也，也是啊…。"
    me "我只不过是想协助你而已。"
    extend "\n与其独自烦恼，还不如找其他人商量，这样心情也会轻松一些，\n而且我认为这么做也会朝着更好的方向发展。"
    show tubasa 32 with dissolve
    tubasa "……确，确实是这样……\n[player_name]君，感觉被你彻底看透了……"
    extend "\n哈啊……为什么会被发现啊……"
    me "因为~翼同学\n你就像把心事写在脸上一样，非常好懂啊……。"
    show tubasa 17 with dissolve
    play sound "fx/cute2.ogg"
    tubasa "诶！！这，这样吗！？"
    me "嗯。真的。"
    show cg dark at center
    show tubasa 7 with dissolve
    play sound "fx/shock.ogg"
    tubasa "（失落）"
    show tubasa 8 with dissolve
    tubasa "那，那么说来……难道说……\n我的心情可能被友君给发现……。"
    me "嗯~……也不是没有这种可能……。"
    hide cg with dissolve
    show tubasa 9 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tubasa "呜，骗人的吧……！该，该怎么办啊……"
    extend "\n这样下去的话，会被友君讨厌的啊啊啊！！"
    me "没事没事！\n就算被发现了，你肯定也不会被讨厌的！"
    extend "\n而且，我也在你身边！\n从现在开始，不管是御咲祭的准备，还是对友君的恋情，都一起努力吧！"
    show tubasa 3 with dissolve
    tubasa "好，好的……我会加油的……！"
    "很好……总算是圆满收场了。"
    extend "\n接下来，不知道会看到什么样子的恋爱发展呢……。"
    extend "\n咕呵呵呵呵"
    window hide
    hide tubasa with dissolve
    pause 0.3
    stop music fadeout 0.3
    window show
    sakuya "好恶心。"
    play sound "fx/dash.ogg"
    $ renpy.transition(Quake(50, 100, 0.1, 0.065), layer='master')
    "咂"
    "呜……就算你不说出来也……"
    extend "\n诶，啥？"
    window hide
    play music "sakuya_theme.ogg"
    show tubasa 21 at topright with dissolve
    window show
    tubasa "作，作哉君……？"
    show sakuya 6 at topleft with dissolve
    sakuya "你从刚才开始就在说恋爱啊丘比特什么的，到底是怎么回事？"
    extend "\n那些和你们这种边缘人无缘吧。"
    me "难道说……刚才的话你全都听见了……？"
    show sakuya 9 with dissolve
    sakuya "我才没听。根本不感兴趣。"
    hide tubasa with dissolve
    hide sakuya with dissolve
    show sakuya 6 at top with dissolve
    extend "\n喂，你这家伙。"
    "作哉靠近我，小声对我说道。"
    window hide
    show cg c40 at center with FadeWhite(0.5)
    window show
    hide sakuya with dissolve
    sakuya "你可别做多余的事。"
    extend "\n要是你太嚣张了我可不饶你。\n知道了吧？"
    window hide
    play sound "fx/running.ogg"
    hide cg with Dissolve(1.0)
    stop music fadeout 1.4
    window show
    "留下这句话，作哉回到了教室。"
    play music "tubasa_theme.ogg"
    show tubasa 21 at top with dissolve
    tubasa "[player_name]嗯……他对你说了些什么……？"
    me "没事，没什么大不了的。"
    extend "\n话说回来，翼同学也很不容易呢……。"
    show tubasa 22 with dissolve
    tubasa "什么……？"
    "但是，少年之间的复杂恋爱关系……"
    play sound "fx/explosion2.ogg"
    extend "\n这真是让我感到无比萌啊……！！"
    extend "\n谢谢你，御咲学园！！同时，也谢谢你，梦想世界！！"
    me "好……不管会遇到什么困难，"
    play sound "fx/cute2.ogg"
    extend "\n都要克服，一定要抵达幸福的结局！！"
    show tubasa 19 with dissolve
    tubasa "……？？！\n你在说些什么啊！？"
    extend "\n我完全跟不上……。"
    me "别管那么多！！"
    extend "\n话也说完了，是时候回教室了！"
    extend "\n作为执行委员，迟到可不好！"
    show tubasa 2 with dissolve
    tubasa "哎……啊，好的……。"
    "翼还跟不上这突如其来的转折，好像还有些摸不着头脑，\n我们强行结束了话题，回到了教室。"
    window hide
    hide tubasa with dissolve
    stop music fadeout 0.5
    hide bg with Dissolve(0.8)
    return

label day1_cooking_tuki:
    show bg infirmary at center
    window show
    me "那，那么，月君！"
    extend "\n不好意思，你能留下来吗？"
    window hide
    show tuki 18 at topleft with dissolve
    window show
    tuki "嗯，我知道了。"
    extend "\n居然说些像是小孩子一样的话，真是拿你没办法啊。"
    "月像是要戏弄我似的微笑着。"
    extend "\n居然被比我小十岁的人这么说……。"
    me "呜……啊，啊哈哈……。"
    show sora 2 at topright with dissolve
    sora "那么，我就先回教室了。"
    extend "\n[player_name]君，保重啊！"
    show tuki 9 with dissolve
    tuki "料理组的工作，就拜托你了。"
    show sora 10 with dissolve
    sora "嗯，我会尽我所能的。"
    play sound "fx/sliding_door.ogg"
    hide sora with dissolve
    "空这么说完，就从保健室里出去了。"
    window hide
    hide tuki with dissolve
    window show
    doctor "哎呀，让大哥哥来陪在身边啊。"
    show tuki 4 at top with dissolve
    tuki "是的，因为[player_surname]说寂寞什么的。"
    me "呜咕……。"
    hide tuki with dissolve
    "虽然我很拼命地劝他们不要离开，\n但被这么一说，还是不由得脸红了起来。"
    extend "\n真是丢脸的成年人……。"
    "我不由得把头埋进了被子里。"
    doctor "哎呀呀，[player_surname]君也还只是个小孩子呢。"
    me "啊，啊哈哈……。"
    teacher "不过，这样我就放心了。"
    extend "\n老师有点事要去办公室一趟，\n赤峰同学你能帮我看一会儿吗？"
    show tuki 15 at top with dissolve
    tuki "好的，我知道了。"
    teacher "谢谢。"
    extend "\n那我就先走一步了。"
    play sound "fx/sliding_door.ogg"
    "就这样，连保健老师也离开了，\n保健室里，就剩我和月两个人了。"
    window hide
    hide tuki with dissolve
    window show
    me "对不起啊……月君，我这么任性。"
    show tuki 9 at top with dissolve
    tuki "没关系的。"
    extend "\n空感冒的时候也说过同样的话，\n你变成这样，也一定是没办法的事情吧。"
    me "嗯……我突然就觉得很寂寞啊。"
    "与其说具体的人，不如说，我是思恋这种少年感。"
    hide tuki with dissolve
    "然后，月把椅子拉到了床边，把手伸了过来。"
    window hide
    stop music fadeout 0.5
    play music "cute_silly.ogg"
    show cg c58 at center with zoominout
    play sound "fx/boing.ogg"
    window show
    me "……月，月君。"
    extend "\n你在做什么呢？"
    "月把手放到了我的头上，就像哄小孩一样摸着我。"
    tuki "空感冒的时候，说这样做能让他平静下来。"
    extend "\n……你不喜欢吗？"
    "虽然我不讨厌，但被小孩摸头，总觉得有点难为情。"
    extend "\n但是，他的手却十分轻柔，还带着能让人安心的温暖，\n让我感到有些不可思议。"
    me "不，不是……没有那种事。"
    "我暂时沉浸在了这种舒适感里。"
    tuki "……还有，其它想要我做的事情吗？"
    extend "\n只要是我力所能及的，无论什么都可以。\n不用客气，尽管说。"
    me "没，没事的。"
    extend "\n我又不是感冒了，不用这么顾虑我的。"
    tuki "你在说什么呢。"
    extend "\n像这样小看这些琐碎小事的话，\n是会把事情闹大的，反而会延长病情的哦。"
    me "那是当然，但是…。"
    tuki "这种时候，就放下你的执念，坦率地向我撒娇吧。"
    extend "\n这样做，对你来说也会很轻松的。"
    "这孩子，真是成熟……。"
    extend "\n与年龄差距无关，让人不禁想要向他撒娇。"
    me "……那么，除了摸摸我的头以外，"
    extend "\n能不能……和我睡在一起？"
    "不由得，就吐露出了真心话。"
    window hide
    hide tuki with dissolve
    hide cg with dissolve
    show tuki 5 at top with dissolve
    window show
    tuki "和我睡一个被窝吗？"
    extend "\n但是，要是我进去的话就会很挤了，而且也会很热吧。"
    me "就是说这样才好！\n你想啊，生病的时候会觉得心里不安嘛，所以～。"
    extend "\n这样做就能让我更加安心……"
    "连我自己都感到心口一痛……。"
    extend "\n不过，这孩子的话一定……。"
    show tuki 9 with dissolve
    tuki "既然你都这么说了，那就没办法了。"
    extend "\n那你能稍微靠边一些吗？"
    me "谢谢你！"
    extend "\n来来！ 请进！！"
    hide tuki with dissolve
    "我退到一边，月爬上了床，躺到我旁边。"
    extend "\n这次他把手放到我的背上，\n开始有节奏地轻拍我的背。"
    window hide
    show cg c59 at top with Radial(1.0)
    window show
    tuki "怎么样？这样冷静下来了吗？"
    me "嗯……谢谢你。\n真感觉很安心。"
    extend "\n真想一直这样下去啊~。"
    tuki "哈哈哈。"
    extend "\n一直这样下去的话，永远也没法恢复健康哦？"
    "……实际上，我现在并不是身体不舒服的状态，真的想一直这样下去。"
    "话说回来……虽然很顺利地就发展成了这样，\n可这是不是也太夸张了！！！？？"
    extend "\n在我这个正太控的旁边，一个中学二年级的男生，正和我躺在一起。"
    extend "\n做梦都没想到会遇到的场景，现在却变成了现实（？）！！！"
    play sound "fx/heartbeat.ogg"
    "我心跳得越来越快。"
    play sound "fx/sparkle.ogg"
    show cg adult with Dissolve(0.8)
    "啊……真想把脸埋在他年轻健壮的胸肌里……。"
    extend "\n想要强抱他……不，应该说想要被他强抱！！"
    extend "\n能够被这样的帅哥抱，就算是男人也会觉得幸福吧……。"
    stop music fadeout 0.5
    hide cg with Dissolve(0.8)
    hide bg with Dissolve(0.8)
    hide tuki with Dissolve(0.8)
    extend "\n如果我现在冲进他的怀里，他会有什么反应呢？"
    window hide
    play music "hurry_up.ogg"
    show bg infirmary at center with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.06), layer='master')
    play sound "fx/cute2.ogg"
    window show
    "我飞扑了过去。"
    tuki "！"
    extend "\n[player_surname]……？"
    "我的身体不受控制地动了起来。"
    me "抱歉，月君。"
    extend "\n我，忍不住……。"
    tuki "……真是拿你没办法啊。"
    extend "\n对啊，是我让你随心所欲的。"
    extend "\n那就随你所愿吧。"
    show cg adult at center with dissolve
    "月把手绕过我的背，紧紧地拥抱着我。"
    extend "\n我把脸埋进那结实的身体里，用全身感受着月。"
    play sound "fx/explosion3.ogg"
    "那一刻，我的开关完全打开了。"
    "无论是梦境还是现实，都可以！！  无论变成什么样都可以！！"
    extend "\n我都要做我想做的事！！！"
    show cg remarkable with FadeWhite(0.3)
    play sound "fx/fall_down.ogg"
    "啪嚓"
    "我变成扑在月身上的姿势。"
    tuki "[player_surname]……？"
    "这种机会，只有现在才有！！"
    extend "\n好，在这个真实的梦里面，得好好发泄一下平时的欲求不满才行……！"
    me "果然比起被人抱，我还是想抱别人……！！"
    extend "\n美味的少年啊……"
    play sound "fx/eureka.ogg"
    extend "我开动了！！"
    stop music fadeout 0.5
    hide bg with Dissolve(0.2)
    hide cg with Dissolve(0.2)
    play sound "fx/wind_slash.ogg"
    "啪"
    window hide
    play music "fx/tsubame.ogg"
    show bg infirmary at center with DefocusWhite(1.4)
    show tuki 1 at top with dissolve
    window show
    tuki "嗯，你醒了吗？"
    extend "\n感觉怎么样？身体有好转吗？"
    "我看了看旁边，月坐在床边的椅子上。"
    show tuki 8 with dissolve
    tuki "你看起来睡得很舒服呢。"
    extend "\n不过醒得那么突然，是不是做了什么可怕的梦？"
    me "咦……？"
    extend "\n我，刚才还……咦？"
    extend "\n我和月君不是一起躺在床上……。"
    show tuki 22 with dissolve
    tuki "你在说什么呢。"
    extend "\n我怎么可能抢病人的床。"
    me "诶……啊……啊！？！？"
    stop music fadeout 0.5
    play sound "fx/shock_big.ogg"
    play music "emergency.ogg"
    show cg dark at center with Dissolve(0.2)
    "呃，刚才那个是做梦吗！！！！！！！！！"
    "居然在梦中又做了梦，我真是……。"
    extend "\n真是的，这个梦到底要让我折腾到什么地步才肯罢休啊……。"
    window hide
    hide tuki with dissolve
    hide cg with dissolve
    show tuki 15 at top with dissolve
    window show
    tuki "看起来身体已经好了不少，太好了。"
    extend "\n医生也回来了，时间也差不多了，\n我先回教室了，[player_surname]你呢？"
    me "呜……我，我也回去……。"
    "既然是梦……刚才正到关键……\n就让我再稍微多做一会儿美梦啊啊啊……！！！！"
    extend "\n呜呜……。"
    hide tuki with dissolve
    "就这样，我的欲望落空，我们回到了教室。"
    window hide
    stop music fadeout 0.5
    hide bg with Dissolve(0.9)
    return

label day1_supply_sakuya:
    window show
    "去教学楼后面吧！"
    "但是，到底为什么会去那种地方呢？"
    extend "\n说到校后……"
    extend "嗯……。"
    "告白……？"
    "不对不对，那样友君也知道的话就很奇怪了。"
    extend "\n说起来，他好像说「卿卿我我」什么的……。"
    show cg adult at center with FadeWhite(0.5)
    play sound "fx/wow2.ogg"
    "难，难道说，是告白之后的事！？！？"
    extend "\n不对，那就不该是校后，而是在体育馆仓库吧！！"
    extend "\n话说回来，御咲学园是男子学校，居然也有这种事！？！？？"
    "我怀着各种各样的臆测，向着校后走去。"
    stop music fadeout 2.0
    window hide
    hide bg with dissolve
    hide cg with dissolve
    play music "fx/tsubame.ogg"
    show bg schoolyard at center with Radial(0.7)
    window show
    me "说是校后，学校这么大……到底在哪呢……"
    show bg gym_backside with dissolve
    "我刚转过教学楼的拐角，就听到了声音。"
    window hide
    window show
    play sound "fx/explosion2.ogg"
    $ renpy.transition(Quake(0, 60, 0.15, 0.1), layer='master')
    sakuya "小翼！我喜欢你啊啊啊！！！"
    me "！？！？"
    "刚，刚才的声音……是作哉君！！"
    extend "\n「喜欢你」……果然还是告白了啊！！？！？"
    play sound "fx/boing.ogg"
    extend "\n而且，还是那位一之濑翼同学！？？！"
    "我怀着激动的心情，悄悄地看过去。"
    window hide
    show bg school_backside with dissolve
    window show
    me "嗯，啊……一个人……？"
    extend "\n作哉君只是蹲在那……。"
    "难道说，是在练习告白？正当我这么想着的时候，\n"
    stop music fadeout 0.5
    show cg remarkable at center with FadeWhite(0.5)
    play sound "fx/wind_slash.ogg"
    "作哉怀里突然飞出什么！"
    unknown "汪！汪汪！！"
    sakuya "啊，喂小翼！"
    extend "\n你要去哪啊！！"
    window hide
    play music "emergency.ogg"
    show cg c75 with zoominout
    window show
    play sound "fx/boing.ogg"
    "是狗！！"
    extend "\n为什么在这里？"
    "就在我思索的时候，那只狗冲着我跑来。"
    me "呜，呜哇！等，等等！！"
    window hide
    hide cg with dissolve
    $ renpy.transition(Quake(0, 60, 0.15, 0.1), layer='master')
    play sound "fx/fall_down.ogg"
    window show
    "我下意识地坐倒在地。"
    extend "\n而狗则无视了我，径直地舔舐我的脸。"
    play sound "fx/running.ogg"
    show sakuya 17 at top with dissolve
    sakuya "诶，[player_surname]！！你怎么会在这里！！？"
    me "作，作哉！"
    extend "\n这狗狗……快，快想想办法啊~…。"
    "我的脸被口水所浸湿，向作哉请求道。"
    show sakuya 26 with dissolve
    sakuya "啊……"
    extend "喂，小翼！快离开这个人。"
    "作哉这么说着，"
    stop music fadeout 1.0
    "小翼就老实地听从了他，离开了我的身边。"
    window hide
    play music "sakuya_theme.ogg"
    show cg c76 at center with Radial(0.5)
    window show
    sakuya "乖孩子……真乖真乖~。"
    "作哉抚摸着狗狗的头，温柔地抱了上去。"
    me "作哉君……这只狗到底是怎么回事？"
    sakuya "最近，经常能看到它出现在学校里。"
    extend "\n因为它很亲近人，忍不住觉得很可爱，就照顾它一下。"
    extend "\n对吧？小翼。"
    "作哉露出了和平时的他无法想象的温柔表情，抚摸着小翼的头。"
    me "原来作哉君喜欢狗啊。"
    extend "\n刚才我还以为你喊「翼我喜欢你！」之类的\n结果居然是「好喜欢狗啊！」，吓我一跳。"
    extend "\n我还以为作哉君要向翼告白呢。"
    hide cg with dissolve
    hide sakuya with dissolve
    show tsubasa 3 at topright
    show sakuya 2 at topleft with dissolve
    play sound "fx/boing.ogg"
    sakuya "什……！！！ 你，你傻吗！！！\n谁会喜欢那种懦弱无力的家伙啊！！"
    extend "\n开什么玩笑啊！"
    "作哉这么说着，表情又变回了平时傲娇的样子。"
    me "抱，抱歉抱歉！"
    extend "\n没想到你在和狗狗说话……。"
    show sakuya 12 with dissolve
    sakuya "什，什么啊……和狗狗说话也不行吗？"
    me "不是那样的。"
    extend "\n就是~觉得很可爱。"
    hide sakuya with dissolve
    hide tsubasa with dissolve
    $ renpy.transition(Quake(0, 80, 0.15, 0.1), layer='master')
    play sound "fx/punch3.ogg"
    "啪！！！"
    show sakuya 27 at top with dissolve
    sakuya "吵，吵死了！！！信不信我揍你！！！"
    me "已，已经揍了……。"
    hide sakuya with dissolve
    show sakuya 27 at topleft
    show tsubasa 5 at topright with dissolve
    tubasa "咕……\n（舔舔）"
    show sakuya 28 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sakuya "啊，对不起，翼。吓到你了吗？"
    extend "\n我不是对翼说的。\n只是对这个笨蛋说的，不用害怕。"
    play sound "fx/triangle.ogg"
    "然后，这个差别。"
    extend "\n对狗温柔，对人严厉……这种类型我还是第一次听说。"
    extend "\n傲犬？"
    extend "不对，是犬娇？"
    me "我刚刚就在想\n那只小狗，叫「翼」是吗？"
    extend "\n难道说是作哉给起的吗？"
    show sakuya 17 with dissolve
    sakuya "哈，哈啊？？不是！！当然不是啊！\n谁会喜欢和那个白痴一之濑起一样的名字啊。"
    extend "\n原本就有名字的，原本就有！"
    hide sakuya with dissolve
    hide tsubasa with dissolve
    show sakuya 2 at top with dissolve
    play sound "fx/dash.ogg"
    extend "\n真是……开什么玩笑！！！"
    hide sakuya with dissolve
    show sakuya 2 at topleft
    show tsubasa 6 at topright with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tsubasa "嗯～！"
    show sakuya 28 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sakuya "啊，啊哈。不是啦～。"
    extend "\n不是说小翼，我只是在说那个大笨蛋蠢货啦。"
    me "但是，那只小狗是野狗吧？\n你是怎么知道它原来的名字？"
    show sakuya 29 with dissolve
    sakuya "少，少啰嗦！！！这很重要吗！！！"
    hide sakuya with dissolve
    hide tsubasa with dissolve
    play sound "fx/wind_slash.ogg"
    show sakuya 27 at top with dissolve
    extend "\n赶紧给我滚！！\n不然的话，我可要再揍你一顿哦！！！"
    hide sakuya with dissolve
    show sakuya 27 at topleft
    show tsubasa 5 at topright with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tsubasa "嗯！"
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    extend "汪汪～！"
    show sakuya 28 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sakuya "不是啦~不是啦~。\n我完全没有生气啊~！"
    extend "\n所以，你就放心吧~！好吗~♪"
    hide sakuya with dissolve
    hide tsubasa with dissolve
    play sound "fx/triangle.ogg"
    "这是完全被驯化了啊……。"
    window hide
    window show
    me "翼酱……是吗？"
    extend "\n虽然说是野狗，但那小东西毛色很好，\n而且，连项圈都戴上了，"
    extend "\n全部都是作哉君做的吗？"
    show sakuya 19 at top with dissolve
    sakuya "是啊……有意见吗？"
    me "没有没有……只是觉得好厉害。简直就像真的狗主人一样。"
    extend "\n小翼能得到如此温柔的主人，真是太幸福了。"
    hide sakuya with dissolve
    show tsubasa 2 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tsubasa "汪！"
    me "哈哈，好厉害！\n居然会好好回答。"
    hide sakuya with dissolve
    hide tsubasa with dissolve
    show tsubasa 3 at topright
    show sakuya 25 at topleft with dissolve
    sakuya "那当然。"
    extend "\n不要小看小翼。"
    "说完，作哉把小翼放到了地上。"
    hide sakuya with dissolve
    hide tsubasa with dissolve
    sakuya "小翼，坐下！"
    show tsubasa 1 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/eureka.ogg"
    tsubasa "（啪叽）"
    "按照作哉说的，小翼摆出了坐下的姿势。"
    sakuya "握手。"
    show tsubasa 2 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tsubasa "（啪叽）"
    sakuya "再来一个。"
    show tsubasa 3 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    tsubasa "（啪叽）"
    sakuya "亲亲！"
    show tsubasa 4 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/wind_slash.ogg"
    tsubasa "（亲）"
    sakuya "转圈！"
    show tsubasa 2 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tsubasa "（转圈）"
    hide tsubasa with dissolve
    show sakuya 21 at top with dissolve
    sakuya "差不多就这样。"
    me "好，好厉害……居然全部都会听从指示。"
    show sakuya 24 with dissolve
    sakuya "那当然。小翼很聪明啊！"
    extend "\n对了，给你奖励。"
    hide sakuya with dissolve
    "作哉从口袋里拿出狗食似的东西，\n放到了小翼的头上。"
    show sakuya 6 at topleft
    show tsubasa 3 at topright with dissolve
    sakuya "小翼，待着。"
    play sound "fx/footsteps.ogg"
    "听到这么说，它就像石化了一样纹丝不动。"
    sakuya "……。"
    me "……。"
    tsubasa "…。"
    sakuya "……"
    stop sound fadeout 0.5
    show sakuya 24 with dissolve
    extend "好了！"
    show tsubasa 2 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    "在我说完的同时，他突然动了下头\n然后完美地接住了从天而降的饵食，并将其送入口中。"
    "我不禁为它的精彩表现鼓起了掌。"
    hide tsubasa with dissolve
    hide sakuya with dissolve
    me "太，太棒了！！"
    extend "\n没想到居然这么听话！"
    show sakuya 21 at top with dissolve
    sakuya "哼哼。\n我已经习惯照顾狗狗了啊。"
    me "意思是，你家也养了狗？"
    show sakuya 5 with dissolve
    sakuya "虽然现在已经没有了，但我以前养过。"
    extend "\n那时候，我学到了不少照顾狗狗的方法。"
    me "诶~厉害啊。"
    extend "\n一般来说，这种事都是交给父母的，\n没想到你居然一直自己来照顾。"
    show sakuya 7 with dissolve
    sakuya "也没什么啦……只是因为喜欢而已。"
    "作哉害羞地说道。"
    extend "\n和平时的他形成鲜明的对比，我的心跳加快了起来。"
    hide sakuya with dissolve
    show sakuya 7 at topleft
    show tsubasa 3 at topright with dissolve
    me "我说，我可以摸摸它吗？"
    show sakuya 21 with dissolve
    sakuya "可以。"
    extend "\n放心吧，它绝对不会闹腾或者咬你。"
    me "谢谢。那……"
    "抚摸抚摸"
    "我轻轻地抚摸作哉的头发。"
    hide sakuya with dissolve
    hide tsubasa with dissolve
    show sakuya 29 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sakuya "！！？"
    me "哇啊~果然很顺滑。好棒啊。"
    show sakuya 27 with dissolve
    sakuya "……你傻吗！！！"
    play sound "fx/dash.ogg"
    "啪！！"
    "作哉无情地甩开了我的手。"
    me "咦……你不是说不会打人或咬人吗…。"
    show sakuya 8 with dissolve
    sakuya "怎么想都是说小翼吧！"
    extend "\n居然像猫山一样做这种无聊的事！！！"
    me "啊哈哈。对不起对不起。\n开玩笑的啦……。"
    "这次我成功地把手放在了小翼身上。温柔的抚摸着"
    hide sakuya with dissolve
    show tsubasa 3 at topright with dissolve
    play sound "fx/sparkle.ogg"
    me "哦哦~！我摸到了！！！"
    extend "\n我，我以前从来没摸过动物，\n好感动啊！！！"
    show sakuya 23 at topleft with dissolve
    sakuya "什么嘛……你对人做这种胡闹的事，对动物倒这么纯洁啊。"
    extend "\n因为小翼是个好孩子，所以会允许像你一样的家伙摸他的。"
    show sakuya 14 with dissolve
    extend "\n心怀感激吧。"
    me "嗯。\n哎呀~今天来这里真是来对了。"
    show sakuya 15 with dissolve
    sakuya "啊对了。\n你怎么知道我在这里的？"
    me "是友告诉我的，他说你大概在这里。"
    show sakuya 10 with dissolve
    sakuya "是那家伙啊……。"
    extend "\n喂，[player_surname]。\n你可千万别把小翼的事告诉别人啊。"
    extend "\n把这话也跟那家伙说一声。"
    me "哎？为什么？"
    show sakuya 26 with dissolve
    sakuya "要是让其他人知道了，传出去的话，\n会有许多看热闹的人跑来看小翼，"
    extend "\n那些没有知识的笨蛋说不定会给小翼喂一些对它有害的东西，\n要是有那些不认识的人接二连三跑来，小翼也会害怕的。"
    me "原来如此……明白了，\n我也会跟友说的。"
    show sakuya 5 with dissolve
    sakuya "好，拜托了。"
    "作哉和我说完话之后，翼好像拼命想要表达些什么。"
    show tsubasa 2 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tsubasa "汪！汪！"
    me "作哉，这是？"
    show sakuya 24 with dissolve
    sakuya "让你抱抱它。"
    extend "\n来吧，温柔地把它抱起来。"
    me "但是……我不仅没有抱过狗，\n连孩子都没抱过……"
    show sakuya 1 with dissolve
    sakuya "……真是的，拿你没办法啊。"
    extend "\n要这样抱。"
    hide sakuya with dissolve
    hide tsubasa with dissolve
    "作哉一边说着，一边靠近小翼，\n如字面意思一样手把手地教我怎么抱小翼。"
    show cg purple at center with FadeWhite(0.5)
    play sound "fx/sparkle.ogg"
    "作，作哉靠得好近……！"
    extend "\n这已经算是紧贴状态了……！！"
    "我呼吸变得急促起来。"
    window hide
    hide cg with dissolve
    hide sakuya with dissolve
    hide tsubasa with dissolve
    show sakuya 17 at top with dissolve
    window show
    sakuya "喂，冷静点，好好抱紧它啊！\n它会掉下来的！"
    extend "\n你要是不小心松手，我可饶不了你啊！！"
    me "嗯，嗯，我知道了…。"
    "啊……没想到，他竟然会离我这么近……。"
    extend "\n平时因为散发出一种难以接近的气息，这份喜悦显得更加强烈！！！"
    hide sakuya with dissolve
    "然后，我虽然笨拙，但还是抱着小翼\n沉浸在柔软的毛发上，第一次体会到了抱小狗的感觉。"
    window hide
    show sakuya 5 at top with dissolve
    window show
    sakuya "小翼好像也很喜欢你啊。"
    me "好高兴啊……没想到我们这么合得来。"
    extend "\n以前我一直以为，狗这样的动物只会汪汪地叫着，\n像在威吓人一样。"
    show sakuya 10 with dissolve
    sakuya "……要是你愿意，以后也多来陪小翼玩吧。"
    me "咦，可以吗？"
    show sakuya 9 with dissolve
    sakuya "嘛，毕竟……小翼好像也挺喜欢你的……"
    extend "\n就破例允许你再陪它玩玩吧。"
    me "太好了！！好开心啊~！"
    extend "\n小翼，以后也请多多关照哦。"
    hide sakuya with dissolve
    show tsubasa 1 at top with dissolve
    tsubasa "汪！"
    "就在我拉进与小翼和作哉的关系时，突然意识到集合的时间快到了。\n"
    hide tsubasa with dissolve
    "放下了小翼后，我们也回到了教室。"
    window hide
    stop music fadeout 0.5
    hide bg with Dissolve(0.9)
    return

label day1_cooking_sora:
    show bg infirmary at center
    window show
    me "那，那么，空！"
    extend "\n不好意思，你能留下来吗？"
    window hide
    show sora 2 at topright with dissolve
    window show
    sora "嗯，我知道了。"
    show sora 1 with dissolve
    extend "\n[player_name]君居然说出了这种孩子气的话！"
    "空用开玩笑的口吻笑道。"
    extend "\n居然被比我小十岁的人这么说……。"
    me "呜……啊，啊哈哈……。"
    show tuki 9 at topleft with dissolve
    tuki "那么，我就先回教室了。"
    extend "\n空，[player_name]就拜托你了哦。"
    show sora 3 with dissolve
    sora "嗯，我知道了。"
    play sound "fx/sliding_door.ogg"
    hide tuki with dissolve
    "月这么说着，走出了保健室。"
    window hide
    hide sora with dissolve
    window show
    teacher "哎呀，弟弟会陪在你身边呢。"
    show sora 1 at top with dissolve
    sora "是的。\n[player_name]说他会很寂寞，所以"
    me "呜咕……。"
    hide sora with dissolve
    "虽然我很拼命地劝他们不要离开，\n但被这么一说，还是不由得脸红了起来。"
    extend "\n真是丢脸的成年人……。"
    "我不由得把头埋进了被子里。"
    doctor "哎呀呀，[player_surname]君也还只是个小孩子呢。"
    me "啊，啊哈哈……。"
    teacher "不过，这样我就放心了。"
    extend "\n老师有点事要去办公室一趟，\n赤峰同学你能帮我看一会儿吗？"
    show sora 2 at top with dissolve
    sora "好的，我知道了。"
    teacher "谢谢。"
    extend "\n那我就先走一步了。"
    play sound "fx/sliding_door.ogg"
    "就这样，连保健老师也离开了，\n保健室里就只剩下我和空两个人了。"
    window hide
    hide sora with dissolve
    window show
    me "抱歉啊……空，说了这么任性的话。"
    show sora 24 at top with dissolve
    sora "没事啦。"
    extend "\n我明白你的心情。"
    extend "\n身体不适的时候，心情也会变得消沉，感觉很孤单。"
    me "啊哈哈。\n是啊~不知不觉就有点黏人了。"
    "与其说具体的人，不如说，我是思恋这种少年感。"
    show sora 20 with dissolve
    sora "……呼啊~……。"
    extend "\n呜……感觉我也困了。"
    show sora 33 with dissolve
    sora "真好呢~[player_name]君能躺在床上……"
    show sora 24 with dissolve
    extend "\n这么说可能不太好，身体不舒服可真方便呢"
    show sora 1 with dissolve
    sora "保健室的床，软软的睡上去很舒服吧。"
    extend "\n房间里也很温暖，有种被温柔的守护着的感觉。"
    extend "\n我之前身体不舒服的时候，也睡过一次~"
    me "是这样啊。"
    extend "\n说起来，好像确实是这样。"
    stop music fadeout 2.0
    extend "被褥也保持的很干净……。"
    me "啊。"
    play sound "fx/eureka.ogg"
    "我想到了一个好主意。"
    play music "cute_silly.ogg"
    me "要不，一起睡吧？"
    extend "\n床上很舒服的~。"
    show sora 19 with dissolve
    sora "诶！？可，可是……。"
    me "如果是在其他床上的话，可能会被老师发现，毕竟已经被收拾得很干净了，"
    extend "\n但在这个床上的话，老师回来之前，都不会有问题的。"
    show sora 18 with dissolve
    sora "是这样吗……。"
    me "而且我也没有感冒什么的，"
    extend "\n不会被传染，所以没问题的！"
    "我拉开被褥，为他腾出了一个位置。"
    me "来吧！"
    show sora 25 with dissolve
    sora "唔~嗯……"
    show sora 34 with dissolve
    extend "\n只睡一会儿的话，应该没问题的吧。"
    extend "\n那就，承蒙好意……打扰了~。"
    hide sora with dissolve
    "空脱掉鞋子上了床，在我身旁躺了下来。"
    window hide
    show cg c49 1 at top with Radial(1.0)
    window show
    sora "诶嘿嘿……。"
    extend "\n啊~果然很舒服呢…。"
    extend "\n躺下来以后，反而更困了呢……。"
    sora "[player_name]君，抱歉，\n如果老师来了的话……就叫醒我……。"
    show cg c49 2 with Dissolve(1.0)
    "呼ー呼ー……。"
    "就，这么快就睡着了！！！"
    "话说回来……虽然很顺利地就发展成了这样，\n可这是不是也太夸张了！！！？？"
    extend "\n我自认为办事还挺利索的，没想到会顺利到这种程度。"
    "这，这孩子不会是不懂得怀疑别人吧？"
    extend "\n这真是毫无防备啊……！！！"
    extend "\n再这样下去，我都不知道会干出什么事情来啊！？"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    hide cg with dissolve
    window show
    "*蠕动"
    window hide
    show bg infirmary at center with dissolve
    $ renpy.transition(Quake(0, 60, 0.15, 0.1), layer='master')
    play sound "fx/boing.ogg"
    window show
    me "唔……！"
    play music "hurry_up.ogg"
    "嗯，大腿上有什么东西……。"
    "掀开被子一看，原来是空翻了过来，\n压在了我的身上。"
    show cg adult at center with dissolve
    play sound "fx/sparkle.ogg"
    me "这，这个是啊啊啊啊……！！！"
    "这，这是多么至福的状况啊啊啊啊！！！"
    "不，不不不不不不……等等等等。"
    extend "\n绝对不能失控。"
    extend "\n我必须要保持一个成人的，绅士的冷静……！"
    extend "\n再慢慢地，改变一下体位吧……慢慢地。"
    hide bg with dissolve
    hide cg with dissolve
    "蹭……蹭……"
    sora "呜……嗯…。"
    "滋滋滋"
    window hide
    show bg infirmary at center with dissolve
    $ renpy.transition(Quake(0, 60, 0.15, 0.1), layer='master')
    play sound "fx/boing.ogg"
    window show
    me "！！！"
    "空的脚，气势汹汹地闯入了我的双腿之间。"
    show cg adult at center with dissolve
    me "啊呜呜呜呜呜……！！"
    "空的脚直接给了我刺激。"
    "怎么办……怎么办……。"
    extend "\n这种刺激，实在是忍不住了！！！"
    "……。"
    window hide
    show cg c49 2 with Dissolve(1.5)
    play sound "fx/heartbeat.ogg"
    window show
    "……对了，这是梦……。"
    extend "\n如果是梦的话……对少年做些色色的事情也可以……。"
    "我心中的邪念开始支配我的内心。"
    "有什么好顾虑的……随心所欲地做就好了[player_name]！！"
    play sound "fx/eureka.ogg"
    extend "\n这样的机会，只有现在了！"
    show cg adult with dissolve
    me "空也邀请我了……。"
    "我完全打开了开关，扑在了空的身上。"
    "好，在这个真实的梦里面，得好好发泄一下平时的欲求不满才行……！"
    me "美味的少年啊……"
    play sound "fx/cute2.ogg"
    extend "我开动了！！"
    stop music fadeout 0.5
    hide bg with Dissolve(0.2)
    hide cg with Dissolve(0.2)
    play sound "fx/wind_slash.ogg"
    "啪嚓"
    window hide
    play music "fx/tsubame.ogg"
    show bg infirmary at center with DefocusWhite(1.4)
    show sora 2 at top with dissolve
    window show
    sora "……啊，早上好。"
    extend "\n你醒了吗？"
    "我一看旁边，空正坐在床边的椅子上。"
    show sora 25 with dissolve
    sora "呼啊……"
    show sora 24 with dissolve
    extend "\n[player_name]君看着睡得好香，我也不由得有些犯困，\n不知不觉靠在你身上就睡着了。"
    extend "\n诶嘿嘿……。"
    me "咦……？"
    extend "\n我，刚才还……咦？"
    extend "\n空君，我们不是一起在床上睡的吗……。"
    show sora 21 with dissolve
    sora "诶？\n虽然是靠着你的，但我可没钻到里面去。"
    extend "\n因为我的体重，让你有那种感觉吗？"
    extend "\n对不起。"
    me "诶……啊……啊！？！？"
    stop music fadeout 0.5
    play sound "fx/shock_big.ogg"
    play music "emergency.ogg"
    show cg dark at center with Dissolve(0.2)
    "呃，刚才那个是做梦吗！！！！！！！！！"
    "居然在梦中又做了梦，我真是……。"
    extend "\n真是的，这个梦到底要让我折腾到什么地步才肯罢休啊……。"
    window hide
    hide cg with dissolve
    hide sora with dissolve
    show sora 3 at top with dissolve
    window show
    sora "不过，太好了。\n你看起来恢复得差不多了。"
    extend "\n老师也已经回来了，而且集合时间也到了，\n我打算回教室，[player_name]君打算怎么办？"
    me "呜……我，我也回去……。"
    "既然是梦……刚才正到关键……\n就让我再稍微多做一会儿美梦啊啊啊……！！！！"
    extend "\n呜呜……。"
    hide sora with dissolve
    "就这样，我的欲望落空，我们回到了教室。"
    window hide
    stop music fadeout 0.5
    hide bg with Dissolve(0.9)
    return

label day1_supply_saburo:
    window show
    "去楼顶吧！"
    window hide
    play sound "fx/running.ogg"
    show bg stairs with dissolve
    window show
    "说起来，楼顶不是已经封闭了么……？"
    extend "\n我一边回想着学生时代的回忆，一边拧着通往楼顶的门把手。"
    stop music fadeout 0.5
    window hide
    play sound "fx/door_open.ogg"
    show bg rooftop with Radial(0.5)
    play music "fx/tsubame.ogg"
    window show
    me "打开了…。"
    extend "\n哎~现在已经可以进来了啊。"
    "第一次看到的屋顶上，放着几张长椅，\n看起来只像是一个休息场所。"
    "是在我毕业之后才整修好的吧。"
    me "噢？在那边的是…。"
    "在最里面的长椅上躺着一个人，引起了我的注意。"
    window hide
    play sound "fx/sparkle.ogg"
    show cg c65 at center with FadeWhite(0.8)
    window show
    me "……是三朗君啊。"
    stop music fadeout 0.5
    "我靠近之后，看到三朗的头发在风中飘动，\n似乎睡得很香的样子。"
    play music "lively_boys.ogg"
    "好，好可爱啊……！"
    "睡脸看起来感觉很幸福，越看越觉得可爱起来。"
    "还想看更多。"
    "我顺着这个想法，把脸凑了过去。"
    window hide
    show cg c66 1 with Radial(0.5)
    window show
    saburo "嗯……"
    extend "嗯……？"
    show cg c66 2 with Dissolve(0.3)
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 80, 0.1, 0.07), layer='master')
    extend "\n……什！？？？？"
    "三朗察觉我的气息后微微睁开了眼睛，然后猛然睁大了眼睛。"
    window hide
    hide cg with Dissolve(0.3)
    show saburo 12 at top with dissolve
    $ renpy.transition(Quake(0, 80, 0.1, 0.1), layer='master')
    play sound "fx/dash.ogg"
    window show
    saburo "你你你你你在干什么！啊啊啊！！！"
    "三朗他，坐起来的同时把我也推开了。"
    me "啊哈哈。\n早上好啊，三朗。"
    show saburo 3 with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    saburo "早上好个鬼啊！！！你在搞什么啊！！"
    extend "\n居然在人家睡觉的时候把脸凑上来！"
    me "啊~三朗的睡脸实在是太可爱了，我一不小心就……。"
    "我坦率地阐述了感想。"
    show saburo 14 with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    saburo "（发抖……！）\n这，这算什么啊……你也是那边？\n是那种人吗……？"
    me "诶？那种是指？？"
    show saburo 3 with dissolve
    saburo "别，别装傻啊你这笨蛋！！明明很清楚！！！"
    extend "\n听好了！我可是一点兴趣都没有！！"
    extend "\n不要误会啊！！我对女人才有兴趣！！"
    extend "\n我只喜欢大胸大屁股！！！"
    "啊~原来如此，是这么回事啊。"
    extend "\n明明我什么都没说，你也不用这么拼命地辩解吧。"
    me "知道啦，知道啦。"
    extend "\n我可不是因为那种想法才凑近的。"
    extend "\n只是，那个……该说是好奇心吗，\n我想知道你的睡脸是什么样子的。"
    show saburo 8 with dissolve
    saburo "你问我睡脸是什么样子的？什么意思啊这……"
    show saburo 11 with dissolve
    extend "\n不过算了！既然你这么说了，那就这样吧。"
    show saburo 18 with dissolve
    saburo "啊~啊，[player_surname]把我吵醒，搞得一点睡意也没了。"
    extend "\n到四点半之前干什么呢~。"
    me "抱，抱歉打扰你睡觉了。"
    extend "\n话说回来，你睡着了还能注意到我。"
    show saburo 6 with dissolve
    saburo "啊啊，我对这种事很敏感呢。"
    extend "\n气息，细微的动作什么的，我可是很擅长察觉的。"
    "就像是猫一样。"
    stop music fadeout 2.0
    hide saburo with dissolve
    extend "\n敏感啊……"
    extend "真好啊。"
    window hide
    play music "saburo_theme.ogg"
    show saburo 18 at top with dissolve
    window show
    saburo "话说回来，好无聊啊~。\n没什么可做啊~↑"
    extend "\n社团活动也休息。"
    me "你在什么社团啊？"
    show saburo 5 with dissolve
    saburo "篮球部。"
    extend "\n和穗海一起。"
    me "诶~是这样啊。"
    play sound "fx/sparkle.ogg"
    "穿着篮球部队服……真是不错啊！！"
    extend "\n那个暴露度挺高的。"
    "因为是无袖所以可以随意地观看腋下。\n宽松的短裤下，若隐若现的大腿，还有，更里面的地方！"
    play sound "fx/impact.ogg"
    show cg remarkable at center with Dissolve(0.2)
    extend "\n真让人受不了啊……真想亲眼看看。"
    extend "\n一定要让他和作哉君一起穿穿看！"
    hide saburo with dissolve
    hide cg with dissolve
    "正当我想着这些的时候，三朗突然从长凳上站了起来。"
    show saburo 19 at top with dissolve
    play sound "fx/eureka.ogg"
    saburo "对了~！"
    extend "\n喂，[player_surname]！我教你一个好事。\n来一下这边。"
    play sound "fx/running.ogg"
    hide saburo with dissolve
    "这样说着，三朗向屋顶的深处走去。"
    "『教你一个好事』……。"
    show cg adult at center with FadeWhite(0.5)
    play sound "fx/wow2.ogg"
    extend "听到初中二年级男生的话，我不禁开始幻想。"
    "当我满怀期待地走近，三朗就看向别处傻笑起来。"
    window hide
    hide cg with dissolve
    show saburo 10 at top with dissolve
    window show
    me "嗯？你在看什么？？"
    saburo "你看，那里，仔细看看！"
    "这么说着，他指向了某一点。"
    window hide
    show cg landscape at center with dissolve
    window show
    extend "在那一点的前方，有另一所学校。"
    me "那里……是御咲女子学院？"
    extend "\n诶~刚好能从这里看到呢。"
    saburo "没错！"
    extend "\n然后啊，要是时机正好，\n就能看到在操场上集合，穿着体操短裤的女孩子们了♪"
    me "……难道说，你是为了偷窥才来这里？"
    window hide
    hide cg with dissolve
    hide saburo with dissolve
    show saburo 20 at top with dissolve
    window show
    saburo "偷窥这个词也太失礼了！！"
    extend "\n『健全的初中生男性，在对平时疲惫的身体进行视觉保养』\n我可是有正当的理由的哦！"
    hide saburo with dissolve
    play sound "fx/triangle.ogg"
    "这种在外面就叫「偷窥」。"
    me "体操服……吗。"
    "我无视了女子学院，看向三朗。"
    "什么嘛……所谓教我好事，原来是这样啊。"
    extend "\n如果是看到那个而性奋的三朗君，我倒是会感兴趣啊。"
    extend "\n如果是这孩子穿的体操短裤，那我倒很想看……。"
    window hide
    window show
    me "嗯，三朗君的短裤……真不错……真让人受不了啊…。"
    show saburo 10 at top with dissolve
    saburo "就是啊！！\n女生的体操服果然是最好的！？"
    "不知道他是怎么听的，三朗一脸天真无邪地高兴回道。"
    stop music fadeout 0.5
    window hide
    hide bg with dissolve
    hide cg with dissolve
    hide saburo with dissolve
    window show
    unknown "我也是，和[player_name]酱的想法一致呢~。"
    extend "\n真想看看三酱穿体操短裤的样子啊~。"
    show bg rooftop at center
    show saburo 21 at top with dissolve
    "三＆我" "诶！？"
    hide saburo with dissolve
    "我们向着声音的来源看去，那里"
    window hide
    play music "sintarou_theme.ogg"
    show sintarou 9 at top with dissolve
    window show
    extend "站着的是慎太郎。"
    hide sintarou with dissolve
    show saburo 12 at topright with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    saburo "你，你你你你这家伙！！！！\n为什么你会在这里啊！！！？"
    me "慎太郎君的组也休息了吗？"
    show sintarou 13 at topleft with dissolve
    sintarou "是~啊~。\n今天也没什么特别要做的事！"
    show saburo 14 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    saburo "呜呀呀！！"
    me "诶，好厉害的警戒啊…。"
    show sintarou 29 with dissolve
    sintarou "就是呢~。\n这只小猫咪，怎么都不肯亲近我呢~。"
    show sintarou 4 with dissolve
    extend "\n不过，那种地方也确实很可爱呢！"
    show saburo 3 with dissolve
    saburo "吵，吵死了！！\n和你在一起的时候，总是会被牵着鼻子走！"
    extend "\n拜托了，你快到一边去吧~！！！"
    show sintarou 11 with dissolve
    sintarou "真无情啊~明明都是老交情了。"
    extend "\n不都还一起泡过澡，互相帮忙洗过彼此的身体吗。"
    hide saburo with dissolve
    hide sintarou with dissolve
    play sound "fx/sparkle.ogg"
    show cg adult at center
    show saburo 7 at top with dissolve
    saburo "是啊……不愧是澡堂店长，技术就是不一样啊。"
    hide cg with Dissolve(0.2)
    hide saburo with Dissolve(0.2)
    show saburo 14 at topright with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/dash.ogg"
    extend "\n啊，你在胡说什么啦这个白痴！！！"
    show sintarou 1 at topleft with dissolve
    sintarou "还是一如既往的合拍呢♪"
    extend "\n你就趁着这股劲，到我们的世界来吧。"
    show saburo 3 with dissolve
    saburo "谁，谁会去啊！！"
    extend "\n我是普通人！！我只对女人有兴趣！！"
    extend "\n我只喜欢巨乳丰臀！！"
    show sintarou 11 with dissolve
    sintarou "好好好。\n我已经听腻了小三朗的这些台词啦～。"
    extend "\n你要是不增加点变化，是当不了艺人的啦~♪"
    hide saburo with dissolve
    hide sintarou with dissolve
    play sound "fx/shock.ogg"
    show cg dark at center
    show saburo 15 at top with dissolve
    saburo "真，真的假的……\n我还只是个生手而已……"
    play sound "fx/entrance.ogg"
    show cg remarkable
    show saburo 22 with dissolve
    extend "但是我，永不言弃！！\n我绝对不会放弃当艺人的梦想！！"
    extend "\n我要让全世界的人都因我而露出笑脸！！！！！！"
    hide saburo with dissolve
    hide cg with dissolve
    show sintarou 8 at topleft with dissolve
    sintarou "你是想说，作为同性恋艺人的梦想，对吧？"
    show saburo 2 at topright with dissolve
    saburo "啊，没错没错。\n我是同性恋！我要把我的魅力传递给全世界的同性恋！！"
    show saburo 3 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/dash.ogg"
    extend "\n不对，乱说什么，笨蛋！！！！！！！"
    show cg light-blue at center with dissolve
    "慎＆我" "（鼓掌）"
    hide saburo with dissolve
    hide cg with dissolve
    hide sintarou with dissolve
    show saburo 8 at top with dissolve
    saburo "别拍手别拍手！"
    show saburo 15 with dissolve
    extend "\n啊啊啊啊啊啊啊，不行……我最近果然很奇怪啊。"
    extend "\n从那天开始……从那件事发生的那天开始，\n我好像就朝着不妙的方向前进啊啊啊。"
    "我无视在一旁抱着脑袋痛苦的三朗，向慎太郎耳语道。"
    window hide
    hide saburo with dissolve
    window show
    me "慎太郎啊。\n你该不会是想把三朗带去耽美之道吧？"
    show sintarou 13 at top with dissolve
    sintarou "答对了！"
    show sintarou 12 with dissolve
    extend "\n怎么怎么？[player_name]你是不是也挺想那啥的？？"
    me "呃……嘛，有一点吧……。"
    show sintarou 1 with dissolve
    sintarou "嚯嚯！\n这下可得到了重要情报。"
    extend "\n阿三他啊~就差一步就要过来了，\n但是却在最后的最后坚持住迟迟不肯过来啊~。"
    "什，什么！！！"
    me "原来如此……是这样啊。"
    show sintarou 9 with dissolve
    sintarou "嘛，做太强硬也不好，\n我就慢慢进攻了~。"
    "我倒是觉得这已经很过分了，不过先不说这些。"
    hide sintarou with dissolve
    "但是，这样一来，我总算明白为什么三朗会如此的慌张了。"
    extend "\n原来如此……原来如此啊。三朗君，原来是这样啊！"
    extend "\n看来我这里也得稍微出点力了！！"
    "在青春期，即使心怀憧憬，也常常因莫名的胆怯而无法迈出一步。"
    extend "\n而作为大人，为这样的少年推上一把乃是理所当然的事！"
    play sound "fx/eureka.ogg"
    show cg adult at center with Dissolve(0.3)
    "笑"
    "我不禁笑了出来。"
    extend "\n看来接下来会有一出好戏哦！"
    window hide
    hide cg with dissolve
    hide saburo with dissolve
    hide sintarou with dissolve
    show saburo 18 at top with dissolve
    window show
    saburo "唉……算了。"
    extend "\n也消磨了不少时间，我先回教室了！"
    hide saburo with dissolve
    show saburo 14 at topright with dissolve
    extend "\n喂！！[player_surname]什么都不知道，不要给他灌输一些奇怪的东西啊！"
    show sintarou 4 at topleft with dissolve
    sintarou "不不，那是只属于我们两个的秘密哦~♪"
    show saburo 3 with dissolve
    saburo "白，白痴！！不是那种意思啊！！！"
    extend "\n我要先走了！别靠得太近！！"
    play sound "fx/running.ogg"
    hide saburo with dissolve
    "三朗说完，从楼顶逃也似的回去了。"
    me "慎太郎君，你的兴趣不错啊。"
    hide sintarou with dissolve
    show sintarou 29 at top with dissolve
    sintarou "对吧？"
    "然后我们两个人相视一笑，跟着一起回到了教室。"
    stop music fadeout 0.5
    window hide
    hide sintarou with Dissolve(0.9)
    hide bg with Dissolve(0.9)
    return

label day1_3:
    show bg school_building_evening_full at center with Radial(0.9)
    play music "quiet_lunch.ogg"
    pause 0.6
    show bg classroom_evening with Dissolve(0.8)
    window show
    "回到教室之后，所有人都到齐了。"
    "向老师报告完的友和翼也回来了。"
    window hide
    show tubasa 5 at topleft
    show tomo 12 at topright with dissolve
    show tomo 1 with dissolve
    window show
    tomo "好了！辛苦大家了~。"
    extend "\n今天御咲祭执行委员的工作到此结束！"
    show tomo 2 with dissolve
    extend "\n那么，大家可以回去了~。"
    show tubasa 12 with dissolve
    tubasa "各位辛苦了。"
    window hide
    hide tubasa with dissolve
    hide tomo with dissolve
    stop music fadeout 2.0
    window show
    "呼……"
    extend "那我也回家吧……"
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 40, 0.15, 0.1), layer='master')
    extend "呃，我到底该怎么做啊！？？"
    "冷静点，冷静啊。这是梦。"
    extend "\n绝不是现实……"
    extend "没错吧？"
    "就算我回到家里，也能顺利地被家人接受吧。"
    extend "\n拜托了！！"
    window hide
    return

label day1_3_tomo:
    show tomo 21 at top with dissolve
    window show
    tomo "[player_name]君，怎么了？"
    me "不，没什么……。"
    hide tomo with dissolve
    return

label day1_3_sintarou:
    show sintarou 14 at top with dissolve
    window show
    sintarou "怎么了？[player_name]酱。"
    me "不，没什么……。"
    hide sintarou with dissolve
    return

label day1_3_sinobu:
    show sinobu 5 at top with dissolve
    window show
    sinobu "……怎么了？"
    me "不，没什么……。"
    hide sinobu with dissolve
    return

label day1_3_tubasa:
    show tubasa 2 at top with dissolve
    window show
    tubasa "那，那个，[player_name]君，怎么了？"
    me "不，没什么……。"
    hide tubasa with dissolve
    return

label day1_3_sora:
    show sora 5 at top with dissolve
    window show
    sora "没事吧？[player_name]君。"
    me "啊，嗯。没什么……。"
    hide sora with dissolve
    return

label day1_3_tuki:
    show tuki 17 at top with dissolve
    window show
    tuki "没事吧？[player_surname]。"
    me "啊，嗯……。没什么……。"
    hide tuki with dissolve
    return

label day1_3_saburo:
    show saburo 6 at top with dissolve
    window show
    saburo "[player_surname]，你干什么呢？"
    me "不，没什么……。"
    hide saburo with dissolve
    return

label day1_3_sakuya:
    show sakuya 6 at top with dissolve
    window show
    sakuya "喂，干什么呢。"
    me "不，没什么……。"
    hide sakuya with dissolve
    return

label day1_4:
    window show
    "难不成，不，或许……。"
    extend "\n怀着难以抹去的不安，我踏上了归途。"
    window hide
    show bg sidewalk_evening with Dissolve(2.0)
    show bg residential_area_evening with Dissolve(2.0)
    play music "haunted_music_room.ogg"
    show bg protagonist_home_evening with FadeBlack(2.0)
    window show
    "……嗯。"
    extend "房子看上去和原来一样。"
    "可话虽如此，家的外观和以前相比也没什么太大的变化。"
    extend "\n如果能证明是我回到了中学时代的话，就能确信这不过是做梦了。"
    "初中时还有的东西，在25岁的时候却已经失去了啊……。"
    extend "\n呜"
    extend "…"
    extend "…"
    extend "啊，对了！"
    extend "自行车！！"
    "是我远赴邻镇时的必备工具，心爱的座驾。"
    extend "\n在我初中毕业时坏掉了，就扔掉了。"
    "嗯，自行车的话记得是放在车库里……"
    "···"
    show bg dark with dissolve
    "……"
    play sound "fx/shock_big.ogg"
    extend "没有！！？？"
    "也就是说，在梦中的现在与现实中处在同一时代吗。"
    "这下我越发觉得不安起来了……。"
    extend "\n难道这不是梦，而是现实。"
    stop music fadeout 0.5
    mother "哎呀，你在做什么呢？"
    play sound "fx/boing.ogg"
    me "噫！？！？"
    "回过头来，\n"
    window hide
    show お母さん c21 at center with Radial(0.5)
    window show
    extend "映入眼帘的正是我母亲骑着我的爱车，还载着购物袋的身姿。"
    me "妈，妈妈……！！"
    mother "啊，忘记把钥匙放在花盆下面了。对不起。"
    extend "\n[player_name]，你在这等了多久呢？"
    me "妈妈啊啊啊！！"
    window hide
    play music "nostalgia.ogg"
    show お母さん adult with dissolve
    window show
    "母亲的身姿还是十年前，我初中时的样子。"
    "我一下从怀念和紧张中解放开来，"
    extend "\n不由得回想起初中时的心境，我一边感到羞耻，一边哭着扑到了母亲怀里。"
    mother "真是的，这孩子……太夸张了。"
    window hide
    hide お母さん with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    window show
    "···"
    window hide
    show bg living_room_night at center with Radial(1.0)
    window show
    father "[player_name]下周有文化祭吧。"
    extend "\n你们班要做什么？"
    "晚饭的时候，父亲问我。"
    me "咖啡厅。"
    extend "\n和风，西式，中式，什么都有的咖啡厅。"
    "现在的孩子还真是讲究啊。"
    extend "\n0"
    me "其实~到最后，只是单纯地，没有想好要做什么，\n所以就全部混在一起了。\n不过呢，倒也挺不错的。"
    father "哈哈，原来如此。"
    extend "\n对了，妈妈是要去参加文化祭吧。"
    mother "是啊。"
    extend "\n和笠崎太太，岸谷太太约好了要一起去。"
    father "哎呀~我要是没有工作的话也想去参加啊。"
    extend "\n偶尔也得回归童心，和孩子们一起享受啊。"
    mother "哎呀哎呀，男人不论到什么时候都不会忘记孩子气呢。"
    "···"
    window hide
    show bg protagonist_home_night with Dissolve(0.9)
    window show
    "一家人齐聚一堂吃饭，这是多久以前的事了啊……。"
    extend "\n回想起来，自从我开始工作后，就几乎没有和母亲独处过。"
    extend "\n和父亲下班时间对不上，近来连碰面的机会都很少。"
    "合家团聚是最棒的调味料。"
    hide bg with dissolve
    stop music fadeout 2.0
    "在温暖的气氛中吃的母亲的料理，总比平时更加美味。"
    window hide
    play sound "fx/door_open.ogg"
    show bg protagonist_room_night at center with dissolve
    window show
    me "……呼。"
    "我回到自己的房间，坐在床上。"
    me "来这个世界之前，记得也是这个时候睡着了吧。"
    "如果，现在闭上眼睛"
    extend "就能从梦中醒来吗？。"
    "还想……"
    extend "留在这个世界啊……"
    extend "再稍微多待一会啊……。"
    "明天还能"
    extend "再与大家见面就好。"
    window hide
    hide bg with dissolve
    return

label day1_4_tomo:
    show tomo at top with dissolve
    window show
    "还想再和友君他们多好好相处，想一起度过御咲祭。"
    extend "\n怀着这种心情，我渐渐进入了梦乡。"
    hide bg with DefocusBlack(5.0)
    hide tomo with DefocusBlack(5.0)
    "Zzz"
    window hide
    return

label day1_4_sintarou:
    show sintarou at top with dissolve
    window show
    "还想再和慎太郎他们多好好相处，想一起度过御咲祭。"
    extend "\n怀着这种心情，我渐渐进入了梦乡。"
    hide bg with DefocusBlack(5.0)
    hide sintarou with DefocusBlack(5.0)
    "Zzz"
    window hide
    return

label day1_4_sinobu:
    show sinobu at top with dissolve
    window show
    "还想再和忍君他们多好好相处，想一起度过御咲祭。"
    extend "\n怀着这种心情，我渐渐进入了梦乡。"
    hide bg with DefocusBlack(5.0)
    hide sinobu with DefocusBlack(5.0)
    stop music fadeout 0.5
    "Zzz"
    window hide
    return

label day1_4_tubasa:
    show tubasa at top with dissolve
    window show
    "还想再和翼君他们多好好相处，想一起度过御咲祭。"
    extend "\n怀着这种心情，我渐渐进入了梦乡。"
    hide bg with DefocusBlack(5.0)
    hide tubasa with DefocusBlack(5.0)
    stop music fadeout 0.5
    "Zzz"
    window hide
    return

label day1_4_sora:
    show sora at top with dissolve
    window show
    "还想再和空君他们多好好相处，想一起度过御咲祭。"
    extend "\n怀着这种心情，我渐渐进入了梦乡。"
    hide bg with DefocusBlack(5.0)
    hide sora with DefocusBlack(5.0)
    stop music fadeout 0.5
    "Zzz"
    window hide
    return

label day1_4_saburo:
    show saburo at top with dissolve
    window show
    "还想再和三朗君他们多好好相处，想一起度过御咲祭。"
    extend "\n怀着这种心情，我渐渐进入了梦乡。"
    hide bg with DefocusBlack(5.0)
    hide saburo with DefocusBlack(5.0)
    stop music fadeout 0.5
    "Zzz"
    window hide
    return

label day1_4_tuki:
    show tuki at top with dissolve
    window show
    "还想再和月君他们多好好相处，想一起度过御咲祭。"
    extend "\n怀着这种心情，我渐渐进入了梦乡。"
    hide bg with DefocusBlack(5.0)
    hide tuki with DefocusBlack(5.0)
    stop music fadeout 0.5
    "Zzz"
    window hide
    return

label day1_4_sakuya:
    show sakuya at top with dissolve
    window show
    "还想再和作哉君他们多好好相处，想一起度过御咲祭。"
    extend "\n怀着这种心情，我渐渐进入了梦乡。"
    hide bg with DefocusBlack(5.0)
    hide sakuya with DefocusBlack(5.0)
    stop music fadeout 0.5
    "Zzz"
    window hide
    return