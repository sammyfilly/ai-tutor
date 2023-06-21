from langchain.chat_models import AzureChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain.schema import {SystemChatMessage, AIMessage}

def ask_for_learning_topic_and_preference():
    llm = AzureChatOpenAI(deployment_name="chat_confluence",model_name="gpt-35-turbo", verbose=True)
    memory = ConversationBufferWindowMemory(memory_key="chat_history", k=10, return_messages=True)
    chain = ConversationChain(llm, memory)
    systemMessage = SystemChatMessage(
        f"You are a before-class teacher. \
        It's your responsibility to make it clear that what the student what to learn and in which way the student want to learn. \
        Be polite and patient. \
        You should begin the chat and end it when you confirm that this task is completed.\
        Begin the chat by saying 'hi，我是你的AI老师，跟我说说你今天在学校学了什么内容吧。'"
    )
    chain.call(systemMessage)
    return {"topic": "topic", "preference": "preference"}

def plan_with_preference_and_topic(topic, preference):
    # TODO
    return plan

def execute_and_evaluate_secition(section): 
    """
    Execute the section and return the evaluation result. True represent meetGoal, vice versa.
    """
    # TODO 
    return True

def ask_for_feedback():
    # TODO
    return

def main():
    topic = ask_for_learning_topic()
    preference = ask_for_user_preference()

    plan = plan_with_preference_and_topic(topic, preference)

    # execute plan
    while (plan.isNotFinished() and plan.isNotTimeout()):
        section = plan.cur_section()
        is_goal_met = execute_and_evaluate_secition(section)
        section = plan.next(section, is_goal_met)

    ask_for_feedback()
