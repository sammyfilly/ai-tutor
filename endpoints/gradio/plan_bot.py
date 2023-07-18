import gradio as gr
from gradio import Text
import threading
from tools.plan import Planner
from queue import Queue
import time


def create_plan_bot(student_requirements_text_box):
    with gr.Tab("PlanBot") as plan_bot_tab:

        plan_button = gr.Button("Make a Lesson Plan")
        chatbot = gr.Chatbot(label="Console")

        def user(essay_info, history):
            return history

        async def bot(student_requirement, history):
            output_signal = []

            def print_to_console(text: str, end: str = "\n"):
                if end == "\n":
                    # create a new entry in the history
                    history.append([None, ""])
                history[-1][1] += text
                output_signal.append(text)
                print(text, end=end)

            essay_content = f"""
    ### Essay Summary
    《小马过河》讲述了一匹年轻的小马在妈妈的要求下去磨坊驮麦子的过程中，遇到了一条河。小马分别听到了牛和松鼠关于河水深浅的不同说法，犹豫不决，最后决定回家请教妈妈。经过妈妈的启发，小马明白了不能只听别人的话，要自己动脑筋，勇敢尝试。最后，小马顺利地过了河，完成了任务。这个故事教育孩子们要学会独立思考和勇敢尝试。
    ### Essay New words
    "驮", "匹", "欣慰", "哗哗", "犹豫", "迈", "淹"
            """

            planner = Planner(print_function=print_to_console)

            result_queue = Queue()

            def put_result_in_queue(result: str):
                result_queue.put(result)

            task_thread = threading.Thread(target=planner.plan, args=(
                essay_content, student_requirement, put_result_in_queue))
            task_thread.start()

            while output_signal or task_thread.is_alive():
                if output_signal:
                    output_signal.pop(0)
                    yield [history, student_requirement]
                    time.sleep(0.1)

            thread_res = result_queue.get()
            print(f"thread_res: {thread_res}")
            yield [history, thread_res]

        plan_button.click(bot, [student_requirements_text_box, chatbot], [
                          chatbot, student_requirements_text_box])
    return plan_bot_tab
