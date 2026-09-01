#!/data/data/com.termux/files/usr/bin/bash
# Start training / fine-tuning

cd "$(dirname "$0")/.."
python -m model.training.train
