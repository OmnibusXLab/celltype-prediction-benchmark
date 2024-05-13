import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches

from scipy.optimize import curve_fit

from sklearn.metrics import f1_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import silhouette_score

cmap_color = colors.LinearSegmentedColormap.from_list(
    "",
    ["#ffffff", "#eeeeee", "#dddddd"],
)


def draw_score_by_study_table(scores, studies_source):
    labels = studies_source["tissues"]
    _, ax = plt.subplots(nrows=1, ncols=1, figsize=(18, 3), constrained_layout=True)

    color = scores**2
    color[scores < 0.8] = 0

    ax.imshow(color, cmap=cmap_color, vmin=0.5, vmax=1, aspect=0.6)
    ax.set_yticks(np.arange(2), labels=["Azimuth", "OmnibusX"])
    ax.set_xticks(
        np.arange(0, len(labels), 2) + 0.5,
        labels=[v for i, v in enumerate(labels) if i % 2 == 0],
    )
    for i in range(len(labels)):
        if i % 2 == 0:
            ax.axvline(x=i + 0.5, color="#333", linestyle="--", linewidth=0.5)
        else:
            ax.axvline(x=i + 0.5, color="#000", linestyle="-", linewidth=1)
    ax.axhline(y=0.5, color="#333", linestyle="--", linewidth=0.5)

    idx = [i for i, v in enumerate(studies_source["source"]) if v != ""]
    ax2 = ax.secondary_xaxis("top")
    ax2.set_xticks(idx, labels=[studies_source["source"][i] for i in idx])

    for i in range(scores.shape[0]):
        for j in range(scores.shape[1]):
            s = scores[i, j]
            if scores[i, j] == 0:
                v = "-"
            else:
                v = f"{s:.4f}"

            if s > scores[(1 - i), j]:
                w = "bold"
            else:
                w = "normal"
            ax.text(j, i, v, ha="center", va="center", color="#000", fontweight=w)

    ax.text(
        0.89,
        1.25,
        "*Dataset from Azimuth's reference",
        fontsize=10,
        transform=ax.transAxes,
        va="top",
        ha="right",
    )
    grey_patches = mpatches.Patch(
        facecolor="#dddddd", edgecolor="#000000", label="Good agreement"
    )
    leg = ax.legend(
        handles=[grey_patches], loc=(0.905, 1.05), frameon=False, alignment="right"
    )
    for patch in leg.get_patches():
        patch.set_height(12)
        patch.set_y(-2)

    ax.set_title(
        "Agreement level (Cohen's Kappa score)", loc="center", fontsize=12, pad=16
    )
    plt.savefig("score_by_study.svg", format="svg")


