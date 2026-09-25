"""Turtle-Modul für die Übung U5_6_Stadtlauf_Bern_Modul.py."""

pos = {
    "Käfigturm": (200, 280, 120, 150),
    "Zytglogge": (410, 490, 140, 160),
    "Bundeshaus": (190, 240, 180, 210),
    "Münster": (570, 725, 200, 250),
    "Kasino": (440, 540, 230, 270),
    "Rathaus": (660, 750, 60, 110),
    "Nydeck Kirche": (870, 950, 60, 100),
}


def check_text(x, y):
    """Liefert Text und Position einer nahe gelegenen Sehenswürdigkeit."""
    text2show, xt, yt = "", x, y

    for name, (x_min, x_max, y_min, y_max) in pos.items():
        if x_min < x < x_max and y_min < y < y_max:
            text2show, xt, yt = name, x, y

    return text2show, xt, yt
