# ai-tutor
An AI teacher who will help you achieve your learning goals based on your abilities and level.

# how-to-use
Just modify the EssayContent, StudentProfile, Activities fields in All_In_One_AI_Tutor.sudo and paste it into chatgpt gpt-4 for conversation.

# Execution Examples
[Chinese Essay: 《小马过河》](https://chat.openai.com/share/d14eb903-11bf-4f37-b60e-0ce5d935ac3c)

# Two ways to achieve a high-performance 1-on-1 AI-Tutor
## Introduction
LessonPlan -1-*-> Activity

LessonPlan: detail plan on how to teach in one lesson 
Activity: detail activity in plan on how to act in one section
## Summary
For AI-Tutor, there are a total of three tasks that need to be accomplished:
1. Requirement&Profile Analysis:
   1. input: communication with students; data on students' prior learning. 
   2. output: student_requirement; student_profile;
2. Lesson Plan Generation: 
   1. input: student_requirement; student_profile;
   2. output: lesson_plan;
3. Teaching: 
   1. input: lesson_plan;
   2. input: lesson;

## Requirement&Profile Analysis

## Lesson Plan Generation

## Teaching
For Teaching, this can be a relatively long process, and there are three ways of thinking about it here. The demo for All in one system prompt has now been completed, and the next focus is on the All in one context.

### All in one system prompt
All_In_One_AI_Tutor.sudo is an implementation of this idea.

* pros: 
  * The entire orchestration process is also done in prompt, which greatly reduces the glue layer
  * High Contextual integrity
* cons:
  * When testing on GPT-4, it was found that once the number of lines of code reached around 230 (of course the number of tokens needs to be measured accurately here), a large amount of interference occurred.
  * Excessively long contexts will cause the execution to lose critical focus

### All in one context

* pros:
  * No need to do everything in one system prompt
  * Toggles the system prompt while keeping the context intact.
* cons:
  * When switching system prompts, need to maintain some consistency, otherwise it may have an impact on the dialog history
  * Excessively long contexts will cause the execution to lose critical focus
  
### Multiple context
The idea for this approach comes from anthropic's article (see references for details)
* pros:
  * No need to do everything in one system prompt
  * Not all tasks need to be accomplished in one context
* cons:
  * Smooth transitions when collaborating across different contexts require specialized designs
  * Choosing which information to synchronize between contexts is the challenge

# References
* This project uses [SudoLang](https://github.com/paralleldrive/sudolang-llm-support/tree/main) to implement the prompt part.
* The previous versions have been referenced in [Mr. Ranedeer](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor).
* The lesson planner section references the prompt combination process for [generating test cases in the openai-cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/Unit_test_writing_using_a_multi-step_prompt.ipynb)
* The requirement bot tries to imitate someone's tone to conduct a requirement interview.
* Anthropic [faithfulness of CoT](https://www-files.anthropic.com/production/files/measuring-faithfulness-in-chain-of-thought-reasoning.pdf)