import numpy as np
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
import matplotlib.pyplot as plt

from hotcold_colormap import make_dynamic_coldhot

# -------------------------
# Quick demo (visual test)
# -------------------------
if __name__ == "__main__":
    vmin, vmax = -0.8, 0.8
    cmap, norm = make_dynamic_coldhot(vmin, vmax, n_colors=512, gamma=1.02)

    fig, ax = plt.subplots(figsize=(2,5))
    m = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    plt.colorbar(m, cax=ax)
    ax.set_title(f"vmin={vmin}, vmax={vmax}\ncenter_pos={(0 - vmin)/(vmax - vmin):.2f}")
    plt.savefig('hotcold_colormap/my_plot_result.png', dpi=300)