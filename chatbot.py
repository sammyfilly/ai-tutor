import gradio as gr
from requirement_bot import create_requirement_bot
from plan_bot import create_plan_bot
from llm_material_bot import create_llm_material_player_bot



with gr.Blocks() as demo:
    student_requirement_markdown = gr.Markdown("### Requirement: ")
    def update_student_requirement(new_requirement: str) -> None:
        student_requirement = new_requirement
        print(f"student_requirement: {student_requirement}")
        gr.Markdown(f"### Requirement: {student_requirement}")

    create_requirement_bot(update_student_requirement) 
    create_plan_bot("123")
    create_llm_material_player_bot("123")

demo.queue()
demo.launch()