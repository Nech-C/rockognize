import os

from dotenv import load_dotenv
from transformers import pipeline
import gradio as gr

load_dotenv()

key = os.getenv("API_KEY")

pipe = pipeline("image-classification", model="Nech-C/mineralimage5K-98", device='cpu', token=key)

def classify_image(image):
    # [{'label': 'quartz', 'score': 0.20238091051578522}, {'label': 'celestine', 'score': 0.11984242498874664},
    # {'label': 'credit', 'score': 0.05711612477898598}, {'label': 'aragonite', 'score': 0.039466191083192825},
    # {'label': 'calcite', 'score': 0.03766309469938278}]
    result = pipe(image)
    output = {}
    for item in result:
        output[item['label']] = item['score']
    return output

examples = [
    ["examples/quartz.jpg"],
    ["examples/agate.jpg"],
    ["examples/topaz.jpg"],
]
with gr.Blocks() as demo:
    gr.Markdown("# 🪨 Rockognize")
    gr.Markdown("Upload an image of a rock or mineral and get its top predictions.")

    with gr.Tab("Mineral Image Classification"):
        with gr.Row(height="80%"):
            with gr.Column():
                image_input = gr.Image(type="pil", label="upload Image", height=300)
                submit_button = gr.Button("Classify")
                gr.Examples(
                    examples=examples,
                    inputs=image_input,
                    outputs=label_output,
                    label="Try Examples",
                    examples_per_page=3,
                    cache_examples=False,
                    fn=classify_image,
                )
            with gr.Column():
                label_output = gr.Label(label="Top 5 Predictions")
        

            submit_button.click(
                classify_image,
                inputs=image_input,
                outputs=label_output
            )

demo.launch()