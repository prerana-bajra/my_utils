
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
import matplotlib.pyplot as plt

def make_dynamic_coldhot(vmin, vmax, n_colors=512, gamma=1.0):
   
    if vmax <= vmin:
        raise ValueError("vmax must be > vmin")
    center_pos = (0.0 - vmin) / (vmax - vmin)
    center_pos = float(np.clip(center_pos, 0.0, 1.0))

    design_stops = [
        (0.00, (0.00, 0.00, 0.45)),   # deep navy (leftmost)
        (0.15, (0.00, 0.20, 0.95)),   # bright blue
        (0.35, (0.00, 1.00, 1.00)),   # cyan
        (0.50, (1.00, 1.00, 1.00)),   # white (design center)
        (0.65, (1.00, 1.00, 0.00)),   # yellow
        (0.82, (0.90, 0.50, 0.00)),   # orange
        (1.00, (0.85, 0.00, 0.00)),   # deep red (rightmost)
    ]
    design_positions, design_colors = zip(*design_stops)
    design_positions = np.array(design_positions)
    design_colors = np.array(design_colors)

    def remap_pos(p):
        if p <= 0.5:
            if 0.5 == 0:
                return 0.0
            return (p / 0.5) * center_pos
        else:
            return center_pos + ((p - 0.5) / 0.5) * (1.0 - center_pos)

    remapped_positions = np.array([remap_pos(p) for p in design_positions])

    xs = np.linspace(0.0, 1.0, n_colors)
    if gamma != 1.0:
        xs = xs ** gamma

    cmap_rgb = np.zeros((n_colors, 3))
    for c in range(3):
        cmap_rgb[:, c] = np.interp(xs, remapped_positions, design_colors[:, c])

    cmap = LinearSegmentedColormap.from_list('dynamic_coldhot', cmap_rgb, N=n_colors)

    norm = TwoSlopeNorm(vmin=vmin, vcenter=0.0, vmax=vmax)

    return cmap, norm




