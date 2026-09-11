# Lab: Structured Planning and Tool Use

## Scenario

You are supporting Project Aurora, a fictional consulting engagement. The client
is deciding whether to keep a tentative November 4 go-live date and which staffing
option fits within the approved budget.

This lab is self-contained. All project facts, policy information, staffing data,
and deterministic tools are included in the accompanying script. It does not
depend on Day 2 Lab 1 or any other repository.

## Learning objectives

By completing this lab, you will be able to:

- Compare a direct-answer prompt with a prompt that requires a visible plan and
  evidence list.
- Define local tools with clear inputs and outputs.
- Implement a model/tool loop that executes tool calls and returns observations to
  the model.
- Evaluate whether tool use improves factual accuracy and calculations.
- Document observable plans, evidence, actions, tool results, final answers, and
  caveats without treating private model reasoning as a required deliverable.

## The two tasks

### Task 1: Go-live recommendation

Answer this question:

> Should the client keep the November 4 go-live date?

The answer must use the project facts and go-live policy. A strong answer should
identify the relevant evidence, state a recommendation, and explain what remains
uncertain.

### Task 2: Staffing cost analysis

Compare the junior-heavy and specialist-heavy staffing options. Calculate the total
cost of each option, including the stated contingency, and identify which option is
within the approved budget.

The answer must use the staffing facts and the calculator tool rather than relying
on unaudited mental arithmetic.

## Three prompt versions per task

For each task, produce these three versions:

1. **Baseline** — ask directly for the answer using the supplied context.
2. **Structured plan** — require a short plan, relevant evidence, assumptions,
   and a final answer, but do not use tools.
3. **Tool use** — allow the model to call the supplied tools, record each action
   and result, and then provide the final answer.

The tool-use version follows this observable workflow:

```text
plan → tool call → tool result → final answer
```

Do not submit unrestricted private chain-of-thought. Record only the concise plan,
evidence, tool calls, observations, final answer, and caveats that a reviewer can
verify.

## Included tools

The script provides three deterministic local tools:

- `lookup_project_fact(key)` — retrieves a fact from the project packet.
- `lookup_go_live_policy(topic)` — retrieves the decision policy.
- `calculate_cost(hours, hourly_rate, contingency_percent)` — returns base cost,
  contingency, and total cost.

The model does not execute Python directly. It requests a named tool with JSON
arguments, and the local dispatcher executes only the allowed function.

## Deliverable

Submit one notebook or Python script containing:

- The two task prompts and all three versions for each task.
- The model parameters used for each run.
- The observable tool-call trace for tool-use versions.
- The final outputs and a short reflection for each task.
- A comparison of factual accuracy, calculation accuracy, unsupported claims, and
  usefulness to the client.

Use a table like this for your comparison:

| Version | Correct facts | Correct calculations | Unsupported claims | Useful to client |
|---|---|---|---|---|
| Baseline |  |  |  |  |
| Structured plan |  |  |  |  |
| Tool use |  |  |  |  |

## Running the example

The solution script runs one hardcoded experiment per process to avoid
exhausting a free-tier request quota. Edit `MODEL_NAME`, `SELECTED_TASK`, and
`SELECTED_VERSION` at the top of the solution file to choose a different
experiment or model.

For Gemini's OpenAI-compatible endpoint:

```bash
pip install openai
export GEMINI_API_KEY="your-key"
python SOLUTION_structured_tool_use.py
```

The Gemini endpoint configuration follows [Google's OpenAI compatibility
guide](https://ai.google.dev/gemini-api/docs/openai). The tool-call message shape
follows the [OpenAI Chat Completions API reference](https://developers.openai.com/api/reference/cli/resources/chat).

## Reflection questions

- Did the baseline answer use unsupported assumptions?
- Did the structured-plan version identify the right evidence without tools?
- Which tool calls were necessary, and did the model call them correctly?
- Did the calculator change the staffing recommendation?
- What would you verify before presenting the result to a client?

## Optional extensions

- Add a tool that retrieves a project fact by category rather than exact key.
- Add a third staffing option and compare all three.
- Run each prompt multiple times and compare variation.
- Add a deliberately incomplete fact and require the model to state what is
  unknown instead of guessing.
