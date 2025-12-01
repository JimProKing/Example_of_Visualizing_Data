from pathlib import Path
import matplotlib.pyplot as plt
from step1_폴더생성 import OUT_DIR
from step3_1 import load_plot_data

plot_data = load_plot_data()
fig, ax = plt.subplots()
ax.barh(plot_data["stem"],plot_data["size"])
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png")