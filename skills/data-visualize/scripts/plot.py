#!/usr/bin/env python3
"""Tạo đồ thị bằng matplotlib từ tham số dòng lệnh.

Usage:
    python3 plot.py --type <chart_type> --data '<json_data>' --output <file.png> [--config '<json_config>']

Chart types: scatter, line, bar, histogram, boxplot, heatmap, pie, regression, multi_line
"""
import argparse
import json
import sys
import os

import matplotlib
matplotlib.use("Agg")  # Non-interactive backend
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, MultipleLocator
import numpy as np

# Hỗ trợ tiếng Việt
plt.rcParams["font.family"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False


def apply_integer_ticks(ax, config):
    """Ép tick trên trục là số nguyên (hoặc theo step) để dễ đọc.

    Mặc định BẬT cho cả x và y. Người dùng có thể tắt riêng từng trục
    bằng `integer_xticks: false` / `integer_yticks: false`, hoặc
    chỉ định bước nhảy cụ thể bằng `xtick_step` / `ytick_step`.
    Nếu trục có tick là chuỗi (categorical) thì bỏ qua, không ép.
    """
    # Trục X
    if config.get("xtick_step") is not None:
        ax.xaxis.set_major_locator(MultipleLocator(config["xtick_step"]))
    elif config.get("integer_xticks", True):
        # Chỉ áp dụng khi trục x là numeric (kiểm tra qua giới hạn hữu hạn)
        try:
            xmin, xmax = ax.get_xlim()
            if np.isfinite(xmin) and np.isfinite(xmax):
                ax.xaxis.set_major_locator(MaxNLocator(integer=True, prune=None))
        except Exception:
            pass

    # Trục Y
    if config.get("ytick_step") is not None:
        ax.yaxis.set_major_locator(MultipleLocator(config["ytick_step"]))
    elif config.get("integer_yticks", True):
        try:
            ymin, ymax = ax.get_ylim()
            if np.isfinite(ymin) and np.isfinite(ymax):
                ax.yaxis.set_major_locator(MaxNLocator(integer=True, prune=None))
        except Exception:
            pass


def setup_plot(config):
    """Tạo figure và axes với cấu hình chung."""
    figsize = config.get("figsize", [10, 6])
    fig, ax = plt.subplots(figsize=tuple(figsize), dpi=100)
    if config.get("title"):
        ax.set_title(config["title"], fontsize=14, fontweight="bold", pad=15)
    if config.get("xlabel"):
        ax.set_xlabel(config["xlabel"], fontsize=12)
    if config.get("ylabel"):
        ax.set_ylabel(config["ylabel"], fontsize=12)
    ax.grid(True, alpha=0.3)
    return fig, ax


def plot_scatter(data, config, ax):
    x = data["x"]
    y = data["y"]
    color = config.get("color", "#3498db")
    label = config.get("label", "Dữ liệu")
    ax.scatter(x, y, s=70, c=color, alpha=0.7, edgecolors="white", linewidth=1.5, label=label)
    if config.get("show_legend", True):
        ax.legend(loc=config.get("legend_loc", "best"))


def smooth_curve(x, y, num_points=300):
    """Nội suy spline bậc 3 để tạo đường cong liên tục mượt mà.

    Trả về (x_smooth, y_smooth). Nếu scipy không có hoặc dữ liệu quá ít
    (< 4 điểm) thì trả về nguyên bản để vẽ đường thẳng nối điểm.
    """
    try:
        from scipy.interpolate import make_interp_spline
        x_arr = np.array(x, dtype=float)
        y_arr = np.array(y, dtype=float)
        if len(x_arr) < 4:
            return x_arr, y_arr
        # Đảm bảo x tăng dần (yêu cầu của spline)
        order = np.argsort(x_arr)
        x_arr, y_arr = x_arr[order], y_arr[order]
        spline = make_interp_spline(x_arr, y_arr, k=3)
        x_smooth = np.linspace(x_arr[0], x_arr[-1], num_points)
        y_smooth = spline(x_smooth)
        return x_smooth, y_smooth
    except Exception:
        return np.array(x, dtype=float), np.array(y, dtype=float)


def plot_line(data, config, ax):
    x = data["x"]
    y = data["y"]
    color = config.get("color", "#3498db")
    label = config.get("label", "Đường")
    linestyle = config.get("linestyle", "-")
    smooth = config.get("smooth", True)

    # Vẽ đường cong mượt (spline) hoặc đường thẳng nối điểm
    if smooth:
        x_smooth, y_smooth = smooth_curve(x, y)
        ax.plot(x_smooth, y_smooth, color=color, linewidth=2.5,
                linestyle=linestyle, label=label)
    else:
        ax.plot(x, y, color=color, linewidth=2.5,
                linestyle=linestyle, label=label)

    # Vẽ các điểm dữ liệu gốc lên trên đường cong
    ax.scatter(x, y, color=color, s=50, zorder=5)

    if config.get("show_legend", True):
        ax.legend(loc=config.get("legend_loc", "best"))


def plot_multi_line(data, config, ax):
    """data: {"x": [...], "series": [{"y": [...], "label": "...", "color": "..."}, ...]}"""
    x = data["x"]
    smooth = config.get("smooth", True)
    for s in data["series"]:
        color = s.get("color")
        linestyle = s.get("linestyle", "-")
        if smooth:
            x_smooth, y_smooth = smooth_curve(x, s["y"])
            ax.plot(x_smooth, y_smooth, color=color, linewidth=2.5,
                    linestyle=linestyle, label=s.get("label", ""))
        else:
            ax.plot(x, s["y"], color=color, linewidth=2.5,
                    linestyle=linestyle, label=s.get("label", ""))
        ax.scatter(x, s["y"], color=color, s=50, zorder=5)
    ax.legend(loc=config.get("legend_loc", "best"))


def plot_bar(data, config, ax):
    labels = data["labels"]
    values = data["values"]
    colors = data.get("colors") or ["#3498db"] * len(labels)
    bars = ax.bar(labels, values, color=colors, alpha=0.8, edgecolor="white", linewidth=1.5)
    if config.get("show_values", True):
        for bar in bars:
            h = bar.get_height()
            ax.annotate(f"{h}", xy=(bar.get_x() + bar.get_width() / 2, h),
                        xytext=(0, 3), textcoords="offset points",
                        ha="center", va="bottom", fontsize=11)


def plot_histogram(data, config, ax):
    values = data["values"]
    bins = config.get("bins", 10)
    color = config.get("color", "#3498db")
    ax.hist(values, bins=bins, color=color, alpha=0.7, edgecolor="white", linewidth=1.2)


def plot_boxplot(data, config, ax):
    """data: {"groups": [{"label": "...", "values": [...]}, ...]}"""
    labels = [g["label"] for g in data["groups"]]
    values = [g["values"] for g in data["groups"]]
    bp = ax.boxplot(values, labels=labels, patch_artist=True)
    for patch in bp["boxes"]:
        patch.set_facecolor("#3498db")
        patch.set_alpha(0.6)


def plot_heatmap(data, config, ax):
    """data: {"matrix": [[...], [...]], "row_labels": [...], "col_labels": [...]}"""
    matrix = np.array(data["matrix"])
    cmap = config.get("cmap", "Blues")
    im = ax.imshow(matrix, cmap=cmap, aspect="auto")
    if data.get("row_labels"):
        ax.set_yticks(range(len(data["row_labels"])))
        ax.set_yticklabels(data["row_labels"])
    if data.get("col_labels"):
        ax.set_xticks(range(len(data["col_labels"])))
        ax.set_xticklabels(data["col_labels"], rotation=45, ha="right")
    # Annotate cells
    if config.get("annotate", True):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                ax.text(j, i, f"{matrix[i, j]:.2f}", ha="center", va="center",
                        color="black", fontsize=10)
    plt.colorbar(im, ax=ax)


def plot_pie(data, config, ax):
    labels = data["labels"]
    values = data["values"]
    colors = data.get("colors")
    ax.pie(values, labels=labels, colors=colors, autopct="%1.1f%%",
           startangle=90, wedgeprops={"edgecolor": "white", "linewidth": 2})
    ax.axis("equal")


def plot_regression(data, config, ax):
    """Scatter plot + linear regression line + optional prediction point."""
    x = np.array(data["x"], dtype=float)
    y = np.array(data["y"], dtype=float)
    # Scatter
    ax.scatter(x, y, s=80, c="#3498db", alpha=0.7, edgecolors="white",
               linewidth=1.5, label="Dữ liệu thực", zorder=3)
    # Linear regression by least squares
    a, b = np.polyfit(x, y, 1)
    x_line = np.linspace(x.min() - (x.max() - x.min()) * 0.05,
                         x.max() + (x.max() - x.min()) * 0.05, 100)
    y_line = a * x_line + b
    ax.plot(x_line, y_line, color="#e74c3c", linestyle="--", linewidth=2.5,
            label=f"Đường hồi quy: y = {a:.3f}x + {b:.3f}", zorder=2)
    # Optional prediction point
    if "predict_x" in config:
        px = config["predict_x"]
        py = a * px + b
        ax.plot([px, px], [ax.get_ylim()[0], py], color="#27ae60",
                linestyle=":", linewidth=1.5, zorder=1)
        ax.plot([ax.get_xlim()[0], px], [py, py], color="#27ae60",
                linestyle=":", linewidth=1.5, zorder=1)
        ax.scatter([px], [py], s=120, facecolors="none", edgecolors="#27ae60",
                   linewidth=2.5, label=f"Dự đoán: x={px} → y≈{py:.2f}", zorder=4)
    ax.legend(loc=config.get("legend_loc", "best"))


def plot_knn(data, config, ax):
    """KNN visualization: scatter + highlight K nearest neighbors of query point.
    data: {"x": [...], "y": [...], "query_x": float, "k": int}
    """
    import math
    x = list(data["x"])
    y = list(data["y"])
    query_x = float(data["query_x"])
    k = int(data.get("k", 3))

    # Tính khoảng cách trên trục X (nearest neighbors theo diện tích)
    dists = [(i, abs(xi - query_x)) for i, xi in enumerate(x)]
    dists.sort(key=lambda t: t[1])
    nearest_idx = [t[0] for t in dists[:k]]

    # Vẽ tất cả điểm
    other_x = [x[i] for i in range(len(x)) if i not in nearest_idx]
    other_y = [y[i] for i in range(len(x)) if i not in nearest_idx]
    ax.scatter(other_x, other_y, s=80, c="#bdc3c7", alpha=0.6,
               edgecolors="white", linewidth=1.5, label="Dữ liệu khác", zorder=2)

    # Highlight K nearest
    near_x = [x[i] for i in nearest_idx]
    near_y = [y[i] for i in nearest_idx]
    ax.scatter(near_x, near_y, s=140, c="#3498db", alpha=0.9,
               edgecolors="white", linewidth=2,
               label=f"{k} hàng xóm gần nhất", zorder=4)

    # Tính trung bình giá của K nearest
    avg_y = sum(near_y) / k

    # Đường thẳng dọc cho query point
    ax.axvline(query_x, color="#27ae60", linestyle=":", linewidth=1.5, alpha=0.7, zorder=1)
    # Đường ngang cho dự đoán
    ax.axhline(avg_y, color="#27ae60", linestyle=":", linewidth=1.5, alpha=0.7, zorder=1)
    ax.scatter([query_x], [avg_y], s=180, marker="*", c="#27ae60",
               edgecolors="white", linewidth=2,
               label=f"Dự đoán: x={query_x} → y≈{avg_y:.2f}", zorder=5)

    # Annotate K nearest with index
    for rank, idx in enumerate(nearest_idx, 1):
        ax.annotate(f"#{rank}", xy=(x[idx], y[idx]),
                    xytext=(8, 8), textcoords="offset points",
                    fontsize=10, fontweight="bold", color="#2980b9")

    ax.legend(loc=config.get("legend_loc", "best"))


PLOTTERS = {
    "scatter": plot_scatter,
    "line": plot_line,
    "multi_line": plot_multi_line,
    "bar": plot_bar,
    "histogram": plot_histogram,
    "boxplot": plot_boxplot,
    "heatmap": plot_heatmap,
    "pie": plot_pie,
    "regression": plot_regression,
    "knn": plot_knn,
}


def main():
    parser = argparse.ArgumentParser(description="Tạo đồ thị bằng matplotlib.")
    parser.add_argument("--type", required=True, choices=list(PLOTTERS.keys()))
    parser.add_argument("--data", required=True, help="Dữ liệu JSON")
    parser.add_argument("--output", required=True, help="Đường dẫn file PNG")
    parser.add_argument("--config", default="{}", help="Config JSON")
    args = parser.parse_args()

    try:
        data = json.loads(args.data)
    except json.JSONDecodeError as e:
        print(f"Lỗi parse data JSON: {e}", file=sys.stderr)
        sys.exit(1)
    try:
        config = json.loads(args.config)
    except json.JSONDecodeError as e:
        print(f"Lỗi parse config JSON: {e}", file=sys.stderr)
        sys.exit(1)

    fig, ax = setup_plot(config)
    PLOTTERS[args.type](data, config, ax)

    # Ép tick là số nguyên cho các loại biểu đồ có trục numeric.
    # Các loại có trục categorical/đặc biệt thì bỏ qua.
    NUMERIC_TYPES = {"scatter", "line", "multi_line", "histogram", "regression", "knn"}
    if args.type in NUMERIC_TYPES:
        apply_integer_ticks(ax, config)

    # Tạo thư mục nếu chưa có
    out_dir = os.path.dirname(args.output)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    fig.tight_layout()
    fig.savefig(args.output, dpi=100, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
