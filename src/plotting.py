import matplotlib.pyplot as plt

def plot_probability_scale(df, output_path):
    df = df.sort_values("probability").reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(14, 6))

    xmax = df["probability"].max() * 1.25

    # Main probability line
    ax.hlines(y=0, xmin=0, xmax=xmax, linewidth=2)

    # Points
    ax.scatter(df["probability"], [0] * len(df), s=90, zorder=3)

    label_positions = [0.32, -0.34, 0.20, -0.22, 0.42]

    for i, row in df.iterrows():
        prob = row["probability"]

        y_text = label_positions[i % len(label_positions)]

        # väike offset, et tekst ei oleks täpselt joone peal
        x_text = prob + (xmax * 0.01)

        # väikeste väärtuste puhul vasak-joondus
        if prob < 0.02:
            ha = "left"
        else:
            ha = "center"

        ax.vlines(
            x=prob,
            ymin=0,
            ymax=y_text * 0.65,
            linewidth=1,
            alpha=0.7,
        )

        ax.text(
            x_text,
            y_text,
            f"{row['event']}\n1 in {row['one_in']:.0f}",
            ha=ha,
            va="center",
            fontsize=9,
        )

    ax.set_xlim(0, xmax)
    ax.set_ylim(-0.5, 0.5)

    ax.set_xlabel("Probability")
    ax.set_title("Probability scale of real-world events in Estonia")

    ax.set_yticks([])

    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    ax.grid(axis="x", alpha=0.25)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

import matplotlib.pyplot as plt


def plot_probability_scale_dark(df, output_path):
    df = df.sort_values("probability").reset_index(drop=True)

    background = "#111827"
    foreground = "#F9FAFB"
    muted = "#9CA3AF"
    line = "#60A5FA"

    fig, ax = plt.subplots(figsize=(14, 6))
    fig.patch.set_facecolor(background)
    ax.set_facecolor(background)

    xmax = df["probability"].max() * 1.25

    ax.hlines(y=0, xmin=0, xmax=xmax, linewidth=2.5, color=line)
    ax.scatter(df["probability"], [0] * len(df), s=100, color=line, zorder=3)

    label_positions = [0.32, -0.34, 0.20, -0.22, 0.42]

    for i, row in df.iterrows():
        y_text = label_positions[i % len(label_positions)]
        prob = row["probability"]

        ax.vlines(
            x=prob,
            ymin=0,
            ymax=y_text * 0.65,
            linewidth=1.2,
            color=line,
            alpha=0.8,
        )

        ax.text(
            prob,
            y_text,
            f"{row['event']}\n1 in {row['one_in']:.0f}",
            ha="center",
            va="center",
            fontsize=9,
            color=foreground,
        )

    ax.set_xlim(0, xmax)
    ax.set_ylim(-0.5, 0.5)

    ax.set_xlabel("Probability", color=foreground, fontsize=11)
    ax.set_title(
        "Probability scale of real-world events in Estonia",
        color=foreground,
        fontsize=15,
        pad=18,
    )

    ax.set_yticks([])
    ax.tick_params(axis="x", colors=muted)

    ax.spines["bottom"].set_color(muted)
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    ax.grid(axis="x", color="white", alpha=0.08)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor())
    plt.close()