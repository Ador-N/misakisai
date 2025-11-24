# -*- coding: utf-8 -*-
# LiveMaker 转场效果定义
# 这些是从 LiveMaker 转换过来的自定义转场效果

# 已知的 Ren'Py 内置效果：
# - dissolve: 淡入淡出（ID 1）
# - fade: 渐变黑屏（ID 12）
# - pixellate: 像素化（ID 14）
# - wipeleft: 左擦除（ID 25）

# LiveMaker 自定义效果（需要实现）：
define lm_blinds = ImageDissolve("images/transitions/blinds.png", 0.5)      # ID 13: 百叶窗
define lm_crossfade = Dissolve(0.5)                                          # ID 18: 交叉淡入淡出
define lm_wiperight = PushMove(0.5, "pushright")                            # ID 26: 右擦除
define lm_wipeup = PushMove(0.5, "pushup")                                  # ID 27: 上擦除
define lm_wipedown = PushMove(0.5, "pushdown")                              # ID 28: 下擦除
define lm_flash = Fade(0.1, 0.0, 0.4, color="#fff")                         # ID 30: 闪白效果

# 未实现的效果（临时使用 dissolve）：
define lm_effect_2 = dissolve
define lm_effect_3 = dissolve
define lm_effect_4 = dissolve
define lm_effect_5 = dissolve
define lm_effect_6 = dissolve
define lm_effect_7 = dissolve
define lm_effect_8 = dissolve
define lm_effect_9 = dissolve
define lm_effect_10 = dissolve
define lm_effect_11 = dissolve
define lm_effect_15 = dissolve
define lm_effect_16 = dissolve
define lm_effect_17 = dissolve
define lm_effect_19 = dissolve
define lm_effect_20 = dissolve
define lm_effect_21 = dissolve
define lm_effect_22 = dissolve
define lm_effect_23 = dissolve
define lm_effect_24 = dissolve
define lm_effect_29 = dissolve

# 说明：
# 1. 如果你知道某个效果ID的实际效果，可以自定义实现
# 2. 可以使用 ATL (Animation and Transformation Language) 创建复杂动画
# 3. 可以使用 ImageDissolve 配合遮罩图片实现特殊转场
# 4. Ren'Py 文档: https://www.renpy.org/doc/html/transitions.html