def draw_score_by_study_box(scores, studies_source):
    _, axs = plt.subplots(
        nrows=1,
        ncols=2,
        figsize=(7, 3.2),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    df = pd.DataFrame(
        {
            "sources": np.array(studies_source["source"] * 2),
            "scores": np.concatenate([scores[0], scores[1]]),
            "tools": ["Azimuth"] * scores.shape[1] + ["OmnibusX"] * scores.shape[1],
        }
    )
    df = df.iloc[df["scores"].values > 0, :]

    title = [
        "Datasets from Azimuth's reference",
        "External datasets",
    ]
    for i, s in enumerate(["*", ""]):
        data = df.iloc[df["sources"].values == s, :]
        ax = axs[i]

        sns.swarmplot(
            data=data,
            x="tools",
            y="scores",
            color="#000",
            edgecolor="#ffffff00",
            linewidth=2,
            size=6,
            ax=ax,
        )
        sns.boxplot(
            data=data,
            x="tools",
            y="scores",
            showcaps=False,
            showfliers=False,
            fill=False,
            width=0.6,
            linewidth=1,
            color="#999",
            ax=ax,
        )

        ax.set(ylim=(0.3, 1))
        ax.axhline(y=0.8, color="#000", linestyle="--", linewidth=1)

        ax.set_title(title[i], fontsize=10)
        ax.set_xlabel("")

    axs[0].set_ylabel("Agreement level (Cohen's Kappa score)")
    axs[1].text(
        1.03,
        0.69,
        "good agreement",
        rotation=-90,
        ha="center",
        transform=ax.transAxes,
        color="#000",
        fontsize=8,
    )
    plt.savefig("study_box.svg", format="svg")


def draw_score_by_celltype_table(scores, celltypes):
    _, ax = plt.subplots(nrows=1, ncols=1, figsize=(3.6, 3.2), constrained_layout=True)

    color = scores**2
    color[scores < 0.8] = 0

    ax.imshow(color, cmap=cmap_color, vmin=0.5, vmax=1, aspect=0.36)
    ax.set_xticks(np.arange(2), labels=["Azimuth", "OmnibusX"])
    ax.set_yticks(np.arange(0, len(celltypes)), labels=celltypes)
    for i in range(len(celltypes)):
        ax.axhline(y=i + 0.5, color="#333", linestyle="--", linewidth=0.5)
    ax.axvline(x=0.5, color="#333", linestyle="--", linewidth=0.5)

    for i in range(scores.shape[0]):
        for j in range(scores.shape[1]):
            s = scores[i, j]
            if scores[i, j] == 0:
                v = "-"
            else:
                v = f"{s:.4f}"

            if s > scores[i, (1 - j)]:
                w = "bold"
            else:
                w = "normal"
            ax.text(j, i, v, ha="center", va="center", color="#000", fontweight=w)

    ax.set_title("Agreement level (F1-score)", loc="center", fontsize=10)
    plt.savefig("score_by_celltype.svg", format="svg")


def linear_fit(x, a, b):
    return a * x + b


def exp_decay_fit(x, a):
    return a - (4 ** (4 * x))


def draw_scores_by_cluster(scores):
    _, axs = plt.subplots(
        nrows=1,
        ncols=2,
        figsize=(7, 3.2),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    x = -(scores["Clusters"] - scores["Clusters"].min())
    steps = np.linspace(np.min(x), np.max(x), 100)

    popt, _ = curve_fit(exp_decay_fit, x, scores["Azimuth"])
    axs[0].scatter(x=x, y=scores["Azimuth"], c="#000", s=6)
    axs[0].plot(
        steps, exp_decay_fit(steps, *popt), color="#000", linestyle="--", linewidth=1
    )

    popt, _ = curve_fit(linear_fit, x, scores["OmnibusX"])
    axs[1].scatter(x=x, y=scores["OmnibusX"], c="#000", s=6)
    axs[1].plot(
        steps, linear_fit(steps, *popt), color="#000", linestyle="--", linewidth=1
    )

    for ax, title in zip(axs, ["Azimuth", "OmnibusX"]):
        ax.set_xticklabels([])
        ax.set_xlabel("Cluster dispersion level")
        ax.set_title(title, loc="center", fontsize=10)
    axs[0].set_ylabel("Agreement level (F1-score)")

    plt.savefig("score_by_cluster.svg", format="svg")


def score_by_study(study_ids, tissues):
    azimuth = []
    omnibusx = []
    for s_id, tissue in zip(study_ids, tissues):
        p = f"{tissue.replace(' ', '_')}/{s_id}"
        df = pd.read_csv(f"../data/studies/{p}/result.tsv", sep="\t")
        truth = df["Truth"].values
        a = (
            df["Azimuth - standardized"].values
            if "Azimuth - standardized" in df.columns
            else np.array(["Unassigned"] * len(truth))
        )
        o = df["OmnibusX - standardized"].values

        azimuth.append(cohen_kappa_score(truth, a))
        omnibusx.append(cohen_kappa_score(truth, o))

    return np.array([azimuth, omnibusx])


def score_by_celltype(study_ids, tissues):
    celltype_group = pd.read_csv("../data/celltype_group.tsv", sep="\t")
    group_map = {
        k: v for k, v in zip(celltype_group["Cell type"], celltype_group["Group"])
    }

    truth = []
    azimuth = []
    omnibusx = []
    for s_id, tissue in zip(study_ids, tissues):
        p = f"{tissue.replace(' ', '_')}/{s_id}"
        df = pd.read_csv(f"../data/studies/{p}/result.tsv", sep="\t")
        if "Azimuth - standardized" not in df.columns:
            continue

        truth.append(df["Truth"].values)
        azimuth.append(df["Azimuth - standardized"].values)
        omnibusx.append(df["OmnibusX - standardized"].values)

    truth = np.concatenate(truth)
    azimuth = np.concatenate(azimuth)
    omnibusx = np.concatenate(omnibusx)
    groups = np.array([group_map[v] for v in truth])

    labels, indices = np.unique(groups, return_inverse=True)
    scores = []
    celltypes = []
    for i, g in enumerate(labels):
        if g == "Unassigned":
            continue

        idx = indices == i
        celltypes.append(g)
        scores.append(
            [
                f1_score(truth[idx], azimuth[idx], average="micro"),
                f1_score(truth[idx], omnibusx[idx], average="micro"),
            ]
        )

    scores = np.array(scores)
    order = np.argsort(scores[:, 0].reshape(-1))
    scores = scores[order]
    celltypes = [celltypes[i] for i in order]

    return scores, celltypes


def score_by_cluster(study_ids, tissues):
    celltype_group = pd.read_csv("../data/celltype_group.tsv", sep="\t")
    group_map = {
        k: v for k, v in zip(celltype_group["Cell type"], celltype_group["Group"])
    }

    cluster_scores = []
    azimuth_scores = []
    omnibusx_scores = []
    for s_id, tissue in zip(study_ids, tissues):
        p = f"{tissue.replace(' ', '_')}/{s_id}"
        df = pd.read_csv(f"../data/studies/{p}/result.tsv", sep="\t")
        if "Azimuth - standardized" not in df.columns:
            continue

        scatter = pd.read_csv(
            f"../data/studies/{p}/tsne.tsv", sep="\t", index_col=0
        ).values
        truth = df["Truth"].values
        azimuth = df["Azimuth - standardized"].values
        omnibusx = df["OmnibusX - standardized"].values

        groups = np.array([group_map[v] for v in truth])
        labels, indices = np.unique(groups, return_inverse=True)

        for i, g in enumerate(labels):
            if g == "Unassigned":
                continue

            idx = indices == i
            t = truth[idx]

            if len(t) < 1000 or len(np.unique(t)) == 1:
                continue

            cluster_scores.append(silhouette_score(scatter[idx], t))
            azimuth_scores.append(f1_score(t, azimuth[idx], average="micro"))
            omnibusx_scores.append(f1_score(t, omnibusx[idx], average="micro"))

    return pd.DataFrame(
        {
            "Clusters": np.array(cluster_scores),
            "Azimuth": np.array(azimuth_scores),
            "OmnibusX": np.array(omnibusx_scores),
        }
    )


def main():
    studies_source = {
        "ids": [
            "human_m1_10x",
            "seeker_et_al",
            "GSE85241",
            "GSE148073",
            "ERP123138",
            "GSE216019",
            "GSE115469",
            "GSE192740",
            "GSE183276",
            "GSE131882",
            "syn21041850",
            "GSE161382",
            "ERP122984",
            "GSE216005",
            "GSE247917",
            "EGAD00001007718",
            "E-MTAB-13664",
            "GSE195665",
            "GSE134809",
            "E-MTAB-8901",
            "GSE135133",
            "GSE169047",
        ],
        "tissues": [
            "brain",
            "brain",
            "pancreas",
            "pancreas",
            "heart",
            "heart",
            "liver",
            "liver",
            "kidney",
            "kidney",
            "lung",
            "lung",
            "bone marrow",
            "bone marrow",
            "pbmc",
            "pbmc",
            "breast",
            "breast",
            "colon",
            "colon",
            "eye",
            "eye",
        ],
        "source": [
            "*",
            "",
            "*",
            "",
            "*",
            "",
            "*",
            "",
            "*",
            "",
            "*",
            "",
            "*",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ],
    }

    scores = score_by_study(studies_source["ids"], studies_source["tissues"])
    draw_score_by_study_table(scores, studies_source)
    draw_score_by_study_box(scores, studies_source)

    scores, celltypes = score_by_celltype(
        studies_source["ids"], studies_source["tissues"]
    )
    draw_score_by_celltype_table(scores, celltypes)

    scores = score_by_cluster(studies_source["ids"], studies_source["tissues"])
    draw_scores_by_cluster(scores)


if __name__ == "__main__":
    main()
