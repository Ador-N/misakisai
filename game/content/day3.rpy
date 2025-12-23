# -*- coding: utf-8 -*-
# Converted from 000001FA.lns

label day3:
    play music "fx/tsubame.ogg"
    show bg protagonist_home at center with Dissolve(1.0)
    pause 0.4
    hide bg with dissolve
    window show
    play sound "fx/alarm.ogg"
    "（哔哔哔哔哔哔哔哔）"
    "伴随着麻雀的呢喃，闹钟的铃声响了起来。"
    window hide
    show bg protagonist_room_morning at center with FadeWhite(0.5)
    play sound "fx/wind_slash.ogg"
    window show
    "（砰！！）"
    "我一边敲着闹钟，一边用力地翻身坐起。"
    extend "\n就这样径直冲向全身镜，确认镜子里依然是那个初中生模样的自己！！"
    stop sound fadeout 0.5
    play music "lively_boys.ogg"
    show cg remarkable at center with FadeWhite(0.5)
    play sound "fx/eureka.ogg"
    me "哟——西！！！"
    extend "\n今天也还是一如既往的不起眼！完美！！"
    window hide
    hide cg with dissolve
    window show
    play sound "fx/door_open.ogg"
    "（喀嚓）"
    mother "[player_name]！还不起来！！"
    extend "\n哦，咦？居然已经起床了，真稀奇呢~。"
    extend "\n一大早就对着镜子傻笑什么呢……。\n你什么时候变得那么自恋啦？"
    me "没啦没啦，没有那么夸张啦~♪"
    extend "\n哼哼~！年轻的身体真好啊！"
    mother "什么呀，真奇怪……。"
    extend "\n可别是染上什么奇怪的癖好了……。"
    "嘛，虽然我确实朝着『奇怪的兴趣』全力疾走中就是了……。"
    extend "\n心情超好的我，匆匆忙忙吃完早饭，便飞奔出了家门。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label day3_1:
    play sound "fx/door_open.ogg"
    show bg sky at center with Radial(0.5)
    play music "going_to_school.ogg"
    window show
    me "嗯！"
    extend "\n今天也是大晴天呐~！！"
    "沐浴着清晨的阳光，我的情绪愈发高涨。"
    "真是太棒了！初中生活太爽了！！！"
    extend "\n今天也要和御咲学园的大家度过快乐的一天啊！！"
    extend "\n不过，千万得注意别因为太得意忘形，又搞得像昨天那样差点被车撞到，\n一定要加倍小心才行……。"
    window hide
    hide bg with dissolve
    return

label day3_1_tomo_sinobu:
    show bg school_route at center with dissolve
    show tomo 13 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    window show
    tomo "喂~，[player_name]君——！"
    hide tomo with dissolve
    show tomo 12 at topright
    show sinobu 1 at topleft with dissolve
    "我朝着声音传来的方向看去，发现友和忍正朝这边走来。"
    show tomo 4 with dissolve
    tomo "早上好~！"
    show sinobu 8 with dissolve
    sinobu "早。"
    me "早上好！！友君，忍君！"
    extend "\n哎呀~你们今天也是魅力四射啊！"
    play sound "fx/sparkle.ogg"
    extend "简直让人想把你们直接吃掉啊，哈哈哈哈！"
    hide tomo with dissolve
    hide sinobu with dissolve
    show tomo 21 at topright
    show sinobu 9 at topleft with dissolve
    play sound "fx/triangle.ogg"
    "友＆忍" "……哈？"
    "哎呀，不好。"
    extend "\n在高涨的情绪驱使下，不小心说出了真心话。"
    window hide
    hide tomo with dissolve
    hide sinobu with dissolve
    show tomo 8 at topright with dissolve
    window show
    tomo "总、总觉得[player_name]你最近好像性格变了呢。"
    extend "\n感觉以前不是这样的？"
    show sinobu 2 at topleft with dissolve
    sinobu "你是不是被友和慎太郎洗脑了？"
    show tomo 16 with dissolve
    tomo "唔！"
    extend "\n我们可没有随随便便去影响别人呢！"
    show sinobu 11 with dissolve
    sinobu "连这点自觉都没有，真是可怜……"
    show sinobu 10 with dissolve
    extend "\n这就叫近朱者赤，近墨者黑。"
    me "哈哈哈。"
    extend "\n说起来，你们两个是从同一个方向过来的，\n你们住得很近吗？"
    show sinobu 1 with dissolve
    sinobu "嗯。"
    extend "\n我们住在宝咲同一栋公寓里。"
    show tomo 1 with dissolve
    tomo "我在301室，忍在201室。"
    extend "\n所以，除了忍有社团晨练的时候以外，\n我们上下学基本上都在一起~！"
    me "嘿~！原来大家住在一起啊。"
    extend "\n那忍君，你楼上应该每天都很吵吧？"
    show tomo 27 with dissolve
    play sound "fx/boing.ogg"
    tomo "这话是什么意思啊？"
    show sinobu 4 with dissolve
    sinobu "确实很吵。"
    show sinobu 12 with dissolve
    extend "……不过，他偶尔练习钢琴的声音，\n倒是挺适合当读书时的BGM。"
    show tomo 2 with dissolve
    tomo "哼哼！能帮上忙是我的荣幸！！"
    show tomo 40 with dissolve
    extend "\n但是，能不能拜托你，每次我『干坏事』的时候，\n别再从窗户闯进来了啊……。"
    me "窗户！？那是怎么回事？？"
    hide tomo with dissolve
    hide sinobu with dissolve
    show tomo 15 at top with dissolve
    tomo "别看忍这副样子，他的运动神经可是非常了得。"
    extend "\n他能从自己房间的阳台跳到隔壁家的屋檐上，\n再直接纵身一跃，跳到我房间的阳台里来。"
    "真像漫画里才会有的场景啊……简直就像忍者一样。"
    extend "\n不如说，我反而觉得忍君才是干了什么坏事的人吧……。"
    show tomo 29 with dissolve
    tomo "就是说啊，这孩子真的挺可怕的……。"
    hide tomo with dissolve
    show sinobu 3 at topleft with dissolve
    sinobu "那还不是因为友总是做些奇怪的事。"
    extend "\n真是的，不知道什么时候才能学着变成熟点。"
    show tomo 23 at topright with dissolve
    tomo "唔唔！"
    show tomo 6 with dissolve
    extend "\n说起这个，忍住的那一楼，\n时不时能听到游戏招式的叫喊声哦~！"
    show sinobu 13 with dissolve
    $ renpy.transition(Quake(30, 0, 0.1, 0.08), layer='master')
    play sound "fx/boing.ogg"
    sinobu "（惊）"
    show tomo 2 with dissolve
    tomo "哼哼~嗯♪我可是全都知道的哦~。"
    extend "\n忍开始学习空手道，是因为受到了漫画的影响吧！"
    extend "\n从这点来看，你还真是个小孩子呢~？↑"
    show sinobu 14 with dissolve
    sinobu "……有什么关系，不可以吗。"
    show tomo 25 with dissolve
    tomo "哦~。还是说，其实还有什么别的理由？"
    show sinobu 15 with dissolve
    sinobu "……秘密。"
    show tomo 40 with dissolve
    tomo "唔~！你这个保密怪~！！"
    show sinobu 6 with dissolve
    sinobu "是友太大嘴巴了。"
    show tomo 3 with dissolve
    tomo "还有啊……对了！"
    show tomo 9 with dissolve
    extend "拜托你好好学学做饭吧。"
    show tomo 27 with dissolve
    extend "\n究竟是用了什么方法才能做出那么可怕的东西啊。"
    extend "\n再这样下去，炸牡蛎做成炸弹牡蛎也不是梦了啊。"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    show sinobu 16 with dissolve
    sinobu "人、人各有所长，总有不擅长的事情嘛。"
    show tomo 26 with dissolve
    tomo "不对不对……再怎么说，\n也不至于把可乐当成酱油加进去啊。"
    show sinobu 17 with dissolve
    sinobu "那、那是……那个……。"
    show tomo 6 with dissolve
    tomo "不过最近啊，\n我也已经习惯忍做的那些神秘料理了。"
    show tomo 31 with dissolve
    extend "\n下次做蛋包饭的时候，一定要成功啊！"
    show sinobu 7 with dissolve
    sinobu "嗯。下次绝对不会再把番茄酱和红味噌搞混了。"
    window hide
    show cg c34 1 at center with Radial(0.5)
    window show
    me "哈哈，你们俩关系真好啊。"
    tomo "是啊！我们可是发小啊！"
    sinobu "……嗯。"
    window hide
    hide tomo with dissolve
    hide sinobu with dissolve
    hide cg with dissolve
    window show
    "之后，我一边听着他们俩没完没了的拌嘴，一边走向学校。"
    extend "\n今天也一定会是美好的一天。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    pause 0.4
    return

label day3_1_saburo_sakuya_tubasa:
    show bg school_route at center with dissolve
    show saburo 10 at top with dissolve
    window show
    saburo "哦，是[player_surname]呀！"
    extend "\n早~安。"
    hide saburo with dissolve
    "我朝着声音传来的方向看去，"
    show saburo 1 at top
    show sakuya 31 at topright with dissolve
    "只见三朗、作哉，"
    show tubasa 5 at topleft with dissolve
    "还有翼正并排走来。"
    show sakuya 23 with dissolve
    sakuya "早上好。"
    show tubasa 31 with dissolve
    tubasa "早、早上好。"
    me "早上好！！大家！"
    extend "\n哎呀~今天也让人心情大好啊！"
    play sound "fx/sparkle.ogg"
    extend "简直让人想把你们直接吃掉啊，哈哈哈哈！"
    hide saburo with dissolve
    hide tubasa with dissolve
    hide sakuya with dissolve
    show saburo 21 at top
    show sakuya 17 at topright
    show tubasa 17 at topleft with dissolve
    play sound "fx/triangle.ogg"
    "三＆作" "……哈？"
    "哎呀，不好。"
    extend "\n在高涨的情绪驱使下，不小心说出了真心话。"
    window hide
    hide saburo with dissolve
    hide sakuya with dissolve
    hide tubasa with dissolve
    show tubasa 22 at topleft with dissolve
    window show
    tubasa "那、那个，你是哪里不舒服吗……？"
    show sakuya 10 at topright with dissolve
    sakuya "我觉得比起去学校，你更应该先去医院挂个号吧？"
    show saburo 16 at top with dissolve
    saburo "同感。"
    extend "\n看着男孩子还觉得可爱什么的，是不是稍微有点怪啊~？"
    "啊啊……这、这冷冰冰的视线简直让人欲罢不能……！！"
    play sound "fx/cute2.ogg"
    extend "\n你们可能不觉得有什么，但对我们正太控来说，这可是最高的奖赏啊！"
    show saburo 8 with dissolve
    saburo "呜哇，表情好怪。"
    show sakuya 15 with dissolve
    sakuya "真恶心。"
    show tubasa 32 with dissolve
    tubasa "……。"
    play sound "fx/dash.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.09), layer='master')
    "呜……被说到这份上，连我也感觉胸口中了一箭。"
    extend "\n再这么得意忘形下去，好感度就真的要跌到底谷了。"
    me "啊、啊哈哈哈！开玩笑的啦！"
    extend "\n别这么疏远我嘛~。"
    show saburo 17 with dissolve
    saburo "[player_surname]君的玩笑话听起来并不好笑，\n还是少说两句比较好……。"
    show tubasa 19 with dissolve
    tubasa "是、是啊。真的吓了我一跳。"
    show sakuya 9 with dissolve
    sakuya "一大清早就遇到一之濑，还遇到了这种恶心的家伙，\n今天真是倒霉呢~。"
    show tubasa 7 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    tubasa "怎、怎么这样……"
    show saburo 4 with dissolve
    saburo "别这么说，穗海。"
    show saburo 2 with dissolve
    extend "\n一之濑，你也不用在意。\n这家伙，正处在叛逆期啊！"
    show sakuya 2 with dissolve
    sakuya "谁叛逆期啊笨蛋。"
    show tubasa 9 with dissolve
    tubasa "呜呜……。"
    show sakuya 16 with dissolve
    sakuya "就是受不了你这种动不动就委屈巴巴的样子，看着就烦！"
    show saburo 4 with dissolve
    saburo "不过还真是不可思议呐~。\n嘴上嫌弃成这样，却总是提到一之濑的事情呢。"
    show saburo 18 with dissolve
    extend "\n呐，[player_surname]，你觉得是为什么？"
    play sound "fx/impact_japanese.ogg"
    me "答案就是，恋爱！！！"
    hide sakuya with dissolve
    hide saburo with dissolve
    hide tubasa with dissolve
    play sound "fx/punch3.ogg"
    $ renpy.transition(Quake(0, 150, 0.1, 0.07), layer='master')
    "（啪！！）"
    me "呜……"
    show sakuya 17 at top with dissolve
    sakuya "少、少在那儿胡说八道！！！\n谁会看上这种家伙啊！！"
    show sakuya 27 with dissolve
    extend "\n我要宰了你这混蛋！！"
    hide sakuya with dissolve
    show saburo 17 at topleft with dissolve
    saburo "喂喂，你这补刀简直是给人判死刑了啊……。"
    show sakuya 2 at topright with dissolve
    play sound "fx/boing.ogg"
    sakuya "少、少啰嗦！！！"
    extend "\n啊~可恶！！一个个都让人火大！！"
    extend "\n不陪你们玩了！我要走了！！"
    "说完，作哉就"
    play sound "fx/running.ogg"
    hide sakuya with dissolve
    "气急败坏地跑向了学校。"
    show tubasa 2 at topright with dissolve
    tubasa "那、那个……[player_name]君，你没事吧？"
    show saburo 2 with dissolve
    saburo "真是个开不起玩笑的家伙啊~。"
    "两人伸手把我从地上扶了起来。"
    me "呼呼呼……被少年殴打，又被少年温柔地扶起来……"
    play sound "fx/eureka.ogg"
    extend "\n无论哪个，都是我想要的啊……。"
    play sound "fx/triangle.ogg"
    show tubasa 22
    show saburo 9 with dissolve
    saburo "……果然[player_surname]还是别开这种玩笑比较好。"
    tubasa "……也是呢……我都被吓到了……。"
    "一早就能融入少年们的日常，真幸福啊……。"
    extend "\n今天也一定会是美好的一天。"
    window hide
    hide saburo with dissolve
    hide tubasa with dissolve
    hide bg with dissolve
    stop music fadeout 0.5
    pause 0.4
    return

label day3_1_sintarou_tuki_sora:
    show bg school_route at center with dissolve
    show sintarou 8 at topleft with dissolve
    window show
    sintarou "早啊[player_name]酱！哈喽——！"
    "我朝着声音传来的方向看去，发现慎太郎和赤峰兄弟正朝这边走来。"
    show sora 3 at topright with dissolve
    sora "早上好，[player_name]君。"
    show tuki 9 at top with dissolve
    tuki "早。"
    me "早上好！！大家！"
    extend "\n哎呀~你们今天也是魅力四射啊！"
    play sound "fx/sparkle.ogg"
    extend "简直让人想把你们直接吃掉啊，哈哈哈哈！"
    hide sintarou with dissolve
    hide tuki with dissolve
    hide sora with dissolve
    show sintarou 14 at topleft
    show sora 13 at topright
    show tuki 11 at top with dissolve
    play sound "fx/triangle.ogg"
    "慎＆月＆空" "……哈？"
    "哎呀，不好。"
    extend "\n在高涨的情绪驱使下，不小心说出了真心话。"
    window hide
    hide sintarou with dissolve
    hide sora with dissolve
    hide tuki with dissolve
    show sora 14 at topright with dissolve
    window show
    sora "[player_name]君……莫、莫非，今天身体也不舒服吗？"
    show tuki 5 at top with dissolve
    tuki "没必要勉强自己去学校吧？"
    extend "\n再这样下去会影响到学园祭的。"
    show sintarou 17 at topleft with dissolve
    sintarou "嗯~看起来倒像是没发烧呢。"
    "哈哈哈。完全被当成病号对待了啊。"
    extend "\n不过，被这么多可爱的男孩子包围，脑子当然会烧坏啊！"
    extend "\n不如说，我到现在还没出手，已经算是很冷静了。"
    show sintarou 29 with dissolve
    sintarou "不过啊！\n要是论变态程度的话，我可不会输给你哦！"
    show sora 4
    show tuki 2 with dissolve
    tuki_and_sora "嗯。"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    show sintarou 21 with dissolve
    sintarou "喂……！"
    extend "\n答应得这么干脆，咱可是一点面子都没了啊。"
    show sintarou 9 with dissolve
    sintarou "不过~要说奇怪程度的话，咱觉得你们二位也半斤八两吧。"
    show sintarou 12 with dissolve
    extend "\n毕竟……你们每晚都玩得挺尽兴的吧？\n明明是亲兄弟~！欸嘿嘿。"
    play sound "fx/eureka.ogg"
    me "你、你们在说什！！！"
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    show sora 16 with dissolve
    sora "小慎！那个那个那个！！！"
    show sora 15 with dissolve
    extend "\n不、不是的！我们才没有做那种事！！！"
    show tuki 12 with dissolve
    tuki "你在说什么呢。实际上每晚都，欸嘿嘿……"
    $ renpy.transition(Quake(0, 100, 0.1, 0.07), layer='master')
    play sound "fx/punch.ogg"
    hide tuki with dissolve
    extend "\n（啪嚓！）"
    show sora 16 with dissolve
    $ renpy.transition(Quake(60, 0, 0.1, 0.15), layer='master')
    sora "哇啊啊啊啊！！真是的！"
    extend "\n哥哥你不需要说那些多余的话！！！！"
    show sintarou 9 with dissolve
    sintarou "哎呀~空害羞的样子真好玩~。"
    show tuki 4 at top with dissolve
    tuki "空可爱的地方就在于此。"
    show tuki 3 with dissolve
    extend "\n真的，他怎么能这么可爱呢。"
    show tuki 10 with dissolve
    extend "\n可爱到我有时候都害怕我会受不了。"
    show sora 15 with dissolve
    sora "够了——！！烦死啦！！"
    show sora 17 with dissolve
    extend "\n哥哥这个笨蛋！再也不理你了！！"
    window hide
    hide sora with dissolve
    hide sintarou with dissolve
    hide tuki with dissolve
    show cg dark at center
    show tuki 13 at top with Dissolve(0.2)
    play sound "fx/shock.ogg"
    window show
    tuki "（受打击！！！）"
    sintarou "啊~完蛋，月被甩掉了呢。"
    window hide
    show tuki 13 with dissolve
    $ renpy.transition(Quake(0, 100, 0.1, 0.065), layer='master')
    play sound "fx/shock_big.ogg"
    window show
    tuki "（受暴击！！！！）"
    show tuki 14 with dissolve
    play sound "fx/ding.ogg"
    tuki "啊……被甩了……。"
    extend "\n我……好像已经找不到生存下去的意义了……。"
    "月的身体摇摇晃晃，好像马上就要被风吹走一样。"
    window hide
    play sound "fx/fall_down.ogg"
    hide tuki with dissolve
    hide cg with dissolve
    show sora 18 at topright with dissolve
    window show
    sora "啊……不、不用这么失落吧……。"
    show sintarou 11 at topleft with dissolve
    sintarou "这就是号称全校最强的剑道部主将吗……。"
    me "现在好像是个人都能给他一记暴击呢。\n（注：『面打ち』作为剑道术语无法直译，这里是基于赤峰兄弟身份玩了一个梗）"
    hide sintarou with dissolve
    hide sora with dissolve
    show sora 19 at topright with dissolve
    sora "哥、哥哥！对不起，是我说得太过分了。"
    extend "\n所以，好了，快站起来！"
    extend "\n再这样下去要上学迟到了。"
    show tuki 10 at topleft with dissolve
    tuki "唔……空……"
    extend "\n我……是笨蛋吗……？"
    extend "\n是真的被甩了吗……？"
    show sora 20 with dissolve
    sora "唉……都不是啦。"
    extend "\n哥哥才不是笨蛋，也不会被我甩的。"
    show sora 12 with dissolve
    extend "\n你是我最最帅气的哥哥哦！"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    show tuki 8 with dissolve
    tuki "是吗。那太好了。"
    me "恢复得也太快了吧！"
    show tuki 4 with dissolve
    tuki "身为空的帅气哥哥，那就绝对不能在那儿垂头丧气。"
    extend "\n要是空在这期间出事了怎么办？"
    show sintarou 13 at top with dissolve
    sintarou "好啊好啊，一大早的嗑得那么甜！！"
    "啊……好幸福……。"
    extend "\n一大早就能加入少年们这么热闹的对话，还不用上班，能去学校上学！"
    hide sintarou with dissolve
    hide sora with dissolve
    hide tuki with dissolve
    "今天也一定会是美好的一天。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    pause 0.4
    return

label day3_2_tomo:
    show bg school_building_morning at center with Radial(0.5)
    play sound "fx/chime.ogg"
    pause 0.4
    play music "quiet_lunch.ogg"
    window show
    "……呼。今天的课程也结束了。"
    extend "\n上午的时间真的好短啊。要是上班的话，现在才算正式开始呢。"
    show bg classroom with dissolve
    "那么，赶紧吃完午饭，开始委员的工作吧。"
    extend "\n正当我起身准备去食堂时，发现友就站在我的身后。"
    window hide
    show tomo 19 at top with dissolve
    window show
    tomo "[player_name]君！"
    extend "\n那个……今天，要不要一起在楼顶吃午餐？"
    me "嗯？啊啊，可以啊。"
    extend "\n不过，为什么要在楼顶？"
    show tomo 35 with dissolve
    tomo "因、因为……"
    show tomo 31 with dissolve
    extend "哎呀，别管那么多啦！\n总之快走吧！！"
    me "啊，等等，我得先去食堂买点吃的才行。"
    show tomo 20 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tomo "没、没关系啦！总之你先过来！！"
    hide tomo with dissolve
    "跟着友来到屋顶，\n"
    stop music fadeout 0.5
    window hide
    play sound "fx/running.ogg"
    show bg hallway with dissolve
    pause 0.4
    show bg stairs with dissolve
    pause 0.4
    play music "fx/tsubame.ogg"
    show bg rooftop with Radial(1.0)
    window show
    extend "发现这里是一处只放了几张长凳、\n宽敞得像休息区一样的地方。"
    "风景很美，气温也恰到好处，还有微风拂面，感觉十分舒爽。"
    me "诶~原来这里是这样子的啊~。"
    extend "\n我记得以前这里是被封锁着的。"
    window hide
    show tomo 21 at top with dissolve
    window show
    tomo "那是什么时候的事情啊？"
    show tomo 12 with dissolve
    extend "\n至少，从我们入学以来，这里就一直是对外开放的哦。"
    "友笑着说道。"
    show tomo 6 with dissolve
    tomo "我之前就在想，"
    extend "\n[player_name]君，有时说话像个大人呢。"
    extend "\n是受到了什么漫画的影响吗？"
    me "没、没有~大概就是那种感觉吧~？"
    "这种蒙混过关的借口，连我自己都觉得尴尬啊！"
    extend "\n不行，得赶紧转移话题……！！"
    me "那、那么，友君。"
    extend "\n为什么今天只有我们两个人呀？\n你平时都是和大家一起吃饭的。"
    show tomo 8 with dissolve
    tomo "稍、稍微有点原因啦……"
    show tomo 15 with dissolve
    extend "给，这个！"
    window hide
    stop music fadeout 0.5
    play music "tomo_theme.ogg"
    show cg c13 at center with Radial(0.5)
    window show
    "友拿出了两个便当盒，将其中的一个朝我递了过来。"
    me "诶，这个难道是……？"
    "是友酱亲手做的便当！？？？"
    play sound "fx/explosion2.ogg"
    extend "\n男孩子亲手做的便当啊啊啊啊啊啊啊啊啊！！！！！！"
    tomo "嗯、嗯。\n算是对昨天的回礼吧。"
    extend "\n这种事情要是被其他男孩子看到会很丢脸的！\n所以，才特意把你带到屋顶来……。"
    "友微微红着脸，扭扭捏捏地说着。"
    play sound "fx/cute2.ogg"
    extend "\n这么可爱的你我也好想直接吃掉啊友酱！！！！！！"
    me "原来是这样啊。"
    extend "\n非常感谢。我很开心！"
    extend "\n那么我就不客气了，我开动啦！"
    window hide
    play sound "fx/sparkle.ogg"
    show cg yellow with FadeWhite(0.5)
    window show
    "打开盒盖，只见里面塞得满满当当，\n是个分量十足的便当。"
    extend "\n虽然摆放得有些随意，但正是这种男孩子气的感觉，反而让人更有食欲。"
    "我从便当盒里夹起一块硕大的鸡蛋烧，送入口中。"
    "啊呜~"
    window hide
    hide cg with dissolve
    hide tomo with dissolve
    show tomo 40 at top with dissolve
    window show
    tomo "怎、怎么样……？"
    "友显得异常紧张，向我问道。"
    me "嗯！！太好吃了！！！"
    show tomo 31 with dissolve
    tomo "真的吗？太好了！"
    show tomo 2 with dissolve
    extend "\n嘛，虽然我原本就对自己很有信心啦！"
    "友先是如释重负地松了口气，"
    extend "\n但随即又立刻摆出一副得意洋洋的架势，和往常一样做了个鬼脸。"
    me "啊哈哈，不过真的很好吃哦！友有自信也是应该的。"
    extend "\n我还以为你已经习惯吃忍君做的料理，稍微有点担心来着。不过要是能做出这么好吃的便当，我甚至想以后每天都吃呢。"
    show tomo 35 with dissolve
    tomo "哪、哪有那么夸张啦。"
    "面对我不带奉承、发自内心的感想，友又露出了一丝羞涩。"
    extend "\n这种浓郁的调味也是我偏好的，\n分量很足，对于食量很大的我来说也十分满意。"
    "啊啊~真想让他嫁给我啊。"
    me "无论是弹钢琴还是做料理，友君你意外地拥有很多细腻的特长呢。"
    show tomo 4 with dissolve
    tomo "啊哈哈，那个啊。月也这么说过我呢~。"
    show tomo 31 with dissolve
    extend "\n不过……也是不得不这样做的。"
    show tomo 22 with dissolve
    tomo "我没有爸爸，家里只有我和我妈妈。"
    extend "\n而且之前也提过，我妈妈经常要去国外演出，所以家务活什么的，自然而然就学会了。"
    show tomo 31 with dissolve
    tomo "不过这些方面，我也会找忍帮忙就是了。"
    extend "\n妈妈也说，正因为有忍他们一家在，她才能放心地去工作。"
    me "这样啊……。"
    show cg sky at center with dissolve
    "原来如此……。"
    extend "\n之前在音乐室时那些不可思议的感慨，就是因为这样吗。"
    extend "\n虽然平时都装出很开朗的样子，"
    extend "\n但是果然有时候会觉得孤单寂寞吧。"
    "想到这里，我感到胸口一紧。"
    window hide
    hide cg with dissolve
    hide tomo with dissolve
    window show
    me "友。"
    extend "\n觉得难过的时候，我会支持你的，尽管依靠我吧，我很可靠的哦。"
    show tomo 33 at top with dissolve
    tomo "[player_name]君……"
    show tomo 34 with dissolve
    extend "\n谢啦！但是，我完全没问题的。"
    show tomo 31 with dissolve
    extend "\n我现在已经没有任何烦恼了！\n毕竟忍和大家都在身边，每天都过得很开心呐。"
    me "是吗是吗，那就好。"
    extend "\n但是，可不要勉强自己哦。"
    "我伸手轻轻地把手放在友的头上，摸了摸。"
    show tomo 36 with dissolve
    tomo "……不知怎么的，[player_name]君，有时候感觉你真的一点都不像同龄人。"
    extend "\n感觉要年长得多得多，总觉得……就像是父亲一样……"
    "确实，实际上我比你们要年长得多，"
    extend "\n但是还没到能被称为父亲的年龄。"
    extend "\n……难道我身上大叔味这么重吗……。"
    show tomo 18 with dissolve
    tomo "啊，我可没说你老哦！！"
    show tomo 23 with dissolve
    extend "\n只是，和你在一起的时候会很安心……。"
    "说到这里的时候，友的脸一下子涨红了。"
    show tomo 30 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tomo "啊，我在说什么啊！！"
    extend "\n抱歉，快忘掉吧！！！！！"
    show tomo 20 with dissolve
    extend "我、我也该吃饭了！！！"
    "友急忙把筷子伸向便当盒。"
    show tomo 28 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tomo "唔……咳！"
    extend "糟糕。\n噎、噎住了……！"
    me "你吃得太急了。"
    extend "来，喝口茶。"
    hide tomo with dissolve
    "我往友带来的水壶盖里倒了些茶水，递给了他。"
    "（咕嘟咕嘟……）"
    window hide
    show tomo 9 at top with dissolve
    window show
    tomo "噗哈……"
    extend "谢了。真是得救了。"
    me "真是的，友……你这家伙真是让人没办法啊。"
    show cg sky at center with dissolve
    tomo "……你看，就是这种地方。"
    "友低声自语。"
    me "嗯？"
    tomo "没、没什么！"
    "就这样，我和友两个人，享受了这段幸福的午餐时光。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    hide tomo with dissolve
    hide cg with dissolve
    return

label day3_2_sinobu:
    show bg school_building_morning at center with Radial(0.5)
    play sound "fx/chime.ogg"
    pause 0.4
    play music "quiet_lunch.ogg"
    window show
    "……呼。今天的课程也结束了。"
    extend "\n上午的时间真的好短啊。要是上班的话，现在才算正式开始呢。"
    show bg classroom with dissolve
    "那么，赶紧吃完午饭，开始委员的工作吧。"
    extend "\n正要起身去食堂的时候，忍站在了我身后。"
    window hide
    show sinobu 2 at top with dissolve
    window show
    sinobu "[player_name]，现在去吃午饭吗？"
    me "嗯，是啊。"
    extend "\n打算去食堂吃。"
    show sinobu 12 with dissolve
    sinobu "这样啊。"
    extend "\n……我可以跟你一起去吗？"
    me "当然可以！"
    extend "\n两个人一起吃也更开心嘛。"
    window hide
    hide sinobu with dissolve
    play sound "fx/sliding_door.ogg"
    show bg hallway with dissolve
    stop music fadeout 1.0
    pause 0.4
    show bg stairs with dissolve
    pause 0.4
    play music "fx/crowd_noise.ogg"
    show bg cafeteria with Dissolve(2.0)
    window show
    "来到热闹非凡的食堂，我扫视着上方的菜单。"
    me "真怀念呐~。"
    extend "\n呃……吃点什么好呢。"
    extend "\n我记得这家的蛋包荞麦面很好吃来着……。"
    window hide
    show sinobu 9 at top with dissolve
    window show
    sinobu "[player_name]原来喜欢蛋包荞麦面啊。"
    me "嗯？"
    extend "\n喜欢是喜欢，但是算不上最喜欢~。"
    show sinobu 8 with dissolve
    sinobu "那，最喜欢什么呢？"
    me "嗯~被你这么一问，我还真有点纠结啊……。"
    extend "\n嗯……先不考虑这个问题了！\n我们先点菜吧。"
    show sinobu 26 with dissolve
    sinobu "……那我也点蛋包荞麦面好了……。"
    window hide
    hide sinobu with dissolve
    window show
    me "嗯。"
    extend "\n阿姨！两份蛋包荞麦面！！"
    cafeteria_lady "收到！两份蛋包荞麦面——！"
    "听完点菜，阿姨一边利索地准备食材，\n一边有一搭没一搭地跟我们搭起话来。"
    cafeteria_lady "你们两个是新面孔啊。"
    extend "\n是一年级的吗？"
    me "啊……我们是二年级的，第一次来食堂吃饭……。"
    cafeteria_lady "这样啊。"
    extend "\n哎呀~毕竟像旁边这位同学，只要见过一次肯定就忘不了！"
    extend "\n没想到咱们学校里，还有长得这么像女孩的男孩子呀，真漂亮！"
    "说着，阿姨的目光落在了忍的身上。"
    stop music fadeout 2.0
    "这位阿姨简直就是在忍的雷区蹦迪啊！我吓得心都提到了嗓子眼，"
    extend "\n紧张地用余光偷瞄忍的反应。"
    window hide
    play music "sinobu_theme.ogg"
    show sinobu 21 at top with dissolve
    window show
    sinobu "……其实内在并没有很柔弱啦。"
    extend "\n阿姨，请给我换成大份的。"
    "忍微笑着说道。"
    cafeteria_lady "好！那我可就期待啦。"
    extend "\n正是长身体的时候呢……为了成为优秀的男子汉，可要多吃点哦！！"
    extend "\n你呢？"
    me "啊，那我也要大份的。"
    cafeteria_lady "嗯嗯！"
    extend "\n年轻的男孩子就该有这种气势！"
    hide bg with dissolve
    hide sinobu with dissolve
    "于是，我和忍接过了各自那份分量十足的蛋包荞麦面。"
    window hide
    show bg cafeteria at center with dissolve
    show sinobu 27 at top with dissolve
    window show
    sinobu "抱歉，就为了陪我……"
    extend "\n差价的部分我会付的。"
    me "不用这么客气啦！"
    extend "\n比起这个，阿姨刚才说的话，你真的不在意吗？"
    show sinobu 4 with dissolve
    sinobu "……说完全不在意那是骗人的，但我并不打算放在心上。"
    extend "\n总不能恶意揣测别人的好意。"
    me "这样啊。"
    show sinobu 21 with dissolve
    sinobu "嗯。"
    extend "\n……而且我觉得，外表和内在存在这种反差，倒也挺不错的。"
    "我惊讶地瞪大了眼睛。"
    extend "\n没想到忍会说这种话……！"
    show sinobu 26 with dissolve
    sinobu "……我们去结账吧。"
    me "好、好的。"
    hide bg with dissolve
    hide sinobu with dissolve
    "我跟着忍结了账，两人来到空位面对面坐了下来。"
    window hide
    show bg cafeteria at center with dissolve
    show sinobu 5 at top with dissolve
    window show
    sinobu "那么，刚才那个问题——你最喜欢吃的东西是什么？"
    me "嗯~我想想啊。\n我现在最喜欢的应该是荞麦面吧！"
    extend "\n乡下的那种手工荞麦面可好吃了~！↑"
    extend "\n最近我才慢慢体会到它的美味呢。"
    show sinobu 26 with dissolve
    sinobu "是这样啊。"
    extend "\n那，你喜欢看什么电视节目？"
    me "唔嗯……以前经常看深夜动画……"
    extend "\n不过最近也开始看大河剧了~。"
    show sinobu 21 with dissolve
    sinobu "这样啊。"
    sinobu "那，你平时会去哪里玩？"
    me "一般是去梅咲吧。"
    extend "\n正好公司也在那……诶，等等？"
    "这台词……简直和我昨天早上问忍的一模一样啊。"
    me "为什么今天突然问我这么多问题？"
    show sinobu 31 with dissolve
    sinobu "……因为我想更加了解[player_name]的事情。"
    me "诶？"
    show sinobu 18 with dissolve
    sinobu "[player_name]君一直在关注我，"
    extend "\n直到昨天我才终于意识到这一点……所以，我也变得想要深入了解[player_name]君了。"
    show sinobu 32 with dissolve
    extend "\n……这样会很奇怪吗？"
    "我不禁怀疑起自己的耳朵。"
    extend "\n这种话竟然能从忍的口中听见……！"
    "这是在做梦吗？不对，是梦中之梦吗！？"
    me "不不不，一点也不奇怪！！"
    extend "\n倒不如说，我很开心！"
    window hide
    show cg c36 at center with Radial(0.5)
    window show
    sinobu "……我也很开心哦。"
    extend "\n多亏了[player_name]君，我终于能稍微积极地看待自己的外貌了。"
    extend "\n谢谢你。"
    me "总觉得有点害羞呐……"
    extend "\n不、不用谢！"
    sinobu "……今天我带了《东斗神拳》前五卷，待会儿在教室交给你。"
    extend "\n在这里给的话，可能会被老师发现。"
    me "是吗~谢谢！"
    extend "\n下次一定好好聊聊剧情！"
    sinobu "嗯。"
    me "这份蛋包荞麦面，真的很好吃呢。"
    sinobu "嗯，很好吃。"
    extend "\n下次，我想去乡下吃荞麦面。"
    me "嗯！好呀！"
    extend "\n虽然价格稍微贵一点，但我知道一家很好吃的店！"
    extend "\n忍肯定能爱上那个味道的！"
    sinobu "……我很期待。"
    me "我也是！"
    extend "\n今天的忍，感觉格外积极呢。"
    sinobu "……偶尔也要这样嘛。"
    window hide
    hide sinobu with dissolve
    hide cg with dissolve
    window show
    "就这样，我与今天稍微有些不同的忍一起，\n充分享受了这顿幸福的午餐。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label day3_2_futago:
    show bg school_building_morning at center with Radial(0.5)
    play sound "fx/chime.ogg"
    pause 0.4
    play music "quiet_lunch.ogg"
    window show
    "……呼。今天的课程也结束了。"
    extend "\n上午的时间真的好短啊。要是上班的话，现在才算正式开始呢。"
    show bg classroom with dissolve
    stop music fadeout 2.0
    "那么，赶紧吃完午饭，开始委员的工作吧。"
    extend "\n正当我起身打算去食堂时，月和空提着手提篮朝我走了过来。"
    play music "twins_theme.ogg"
    show sora 1 at topright
    show tuki 9 at topleft with dissolve
    tuki "[player_surname]，现在是午饭时间吗？"
    sora "如果不介意的话，就和我们一起吃吧！"
    me "嗯？啊啊，可以啊。"
    extend "\n不过我本来打算去食堂买点吃的，没问题吗？"
    show sora 2 with dissolve
    sora "没那个必要哦，[player_name]君。"
    me "诶？什么意思？"
    show tuki 15 with dissolve
    tuki "昨天，佣人们吃了我们做的料理，大家都赞不绝口。\n他们非要表达谢意，所以特意为[player_surname]君做了便当。"
    window hide
    show cg c53 at center with Radial(0.5)
    window show
    "月这么说着，把和自己那盒便当不一样的\n另一盒便当从袋子里取了出来。"
    me "真的吗！？"
    extend "\n哇啊啊~！！好开心啊！\n谢谢你们特意带过来！！！"
    extend "\n我明明也没做什么……。"
    tuki "并非如此。"
    extend "\n如果当时没有[player_surname]君的建议，我们可能至今都无法察觉到自己的问题。"
    sora "而且，昨天大家聚在一起热热闹闹的，真的很开心！"
    me "是、是吗……"
    extend "\n那就太好了。"
    tuki "啊啊，以后也请务必再来玩。"
    sora "那么，把桌子拼在一起，大家一起开动吧！"
    window hide
    hide cg with dissolve
    hide tuki with dissolve
    hide sora with dissolve
    window show
    "大家把各自的桌椅拉了过来，然后打开了便当盒。"
    me "嗯嗯~好香啊！！"
    extend "\n那我就不客气了！！"
    "（大口嚼）"
    play sound "fx/sparkle.ogg"
    show cg adult at center with Radial(0.5)
    "嗯，好好吃！！！"
    extend "\n真不愧是每天在那种豪宅里掌勺的大厨手艺……。"
    "在各种专业级的配菜之中，我注意到了一块略显笨拙的鸡蛋烧。"
    window hide
    hide cg with dissolve
    hide sora with dissolve
    hide tuki with dissolve
    window show
    me "嗯？这个鸡蛋烧……好像稍微有点咸呢。"
    return

