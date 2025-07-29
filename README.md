# Lab: Chain-of-Thought & ReAct Prompting

---

## Table of Contents

* [Scenario / Background](#scenario--background)
* [Objectives](#objectives)
* [Task Overview](#task-overview)
* [Requirements](#requirements)
* [Data Guidance](#data-guidance)
* [Deliverables](#deliverables)
* [Steps & Recommendations](#steps--recommendations)
* [Extension / Stretch Goals](#extension--stretch-goals)
* [References & Resources](#references--resources)

---

### Scenario / Background

As generative AI models become more capable, they can tackle multi‑step reasoning tasks such as planning museum exhibits, composing educational content or solving logic puzzles. Simply asking the model for an answer often produces shallow results. Research on *chain‑of‑thought* (CoT) prompting has shown that guiding a model to articulate intermediate reasoning steps dramatically improves performance on complex tasks. [See Google Research](https://research.google/pubs/towards-understanding-chain-of-thought-prompting-an-empirical-study-of-what-matters/#:~:text=Abstract)

A complementary technique, *ReAct*, interleaves **Re**asoning and **Act**ion steps, enabling the model to update its plan and interact with external tools (e.g., search engines or APIs); this helps reduce hallucinations and leads to more interpretable solutions. [See arXiv](https://arxiv.org/abs/2210.03629)

In this lab you will practise both methods and combine them for robust multi‑step problem solving.

### Objectives

By the end of this lab you will be able to:

* **Formulate chain‑of‑thought prompts** that encourage the model to articulate intermediate reasoning steps when tackling complex tasks.
  [Read Google Research](https://research.google/pubs/towards-understanding-chain-of-thought-prompting-an-empirical-study-of-what-matters/#:~:text=Abstract)
* **Apply the ReAct paradigm** by alternating reasoning with external actions, such as querying a knowledge base or performing intermediate calculations, to obtain accurate and grounded outputs.
  [See arXiv](https://arxiv.org/abs/2210.03629)
* **Combine CoT and ReAct** for challenging multi‑step tasks, observing how structured reasoning and actionable queries complement each other.
* **Practise task decomposition**, breaking down complex problems into smaller steps and guiding the model through each stage.

### Task Overview

You will design prompts for at least two multi‑step tasks of your choice. Possible scenarios include crafting a descriptive overview of a museum exhibit using multiple information sources, solving a logic or mathematical puzzle, or creating a step‑by‑step guide for an educational concept. For each task you will:

1. **Develop a baseline prompt** asking for the final answer without explicit reasoning.
2. **Write a chain‑of‑thought prompt** that instructs the model to "think step by step" or "show its reasoning" before answering. Observe differences in output quality and completeness.
   [See Google Research](https://research.google/pubs/towards-understanding-chain-of-thought-prompting-an-empirical-study-of-what-matters/#:~:text=Abstract)
3. **Implement a ReAct prompt** that interleaves reasoning and actions. After each reasoning step, instruct the model to call a function, look up information or perform calculations. Provide mock results for external calls if necessary.
   [See arXiv](https://arxiv.org/abs/2210.03629)
4. **Combine CoT and ReAct** into one workflow, where the model uses chain‑of‑thought reasoning to plan and then executes actions to retrieve or verify information.

### Requirements

Your submission must include:

* **At least two distinct tasks**, each involving complex reasoning or multi‑step problem solving.
* **Three versions per task**: baseline (no reasoning), chain‑of‑thought, and ReAct or combined CoT+ReAct.
* **Documentation of reasoning chains** for CoT and ReAct versions, showing intermediate thoughts and actions.
* **Reflection** on the effectiveness of chain‑of‑thought and ReAct techniques: discuss which methods yielded better results, challenges encountered, and potential improvements.

### Data Guidance

This lab does not provide specific datasets. Choose or create your own short texts, logic puzzles, or scenarios for your tasks. For summarization or translation tasks, ensure you have both the source text and a reference answer if you wish to compare output quality. Suitable reference materials include:

* A paragraph or article to summarise (with a gold‑standard summary).
* A short sentence or paragraph in a foreign language with its official translation.

If you need to source data, search open platforms such as **Hugging Face Datasets**, **Kaggle**, or **data.gov**, which host a variety of datasets across domains.
[Hugging Face Datasets](https://huggingface.co/docs/hub/en/datasets-overview#:~:text=Datasets%20on%20the%20Hub)
[data.gov](https://data.gov/#:~:text=The%20Home%20of%20the%20U,Government%27s%20Open%20Data)

Choose datasets that include both input and reference outputs if you wish to manually assess output quality.

### Deliverables

You should submit:

* A **notebook or Python script** implementing each task. Include prompts, model calls, and intermediate reasoning and actions.
* A **short report or markdown file** summarizing each task: describe the problem, outline the prompts, present key outputs, and reflect on the results.

### Steps & Recommendations

1. **Choose your tasks.** Select two tasks requiring multiple reasoning steps (e.g., summarising a museum exhibit plan, solving a logic puzzle or constructing an educational lesson plan).
2. **Write a baseline prompt.** Ask the model for the final answer without explicit reasoning. Save the output.
3. **Craft a chain‑of‑thought prompt.** Instruct the model to think step by step, list intermediate steps or rationales. Research from Google notes that chain‑of‑thought prompts can dramatically improve reasoning performance.
   [See Google Research](https://research.google/pubs/towards-understanding-chain-of-thought-prompting-an-empirical-study-of-what-matters/#:~:text=Abstract)
4. **Implement ReAct prompts.** Alternate reasoning steps with explicit actions. For example, after explaining what information is needed, instruct the model to call a search function or look up facts. Provide mock or real responses for actions. ReAct integrates reasoning and action to reduce hallucinations and improve interpretability.
   [See arXiv](https://arxiv.org/abs/2210.03629)
5. **Combine CoT and ReAct.** Build a prompt that uses chain‑of‑thought to plan the solution and ReAct to perform retrieval or calculations at appropriate times.
6. **Reflect.** Discuss which prompting strategy produced the best reasoning or most accurate result. Consider whether chain‑of‑thought alone sufficed or whether ReAct helped gather external information. Note any limitations or potential improvements.

### Extension / Stretch Goals

* **Few‑shot prompting:** Provide one or two examples of solved tasks in your prompt to see if it improves reasoning.
* **Tool integration:** Explore integrating simple external tools (e.g., a Wikipedia API or a calculator) into your ReAct workflows. Document how the model uses these tools and whether they enhance performance.
* **Comparison across models:** Evaluate prompts using different models (e.g., GPT‑4o vs. smaller models like OPT‑1.3B) and compare reasoning quality and hallucination rates.
  [OPT-1.3B on HuggingFace](https://huggingface.co/facebook/opt-1.3b#:~:text=,models%20are%20available%20for%20study)

### References & Resources

* **Chain‑of‑Thought prompting -- Google research**: explains that encouraging models to produce intermediate rationales can significantly improve multi‑step reasoning.
  [Google Research](https://research.google/pubs/towards-understanding-chain-of-thought-prompting-an-empirical-study-of-what-matters/#:~:text=Abstract)
* **ReAct: Synergizing reasoning and acting**: describes the ReAct paradigm, which interleaves reasoning traces with actions to reduce hallucinations and improve task‑solving.
  [arXiv](https://arxiv.org/abs/2210.03629)
* **Hugging Face datasets**, **Kaggle**, **data.gov**: offer a variety of datasets for summarization, translation and other tasks.
  [Hugging Face Datasets](https://huggingface.co/docs/hub/en/datasets-overview#:~:text=Datasets%20on%20the%20Hub)
  [data.gov](https://data.gov/#:~:text=The%20Home%20of%20the%20U,Government%27s%20Open%20Data)
