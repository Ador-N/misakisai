# 从 LiveMaker 转换的自定义转场效果

transform ZoomInOut(duration=0.5, *, new_widget=None, old_widget=None):
    delay duration

    xanchor 0.0
    yanchor 0.0

    old_widget
    events False
    easeout_quint duration / 2 zoom 20

    new_widget
    events True
    zoom 20
    easein_quint duration / 2 zoom 1

define zoominout = ZoomInOut()

transform Quake(x, y, in_duration=0.1, out_duration=0.5, *, new_widget=None, old_widget=None):
    delay (in_duration + out_duration) / 2

    offset (0, 0)
    easein in_duration / 2 offset (-x/2, y/2)
    easeout out_duration / 2 offset (0, 0)

transform Defocus(duration, brightness=0.5, *, new_widget=None, old_widget=None):
    delay duration

    old_widget
    events False
    parallel:
        blur 0
        easein duration / 2 blur 100
    parallel:
        matrixcolor BrightnessMatrix(0.0)
        pause duration * 0.35
        easein duration * 0.15 matrixcolor BrightnessMatrix(brightness)

    new_widget
    events True
    parallel:
        blur 100
        easeout duration / 2 blur 0
    parallel:
        matrixcolor BrightnessMatrix(brightness)
        pause duration * 0.15
        easeout duration * 0.35 matrixcolor BrightnessMatrix(0.0)

init python:
    renpy.register_shader("transition.radial_glow", variables="""
        uniform sampler2D tex0;
        uniform sampler2D tex1;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_radial_progress;
        uniform float u_aspect_ratio;
        uniform float u_glow_width;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec2 ratio = vec2(1.0 / u_aspect_ratio, 1.0);
        float dist = length((v_tex_coord.st - vec2(0.5)) * ratio) / length(ratio * 0.5);

        vec4 color1 = texture2D(tex0, v_tex_coord.st);
        vec4 color2 = texture2D(tex1, v_tex_coord.st);
        vec4 base_color = mix(color1, color2, step(dist, u_radial_progress));

        vec4 glow_color = vec4(1.0, 1.0, 1.0, 1.0);
        float glow_strength = smoothstep(u_radial_progress - u_glow_width, u_radial_progress, dist)
                            - smoothstep(u_radial_progress, u_radial_progress + u_glow_width, dist);

        gl_FragColor = base_color + glow_color * glow_strength;

    """)

transform Radial(duration=0.5, *, new_widget=None, old_widget=None):
    delay duration

    Model().texture(old_widget).child(new_widget)
    shader [ "transition.radial_glow" ]
    u_aspect_ratio 0.75
    u_glow_width 0.3

    u_radial_progress -0.3
    linear duration u_radial_progress 1.3


init python:
    def FadeBlack(duration): return Fade(duration / 2, 0, duration / 2, color="#000")
    def FadeWhite(duration): return Fade(duration / 2, 0, duration / 2, color="#FFF")
    def DefocusWhite(duration): return Defocus(duration, 0.5)
    def DefocusBlack(duration): return Defocus(duration, -0.5)