label day3_2_sintarou:
    show bg school_building_morning at center with Radial(0.5)
    play sound "fx/chime.ogg"
    pause 0.4
    play music "quiet_lunch.ogg"
    window show
    "……呼。今天的课程也结束了。"
    extend "\n上午的时间真的好短啊。要是上班的话，现在才算正式开始呢。"
    show bg classroom with dissolve
    "那么，赶紧吃完午饭，开始委员的工作吧。"
    extend "\n正当我起身打算去食堂时，慎太郎提着一个塑料袋凑了过来。"
    window hide
    show sintarou 8 at top with dissolve
    window show
    sintarou "[player_name]酱~"
    extend "\n我们一起吃午饭吧~！"
    me "嗯？啊啊，可以啊。"
    extend "\n不过我打算去食堂吃，没问题吧？"
    show sintarou 31 with dissolve
    sintarou "OK。"
    show sintarou 13 with dissolve
    extend "\n啊，不用带钱也没关系哦！"
    me "诶？为什么？"
    extend "\n你要请客嘛？？"
    show sintarou 12 with dissolve
    sintarou "诶~你都这把年纪的人了，还好意思跟小孩子计较这点钱吗~？"
    me "诶？不、不是……可是你刚才不是说不用钱吗……。"
    show sintarou 13 with dissolve
    sintarou "不要在意这种细节~。"
    me "……？"
    extend "\n慎太郎你带了便当吗？"
    "我盯着他手里的塑料袋问道。"
    show sintarou 4 with dissolve
    sintarou "嗯哼哼。"
    extend "\n到食堂之前，这是秘密！"
    show sintarou 2 with dissolve
    extend "\n总之，走啦走啦！！"
    hide sintarou with dissolve
    "我就这样被慎太郎拉着，朝食堂走去。"
    window hide
    stop music fadeout 0.5
    play sound "fx/running.ogg"
    show bg hallway with dissolve
    pause 0.4
    show bg stairs with dissolve
    pause 0.4
    play music "fx/crowd_noise.ogg"
    show bg cafeteria with Dissolve(2.0)
    window show
    me "我真的没带钱哦。"
    extend "\n没关系吗？"
    window hide
    show sintarou 4 at top with dissolve
    window show
    sintarou "没事没事！"
    "慎太郎边说边从塑料袋里拿出一个食盒，\n然后打开了盖子。"
    play sound "fx/tadaa.ogg"
    show cg remarkable at center with dissolve
    sintarou "锵锵——！！！"
    extend "\n怎么样！我把我家食堂里各种菜色都塞进去了，\n这是专门为[player_name]酱制作的特供便当哦~！！"
    "盒子里整齐地摆放着琳琅满目的配菜。"
    me "真的吗！！？"
    extend "\n哇啊啊啊啊啊！！！太开心了！！！"
    stop music fadeout 2.0
    "虽说本就是他家食堂的菜单，但这是慎太郎大清早拼命制作的便当！"
    extend "\n怎么可能不开心呢！！"
    window hide
    hide cg with dissolve
    hide sintarou with dissolve
    play music "sintarou_theme.ogg"
    show sintarou 30 at top with dissolve
    window show
    sintarou "因为前天说了不让你来澡堂，"
    extend "\n昨天又因为回来得太晚没顾上，"
    extend "\n所以至少想让你尝尝我家的菜色呐。"
    me "是、是特意为了我……！"
    extend "\n谢谢你，慎太郎！！！"
    extend "\n真是的，你也太可爱了吧~！你这小家伙♪"
    "我揉起了慎太郎的脑袋。"
    $ renpy.transition(Quake(60, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    show sintarou 32 with dissolve
    sintarou "[player_name]酱！在、在这种地方做这种事太羞耻了啦……"
    "慎太郎的脸蛋微微泛红，有些局促地低头说道。"
    extend "\n好想把你也吃掉啊，慎太郎！！！！！"
    me "那我就不客气，赶紧开动啦！！"
    "我从食盒里夹起一颗裹满芡汁的肉丸送入口中。"
    "啊呜~"
    show sintarou 4 with dissolve
    sintarou "怎么样？"
    extend "\n我家食堂的菜很不错吧？"
    me "嗯，好吃！！！"
    extend "\n真没想到澡堂里竟然能做出这么美味的饭菜！"
    extend "\n这水准绝对比外面的普通餐厅高出好几个档次啊！！"
    show sintarou 13 with dissolve
    sintarou "对吧~。"
    extend "\n呐，你就尽情享受吧！"
    extend "\n我稍微离开一下哦~。"
    me "嗯？你要去哪儿？"
    show sintarou 4 with dissolve
    sintarou "去把这个加热一下。"
    "说着，慎太郎拿着一个小包装盒走进了食堂后厨。"
    play sound "fx/running.ogg"
    hide sintarou with dissolve
    extend "\n难道还有什么好菜要上吗？"
    "我正毫不客气地吃着，慎太郎很快就回来了。"
    window hide
    play sound "fx/running.ogg"
    show cg c27 at center with Radial(0.5)
    window show
    sintarou "久等了~！"
    extend "\n给！\n热乎乎的关东煮来喽。"
    "揭开包装盖，在腾起的阵阵热气中，竹轮和鸡蛋若隐若现。"
    me "还特意去加热了啊！"
    # show sintarou 3 at top with dissolve
    sintarou "凉掉的关东煮那还能叫关东煮嘛~。"
    # show sintarou 31 with dissolve
    extend "\n来，趁热吃吧。\n我对我家的关东煮的味道可是很有自信的哦~！"
    me "还有比之前的菜更有自信的作品啊……"
    extend "\n那么，这一份我也开动啦！"
    window hide
    hide cg with dissolve
    # hide sintarou with dissolve
    window show
    "呼——呼……（大口嚼）"
    play sound "fx/cute2.ogg"
    me "好好吃！！！真的太好吃了，慎太郎！！"
    show cg orange at center with dissolve
    play sound "fx/sparkle.ogg"
    "简直太美味了啊啊啊啊啊！！"
    extend "\n高汤充分浸透到了食材里，\n浓郁的咸鲜味也完全符合我的口味！"
    me "太好吃了！！"
    extend "\n我都想拜托你爸爸妈妈把秘方传授给我了！"
    window hide
    hide cg with dissolve
    show sintarou 20 at top with dissolve
    window show
    sintarou "哼哼♪是吧是吧！"
    show sintarou 9 with dissolve
    extend "\n这道关东煮，可是咱亲手做的哦~！！"
    extend "\n我可是搜了又搜、查了很多攻略，\n最后才总算研究出这个味道的呢！！"
    me "这竟然是你一个人完成的！！？"
    me "……好厉害啊，慎太郎。"
    extend "\n明明只是这个年纪，不仅能在店里帮忙，还会自己钻研厨艺。\n这种向上心和干劲真的很了不起。"
    extend "\n跟我初中那时候相比简直是天上地下啊。"
    show sintarou 30 with dissolve
    sintarou "能得到你的夸奖，咱深感荣幸。"
    show sintarou 4 with dissolve
    extend "\n不过，比起每天都要跑去梅咲，\n在那儿拼命工作的[player_name]酱，咱这点努力根本不算什么啦。"
    me "不不不，那是因为我已经是大人了……"
    extend "\n诶？"
    show sintarou 33 with dissolve
    sintarou "哼哼♪\n我不是说过嘛，[player_name]酱说的话，我可是全都相信的哦。"
    show sintarou 34 with dissolve
    extend "\n所以，[player_name]酱，也要加油呀！"
    me "慎太郎……。"
    "慎太郎轻描淡写的一句话，却让我的胸口一阵发热。"
    me "嗯。\n我会努力的。"
    hide sintarou with dissolve
    "多亏了慎太郎，我尽情享受了一段无比幸福且充满力量的午餐时光。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label day3_2_tubasa:
    show bg school_building_morning at center with Radial(0.5)
    play sound "fx/chime.ogg"
    pause 0.4
    play music "quiet_lunch.ogg"
    window show
    "……呼。今天的课程也结束了。"
    extend "\n上午的时间真的好短啊。要是上班的话，现在才算正式开始呢。"
    "那么，赶紧吃完午饭，开始委员的工作吧。"
    play sound "fx/sliding_door.ogg"
    show bg hallway with dissolve
    stop music fadeout 2.0
    extend "\n我正打算去食堂，刚走出教室，翼便叫住了我。"
    window hide
    play sound "fx/running.ogg"
    show tubasa 9 at top with dissolve
    play music "tubasa_theme.ogg"
    window show
    tubasa "那、那个……[player_name]君。"
    me "嗯，怎么了？"
    show tubasa 2 with dissolve
    tubasa "你现在是要去吃午饭吗？"
    me "嗯。"
    show tubasa 22 with dissolve
    tubasa "那个……呃……。"
    me "……？"
    show tubasa 1 with dissolve
    tubasa "……。"
    me "……翼君也要一起去吃午饭吗？"
    extend "\n又想找我商量事情吧？"
    show tubasa 13 with dissolve
    tubasa "啊？啊……嗯、嗯！"
    show tubasa 4 with dissolve
    extend "\n要是你还愿意听我说的话，我会很高兴的……"
    "翼看起来很害羞，扭扭捏捏地说着。"
    "啊啊真是的！他真是可爱极了！！"
    extend "\n我不由自主就想保护他……。"
    "我一边压住因翼的举止而变得兴奋的情绪，一边朝食堂走去。"
    window hide
    hide tubasa with dissolve
    hide bg with dissolve
    stop music fadeout 0.5
    show bg stairs at center with dissolve
    pause 0.4
    play music "fx/crowd_noise.ogg"
    show bg cafeteria with Dissolve(2.0)
    window show
    "我们点好餐，结账，然后面对面地坐了下来。"
    show tubasa 31 at top with dissolve
    tubasa "你、你看昨晚的《小鬼使》了吗？"
    me "啊？哦，看了看了。"
    extend "\n昨晚是盲猜系列那一集吧！\n每次今崎的反应都很有趣啊！"
    show tubasa 4 with dissolve
    tubasa "是啊。\n我对コキリコ那两位的印象最深刻。\n（注：『コキリコ』影射ココリコ，是《小鬼使》中的常驻组合）"
    show tubasa 5 with dissolve
    extend "\n舔一下蛋黄酱就能猜出品牌，这种事真的能做到吗？\n如果是我，恐怕一开始就会猜错。"
    me "我也肯定不行。\n舌头没有那么灵敏。"
    extend "\n那几位也是啊，每次被打屁股，还能继续猜，真够拼的。"
    show tubasa 18 with dissolve
    $ renpy.transition(Quake(0, 65, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    tubasa "嘟嘟嗯！\n[player_name]君，出局！"
    play sound "fx/boing.ogg"
    me "诶？\n突、突然怎么了？"
    stop music fadeout 2.0
    show tubasa 19 with dissolve
    tubasa "那个……那个……其实只是，"
    extend "\n想稍微模仿一下试试……而已。"
    "鼓起勇气却冷场了的翼，非常害羞地说道。"
    play music "tubasa_theme.ogg"
    play sound "fx/sparkle.ogg"
    "糟糕……太可爱了……！！\n这孩子到底怎么回事啊啊啊啊啊啊啊啊！！"
    extend "\n午饭什么的已经无所谓了……。"
    extend "\n好想吃掉他！好想把他带回家！！！"
    show tubasa 5 with dissolve
    tubasa "啊……虽然是不同类型的节目，\n今晚还有《三文鱼宫殿》哦。"
    extend "\n我也很喜欢这个节目……。"
    "嗯……？话说回来，翼今天话还真多。"
    extend "\n而且，谈论的不是关于友的事，全是综艺节目的话题……。"
    me "翼君，你今天感觉挺有精神的呢。"
    extend "\n发生什么事了？"
    show tubasa 23 with dissolve
    tubasa "诶？不……没什么……和平常一样哦。"
    me "是吗。"
    extend "\n总感觉，和平时的样子不太一样呢……。"
    show tubasa 37 with dissolve
    tubasa "……因为一直都在和[player_name]君聊友君的事，所以我在想，偶尔也想像这样聊聊普通的话题……。"
    show tubasa 22 with dissolve
    extend "\n而、而且，总让你听我发牢骚也不太好……。"
    extend "\n果然……还是很奇怪吗？"
    me "不、不是，一点也不奇怪哦！！"
    extend "\n……但是，你看，难得有两人独处的机会，\n为了翼的恋情修成正果，不聊聊这个话题怎么行！"
    stop music fadeout 2.0
    show tubasa 15 with dissolve
    tubasa "诶……。"
    extend "\n好、好的。也是呢……。"
    "翼露出有些寂寞的表情，说道。"
    "……我也很想和他聊些愉快的闲话，多看看他的笑容。"
    "但是，感觉这么一来，我就没法再真心实意地去为他的恋情加油了……。"
    me "说、说起来，你和友君成为朋友的契机是什么呢？"
    show tubasa 13 with dissolve
    tubasa "啊，那个……我是二年二班的班长，友君是一班的班长。"
    extend "\n在二年级刚开学第一次集合的时候，他主动向我搭了话。"
    window hide
    play music "reminiscence.ogg"
    show cg c44 at center with FadeWhite(1.5)
    window show
    tomo "哟~！你是哪个班的？我是一班的。"
    tubasa "诶……那、那个……。"
    tomo "我叫森海友！\n是二年一班的班长！今后请多指教啦！"
    extend "\n呐，你是几班的？叫什么名字？"
    tubasa "那个……我是二班的。"
    extend "\n我叫一之濑翼。"
    tomo "啊~一之濑同学吗！\n去年体育课打手球的时候，我听到老师叫你了！"
    extend "\n那时你好像被批评了啊~。\n发生什么事了吗？"
    tubasa "手、手球……啊啊。"
    extend "\n那时，老师说我干劲不足所以批评我了……。"
    extend "\n我不擅长运动，就躲在场边……。"
    tomo "这样啊这样啊！\n我也不擅长运动啊~。"
    extend "\n不过学习也不擅长就是了！"
    tubasa "我、我也一样……。"
    extend "\n不过友君的性格和我完全相反，感觉很开朗呢。"
    tomo "没那回事啦！\n我们是一样的！"
    "友君当时就像对待老熟人一样，亲切地和我聊着。"
    "或许对有些人来说，这种做法会显得有些自来熟，"
    extend "\n但是对消极的我来说，他这种积极的引导反而让我感到很舒服，让我十分感激。"
    window hide
    hide cg with FadeWhite(1.5)
    hide tubasa with FadeWhite(1.5)
    window show
    me "原来如此。"
    extend "\n所以，在相处的过程中逐渐被他吸引，"
    extend "\n慢慢产生了超越友情的情感吧。"
    window hide
    show tubasa 35 at top with dissolve
    window show
    tubasa "……是、是的……。"
    "如果只是积极引导的话，我也能……。"
    "不，但是，我和翼在一起的时间并不长。"
    extend "\n翼是因为长时间的积累才喜欢上友的……。"
    "我对着如此喜欢着友的翼说道："
    stop music fadeout 2.0
    me "……我会支持你的哦。"
    "连我自己都对这个声音感到惊讶。它和我脑中的想法完全不同，听起来也很单薄。"
    show tubasa 23 with dissolve
    tubasa "[player_name]君……。"
    me "诶……什、什么事？"
    show tubasa 15 with dissolve
    tubasa "……不，没什么。"
    hide tubasa with dissolve
    "就这样，我和翼两个人一边感受着共处的喜悦，\n一边怀着复杂的心情，度过了这段午餐时光。"
    window hide
    hide bg with dissolve
    return

label day3_2_saburo:
    show bg school_building_morning at center with Radial(0.5)
    play sound "fx/chime.ogg"
    pause 0.4
    play music "quiet_lunch.ogg"
    window show
    "……呼。今天的课程也结束了。"
    extend "\n上午的时间真的好短啊。要是上班的话，现在才算正式开始呢。"
    "那么，赶紧吃完午饭，开始委员的工作吧。"
    play sound "fx/sliding_door.ogg"
    stop music fadeout 2.0
    show bg hallway with dissolve
    extend "\n我正打算去食堂，刚走出教室，三朗便凑了上来。"
    window hide
    play sound "fx/running.ogg"
    show saburo 5 at top with dissolve
    play music "saburo_theme.ogg"
    window show
    saburo "啊，[player_surname]。"
    extend "\n来得正好，\n要不要一起去吃饭？"
    me "啊，当然可以了！"
    extend "\n我没带便当，正打算去食堂呢，没问题吗？"
    saburo "没那个必要啦♪"
    window hide
    show cg c70 at center with Radial(0.5)
    window show
    "说着，三朗得意地显摆了一下手里拎着的塑料袋。"
    saburo "我先在食堂里把[player_surname]的饭菜也买好啦！"
    me "诶……这怎么好意思，让你特意费心了。"
    extend "\n花了多少钱？"
    saburo "没事啦！\n今天由我请客！"
    me "可、可是……。"
    saburo "好啦好啦，今天你就乖乖让我请这一回吧！"
    extend "\n毕竟你昨天在人行道上救了我一命，对我有恩呢！\n而且你昨天还请我们去咖啡店喝咖啡。"
    extend "\n还有……就是，你还愿意耐心地听我发牢骚。"
    me "……好吧。"
    extend "\n那我就恭敬不如从命，谢谢款待了。"
    saburo "啊哈哈。\n你在这种地方还真是挺周到的啊~。"
    extend "\n去屋顶吧，我们去那里吃！\n好嘞，走吧~！"
    "就这样，我们朝着屋顶出发了。"
    window hide
    hide saburo with dissolve
    hide cg with dissolve
    hide bg with dissolve
    show bg stairs with dissolve
    stop music fadeout 0.4
    pause 0.5
    play music "tsubame.ogg"
    show bg rooftop with Radial(1.4)
    show saburo 2 at top with dissolve
    window show
    saburo "嗯~……！"
    extend "\n果然，比起待在教学楼里，还是出来透透气更舒服啊~。"
    "到了屋顶后，三朗一边伸懒腰一边说道。"
    me "前天也是这样呢，三朗君很喜欢屋顶吗？"
    show saburo 10 with dissolve
    saburo "超喜欢的！"
    extend "\n一边晒着太阳，一边暖烘烘地睡个午觉，\n真的是太爽了~。"
    "哈哈，简直就像只猫一样呢。"
    show saburo 1 with dissolve
    saburo "那就坐到长凳上吃吧！"
    window hide
    stop music fadeout 0.5
    show cg sky at center with Dissolve(0.8)
    play music "saburo_theme.ogg"
    window show
    saburo "来，这是你的，这是我的！"
    "说着，三朗将一份便当递到了我的手中。"
    me "嗯……？"
    extend "\n这不是食堂里份量最大、也是最贵的『超大份炸鸡便当EX』吗！！！"
    extend "\n真、真的可以不用把钱付给你吗？"
    "看着另一边的三朗正准备吃的只是一份普通的炒面便当，\n这样的落差让我即便心怀感激，也有些难以下嘴。"
    window hide
    hide cg with dissolve
    hide saburo with dissolve
    show saburo 2 at top with dissolve
    window show
    saburo "不用不用！不用在意。"
    extend "\n那么，我开动咯——！！"
    "说完，三朗便吃起了炒面。"
    hide saburo with dissolve
    extend "\n然而，嘴上虽然逞强，炸鸡那股毫不留情的香味却还是不断地诱惑着他。"
    extend "\n似乎难以彻底抗拒那份诱惑，他还是用余光看了看我手中的便当。"
    me "……三朗君，来！给你吃。"
    "看着这样的三朗，我用筷子夹起了一块炸鸡，递到了他的面前。"
    window hide
    show saburo 24 at top with dissolve
    window show
    saburo "诶……真、真的可以吗？"
    me "反正还有很多呢。"
    extend "\n况且这可是你请客买的，分你一块完全没关系啦。"
    show saburo 1 with dissolve
    saburo "是吗……？\n既然[player_surname]君都这么说了，那我就恭敬不如从命啦……！"
    extend "\n那，就放这儿吧。"
    "三朗把炒面往旁边拨了拨，腾出了一个空位。"
    me "嗯？"
    extend "机会难得，那就让我喂给你吃吧。"
    show saburo 3 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    saburo "啊！！"
    extend "你、你在说什么呢！！！"
    me "只有这样才能吃到这块炸鸡哦~。"
    extend "\n你就乖乖接受我的这份好意嘛~。"
    show saburo 8 with dissolve
    saburo "呜咕……！！"
    "三朗似乎在眼前的炸鸡和羞耻心之间挣扎着，\n"
    show cg light-blue at center with dissolve
    "但过了一会儿，他还是红着脸转向我，张开嘴，闭上了眼睛。"
    saburo "好啦！！这样就行了吧！快给我！"
    me "OK♪"
    "呵呵……年轻男孩子果然抵抗不了肉类的诱惑啊！"
    play sound "fx/sparkle.ogg"
    extend "\n你那露出的虎牙也真可爱啊，三朗酱！！！"
    me "好，啊——嗯！"
    "啊呜~"
    "（嚼嚼）"
    window hide
    hide cg with dissolve
    hide saburo with dissolve
    show saburo 5 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    window show
    saburo "呜哦……好好吃！！！！"
    extend "\n以前总看到别人吃得那么香，\n果然这炸鸡多汁又好吃啊！！"
    extend "\n以后等手头宽裕了，我也要买来吃~！"
    me "啊哈哈。\n能让你达成炸鸡初体验的心愿真是太好了。"
    show saburo 10 with dissolve
    saburo "确实啊~！"
    extend "\n谢啦，[player_surname]。"
    me "不客气不客气。"
    show saburo 24 with dissolve
    saburo "……啊，对了！\n忘了把喝的拿出来了。"
    "这样说着，三朗在塑料袋里哗啦哗啦地翻找了一阵，取出了一瓶乌龙茶。"
    hide saburo with dissolve
    window hide
    show saburo 16 at top with dissolve
    window show
    saburo "啊……抱歉，[player_surname]。\n喝的我就只买了这一瓶。"
    extend "\n我已经没钱了……所以饮料就分着喝，可以吗？"
    "诶，那不就是……和男孩子间接接吻的机会！？！？"
    play sound "fx/eureka.ogg"
    show cg remarkable at center with Dissolve(0.2)
    extend "\n来了……终于来了……这是命运的高塔在召唤我啊！！！"
    "三朗酱！！\n务必请你在喝的时候，在瓶口留下你的唾液吧！！！"
    extend "\n剩下的部分，就由我帮你舔干净哦哦哦……！！"
    window hide
    hide cg with Dissolve(0.2)
    hide saburo with Dissolve(0.2)
    window show
    me "完、完全没关系的！！"
    extend "不如说，谢谢你分给我！"
    show saburo 1 at top with dissolve
    saburo "噢。"
    extend "\n那我就先喝啦……。"
    hide saburo with dissolve
    "（咕噜咕噜）"
    "我目不转睛地盯着三朗，\n确认他的嘴唇紧贴着瓶口，把乌龙茶喝了下去。"
    window hide
    show saburo 5 at top with dissolve
    window show
    saburo "给……喂，[player_surname]。"
    show saburo 6 with dissolve
    extend "\n你盯着我看什么啊……。"
    extend "\n你已经这么渴了吗？"
    me "啊……嘛、嘛，是啊！"
    hide saburo with dissolve
    "我盯着三朗递来的水。"
    extend "\n这可是三朗喝过、里面绝对混入了他的成分的神圣茶水……我就心怀感激地收下了！！！"
    "（咕噜咕噜咕噜咕噜）"
    play sound "fx/explosion2.ogg"
    show cg remarkable at center with Dissolve(0.2)
    me "好喝！！"
    extend "\n三朗茶最棒了！！"
    window hide
    hide cg with dissolve
    show saburo 8 at top with dissolve
    window show
    saburo "哈、哈啊？\n你到底在说什么啊？"
    extend "\n话说，你这家伙是不是喝得也太多了点~？"
    me "不，没什么~一想到是和三朗君间接接吻，就不知不觉……。"
    show saburo 3 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    saburo "！？！？！"
    extend "\n啊，笨蛋！！！！你在胡说什么呢！！！！！"
    extend "\n还、还说间接接吻什么的……你这家伙……！！"
    "听到我的话，三朗突然慌张起来。"
    "啊，这种地方真的很可爱呢~♪"
    hide saburo with dissolve
    window hide
    show saburo 26 at top with dissolve
    stop music fadeout 2.0
    window show
    saburo "……说起来，昨天你给我看的本子里的图，\n也有两个男人接吻来着……。"
    me "诶。"
    extend "\n啊、啊哈~是这样吗……？"
    "听到三朗突然压低声音小声嘟囔，我顿时慌了神，赶紧又灌了一口乌龙茶。"
    play music "good_atmosphere.ogg"
    show saburo 28 with dissolve
    saburo "……[player_surname]……那个……"
    extend "\n和男人，接吻之类的……那种事，做过了吗？"
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.1), layer='master')
    me "噗——！！！"
    "突如其来的直球提问让我把刚喝的茶喷了出来。"
    show saburo 12 with dissolve
    saburo "你这家伙，弄得好脏啊！！"
    extend "\n搞什么嘛……。"
    me "咳咳……还不是因为三朗君突然问这种问题……。"
    extend "\n咳……吓了我一跳……。"
    show saburo 16 with dissolve
    saburo "因、因为我很在意啊，这也没办法吧！"
    extend "\n……所以呢，到底怎么样？做过吗……。"
    me "没有……唔，算是有过吧……。"
    show saburo 23 with dissolve
    saburo "嗯~……那，感觉怎么样？"
    me "诶！？？感、感觉……"
    extend "\n啊……挺舒服的……吧。"
    show saburo 26 with dissolve
    saburo "嘿……原来两个男人之间也会觉得舒服啊。"
    me "那当然了。"
    extend "\n只要有爱，无论对方是谁，都会很舒服很幸福的~！"
    show saburo 18 with dissolve
    saburo "只要有爱……吗。"
    extend "\n那是不是说，性别什么的就无所谓了？"
    me "当然。"
    extend "\n爱与性别，年龄，身份都没有关系哦。"
    show saburo 16 with dissolve
    saburo "……是这样吗……。"
    me "三朗君，对这方面的事情还是有些纠结呢。"
    show saburo 17 with dissolve
    saburo "算是吧……。"
    me "其实，自己究竟是异性恋还是同性恋，都无所谓，\n也没必要急着去下定义。"
    extend "\n我觉得真正重要的是，当你喜欢上一个人的时候，\n无论对方是谁，你是否能正视自己的那份心情。"
    show saburo 29 with dissolve
    saburo "正视自己吗……你这家伙，竟然能说出这么深刻的话啊。"
    extend "\n我也觉得这是很重要的……。"
    show saburo 30 with dissolve
    extend "\n听了你这番话，心里一下子轻松不少。"
    extend "\n谢谢。"
    me "不用谢！"
    extend "\n不过，我觉得像这样努力尝试去理解这些复杂问题的三朗君，也非常了不起哦。"
    "我这么说着，摸了摸三朗的头。"
    show saburo 33 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    saburo "白、白痴！快住手啦……！！"
    extend "\n好不容易打理好的发型，要被你弄乱了啦！"
    "三朗这么说着，脸上却是一副幸福的表情……\n是我的错觉吗……。"
    show cg sky at center with dissolve
    extend "\n就这样，我与三朗一起，尽情享受了这段极其幸福的午餐时光。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    hide saburo with dissolve
    hide cg with dissolve
    return

label day3_2_sakuya:
    show bg school_building_morning at center with Radial(0.5)
    play sound "fx/chime.ogg"
    pause 0.4
    play music "quiet_lunch.ogg"
    window show
    "……呼。今天的课程也结束了。"
    extend "\n上午的时间真的好短啊。要是上班的话，现在才算正式开始呢。"
    "那么，赶紧吃完午饭，开始委员的工作吧。"
    play sound "fx/sliding_door.ogg"
    stop music fadeout 2.0
    show bg hallway with dissolve
    "正当我走出教室准备去食堂时，作哉向我搭话了。"
    window hide
    show sakuya 6 at top with dissolve
    play music "sakuya_theme.ogg"
    window show
    sakuya "喂。"
    me "啊，是作哉君。"
    extend "\n怎么了？"
    show sakuya 10 with dissolve
    sakuya "……。"
    me "……。"
    show sakuya 32 with dissolve
    sakuya "……。"
    me "……"
    extend "？"
    show sakuya 12 with dissolve
    sakuya "没、没什么事。再见！！"
    play sound "fx/running.ogg"
    hide sakuya with dissolve
    play sound "fx/boing.ogg"
    me "诶诶！？"
    extend "\n等等……等一下！！"
    "我连忙叫住已经转身要走的作哉。"
    "你绝对是有事才来找我的吧！？"
    extend "\n就这样直接走掉的话，我完全搞不懂你在想什么啊！"
    window hide
    show sakuya 10 at top with dissolve
    window show
    sakuya "……嗯？"
    "既然如此，只能出此下策了……。"
    me "那、那个，我准备去吃午饭了！"
    extend "\n方便的话，作哉君要不要和我一起？"
    show sakuya 4 with dissolve
    sakuya "哈、哈啊？"
    extend "\n和你这家伙一起……"
    me "好啦好啦！！"
    extend "\n反正我们平时不也是一起照顾小翼的嘛！"
    extend "\n边吃午饭边聊小翼的事，肯定能聊得很热闹的！！"
    show sakuya 32 with dissolve
    sakuya "……好、好吧，既然你这么坚持的话……。"
    "说完，作哉便向食堂走去。"
    "看他并没有回教室的意思，看来早就带够钱了。"
    extend "\n果然，他肯定是打算邀请我一起吃午饭。"
    play sound "fx/sparkle.ogg"
    show cg purple at center with FadeWhite(0.5)
    "哼哼哼……这家伙！！"
    extend "\n既然想邀请我，直说不就好了。"
    extend "\n不过，这也是他的魅力所在啊♪"
    "我一边压下因作哉那可爱性格而泛起的躁动，一边走向食堂。"
    window hide
    hide bg with dissolve
    hide sakuya with dissolve
    hide cg with dissolve
    stop music fadeout 0.5
    show bg stairs at center with dissolve
    pause 0.4
    play music "fx/crowd_noise.ogg"
    show bg cafeteria with Dissolve(2.0)
    window show
    me "嗯~我就点一份炸猪排咖喱吧~。"
    extend "\n作哉君吃什么？"
    stop music fadeout 0.5
    play music "sakuya_theme.ogg"
    show sakuya 24 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    sakuya "啥？要请我吃啊？"
    extend "\n那就多谢款待啦~♪"
    me "诶？不、不是想请你……"
    extend "\n算了，也可以吧。"
    show sakuya 11 with dissolve
    play sound "fx/boing.ogg"
    sakuya "真的吗！"
    show sakuya 1 with dissolve
    extend "\n……开玩笑的。"
    extend "\n我怎么可能让你请客啊。\n真是的，你这家伙一点幽默细胞都没有啊~。"
    me "哈、哈啊……。"
    "真搞不懂最近的年轻人……。"
    extend "\n不过，平时总是阴沉着脸像是在生谁气的作哉，竟然会开这种玩笑，\n是不是说明他已经对我放下了戒心，开始慢慢向我敞开心扉了呢？"
    "这么一想就觉得有些开心了。"
    show sakuya 5 with dissolve
    sakuya "嗯，那我就要蛋包饭吧。"
    "我们各自拿到点好的饭菜，结完账，\n面对面坐到座位上，开始吃了起来。"
    window hide
    hide sakuya with dissolve
    hide bg with dissolve
    show bg cafeteria at center with dissolve
    show sakuya 23 at top with dissolve
    window show
    sakuya "你点的炸猪排咖喱看起来好好吃啊！"
    extend "\n给我尝一口吧~。"
    "说着，作哉把盘子伸到我面前。"
    "没有拒绝权么……。"
    extend "这孩子真是……。"
    me "好好好，给你。"
    "我夹起一块炸猪排，放到作哉的盘子里。"
    show sakuya 24 with dissolve
    sakuya "谢啦！"
    me "那，我也可以尝一口你的蛋包饭吗？"
    show sakuya 4 with dissolve
    play sound "fx/boing.ogg"
    sakuya "诶——！"
    me "诶什么诶啊！！"
    extend "\n这种时候不都应该交换一下嘛！"
    show sakuya 14 with dissolve
    sakuya "你听说过『阿加佩』这个词吗？\n（注：Agape，意为基督教中指人与神的无私互爱，也用来特指一种与圣餐相关的共餐活动）"
    me "我不信基督教，不知道。"
    extend "\n不过我知道『礼尚往来』。"
    show sakuya 19 with dissolve
    sakuya "……切，真拿你没办法。"
    extend "\n给你。"
    hide sakuya with dissolve
    "作哉象征性地往我盘子里拨了那么一丁点儿蛋包饭。"
    window hide
    show sakuya 21 at top with dissolve
    window show
    sakuya "哼哼，心怀感激地收下吧。"
    me "啊，好的……"
    extend "\n真是不好意思，作哉先生……多谢您特意分给我这么珍贵的……"
    play sound "fx/dash.ogg"
    extend "\n……不对，喂！！凭什么只有我低声下气的啊！！\n咱俩地位明明是平等的吧！！"
    show sakuya 24 with dissolve
    sakuya "啊哈哈！！这吐槽接得漂亮！"
    extend "\n[player_surname]，你总算开始懂我的节奏了嘛~。"
    "说完，作哉开心地大笑起来。"
    "……啊，总觉得这种气氛……感觉其实还不错呢。"
    window hide
    show cg c79 at center with Radial(0.5)
    window show
    sakuya "干嘛？你还在笑啊？"
    me "没，只是觉得……。"
    extend "\n一想到和作哉君像这样当朋友，就不禁笑出来了。"
    sakuya "当朋友？？？"
    extend "\n那是，什么意思啊。"
    me "意思就是说，比起一开始，我们的关系已经变得很好了。"
    sakuya "是、是吗……？"
    me "是哦。"
    extend "\n刚开始那会儿，作哉君看起来一直闷闷不乐的，\n总给人一种在生谁的气的感觉，说实话还挺可怕的呢。"
    sakuya "你、你在胡说什么啊……"
    extend "\n我又没那么生气。"
    me "不不不，你就是生气了，特别明显。"
    extend "\n你身上一直散发着那种冷冰冰、满是倒刺的气场呢。"
    show cg purple with FadeWhite(0.5)
    play sound "fx/cute.ogg"
    sakuya "我才没有——"
    play sound "fx/cute2.ogg"
    me "你就是有——"
    show cg remarkable with Radial(0.5)
    play sound "fx/explosion1.ogg"
    sakuya "没——有——！"
    play sound "fx/explosion3.ogg"
    me "就——有——！"
    window hide
    hide cg with dissolve
    hide sakuya with dissolve
    show sakuya 21 at top with dissolve
    play sound "fx/eureka.ogg"
    window show
    sakuya "你再敢说我有，我就再拿一块炸猪排。"
    play sound "fx/boing.ogg"
    me "这、这也太卑鄙了！！"
    show sakuya 3 with dissolve
    sakuya "诶！哪里卑鄙了！！"
    extend "\n我可没有故意欺负你。\n来，跟着我念。"
    me "你……你生……"
    show sakuya 14 with dissolve
    sakuya "嗯~？"
    extend "\n接下来的话要是说错了，可是要牺牲掉一块猪排的哦？"
    "作哉坏笑着。"
    me "……你、你不是没在生气！"
    show sakuya 17 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sakuya "啊！？哇，你也太狡猾了吧！！"
    extend "\n那才叫卑鄙！！！"
    me "诶嘿~♪我可没有卑鄙！"
    "没想到，即使不聊关于小翼的话题，我们也能相处得这么融洽。"
    extend "\n无论多么无聊的对话，只要是和作哉在一起，我都会觉得非常快乐。"
    window hide
    hide sakuya with dissolve
    window show
    me "啊，说起来……不用给小翼喂食吗？"
    show sakuya 5 at top with dissolve
    sakuya "哦，狗狗的话，一天其实只要喂早晚两顿就行了。"
    extend "\n午饭的话，稍微喂一点零食就好。"
    me "这样啊。"
    extend "\n那等吃完午饭，我们就一起去喂它吧！"
    show sakuya 35 with dissolve
    sakuya "好。"
    hide sakuya with dissolve
    "就这样，我和作哉两个人一起，度过了愉快的午餐时光。"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    return

label day3_design:
    hide 班選択 with dissolve
    window show
    "去『服装制作组』看看吧！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "quiet_lunch.ogg"
    show sintarou 1 at topright with dissolve
    window show
    sintarou "小友。\n今天到底要做什么啊~？"
    extend "\n在周五服装到手前，闲着也没事做吧？"
    show tomo 7 at topleft with dissolve
    tomo "就是啊。"
    extend "\n预算也所剩不多了，要额外再买些东西也不太可能……。"
    show tomo 9
    show sintarou 16 with dissolve
    tomo_and_shin "嗯嗯……。"
    me "那么，做全员的名牌怎么样？"
    extend "\n要是做名牌的话，应该不会那么贵，\n只要有纸和笔就能做。"
    show sintarou 8 with dissolve
    sintarou "哦~！[player_name]酱，好主意~！！"
    show tomo 1 with dissolve
    tomo "嗯！不错啊。"
    extend "\n那么，马上开始作业吧！"
    extend "\n首先要去买板子。"
    show tomo 21 with dissolve
    extend "\n有在哪儿卖的吗？"
    show sintarou 15 with dissolve
    sintarou "在百元店里会有吧。"
    extend "\n不过，这附近有那种店吗？"
    me "那么，在网上买不就好了？"
    show tomo 28 with dissolve
    tomo "网上买……！！"
    show tomo 27 with dissolve
    extend "\n我说，小慎。\n我们昨天还特地跑到梅咲去买服装，\n那些网上有卖的……。"
    show sintarou 21 with dissolve
    stop music fadeout 0.5
    sintarou "友，友！ 不能再说下去了！！"
    play music "hurry_up.ogg"
    show tomo 30 with dissolve
    tomo "可，可是慎太郎酱！\n我们之前那么辛苦，真的有必要吗？"
    show cg c14 at center with zoominout
    play sound "fx/dash.ogg"
    sintarou "笨蛋！！"
    tomo "呜呜"
    window hide
    hide cg with dissolve
    hide sintarou with dissolve
    hide tomo with dissolve
    window show
    play sound "fx/triangle.ogg"
    "……这好像有什么事情要发生了呢。"
    show tomo 30 at topleft
    show sintarou 26 at topright with dissolve
    sintarou "这世上没有无用的东西！"
    extend "\n过去不是用来后悔的……而是用来吸取教训的！"
    show sintarou 24 with dissolve
    extend "\n所以，我们必须向前看，继续前进！！"
    show tomo 29 with dissolve
    tomo "慎，慎太郎酱……！"
    show sintarou 20 with dissolve
    sintarou "友酱！"
    show cg adult at center
    play sound "fx/sparkle.ogg"
    show tomo 13 with dissolve
    tomo "慎太郎酱……！"
    show sintarou 7 with dissolve
    sintarou "友酱！！！"
    me "好，卡！"
    extend "\n那么，接下来就去拍床戏吧！！"
    hide cg with dissolve
    show sintarou 9 with dissolve
    tomo_and_shin "[player_name]酱也一起来吗？"
    me "当然！！！"
    extend "\n我要把你们两个吃干抹净！！！"
    show tomo 25 with dissolve
    tomo "不要~！变态~！！"
    me "男人都有兽欲！"
    extend "\n不是吗，两位…。"
    show tomo 38 with dissolve
    tomo "呼……您说得是。"
    show sintarou 12 with dissolve
    sintarou "哎呀，你也有不对的地方啊…。"
    me "我可不像慎太郎大人那般…。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    show sakuya 11 at topleft with dissolve
    window show
    sakuya "喂，小不点儿。"
    extend "\n你不阻止那群蠢货吗？。"
    show sinobu 19 at topright with dissolve
    sinobu "……我已经不打算去阻止了…。"
    window hide
    hide sinobu with dissolve
    hide sakuya with dissolve
    show tubasa 14 at top with dissolve
    window show
    tubasa "……。"
    hide tubasa with dissolve
    show sakuya 6 at top with dissolve
    play sound "fx/boing.ogg"
    sakuya "唔……"
    hide sakuya with dissolve
    hide tubasa with dissolve
    show tubasa 14 at topright with dissolve
    show sakuya 9 at topleft with dissolve
    extend "\n2组的代表也别东张西望的，\n应该去商讨或者进行作业才是！"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    show tubasa 3 with dissolve
    tubasa "（抖）"
    "面对着一脸羡慕地注视着服装组的翼，\n作哉用带着刺儿的话语泼了他冷水。"
    show sakuya 2 with dissolve
    sakuya "喂，一～之～濑～！"
    show sakuya 8 with dissolve
    extend "\n你是和小不点儿同组的吧。"
    extend "\n如果不能集中注意力的话，就去远一点的地方干活去。"
    show tubasa 7 with dissolve
    $ renpy.transition(Quake(60, 0, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tubasa "好痛痛痛……别，别再拉我了啦~。"
    show sakuya 12 with dissolve
    sakuya "……。"
    "一脸无奈的作哉强行拉着哭哭啼啼的翼走了。"
    stop music fadeout 1.0
    extend "\n那两人，说不定关系还不错呢。"
    window hide
    hide sakuya with dissolve
    hide sinobu with dissolve
    hide tubasa with dissolve
    play music "quiet_lunch.ogg"
    window show
    me "好。那我们也开始做自己能做的事吧。"
    extend "\n先把那块板子放下，先做个名牌吧"
    show tomo 1 at topleft with dissolve
    tomo "啊，老师说有剩余的画纸。"
    "我顺着友的指向看去，的确还有几张图画纸。"
    me "嗯。\n有这些应该足够了吧。"
    show tomo 12 with dissolve
    tomo "是吗！"
    extend "\n那么接下来就用美工刀和剪刀裁剪成合适大小的……"
    show tomo 21 with dissolve
    extend "\n啊，不过，到底要裁成什么尺寸才好呢？"
    show sintarou 2 at topright with dissolve
    sintarou "我家澡堂就有名牌\n照着那个裁不就好了吗？"
    show tomo 4 with dissolve
    tomo "小慎真是聪明！"
    extend "\n那么，嚓嚓嚓嚓嚓嚓~♪"
    "那么，从哪个颜色开始剪呢。"
    hide sintarou with dissolve
    hide tomo with dissolve
    return

label day3_layout:
    hide 班選択 with dissolve
    window show
    "去『布置组』看看吧！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "quiet_lunch.ogg"
    window show
    show sinobu 25 at topleft with dissolve
    sinobu "那我们今天先分头进行吧。"
    extend "\n我现在去老师那里，\n把用作咖啡店的教室给定下来。"
    show tubasa 5 at topright with dissolve
    tubasa "好的。"
    extend "\n那我就根据之前去过那家咖啡厅，构思一下内部构造。"
    show sinobu 26 with dissolve
    sinobu "嗯。"
    "那个，我……"
    hide sinobu with dissolve
    hide tubasa with dissolve
    return

label day3_cooking:
    hide 班選択 with dissolve
    window show
    "去『料理组』看看吧！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "quiet_lunch.ogg"
    show tuki 2 at topleft with dissolve
    window show
    tuki "昨天，菜单基本就定下来了，"
    extend "\n今天就在烹饪室来练习烹饪吧。"
    show sora 2 at topright with dissolve
    sora "食材因为昨天还剩了一些，所以能练习好几次哦。"
    extend "\n现在先把料理做熟练了，之后再教给大家吧。"
    show tuki 9 with dissolve
    tuki "我知道了。"
    extend "\n那么，那就马上前往烹饪室吧。"
    window hide
    hide tuki with dissolve
    hide sora with dissolve
    hide bg with dissolve
    play sound "fx/sliding_door.ogg"
    show bg home_economics_room with Dissolve(0.8)
    window show
    "进入烹饪室后，里面已经有很多班级在练习烹饪了。"
    show tuki 1 at topleft with dissolve
    tuki "我先预留了最里面的位置的桌子，就在那边做吧。"
    show sora 1 at topright with dissolve
    sora "太好了~。"
    extend "\n昨天因为人太多了所以没能使用呢。"
    show tuki 9 with dissolve
    tuki "好，我去把餐具拿过来。"
    show sora 2 with dissolve
    sora "好的。"
    extend "\n我来把材料准备好。"
    me "那我就去把冰淇淋啊，肉啊什么的放到冰箱里去吧"
    window hide
    stop music fadeout 0.5
    hide tuki with dissolve
    hide sora with dissolve
    hide bg with dissolve
    show bg home_economics_room at center with Dissolve(0.8)
    play music "cute_silly.ogg"
    show tuki 6 at top with dissolve
    window show
    tuki "好，准备好了。"
    show tuki 5 with dissolve
    extend "\n首先，先练习一下食物的制作吧。"
    extend "\n[player_surname]君可以教教我昨天那个汉堡怎么做吧！"
    me "OK。"
    extend "\n那么，我就教教你们里面汉堡肉的制作方法吧。"
    extend "\n作为准备，先把洋葱切成碎末。\n像这样，像小猫的手一样，咚咚咚地……。"
    "我之后，月和空分别开始切洋葱。"
    play music "fx/cooking4.ogg"
    window hide
    hide tuki with dissolve
    show sora 25 at topright with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    window show
    sora "嗯……[player_name]君切菜可真麻利，我却不怎么擅长"
    extend "\n有点要流泪了……。"
    show tuki 22 at topleft with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tuki "我，我也是……这可真是不容易啊。"
    play sound "fx/wow2.ogg"
    show cg adult at center with dissolve
    "看着两人不停流着泪的样子，我不由得想到了下流的事情。\n但现在在做料理……要先不去想别的事，甩了甩头，甩掉了妄想。"
    window hide
    hide tuki with dissolve
    hide sora with dissolve
    hide cg with dissolve
    window show
    me "你们俩可别受伤了啊！"
    extend "\n觉得用嘴呼吸的话应该会好一点。"
    show tuki 22 at topleft
    show sora 9 at topright with dissolve
    sora "好～……。"
    tuki "这种事，要是早一点告诉我就好了……。"
    window hide
    stop music fadeout 0.5
    hide tuki with dissolve
    hide sora with dissolve
    window show
    "切完洋葱之后，就进行到下一个步骤吧。"
    extend "\n2人立刻就理解了我说的话，顺利完成了汉堡肉饼。"
    show cg remarkable at center with dissolve
    play sound "fx/sparkle.ogg"
    "过了一会，3个汉堡肉饼就做好了，完全看不出是初学者做的。"
    me "两位，做得很好！！"
    extend "\n哎呀~好厉害好厉害……学习能力强的孩子果然不一样啊~。"
    window hide
    hide cg with dissolve
    show tuki 9 at topleft with dissolve
    window show
    tuki "是吗？"
    extend "\n听你这么一说，我也有了自信呢。"
    show sora 2 at topright with dissolve
    sora "[player_name]君教得比较好，所以才能这么顺利。"
    extend "\n这样就不用担心做汉堡肉饼了！"
    hide tuki with dissolve
    hide sora with dissolve
    "之后我们也互相教学，学习了料理的制作方法，\n练习了料理的制作。"
    window hide
    show sora 10 at top with dissolve
    window show
    play sound "fx/eureka.ogg"
    sora "差不多该做甜品了吧！"
    show sora 11 with dissolve
    extend "\n只要把冰淇淋装饰好就行了，做芭菲\n一定马上就能学会！"
    hide sora with dissolve
    "嘛，做了这么多食物，肯定能做出来。"
    extend "\n……虽然我是这么想的，但实际上并没有那么简单。"
    extend "明明是甜品。"
    window hide
    show tuki 10 at topleft with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    window show
    tuki "唔……嗯。\n打发奶油的时候用力不得当……。"
    show tuki 12 with dissolve
    extend "\n啊……又喷出来了……！\n这样形状就会不好看了。"
    me "又失败了……"
    extend "\n这个要做得好，可没那么容易啊……。"
    show sora 14 at topright with dissolve
    sora "真是的，你们俩完全不行啊！"
    extend "\n这样子的芭菲，根本没人会点单的嘛！！"
    "就算被这么说，我们也无法反驳。"
    extend "\n我们做出的这个，已经不知道是什么东西了，\n已经变成了令人发指的奶油块了。"
    hide tuki with dissolve
    hide sora with dissolve
    show sora 8 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sora "你看，浪费时间过久了，冰淇淋都融化了~！"
    show sora 23 with dissolve
    extend "\n我已经看不下去了！\n在它再变成更惨不忍睹的样子之前，我要把它吃掉！！"
    window hide
    hide sora with dissolve
    window show
    me "……我们继续努力，做好正餐吧，月。"
    show tuki 22 at top with dissolve
    tuki "……是啊。"
    extend "\n每个人都有擅长和不擅长的地方。"
    extend "\n甜点就交给空了。"
    window hide
    show cg school_building_morning at center with dissolve
    window show
    "看着空津津有味地吃着形状扭曲的巴菲，\n我们小声说道。"
    stop music fadeout 2.0
    show bg home_economics_room_evening at center
    window hide
    show cg school_building_evening with Dissolve(1.0)
    pause 0.7
    hide tuki with Dissolve(1.0)
    hide sora with Dissolve(1.0)
    hide cg with Dissolve(1.0)
    play music "quiet_lunch.ogg"
    show sora 2 at topright with dissolve
    window show
    sora "那么，大致的菜单制作方法，你们练习过了吗？"
    show tuki 9 at topleft with dissolve
    tuki "啊啊，这样就没问题了。"
    extend "\n那么，开始收拾吧。"
    me "嗯。"
    extend "\n那么，我来洗碗，\n空负责擦桌子，月负责收拾。"
    show tuki 15
    show sora 3 with dissolve
    tuki_and_sora "明白。"
    hide tuki with dissolve
    hide sora with dissolve
    "我开始洗碗不久，就看到了稍微远点的一个碗。"
    extend "\n那个碗手伸长也摸不到。"
    extend "\n怎么办……。"
    return

label day3_supply:
    hide 班選択 with dissolve
    window show
    "去「采购组」吧！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "quiet_lunch.ogg"
    show tuki 1 at topleft
    show sinobu 24 at topright with dissolve
    window show
    sinobu "采购组，这是买的东西清单。"
    show tuki 6 with dissolve
    tuki "标星号的要从明天开始准备，\n没标星号的就在开始前一天去买。"
    extend "\n比如料理的材料。"
    show sinobu 4 with dissolve
    sinobu "那么，多多指教。"
    window hide
    play sound "fx/running.ogg"
    hide sinobu with dissolve
    hide tuki with dissolve
    pause 0.4
    show saburo 7 at topright with dissolve
    window show
    saburo "呜哇啊~，我们也有活干了啊，穗海同学。"
    show sakuya 5 at topleft with dissolve
    sakuya "我看看……我看看……"
    show sakuya 6 with dissolve
    extend "\n什么啊，居然有这么多小东西。"
    extend "\n话说，浆糊和折纸之类的，自己买不就好了吗。"
    me "算，算了算了。\n这也算是我们的工作，加油吧。"
    show saburo 27 with dissolve
    saburo "说得对~。"
    extend "\n东西很多，不过也就代表不会是大手笔的购物，\n那就一鼓作气去吧~。"
    show sakuya 15 with dissolve
    sakuya "好的~。\n这种程度，去市内的百货公司就可以了吧。"
    extend "\n赶紧出发，赶紧结束。"
    "这么决定了之后，我们离开了学校，前往附近的百货公司。"
    window hide
    stop music fadeout 2.0
    hide saburo with dissolve
    hide sakuya with dissolve
    hide bg with dissolve
    show bg school_route at center with dissolve
    pause 0.5
    show bg downtown with dissolve
    pause 0.5
    play music "umesaki2.ogg"
    show bg department_store1 with Dissolve(1.5)
    show sakuya 19 at top with dissolve
    window show
    sakuya "给，这个。"
    "作哉把刚才的购物清单漂亮地分成三等份，分别交到了各人手中。"
    show sakuya 20 with dissolve
    sakuya "然后你们就把要买的东西放进购物篮里。"
    extend "\n钱放在我这里，用来买材料。\n等你们买齐后，我来算你们的钱。"
    extend "\n可以吗？"
    me "知，知道了。"
    extend "\n话说回来，作哉，你办事真麻溜啊。"
    hide sakuya with dissolve
    show saburo 21 at topright with dissolve
    saburo "明明以前那么磨蹭的家伙，\n是着了什么道吗？"
    show sakuya 8 at topleft with dissolve
    sakuya "麻利点也没什么吧！！"
    extend "\n我只是在思考怎么才能快点把这个麻烦事给解决掉！"
    show saburo 17 with dissolve
    saburo "嘴上这么说……其实是想快点参加学园祭吧~？"
    show sakuya 17 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sakuya "怎么可能！！\n开咖啡店什么的，真的是麻烦得要死！"
    extend "\n稍微动动脑子就知道这是个馊主意了，猫头！！"
    me "啊哈哈。"
    extend "\n作哉你真不坦率啊。"
    show sakuya 16 with dissolve
    sakuya "哈，哈啊？不要擅自下定论啊！"
    extend "\n话说，别光在那瞎说，快点分头去买啊！！"
    extend "\n要尽快搞定这个麻烦事！"
    "作哉趁我和咧嘴坏笑的三朗不注意的空隙，开始行动起来了。"
    play sound "fx/running.ogg"
    hide sakuya with dissolve
    "\n然后我们便也跟着动了起来，开始收集笔记上所写的东西。"
    window hide
    play sound "fx/running.ogg"
    hide saburo with Dissolve(0.8)
    hide bg with Dissolve(0.8)
    stop music fadeout 1.0
    pause 0.4
    show bg department_store2 at center with Radial(0.8)
    return

label day3_design_tomo:
    show bg classroom at center
    window show
    "从黄色开始吧。"
    "嗯，话说，友的形象像是黄色的呢。"
    extend "\n对他这种大大咧咧的性格来说，这种颜色应该很适合……。"
    window hide
    stop music fadeout 0.5
    show tomo 20 at topleft with dissolve
    $ renpy.transition(Quake(60, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    window show
    tomo "好痛。"
    show sintarou 27 at topright with dissolve
    sintarou "友，怎么了？"
    show tomo 26 with dissolve
    tomo "手指破了。"
    show sintarou 10 with dissolve
    sintarou "没事吧？"
    extend "\n好像有点出血呢。"
    me "友，没事吧？"
    extend "\n给我看看。"
    "我抓住友的手臂，看了看他的伤口。"
    play sound "fx/shock.ogg"
    "啊啊啊\n我心爱的男生的手指居然受了伤！"
    extend "\n看上去伤口好像不深，但还是不能大意。"
    extend "\n说不定会因此而感染！"
    window hide
    play music "emergency.ogg"
    show cg c15 at center with Radial(0.5)
    $ renpy.transition(Quake(0, 100, 0.1, 0.065), layer='master')
    play sound "fx/cute.ogg"
    window show
    "啪嗒"
    extend "\n啪嗒"
    tomo "呀啊！"
    extend "\n等，[player_name]君？！！"
    "正太的手简直是美味！！"
    sintarou "噢！[player_name]酱做得不错~♪"
    extend "\n舔伤口这种动作，现在即便在漫画里都很少见了~！"
    me "在之前的漫画里倒是挺常见的。"
    extend "\n为了以防万一，我去拿创可贴。"
    window hide
    hide cg with dissolve
    hide tomo with dissolve
    hide sintarou with dissolve
    show tomo 19 at top with dissolve
    window show
    tomo "啊，嗯。"
    extend "\n谢谢，[player_name]君。"
    play sound "fx/sliding_door.ogg"
    hide tomo with dissolve
    hide sintarou with dissolve
    show bg hallway with dissolve
    "我出了教室，朝保健室走去。"
    window hide
    play sound "fx/running.ogg"
    hide bg with dissolve
    pause 0.5
    show bg classroom at center with dissolve
    show sintarou 12 at topright with dissolve
    window show
    sintarou "唔呵呵~友酱~。"
    extend "\n你的脸好红啊~？"
    show tomo 30 at topleft with dissolve
    tomo "啊，啊啊被那样对待是当然的啊啊啊！？"
    show tomo 7 with dissolve
    extend "\n……啊，又流血了。"
    "啊呜"
    show sintarou 7 with dissolve
    play sound "fx/cute2.ogg"
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    sintarou "喵啊啊啊啊！！间接接吻啊啊啊！！！"
    extend "\n现实中的BL啊啊啊啊！！！！"
    show tomo 32 with dissolve
    play sound "fx/boing.ogg"
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    tomo "不，不不不不是的呜呜呜呜！！！！！"
    extend "\n这，这是无意识的……！"
    hide tomo with dissolve
    hide sintarou with dissolve
    show bg school_building_morning with dissolve
    extend "\n啊~啊~~！[player_name]君是个大笨蛋啊啊啊啊！！"
    window hide
    stop music fadeout 1.0
    hide bg with Dissolve(0.8)
    pause 0.5
    show bg classroom at center with dissolve
    play music "cute_silly.ogg"
    window show
    "我从保健室拿了创可贴回来后，把创可贴给了友，继续工作。"
    "但是，友的样子和刚才有点不一样。"
    show tomo 23 at topleft with dissolve
    extend "\n即使和友目光对上了，"
    show tomo 8 with dissolve
    "视线也会很快被移开。"
    "感觉像被避开了一样……？"
    extend "\n舔手指果然还是做过火了……。"
    show sintarou 12 at topright with dissolve
    sintarou "（嘿嘿）"
    "在略显尴尬的氛围中，我们把所有的纸都切分完毕"
    extend "\n各自写上所有同学的名字，任务全部完成了。"
    window hide
    hide sintarou with dissolve
    hide tomo with dissolve
    show sintarou 2 at topright with dissolve
    window show
    sintarou "哎呀~今天的任务完成得意外早啊。"
    show tomo 21 at topleft with dissolve
    tomo "怎么办。"
    extend "\n没必要勉强在学校留到这么晚，今天就解散吧？"
    play sound "fx/boing.ogg"
    "什么！！"
    extend "\n也就是说，今天愉快的校园生活已经结束了吗？"
    return

label day3_design_sintarou:
    show bg classroom at center
    window show
    "那就从橘色开始吧。"
    "嗯这么说起来，橘色总感觉和慎太郎的形象挺像的。"
    extend "\n对各种意义上都很浮夸的他来说，这种颜色或许很适合他……。"
    window hide
    stop music fadeout 0.5
    show sintarou 21 at topright with dissolve
    $ renpy.transition(Quake(60, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    window show
    sintarou "啊好疼啊。"
    show tomo 21 at topleft with dissolve
    tomo "怎么了？慎酱。"
    show sintarou 23 with dissolve
    sintarou "我干了件蠢事啊……"
    extend "\n划到了，连手指尖都划破了。"
    show tomo 29 with dissolve
    tomo "啊哇哇！流血了！！"
    extend "\n创可贴在哪里来着…。"
    me "慎太郎，没事吧？"
    extend "\n给我看看。"
    "我抓住慎太郎的手臂，看了看他受伤的地方。"
    play sound "fx/shock.ogg"
    "啊啊啊\n我心爱的男生的手指居然受了伤！"
    extend "\n看上去伤口好像不深，但还是不能大意。"
    extend "\n说不定会因此而感染！"
    window hide
    play music "emergency.ogg"
    show cg c28 at center with Radial(0.5)
    $ renpy.transition(Quake(0, 100, 0.1, 0.065), layer='master')
    play sound "fx/cute.ogg"
    window show
    "啪嗒"
    extend "\n啪嗒"
    sintarou "等，等下！"
    extend "\n[player_name]桑？？！？"
    "正太的手简直是美味！！"
    tomo "[player_name]君，好厉害！"
    extend "\n像以前的少女漫画一样。"
    me "在之前的漫画里倒是挺常见的。"
    extend "\n为了以防万一，我去拿创可贴。"
    window hide
    hide cg with dissolve
    hide tomo with dissolve
    hide sintarou with dissolve
    show sintarou 22 at top with dissolve
    window show
    sintarou "多，多谢…。"
    play sound "fx/sliding_door.ogg"
    hide tomo with dissolve
    hide sintarou with dissolve
    show bg hallway with dissolve
    "我出了教室，朝保健室走去。"
    window hide
    play sound "fx/running.ogg"
    hide bg with dissolve
    pause 0.5
    show bg classroom at center with dissolve
    show tomo 11 at topleft with dissolve
    window show
    tomo "哎哎哎！"
    extend "\n小慎，你脸都变红了！"
    show sintarou 32 at topright with dissolve
    sintarou "刚才的事我也觉得很意外啊~。"
    show sintarou 27 with dissolve
    extend "\n……哎呀，又流血了。"
    "啊呜"
    show tomo 13 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tomo "呀啊啊啊！！间接接吻了！！"
    show sintarou 21 with dissolve
    sintarou "你是女高中生吗！"
    show sintarou 17 with dissolve
    extend "\n那种事情我完全都没在想的~。"
    hide tomo with dissolve
    hide sintarou with dissolve
    show bg school_building_morning with dissolve
    extend "\n[player_name]君竟然做了这种事......"
    window hide
    stop music fadeout 1.0
    hide bg with Dissolve(0.8)
    pause 0.5
    show bg classroom at center with dissolve
    play music "cute_silly.ogg"
    window show
    "我从保健室回来之后，把创可贴递给慎太郎，再次开始工作。"
    "但是，友的样子和刚才有点不一样。"
    show sintarou 3 at topright with dissolve
    extend "\n慎太郎则一直盯着我。"
    me "……怎么了？"
    show sintarou 20 with dissolve
    sintarou "没什么~，继续吧继续吧。"
    "怎么回事？我做了什么吗……？是舔了他的手指惹他不高兴了吗！？"
    me "……什么啊~。"
    show sintarou 1 with dissolve
    sintarou "没事啦~。"
    show tomo 39 at topleft with dissolve
    tomo "（坏笑）"
    "在这稍微有些尴尬的氛围中，我们把所有的纸都剪开分好了。"
    extend "\n各自写上所有同学的名字，任务全部完成了。"
    window hide
    hide sintarou with dissolve
    hide tomo with dissolve
    show sintarou 2 at topright with dissolve
    window show
    sintarou "哎呀~今天的任务完成得意外早啊。"
    show tomo 21 at topleft with dissolve
    tomo "怎么办。"
    extend "\n没必要勉强在学校留到这么晚，今天就解散吧？"
    "什么！！"
    extend "\n也就是说，今天愉快的校园生活已经结束了吗？"
    return

label day3_layout_tubasa:
    show bg classroom at center
    window show
    me "那么，我就去给翼同学帮忙了。"
    window hide
    show sinobu 2 at topleft with dissolve
    window show
    sinobu "好的。"
    extend "\n把内部结构画在那张模造纸上。"
    extend "\n我先走了。"
    me "哦。"
    show tubasa 5 at topright with dissolve
    tubasa "一路顺风。"
    extend "\n好好加油哦。"
    play sound "fx/sliding_door.ogg"
    hide sinobu with dissolve
    "忍走出教室后，翼把桌子拼起来，\n然后把图纸放在桌子上，画着教室的平面图。"
    hide tubasa with dissolve
    stop music fadeout 0.5
    window hide
    window show
    me "这是哪间教室？"
    show tubasa 2 at top with dissolve
    play music "cute_silly.ogg"
    tubasa "在一楼的多功能教室2号厅。"
    me "嗯？我们要用的教室是忍来负责借的吧。"
    extend "\n那我们还不一定能够借到那间教室，\n这个时候就考虑构造，也没太大的意义啊……。"
    show tubasa 10 with dissolve
    tubasa "忍说过，为了能让大家一起开展工作，他一定会借到第二间多功能室\n所以……。"
    me "真，真有自信啊……。"
    show tubasa 4 with dissolve
    tubasa "是的。"
    extend "\n不过，他这么说，总有种莫名的说服力。"
    me "确实……他就是有这种魅力。"
    extend "\n要真到了紧要关头，估计能成为超级赛亚人吧。"
    show tubasa 8 with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tubasa "这，这种事情，要是忍知道的话会生气的吧。"
    show tubasa 5 with dissolve
    extend "\n那就来考虑咖啡店的内部构造吧。"
    return

label day3_layout_sinobu_unused:
    window show
    me "忍，我也要去！"
    window hide
    show sinobu 21 at topleft with dissolve
    window show
    sinobu "嗯，我知道了。"
    extend "\n那就跟我来吧。"
    show tubasa 4 at topright with dissolve
    tubasa "我，我走了。"
    extend "\n好好加油哦。"
    window hide
    hide sinobu with dissolve
    hide tubasa with dissolve
    play sound "fx/sliding_door.ogg"
    show bg hallway with dissolve
    window show
    "我们把翼留在教室后，便向教职员室走去。"
    me "连借教室都还没决定好，\n就让翼考虑内部构造吗？"
    window hide
    show sinobu 23 at top with dissolve
    window show
    sinobu "我已经告诉一之濑同学可以去哪间教室了，所以没问题。"
    me "诶，可是，接下来还要去借教室的……"
    show sinobu 12 with dissolve
    sinobu "嗯。"
    extend "\n我一定会借到教室的，放心。"
    me "哦，哦哦…。"
    "好强大的自信啊。"
    extend "\n即便如此，我也觉得安心了，不愧是忍啊。"
    hide sinobu with dissolve
    sinobu "失礼了。"
    play sound "fx/sliding_door.ogg"
    stop music fadeout 0.5
    hide bg with dissolve
    "他打开教师办公室的门，向负责的海老师走去。"
    "……。"
    window hide
    play music "sinobu_theme.ogg"
    show cg c35 1 at center with Radial(0.5)
    window show
    sinobu "您好，海老师。"
    extend "\n我是二年一班的绫濑。"
    extend "\n为了准备御咲祭，我前来向您询问教室的借用事宜。"
    umi "啊，你好。"
    extend "\n那个，二年一班的话……你们是打算和二年二班合开咖啡店吧。"
    extend "\n既然是要用火，又要在合办的地方，那宽敞的教室是必要的吧。"
    extend "\n有想要的地方吗？"
    sinobu "有的。"
    extend "\n我想借用一楼的多功能教室2号厅。"
    umi "啊，那里原本是打算作为休息室的哦。"
    extend "\n其他的教室不行吗？"
    sinobu "那么大的教室当休息室？"
    umi "是啊。"
    extend "\n宽敞的空间会让人更放松的。"
    sinobu "……您说的没错，但是……"
    show cg hallway with FadeWhite(0.5)
    extend "\n那个教室位于食堂的旁边，人流量很大，"
    extend "\n如果当天人流量进一步增加的话，\n哪怕只是做为休息场所，人太多大概也没法让人好好休息吧。"
    show cg school_building_full with FadeWhite(0.5)
    sinobu "另外，从正门到食堂的路上很长，而且道路错综复杂，"
    extend "\n需要休息的老年人，或者是身体有障碍的人，\n还有那些第一次来学园，人生地不熟的人们，\n对于他们，食堂旁边的这个2号厅作为休息室来说并不便利。"
    show cg school_building_morning with FadeWhite(0.5)
    sinobu "因此，如果要作为休息场所使用的话，\n我推荐使用位于正门和食堂中间的多功能教室1号厅。"
    extend "\n那里虽然不大，但是位置显眼，\n厕所和自动贩卖机都很近，作为休息场所来说是最合适的。"
    "忍像往常一样，平淡地陈述着自己的意见。"
    "另一方面，海老师本以为忍会选择其他教室，\n对于休息场所一事，面对忍意料之外的提案，显得有些不知所措。"
    umi "确，确实如此……你说的确实可行。"
    extend "\n滑子老师，关于这个意见，您怎么看？"
    "话音刚落，旁边的滑子老师便转过身来。"
    extend "\n噢噢，好怀念啊！明明都已经过去10年了，这个人看起来还是一点都没老啊。"
    nameko "嗯~我刚刚推举多功能教室2号厅主要是因为那里面积大，\n不过听你这么一说，我倒觉得用多功能教室1号厅更好。"
    extend "\n1号厅一直没人用过，把那里弄成休息室，\n让2年级1，2班的人去那里休息不是很好吗。"
    umi "有道理。"
    extend "\n不过，离食堂那么近，应该不会有什么生意吧？"
    window hide
    show cg c35 2 with dissolve
    window show
    sinobu "不，食堂和咖啡厅的风格不一样。"
    extend "\n前者是为了填饱肚子，后者是为了享受品茶。"
    extend "\n我想，大部分来食堂吃饭的人，都会选择去咖啡厅稍作休息，\n顺便喝杯茶吧。"
    sinobu "我们二年级1，2班的咖啡厅绝对生意兴隆。"
    extend "\n一定会成功的。"
    "虽然忍的语气很冷静，但最后那句话却充满了力量。"
    umi "……我明白了。既然你这么热情，"
    extend "\n二年级1，2班就用多功能教室2号厅吧。"
    sinobu "非常感谢。"
    extend "\n那么，我就先告辞了。"
    "说着，我们离开了办公室。"
    window hide
    stop music fadeout 0.5
    play sound "fx/sliding_door.ogg"
    hide cg with dissolve
    show bg hallway with dissolve
    play music "quiet_lunch.ogg"
    window show
    "走在回教室的路上，我跟忍说："
    me "忍～好厉害！真的太棒了。"
    extend "\n要是刚才那样的话，今后商谈也肯定很顺利的。"
    window hide
    show sinobu 10 at top with dissolve
    window show
    sinobu "商谈什么的，还太早了啦。"
    me "不过，真是被吓到了呢……"
    extend "\n竟然颠覆了老师的论点，让他心悦诚服。"
    show sinobu 14 with dissolve
    sinobu "论点中有很多漏洞和破绽呢。"
    me "海老师也说过，你的热情打动了他不是吗？"
    extend "\n这时候最重要的，是比论点还要坚定不移的信念。"
    extend "\n即使论点毫无矛盾，也必须让他心服口服。"
    extend "\n关键的结论也很成功，真是太棒了。"
    return

label day3_cooking_tuki:
    show bg home_economics_room_evening at center
    window show
    me "月。"
    extend "\n不好意思，可以帮我把放在那边的碗\n拿过来吗？"
    window hide
    show tuki 6 at top with dissolve
    window show
    tuki "啊，好呢。"
    hide tuki with dissolve
    "说完，月走到了放着碗的那边，\n然后端着碗走了回来。"
    me "谢谢。"
    extend "\n在那里就好，我来拿！！？"
    stop music fadeout 0.5
    "我正准备走向月，脚却在洗盘子时打湿的地板上滑了一下。"
    me "呜噢！？"
    show tuki 11 at top with dissolve
    tuki "嗯！？"
    hide tuki with dissolve
    $ renpy.transition(Quake(0, 70, 0.1, 0.06), layer='master')
    play sound "fx/fall_down.ogg"
    "喀嚓！！"
    "月的强壮的胸膛就在我的眼前。"
    "出乎意料的甜蜜展开！"
    "但是，实际上也没那么“甜蜜”。"
    play music "lively_boys.ogg"
    show cg remarkable at center with FadeWhite(0.5)
    extend "\n我的碗里，还剩大量的奶油。"
    window hide
    show cg c61 with FadeWhite(0.5)
    play sound "fx/boing.ogg"
    window show
    me "哇，啊哇哇哇哇月对不起！！"
    extend "\n啊啊啊啊好多的奶油沾到身上了…。"
    tuki "不，我没事。"
    extend "\n重要的是，[player_surname]没受伤吧？\n摔得可真惨。"
    me "我也没事。"
    extend "\n但是，怎么办好呢……把月的衣服弄脏了，对不起！"
    tuki "别在意。"
    extend "\n但是，衣服这么脏的话，最好还是换一下衣服……。"
    sora "啊~啊，你们两个都溅了这么多的奶油……"
    extend "\n这里交给我来收拾，你们两个去换衣服吧。"
    tuki "啊啊。\n抱歉，这里就交给你了。"
    me "空也是，对不起。"
    extend "\n给你添了麻烦。"
    sora "没有用完全部奶油的我也有一部分责任，所以别在意。\n走好，待会见。"
    window hide
    stop music fadeout 0.5
    hide sora with dissolve
    hide cg with dissolve
    hide bg with dissolve
    play sound "fx/sliding_door.ogg"
    show bg hallway_evening at center with dissolve
    play music "quiet_lunch.ogg"
    window show
    "我从厨房出来，然后就听到从教室里传来的说话声。"
    show tuki 3 at top with dissolve
    tuki "嗯？"
    extend "\n里面好像有别的小组在工作。"
    me "呜呜……我不想被看到这副样子啊。"
    "我们不情愿地走进教室。"
    window hide
    hide tuki with dissolve
    play sound "fx/sliding_door.ogg"
    show bg classroom_evening with dissolve
    show sintarou 14 at topright with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    window show
    sintarou "呜噢！？\n你们两个这是什么打扮！！"
    extend "\n浑身都是牛奶！！"
    show tomo 18 at top with dissolve
    tomo "呜哇~~~！！！"
    show tomo 25 with dissolve
    extend "\n我说，慎酱。\n这不就像是，那个“东西”吗？"
    show sintarou 12 with dissolve
    sintarou "小友也这么认为吗？"
    extend "\n果然是那个吧~"
    show tuki 17 at topleft with dissolve
    tuki "那个？ 你在说什么呢。"
    me "呜……讨厌秒懂的自己…。"
    show sintarou 9 with dissolve
    sintarou "你们两个一直相互打情骂俏！"
    extend "\n这里可是学校，别太过火哦~"
    show tuki 29 with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    tuki "什……你，你个蠢货！！！\n你可不要误会了！！"
    extend "\n这只是普通的奶油而已！！"
    show tomo 4 with dissolve
    tomo "[player_name]君的？"
    play sound "fx/boing.ogg"
    me "不，不是的！！！\n这只是用来烹饪的普通奶油！！"
    extend "\n只是我摔倒时打翻了而已……"
    show sintarou 1 with dissolve
    sintarou "开玩笑的啦，别当真！"
    extend "\n哎呀，你们两个都认真起来了呀~♪"
    show tomo 12 with dissolve
    tomo "连月都这么慌张，真少见啊！"
    show tuki 27 with dissolve
    tuki "啊，我并没有慌张。"
    extend "\n我们只是来拿换洗衣物而已。"
    extend "\n我们先走了哦。"
    "月一把抓起我和他的体操袋。"
    window hide
    hide sintarou with dissolve
    hide tomo with dissolve
    hide tuki with dissolve
    show tuki 28 at top with dissolve
    window show
    tuki "我本来打算在这里换的，\n但是他们俩还在，我就不想再被捉弄了。"
    extend "\n去隔壁教室换吧。"
    me "嗯，好吧。"
    window hide
    hide tuki with dissolve
    play sound "fx/sliding_door.ogg"
    show bg hallway_evening with dissolve
    pause 0.6
    show bg classroom_evening with Dissolve(1.0)
    window show
    "幸运的是，隔壁教室空无一人。"
    "我从月手里接过他的换洗衣物，然后取出毛巾。"
    me "月，别动。"
    "我小心地擦拭掉月脸上沾的牛奶。"
    show tuki 27 at top with dissolve
    tuki "不用了。"
    extend "\n这点小事我自己来……。"
    me "不行。"
    extend "\n这都是我的错，所以这种小事就让我来吧。"
    show tuki 28 with dissolve
    tuki "呜呜……。"
    stop music fadeout 2.0
    "月害羞地转过脸去。"
    extend "\n呵呵……平时都那么从容不迫的他，现在却害羞了，真是太可爱了！！"
    play music "hurry_up.ogg"
    window hide
    show cg c62 1 at center with zoominout
    play sound "fx/cute2.ogg"
    window show
    me "接下来就擦掉你校服上沾的牛奶吧。"
    tuki "喂，喂！"
    extend "\n我自己来……"
    me "别动。"
    extend "\n你不小心擦掉的话，校服反而会更脏的哦。"
    tuki "呜……立场好像颠倒过来了？"
    me "你想多了想多了♪"
    hide bg
    hide tuki
    "我一边用毛巾擦掉月身上的牛奶，\n一边隔着学生服享受着月紧致的肌肤。"
    show cg adult with FadeWhite(0.5)
    tuki "呜……嗯咕……。"
    play sound "fx/sparkle.ogg"
    "呜嘿嘿……我这家伙享受过头了啊啊啊啊！！！！"
    "每当我的毛巾擦过，月都会敏感地作出反应。"
    "难道说他其实很敏感吗？"
    extend "\n这里？这里很舒服吗？？？"
    play sound "fx/cute2.ogg"
    "我完全进入了变态大叔模式。"
    show cg c62 2 with FadeWhite(0.5)
    me "来来！\n那么，终于到了该换衣服的环节了！"
    extend "\n好啦，赶紧脱掉学生服吧~♪"
    "我迅速将学生服的扣子解开，"
    show bg classroom_evening at center
    tuki "已，已经够了！！"
    extend "\n[player_surname]，不许再乱来了……"
    "月焦急地说道，但我还是解开了他衬衫的扣子。"
    window hide
    stop music fadeout 0.2
    play sound "fx/sliding_door.ogg"
    hide cg with FadeWhite(0.5)
    window show
    "咔啦"
    show sora 3 at top with dissolve
    sora "哥哥，[player_name]居然在这里啊。"
    extend "\n对面那边已经收拾完了，"
    pause 0.5
    show sora 4 with dissolve
    extend "啊……。"
    show cg school_building_evening at center with Dissolve(0.3)
    play sound "fx/triangle.ogg"
    tuki_and_me "啊……。"
    window hide
    pause 0.4
    hide tuki with dissolve
    hide bg with dissolve
    hide cg with dissolve
    hide sora with dissolve
    play music "twins_theme.ogg"
    show bg classroom_evening at center with Radial(1.0)
    window show
    "我们为了消除误会，向呆住的空重新说明了事情的经过。"
    show sora 12 at top with dissolve
    sora "原，原来如此……知道大概的经过了。"
    show sora 20 with dissolve
    extend "\n但是，[player_name]啊！\n无论如何，你都做得太过火了。"
    extend "\n在旁人看来，可能会觉得你行为很奇怪。"
    me "对，对不起……。"
    hide sora with dissolve
    show sora 23 at topright with dissolve
    sora "哥哥也是。\n为什么什么都不说，任凭他做这种事嘛。"
    extend "\n即便真的是那样，至少拒绝一下也好吧。"
    show tuki 14 at topleft with dissolve
    tuki "……抱歉……不由得就同意了。"
    show sora 14 with dissolve
    sora "还说什么不由得，真是的……。"
    show sora 34 with dissolve
    extend "\n对了，[player_name]君。\n把我们的行李拿到这边来。"
    extend "\n毕竟你也很累了，慢慢来也可以。"
    me "诶？"
    extend "\n那，那个，为什么是我……？"
    hide tomo with dissolve
    hide tuki with dissolve
    hide sora with dissolve
    stop music fadeout 1.0
    show sora 26 at top with dissolve
    sora "让人误会的人，不是你吗？"
    "空的脸上挂着笑容。"
    me "是，是的……是我呢！"
    extend "\n那么，请让我马上把行李拿过来！"
    window hide
    hide sora with dissolve
    play sound "fx/sliding_door.ogg"
    show bg hallway_evening with dissolve
    pause 0.6
    show bg classroom_evening with Dissolve(1.0)
    show sintarou 30 at topright with dissolve
    play music "cute_silly.ogg"
    window show
    sintarou "啊咧，[player_name]酱！"
    extend "\n又怎么了？"
    me "啊~去拿三个人的行李。"
    show tomo 21 at topleft with dissolve
    tomo "还没换上体操服吗。"
    me "啊哈哈……发生了很多事……。"
    show sintarou 12 with dissolve
    sintarou "发生了很多事啊……。"
    show tomo 25 with dissolve
    tomo "什么什么？发生了什么啊？？"
    me "这，这个嘛！"
    show tomo 40 with dissolve
    tomo "诶~！！哎呀哎呀！\n快告诉我吧~。"
    hide tomo with dissolve
    hide sintarou with dissolve
    show sintarou 18 at top with dissolve
    sintarou "……[player_name]君，难道对阿月有意思？"
    me "什！！？"
    extend "\n怎，怎么会！！"
    show sintarou 1 with dissolve
    sintarou "哼哼……是嘛是嘛♪"
    extend "\n我估计要插足那对兄弟的感情的话难度很高，\n我不太推荐哦~。"
    me "所，所以说，不是啊！！"
    extend "\n我喜欢月，也喜欢空，"
    extend "\n三个人在一起我也会感到开心，我很喜欢这样啊。"
    show sintarou 31 with dissolve
    sintarou "原来如此~。\n那就当我之前的话没说。"
    me "……。"
    extend "\n话说回来，虽然你说要在兄弟之间插足很难，"
    extend "\n但对他们来说，果然还是两个人相处比较好吗？"
    extend "\n他不会觉得我在妨碍他们吧……。"
    show sintarou 29 with dissolve
    sintarou "啊~没有没有！哈，"
    extend "\n[player_name]可能觉得他们眼里只有彼此吧，\n但从旁观者的角度来说，[player_name]君的存在也让他们很开心呢！"
    extend "\n对吧，友？"
    hide sintarou with dissolve
    show tomo 4 at topleft with dissolve
    tomo "嗯嗯。"
    extend "\n之前，月和空感觉像是双子星，\n现在的话，[player_name]君也算上，你们三个人更像是三剑客呢！"
    extend "\n都相处得那么好了，你大可自信一点！"
    show sintarou 30 at topright with dissolve
    sintarou "就是就是！"
    extend "\n不要莫名担心啊~"
    me "是，是么！\n谢谢……总算是放心了。"
    extend "\n那我就先回他俩那边去了！\n再见。"
    show tomo 1
    show sintarou 1 with dissolve
    tomo_and_shin "哦~，记得代我们问好~。"
    "我提着他们的东西，走出了教室。"
    stop music fadeout 1.0
    window hide
    hide sintarou with dissolve
    hide tomo with dissolve
    play sound "fx/sliding_door.ogg"
    show bg hallway_evening with dissolve
    pause 0.6
    show bg classroom_evening with Dissolve(1.0)
    window show
    play music "twins_theme.ogg"
    me "久等了~！\n东西我就放在桌子上哦。"
    show tuki 9t at topleft with dissolve
    tuki "啊，麻烦你了。"
    show sora 32 at topright with dissolve
    sora "辛苦了，[player_name]君。"
    me "咦，月已经换好了啊。"
    show tuki 4t with dissolve
    tuki "[player_surname]去拿东西的时候我趁机换的。"
    hide tuki with dissolve
    hide sora with dissolve
    play sound "fx/shock.ogg"
    "呜……这什么情况啊！！"
    extend "\n听了客观的意见后有了自信固然好，\n但我却因此错过了看到月换衣服的场景！！！"
    window hide
    show sora 29 at top with dissolve
    window show
    sora "因为，要是不这样做，\n[player_name]君就会用下流的眼光盯着哥哥看。"
    play sound "fx/boing.ogg"
    "咕"
    me "到，到底，什么情况啊~？？\n那，那种家伙在哪里，我去收拾他！"
    extend "\n啊哈哈哈……。"
    hide sora with dissolve
    show tuki 20t at topleft
    show sora 29 at topright with dissolve
    play sound "fx/eureka.ogg"
    tuki_and_sora "（盯……）"
    me "呜……。"
    show sora 10 with dissolve
    sora "之前就说过了，撒谎也没用哦。"
    extend "\n因为那种事，会直接表现在眼睛上的。"
    show tuki 18t with dissolve
    tuki "别小看我们的眼睛。"
    me "啊，好的……对不起。"
    extend "\n我会老老实实去换衣服的。"
    "虽然不能亲眼看到月穿短裤的样子有点遗憾，\n但今天玩得挺开心的，所以也没什么好抱怨的……。"
    window hide
    show cg school_building_evening at center with Dissolve(0.8)
    window show
    "就这样，作为烹饪组的我们的工作，也到此告一段落了。"
    window hide
    stop music fadeout 0.5
    hide bg with Dissolve(1.0)
    hide cg with Dissolve(1.0)
    hide tuki with Dissolve(1.0)
    hide sora with Dissolve(1.0)
    return

label day3_cooking_sora:
    show bg home_economics_room_evening at center
    window show
    me "空。"
    extend "\n不好意思，可以帮我把放在那边的碗\n拿过来吗？"
    window hide
    show sora 3 at top with dissolve
    window show
    sora "嗯，我知道了！"
    hide sora with dissolve
    "说完，空就走向碗盆放在的那面，\n然后拿着碗盆回来了。"
    stop music fadeout 0.5
    "然后就在这时候"
    window hide
    show sora 8 at top with dissolve
    window show
    sora "呜哇！？"
    me "诶！？"
    hide sora with dissolve
    $ renpy.transition(Quake(0, 70, 0.1, 0.06), layer='master')
    play sound "fx/fall_down.ogg"
    "喀嚓！！"
    "空在拿碗的时候踩到湿漉漉的地板滑了一跤，失去平衡撞到了我。"
    "可爱的少年，向我扑过来的事故！！"
    "但是，实际上也没那么“甜蜜”。"
    play music "lively_boys.ogg"
    show cg remarkable at center with FadeWhite(0.5)
    extend "\n空拿着的碗里，还剩下大量的鲜奶油。"
    window hide
    show cg c54 with FadeWhite(0.5)
    play sound "fx/cute2.ogg"
    window show
    sora "哇啊啊啊啊[player_name]君，对不起！！！"
    extend "\n啊啊啊啊沾了那么多奶油…。"
    me "没，没事的。"
    extend "\n比起这个，空身上也沾满了奶油……。"
    "身上沾满了大量白色奶油的空！！！！"
    play sound "fx/sparkle.ogg"
    extend "\n这，这还真是……真是令人兴奋的……充满艺术美感的……！"
    tuki "你们没事吧？"
    extend "\n制服都脏了啊……。"
    extend "\n这里就由我来打扫，你们先去换衣服吧。"
    sora "嗯，好的……。"
    extend "\n[player_name]君，真的对不起！"
    me "没关系没关系！你别太在意！！"
    extend "\n从结果上来看，我也饱了眼福。"
    sora "……？\n嘛，总之我们得换上体操服了！"
    extend "\n[player_name]君身上粘的奶油更多呢……。"
    extend "\n那，我们走吧！"
    window hide
    stop music fadeout 0.5
    hide sora with dissolve
    hide cg with dissolve
    hide bg with dissolve
    play sound "fx/sliding_door.ogg"
    show bg hallway_evening at center with dissolve
    play music "quiet_lunch.ogg"
    window show
    "我从厨房出来，然后就听到从教室里传来的说话声。"
    show sora 5 at top with dissolve
    sora "啊~其他的小组都在教室里干活呢…。"
    "空通过门上的窗户观察了下教室里面的状况，然后说道。"
    show sora 24 with dissolve
    sora "隔壁的教室好像没人，我们就在那里换衣服吧。"
    extend "\n[player_name]君就在这边的教室等着。"
    extend "\n我拿好体操服之后，再过会儿就去。"
    me "诶？不用了，我自己去拿体操服就行。"
    show sora 25 with dissolve
    sora "被其他的人看见你这个样子的话，肯定不好吧？"
    extend "\n归根到底，这都是我的错，[player_name]君你不用在意。"
    me "谢，谢谢。"
    hide sora with dissolve
    "一边感谢着空的关心，我走进了空说的空无一人的隔壁教室，"
    play sound "fx/sliding_door.ogg"
    show bg classroom_evening with dissolve
    extend "\n没过多久，空也走了进来。"
    show sora 24 at top with dissolve
    sora "让你久等了！"
    extend "\n果然，友君和慎酱都笑我了……。"
    me "啊哈哈。\n他们怎么说的？"
    show sora 14 with dissolve
    sora "那，那个我就不说了！"
    extend "\n好难为情啊……。"
    me "嗯？难为情？"
    show sora 9 with dissolve
    sora "没事了！！总之[player_name]别在意！"
    show sora 24 with dissolve
    extend "\n这是[player_name]君的体操服哦！                    还有，我给你带了毛巾过来。"
    hide sora with dissolve
    "如此说着，空用手上拿着的毛巾擦了我的身体。"
    extend "\n像是在小心注意不让我受伤一般，他擦得非常温柔。"
    "明明自己也弄脏了，却不先给自己擦。\n而是先考虑我，他真的是一位温柔的男孩子……。"
    window hide
    show sora 5 at top with dissolve
    window show
    stop music fadeout 0.7
    sora "……脸应该，这样就干净了。"
    extend "\n还有，衣服也必须换掉才行啊。"
    play music "hurry_up.ogg"
    window hide
    show cg c55 1 at center with zoominout
    play sound "fx/boing.ogg"
    window show
    "空的手伸向了我的制服。"
    me "诶，等等！ 空？？"
    sora "嗯？ 怎么了？"
    me "那，那个……为什么要把我的制服给？"
    sora "诶？ 因为弄脏了，必须要换掉才行啊……。"
    me "我不是那个意思！"
    extend "\n换衣服这种小事，我自己会做的。"
    sora "不行。[player_name]君是我弄脏的。"
    hide sora
    hide bg
    extend "\n我有责任。\n所以，什么我都会为你做的！"
    show cg adult with FadeWhite(0.5)
    play sound "fx/impact.ogg"
    "[player_name]君是被空弄脏的……"
    play sound "fx/impact.ogg"
    extend "\n什么都为你做......"
    play sound "fx/impact.ogg"
    extend "\n什么都为你做......"
    extend "\n做……做……"
    play sound "fx/wow2.ogg"
    extend "做……！？"
    $ renpy.transition(Quake(0, 70, 0.15, 0.1), layer='master')
    play sound "fx/cute2.ogg"
    me "什么什么什么啊啊啊啊！！！？？"
    extend "\n空，空，你这么大胆！！！！！！"
    sora "哎……？"
    $ renpy.transition(Quake(0, 70, 0.15, 0.1), layer='master')
    play sound "fx/boing.ogg"
    extend "\n啊，我，我说[player_name]君，你到底在想些什么啊！？"
    extend "\n我，我可没有那个意思！！"
    "空的脸一瞬间变得通红。"
    show cg c55 2 with FadeWhite(0.5)
    sora "真，真是的！！"
    extend "\n[player_name]君说什么奇怪的话呢！害我现在不知道该怎么做了。"
    extend "\n但是，这都是我的责任啊……必须得做到最后才行。"
    "空一边脸红，一边解开了我校服的纽扣。"
    "不妙……总觉得这个行为，有种犯罪的味道啊。"
    "校服的下面，就只有一件T恤……。"
    extend "\n就这样让他脱真的好吗……。"
    show bg classroom_evening at center
    extend "\n但是，又不是我强迫他的。"
    extend "\n这是空自己所期望的事情。"
    show cg remarkable with Radial(0.5)
    play sound "fx/eureka.ogg"
    "不管了，直接开始吧！！！来吧，赤峰空！！"
    play sound "fx/explosion2.ogg"
    extend "\n我会全盘接受的！"
    "空解开了我T恤的纽扣。"
    window hide
    stop music fadeout 0.2
    play sound "fx/sliding_door.ogg"
    hide cg with FadeWhite(0.5)
    window show
    "咔啦"
    show tuki 6 at top with dissolve
    tuki "空，[player_surname]君，原来你们在这里啊。"
    extend "\n那边我已经收拾好了，"
    pause 0.5
    show tuki 12 with dissolve
    extend "了……。"
    show cg school_building_evening at center with Dissolve(0.3)
    play sound "fx/triangle.ogg"
    "空＆我" "啊……。"
    window hide
    hide tuki with dissolve
    hide bg with dissolve
    hide cg with dissolve
    pause 0.4
    play music "twins_theme.ogg"
    show bg classroom_evening at center with Radial(1.0)
    window show
    "空安抚着即将暴走的月，向他说明了情况，事态终于平息了下来。"
    show tuki 16 at topleft with dissolve
    tuki "原来如此，是这么回事啊……"
    extend "\n别这样，别让我吓一跳啊。\n一瞬间，我都搞不懂发生了什么了。"
    show sora 1 at topright with dissolve
    sora "啊，啊哈哈……吓了哥哥一跳呢。"
    extend "\n但是，我得好好负起责任来才行……。"
    show tuki 17 with dissolve
    tuki "这股志气我认可，不过再怎么说这也做过头了。"
    extend "\n[player_surname]君不也是，因为你而不知所措。"
    me "啊，啊哈哈哈……。"
    show sora 18 with dissolve
    sora "呜呜……真的非常抱歉。"
    me "没事没事！"
    extend "\n空的心意我已经好好感受到了！"
    extend "\n所以你不用在意的！！"
    show sora 21 with dissolve
    sora "嗯……。"
    "和我说话时相反，空已经完全进入消沉模式了。"
    show tuki 6 with dissolve
    tuki "……[player_surname]，我先把你们的行李给收拾好，\n这期间，能麻烦你照看下空吗？"
    me "好。"
    extend "\n谢谢你啦，月。"
    play sound "fx/sliding_door.ogg"
    hide tuki with dissolve
    "月离开了教室。"
    window hide
    hide sora with dissolve
    show sora 20 at top with dissolve
    window show
    sora "为什么我不能像哥哥一样办事麻利啊......"
    extend "\n就因为这样，大家都能看出我是弟弟了。"
    extend "\n因为是双胞胎，我明明也可以被大家认为是哥哥的，\n可从来没有过这种情况……。"
    "不对，比起内在，月的外在成长明显快得多……"
    extend "\n虽然我这样想，但没有说出口。"
    me "没问题的。"
    extend "\n空就是空，也有比月优秀的地方。"
    show sora 25 with dissolve
    sora "才没有……"
    extend "\n不管怎么做，我都比不过哥哥……"
    "空比较感性，所以他的失落也更加真切可见。"
    extend "\n虽然一直没有表现出来，但内心怀着的那种情结，还有平日里一直放在心上的事情，就感觉像是一下子流露出来了一样……。"
    me "虽然你可能自己没有意识到，"
    extend "\n但在旁人看来，你也是有优点的。"
    show sora 21 with dissolve
    sora "……在旁人眼里，是怎样的？"
    me "嗯～……月是很坚强的，很可靠的。空是很温柔的，会支持别人的。"
    extend "\n虽然性格不同，但各自都很可靠。"
    extend "\n只是，今天是事与愿违，所以才出错了，"
    extend "\n对……比如说，昨天我就看到了空的优点哦。"
    show sora 5 with dissolve
    sora "优点？"
    me "嗯。"
    extend "\n昨天，在空的家出现了蜘蛛的时候，\n空自己主动去帮助月。"
    extend "\n正因为有你在，月才能发挥出强大的一面。"
    me "而且我一直都很佩服空的亲切。"
    extend "\n周围的人也都看到了空的长处，\n没有人会觉得空比月差。"
    show sora 30 with dissolve
    sora "……是吗，谢谢你。"
    extend "\n总感觉，心情变好了。"
    "说着，空露出了平时的那种可爱笑容。"
    window hide
    hide sora with dissolve
    play sound "fx/sliding_door.ogg"
    window show
    "哐当哐当"
    show tuki 9 at topleft with dissolve
    tuki "让你们久等了。"
    extend "\n你们的东西就放这里了。"
    show sora 3 at topright with dissolve
    sora "谢谢，哥哥。"
    me "谢谢。"
    show tuki 6 with dissolve
    tuki "嗯？你们俩衣服还没换吗。"
    extend "\n沾了奶油的衣服很难看，没法回去吧。"
    extend "\n趁现在换掉比较好哦。"
    show sora 5 with dissolve
    sora "啊……是啊。"
    extend "\n刚才那么忙乱，完全忘记了要换体操服！"
    "空马上脱掉立领制服，开始解衬衫扣子。"
    hide sora with dissolve
    hide tuki with dissolve
    stop music fadeout 0.5
    "咕噜……"
    window hide
    play music "emergency.ogg"
    show tuki 5 at topleft with dissolve
    window show
    tuki "等一下，空。\n你去储物柜前换衣服。"
    extend "\n然后，[player_surname]。\n你去黑板前换衣服。"
    show sora 4 at topright with dissolve
    sora "诶？为什么？"
    show tuki 17 with dissolve
    tuki "有人会用不怀好意的眼光看你。"
    play sound "fx/boing.ogg"
    "咕"
    me "到，到底，什么情况啊~？？\n那，那种家伙在哪里，我去收拾他！"
    extend "\n啊哈哈哈……。"
    show tuki 20
    show sora 29 with dissolve
    play sound "fx/eureka.ogg"
    tuki_and_sora "（盯……）"
    me "呜……。"
    show tuki 8 with dissolve
    tuki "不要小看我们的目光。"
    extend "\n人们的心思其实都表现在眼睛里哦。"
    show sora 23 with dissolve
    sora "就算说谎也没用的。"
    extend "\n[player_name]君，你又在想什么奇怪的事情呢！"
    me "啊，好的……对不起。"
    extend "\n我老老实实地转过身开始换衣服。"
    window hide
    hide sora with dissolve
    hide tuki with dissolve
    window show
    "我灰头土脸地走到黑板前，开始换衣服……但是不会放弃！！"
    "身为正太控的这个秘密已经伴随我25年，"
    extend "\n平日里就经常偷看少年的我，已经变成了一个偷窥高手！！！"
    extend "\n这种程度的状况，没有什么了不起的……我随随便便就能偷窥到的！！"
    play sound "fx/heartbeat.ogg"
    "慎重地……"
    extend "冷静地……"
    extend "趁机……"
    extend "算准绝妙的时机……"
    stop music fadeout 0.3
    show cg c56 at center with FadeWhite(0.5)
    play sound "fx/eureka.ogg"
    "偷看"
    window hide
    play music "bwv147.ogg"
    show cg adult with dissolve
    window show
    "看到了……看到了！！"
    extend "\n终于，我亲眼确认了！！"
    "那时说的都是真的……！！！！"
    extend "\n……他真的穿着兜裆布……！！"
    "光是知道这个事实，我就已经满足了……。"
    window hide
    stop music fadeout 0.3
    show cg school_building_evening with dissolve
    window show
    play sound "fx/triangle.ogg"
    "在这之后，不出所料，月发现了被真相所震撼的我。"
    window hide
    hide bg with Dissolve(1.0)
    hide cg with Dissolve(1.0)
    return

label day3_supply_sakuya:
    show bg department_store2 at center
    play music "sakuya_theme.ogg"
    window show
    me "这就是最后一项……了。"
    "我收集完要负责的东西后，从商品架的缝隙间看到了作哉。"
    "嗯……？"
    extend "那个地方是宠物用品的区域，\n购物清单上有这样东西吗？"
    window hide
    window show
    me "作哉君，怎么样？"
    extend "\n购物顺利吗？？"
    show sakuya 29 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sakuya "呃！[player_surname]……。"
    show sakuya 12 with dissolve
    extend "\n还，还行吧。"
    extend "\n别管我了，你那边怎么样了？"
    me "我这边已经买齐了。"
    extend "\n作哉，你为什么要把篮子藏起来啊？"
    show sakuya 11 with dissolve
    sakuya "呃……这个……"
    me "等等，让我看一下！"
    hide sakuya with dissolve
    "我用点强硬的手段从作哉的篮子里抢走了篮子和便签。"
    window hide
    window show
    me "……狗粮不在清单里吧？"
    extend "\n为什么装进篮子里了啊？？"
    show sakuya 7 at top with dissolve
    sakuya "呜……平时的宠物店不卖这个……。"
    extend "\n小翼最喜欢这个了……。"
    me "不行！"
    extend "\n这种东西就用你自己的钱买吧。"
    show sakuya 8 with dissolve
    sakuya "稍微用点钱又有什么关系！"
    extend "\n反正也不会被发现的。"
    me "不行！"
    extend "\n要是提交收据和明细单的话，迟早会暴露的。"
    extend "\n而且，就算不被发现也不可以做坏事啊。"
    show sakuya 32 with dissolve
    sakuya "……小气鬼。"
    me "唔……"
    play sound "fx/eureka.ogg"
    extend "\n我要告诉小翼。"
    show sakuya 9 with dissolve
    sakuya "我，我知道了啦……真是的。\n自己花钱买总行了吧。"
    extend "\n……真是的，说话的语气像大叔一样。"
    "作哉一边小声嘟囔一边把宠物食品放到其他篮子里。"
    window hide
    stop music fadeout 1.0
    hide bg with Dissolve(0.8)
    hide sakuya with Dissolve(0.8)
    return

label day3_supply_saburo:
    show bg department_store2 at center
    play music "saburo_theme.ogg"
    window show
    me "这就是最后一项……了。"
    "当我把负责的货品都拿完了之后，三朗出现在了商品架的缝隙里。"
    "嗯……？"
    extend "那个方向是零食区的位置，\n购物单上有那样的东西吗？"
    window hide
    window show
    sakuya "三朗，怎么样？"
    extend "\n购物顺利吗？？"
    show saburo 21 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    saburo "哇啊！！吓死人了！！！"
    show saburo 7 with dissolve
    extend "\n很顺利的呢哈哈哈哈哈！"
    sakuya "……三朗，你为什么要把篮子藏起来？"
    show saburo 4 with dissolve
    saburo "呃~那个~这个~"
    me "等等，让我看一下！"
    hide saburo with dissolve
    "我强行从三朗手中拿走了篮子和笔记。"
    window hide
    window show
    sakuya "……这个零食不在购物单里吧？"
    extend "\n为什么装进篮子里了啊？？"
    show saburo 17 at top with dissolve
    saburo "啊哈哈哈！"
    extend "\n我，我啊，现在在工作呢，\n买一两样零食应该没什么问题吧~反正……。"
    extend "\n这，这是海外所说的给小费吧？"
    me "不行！"
    extend "\n还给我。"
    show saburo 6 with dissolve
    saburo "诶~！！没关系的只有一点点~。"
    sakuya "不行。"
    extend "\n要是提交收据和明细单的话，迟早会暴露的。"
    play sound "fx/eureka.ogg"
    extend "\n……如果太任性的话，我会告诉慎太郎的。"
    show saburo 12 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    saburo "呀~~~！！放过我吧！！"
    extend "\n明白了！我这就去放回去！！\n所以，千万不要跟那家伙说！"
    extend "\n我也不知道会受到什么样的惩罚……。"
    "三朗边说边心不甘情不愿地把点心放了回去。"
    window hide
    stop music fadeout 1.0
    hide saburo with Dissolve(0.8)
    hide bg with Dissolve(0.8)
    return

label day3_layout_2:
    show bg multipurpose_room2 at center with dissolve
    play music "afternoon_class.ogg"
    show tubasa 13 at topright with dissolve
    window show
    tubasa "太，太厉害了……"
    extend "\n真的跟你保证的一样，把这么大的教室给借到了。"
    "翼在多功能教室2号厅中说道。"
    show sinobu 26 at topleft with dissolve
    sinobu "嗯，总算搞定了。"
    extend "\n翼，你的构造图画的怎么样了？"
    show tubasa 5 with dissolve
    tubasa "嗯，大概完成了。"
    extend "\n大，大概是这种感觉，怎么样？"
    show sinobu 12 with dissolve
    sinobu "……嗯，不错。"
    extend "\n当天那里就是厨房，所以要把里面的门关上，\n为了防止客人误闯进去。"
    show tubasa 31 with dissolve
    tubasa "是啊。"
    extend "\n还有，那里比想象的空旷，\n该怎么办好呢？"
    me "那么，放些花朵如何？"
    extend "\n不管是日式的，欧式的，还是中式的，都合适。"
    show sinobu 26 with dissolve
    sinobu "是啊，老少男女都适合，我觉得不错。"
    "感觉，渐渐能看见咖啡店的雏形了。"
    extend "\n果然，大家一起做出来的东西，才更有意义啊。"
    extend "\n虽然对他们来说，如果能成为美好的回忆，那就好了……。"
    hide tubasa with dissolve
    hide sinobu with dissolve
    stop music fadeout 0.5
    play sound "fx/sliding_door.ogg"
    "哐哐！"
    window hide
    show cg remarkable at center with FadeWhite(0.5)
    play music "delinquent_appears.ogg"
    window show
    student_a "怎么了~？中学部的人来了！"
    student_b "不会吧，真倒霉。"
    student_c "得让他们离开，腾出教室来才行。"
    "往声音的方向看去，发现有三个体格比我们大了一圈的男生从入口处进来了。"
    tubasa "诶……为什么高等部的人会在这里……？"
    sinobu "前辈，你们有什么事吗？"
    student_a "你们这些家伙，要用这间教室举办学园祭吗？"
    student_b "如果是这样的话，那真是不好意思了，请让出来吧。"
    extend "\n我们想在这里举行乐队的演奏会呢。"
    student_c "既然是前辈的请求，你们肯定会答应的吧？"
    window hide
    hide cg with dissolve
    show sinobu 4 at topleft with dissolve
    play sound "fx/eureka.ogg"
    window show
    sinobu "我拒绝。"
    show tubasa 7 at topright with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tubasa "忍，忍君！"
    extend "\n别回答得那么快嘛……！！"
    show sinobu 5 with dissolve
    sinobu "这间教室是为了大家才争取到的。"
    extend "\n我们已经按照正规的流程申请了，所以不能让出来。"
    hide tubasa with dissolve
    hide sinobu with dissolve
    student_a "啊啊？你什么意思啊！！"
    extend "\n我们是要你们让给我们啊……这是前辈的命令。"
    student_c "身为后辈，就该老老实实听话。"
    extend "\n赶紧离开这里！"
    student_b "不那么做的话……你会尝到苦头的哦，小不点！！"
    $ renpy.transition(Quake(0, 100, 0.1, 0.065), layer='master')
    play sound "fx/dash.ogg"
    "说完，一名男学生抓住了忍的前襟。"
    window hide
    show sinobu 3 at top with dissolve
    window show
    sinobu "…"
    play sound "fx/wind_slash.ogg"
    "忍抓住他的手甩开，拉开距离，迅速摆出架势。"
    student_b "什么！？你！"
    student_a "喂，给我等一下。"
    extend "\n这家伙……我记得是空手道部初中部的主将。"
    extend "\n很强，听说还常跟着高中部主将一起训练。"
    student_c "那就正好啊？"
    extend "\n这家伙要是让我们受伤了，就会马上被要求退部吧。"
    student_b "原来如此~。"
    extend "\n就是这么回事。\n别瞎抵抗，乖乖让开。"
    extend "\n孩子就得听大人的呀？"
    show sinobu 30 with dissolve
    sinobu "可……。"
    window hide
    hide sinobu with dissolve
    window show
    me "喂，你们几个，给我适可而止。"
    extend "\n你们这种毛头小子也能叫大人了，真是可笑得让我笑得肚子疼。"
    student_a "……啊？你刚才说什么？"
    me "我说啊，像你们这样靠年龄来装大人，真是不像样。"
    extend "\n靠年龄来压别人，不觉得丢脸吗？"
    extend "\n连这种事都不知道的话，就别想当大人了哟。"
    student_b "小鬼……！"
    extend "\n竟然敢这么狂妄地教训我们！！"
    student_a "像这种不懂世故的学弟，\n必须由前辈好好地教育一番。"
    student_c "不要误会了……这不是暴力。\n是体罚！！"
    $ renpy.transition(Quake(0, 100, 0.1, 0.065), layer='master')
    play sound "fx/dash.ogg"
    "一名男生抓住我的胸襟。"
    show sinobu 30 at topleft
    show tubasa 17 at topright with dissolve
    tubasa_and_sinobu "[player_name]君！"
    stop music fadeout 0.5
    play sound "fx/wind_slash.ogg"
    "我迅速从外侧拍击对方抓我衣领的手臂肘关节，\n"
    $ renpy.transition(Quake(0, 100, 0.1, 0.065), layer='master')
    play sound "fx/dash.ogg"
    "趁他失去平衡时顺势扭转其胳膊，将其直接摁倒在地。"
    window hide
    play music "hurry_up.ogg"
    play sound "fx/entrance.ogg"
    show cg c12 2 at center with FadeWhite(0.5)
    hide tubasa with dissolve
    hide sinobu with dissolve
    window show
    me "用合气道的话，就能不伤人的制服对手呢。"
    extend "\n这样就不会受罚了哦，前辈。"
    student_c "你，你这混蛋！！"
    "男生试图用另一只手反击。"
    play sound "fx/wind_slash.ogg"
    extend "\n见状我立即扣住他受制的肘关节，锁死了他的肩膀。"
    student_c "咿呀！！"
    me "别乱动哦。"
    extend "\n虽然不会留下外伤，但可能会痛哦？"
    "说完，不知道什么时候离开的翼又回来了。"
    window hide
    hide cg with dissolve
    play sound "fx/sliding_door.ogg"
    show tubasa 18 at top with dissolve
    window show
    tubasa "[player_name]君"
    extend "\n我把老师叫来了！！"
    hide tubasa with dissolve
    play sound "fx/boing.ogg"
    student_a "什么？！"
    student_b "啧！！那家伙，什么时候……！"
    "听到这句话，我松开了男生的手臂，\n他站起身来的时候，老师走进了教室。"
    play sound "fx/dash.ogg"
    $ renpy.transition(Quake(0, 100, 0.1, 0.065), layer='master')
    nameko "你们在干什么！？"
    extend "\n都已经是高三生了，一点分寸都没有吗！！"
    umi "你们是轻音部的吧。"
    extend "\n小心受到禁止参加御咲祭的顶格处罚！"
    student_a "怎，怎么能这样！"
    student_b "我们这段时间一直在拼命练习！！"
    nameko "少说废话！！"
    extend "\n在说这些话之前，先好好反省一下自己的过失！！"
    me "老师，请等一下。"
    extend "\n那个……我们，只是稍微起了点口角，\n不需要那么严厉地责备他们。"
    nameko "什么？"
    extend "\n我听这孩子说他动了暴力。"
    window hide
    show tubasa 21 at top with dissolve
    window show
    tubasa "那，那个……。"
    hide tubasa with dissolve
    me "不是，那是因为他大声地吼我，所以我才有点\n反应过度了……。"
    extend "\n你看，我们没有哪里受伤不是吗。"
    umi "的确……。"
    extend "\n不过，当事人的你们这样说的话，那就算了。"
    me "嗯。\n老师这么忙还把您叫来，非常抱歉。"
    extend "\n前辈他们应该已经确认过我们已经得到了老师的许可了，\n所以没有问题了。"
    nameko "嗯ーー……我知道了。"
    extend "\n那我们回去吧。"
    umi "有道理。"
    extend "\n可千万不要引起骚动哦。"
    me "好的。\n非常感谢。"
    play sound "fx/sliding_door.ogg"
    "这样说完，老师就回去了。"
    window hide
    stop music fadeout 0.5
    show sinobu 4 at topleft
    show tubasa 14 at topright with dissolve
    window show
    "教室内还剩下6个人。"
    window hide
    hide tubasa with dissolve
    hide sinobu with dissolve
    hide bg with dissolve
    play music "nostalgia.ogg"
    show bg school_building_morning at center with dissolve
    window show
    student_b "喂……为什么要替我们说话？"
    me "刚才不是说已经练习很多次了吗。"
    extend "\n那么努力却因为这种事而付诸流水的话，也太可惜了吧。"
    student_b "……。"
    me "我们也是啊。"
    extend "\n为了开咖啡店，大家一起讨论，去真正的咖啡店里考察，\n我们做足了准备，一心想要把学园祭办好。"
    extend "\n所以，我很能明白那种可惜的心情啊。"
    student_b "……是我们不好。"
    extend "\n我们太沉迷于练习了，结果忘记确定地点了。"
    extend "\n然后，一时焦急……什么都不管了。"
    student_c "的确，做了那种不分轻重，丢脸的事啊。"
    extend "\n抱歉打扰了你们啊。"
    extend "\n你们和那边的家伙，都抱歉了。"
    student_a "我们也一定会用正当的方式找个好地方"
    extend "\n有时间的话，来听我们演奏吧。\n你的咖啡厅，我也会去光顾的！"
    extend "\n我们都要努力哦！。"
    window hide
    show bg multipurpose_room2 with dissolve
    show sinobu 26 at topleft
    show tubasa 13 at topright with dissolve
    window show
    tubasa "好，好的！"
    sinobu "我们等你！"
    play sound "fx/sliding_door.ogg"
    stop music fadeout 2.0
    "听了他们的话，高中部的学生离开了教室。"
    window hide
    hide bg with dissolve
    hide sinobu with dissolve
    hide tubasa with dissolve
    play music "quiet_lunch.ogg"
    show bg music_room_evening at center with dissolve
    window show
    me "呼~……总算是平平安安地过去了……。"
    show sinobu 12 at topleft with dissolve
    sinobu "辛苦了。"
    show tubasa 31 at topright with dissolve
    tubasa "[player_name]君好厉害！"
    play sound "fx/boing.ogg"
    me "啊哈哈哈！\n我永远是少年的伙伴啊！"
    extend "\n对我来说，那些孩子们，也是值得被爱的正太！！"
    stop music fadeout 0.5
    play sound "fx/ding.ogg"
    show tubasa 19
    show sinobu 16 with dissolve
    tubasa_and_sinobu "不说这句话的话明明还挺帅的……。"
    "就这样，我们完成了内部结构图，\n剩下的，就是和班上的同学一起安装了，小组的工作到此结束。"
    stop sound fadeout 0.5
    window hide
    hide tubasa with dissolve
    hide sinobu with dissolve
    hide bg with dissolve
    return

label day3_layout_2_sinobu:
    show bg shoe_locker_evening at center with dissolve
    window show
    me "好，今天也辛苦了！"
    "我换好鞋，正要走出教学楼的时候，"
    play music "sinobu_theme.ogg"
    show sinobu 8 at top with dissolve
    sinobu "[player_name]……。"
    me "咦？忍！"
    extend "\n你还没回去吗？"
    show sinobu 31 with dissolve
    sinobu "嗯。[player_name]，我在等你呢。"
    extend "\n今天我想和你一起回去。"
    play sound "fx/explosion2.ogg"
    "忍突然发来邀请啊啊啊啊啊啊啊啊啊啊啊！！！！"
    "看到这突如其来的惊喜，我拼命地抑制住自己激动到快要跳出来的心脏，看向忍的脸。"
    "夕阳的余晖洒在他的脸上，他微笑着，脸颊染上了淡淡的红晕……。"
    extend "\n这场景实在太艺术了！！"
    me "哇，哇啊啊啊~！！好，好开心啊！"
    extend "\n竟然能从忍的口中听到邀请啊！"
    show sinobu 18 with dissolve
    sinobu "是嘛，那太好了。"
    "虽然他的话语有些冷淡，"
    extend "但是表情却出奇地温柔。"
    window hide
    hide sinobu with dissolve
    show bg sidewalk_evening with Dissolve(2.0)
    window show
    "我和忍一起走在回家的路上。"
    "站在一起一看，才发觉他的身材原来这么娇小。"
    extend "\n和往常的忍重合起来看，不知为何总让人感觉十分惹人怜爱。"
    window hide
    show sinobu 3 at top with dissolve
    window show
    sinobu "[player_name]对了，刚才在多功能教室发生的事……。"
    me "嗯？怎么了？"
    show sinobu 21 with dissolve
    sinobu "谢谢你，保护了我们。"
    me "不，没什么。"
    extend "\n只是那种情况下，最适合使用合气道罢了。"
    show sinobu 12 with dissolve
    sinobu "那个既强大，又温柔的你……我也想跟你一样。"
    me "跟我一样什么的，太……太夸张了啊！"
    extend "\n你也很强大，也很温柔啊。"
    show sinobu 22 with dissolve
    sinobu "是嘛……。"
    me "是啊。"
    show sinobu 18 with dissolve
    sinobu "这样啊。"
    extend "\n[player_name]君这样说的话，那应该就是了。"
    extend "\n谢谢你……保护了我。"
    "忍向前迈了一步，带着满满的自信微笑着。"
    "（心动）"
    "最近，忍经常对我露出笑容。"
    extend "\n并且，每次看到他重新露出笑容，我的心跳都会加快。"
    "这种感觉……"
    extend "\n难道我真的，对这个孩子……！"
    show sinobu 29 with dissolve
    sinobu "[player_name]，我们一定会在御咲祭玩得开心的吧。"
    me "……嗯嗯，一定会的。"
    "只要跟忍在一起。"
    show sinobu 9 with dissolve
    sinobu "啊…。"
    "说着，忍突然停下了脚步。"
    me "嗯？怎么了？"
    window hide
    show 夕空 evening at center with dissolve
    window show
    sinobu "空……晚霞好美啊。"
    me "真的…。"
    extend "\n不过，比起晚霞，我还是更喜欢忍的笑容…。"
    window hide
    show 夕空 c37 2 with dissolve
    window show
    sinobu "诶？"
    me "没什么！自言自语而已。"
    sinobu "……要是月亮出来的话，我也能这么说来着。"
    me "诶？什么？"
    show 夕空 c37 1 with dissolve
    sinobu "没什么。别在意。"
    me "什么啊~你这样让人很在意啊。"
    extend "\n啊……快点快点！要说出来，对方才能知道你的心意嘛！"
    sinobu "……那个[player_name]君不也这样嘛。"
    extend "\n不深究对方也是温柔。"
    me "唔咕……。"
    sinobu "这种时候，直到该说的时候为止都是秘密。"
    me "说的也是……那今天这个话题就打住吧。"
    "我和忍一边聊着天，一边走着。"
    window hide
    show 夕空 evening with Dissolve(2.0)
    window show
    "在这个梦的世界里，遇到了各种各样的少年。"
    extend "\n大家都很可爱。"
    extend "\n每个人都有各自的魅力，老实说，我也想象过。"
    "但是，现在，和我在一起的这个孩子……"
    extend "忍，特别。"
    "忍，是特别的。"
    extend "我对他怀有特殊的感情。"
    window hide
    hide sinobu with dissolve
    hide cg with dissolve
    hide bg with dissolve
    hide 夕空 with dissolve
    show bg sidewalk_evening at center with Dissolve(1.0)
    show tomo 12 at topright with dissolve
    window show
    tomo "你们两人都……气氛很不错呢！"
    show tubasa 5 at topleft with dissolve
    tubasa "……嗯。总感觉很开心呢。"
    show tomo 40 with dissolve
    tomo "呜~！！"
    extend "\n虽然忍被抢走很不甘心，\n但是作为青梅竹马，我也该支持你们呢~！！"
    show tomo 19 with dissolve
    extend "\n[player_name]君，你小子可不能欺负忍，把他弄哭哦！"
    show tubasa 12 with dissolve
    tubasa "嘻嘻，我会温柔地守护你们的。"
    show tomo 6 with dissolve
    tomo "是啊~。"
    show tomo 22 with dissolve
    extend "\n但是，果然还是有点寂寞啊……。"
    show tubasa 2 with dissolve
    tubasa "……。"
    show tubasa 32 with dissolve
    extend "\n……有我陪着友哦……。"
    show tomo 21 with dissolve
    tomo "诶？为什么？\n我没听见。"
    show tubasa 7 with dissolve
    play sound "fx/cute.ogg"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    tubasa "噗嗯……没，没什么！"
    window hide
    hide tomo with dissolve
    hide tubasa with dissolve
    stop music fadeout 0.5
    hide bg with Dissolve(0.9)
    return

label day3_layout_2_tubasa:
    show bg shoe_locker_evening at center with dissolve
    window show
    me "好，今天也辛苦了！"
    "我换好鞋，正要走出教学楼的时候，"
    play music "tubasa_theme.ogg"
    show tubasa 23 at top with dissolve
    tubasa "啊。[player_name]君……。"
    me "咦？翼！"
    extend "\n你还没回去吗？"
    show tubasa 35 with dissolve
    tubasa "在，我在！"
    extend "\n那个……如果你不介意的话，要不要和我一起回家？"
    "心跳"
    me "好，好啊！！没问题！走吧！"
    window hide
    hide tubasa with dissolve
    stop music fadeout 0.5
    show bg sidewalk_evening with Dissolve(2.0)
    play music "good_scene.ogg"
    window show
    "我和翼一起走在这条上学路上。"
    me "……。"
    show tubasa 30 at top with dissolve
    tubasa "……。"
    hide tubasa with dissolve
    "气氛十分尴尬。"
    "要是被他问到关于友的恋爱话题，我可受不了。"
    extend "\n但是，"
    extend "要和翼聊其他话题，又很难和他搞好关系。"
    extend "\n我到底该怎么做才好……？"
    extend "\n本该是幸福的放学回家路上，我却纠结得喘不过气来。"
    show tubasa 32 at top with dissolve
    tubasa "[player_name]君……。"
    me "什，什么？"
    "好了，他要说什么呢……？"
    show tubasa 15 with dissolve
    tubasa "果然，像这样子和我在一起……\n你……不喜欢吗？"
    me "诶。"
    show tubasa 1 with dissolve
    tubasa "毕竟我们总是在聊我的烦恼不是吗。"
    extend "\n一直这样，果然让你不开心了。"
    me "……。"
    show tubasa 3 with dissolve
    tubasa "那，那个，从今往后那些事我自己一个人消化就可以！"
    extend "\n从今往后[player_name]君，我不会再给你添麻烦了。"
    extend "\n虽然你老是装作不介意的样子，但其实我心里都明白的。"
    show tubasa 4 with dissolve
    extend "\n……那，那就，我先走了！"
    play sound "fx/running.ogg"
    hide tubasa with dissolve
    "翼这么说着，就准备跑走。"
    me "等……！"
    "我追上翼，抓住了他。"
    "（抓）"
    $ renpy.transition(Quake(0, 100, 0.2, 0.065), layer='master')
    play sound "fx/fall_down.ogg"
    tubasa "哇！"
    "如同之前的早晨一样，翼失去了平衡，\n连带着牵着他的我的手一起摔在了地上。"
    window hide
    show cg c45 1 at center with FadeWhite(0.5)
    window show
    "面前是翼的脸。"
    extend "\n比以往都要近得多的距离。"
    me "……翼你的话，遇到这种情况，会怎么做？"
    tubasa "诶……？"
    me "遇到喜欢的人变成这种状态的情况，你会怎么做？"
    tubasa "……。"
    "虽然并不是适合提问的姿势，但翼还是在认真思考。"
    show cg c45 2 with dissolve
    tubasa "我……的话，会什么都不做……。"
    extend "\n在弄清对方的心意之前，会顺势保持原状……。"
    me "……对啊。"
    show bg evening at center
    "我从翼身上退下，抱起了他。"
    window hide
    hide tubasa with FadeWhite(1.0)
    hide cg with FadeWhite(1.0)
    window show
    me "嗯！没错！这样就行了！"
    extend "\n这才是男人嘛！！"
    "感觉心中有阳光照耀了一般。"
    extend "\n没错，在搞清楚对方的感情之前，绝对不可以做进一步的事。"
    stop music fadeout 2.0
    extend "\n而且，当发现对方对自己没有感情时，就必须果断放弃。"
    extend "\n这样就可以了。"
    window hide
    play music "good_atmosphere.ogg"
    show bg sidewalk_evening with Dissolve(1.0)
    show tubasa 23 at top with Dissolve(0.8)
    window show
    tubasa "[player_name]君……？"
    me "其实啊，我刚才也有烦恼呢。"
    extend "\n所以，那可能就表现在了脸上，让翼产生了误会。"
    extend "\n但是，多亏了翼，这个误会已经烟消云散了。\n谢谢。"
    show tubasa 2 with dissolve
    tubasa "多亏了我……？？"
    show tubasa 12 with dissolve
    extend "\n是这样啊……那真是太好了。"
    extend "\n我还以为自己被你讨厌了呢……。"
    me "没有这回事！！"
    extend "\n谁会和讨厌的人一起工作，一起回家吧！"
    extend "\n并且正相反，我最喜欢你了！"
    show tubasa 23 with dissolve
    tubasa "……是指作为同伴……？"
    me "不，是作为朋友！"
    extend "\n我们是朋友！！对吧！"
    show tubasa 36 with dissolve
    tubasa "……嗯！"
    extend "\n是朋友，呢！"
    "没错，这并不是需要每天烦恼的难题。"
    extend "\n不要过度在意细节，应该享受当下。"
    me "说起来，我们中午讨论过喜剧综艺来着，你喜欢看吗？"
    show tubasa 13 with dissolve
    tubasa "诶，啊……嗯。"
    show tubasa 34 with dissolve
    extend "\n因为我自己也不太擅长表达，"
    extend "\n所以，我很羡慕那种能滔滔不绝地说出有趣的话的人，\n或者迅速作出适当的吐槽的人。"
    me "这样啊。"
    extend "\n就像“小鬼使”里的杉本先生一样"
    me "「比起那种善于社交、很受家人亲戚欢迎的开朗孩子那种浅浅的笑容，我觉得那种内心世界丰富、沉稳的孩子发自内心的笑容更加有趣。」"
    me "我以前听说过这句话。"
    show tubasa 2 with dissolve
    tubasa "是，是这样啊……"
    show tubasa 4 with dissolve
    extend "\n一想到那个人说过这话，我都有点自信了。"
    me "啊，对了，说到「小鬼使」，\n以前他可做过更过分的事情哦~。"
    show tubasa 13 with dissolve
    tubasa "是吗！"
    extend "\n比如说，什么样子的事情？"
    me "有一次，今崎在惩罚游戏里玩过跳伞……"
    show cg blue at center with FadeWhite(0.7)
    "和翼在一起的时候，话题就一个接一个地冒出来。"
    extend "\n对，和翼在一起的时间就是这么愉快。"
    stop music fadeout 2.0
    window hide
    show cg misaki_station_evening with Dissolve(0.9)
    window show
    "我一边想着，一边和翼享受着在一起的时光，\n在车站和翼分开后，我一个人步行回家。"
    window hide
    hide bg with Dissolve(1.0)
    hide cg with Dissolve(1.0)
    hide tubasa with Dissolve(1.0)
    pause 0.4
    play music "fx/tsubame.ogg"
    show bg residential_area_evening at center with Dissolve(1.5)
    window show
    "就在这时，"
    window hide
    show sakuya 15 at top with Dissolve(0.9)
    window show
    sakuya "哟。"
    "我朝声音的方向看去，是作哉。"
    me "作哉！！你怎么在这里！"
    play sound "fx/boing.ogg"
    extend "\n难，难道说，你是和我一起"
    show sakuya 6 with dissolve
    sakuya "怎么可能啊。\n我可不想和你一起走啊。"
    extend "\n更何况，我也是坐电车上学的啊。"
    me "啊，啊哈哈哈……也对啊……"
    extend "\n所以呢，你来这里干嘛？车站不是再往前一点吗？"
    show sakuya 8 with dissolve
    sakuya "烦，烦死了！"
    extend "\n不要在意这种细节啦！！"
    stop music fadeout 0.5
    show sakuya 15 with dissolve
    sakuya "话说回来……你最近好像和一之濑关系挺好的啊。"
    me "诶？算是吧……"
    show sakuya 14 with dissolve
    sakuya "今天工作期间，你们牵着手，脸还红了。"
    extend "\n难道说，你喜欢上一之濑了？"
    me "……。"
    play music "serious.ogg"
    show sakuya 3 with dissolve
    sakuya "要是这样的话，那可真恶心啊~。我真是要退避三舍了。"
    extend "\n同性之间怎么会有恋爱这回事呢。"
    me "恋爱这种事……和性别什么的无关的。"
    show sakuya 18 with dissolve
    sakuya "哈啊？\n怎么可能无关啊。"
    extend "\n一般来说，男人都是喜欢女人的。\n你是个异类，懂吗？"
    me "一般来说是什么意思啊。"
    extend "\n用这种话随便束缚住自己，然后放弃自己坦率的愿望的话，\n那可是什么也开心不起来的，也无法变得幸福的。"
    extend "\n你也是一样，因为你喜欢一之濑君，这种心情你也明白吧？"
    show sakuya 17 with dissolve
    play sound "fx/dash.ogg"
    sakuya "哈！？怎么可能啊！！！"
    extend "\n不要把我和你混为一谈！"
    me "那种事我明白的。"
    extend "\n虽然我不清楚是不是所有这个年纪的孩子都以为自己没有被发现，\n但意外地只要站在旁边看就能看出来。"
    extend "\n你也是，也不例外。"
    show sakuya 16 with dissolve
    sakuya "别，别开玩笑了！！\n不要自以为是的教训我。"
    extend "\n你是白痴吗！？"
    me "不要被周遭的氛围影响而否定真实的自己。"
    extend "\n青春时期恋情是自由自在的。"
    extend "\n没有必要自己特意去制造障碍。"
    extend "\n毕竟长大成人后，不管愿不愿意，也不得不对社会有所顾虑。"
    me "为了不让自己长大后后悔，不要锋芒毕露哦。"
    extend "\n不过，这也是年轻人的特权……但不要过早下定论。"
    extend "\n要相互坦率地加油。那么，明天见。"
    show sakuya 4 with dissolve
    sakuya "啊，喂……！"
    hide bg with dissolve
    hide cg with dissolve
    hide sakuya with dissolve
    stop music fadeout 2.0
    play sound "fx/running.ogg"
    "我丢下作哉，跑开了。"
    window hide
    pause 0.4
    show bg residential_area_evening at center with Dissolve(1.0)
    show sakuya 30 at top with dissolve
    window show
    sakuya "可恶……他到底是什么人啊，一副领悟了的样子……。\n真是的，每个人都有点让人恼火！！"
    show sakuya 31 with dissolve
    sakuya "话说，"
    show sakuya 32 with dissolve
    extend "\n恋爱和年纪大小没有关系吧……。"
    stop music fadeout 0.5
    window hide
    hide sakuya with Dissolve(0.7)
    hide bg with Dissolve(0.7)
    window show
    "…"
    window hide
    return

label day3_3:
    pause 0.4
    show bg hallway at center with dissolve
    play music "going_to_school.ogg"
    window show
    "吃过午饭，我们再次回到教室集合。"
    extend "\n走廊上，几个正准备回家的学生往教室里探头张望。"
    show bg classroom with dissolve
    student1 "噢，是执行委员们啊。辛苦啦~！"
    student2 "今天也要一起商量吗？"
    extend "\n你们打算开什么样的咖啡店，我可是很期待的哦！"
    student3 "等到了我们可以帮忙的阶段，随时都可以来找我们哦。"
    extend "\n反正就算早早回家，也就是玩游戏打发时间而已。"
    window hide
    show tomo 4 at topleft with dissolve
    window show
    tomo "噢——谢谢你们！！"
    extend "\n我们一定会打造出一个超棒的咖啡店的！！"
    show sora 10 at topright with dissolve
    sora "能听到你们这么说，我们现在干劲满满！"
    hide sora with dissolve
    hide tomo with dissolve
    show saburo 7 at topright with dissolve
    saburo "虽然我们采购组到现在还啥都没干呢~。"
    show sakuya 1 at topleft with dissolve
    sakuya "嘘。少说废话，蠢货。"
    hide saburo with dissolve
    hide sakuya with dissolve
    student1 "一之濑作为委员代表也很辛苦吧？"
    extend "\n虽然平时没怎么和你说过话，但有什么需要帮忙的尽管告诉我哦。"
    show tubasa 17 at top with dissolve
    tubasa "好、好的。谢谢你们……。"
    hide tubasa with dissolve
    "说完，学生们便有说有笑地离开了。"
    me "友情真是美妙啊……。"
    show tuki 4 at topleft with dissolve
    tuki "是啊。"
    extend "\n御咲学园的学生们都是重情重义的好人呢。"
    show sintarou 13 at top with dissolve
    sintarou "再加上颜值也很高♪"
    show sinobu 6 at topright with dissolve
    play sound "fx/boing.ogg"
    sinobu "那根本没关系吧。"
    hide tuki with dissolve
    hide sintarou with dissolve
    hide sinobu with dissolve
    "看着学弟们能拥有如此暖心的伙伴，作为毕业生，我感到很自豪。"
    extend "\n每个人都这么有干劲，"
    extend "\n今年的御咲祭一定会办得很精彩。"
    "……御咲祭结束后，我还能继续待在这个梦境里吗？"
    extend "\n在我来到这个世界之前，许下的愿望确实只到学园祭为止。"
    extend "\n也就是说……"
    window hide
    return

label day3_3_tomo:
    show tomo 7 at top with dissolve
    window show
    tomo "[player_name]君，怎么了吗？"
    me "没、没事，没什么。"
    hide tomo with dissolve
    return

label day3_3_sintarou:
    show sintarou 22 at top with dissolve
    window show
    sintarou "怎么了~[player_name]酱。"
    me "没、没事，没什么。"
    hide sintarou with dissolve
    return

label day3_3_sinobu:
    show sinobu 2 at top with dissolve
    window show
    sinobu "怎么了？"
    me "没、没事，没什么。"
    hide sinobu with dissolve
    return

label day3_3_tubasa:
    show tubasa 1 at top with dissolve
    window show
    tubasa "[player_name]君……？"
    me "没、没事，没什么。"
    hide tubasa with dissolve
    return

label day3_3_sora:
    show sora 5 at top with dissolve
    window show
    sora "[player_name]君，怎么了？"
    me "没、没事，没什么。"
    hide sora with dissolve
    return

label day3_3_tuki:
    show tuki 6 at top with dissolve
    window show
    tuki "怎么了？[player_surname]。"
    me "没、没事，没什么。"
    hide tuki with dissolve
    return

label day3_3_saburo:
    show saburo 6 at top with dissolve
    window show
    saburo "怎么啦？[player_surname]。"
    me "没、没事，没什么。"
    hide saburo with dissolve
    return

label day3_3_sakuya:
    show sakuya 10 at top with dissolve
    window show
    sakuya "喂，怎么了？"
    me "没、没事，没什么。"
    hide sakuya with dissolve
    return

label day3_4:
    window show
    "现在去想这些也没用。"
    extend "\n先集中精神做眼前的事吧。"
    show tomo 13 at top with dissolve
    tomo "好——各位！\n今天也继续作为御咲祭实行委员加油吧！！"
    show tomo 17 with dissolve
    extend "\n那么，各个小组开始行动！！"
    hide tomo with dissolve
    "好。"
    extend "\n今天，去哪边帮忙好呢……？"
    window hide
    show 班選択 choose_group_message at center with dissolve
    return

label day3_2_sora:
    show bg classroom at center
    show sora 19 at top with dissolve
    window show
    sora "啊，这个是我做的。"
    show sora 33 with dissolve
    extend "\n……果然还是不太好吃吗？"
    "空有些拘谨地说道。"
    play sound "fx/boing.ogg"
    me "诶！？？"
    extend "\n居、居然是这样！！？？？"
    show cg dark at center with Dissolve(0.2)
    play sound "fx/ding.ogg"
    "真、真真真真的假的啊！！！你早说啊啊啊！！"
    extend "\n早知道这样，我就说些更加动听的感想了！！！！！"
    extend "\n我也是个蠢货，明明味道和其他菜不太一样，居然没发现！！！"
    extend "\n看吧，空都露出这么悲伤的表情了……啊啊啊啊啊……！！！"
    stop sound fadeout 0.5
    window hide
    hide cg with dissolve
    hide sora with dissolve
    window show
    me "不、不，不对！其实我超喜欢这种偏咸的口味！"
    extend "\n不如说，我一直都想要吃这种偏咸的鸡蛋烧啊！！！"
    extend "\n没想到空君竟然会为我做这些，我做梦都没想到！！"
    extend "\n真的很好吃！！超级美味！！"
    window hide
    show sora 30 at top with dissolve
    window show
    sora "[player_name]……谢谢你。"
    show sora 31 with dissolve
    extend "\n能听到你这么说，我很开心哦。"
    hide sora with dissolve
    show tuki 4 at topleft with dissolve
    tuki "空也说，想跟佣人一起向你道谢。"
    me "道谢？"
    extend "\n我有为空做过什么吗？"
    show sora 24 at topright with dissolve
    sora "……就、就是昨天啊，在第二厨房出现虫子的时候，\n你不仅帮了我，还一直温柔地安慰我……这是那件事的回礼哦。"
    me "啊，是那件事啊。"
    extend "\n那时候空君吓得战战兢兢的样子，真的很可爱呢~。"
    extend "\n让我看到了那么棒的场面，我反而还想报答你啊。"
    show tuki 21 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    tuki "噢！[player_surname]也这么想吗。"
    extend "\n其实我每次看到空害怕的样子，心里也会涌起一股热潮。"
    show sora 8 with dissolve
    sora "呜，你们俩太过分了~！！"
    show sora 27 with dissolve
    extend "\n我真的很害怕虫子！"
    me "那么，下次要是再出现虫子，你就直接扑到我怀里来。"
    extend "\n我会温柔地安慰你的。"
    show sora 16 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sora "才、才不要！"
    extend "\n[player_name]君大坏蛋！再也不找你帮忙了！"
    show tuki 18 with dissolve
    tuki "那就扑到我的怀里来吧。"
    extend "\n就算没有虫子我也不会介意的。"
    show tuki 21 with dissolve
    extend "\n现在也可以！！来吧！空！！！"
    show sora 15 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute3.ogg"
    sora "绝对不去！！"
    extend "\n呜~……哥哥也是，[player_name]君也是，都在把我当笨蛋耍吧！"
    show tuki 4 with dissolve
    tuki_and_me "没有没有。"
    show sora 16 with dissolve
    sora "骗人！"
    extend "\n不理你们了！"
    "月和我看着气鼓鼓的空，会心一笑。"
    window hide
    hide sora with dissolve
    hide tuki with dissolve
    window show
    me "空君真的很可爱呢~。"
    show tuki 18 at top with dissolve
    tuki "啊，真的非常可爱……。"
    me "真好啊，月君，你有个这么可爱的弟弟。"
    extend "\n太羡慕你了。"
    show tuki 8 with dissolve
    tuki "哼哼。毕竟我是当哥哥的。"
    me "嘿~。"
    extend "\n既然如此，那我就来填补一下『恋人』这个位置怎么样？~"
    show tuki 15 with dissolve
    tuki "嚯……在身为哥哥的我面前说这话啊。\n你胆子挺大的嘛。"
    me "啊哈哈，开玩笑的啦。"
    extend "\n我要是真那么做，感觉会被月君一刀两断呢。"
    show tuki 18 with dissolve
    tuki "太软弱了。"
    extend "\n身为男人，无论何时，\n都要做好这种程度的觉悟去发起挑战才对。"
    me "哦，这回答有点意外啊。"
    extend "\n难道说，这种程度的挑战，你都不介意吗？"
    show tuki 9 with dissolve
    tuki "挑战这种事不需要谁的许可。而且，"
    extend "\n[player_surname]也有优点，值得期待呢。"
    me "是、是吗……"
    extend "\n能得到赤峰家长子的评价，我感到很荣幸。"
    show tuki 4 with dissolve
    tuki "呵呵……这样啊。"
    extend "\n那你就坦率地接受吧。"
    me "……噢，嗯。"
    hide tuki with dissolve
    "本来只想开个玩笑，没想到他这么认真……。"
    extend "\n看来，他还是很给我面子的。"
    window hide
    show sora 14 at topright with dissolve
    window show
    sora "我说你们！\n从刚才开始就在嘀嘀咕咕什么呢——？"
    "已经消了气的空，疑惑地看向我们。"
    show tuki 18 at topleft with dissolve
    tuki "没什么。"
    extend "\n对吧，[player_surname]。"
    me "嗯。就是聊空很可爱啦。"
    show tuki 9 with dissolve
    tuki "没错。"
    show sora 12 with dissolve
    sora "唔……总感觉你们两个越来越像了啊……。"
    extend "\n不要啦~。光是应付哥哥一个就够我忙活的了，\n要是[player_name]君也来的话，我一定会晕过去的。"
    show cg school_building_morning at center with Dissolve(0.7)
    tuki_and_me "哈哈哈哈。"
    "就这样，我和空、月一起，享受了一顿热闹又幸福的午餐。"
    window hide
    hide bg with dissolve
    hide cg with dissolve
    hide sora with dissolve
    hide tuki with dissolve
    stop music fadeout 0.5
    return

label day3_2_tuki:
    show bg classroom at center
    show tuki 16 at top with dissolve
    window show
    tuki "这个，是我试着做的……"
    show tuki 23 with dissolve
    extend "果然，味道还是不怎么样吗？"
    extend "\n……抱歉。毕竟我也是第一次做鸡蛋烧。"
    "月的语气中带着一丝顾虑。"
    play sound "fx/boing.ogg"
    me "诶！？？"
    extend "\n居、居然是这样！！？？？"
    show cg dark at center with Dissolve(0.2)
    play sound "fx/ding.ogg"
    "真、真真真真的假的啊！！！你早说啊啊啊！！"
    extend "\n早知道这样，我就说些更加动听的感想了！！！！！"
    extend "\n我也是个蠢货，明明味道和其他菜不太一样，居然没发现！！！"
    extend "\n看吧，月都露出这么悲伤的表情了……啊啊啊啊啊……！！！"
    stop sound fadeout 0.5
    window hide
    hide cg with dissolve
    hide tuki with dissolve
    window show
    me "不、不，不对！其实我超喜欢这种偏咸的口味！"
    extend "\n不如说，我一直都想要吃这种偏咸的鸡蛋烧啊！！！"
    extend "\n没想到月君竟然会为我做这些，我做梦都没想到！！"
    extend "\n真的很好吃！！超级美味！！"
    window hide
    show tuki 24 at top with dissolve
    window show
    tuki "[player_surname]……你真是个体贴的人呢。"
    extend "\n能听到你这么说，我很开心哦。"
    hide tuki with dissolve
    show sora 2 at topright with dissolve
    sora "哥哥说他也想跟着佣人们一起向你道谢呢。"
    me "道谢？"
    me "我有做过什么让月君高兴的事情吗？"
    show tuki 25 at topleft with dissolve
    tuki "就是昨天，在第二厨房发现虫子时帮了我一把。"
    extend "\n虽然[player_surname]你当时说只是举手之劳，但我至今仍心怀感激。"
    me "啊，对哦对哦。\n那么，我就坦率地接受这份心意好了。"
    extend "\n话说回来，昨天月君手持竹刀严阵以待的样子，\n真的好帅啊~。"
    show sora 1 with dissolve
    sora "啊，果然[player_name]君也是这么想的吗？"
    extend "\n我也总是看哥哥练剑看得入迷呢。"
    extend "\n明明是双子，为什么差别会这么大呢，真是值得我好好学习啊。\n啊哈哈哈。"
    me "兼具了成熟和帅气的少年，像你这种人物\n现在可不常见哦~。"
    extend "\n在学校里肯定很受欢迎的吧？"
    show tuki 23 with dissolve
    tuki "你……你们两个，夸过头了。"
    extend "\n我并没那么了不起。"
    me "哎呀哎呀？"
    extend "\n明明是月君先对我说不要谦虚的呢，怎么轮到你谦虚了？"
    show tuki 26 with dissolve
    tuki "呜……[player_surname]可真是会欺负人呢。"
    me "啊哈哈！\n呐，空。"
    extend "\n月君他不仅是帅，\n看来也有这种非常可爱的一面哦~。"
    show sora 24 with dissolve
    sora "真的耶~！\n我也是第一次看到哥哥这个样子！"
    extend "\n确实，和平时不同，很可爱呢。"
    show tuki 10 with dissolve
    tuki "连、连空你也……"
    show tuki 23 with dissolve
    extend "\n你们两个都欺负我啊，太坏了。"
    me "哪有啦！"
    extend "\n我们只是说出自己真实的感想而已啦。"
    extend "\n对吧？空。"
    show sora 11 with dissolve
    sora "嗯！"
    extend "\n哥哥啊，身为男子汉，可不能连这种事都容不下啊！"
    show tuki 26 with dissolve
    tuki "唔……唔嗯。"
    "空和我看着脸红低下头的月，会心一笑。"
    window hide
    hide sora with dissolve
    hide tuki with dissolve
    window show
    me "真好啊空，有一个这么出色的哥哥。"
    extend "\n太羡慕你了。"
    show sora 26 at top with dissolve
    sora "诶嘿嘿……。"
    show sora 32 with dissolve
    extend "\n虽然没有直接说过这种话，\n但其实我一直觉得，能当哥哥的弟弟真是太好了。"
    extend "\n我不仅尊敬他，也一直以他为傲哦。"
    me "要是月君听到这些，一定会很开心吧~。"
    show sora 13 with dissolve
    sora "不、不准告诉他！"
    extend "\n要是说了，哥哥肯定会得意忘形的……。"
    me "啊哈哈。"
    extend "\n月君在某些地方也有点天然呆啊。"
    show sora 14 with dissolve
    sora "是啊~。"
    extend "\n哥哥他啊，身体里肯定有个开关什么的，\n一打开的话，就会变成只会横冲直撞的怪机器了。"
    me "这、这说法也太过分了……。"
    extend "\n不过话虽如此，空其实，\n连这些地方在内，都最喜欢哥哥了吧？"
    show sora 19 with dissolve
    sora "诶……！\n我、我才没说已经到了那种程度呢……"
    me "只要看看你们的日常，就知道了哦。"
    extend "\n因为你们看起来总是那么幸福，感觉特别开心呢。"
    show sora 24 with dissolve
    sora "……这么说的[player_name]君，\n其实也相当喜欢哥哥吧？"
    me "诶！？为什么你会知道……"
    show sora 34 with dissolve
    sora "因为从旁边看的话，简直一目了然啊。"
    extend "\n无论什么时候，看着哥哥的眼神都是幸福的，充满愉悦的！"
    hide sora with dissolve
    me "啊、啊哈哈……被你占上风了啊。"
    "虽然自己没意识到，但原来我就是那样看着月的吗……"
    window hide
    show tuki 5 at topleft with dissolve
    window show
    tuki "你们两个，从刚才开始就在说什么悄悄话呢？"
    "已经恢复了平时那副冷静模样的月，疑惑地看向我们。"
    show sora 34 at topright with dissolve
    sora "没什么——！"
    extend "\n我是在说哥哥好帅好可爱！！"
    extend "\n对吧？[player_name]君。"
    me "啊，嗯。"
    show tuki 28 with dissolve
    tuki "又在胡说……。"
    show tuki 23 with dissolve
    extend "\n只瞒着我说悄悄话，把我排除在外太不公平了。"
    extend "\n下次说点我们三人都能听懂的话题吧！"
    show cg school_building_morning at center with Dissolve(0.7)
    "空＆我" "啊哈哈哈。"
    "看着不顾形象、拼命想挤进话题的月，我和空都忍不住笑了出来。"
    "就这样，我和月、空一起，享受了一顿热闹又幸福的午餐。"
    window hide
    hide bg with dissolve
    hide tuki with dissolve
    hide sora with dissolve
    hide cg with dissolve
    stop music fadeout 0.5
    return

label day3_supply_2:
    play music "umesaki2.ogg"
    show bg department_store1 at center with Dissolve(0.8)
    window show
    "就这样，在我们把各自点的东西都凑齐之后，我们便去结账了。"
    extend "\n多亏了作哉的提案，不到一小时我们就买完了清单上写的所有东西。"
    show sakuya 15 at topleft with dissolve
    sakuya "好嘞。\n这样就买完了清单上写的所有东西。"
    extend "\n接下来只要买好明天的食材就可以了。"
    show saburo 25 at topright with dissolve
    saburo "怎么，这么快就搞定了啊。"
    extend "\n采购组难道是最轻松的组吗？"
    me "可能吧。"
    extend "\n那么，买好东西之后回学校吧。"
    show saburo 6 with dissolve
    saburo "诶~这么快就要回去了吗？"
    extend "\n机会难得，要不要去哪逛逛？"
    show sakuya 10 with dissolve
    sakuya "要去哪逛啊。"
    show saburo 10 with dissolve
    saburo "去游戏中心之类的或者卡拉OK之类的。"
    extend "\n毕竟今天这么快就搞定了嘛。"
    extend "\n稍微玩一下再回去也没事的。"
    "嗯……。"
    hide sakuya with dissolve
    hide saburo with dissolve
    return

label day3_supply_2_saburo:
    stop music fadeout 2.0
    window show
    "说得也是。"
    extend "\n机会难得，就去逛逛吧。"
    window hide
    play music "saburo_theme.ogg"
    window show
    me "稍微玩一下再回去吧。"
    show saburo 10 at topright with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    saburo "好嘞ー！"
    extend "\n那我们去游戏中心吧！游戏中心！！"
    show sakuya 25 at topleft with dissolve
    sakuya "你还真是喜欢啊……"
    extend "\n不过算了。"
    window hide
    hide saburo with dissolve
    hide sakuya with dissolve
    hide bg with dissolve
    show bg downtown at center with dissolve
    window show
    "我们离开百货商店，朝着游戏中心走去。"
    extend "\n我很少来这种地方，不清楚这家店的具体位置，但是\n他们两人的步调很快，感觉他们对这里很熟悉。"
    window hide
    show bg game_center1 with Dissolve(1.0)
    window show
    me "诶。"
    extend "\n在这种地方居然还有游戏厅。"
    show saburo 1 at topright with dissolve
    saburo "就是啊。"
    extend "\n话说，这里可是很有名的哦！\n[player_surname]君没有来过吗？"
    show sakuya 3 at topleft with dissolve
    sakuya "啊~确实，你好像不太会来这种地方呢。"
    extend "\n如果你是一个人的话，绝对会被小混混缠上。"
    "是是是，反正你看着也不像好人的样子。"
    window hide
    hide saburo with dissolve
    hide sakuya with dissolve
    hide bg with dissolve
    play sound "fx/crowd_noise.ogg"
    show bg game_center2 at center with Radial(0.8)
    window show
    "进入店内，各种各样的灯光和声音从游戏机中迸发出来。"
    me "哇……。"
    extend "\n不仅很吵，而且闪得让人眼睛疼，我最怕这种地方了。"
    show sakuya 25 at topleft with dissolve
    sakuya "你是大叔吗……。"
    show sakuya 23 with dissolve
    extend "\n所以，你今天要玩什么？"
    show saburo 10 at topright with dissolve
    saburo "我今天要玩的是UFO抓娃娃机！"
    me "嘿~。"
    extend "\n三朗，你很擅长抓娃娃吗？"
    show saburo 25 with dissolve
    saburo "哼哼~。"
    extend "\n这个嘛，你就看着吧。"
    hide sakuya with dissolve
    hide saburo with dissolve
    "一边说着，三朗走向了抓娃娃机，然后放下了硬币。"
    window hide
    show cg c71 1 at center with FadeWhite(0.5)
    window show
    "我看到游戏机的箱子里放着好多手掌大小的蘑菇人偶，\n它们有着一张张憨态可掬的表情。"
    me "……现在这种东西很流行吗？"
    sakuya "你这家伙，太不跟潮流了……"
    extend "\n现在学校里最流行的是吉祥物了。"
    me "诶~……吉祥物啊……。"
    "我沉浸于「不了解年轻人的品味啊」这种大叔思想中，\n而三朗一边熟练地操作着夹子，向着布偶的头顶靠近。"
    show cg remarkable with FadeWhite(0.5)
    play sound "fx/eureka.ogg"
    saburo "好~，就这一块。"
    "三朗定好目标，按下决定键，\n机械臂的嘴就张开，然后机械臂渐渐下降。"
    window hide
    show cg c72 2 with Radial(0.5)
    window show
    "被机械臂抓住的奈美太郎，可怜地被吊在机械臂上。"
    saburo "好嘞ー！"
    extend "奈美太郎get~♪"
    "奈美太郎掉到接收口后，三朗就把它拿在手上。"
    window hide
    hide cg with FadeWhite(0.5)
    show saburo 10 at top with dissolve
    window show
    saburo "怎么样♪很厉害吧。"
    extend "\n最近我很擅长这个的！"
    hide saburo with dissolve
    show sakuya 14 at topleft with dissolve
    sakuya "因为这个，你的钱包里都空空如也了。"
    show saburo 15 at topright with dissolve
    saburo "那，那个可不能说！！"
    extend "\n在这梦的游乐场，会被一下子拉回现实的！"
    me "奈美太郎啊……。"
    extend "\n的确，越看越感觉自己涌起对奈美太郎的爱，\n但也不至于为了它而穷困潦倒吧……。"
    hide saburo with dissolve
    hide sakuya with dissolve
    show saburo 19 at top with dissolve
    saburo "在说些什么啊！"
    extend "\n送给女生的话，她们肯定会高兴的！！！"
    extend "\n多亏了这个，我就成功搭讪过一次哦~"
    me "就为了这种事情……。"
    show saburo 20 with dissolve
    saburo "那当然啦！"
    extend "\n这种玩偶，就算男生带着也是很奇怪的吧。"
    hide saburo with dissolve
    show sakuya 11 at topleft with dissolve
    sakuya "你这个家伙真的是笨蛋啊~。"
    extend "\n只成功过一次，就摆着架子，还花那么多钱去抓……。"
    me "三朗君，你真是拼命啊……。"
    show saburo 31 at topright with dissolve
    saburo "别，别管我！"
    extend "\n男人什么时候都会为恋爱而拼命的！！"
    window hide
    hide sakuya with dissolve
    hide saburo with dissolve
    window show
    "作哉瞥了一眼手表。"
    show sakuya 25 at topleft with dissolve
    sakuya "啊……已经这个时间了吗。"
    extend "\n不好意思，我有点事要办，先回去了。"
    show saburo 24 at topright with dissolve
    saburo "诶，这样吗？"
    extend "\n那么，顺便把我们的东西也带去学校吧。"
    show sakuya 4 with dissolve
    sakuya "哈？"
    extend "\n为什么要我拿。"
    extend "\n你自己拿。"
    play sound "fx/running.ogg"
    hide sakuya with dissolve
    "说完，作哉就走出了游戏中心。"
    hide saburo with dissolve
    window hide
    show saburo 6 at top with dissolve
    window show
    saburo "真是冷淡呢~。"
    extend "\n我只不过是让你想顺便带着而已嘛~。"
    me "让人家带着我们全部的东西走也太过分了嘛。"
    extend "\n还是说，你有什么目的吗？"
    show saburo 20 with dissolve
    saburo "那小子，最近玩的时候经常半路溜出去~。"
    extend "\n该不会是和傻乎乎的毛头小子顺利发展，去约会了吧。"
    play sound "fx/sparkle.ogg"
    me "啊~友的事情啊！！"
    extend "可能吧！"
    extend "\n哎呀，但是啊，作哉也不能放着不管啊。"
    extend "\n那两个人，是怎样的感觉在一起呢。"
    extend "\n虽然平常互相仇视，但是一起两人世界的时候会不会很甜蜜呢？？"
    show saburo 16 with dissolve
    saburo "怎，怎么突然这么精神地聊起来了……"
    extend "\n你看上去好像对此挺有兴趣的啊。"
    me "因为，这是现实中的BL啊！！！"
    extend "\n肯定会感兴趣的啊！！"
    extend "\n啊~……光是想象就兴奋起来了啊！！"
    show saburo 9 with dissolve
    saburo "BL？那是什么。"
    me "是指男生之间的恋爱关系的词语！"
    extend "\n慎太郎给你的那本漫画也是BL啊。"
    show saburo 31 with dissolve
    stop music fadeout 2.0
    saburo "唔，唔……是这样吗。"
    extend "\nBL吗……。"
    "三朗呆呆地看着手里的奈美太郎。"
    window hide
    play music "cute_silly.ogg"
    show cg c73 1 at center with Radial(0.5)
    window show
    saburo "……呐[player_surname]，这个玩偶你要吗？"
    "这样说着，三朗把奈美太郎交给了我。"
    me "诶？可以吗？？"
    extend "\n毕竟，这个不是你拿着准备给女孩子的嘛......"
    saburo "诶，诶诶诶！反正家里有很多。"
    extend "\n……而且，你今天白天的时候说过吧。"
    extend "\n对喜欢的人，无论是男生还是女生，\n都不能够撒谎，坦诚相待很重要。"
    me "诶，嗯……"
    extend "\n但是，那个……"
    "三朗君喜欢我……！！？！？"
    show cg c73 2 with dissolve
    play sound "fx/boing.ogg"
    saburo "可，可别误会啊！！！！"
    extend "\n这，这再怎么说都是作为朋友的喜欢！！！"
    saburo "……我，可能一直以来都太执着于性别了。"
    extend "\n虽然觉得男人送男人礼物什么的很奇怪，\n不过我喜欢你，觉得你是个好人。"
    extend "\n所以……"
    extend "给你。"
    me "嗯……谢谢。"
    extend "\n会好好珍惜的。"
    hide saburo with FadeWhite(0.5)
    hide cg with FadeWhite(0.5)
    show saburo 10 at top with dissolve
    saburo "嘿嘿。"
    play sound "fx/vibrate.ogg"
    "嗡嗡……嗡嗡……"
    "突然，震动声响起。"
    show saburo 24 with dissolve
    saburo "嗯？是我的来电。"
    extend "\n是谁啊。"
    "三朗取出放在口袋里的手机接听了。"
    show saburo 32 with dissolve
    saburo "怎么了，是四朗啊。"
    hide saburo with dissolve
    "哔"
    saburo "喂，你好。"
    extend "\n嗯……嗯……"
    extend "哈？\n什么事……你自己说呀。"
    extend "\n哈啊……嗯……好。再见。"
    "哔"
    show saburo 4 at top with dissolve
    saburo "抱歉打断你说话。"
    me "没事没事。"
    extend "\n谁打来的？"
    show saburo 18 with dissolve
    saburo "我的弟弟四朗。"
    extend "\n他说今天他会晚点回家，要我帮他跟妈妈说一声。"
    extend "\n自己跟妈妈说的话会被骂的，所以他不想……。"
    extend "\n真是拿他没辙。"
    me "三朗君，你居然有弟弟啊！\n嘿~真意外啊。"
    extend "\n你们俩相差多少？"
    show saburo 32 with dissolve
    saburo "小学六年级吧~差2岁。"
    stop music fadeout 2.0
    show saburo 31 with dissolve
    extend "\n他是个调皮鬼，超嚣张的。"
    play sound "fx/eureka.ogg"
    show cg remarkable at center with Dissolve(0.2)
    play music "lively_boys.ogg"
    "哦哦哦哦是小学生呀！！！"
    extend "\n也就是说，你弟弟还是个背着书包的小朋友吧！！"
    extend "\n既然是三朗君的弟弟，那肯定很可爱吧！！"
    me "呐，呐，呐！照片之类的东西有吗？"
    extend "\n务必让我看看！！"
    window hide
    hide cg with dissolve
    hide saburo with dissolve
    show saburo 16 at top with dissolve
    window show
    saburo "你，你是不是有点太兴奋了？"
    me "没，没事~我只是好奇他会不会像哥哥一样可爱。"
    show saburo 26 with dissolve
    saburo "可，可爱……你在说什么啊傻子！"
    show saburo 31 with dissolve
    extend "\n……不过算了。\n我记得家里有照片……。"
    hide saburo with dissolve
    stop music fadeout 2.0
    "三朗玩了一会手机，然后把屏幕转给了我。"
    window hide
    play music "siro_theme.ogg"
    show cg c74 at center with Radial(0.5)
    window show
    saburo "嗯……就是这种家伙。"
    "屏幕上的，正是三朗所说，看上去有些调皮可爱的少年。"
    play sound "fx/sparkle.ogg"
    me "好可爱啊~！！"
    extend "\n短发正太，实在是太棒了……。"
    extend "\n真好啊……能有这么可爱的弟弟，太羡慕了……。"
    saburo "……嗯？\n你在搞什么鬼……"
    extend "难道喜欢这种小鬼头？"
    me "诶？不是~嘛，小学生也挺好的。"
    extend "\n还很年幼，真的很可爱啊！"
    extend "\n呐呐，还有没有其他的？"
    window hide
    hide saburo with dissolve
    hide cg with dissolve
    show saburo 22 at top with dissolve
    window show
    saburo "没有了！"
    extend "\n没有其他的了！"
    me "诶~！\n那能让我再看一眼刚才的相片吗！"
    show saburo 31 with dissolve
    saburo "啊啊！"
    show saburo 33 with dissolve
    extend "\n还有，快把奈美太郎还给我。"
    me "为，为什么啊！！"
    extend "\n难得三朗对我的好意，还把它送给我作为礼物的啊！"
    show saburo 14 with dissolve
    saburo "吵死了白痴[player_name]！"
    extend "\n我不管了！！"
    hide saburo with dissolve
    "三朗一下子把头转过去了。"
    window hide
    pause 0.4
    window show
    me "三朗……难道说，是嫉妒了？"
    "听到这话，从后方看去，三朗脸红得一目了然。"
    show saburo 22 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    saburo "有，有什么不好！！"
    extend "\n这没办法啊！！！ 这是我真实的感受！！"
    extend "\n才，才不奇怪啊！！"
    me "……是啊，一点也不奇怪。"
    extend "\n应该说是令人开心。"
    show saburo 33 with dissolve
    saburo "为，为什么啊。"
    me "因为，这正说明三朗对我的好意都直接向我表达，对我非常认真。"
    show saburo 16 with dissolve
    saburo "别，别用抱有好感这种说法……太羞耻了。"
    show saburo 31 with dissolve
    extend "\n而且，刚才也说过了，我们只是朋友！！\n不要误会！！"
    me "好好好，是这样啊。"
    show saburo 14 with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    saburo "这是什么无所谓的态度！！真的超气人的！"
    show saburo 14 with dissolve
    extend "\n把奈美太郎还给我！~~！！"
    me "那可不行。\n这是三朗对我抱有好感的证明。"
    show saburo 12 with dissolve
    saburo "哇啊啊啊。\n所以别再说这么让人误解的话了~~！！"
    window hide
    show cg evening at center with Dissolve(1.0)
    window show
    "就这样，我们在街机厅开心地玩了会儿后"
    extend "\n回到学校放下材料后就解散了，完成了采购组的工作。"
    window hide
    stop music fadeout 0.5
    hide bg with Dissolve(1.0)
    hide cg with Dissolve(1.0)
    hide saburo with Dissolve(1.0)
    return

label day3_supply_2_sakuya:
    stop music fadeout 2.0
    window show
    "不，这里不需要绕路，直接回学校吧。"
    window hide
    play music "sakuya_theme.ogg"
    window show
    me "先回学校吧！"
    extend "\n拿着材料走很累人，而且绕路也不好。"
    show saburo 28 at top with dissolve
    saburo "诶！有什么不好的嘛！"
    me "要绕路的话，等放学了再绕也行吧？"
    show saburo 18 with dissolve
    saburo "嘛……倒也是啊。"
    hide saburo with dissolve
    show sakuya 25 at topleft with dissolve
    sakuya "不也挺好嘛。"
    extend "\n那样的话，就算麻烦的工作也很快就能搞定，\n之后就无忧无虑地自由行动了不是嘛。"
    show saburo 9 at topright with dissolve
    saburo "是啊~……"
    extend "\n那要不就回学校吧。"
    window hide
    hide saburo with dissolve
    hide sakuya with dissolve
    hide bg with dissolve
    show bg school_building_full at center with Radial(0.5)
    pause 0.5
    show bg classroom with Dissolve(0.8)
    show saburo 5 at topright with dissolve
    window show
    saburo "材料放教室里就行了吧？"
    show sakuya 31 at topleft with dissolve
    sakuya "啊啊。"
    extend "\n随便放那就行了吧。"
    me "好了，这回采购组的工作总算是干完了吧。"
    show saburo 7 with dissolve
    saburo "哎呀~真是帮大忙了~。"
    show saburo 2 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    extend "\n那么~！接下来去哪玩呢？"
    show sakuya 15 with dissolve
    sakuya "啊不好意思！"
    extend "\n我还有点事要办，哒咩！"
    show saburo 11 with dissolve
    $ renpy.transition(Quake(40, 0, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    saburo "诶~！！为什么啊~！"
    extend "\n去玩嘛穗海~！！！"
    show sakuya 9 with dissolve
    sakuya "不行。"
    extend "\n想去就你自己去吧。"
    show saburo 18 with dissolve
    saburo "明白了~。"
    extend "\n那么，[player_surname]就和我一起去游戏中心~！"
    show sakuya 21 with dissolve
    sakuya "啊啊，[player_surname]不行。"
    extend "\n我这边还得用他。"
    play sound "fx/boing.ogg"
    me "诶，是这样的吗？"
    show sakuya 8 with dissolve
    sakuya "好，好啦！"
    extend "\n你留在这里！！"
    show saburo 8 with dissolve
    saburo "唔唔~什么嘛~！！"
    extend "\n要是这样的话，我也留下啊。"
    stop music fadeout 2.0
    show sakuya 3 with dissolve
    sakuya "我觉得还是不留下比较好……。"
    extend "\n因为，你，害怕那种东西吧？"
    window hide
    play music "discovery.ogg"
    show cg c80 at center with zoominout
    window show
    "这样说着，作哉把放着狗粮的包拿给三朗看。"
    play sound "fx/dash.ogg"
    saburo "诶！！！"
    extend "\n那，那是狗的……饲料！？！？"
    sakuya "就是这样。"
    extend "\n拿着这个的话，\n大概能够想象得到，我们现在要见的是什么。"
    play sound "fx/shock.ogg"
    saburo "狗，狗呜呜呜呜！！"
    extend "\n我讨厌狗绝对讨厌！！"
    extend "\n猫山家，代代都不擅长应付狗啊~~！！"
    play sound "fx/boing.ogg"
    "这不就是猫嘛！！"
    window hide
    hide saburo with dissolve
    hide sakuya with dissolve
    hide cg with dissolve
    show saburo 15 at top with dissolve
    window show
    saburo "呜……那么，我一个人去吧~……。"
    extend "\n我绝对不想见狗……。"
    extend "\n那么，你们俩，明天见吧~。"
    play sound "fx/running.ogg"
    hide saburo with dissolve
    "这样说着，三朗就垂头丧气地离开了教室。"
    stop music fadeout 0.5
    window hide
    window show
    play music "sakuya_theme.ogg"
    me "原来如此。"
    extend "\n所以，昨天也希望三朗回去呢。"
    show sakuya 5 at top with dissolve
    sakuya "就是这样！"
    extend "\n那么，走吧。"
    me "啊，嗯。"
    show sakuya 4 with dissolve
    sakuya "怎么慢吞吞的啊。"
    extend "\n是你主动说的，\n要和我一起照顾小翼的。"
    me "嗯，嗯，没错！"
    extend "\n好嘞，赶紧去见小翼吧！"
    play sound "fx/running.ogg"
    "这么说着，我迈开了脚步。"
    window hide
    hide sakuya with dissolve
    show sakuya 26 at top with dissolve
    window show
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    sakuya "等等……慢着！！"
    show sakuya 19 with dissolve
    extend "\n真是的，没必要一下子就跑起来吧......"
    window hide
    hide bg with dissolve
    hide sakuya with dissolve
    play music "fx/tsubame.ogg"
    show bg schoolyard at center with Radial(0.5)
    pause 0.4
    show bg school_backside with dissolve
    window show
    me "诶？"
    extend "\n小翼不见了。"
    stop music fadeout 0.5
    show sakuya 25 at top with dissolve
    sakuya "我来叫他，你先冷静下来。"
    "作哉一边说着一边从包里拿出一根绳子。"
    show sakuya 23 with dissolve
    sakuya "喂，小翼！出来吧！！"
    me "那根绳子是？"
    show sakuya 5 with dissolve
    sakuya "那是牵引绳。"
    extend "\n等会我用这个把小翼牵出来带出去散步。"
    window hide
    hide sakuya with dissolve
    window show
    "草木丛生的地方传来了一阵窸窸窣窣的声音，\n不久，一个小小的脑袋从里头探了出来。"
    show tsubasa 2 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tubasa "汪！汪！"
    me "噢噢~！真的冒出来了！！"
    hide tsubasa with dissolve
    show tsubasa 3 at topright
    show sakuya 24 at topleft with dissolve
    sakuya "乖乖，好孩子。"
    extend "\n看，这是小翼最喜欢的散步时间哦～。"
    extend "\n今天，因为[player_surname]也在，所以我们3人开开心心地散步吧～。"
    "作哉一边说着，一边细心地给小翼挂上了项圈。"
    show sakuya 28 with dissolve
    sakuya "好了，弄好了！"
    extend "\n走吧。"
    "作哉微笑着，牵着小翼走。"
    hide sakuya with dissolve
    hide tsubasa with dissolve
    show sakuya 12 at top with dissolve
    play sound "fx/dash.ogg"
    sakuya "喂[player_surname]，走咯。\n别发呆了。"
    play sound "fx/triangle.ogg"
    "就这样，我被拉开了一段距离。"
    window hide
    hide sakuya with dissolve
    hide tsubasa with dissolve
    hide bg with dissolve
    show bg residential_area at center with dissolve
    window show
    "我们离开学校，将小翼带到了城市里。"
    "小翼就像是在引导我们散步一样，\n精力充沛地在前方走着。"
    window hide
    show cg c81 at center with Radial(0.5)
    window show
    me "啊哈哈。\n小翼看起来很开心呢~。"
    extend "\n很喜欢散步呢。"
    sakuya "在学校里不能活动，压力积累了很多，\n所以要在这种地方发泄掉。"
    extend "\n对吧，小翼。"
    play sound "fx/cute2.ogg"
    tsubasa "汪！"
    "怎么说呢，这简直就像一家人一样。"
    extend "\n我是父亲，作哉是母亲，而小翼是小孩……太棒了。"
    "回到家后，小翼累倒了，\n我们两口子在卧室里互相治愈对方的疲劳……。"
    play sound "fx/sparkle.ogg"
    show cg adult with Radial(0.5)
    "呜哇啊啊啊！！"
    extend "\n那样的话就太棒啦啊啊啊！！！！"
    sakuya "喂。"
    play sound "fx/eureka.ogg"
    me "怎么了，亲爱的！"
    window hide
    hide sakuya with Dissolve(0.2)
    hide cg with Dissolve(0.2)
    $ renpy.transition(Quake(0, 50, 0.15, 0.09), layer='master')
    play sound "fx/punch2.ogg"
    window show
    "啪！"
    show tsubasa 3 at topright
    show sakuya 27 at topleft with dissolve
    "欠打吗？"
    me "诶……抱歉……。"
    show sakuya 5 with dissolve
    sakuya "你知道这附近有什么宽敞的公园吗？"
    me "宽敞？"
    extend "\n嗯~比如车站附近的中央公园之类的？"
    show sakuya 25 with dissolve
    sakuya "那里不行……这种时间点小孩子会很多很危险。"
    show sakuya 23 with dissolve
    extend "\n我想让小翼多自由一些。"
    extend "\n在学校里不行，在这种马路上也不行……"
    extend "\n我一直在想哪里有什么好的地方……。"
    me "自由吗……\n嗯ー……"
    extend "啊！！"
    extend "\n这样的话，我知道一个最合适的地方！！\n跟我来！"
    show sakuya 31 with dissolve
    stop music fadeout 2.0
    sakuya "诶……啊啊。"
    window hide
    hide sakuya with dissolve
    hide tsubasa with dissolve
    hide bg with dissolve
    play music "fx/tsubame.ogg"
    show bg mountain_path1 with Dissolve(0.7)
    pause 0.4
    show bg mountain_path2 with Dissolve(0.7)
    pause 0.4
    show bg mountain_path3 with FadeWhite(1.0)
    show sakuya 31 at top with dissolve
    window show
    sakuya "这，这种地方，竟然有条宽敞的道路……"
    extend "\n我都不知道。"
    me "啊啊。"
    extend "\n我初中时代，经常来这玩秘密基地。"
    extend "\n哎呀~好怀念……。"
    show sakuya 15 with dissolve
    sakuya "初中生，你是不是最近才刚上初中？"
    show sakuya 24 with dissolve
    extend "\n小翼，怎么样？"
    extend "\n第一次看到这样的自然景色吧？"
    hide sakuya with dissolve
    show tsubasa 2 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tsubasa "汪汪！"
    me "再稍微爬点上去，就能到个更好的地方了。"
    extend "\n要再稍微努力一下哦。"
    hide tsubasa with dissolve
    show tsubasa 4 at topright
    show sakuya 21 at topleft with dissolve
    sakuya "嗯。\n这种山上的小路，根本不算什么。"
    show sakuya 23 with dissolve
    extend "\n啥，那是什么？"
    show tsubasa 1 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tsubasa "汪！"
    window hide
    hide sakuya with dissolve
    hide tsubasa with dissolve
    hide bg with dissolve
    play music "fx/waves.ogg"
    show bg mountain_path4 at center with Radial(1.0)
    window show
    "我们登上了山顶，眼前出现了一片湖泊。"
    sakuya "哇……好棒……"
    extend "\n我从来都不知道还有这么漂亮的地方……"
    me "对吧~？"
    extend "\n因为这是我的秘密基地哦！"
    show tsubasa 3 at topright
    show sakuya 5 at topleft with Dissolve(0.7)
    sakuya "啊……对了，现在可不能在这里发呆了。"
    extend "\n我马上把钓钩解开~。"
    "我一边说着，一边取下了鱼钩，而小翼则一下子精神地冲了出去。"
    hide sakuya with dissolve
    hide tsubasa with dissolve
    show tsubasa 2 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute2.ogg"
    tsubasa "汪！汪汪！"
    window hide
    hide tsubasa with dissolve
    window show
    me "啊哈哈。"
    extend "\n看他这么开心，我也忍不住笑了起来。"
    show sakuya 23 at top with dissolve
    sakuya "是啊。"
    extend "\n看来平时小翼也想这样玩玩呢。"
    extend "\n……话说回来，挺厉害的嘛。\n居然会知道这么好的地方。"
    me "因为这种地方我们之前找到过很多呢。"
    show sakuya 26 with dissolve
    sakuya "真的假的……你看起来是个宅男，没想到还挺喜欢出门呢。"
    extend "\n反倒是我们，要一起玩的话"
    extend "\n不是去游戏厅就是去卡拉OK，不然就是去打保龄球，\n或者在家打打游戏……差不多就是这样。"
    me "现在的年轻人真是没救了啊。"
    extend "\n应该趁年轻的时候多出去玩玩，不然会变得越来越软弱的！"
    show sakuya 11 with dissolve
    sakuya "干，干嘛啦。"
    extend "\n我们有自己的乐趣。"
    show sakuya 19 with dissolve
    extend "\n运动的话社团活动里已经足够了。"
    extend "\n明明是同龄，你竟然用这样居高临下的语气说话"
    me "啊，是啊……抱歉抱歉。"
    window hide
    show cg evening at center with Dissolve(0.8)
    window show
    "我们暂时停止了对话，欣赏着美丽的风景。"
    extend "\n小翼依然在湖边跑着。"
    me "太阳落山了啊。"
    sakuya "……啊。"
    me "嗯？怎么了，没精打采的。"
    extend "\n果然是累了吧？"
    sakuya "不是……"
    stop music fadeout 2.0
    extend "\n我想让那家伙也到这种地方跑跑啊。"
    "那家伙……就是以前养的那条狗吗。"
    window hide
    hide cg with dissolve
    hide sakuya with dissolve
    play music "good_scene.ogg"
    show sakuya 22 at top with dissolve
    window show
    sakuya "要是能让它自由地玩就好了。"
    extend "\n以前，无论是待在家里，还是出去的时候，都得绑上绳子，\n现在想来，以前的它或许很可怜。"
    extend "\n毕竟是动物，肯定想像现在小翼一样，自由自在地跑啊跑。"
    "话虽如此，在它不在的广场上，怎么可能能找到他呢？"
    show sakuya 7 with dissolve
    sakuya "我以前一直觉得，保护好那家伙，让它待在家里，对他来说就是幸福的。"
    extend "\n但是你说得没错，我可能反而害死了它。"
    extend "\n然后我还用不好的饲料喂养了它，害得它染上了病……。\n这简直像是，出于满足自己的欲望而杀掉了它一样……。"
    me "作哉……。"
    show sakuya 34 with dissolve
    sakuya "那家伙一定一直过得很痛苦吧……。"
    extend "\n它肯定很讨厌我，"
    extend "\n所以才会想快点离开我，就这样走了……。"
    me "作哉！\n不是这样的，一定不是这样！！"
    window hide
    show cg evening at center with Dissolve(0.8)
    window show
    me "以前，我听一个想要成为兽医的人说过。\n宠物能够敏感地感受到饲主的爱！"
    extend "\n人类也一样，能够感受到对方的好意。"
    extend "\n作哉对狗狗的爱，狗狗是可以感受到的哦。"
    sakuya "……。"
    me "在你的回忆中，狗狗的脸上都是幸福的表情吧。"
    extend "\n能那么爱那家伙的，世界上也就只有作哉一个人了吧。"
    extend "\n被作哉饲养，对那家伙来说，\n是世界上最幸福的人生了……"
    extend "不对，应该是最幸福的狗生了。"
    window hide
    hide cg with Dissolve(0.8)
    hide sakuya with Dissolve(0.8)
    show sakuya 22 at top with dissolve
    window show
    sakuya "……嗯。"
    extend "\n是……这样啊……谢谢你。"
    show sakuya 7 with dissolve
    extend "\n咦……抱歉……等一下……为什么？"
    hide sakuya with dissolve
    "作哉的眼眶里泪花闪烁。"
    window hide
    show cg c82 1 at center with Radial(0.5)
    window show
    "然后，他发现后马上跑了过来，舔了舔作哉的脸颊。"
    extend "\n仿佛是在说：打起精神来！"
    sakuya "你看，小翼也在说着「打起精神来」呢。"
    sakuya "哈哈哈。\n谢谢你，小翼。"
    extend "\n也要谢谢你，这么关心我。"
    extend "\n今天说了这些话，对不起。"
    me "不用谢。"
    extend "\n我很高兴能帮上作哉的忙。"
    show cg c82 2 with Dissolve(0.8)
    sakuya "……你这家伙，真是个好人啊。"
    me "诶……啊哈哈。\n有，有吗……真不好意思啊~。"
    sakuya "……嗯。\n你真的……是个非常好的人。"
    window hide
    hide cg with Dissolve(0.8)
    hide sakuya with Dissolve(0.8)
    show sakuya 33 at top with dissolve
    window show
    sakuya "不过"
    extend "「狗生」可没有啊。「狗生」。"
    extend "\n没什么品味啊。\n就没有别的说法吗？"
    me "不，不……因为，狗的“人生”听起来实在是太奇怪了……。"
    show sakuya 35 with dissolve
    sakuya "啊哈哈。"
    extend "\n真是的，你这家伙真是傻啊~。"
    window hide
    hide sakuya with dissolve
    window show
    "我们望着黄昏中染着晚霞的湖泊，慢慢谈笑着"
    stop music fadeout 2.0
    show bg school_backside_night with Dissolve(0.8)
    extend "\n短暂享受了自由时间的翼回到学校，大家也就解散了。"
    window hide
    hide bg with Dissolve(1.0)
    return

label day3_design_2_tomo:
    window show
    "这样下去欲求不满可是会收不回来的啊！！"
    "现在就是一不做二不休……！！"
    me "那要不要现在就一起去玩？"
    extend "\n说起来~去你家怎么样？"
    hide tomo with dissolve
    hide sintarou with dissolve
    show tomo 28 at top with dissolve
    tomo "诶，我家？"
    show tomo 7 with dissolve
    extend "\n也行啊，不过没什么好玩的。啊，倒是有Uii。"
    extend "\n但是老妈出门了，所以也没什么零食。"
    me "完全不要紧！"
    extend "\n正好也想见识一下友的家是什么样的。"
    hide tomo with dissolve
    show tomo 12 at topleft
    show sintarou 12 at topright with dissolve
    play sound "fx/eureka.ogg"
    sintarou "嚯嚯……原来如此。"
    show sintarou 13 with dissolve
    sintarou "抱歉了，二位！\n这次我就不去了。"
    extend "\n还要去澡堂帮忙呢。"
    "说完慎太郎凑近我，贴着我的耳朵说。"
    hide sintarou with dissolve
    hide tomo with dissolve
    show sintarou 4 at top with dissolve
    sintarou "身为男人就要一不做二不休哦！"
    extend "\n我会为你加油的~♪"
    me "什！不，不是，不是这样的！"
    show sintarou 20 with dissolve
    sintarou "别害羞啦！"
    show sintarou 31 with dissolve
    extend "\n回头告诉我进展呦~"
    window hide
    hide sintarou with dissolve
    show tomo 21 at topleft
    show sintarou 1 at topright with dissolve
    window show
    tomo "诶，什么什么？"
    sintarou "没什么~！"
    extend "\n那么，我就先走一步了！"
    "说完慎太郎"
    play sound "fx/sliding_door.ogg"
    hide sintarou with dissolve
    hide tomo with dissolve
    "就离开了教室。"
    window hide
    show tomo 7 at top with dissolve
    window show
    tomo "慎酱也真辛苦啊。"
    show tomo 3 with dissolve
    extend "\n不过，我们现在要回家了，\n要是一起去就好了……。"
    show tomo 21 with dissolve
    extend "\n是吧？[player_name]君。"
    me "诶。啊，不是，啊哈哈。是啊。"
    "慎太郎这家伙。被他这么一说，就算我不愿意也会在意的。"
    extend "\n不，我也没觉得讨厌！！"
    "我一个人烦恼着，往友家走去。"
    window hide
    hide tomo with dissolve
    stop music fadeout 2.5
    show bg shoe_locker with dissolve
    pause 0.5
    show bg school_route with dissolve
    pause 0.5
    show bg residential_area with Dissolve(1.5)
    window show
    "话说，仔细想想，"
    extend "他妈妈不在的话，就……\n"
    play music "lively_boys.ogg"
    play sound "fx/eureka.ogg"
    "我们两人独处……！！"
    extend "\n这，这，我应该要意识到的吧！！"
    extend "\n不行。我心跳加速，感觉心快要从胸口裂开……！！！"
    "没事吧。"
    extend "发型OK？"
    extend "\n表情没有变得很奇怪？没有油光满面？"
    extend "\n服装……姑且扣上第一个扣子吧。"
    extend "\n去别人家里，要保持安静！"
    "剩下的就是……"
    window hide
    show tomo 18 at top with dissolve
    window show
    tomo "喂，[player_name]君"
    extend "\n你要去哪里啊~？"
    me "诶？呜哇！？"
    hide tomo with dissolve
    stop music
    play sound "fx/dash.ogg"
    $ renpy.transition(Quake(100, 150, 0.1, 0.07), layer='master')
    "咚"
    "我的头撞到了电线杆上。"
    "友看着这样的我，笑着说。"
    window hide
    show tomo 31 at top with dissolve
    play music "quiet_lunch.ogg"
    window show
    tomo "什么啦～。"
    extend "\n看，已经到公寓啦。\n快进去快进去！"
    window hide
    hide tomo with dissolve
    show bg moriumi_apartment with Dissolve(1.5)
    window show
    "友所指的方向，是3层高的可爱公寓，\n其外观上有着淡茶色的砖瓦拼图。"
    show tomo 12 at top with dissolve
    tomo "我家，就在这里的最上面，右手边的拐角房间！"
    "上了楼梯后，打开了301号室的门。"
    show tomo 2 with dissolve
    tomo "请进，请进！"
    me "打扰了。"
    hide tomo with dissolve
    window hide
    play sound "fx/door_open.ogg"
    show bg moriumi_living_room with Radial(1.5)
    show tomo 1 at top with dissolve
    window show
    tomo "你随便坐吧。我先去泡茶了。"
    hide tomo with dissolve
    me "嗯，嗯。谢谢你特地招待我。"
    "我在客厅的沙发上坐下，环顾四周。"
    "这里就是友的家啊……。"
    "家具收拾得干干净净，四处点缀着花盆和画作。"
    extend "\n西洋风，很时髦的感觉啊。大概是妈妈的品味吧。"
    "然后，"
    extend "四散在周围，友君的味道……！"
    extend "\n闻着这个味道，感觉心情莫名平静。"
    extend "\n之后再问问他是用什么洗洁剂来洗衣服吧？"
    "正当我这么想着的时候，友把茶送了过来。"
    show tomo 4 at top with dissolve
    tomo "请用！"
    me "谢谢。"
    "这就是友君家用的杯子吗……。"
    show tomo 12 with dissolve
    play sound "fx/sparkle.ogg"
    extend "\n是友君多次亲吻过，这个杯子……。"
    extend "\n我要开动了！！"
    "（咽口水）"
    extend "\n嗯！真好喝！！！！"
    show tomo 1 with dissolve
    tomo "那，玩什么呢~？"
    extend "\n游戏的话，有赛车和卡丁车，你想玩哪一种~？"
    show tomo 10 with dissolve
    extend "\n啊，还有《寂静陵》哦！这是从忍那借来的。"
    me "嗯~选赛车的话，卡丁车如何！"
    show tomo 4 with dissolve
    tomo "OK~♪"
    "友打开电视，启动游戏。"
    hide tomo with dissolve
    stop music fadeout 1.0
    "……看来，友的游戏技术不是很好。"
    extend "\n虽然我也不太会玩游戏，但还是打得挺开心的。"
    window hide
    play music "tomo_theme.ogg"
    show cg c16 at center with zoominout
    window show
    play sound "fx/cute.ogg"
    tomo "喵ー！！好爽！！！\n居然撞到障碍了！！！"
    extend "\n哇啊ー！被他甩得越来越远了ー！"
    play sound "fx/cute3.ogg"
    me "哇哦，真的假的~你刚刚是不是转了弯啊！！"
    extend "\n啊啊可恶，掉下去了啊啊啊……啊ー啊，垫底了……。"
    tomo "好，我来一发雷劈！！！"
    play sound "fx/cute2.ogg"
    extend "\n吃我这招啊啊！！！"
    me "哇哈哈！正好掉到赛道外的我可就不管了哦……"
    extend "\n我的道具~好，来了，护甲！！！"
    extend "\n不想被撞到的人就给我躲开啊啊啊！"
    play sound "fx/explosion2.ogg"
    extend "呀哈！保险费又要涨了！"
    play sound "fx/shock.ogg"
    tomo "呀啊啊啊别过来啊啊啊啊！！！"
    "旁人看来，肯定会觉得这游戏玩法毫无章法。\n但正因为同为低水平的人，我们才能专注于游戏本身。"
    window hide
    hide tomo with dissolve
    hide cg with dissolve
    hide bg with dissolve
    show bg moriumi_living_room_evening at center with dissolve
    window show
    me "呜……3D眩晕症要犯了。"
    extend "\n哎呀，不过说真的，现在的游戏真的是气势非凡，和红白机简直是天壤之别。"
    window hide
    show tomo 12 at top with dissolve
    window show
    tomo "稍微休息一下？"
    me "嗯，那就休息一下吧。"
    extend "\n说起来，你房间在哪？"
    show tomo 7 with dissolve
    tomo "啊，在那边，很乱的哦~？"
    extend "\n衣服什么的都扔在地上。"
    me "完全没问题哦~。"
    extend "\n我想看看，可以吗？"
    show tomo 8 with dissolve
    tomo "那也好……不过不要到处乱看！"
    me "哎呀，竟然要瞒着我吗~？好见外啊……"
    "我打开房门，走进了友的房间。"
    window hide
    hide tomo with dissolve
    play sound "fx/door_open.ogg"
    show bg tomo_room_evening with FadeWhite(0.5)
    window show
    "这里弥漫着友的味道，和整洁的客厅不同，\n正如友所说，房间确实有些杂乱，很有青春期少年的风格。"
    "现实中也是这种感觉啊~。"
    play sound "fx/cute2.ogg"
    "嗯？这比基尼内裤是什么？？"
    me "友，这个……？"
    window hide
    show tomo 7 at top with dissolve
    window show
    tomo "诶？"
    show tomo 18 with dissolve
    play sound "fx/cute3.ogg"
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    extend "啊！！！\n我忘记了收起来了！！！"
    extend "\n呜哇，别看别看！！"
    "什么！？这是友君的吗！？"
    extend "\n哦哦……他有这种兴趣吗……。"
    extend "\n……待会儿偷偷拿回去吧。"
    me "啊，这个电动按摩器……。"
    extend "\n原来是这样。友君每天都这样……"
    show tomo 20 with dissolve
    $ renpy.transition(Quake(60, 0, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    tomo "不，不不不不！！"
    extend "\n我房间里不行！！\n禁止入侵！！"
    stop music fadeout 2.0
    "咦，这反应倒是有些出乎意料。"
    extend "\n我一直以为，看他和慎太郎关系那么好，\n这种程度会完全不为所动的……。"
    me "没事，不用在意啦~！\n我们都是男生嘛~？"
    extend "\n来来来，照惯例来吧！"
    show tomo 35 with dissolve
    tomo "……如果是别人的话，我不会这么激动的。"
    me "啊？"
    window hide
    play music "good_scene.ogg"
    hide tomo with dissolve
    show cg c17 1 at center with Dissolve(2.0)
    window show
    tomo "……怎么说呢，[player_name]你……感觉有些不一样。"
    "友突然露出一本正经的表情，坐到床上低下了头。"
    me "呃……那个……。"
    tomo "我，我不知道。\n我为什么会变成这样啊！"
    extend "\n好奇怪。啊，啊哈哈。"
    "友无力地笑了笑。"
    "……。"
    "换做平时的我，会直接推倒他，\n然后强行撬开他的心房，走进他的世界……。"
    extend "\n但看到他这副表情，这次我就完全没那个想法了。"
    show cg c17 2 with dissolve
    "我坐到友的身旁，摸了摸他的头。"
    me "一点也不奇怪。"
    extend "\n友，你慢慢想就行了，\n如果能明白自己为什么会有那种感觉，那就再好不过了。"
    tomo "[player_name]君……。"
    me "嗯？怎么了？"
    tomo "啊……呜……"
    extend "\n果然没什么！！"
    extend "\n那个……嗯！我，再稍微想一下！！"
    show cg yellow with FadeWhite(0.7)
    "在这个梦的世界里，遇到了各种各样的少年。"
    extend "\n大家都很可爱。"
    extend "\n每个人都有各自的魅力，老实说，我也想象过。"
    "但是，现在，坐在眼前的这个人是……"
    extend "友，是特别的。"
    extend "\n他肯定对我怀有与对待其他人不同的，特别的感情。"
    extend "\n这世界是梦什么的，已经无所谓了。"
    extend "\n我想坦率地与友相处。"
    "所以在友自己察觉到之前，先等一下吧。"
    hide tomo with Dissolve(0.7)
    hide cg with Dissolve(0.7)
    hide bg with Dissolve(0.7)
    "\n不着急，慢慢来……。"
    window hide
    show bg moriumi_living_room_evening at center with dissolve
    window show
    me "啊，在梦醒之前。"
    window hide
    show tomo 23 at top with dissolve
    window show
    tomo "嗯？什么意思？"
    me "没什么，就我个人的想法。"
    extend "\n那么，我差不多该告辞了。\n打扰了！明天再见。"
    stop music fadeout 2.5
    window hide
    hide tomo with dissolve
    play sound "fx/door_open.ogg"
    show bg moriumi_apartment_evening with dissolve
    window show
    "就这样，我从友家出来，朝自己家走去。"
    window hide
    play sound "fx/running.ogg"
    hide bg with Dissolve(0.8)
    pause 0.6
    show bg moon_night with Dissolve(1.0)
    pause 0.6
    play music "fx/night_insects.ogg"
    show bg moriumi_apartment_night with Dissolve(1.0)
    pause 0.8
    show bg tomo_room_night with Dissolve(2.0)
    show tomo 26 at top with dissolve
    window show
    tomo "哈啊……。"
    play sound "fx/wind_slash.ogg"
    show cg remarkable at center with dissolve
    "唰！！"
    play sound "fx/sliding_door.ogg"
    extend "\n哗啦哗啦"
    hide tomo with dissolve
    hide cg with dissolve
    show tomo 30 at top with dissolve
    $ renpy.transition(Quake(0, 60, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tomo "噫！？"
    window hide
    hide tomo with dissolve
    play music "sinobu_theme.ogg"
    play sound "fx/fall_down.ogg"
    show sinobu 2 at topright with dissolve
    window show
    sinobu "……每次都来阳台打扰，真是不好意思。"
    show tomo 20 at topleft with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    tomo "忍，忍！！"
    extend "\n能不能正常地进个房间啊！！\n每次都这样，心脏真的要受不了了。"
    show sinobu 3 with dissolve
    sinobu "因为，现在从玄关进的话，\n[player_name]不就和我擦肩而过了吗？"
    show tomo 27 with dissolve
    tomo "就，就这种程度而已，没什么大不了的吧。"
    show sinobu 5 with dissolve
    sinobu "我可是很困扰的。"
    show sinobu 7 with dissolve
    extend "\n……然后呢，心意传达了吗？"
    show tomo 29 with dissolve
    tomo "呜……还，还没。"
    show sinobu 10 with dissolve
    sinobu "哈啊……真是没出息的男人。"
    show tomo 19 with dissolve
    tomo "这，这也没办法吧！！"
    extend "\n我还是第一次做这种事啊！！"
    show sinobu 5 with dissolve
    sinobu "是啊。"
    extend "\n一开始听说的时候，我也吓了一跳。"
    show tomo 35 with dissolve
    tomo "嗯…。"
    stop music fadeout 2.0
    show sinobu 4 with dissolve
    sinobu "打算什么时候说啊？"
    show sinobu 5 with dissolve
    extend "\n不过我觉得你也不用勉强去说就是了。"
    window hide
    show cg moon_night at center with dissolve
    window show
    tomo "……！"
    extend "\n再，再让我考虑一下。"
    show tomo 37 with dissolve
    extend "\n在御咲祭之前，我会给出答案的。"
    show sinobu 4 with dissolve
    sinobu "这样啊…。"
    window hide
    hide tomo with Dissolve(1.0)
    hide sinobu with Dissolve(1.0)
    hide cg with Dissolve(1.0)
    hide bg with Dissolve(1.0)
    stop music fadeout 0.5
    return

label day3_design_2_sintarou:
    window show
    "这样下去欲求不满可是会收不回来的啊！！"
    "现在就是一不做二不休……！！"
    me "那要不要现在就一起去玩？"
    extend "\n这样啊~慎太郎家怎么样？"
    show sintarou 30 with dissolve
    sintarou "可以哦~。"
    extend "\n只是间毫无趣味的澡堂，可能会有点无聊，"
    extend "\n不过要是没问题的话就请便吧~。"
    me "太好了！！\n终于可以去慎太郎家的澡堂了！"
    show tomo 25 with dissolve
    play sound "fx/eureka.ogg"
    tomo "……原来如此啊。[player_name]你也很有希望呢。"
    show tomo 24 with dissolve
    tomo "抱歉啊，你们两个！"
    extend "\n我今天之后还有事情要做，不能和你们去。"
    "说完后，友便把脸凑了上来，在我耳边说悄悄话。"
    hide sintarou with dissolve
    hide tomo with dissolve
    show tomo 25 at top with dissolve
    tomo "装得这么冷淡，你其实很积极嘛~！"
    extend "\n加油！我会支持你的♪"
    me "什！不，不是，不是这样的！"
    show tomo 31 with dissolve
    tomo "别害羞嘛~。"
    extend "\n明天再告诉我你们的事吧。"
    window hide
    hide tomo with dissolve
    show sintarou 17 at topright
    show tomo 25 at topleft with dissolve
    window show
    sintarou "嗯？你们在说什么悄悄话~？"
    show tomo 4 with dissolve
    tomo "没什么♪"
    show tomo 10 with dissolve
    extend "\n那么，我这个电灯泡就先撤了！\n再见！"
    play sound "fx/sliding_door.ogg"
    hide tomo with dissolve
    "留下这句话后，友离开了教室。"
    window hide
    hide sintarou with dissolve
    show sintarou 17 at top with dissolve
    window show
    sintarou "喂……阿友。"
    extend "\n可恶~完全是在嘲笑我呢。"
    me "啊哈哈哈……。"
    "说起来，我好像从来没有意识到过慎太郎是恋爱对象。"
    extend "\n被友嘲笑后，突然间就对慎太郎产生了兴趣。"
    "我恍惚地望着他，"
    show sintarou 28 with dissolve
    "注意到我的视线后，慎太郎回头了，\n我慌慌张张地移开视线，找起了其他话题。"
    me "啊……对了。"
    extend "\n那个，现在时间比平时充裕很多，\n稍微绕个远路可以吗？"
    hide sintarou with dissolve
    stop music fadeout 0.5
    "我这么说着，邀请慎太郎一起去。"
    extend "\n那里是……"
    window hide
    show bg shoe_locker with dissolve
    pause 0.5
    show bg school_route with dissolve
    pause 0.5
    play music "fx/tsubame.ogg"
    show bg park with Radial(1.5)
    window show
    "从神秘少年那得到过糖果的公园。"
    window hide
    show sintarou 3 at top with dissolve
    window show
    sintarou "你想绕道去的地方，是这个公园吗？"
    me "啊啊。"
    extend "\n慎太郎，你会相信我其实是25岁的大人吗？"
    show sintarou 29 with dissolve
    stop music fadeout 0.5
    sintarou "对呀~。"
    extend "\n说实话，虽然我很难想象，但我相信[player_name]但我相信你。"
    me "谢谢。"
    window hide
    play music "fx/wind.ogg"
    show cg sepia1 at center with FadeWhite(0.5)
    window show
    me "在我恢复成现在这个样子之前，\n我在这里得到了一种叫做魔法糖的东西。"
    me "给我的小孩说，这是能实现愿望的东西。"
    extend "\n我想变回初中生享受学园祭。"
    extend "\n正想着这些，就变成了这样了呢"
    window hide
    show cg sepia2 with dissolve
    window show
    "慎太郎默默地听我说话。"
    me "真的像漫画或动画一样。"
    extend "\n我不知道这个世界是梦还是现实。"
    extend "\n一开始以为是做梦，所以不当一回事，\n但是现实感太强烈，所以不敢这么想。"
    me "只能接受眼前的现实。"
    "慎太郎第一次开口说话。"
    window hide
    stop music fadeout 0.5
    hide cg with FadeWhite(0.9)
    hide bg with FadeWhite(0.9)
    hide sintarou with FadeWhite(0.9)
    pause 0.4
    play music "sintarou_theme.ogg"
    show bg park at center with Radial(0.8)
    show sintarou 19 at top with dissolve
    window show
    sintarou "[player_name]的立场看来，确实是这样……"
    me "嗯……"
    extend "\n这个我只对慎太郎你一个人说过。"
    extend "\n我觉得这是正确的判断。"
    me "因为有慎太郎在身边支持我，安慰我，"
    extend "\n我才能不害怕地在这个世界上活下去。"
    show sintarou 32 with dissolve
    sintarou "你，你刚刚竟然用很平常的语气说这些吗...能这么不害臊地说出来，是因为年龄吗？"
    show sintarou 27 with dissolve
    extend "\n能很自然地说出这种话，是那个？果然是因为年龄的关系吗？"
    "慎太郎的脸颊微微泛红。"
    extend "\n看到他这样，我察觉到了自己说了什么，"
    extend "\n回想起了友的调侃，我的脸也一下子变热了。"
    me "真真真真是失礼了！"
    extend "\n25岁还很年轻哦！！"
    show sintarou 9 with dissolve
    sintarou "是吗~？"
    extend "\n在我们看来，25岁四舍五入后30岁了，\n已经算是大叔了呢~。"
    play sound "fx/shock.ogg"
    "大受打击！！！"
    me "怎，怎么会……。\n对现在的年轻人来说，25岁就是大叔了吗……。"
    extend "\n已经不是被称作大哥哥的年龄了吗……。"
    "是这样啊……"
    extend "\n重新想想，我们之间差了10岁……"
    extend "\n我在激动个什么啊……（害羞）。"
    show sintarou 29 with dissolve
    sintarou "好！不要这么消沉啊。"
    extend "\n我的接受范围可是很大的哦"
    me "诶……？"
    show sintarou 13 with dissolve
    sintarou "你不懂吗？脑袋这么死板，果然是大叔！"
    extend "\n好了，差不多该走了吧！"
    me "别，别说大叔大叔！！"
    extend "\n……啊，走吧。"
    play sound "fx/running.ogg"
    hide sintarou with dissolve
    "离开公园，我们走向慎太郎的家。"
    show bg sky with dissolve
    "刚才的那个……能这么理解吗……？"
    window hide
    show bg evening with Dissolve(0.7)
    pause 0.5
    show bg residential_area_evening with Dissolve(0.75)
    pause 0.5
    show bg hananoyu_hallway with Radial(1.5)
    show sintarou 1 at top with dissolve
    window show
    sintarou "嘿，到了哦！"
    extend "\n欢迎光临『花乃汤』~。"
    "慎太郎的家有着大大的烟囱，是有着旧式优良传统的澡堂。"
    extend "\n也许是因为时间还早，除了我好像没有其他客人。"
    me "诶~。很有怀旧的气氛呢。"
    show sintarou 4 with dissolve
    sintarou "对吧~。"
    extend "\n这个时间段基本不会有客人，所以可以放松一下哦！"
    show sintarou 2 with dissolve
    extend "\n啊，机会难得，要不泡个澡？"
    show sintarou 13 with dissolve
    extend "\n这次特别破例，不用钱哦。"
    play sound "fx/eureka.ogg"
    "从，从慎太郎那收到了邀请……洗澡……！？"
    extend "\n能看到他不穿衣服的样子吗？"
    play sound "fx/explosion2.ogg"
    extend "\n呜哦哦哦哦哦哦！！！我要进去！进去！！"
    me "真，真的吗？！"
    extend "\n那一定要进去哦！"
    show sintarou 31 with dissolve
    sintarou "那么，左侧的更衣室是男性的更衣室。\n去那边换衣服吧。"
    "……。"
    me "诶……？"
    extend "\n那个……慎太郎先生呢……？"
    show sintarou 14 with dissolve
    sintarou "嗯？"
    show sintarou 8 with dissolve
    stop music fadeout 2.0
    extend "\n我还要打扫浴室，所以先留在这里打扫哦~。"
    hide sintarou with dissolve
    play sound "fx/ding.ogg"
    "好的。"
    extend "\n人生果然不会一帆风顺呢。"
    "……但是！！"
    extend "\n至少，在梦中可以让我享受一下吧！"
    extend "\n现实也太现实了啊啊啊！！！"
    stop sound fadeout 1.0
    hide bg with dissolve
    "怀着懊悔的心情，我沮丧地走向了更衣室。"
    window hide
    show bg changing_room at center with Dissolve(0.8)
    pause 0.5
    play sound "fx/sliding_door.ogg"
    play music "fx/bathhouse.ogg"
    show bg hananoyu with Radial(1.5)
    window show
    "砰"
    "我沐浴过后，泡进了浴缸里。"
    "唰"
    me "哈啊啊啊……好舒服……"
    extend "\n简直就是天堂啊啊啊……"
    "虽然慎太郎不在场很可惜，但泡澡还是十分舒服的……。"
    extend "\n热水也很好啊……不热不冷，身体能够完全放松下来。"
    extend "\n疲劳也消失得无影无踪。"
    "话说回来，这热水闻起来很香啊。"
    extend "\n总觉得和慎太郎的味道很相似呢。"
    "那孩子工作结束后也会来泡澡吗？"
    extend "\n肌肤一定也光滑细嫩吧……。"
    show cg adult at center with dissolve
    play sound "fx/sparkle.ogg"
    extend "\n真好啊……只要一次就好，让我摸一摸！！"
    "……正想着，他却突然出现了。"
    show bg hananoyu3 with dissolve
    extend "\n哈哈，什么嘛，原来我还是个色鬼啊！"
    extend "\n原来我在澡堂里也会春心荡漾啊，啊哈哈哈"
    window hide
    hide cg with FadeWhite(0.5)
    play sound "fx/sliding_door.ogg"
    window show
    "哐当哐当"
    sintarou "[player_name]～水温怎么样？"
    play sound "fx/boing.ogg"
    me "哇啊！慎，慎太郎！？"
    extend "\n不是在打扫外面吗…。"
    window hide
    show bg c29 1 with dissolve
    window show
    sintarou "对哦~。"
    extend "\n现在是在打扫浴室哦~。"
    "慎太郎换上了工作服，\n用手上的瓷砖刷开始刷瓷砖。"
    sintarou "不好意思打扰你洗澡了~。"
    extend "\n现在不弄的话，待会儿客人会变多的……。"
    extend "\n喂，喂，[player_name]你在听吗？"
    me "哦，哦。辛苦了！！"
    extend "\n我完全不介意！"
    sintarou "为什么你背对着我啊~？"
    me "因，因为那边有墙！"
    sintarou "你干嘛要装傻啊……。"
    extend "\n明明没什么好害羞的啊~。"
    window hide
    show bg hananoyu2 with dissolve
    window show
    "白痴！！"
    extend "\n在做下流的妄想时，本人突然出现，谁都会想逃避啊！"
    "更何况是在穿着衣服的慎太郎和我之间，\n我可是感受到了近似屈辱的羞耻啊！！"
    me "慎太郎是穿着衣服，所以没问题吧……"
    stop music fadeout 2.0
    sintarou "哈啊……真拿你没办法啊~"
    "我听到衣服摩擦的声音。"
    sintarou "嘿。这样就好了吗？"
    window hide
    play music "hurry_up.ogg"
    play sound "fx/cute2.ogg"
    show bg c29 2 with zoominout
    window show
    me "什！ ！？ 那，那个是！！！"
    "我一回头，就看到脱掉工作服的慎太郎站在那里。"
    "呜哦哦哦这次太刺激了啊啊啊啊！！！"
    "的确，羞耻感减轻了，但是……！"
    extend "\n被他这样盯着，能收起来的东西也收不起来了……别的理由也出不来了！"
    window hide
    hide bg with dissolve
    hide cg with dissolve
    window show
    "…"
    window hide
    show bg hananoyu at center with dissolve
    window show
    "泡进浴池后不到几十分钟，"
    extend "\n我盯着打扫浴场的慎太郎，\n身体就像被钉在浴池里一样。"
    show bg c29 2 with dissolve
    sintarou "那个浴室虽说暖暖的，但[player_name]泡了挺久呢。"
    extend "\n果然是因为岁数吗？"
    "不要把我当大叔啊啊啊啊！！你以为是谁的错啊！"
    extend "\n我想吐槽，但是没有力气吐槽。"
    "不行……泡晕了吗…。"
    window hide
    show bg hananoyu with DefocusWhite(0.5)
    play sound "fx/dive.ogg"
    stop music fadeout 0.5
    window show
    "咕噜咕噜咕噜"
    sintarou "好，结束了。抱歉打扰你了。"
    extend "\n我回前台了……[player_name]！？"
    window hide
    show bg hananoyu2 with FadeWhite(0.5)
    window show
    $ renpy.transition(Quake(0, 100, 0.1, 0.065), layer='master')
    play sound "fx/boing.ogg"
    sintarou "沉下去了，沉下去了呜呜呜！！！"
    window hide
    hide bg with Dissolve(0.9)
    window show
    "…"
    window hide
    show bg sintarou_room at center with DefocusBlack(5.0)
    play music "good_atmosphere.ogg"
    window show
    "当我醒来时，发现自己看着陌生的天花板。"
    window hide
    show sintarou 20s at top with dissolve
    window show
    sintarou "你醒了吗？"
    "旁边传来了慎太郎的声音。"
    me "嗯……"
    extend "\n诶……这里是？"
    show sintarou 23s with dissolve
    sintarou "这里是我的房间。"
    show sintarou 29s with dissolve
    extend "\n总之，先喝口水吧。"
    "我从慎太郎手中接过杯子，喝了一口。"
    show sintarou 29s with dissolve
    sintarou "……真是的。"
    show sintarou 32s with dissolve
    extend "\n晕倒这种麻烦事还是只有你们这些老头子才会摊上吧。"
    me "抱歉给你添麻烦了……。"
    show sintarou 29s with dissolve
    sintarou "哎呀！没事没事，别在意。"
    show sintarou 35s with dissolve
    extend "\n……毕竟我也是有原因的。\n是我没发现，抱歉。"
    "慎太郎尴尬地扭头看向一旁。"
    me "诶？\n啊，不是……只是我擅自感到很羞耻而已！"
    extend "\n都多大岁数了，还是不能有点担当啊~！！"
    extend "\n真是的，为什么我会在意那种事呢。"
    "啊啊真是的！只是因为慎太郎的小动作就让我感到很心动。"
    show sintarou 32s with dissolve
    sintarou "那，那个，那是在漫画和动画中，那种\n迷上了对方的人才会有这种现象吧？"
    me "！！"
    "我……难道是迷上了慎太郎吗……？"
    show cg orange at center with Radial(0.7)
    "在这个梦的世界里，遇到了各种各样的少年。"
    extend "\n大家都很可爱。"
    extend "\n每个人都有各自的魅力，老实说，我也想象过。"
    "但是，现在，坐在眼前的这个人是……"
    extend "慎太郎他……。"
    window hide
    hide cg with dissolve
    hide sintarou with dissolve
    show sintarou 23s at top with dissolve
    window show
    sintarou "那，那个~……我只是开个玩笑，\n不用那么认真的想这个问题……。"
    me "那，那倒也是！！"
    "慎太郎的一句话让我回过神来。"
    me "对了，店里的事情没问题吧？"
    extend "\n自从我晕倒后，你不是一直在我身边照顾我吗？"
    show sintarou 31s with dissolve
    sintarou "嗯，没问题的。"
    extend "\n我已经跟父亲母亲说过了，之后就换他们来店里帮忙了。"
    me "这样啊……\n也给你的父母添麻烦了……真的非常抱歉。"
    extend "\n不过，已经没事了，意识也恢复了很多。\n谢谢你啊。"
    show sintarou 33s with dissolve
    sintarou "……好啦，你就在这里再多休息一会儿吧。"
    me "诶，但是……"
    show sintarou 34s with dissolve
    sintarou "没事的。"
    extend "\n……你这样做的话，我也会很高兴的。"
    me "……！"
    extend "\n那，我就再休息一会儿……。"
    "我就这样躺在慎太郎的旁边。"
    window hide
    hide sintarou with Dissolve(0.7)
    hide bg with Dissolve(0.7)
    stop music fadeout 0.5
    window show
    play sound "fx/triangle.ogg"
    "过了很久，我才发现其实我什么都没穿，只是裹着毛毯。"
    stop sound fadeout 1.0
    window hide
    return

label day3_design_2_self:
    window show
    me "那么……"
    window hide
    show sintarou 15 with dissolve
    window show
    sintarou "是嘛~。"
    extend "\n昨天太晚了没能来得及去店里帮忙，"
    extend "\n今天就快点收拾完，赶紧回家吧！"
    show tomo 3 with dissolve
    tomo "是啊。今天先休息休息，明天继续努力吧！"
    show tomo 21 with dissolve
    extend "\n[player_name]刚才你好像说了什么？"
    me "啊……没有，没什么。"
    extend "\n今天就到此解散吧。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    window show
    "他们两个也是各有各的情况啊……。"
    extend "\n因为我的任性而特意抽出时间，总觉得有点对不起他们。"
    extend "\n今天就先以一个成年人的身份忍耐一下吧。"
    window hide
    show cg school_building_morning at center with Dissolve(0.7)
    window show
    "就这样，我们把散乱的道具都收拾好了，\n作为服装组，今天的任务也完成了。"
    stop music fadeout 1.0
    window hide
    hide bg with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    return

label day3_layout_sinobu_2:
    show sinobu 18 with dissolve
    window show
    sinobu "嘻嘻。是嘛。"
    extend "\n[player_name]你能这么说，真是太好了。"
    "忍露出微笑了！！"
    me "不过，和执行委员成立之初相比，\n你变得很积极了呢，忍。"
    show sinobu 26 with dissolve
    sinobu "……[player_name]是不是多亏了最初喝斥了我呢？"
    show sinobu 22 with dissolve
    extend "\n在面对某件事的时候，心情是很重要的，\n我明明应该更懂的才是。"
    me "是，是吗？\n怎么感觉有点害羞呢……"
    extend "\n我也没做什么大事哦。"
    extend "\n这次的活动也全都交给忍，我完全就是个装饰品。"
    show sinobu 31 with dissolve
    sinobu "……才没有呢。"
    extend "\n[player_name]你在的话，我……就能安心下来了。"
    me "诶？！"
    extend "\n总，总觉得，又有点害羞了呢~。"
    show sinobu 21 with dissolve
    sinobu "呵呵。明明不用害羞的…。"
    "没想到，忍竟然和我想的一样！！"
    hide sinobu with dissolve
    "虽然一开始觉得他是一个协调性不好，冷淡的男孩子，"
    extend "\n但其实我想错了，我们俩说不定很合得来！"
    "想着想着，就来到了教室。"
    window hide
    show sinobu 29 with dissolve
    window show
    sinobu "那么，叫上一之濑，赶紧去多功能教室2号厅吧。"
    stop music fadeout 1.0
    play sound "fx/running.ogg"
    window hide
    hide sinobu with dissolve
    hide bg with Dissolve(0.8)
    return

label day3_layout_tubasa_2:
    show cg class12_cafe_imagination at center with Radial(0.5)
    window show
    me "嗯。\n嗯，我记得店长说过，设置柜台的话就在这里。"
    extend "\n还有，我希望店内的座席和桌子都朝着窗户，\n所以教室必须纵向分隔。"
    tubasa "对的。\n那么，就在这里安装窗帘吧……。"
    extend "\n另外，店是禁烟的对吧？"
    me "嗯。\n我记得，学校本身是禁烟的，吸烟区是另外设置的。"
    tubasa "那么，为了让学生们更好理解，\n入口处和墙壁上贴上标识比较好。"
    extend "\n『美馨儿咖啡』就是这样做的。"
    me "哦~你观察得很仔细呢！"
    "我们一边听着在『美馨儿咖啡』的体验和建议，\n一边想象着完成后的样子，顺利地进行着作业。"
    window hide
    hide tubasa with Radial(0.5)
    hide cg with Radial(0.5)
    window show
    me "好！差不多是这种感觉。"
    extend "\n不愧是我和翼，配合得越来越好了！"
    show tubasa 4 at top with dissolve
    tubasa "哎嘿嘿……是的。"
    me "翼也比最开始要积极主动多了。\n真让人佩服！"
    show tubasa 37 with dissolve
    tubasa "哎，是吗……。"
    extend "\n这一定是[player_name]君在不断督促我的结果。"
    me "没有没有，我也没有做什么了不起的事啊。"
    extend "\n是翼自己意识有所改变的。"
    show tubasa 23 with dissolve
    tubasa "不是的。\n让我想法有所改变的人是你啊，[player_name] 君。"
    extend "\n我，[player_name]我真的很高兴你能陪在我身边…。"
    me "是，是吗？"
    extend "\n哎呀~翼能这么说，我都有点不好意思了。"
    show tubasa 35 with dissolve
    tubasa "是，是啊。"
    extend "\n我自己说出来都感觉有点不好意思了…。"
    me "什，什么嘛~！"
    hide tubasa with dissolve
    "看到满脸通红的翼，我再次动摇了。"
    "不行不行……不能背叛翼。"
    extend "\n冷静冷静……"
    stop music fadeout 0.5
    "砰"
    "啊，橡皮擦掉了。"
    "我弯下腰伸出手，"
    extend "与此同时，另一只手也伸了出来，\n正好和橡皮擦重合在了一起。"
    window hide
    hide tubasa with dissolve
    play music "tubasa_theme.ogg"
    show cg c43 at center with FadeWhite(0.5)
    window show
    "翼＆我" "啊…。"
    play sound "fx/heartbeat.ogg"
    "扑通扑通扑通！！！"
    "心跳声更加激烈了。"
    extend "\n我，我是少女漫画的男主角啊！"
    "正当我僵直在原地时，翼先捡起了橡皮，递给了我。"
    window hide
    hide cg with dissolve
    hide tubasa with dissolve
    show tubasa 5 at top with dissolve
    window show
    tubasa "来，给你。"
    extend "\n……？"
    show tubasa 2 with dissolve
    extend "\n[player_name]君，你怎么了？"
    play sound "fx/boing.ogg"
    me "啊，没，没什么。"
    "我才是真有问题……。"
    "这里是我现在所在的教室。"
    extend "\n在教室里，明明是如此微不足道的小事，却让我如此激动。"
    window hide
    play sound "fx/vibrate.ogg"
    window show
    "嘟嘟"
    "翼的手机响了起来。"
    show tubasa 13 with dissolve
    tubasa "啊，是忍酱。"
    hide tubasa with dissolve
    tubasa "嗯，你好。"
    extend "\n……真的吗，那太好了！"
    extend "\n嗯，嗯，我知道了。"
    extend "\n那我马上过去。"
    "哔"
    show tubasa 31 at top with dissolve
    tubasa "忍君他顺利地借到了多功能教室2号厅！"
    extend "\n为了能确认一下，我们就在那里会合吧。"
    me "哦，好！太好了。"
    extend "\n那我们就赶紧过去吧。"
    show cg school_building_morning at center with Dissolve(1.0)
    "没错。我现在是执行委员。"
    extend "\n工作时间就该专心工作！不要被其他事分散注意力。"
    extend "\n必须作为一个成年人，理清自己的立场，做个了断！"
    window hide
    hide tubasa with dissolve
    hide cg with dissolve
    hide bg with dissolve
    stop music fadeout 0.5
    return

label day3_layout_sinobu_2_noday2:
    hide sinobu with dissolve
    show sinobu 29 at top with dissolve
    window show
    sinobu "谢谢。"
    extend "\n那这样就顺利地确定了地点，\n叫上一之濑同学，赶紧去多功能教室2号厅吧。"
    stop music fadeout 1.0
    window hide
    hide bg with Dissolve(0.8)
    hide sinobu with Dissolve(0.8)
    return

label day3_layout_tubasa_2_noday2:
    show cg class12_cafe_imagination at center with Radial(0.5)
    window show
    tubasa "根据前几天去的「美馨儿咖啡」的店长的说明，\n如果想要设置柜台座位，这里是最适合的。"
    extend "\n而且，无论是座位还是桌子都希望面向窗户，\n所以教室必须被纵向切割。"
    me "诶~特意去真正的咖啡厅调查过了啊。"
    tubasa "嗯，学到了很多。"
    extend "\n……因为是初体验，非常羞耻……。"
    play sound "fx/cute.ogg"
    "什，什么，羞耻的初体验是什么啊！！？"
    show cg remarkable with FadeWhite(0.5)
    play sound "fx/explosion2.ogg"
    "翼老师！请详细地告诉我！！！！"
    window hide
    hide tubasa with Radial(0.5)
    hide cg with Radial(0.5)
    show tubasa 12 at top with dissolve
    window show
    tubasa "然后在这里挂上窗帘……。"
    extend "\n另外，店是禁烟的对吧？"
    play sound "fx/boing.ogg"
    me "诶！？啊，嗯。\n我记得，校舍本身是禁烟的，所以吸烟的地方另设。"
    show tubasa 5 with dissolve
    tubasa "那么，为了让学生们更好理解，\n入口处和墙壁上贴上标识比较好。"
    extend "\n『美馨儿咖啡』就是这样做的。"
    hide tubasa with dissolve
    "我们根据翼去过的「美馨儿咖啡」提供的体验和建议，\n想象着完成品的样子，顺利地进行着制作。"
    window hide
    play sound "fx/vibrate.ogg"
    window show
    "嘟嘟"
    "翼的手机响了起来。"
    show tubasa 13 at top with dissolve
    tubasa "啊，是忍酱。"
    hide tubasa with dissolve
    tubasa "嗯，你好。"
    extend "\n……真的吗，那太好了！"
    extend "\n嗯，嗯，我知道了。"
    extend "\n那我马上过去。"
    "哔"
    show tubasa 31 at top with dissolve
    tubasa "忍君他顺利地借到了多功能教室2号厅！"
    extend "\n为了能确认一下，我们就在那里会合吧。"
    me "哦，好！太好了。"
    extend "\n那我们就赶紧过去吧。"
    stop music fadeout 1.0
    window hide
    hide tubasa with Dissolve(0.8)
    hide bg with Dissolve(0.8)
    return

label day3_supply_self:
    show bg department_store2 at center
    play music "cute_silly.ogg"
    window show
    me "这就是最后一项……了。"
    "我将要负责的东西都收集完毕之后，便从商品架的缝隙中看到了作哉和三朗。"
    "嗯……？"
    extend "那里，是游戏区的位置，\n但是采购清单上不可能有那个……的啊。"
    window hide
    window show
    me "喂，你们两个。"
    extend "\n在这干什么呢？？"
    show saburo 21 at topright with dissolve
    $ renpy.transition(Quake(0, 40, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    saburo "哎，[player_surname]……。"
    show sakuya 15 at topleft with dissolve
    sakuya "啊啊，被发现了。"
    me "还以为你突然变得正经了呢，结果还是老样子啊。"
    extend "\n虽然我觉得你们已经知道了，但你们可别用收到的钱去玩啊。"
    show saburo 9 with dissolve
    saburo "诶诶，我们知道的啦~。"
    show sakuya 24 with dissolve
    sakuya "但是，我们还剩了挺多钱的，就算不拿来玩，\n稍微买点别的东西也没关系的吧……。"
    play sound "fx/eureka.ogg"
    me "会挨骂的。"
    show saburo 8
    show sakuya 11 with dissolve
    play sound "fx/boing.ogg"
    sakuya_and_saburo "小气！"
    me "就是小气了才好。"
    extend "\n而且，你们也要提交收据和明细的，反正你们的事情已经暴露了。"
    extend "\n老师还唠唠叨叨地批评你们也挺麻烦的吧。"
    show saburo 6 with dissolve
    saburo "嘛~，虽然这么说也是有道理啦。"
    show sakuya 19 with dissolve
    sakuya "真是的。[player_surname]啊，平时的时候就喜欢胡闹，\n只有这种时候突然变得很正经呢~。"
    window hide
    stop music fadeout 1.0
    hide bg with Dissolve(0.8)
    hide sakuya with Dissolve(0.8)
    hide saburo with Dissolve(0.8)
    play music "umesaki2.ogg"
    show bg department_store1 at center with Dissolve(0.8)
    window show
    "就这样，在我们把各自点的东西都凑齐之后，我们便去结账了。"
    extend "\n多亏了作哉的提案，不到一小时我们就买完了清单上写的所有东西。"
    show sakuya 15 at topleft with dissolve
    sakuya "好嘞。\n这样就买完了清单上写的所有东西。"
    extend "\n接下来只要买好明天的食材就可以了。"
    show saburo 25 at topright with dissolve
    saburo "怎么，这么快就搞定了啊。"
    extend "\n采购组难道是最轻松的组吗？"
    me "可能吧。"
    extend "\n那么，买好东西之后回学校吧。"
    window hide
    show cg sky at center with Dissolve(0.7)
    window show
    "就这样，我们把采购的材料放在了学校之后就解散了，\n然后顺利地完成了今天的任务。"
    stop music fadeout 1.0
    window hide
    hide bg with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    hide saburo with Dissolve(0.8)
    hide sakuya with Dissolve(0.8)
    return

label day3_design_sirou:
    hide 班選択 with dissolve
    window show
    "去『服装制作组』看看吧！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "quiet_lunch.ogg"
    window show
    me "那么，我要做些什么才好呢？"
    show tomo 1 at topleft with dissolve
    tomo "[player_name]君，我们小组的工作到昨天就已经完成了哦。"
    show sintarou 1 at topright with dissolve
    sintarou "所以，今天就解散吧！"
    extend "\n我们也可以回家了哦~。"
    me "诶！怎，怎么这样！！"
    extend "\n那么，今天开心的校园生活，就要到此结束了？！"
    show tomo 3
    show sintarou 15 with dissolve
    tomo_and_shin "嗯。"
    window hide
    hide tomo with dissolve
    hide sintarou with dissolve
    play sound "fx/shock.ogg"
    window show
    "轰！！"
    me "诶诶诶诶诶！！怎么可以这样……。"
    extend "\n这样我可是不满足的啊啊啊啊啊……。"
    show tomo 8 at topleft with dissolve
    tomo "[player_name]君，这是怎么了呢……？"
    show sintarou 27 at topright with dissolve
    sintarou "谁知道……我不知道。"
    show tomo 2 with dissolve
    tomo "那么，我们，现在就回家吧！！\n拜拜！"
    show sintarou 8 with dissolve
    sintarou "[player_name]老师，明天见~！"
    window hide
    play sound "fx/running.ogg"
    hide tomo with dissolve
    hide sintarou with dissolve
    return

label day3_supply_sirou:
    hide 班選択 with dissolve
    window show
    "去「采购组」吧！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "quiet_lunch.ogg"
    window show
    me "那么，我要做些什么才好呢？"
    show saburo 10 at topright with dissolve
    saburo "这·是·说·呢~！"
    extend "高兴吧，[player_surname]！！"
    extend "\n刚才已经和各个小组确认过了，我们的工作在昨天之前就结束了，\n今天就可以回家了！"
    show sakuya 6 at topleft with dissolve
    "真是的，真会挑时间。一直都在划水。"
    extend "\n至今为止有好好地派上用场吗。"
    me "诶！怎，怎么这样！！"
    extend "\n那么，今天开心的校园生活，就要到此结束了？！"
    show saburo 17 with dissolve
    saburo "是啊！很高兴吧。"
    window hide
    hide saburo with dissolve
    hide sakuya with dissolve
    play sound "fx/shock.ogg"
    window show
    "轰！！"
    me "诶诶诶诶诶！！怎么可以这样……。"
    extend "\n这样我可是不满足的啊啊啊啊啊……。"
    show sakuya 10 at topleft with dissolve
    sakuya "这家伙，说什么呢？"
    show saburo 24 at topright with dissolve
    saburo "这里应该高兴才对。"
    show sakuya 15 with dissolve
    sakuya "奇怪的家伙……。"
    extend "\n那么，猫山，我们回家吧。"
    show saburo 5 with dissolve
    saburo "噢！"
    show saburo 4 with dissolve
    extend "\n那回头见~[player_surname]。"
    window hide
    play sound "fx/running.ogg"
    hide saburo with dissolve
    hide sakuya with dissolve
    return

label day3_layout_sirou:
    hide 班選択 with dissolve
    window show
    "去『布置组』看看吧！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "quiet_lunch.ogg"
    window show
    me "那么，我要做些什么才好呢？"
    show sinobu 1 at topleft with dissolve
    sinobu "……你什么都不用做哦。已经结束了。"
    show tubasa 5 at topright with dissolve
    tubasa "昨天，我们就已经把能做的全部都做了。"
    extend "\n所以，今天你可以先回家了。"
    me "诶！怎，怎么这样！！"
    extend "\n那么，今天开心的校园生活，就要到此结束了？！"
    show tubasa 17 with dissolve
    tubasa "那个……也是啊。"
    window hide
    hide sinobu with dissolve
    hide tubasa with dissolve
    play sound "fx/shock.ogg"
    window show
    "轰！！"
    me "诶诶诶诶诶！！怎么可以这样……。"
    extend "\n这样我可是不满足的啊啊啊啊啊……。"
    show tubasa 20 at topright with dissolve
    tubasa "[player_name]君，怎么了？"
    show sinobu 4 at topleft with dissolve
    sinobu "谁知道呢……？"
    extend "\n那么，我们就先回去了。"
    show tubasa 21 with dissolve
    tubasa "那个……再，再见。"
    window hide
    play sound "fx/running.ogg"
    hide sinobu with dissolve
    hide tubasa with dissolve
    return

label day3_cooking_sirou:
    hide 班選択 with dissolve
    window show
    "去『料理组』看看吧！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "quiet_lunch.ogg"
    window show
    me "那么，我要做些什么才好呢？"
    show sora 2 at topright with dissolve
    sora "[player_name]君，我们组到昨天为止所有的作业就已经完成了，\n所以今天你可以先回家了。"
    show tuki 4 at topleft with dissolve
    tuki "让你特地跑一趟真是不好意思啊。"
    extend "\n今天你就在家好好休息吧。"
    me "诶！怎，怎么这样！！"
    extend "\n那么，今天开心的校园生活，就要到此结束了？！"
    show tuki 1
    show sora 4 with dissolve
    tuki_and_sora "……嗯。"
    window hide
    hide sora with dissolve
    hide tuki with dissolve
    play sound "fx/shock.ogg"
    window show
    "轰！！"
    me "诶诶诶诶诶！！怎么可以这样……。"
    extend "\n这样我可是不满足的啊啊啊啊啊……。"
    show sora 5 at topright with dissolve
    sora "哥哥，[player_name]君，怎么了？"
    show tuki 5 at topleft with dissolve
    tuki "谁知道呢？\n你应该是很高兴能早点回家吧？"
    show sora 1 with dissolve
    sora "啊哈哈。是啊！这样就好了。"
    extend "\n那么，[player_name]君，明天见！"
    show tuki 8 with dissolve
    tuki "再见。"
    extend "\n可别太兴奋被车撞了哦。"
    window hide
    play sound "fx/running.ogg"
    hide sora with dissolve
    hide tuki with dissolve
    return

label day3_sirou:
    stop music fadeout 0.5
    pause 0.4
    show cg school_building at center with Dissolve(0.7)
    play sound "fx/ding.ogg"
    window show
    "……。"
    "其他组都已经去做其他工作了，我也回家吧……。"
    extend "\n明明有那么多男孩子，但没一个能跟我一块儿回家。"
    extend "\n唉……。"
    window hide
    stop sound fadeout 0.5
    hide bg with Dissolve(0.7)
    hide cg with Dissolve(0.7)
    play music "fx/tsubame.ogg"
    show bg school_route at center with Dissolve(0.7)
    pause 0.4
    show bg sidewalk with Dissolve(0.7)
    pause 0.4
    show bg intersection with Dissolve(1.2)
    window show
    "走出学校之后，我无精打采地走在回家的路上。"
    "就在这时"
    show bg sky with FadeWhite(0.5)
    unknown "呜哇！！"
    me "诶！？"
    $ renpy.transition(Quake(0, 70, 0.15, 0.09), layer='master')
    play sound "fx/fall_down.ogg"
    "咚！"
    stop music fadeout 0.5
    "一个背着书包的小男孩突然从拐角处冲了出来。"
    window hide
    play music "siro_theme.ogg"
    show cg c84 at center with Radial(0.5)
    window show
    unknown "痛痛痛痛痛……"
    extend "\n啊……对，对不起！！\n你没事吧？"
    me "诶……我，我没事，但是你才是，膝盖都擦到了，受伤了吧！"
    unknown "诶？"
    play sound "fx/boing.ogg"
    extend "\n啊啊啊啊真的啊！！\n我一回过神来，膝盖就突然开始疼了……。"
    me "真，真糟糕……\n消，消毒液……没有吧。"
    extend "\n该怎么办呢……。"
    unknown "没，没事的！"
    show bg intersection
    extend "\n撞到你的人是我，所以你不用在意……。"
    "说完后，背着书包的小男孩试图站起来，"
    window hide
    hide cg with dissolve
    show sirou 1 at top with dissolve
    window show
    unknown "呜……！"
    "但因为腿上伤口的疼痛，他做不到。"
    me "别逞强了，在附近的公园休息一下吧。"
    extend "\n来吧，我来背你，坐在我的背上。"
    "我背对着小男孩蹲了下来。"
    show sirou 2 with dissolve
    unknown "诶……但，但是……"
    me "别客气了！"
    extend "\n这种时候就该老老实实地听大人的话。"
    show sirou 3 with dissolve
    unknown "啊……嗯！谢谢你。"
    extend "\n……那么，失礼了。"
    window hide
    hide sirou with dissolve
    window show
    "说完，少年便贴着我的背，双臂架到了我的肩膀上。"
    "等站起来后，我想到自己正背着一个背着书包的少年，这个画面有点傻乎乎的，又有点好笑"
    window hide
    show cg c85 at center with Radial(0.5)
    window show
    unknown "那个……您不觉得重吗？"
    me "没问题的。"
    extend "\n倒不如说，感觉很舒服！"
    unknown "舒服？"
    "和小学生的纤细身体贴得这么紧，感觉好舒服啊！"
    play sound "fx/eureka.ogg"
    extend "\n完全不会觉得累！！"
    "啊……少年的体温，还有香甜的气息也能够感觉到……。"
    play sound "fx/sparkle.ogg"
    extend "\n这是何等……何等幸福的时光……。"
    extend "\n一辈子都这样也行啊……！！"
    play sound "fx/boing.ogg"
    unknown "哥，哥哥！！你喘着粗气呢！"
    extend "\n果然很累吧……。"
    me "没有没有没有，完全相反哦！！"
    show cg remarkable with FadeWhite(0.5)
    play sound "fx/explosion2.ogg"
    extend "\n我的力气正喷涌而出！"
    unknown "诶，诶诶诶诶诶！！？"
    show cg sky with FadeWhite(0.5)
    play music "fx/wind_slash.ogg"
    "看着忍不住开始跑起来的我，少年疑惑地叫出声来。"
    "没关系！再多让我听听那种声音吧！！"
    extend "\n虽然没办法和大家一起回去让我很遗憾，\n但是，这或许就是和这个孩子相遇的命运！！"
    stop music fadeout 2.0
    window hide
    hide cg with dissolve
    hide bg with dissolve
    hide sirou with dissolve
    pause 0.4
    play music "fx/tsubame.ogg"
    show bg park_bench at center with Radial(0.7)
    window show
    "我兴奋地向前跑着，很快到达了公园。"
    extend "\n虽然有些舍不得，但我还是让少年坐在长凳上。"
    me "稍微等我一下哦。"
    "说完，我在稍远的地方找到一个水龙头，将水倒进手里的碗里。"
    window hide
    pause 0.3
    window show
    me "可能会有点疼，你忍一下哦。"
    "回到少年身旁，我开始用水给他洗膝盖。"
    show sirou 1 at top with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/boing.ogg"
    unknown "好痛……。"
    "痛苦的表情在少年脸上蔓延开来。"
    window hide
    show cg evening at center with dissolve
    window show
    me "……嗯，我是不是该用更温柔一点的方式呀？"
    "我蹲下来，脸靠近少年的下半身。"
    "然后伸出舌头"
    stop music fadeout 0.5
    window hide
    play music "emergency.ogg"
    show cg c86 with Radial(0.5)
    window show
    "舔"
    play sound "fx/cute.ogg"
    unknown "诶……大，大哥哥！"
    extend "\n这，这样好脏！！"
    extend "\n住，住手……！"
    me "好啦，乖乖别动。"
    me "这样做可以进行消毒，而且也能加快恢复哦。"
    unknown "真的吗……？"
    me "啊啊，唾液中含有杀菌的成分哦。"
    window hide
    hide cg with dissolve
    hide sirou with dissolve
    window show
    stop music fadeout 2.5
    "我将他的膝盖全部舔完一遍，突然回过神来。"
    "手指的割伤舔舔也就算了，连膝盖的伤口都舔是不是太过头了！？"
    "我战战兢兢地抬起头，只见少年正笑嘻嘻地看着我。"
    window hide
    play music "siro_theme.ogg"
    show sirou 4 at top with dissolve
    window show
    play sound "fx/sparkle.ogg"
    "消毒都考虑得到，谢谢大哥哥帮我！"
    extend "\n大哥哥真是既亲切又聪明呢~！"
    extend "\n我也要好好学习，和大哥哥一样也能够做到这些事。"
    play sound "fx/boing.ogg"
    me "咦……啊，啊哈哈！"
    extend "\n不用谢~。"
    show sirou 5 with dissolve
    unknown "那个，可以的话，能请教一下你的名字吗？"
    extend "\n我叫四朗。"
    me "四朗啊……是个好名字。"
    extend "\n就叫我[player_name]吧。\n请多指教，四朗。"
    show sirou 3 with dissolve
    sirou "好的，[player_name]同学！"
    show sirou 5 with dissolve
    extend "\n话说回来，有件事我一直想问一下。那个制服……[player_name]同学，你是御咲学园的学生吗？"
    me "诶？啊，嗯，是啊。"
    show sirou 3 with dissolve
    sirou "就是啊！\n和我老哥穿得一样！"
    extend "\n几年级的？"
    me "那个……我记得他是二年级的。"
    extend "\n四朗的哥哥多大了？"
    show sirou 4 with dissolve
    sirou "哥哥他，[player_name]和我一样，也是初中二年级！"
    show sirou 6 with dissolve
    extend "\n不过，我完全不觉得我们是同年生的啊……"
    extend "\n[player_name]君比我哥哥成熟一万倍"
    me "啊哈哈，原来是这样。"
    extend "\n你哥哥有那么幼稚吗？"
    show sirou 7 with dissolve
    sirou "他哪里是像小孩子，他简直就是小孩子！比我幼稚一万倍的小孩子！！"
    show sirou 2 with dissolve
    sirou "房间特别乱，垃圾也不分类。"
    show sirou 9 with dissolve
    extend "\n真是伤脑筋啊。"
    me "诶~是这样啊。"
    extend "\n反过来说，四朗明明还是小学生，却非常地懂事呢。"
    extend "\n能真诚地说『对不起』，『谢谢』……。\n这种礼仪非常重要，我很佩服。"
    show sirou 8 with dissolve
    sirou "诶……是，是吗……？"
    extend "\n诶嘿嘿……总觉得有点害羞呢……。"
    play sound "fx/sparkle.ogg"
    "真是可爱呢~~~！！"
    extend "\n初中生固然好，小学生也很不错呢~~~！！！"
    show sirou 5 with dissolve
    sirou "但，但是，[player_name]桑也，和年龄相符地很成熟呢。"
    extend "\n非常沉稳，应对突发事件也非常完美。"
    show sirou 12 with dissolve
    extend "\n啊……还是说，因为一直看到的是那样的哥哥呢。"
    me "嗯~嘛，我也这么觉得……吧。"
    "嘛，实际上也确实很成熟。"
    show sirou 6 with dissolve
    sirou "啊哈哈。就是说呢~。"
    extend "\n真是的，我也想让哥哥好好学学呢。"
    me "我，我也没有那么了不起啦。"
    play sound "fx/triangle.ogg"
    "只是一个喜欢少年的变态而已。"
    show sirou 9 with dissolve
    $ renpy.transition(Quake(0, 50, 0.1, 0.15), layer='master')
    play sound "fx/cute.ogg"
    sirou "诶~！不是这样哦！！"
    show sirou 7 with dissolve
    extend "\n唉，要是能有你这样的哥哥就好了。"
    "呜……虽然对哥哥来说有点抱歉，但听到这话我还是很高兴。"
    play sound "fx/dash.ogg"
    extend "\n我也好想要四朗君那样的弟弟啊！"
    extend "\n我迄今为止做过多少次这样的梦啊！！"
    show sirou 10 with dissolve
    sirou "啊……不好！\n我朋友还在等着我呢……"
    show sirou 8 with dissolve
    extend "\n抱歉，大哥，我差不多该走了！"
    extend "\n托你的福，已经不怎么疼了。"
    me "诶……啊，嗯。"
    extend "\n下次要注意别再撞到了哦。"
    show sirou 4 with dissolve
    sirou "好的。非常感谢你的善意！"
    show sirou 5 with dissolve
    extend "\n……啊，说起来，下周是御咲祭吧？"
    show sirou 3 with dissolve
    extend "\n我也会去玩的，到时候能再见到就好了呢！！"
    show sirou 15 with dissolve
    extend "\n那么，再见了！"
    play sound "fx/running.ogg"
    hide sirou with dissolve
    "四朗说完后便离开了。"
    window hide
    pause 0.3
    window show
    me "御咲祭……也就是说，说不定还能再见到那个孩子！"
    show cg remarkable at center with FadeWhite(0.5)
    play sound "fx/impact.ogg"
    extend "\n好，那可得加油了啊！！"
    extend "\n在学园祭当天，我也要让那个孩子见识一下我的厉害！"
    "下定决心后，我也离开了公园。"
    window hide
    stop music fadeout 0.5
    hide bg with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    return

label day3_cooking_all:
    hide 班選択 with dissolve
    window show
    "去『料理组』看看吧！"
    window hide
    stop music fadeout 0.5
    hide bg with dissolve
    show bg classroom at center with dissolve
    play music "quiet_lunch.ogg"
    window show
    me "那么，我要做些什么才好呢？"
    show sora 2 at topright with dissolve
    sora "[player_name]君，我们组到昨天为止所有的作业就已经完成了，\n所以今天你可以先回家了。"
    show tuki 4 at topleft with dissolve
    tuki "让你特地跑一趟真是不好意思啊。"
    extend "\n今天你就在家好好休息吧。"
    me "诶！怎，怎么这样！！"
    extend "\n那么，今天开心的校园生活，就要到此结束了？！"
    show tuki 1
    show sora 4 with dissolve
    tuki_and_sora "……嗯。"
    window hide
    hide sora with dissolve
    hide tuki with dissolve
    play sound "fx/shock.ogg"
    window show
    "轰！！"
    me "诶诶诶诶诶！！怎么可以这样……。"
    extend "\n这样我可是不满足的啊啊啊啊啊……。"
    show sora 5 at topright with dissolve
    sora "哥哥，[player_name]君，怎么了？"
    show tuki 5 at topleft with dissolve
    tuki "谁知道呢？\n你应该是很高兴能早点回家吧？"
    show sora 1 with dissolve
    sora "啊哈哈。是啊！这样就好了。"
    extend "\n那么，[player_name]君，明天见！"
    show tuki 8 with dissolve
    tuki "再见。"
    extend "\n可别太兴奋被车撞了哦。"
    window hide
    play sound "fx/running.ogg"
    hide sora with dissolve
    hide tuki with dissolve
    stop music fadeout 0.5
    show cg school_building at center with Dissolve(0.7)
    play sound "fx/ding.ogg"
    window show
    "……。"
    "其他组都已经去做其他工作了，我也回家吧……。"
    extend "\n明明有那么多男孩子，但没一个能跟我一块儿回家。"
    extend "\n唉……。"
    window hide
    stop sound fadeout 0.5
    hide bg with Dissolve(0.8)
    hide cg with Dissolve(0.8)
    return

label day3_layout_sinobu:
    window show
    me "忍，我也要去！"
    window hide
    show sinobu 21 at topleft with dissolve
    window show
    sinobu "嗯，我知道了。"
    extend "\n那就跟我来吧。"
    show tubasa 4 at topright with dissolve
    tubasa "我，我走了。"
    extend "\n好好加油哦。"
    window hide
    hide sinobu with dissolve
    hide tubasa with dissolve
    play sound "fx/sliding_door.ogg"
    show bg hallway with dissolve
    window show
    "我们把翼留在教室后，便向教职员室走去。"
    me "连借教室都还没决定好，\n就让翼考虑内部构造吗？"
    window hide
    show sinobu 23 at top with dissolve
    window show
    sinobu "我已经告诉一之濑同学可以去哪间教室了，所以没问题。"
    me "诶，可是，接下来还要去借教室的……"
    show sinobu 12 with dissolve
    sinobu "嗯。"
    extend "\n我一定会借到教室的，放心。"
    me "哦，哦哦…。"
    "好强大的自信啊。"
    extend "\n即便如此，我也觉得安心了，不愧是忍啊。"
    hide sinobu with dissolve
    sinobu "失礼了。"
    play sound "fx/sliding_door.ogg"
    stop music fadeout 0.5
    hide bg with dissolve
    "他打开教师办公室的门，向负责的海老师走去。"
    window hide
    play music "sinobu_theme.ogg"
    show cg c35 1 at center with Radial(0.5)
    window show
    sinobu "您好，海老师。"
    extend "\n我是二年一班的绫濑。"
    extend "\n为了准备御咲祭，我前来向您询问教室的借用事宜。"
    umi "啊，你好。"
    extend "\n那个，二年一班的话……你们是打算和二年二班合开咖啡店吧。"
    extend "\n既然是要用火，又要在合办的地方，那宽敞的教室是必要的吧。"
    extend "\n有想要的地方吗？"
    sinobu "有的。"
    extend "\n我想借用一楼的多功能教室2号厅。"
    umi "啊，那里原本是打算作为休息室的哦。"
    extend "\n其他的教室不行吗？"
    sinobu "那么大的教室当休息室？"
    umi "是啊。"
    extend "\n宽敞的空间会让人更放松的。"
    sinobu "……您说的没错，但是……"
    show cg hallway with FadeWhite(0.5)
    extend "\n那个教室位于食堂的旁边，人流量很大，"
    extend "\n如果当天人流量进一步增加的话，\n哪怕只是做为休息场所，人太多大概也没法让人好好休息吧。"
    show cg school_building_full with FadeWhite(0.5)
    sinobu "另外，从正门到食堂的路上很长，而且道路错综复杂，"
    extend "\n需要休息的老年人，或者是身体有障碍的人，\n还有那些第一次来学园，人生地不熟的人们，\n对于他们，食堂旁边的这个2号厅作为休息室来说并不便利。"
    show cg school_building_morning with FadeWhite(0.5)
    sinobu "因此，如果要作为休息场所使用的话，\n我推荐使用位于正门和食堂中间的多功能教室1号厅。"
    extend "\n那里虽然不大，但是位置显眼，\n厕所和自动贩卖机都很近，作为休息场所来说是最合适的。"
    "忍像往常一样，平淡地陈述着自己的意见。"
    "另一方面，海老师本以为忍会选择其他教室，\n对于休息场所一事，面对忍意料之外的提案，显得有些不知所措。"
    umi "确，确实如此……你说的确实可行。"
    extend "\n滑子老师，关于这个意见，您怎么看？"
    "话音刚落，旁边的滑子老师便转过身来。"
    extend "\n噢噢，好怀念啊！明明都已经过去10年了，这个人看起来还是一点都没老啊。"
    nameko "嗯~我刚刚推举多功能教室2号厅主要是因为那里面积大，\n不过听你这么一说，我倒觉得用多功能教室1号厅更好。"
    extend "\n1号厅一直没人用过，把那里弄成休息室，\n让2年级1，2班的人去那里休息不是很好吗。"
    umi "有道理。"
    extend "\n不过，离食堂那么近，应该不会有什么生意吧？"
    window hide
    show cg c35 2 with dissolve
    window show
    sinobu "不，食堂和咖啡厅的风格不一样。"
    extend "\n前者是为了填饱肚子，后者是为了享受品茶。"
    extend "\n我想，大部分来食堂吃饭的人，都会选择去咖啡厅稍作休息，\n顺便喝杯茶吧。"
    sinobu "我们二年级1，2班的咖啡厅绝对生意兴隆。"
    extend "\n一定会成功的。"
    "虽然忍的语气很冷静，但最后那句话却充满了力量。"
    umi "……我明白了。既然你这么热情，"
    extend "\n二年级1，2班就用多功能教室2号厅吧。"
    sinobu "非常感谢。"
    extend "\n那么，我就先告辞了。"
    "说着，我们离开了办公室。"
    window hide
    stop music fadeout 0.5
    play sound "fx/sliding_door.ogg"
    hide cg with dissolve
    show bg hallway with dissolve
    play music "quiet_lunch.ogg"
    window show
    "走在回教室的路上，我跟忍说："
    me "忍～好厉害！真的太棒了。"
    extend "\n要是刚才那样的话，今后商谈也肯定很顺利的。"
    window hide
    show sinobu 10 at top with dissolve
    window show
    sinobu "商谈什么的，还太早了啦。"
    me "不过，真是被吓到了呢……"
    extend "\n竟然颠覆了老师的论点，让他心悦诚服。"
    show sinobu 14 with dissolve
    sinobu "论点中有很多漏洞和破绽呢。"
    me "海老师也说过，你的热情打动了他不是吗？"
    extend "\n这时候最重要的，是比论点还要坚定不移的信念。"
    extend "\n即使论点毫无矛盾，也必须让他心服口服。"
    extend "\n关键的结论也很成功，真是太棒了。"
    return

label day3_layout_tubasa_2_noinroute:
    show cg class12_cafe_imagination at center with Radial(0.5)
    window show
    me "嗯。\n嗯，我记得店长说过，设置柜台的话就在这里。"
    extend "\n还有，我希望店内的座席和桌子都朝着窗户，\n所以教室必须纵向分隔。"
    tubasa "对的。\n那么，就在这里安装窗帘吧……。"
    extend "\n另外，店是禁烟的对吧？"
    me "嗯。\n我记得，学校本身是禁烟的，吸烟区是另外设置的。"
    tubasa "那么，为了让学生们更好理解，\n入口处和墙壁上贴上标识比较好。"
    extend "\n『美馨儿咖啡』就是这样做的。"
    me "哦~你观察得很仔细呢！"
    "我们一边听着在『美馨儿咖啡』的体验和建议，\n一边想象着完成后的样子，顺利地进行着作业。"
    window hide
    play sound "fx/vibrate.ogg"
    window show
    "嘟嘟"
    "翼的手机响了起来。"
    show tubasa 13 at top with dissolve
    tubasa "啊，是忍酱。"
    hide tubasa with dissolve
    tubasa "嗯，你好。"
    extend "\n……真的吗，那太好了！"
    extend "\n嗯，嗯，我知道了。"
    extend "\n那我马上过去。"
    "哔"
    show tubasa 31 at top with dissolve
    tubasa "忍君他顺利地借到了多功能教室2号厅！"
    extend "\n为了能确认一下，我们就在那里会合吧。"
    me "哦，好！太好了。"
    extend "\n那我们就赶紧过去吧。"
    stop music fadeout 1.0
    window hide
    hide tubasa with Dissolve(0.8)
    hide bg with Dissolve(0.8)
    return