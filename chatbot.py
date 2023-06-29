import gradio as gr
from requirement_bot import create_requirement_bot
from plan_bot import create_plan_bot
from llm_material_bot import create_llm_material_player_bot


with gr.Blocks() as demo:
    intermedia_res_text_area = gr.TextArea(
        "", label="Intermedia Result", interactive=True, visible=True)
    create_requirement_bot(intermedia_res_text_area)
    create_plan_bot(intermedia_res_text_area)
    create_llm_material_player_bot(intermedia_res_text_area)

demo.queue()
demo.launch()
