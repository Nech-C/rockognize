---
title: Mineral Identifier
emoji: 🪨
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 5.29.1
python_version: 3.11
app_file: app.py
fullWidth: true
header: default
short_description: Upload a rock image to identify its mineral composition using a trained model.
tags:
  - geology
  - mineralogy
  - image-classification
  - gradio
  - computer-vision
datasets:
  - Nech-C/mineralimage5K-98
pinned: true
---

# 🪨 Mineral Identifier

Welcome to the **Mineral Identifier** app! This tool uses a deep learning model to identify the **type of mineral** in a rock image you upload.

## 🚀 Features

- 🔍 **Image classification** powered by a trained neural network
- 📸 Upload an image of a mineral sample
- 💡 Get a **prediction** along with confidence levels
- 🌐 Built with [Gradio](https://gradio.app/) for fast, accessible user interaction

## 🧠 Behind the Model

The app is powered by a convolutional neural network trained on a curated dataset of mineral images including:
- Quartz
- Calcite
- Feldspar
- Mica
- And more!

If you’d like to explore the dataset used:
- [Dataset on Hugging Face Hub](https://huggingface.co/datasets/Nech-C/mineralimage5K-98)

## 🛠️ How to Use

1. Choose a photo of your rock/mineral sample.
2. The app will process the image and output the **predicted mineral type**.

## 💬 Feedback

If you encounter any issues or have suggestions for improvements, feel free to open an [issue on GitHub](https://github.com/Nech-C/rockognize/issues) or reach out on the [Hugging Face community](https://huggingface.co/spaces/Nech-C/Rock-Identifier).
