import gradio as gr
from gradio import Text
import threading
from plan import Planner

def create_plan_bot(student_requirements_input: str):
    with gr.Tab("PlanBot") as plan_bot_tab:
        essay_content_text_box = gr.Text(
            f"""
    ### Essay Summary
    《小马过河》讲述了一匹年轻的小马在妈妈的要求下去磨坊驮麦子的过程中，遇到了一条河。小马分别听到了牛和松鼠关于河水深浅的不同说法，犹豫不决，最后决定回家请教妈妈。经过妈妈的启发，小马明白了不能只听别人的话，要自己动脑筋，勇敢尝试。最后，小马顺利地过了河，完成了任务。这个故事教育孩子们要学会独立思考和勇敢尝试。
    ### Essay New words
    "驮", "匹", "欣慰", "哗哗", "犹豫", "迈", "淹"
            """,
            lines=1, placeholder="Enter your essay content here", label="Essay Content")
        student_requirement_text_box = gr.Text(
            f"""
    ### profile
    我是一个小学3年级男生。
    ### requirements
    {student_requirements_input}
    ### prefered_format
    我更喜欢通过游戏和讲故事的方式来学习。
            """,
            lines=1, placeholder="Enter your student requirement here", label="Student Requirement")

        chatbot = gr.Chatbot()
        clear = gr.ClearButton(
            [essay_content_text_box, student_requirement_text_box, chatbot])

        output_signal = []

        def user(essay_info, student_requirement_content, history):
            return essay_info, history

        async def bot(essay_content, student_requirement, history):

            def print_to_console(text: str, end: str = "\n"):
                if end == "\n":
                    # create a new entry in the history
                    history.append([None, ""])
                history[-1][1] += text
                output_signal.append(text)
                print(text, end=end)

            print(f"Essay Content: {essay_content}")
            planner = Planner(print_function=print_to_console)
            task_thread = threading.Thread(target=planner.plan, args=(
                essay_content, student_requirement))
            task_thread.start()
            while output_signal or task_thread.is_alive():
                if output_signal:
                    yield history

        student_requirement_text_box.submit(user, [essay_content_text_box, student_requirement_text_box, chatbot], [essay_content_text_box, chatbot], queue=False).then(
            bot, [essay_content_text_box,
                student_requirement_text_box, chatbot], [chatbot]
        )
    return plan_bot_tab