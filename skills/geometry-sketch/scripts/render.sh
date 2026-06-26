#!/usr/bin/env bash
# render.sh - biên dịch file TikZ standalone ra PNG.
#
# Usage:
#   render.sh <input.tex> <output.png> [max_size]
#
# - input.tex   : đường dẫn file TeX (dùng \documentclass[border=...]{standalone}).
# - output.png  : đường dẫn PNG đầu ra. Thư mục đích sẽ được tạo nếu cần.
# - max_size    : tuỳ chọn, cạnh dài nhất tính theo pixel (mặc định 2400).
#
# Yêu cầu: pdflatex + (sips trên macOS hoặc pdftoppm trên Linux).

set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <input.tex> <output.png> [max_size]" >&2
  exit 2
fi

INPUT_TEX="$1"
OUTPUT_PNG="$2"
MAX_SIZE="${3:-2400}"

if [[ ! -f "$INPUT_TEX" ]]; then
  echo "Error: input file not found: $INPUT_TEX" >&2
  exit 1
fi

if ! command -v pdflatex >/dev/null 2>&1; then
  echo "Error: pdflatex not found. Install TeX Live first." >&2
  exit 1
fi

# Tạo thư mục đích cho PNG nếu chưa có.
OUT_DIR="$(dirname "$OUTPUT_PNG")"
mkdir -p "$OUT_DIR"

# Biên dịch trong thư mục tạm để không để rác lại.
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

cp "$INPUT_TEX" "$WORK/fig.tex"

# Biên dịch. In log nếu lỗi.
if ! ( cd "$WORK" && pdflatex -interaction=nonstopmode -halt-on-error fig.tex >pdflatex.log 2>&1 ); then
  echo "Error: pdflatex failed. Last 40 lines of log:" >&2
  tail -n 40 "$WORK/pdflatex.log" >&2
  exit 1
fi

# Chuyển PDF -> PNG. Ưu tiên pdftoppm (chất lượng cao, control DPI), fallback sips trên macOS.
if command -v pdftoppm >/dev/null 2>&1; then
  # 300 DPI cho đẹp cả khi in.
  pdftoppm -png -r 300 "$WORK/fig.pdf" "$WORK/fig" >/dev/null
  # pdftoppm thêm hậu tố -1 cho trang đầu.
  if [[ -f "$WORK/fig-1.png" ]]; then
    mv "$WORK/fig-1.png" "$OUTPUT_PNG"
  elif [[ -f "$WORK/fig-01.png" ]]; then
    mv "$WORK/fig-01.png" "$OUTPUT_PNG"
  else
    echo "Error: pdftoppm did not produce expected output." >&2
    exit 1
  fi
elif command -v sips >/dev/null 2>&1; then
  sips -s format png --resampleHeightWidthMax "$MAX_SIZE" "$WORK/fig.pdf" --out "$OUTPUT_PNG" >/dev/null
else
  echo "Error: need pdftoppm (Linux) or sips (macOS) to convert PDF to PNG." >&2
  exit 1
fi

echo "$OUTPUT_PNG"
