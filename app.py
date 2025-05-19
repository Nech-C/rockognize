import os

from dotenv import load_dotenv
from transformers import pipeline
import gradio as gr

load_dotenv()

key = os.getenv("KEY")

pipe = pipeline("image-classification", model="Nech-C/mineralimage5K-98", device='cpu')

def classify_image(image):
    # [{'label': 'quartz', 'score': 0.20238091051578522}, {'label': 'celestine', 'score': 0.11984242498874664},
    # {'label': 'credit', 'score': 0.05711612477898598}, {'label': 'aragonite', 'score': 0.039466191083192825},
    # {'label': 'calcite', 'score': 0.03766309469938278}]
    result = pipe(image)
    output = {}
    for item in result:
        output[item['label']] = item['score']
    return output
demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=5),
    title="Rockognize",
    description="A simple app to classify rocks and minerals.",
    theme="default",
)



demo.launch()