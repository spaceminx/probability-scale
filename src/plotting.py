import matplotlib.pyplot as plt


def plot_probability_scale(df, output_path):
    df = df.sort_values("probability").reset_index(drop=True)

    background = "#111827"
    foreground = "#F9FAFB"
    muted = "#9CA3AF"
    line = "#60A5FA"

    fig, (ax_full, ax_zoom) = plt.subplots(
        2,
        1,
        figsize=(15, 8),
        gridspec_kw={"height_ratios": [1, 3]},
    )

    fig.patch.set_facecolor(background)

    for ax in [ax_full, ax_zoom]:
        ax.set_facecolor(background)
        ax.set_yticks([])
        ax.tick_params(axis="x", colors=muted)
        ax.grid(axis="x", color="white", alpha=0.08)

        for spine in ["left", "right", "top"]:
            ax.spines[spine].set_visible(False)

        ax.spines["bottom"].set_color(muted)

    # --- Full 0–1 scale ---
    ax_full.hlines(0, 0, 1, linewidth=2.5, color=line)
    ax_full.scatter(df["probability"], [0] * len(df), s=80, color=line, zorder=3)

    ax_full.set_xlim(0, 1)
    ax_full.set_ylim(-0.3, 0.3)
    ax_full.set_title(
        "Probability scale of real-world events in Estonia",
        color=foreground,
        fontsize=17,
        pad=18,
    )
    ax_full.set_xlabel("Full 0–1 probability scale", color=foreground)

    # --- Zoomed scale ---
    xmax = df["probability"].max() * 1.2

    ax_zoom.hlines(0, 0, xmax, linewidth=2.5, color=line)
    ax_zoom.scatter(df["probability"], [0] * len(df), s=90, color=line, zorder=3)

    label_positions = [0.36, -0.36, 0.22, -0.22, 0.50]

    for i, row in df.iterrows():
        prob = row["probability"]
        y_text = label_positions[i % len(label_positions)]

        ax_zoom.vlines(
            prob,
            0,
            y_text * 0.65,
            linewidth=1.2,
            color=line,
            alpha=0.8,
        )

        ax_zoom.text(
            prob,
            y_text,
            f"{row['event']}\n1 in {row['one_in']:.0f}",
            ha="center",
            va="center",
            fontsize=9,
            color=foreground,
        )

    ax_zoom.set_xlim(0, xmax)
    ax_zoom.set_ylim(-0.62, 0.62)
    ax_zoom.set_title(
        f"Zoomed view: 0–{xmax:.2f}",
        color=foreground,
        fontsize=13,
        pad=12,
    )
    ax_zoom.set_xlabel("Probability", color=foreground)

    plt.subplots_adjust(
        left=0.06,
        right=0.98,
        top=0.9,
        bottom=0.1,
        hspace=0.55,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor())
    plt.close()
