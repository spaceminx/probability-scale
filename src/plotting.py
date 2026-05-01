import matplotlib.pyplot as plt

def plot_probability_scale(df, out_path):
    df = df.sort_values(by=["probability"], ascending=True)

    fig, ax = plt.subplots(figsize=(10,6))

    ax.scatter(df["probability"], df["event"])

    ax.set_xscale("log")

    ax.set_xlabel("Probability log scale")
    ax.set_ylabel("")
    ax.set_title("Probability log scale")

    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
