"""Figuras del oral Cuba / homosexualidad."""

from __future__ import annotations

import theme
from style import C, band, box, canvas, disc, save, tag, arrow, note


def fig_contraste_moral():
    key = "contraste_moral"
    W, H = theme.FIGURE_WITH_CAPTION.width, theme.FIGURE_WITH_CAPTION.height
    fig, ax = canvas(W, H)

    box(ax, 0.30, 1.70, 4.9, 2.7,
        ["Fresa y chocolate", "Integrar", "Amistad y respeto"],
        fill=C["pale"], edge=C["teal"], sizes=(16, 13))
    box(ax, 6.30, 1.70, 4.9, 2.7,
        ["Antes que anochezca", "Denunciar", "Dolor y memoria"],
        fill=C["white"], edge=C["navy"], sizes=(16, 13))

    disc(ax, 5.75, 3.05, 0.42, "≠", C["gold"], size=20)
    band(ax, 0.30, 0.35, W - 0.60, 0.95,
         "Misma isla, dos miradas.",
         size=18, bold=True)
    tag(ax, 0.35, 4.55, "dos ideas", size=11)
    note(ax, W / 2, 1.35, "Dos formas de ver Cuba.", size=12, ha="center")
    return save(fig, key)


ALL = (fig_contraste_moral,)
