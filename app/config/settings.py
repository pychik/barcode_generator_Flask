from os import getcwd

folder_static = f'{getcwd()}/generated/'


class Settings:
    SECRET = "mysupersecret"
    folder = folder_static
    options = dict(module_width=0.3, module_height=10, quiet_zone=2, text_distance=3,
                   font_size=8, center_text=True)