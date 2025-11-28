init python:
    cg_list = [
        "少年たち c1 2",
        "nori c2",
        "飴 c3",
        "飴 c4",
        "tomo c5 1",
        "tomo c5 2",
        "俺 c6",
        "sinobu c7 2",
        "sinobu c7 3",
        "sinobu c7 1",
        "cg c8",
        "cg c22",
        "cg c23",
        "cg c31",
        "cg c39 2",
        "cg c39 1",
        "cg c40",
        "cg c47 2",
        "cg c49 1",
        "cg c49 2",
        "cg c58",
        "cg c59",
        "cg c65",
        "cg c66 1",
        "cg c66 2",
        "cg c75",
        "cg c76",
        "お母さん c21",
        "cg c10",
        "cg c24",
        "cg c32",
        "cg c41",
        "cg c50",
        "cg c67",
        "cg c77",
        "cg c9",
        "cg c11",
        "cg c12 1",
        "cg c12 2",
        "cg c25",
        "cg c26",
        "cg c33 1",
        "cg c33 2",
        "cg c33 3",
        "cg c33",
        "cg c42 1",
        "cg c42 2",
        "cg c51",
        "cg c60",
        "cg c48 2",
        "cg c52",
        "cg c68 1",
        "cg c68 2",
        "cg c69",
        "cg c78",
        "cg c102",
        "bg c103",
        "cg c104 1",
        "cg c104 2",
        "cg c106 1",
        "cg c106 2",
        "cg c105",
        "cg c34 2",
        "cg c34 1",
        "cg c13",
        "cg c27",
        "cg c36",
        "cg c44",
        "cg c53",
        "cg c70",
        "cg c79",
        "cg c14",
        "cg c15",
        "cg c16",
        "cg c17 1",
        "cg c17 2",
        "cg c28",
        "bg c29 1",
        "bg c29 2",
        "cg c35 1",
        "cg c35 2",
        "夕空 c37 2",
        "夕空 c37 1",
        "cg c43",
        "cg c45 1",
        "cg c45 2",
        "cg c54",
        "cg c55 1",
        "cg c55 2",
        "cg c56",
        "cg c61",
        "cg c62 1",
        "cg c62 2",
        "cg c71 1",
        "cg c72 2",
        "cg c73 1",
        "cg c73 2",
        "cg c74",
        "cg c80",
        "cg c81",
        "cg c82 1",
        "cg c82 2",
        "cg c18",
        "cg c19 1",
        "cg c19 2",
        "cg c19 3",
        "cg c19 4",
        "cg c20 1",
        "cg c20 2",
        "cg c20 3",
        "cg c20 4",
        "cg c20 5",
        "cg c30 1",
        "cg c30 2",
        "cg c30 3",
        "cg c38 1",
        "cg c38 2",
        "cg c38 3",
        "cg c46 1",
        "cg c46 2",
        "cg c46 3",
        "cg c46 4",
        "cg c57 1",
        "cg c57 2",
        "cg c57 3",
        "cg c57 4",
        "cg c63 1",
        "cg c63 2",
        "cg c63 3",
        "cg c63 4",
        "cg c63 5",
        "cg c64 1",
        "cg c64 2",
        "cg c64 3",
        "cg c74 1",
        "cg c74 2",
        "cg c74 3",
        "cg c83 1",
        "cg c83 2",
        "cg c83 3",
        "cg c84",
        "cg c85",
        "cg c86",
        "cg c87",
        "cg c88 8",
        "cg c89",
        "cg c90",
        "cg c91 1",
        "cg c91 2",
        "cg c92 1",
        "cg c92 2",
        "cg c92 3",
        "cg c93 1",
        "cg c93 2",
        "cg c93 3",
        "cg c94",
        "cg c97",
        "cg c95",
        "cg c96",
        "cg c98",
        "cg c99",
        "cg c100",
        "cg c101"
    ]

transform gallery_image_zoom:
    on hover:
        easein .25 zoom 1.25
    on idle:
        easein .25 zoom 1.0

