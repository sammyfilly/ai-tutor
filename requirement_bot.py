import gradio as gr
import openai
from typing import Callable
from config import chatgpt_deployment_id

student_requirements = ""

def create_requirement_bot(callback_func: Callable[[str], None]):
    with gr.Tab("Requirement") as requirement_tab:
        msg = gr.Text(
            lines=1, placeholder="Enter your function under test here")
        chatbot = gr.Chatbot()
        clear = gr.ClearButton([msg, chatbot])

        def user(user_message, history):
            return "", history + [[user_message, None]]

        async def bot(msg, history):
            formatted_msgs = format_array([msg for pair in history for msg in pair if msg is not None])
            response = openai.ChatCompletion.create(
                engine=chatgpt_deployment_id,
                messages=formatted_msgs,
                temperature=0.4,
                stream=True)

            for chunk in response:
                delta = chunk["choices"][0]["delta"]
                if "role" in delta:
                    role = delta["role"]
                    history[-1][1] = f""
                    print(f"{role}: ", end="")
                if "content" in delta:
                    content = delta["content"]
                    history[-1][1] += content
                    print(f"{content}: ", end="")
                else:
                    pass
                yield history

            if "###Requirement Analysis Finished###" in history[-1][1]:
                student_requirements = summarize_student_requirements(history)
                callback_func(student_requirements)

        response = msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot, [msg, chatbot], [chatbot]
        )
    return requirement_tab

def format_array(array):
    result = [{"role": "system", 
            "content": f"""
            As an AI one-on-one requirement analysist specializing in Chinese language studies, your objective is to help users reflect on their day and analyze any challenges they faced in their studies.
            You are very good at communicate with students.
            Start by asking open-ended questions, attentively listening to their responses, and providing tailored follow-up questions for a comprehensive understanding of their difficulties.

            #Rules
            1. Always use Chinese
            2. When you are sure you know challenges the user faced, restate the needs in your own words and confirm with the student.
            8. When the student confirms that your statement encompasses all the challenges they have encountered, just reply ###Requirement Analysis Finished###.
            3. Show your care and concern for the student
            4. Use a friendly and casual tone
            5. Ask one question at a time
            6. Don't try to give advice or solve the problem
            7. In the process of advancing a conversation, transitions and progressions should be as natural as possible.

            Start by introducing yourself and ask how his/her day went.
            """}]
    for index, element in enumerate(array):
        if index % 2 == 0:
            result.append({"role": "user", "content": element})
        else:
            result.append({"role": "assistant", "content": element})
    return result

def summarize_student_requirements(history):
    formatted_msgs = format_array([msg for pair in history for msg in pair if msg is not None])
    formatted_msgs.append({"role": "user", "content": "What's the student requirements?"})
    response = openai.ChatCompletion.create(
        engine=chatgpt_deployment_id,
        messages=formatted_msgs,
        temperature=0.4,
        stream=False)
    print(response)
    return response["choices"][0]["message"]["content"]