init python:
    ### CONFIG ###
    # file extension of the CGs, used in creating automatic thumbnails
    cg_format = ".png" 
    # path to CGs
    cg_path = "images/eventcg/" 
    # number of columns of thumbnails in the gallery grid
    max_x = 5
    # number of rows of thumbnails in the gallery grid
    max_y = 4
    # this will be the width of the thumbnails, height will be calculated automatically for 16:9 aspect ratio thumbnails
    thumbnail_x = 128
    ### END OF CONFIG ###

    max_page = max_x * max_y
    thumbnail_y = int(thumbnail_x * 0.75)
    x_size = thumbnail_x * max_x + (max_x - 1) * 8
    y_size = thumbnail_y * max_y + (max_y - 1) * 6
    gallery_page = 0
    gallery_items = []
    g = Gallery()
    g.transition = dissolve
    g.locked_button = Transform("images/box/black.png", xsize=thumbnail_x, ysize=thumbnail_y)

    # A class for gallery items (no need to change anything here)
    # when creating a GalleryItem object, provide images in a list, you can put more than one to have more images displayed consecutively after another under one button
    # if no thumbnail is provided as the 3rd argument, it will be built automatically from the 1st image in 16:9 aspect ratio
    # alternatively the path to the custom thumbnail can be provided as the 3rd argument during object creation
    class GalleryItem:
        def __init__(self, name, images):
            self.name = name
            self.images = images
            self.thumb = Transform(images[0], xsize=thumbnail_x, ysize=thumbnail_y)
            self.thumb_with_zoom = Transform(self.thumb, style="gallery_button")

        def num_images(self):
            return len(self.images)

screen gallery():

    python:
        if len(gallery_items) == 0:

            ### CGs ###
            # Provide button name, a list of images to display, and alternatively a path to a custom thumbnail

            for cg in cg_list:
                gallery_items.append(GalleryItem(cg, [cg]))

            for item in gallery_items:
                g.button(item.name)
                for img in item.images:
                    g.unlock_image(img)

        start = gallery_page * max_page
        end = min(start + max_page - 1, len(gallery_items) - 1)
        page_count = (len(gallery_items) + max_page - 1) // max_page
        unlocked_count = sum(int(g.get_fraction(item.name, "{seen}")) for item in gallery_items)


    ### Layout ###
    tag menu
    style_prefix "gallery"
    add "images/startmenu/cgmode.png"

    textbutton _("回到开始界面"):
        action Return()
        style "choice_button"
        xpos 420
        ypos 12

    text "[unlocked_count]  /  [len(gallery_items)]":
        xpos 250
        ypos y_size + 140
        xanchor 0.5
        yanchor 0.5

    fixed:
        xalign 0.5
        yalign 0.5
        xsize x_size
        ysize y_size
        yoffset -10
        
        for i in range(end - start + 1):
            $ item = gallery_items[i + start]
            add g.make_button(item.name, item.thumb,
                    xpos=i % max_x * (thumbnail_x + 8) + thumbnail_x // 2,
                    ypos=i // max_x * (thumbnail_y + 6) + thumbnail_y // 2,
                    style="gallery_button",
                    hovered=Show("zoomed_cg", i=i + start),
                    unhovered=Hide("zoomed_cg", transition=zoomout)
                )
        for i in range(end - start + 1, max_page):
            null
        
    hbox:
        xanchor 0.5
        yanchor 0.5
        xpos 650
        ypos y_size + 140
        spacing 20
        imagebutton auto "images/startmenu/gallery_prev_%s.png" yalign 0.5:
            if gallery_page > 0:
                action SetVariable("gallery_page", gallery_page - 1)
        text "[gallery_page + 1]  /  [page_count]" yoffset -2
        imagebutton auto "images/startmenu/gallery_next_%s.png" yalign 0.5:
            if gallery_page < page_count - 1:
                action SetVariable("gallery_page", gallery_page + 1)
    
    on "replace" action Play("music", "quiet_lunch.ogg")
    on "replaced" action Play("music", config.main_menu_music)

style gallery_text:
    size 32
    color "#34a7ca"
    outlines [(2, "#FFF", 0, 0)] 

screen zoomed_cg(i):
    zorder 100

    add gallery_items[i].images[0] at transform:
        xanchor 0.5
        yanchor 0.5
        xsize thumbnail_x
        ysize thumbnail_y
        xpos (i % max_page) % max_x * (thumbnail_x + 8) + thumbnail_x
        ypos (i % max_page) // max_x * (thumbnail_y + 6) + int(thumbnail_y * 1.5) - 7
        on show:
            easein .25 zoom 1.2
        on hide:
            easeout .25 zoom 1.0


style gallery_button:
    xalign 0.5
    yalign 0.5