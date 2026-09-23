import json
from openai import OpenAI

API_KEY = ""
MODEL_NAME = "gemini-1.5-pro"
SELECTED_TASK = "go_live"       # "go_live" or "staffing"
SELECTED_VERSION = "tool_use"   # "baseline", "structured_plan", or "tool_use"

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

PROJECT_FACTS = {
    "client": "Meridian Financial Group",
    "project": "Aurora",
    "go_live_date": "November 4",
    "uat_status": "UAT completed with 3 critical defects open",
    "defects_open": "3 critical, 12 minor",
    "training_status": "Training 60% complete",
    "data_migration": "Data migration dry run passed",
    "infrastructure": "Infrastructure sign-off received",
    "stakeholder_approval": "Pending CFO sign-off",
    "approved_budget": "$520,000",
    "budget_amount": 520000,
}

GO_LIVE_POLICY = {
    "critical_defects": "Go-live is not permitted if any critical defects remain open.",
    "training": "Training must be at least 80% complete before go-live.",
    "data_migration": "A successful data migration dry run is required.",
    "infrastructure": "Infrastructure sign-off is required.",
    "stakeholder": "All required stakeholder approvals must be obtained before go-live.",
}

STAFFING_OPTIONS = {
    "junior_heavy": {"hours": 3200, "hourly_rate": 120, "contingency_percent": 15},
    "specialist_heavy": {"hours": 1800, "hourly_rate": 210, "contingency_percent": 10},
}


def lookup_project_fact(key):
    return str(PROJECT_FACTS.get(key, f"No fact found for key: {key}"))


def lookup_go_live_policy(topic):
    return GO_LIVE_POLICY.get(topic, f"No policy found for topic: {topic}")


def calculate_cost(hours, hourly_rate, contingency_percent):
    base = hours * hourly_rate
    contingency = base * contingency_percent / 100
    total = base + contingency
    return {"base_cost": base, "contingency": contingency, "total_cost": total}


def dispatch_tool(name, args):
    if name == "lookup_project_fact":
        return lookup_project_fact(**args)
    elif name == "lookup_go_live_policy":
        return lookup_go_live_policy(**args)
    elif name == "calculate_cost":
        return calculate_cost(**args)
    else:
        return f"Unknown tool: {name}"


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "lookup_project_fact",
            "description": "Retrieves a fact from the Project Aurora packet.",
            "parameters": {
                "type": "object",
                "properties": {
                    "key": {"type": "string", "description": "The fact key to look up."}
                },
                "required": ["key"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "lookup_go_live_policy",
            "description": "Retrieves the go-live decision policy for a given topic.",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "Policy topic (e.g. critical_defects, training)."}
                },
                "required": ["topic"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_cost",
            "description": "Calculates base cost, contingency, and total cost for a staffing option.",
            "parameters": {
                "type": "object",
                "properties": {
                    "hours": {"type": "number"},
                    "hourly_rate": {"type": "number"},
                    "contingency_percent": {"type": "number"}
                },
                "required": ["hours", "hourly_rate", "contingency_percent"]
            }
        }
    }
]

GO_LIVE_CONTEXT = """Project Aurora facts:
- Client: Meridian Financial Group
- Proposed go-live: November 4
- UAT status: UAT completed with 3 critical defects open
- Open defects: 3 critical, 12 minor
- Training status: 60% complete
- Data migration: dry run passed
- Infrastructure: sign-off received
- Stakeholder approval: CFO sign-off pending

Go-live policy:
- Go-live is not permitted if any critical defects remain open.
- Training must be at least 80% complete before go-live.
- A successful data migration dry run is required.
- Infrastructure sign-off is required.
- All required stakeholder approvals must be obtained before go-live."""

STAFFING_CONTEXT = """Project Aurora staffing options:
- Junior-heavy: 3,200 hours at $120/hr with 15% contingency
- Specialist-heavy: 1,800 hours at $210/hr with 10% contingency
- Approved budget: $520,000"""

PROMPTS = {
    "go_live": {
        "baseline": f"{GO_LIVE_CONTEXT}\n\nShould the client keep the November 4 go-live date?",
        "structured_plan": (
            f"{GO_LIVE_CONTEXT}\n\n"
            "Answer whether the client should keep the November 4 go-live date.\n"
            "Structure your response as:\n"
            "Plan: (what you need to check)\n"
            "Evidence: (relevant facts from the context)\n"
            "Assumptions: (anything you are assuming)\n"
            "Recommendation: (yes or no, with brief reasoning)\n"
            "Caveats: (what remains uncertain)"
        ),
        "tool_use": (
            "You have access to tools to look up Project Aurora facts and go-live policy. "
            "Use them to determine whether the client should keep the November 4 go-live date. "
            "State your plan, call the relevant tools, then give a final recommendation with caveats."
        ),
    },
    "staffing": {
        "baseline": f"{STAFFING_CONTEXT}\n\nCompare the two staffing options and identify which is within the approved budget.",
        "structured_plan": (
            f"{STAFFING_CONTEXT}\n\n"
            "Compare the junior-heavy and specialist-heavy staffing options.\n"
            "Structure your response as:\n"
            "Plan: (what calculations are needed)\n"
            "Evidence: (the numbers from the context)\n"
            "Calculations: (show your work)\n"
            "Recommendation: (which option fits the budget)\n"
            "Caveats: (any uncertainties)"
        ),
        "tool_use": (
            "You have access to a calculate_cost tool and project fact lookup tools. "
            "Compare the junior-heavy (3200 hrs, $120/hr, 15% contingency) and specialist-heavy "
            "(1800 hrs, $210/hr, 10% contingency) staffing options for Project Aurora. "
            "The approved budget is $520,000. "
            "Use the calculator for each option and state which fits the budget."
        ),
    },
}


def run_baseline(task):
    prompt = PROMPTS[task]["baseline"]
    print(f"\n=== BASELINE — {task} ===")
    print(f"Prompt: {prompt}\n")
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message.content
    print(f"Response:\n{answer}\n")
    return answer


def run_structured_plan(task):
    prompt = PROMPTS[task]["structured_plan"]
    print(f"\n=== STRUCTURED PLAN — {task} ===")
    print(f"Prompt: {prompt}\n")
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message.content
    print(f"Response:\n{answer}\n")
    return answer


def run_tool_use(task):
    prompt = PROMPTS[task]["tool_use"]
    print(f"\n=== TOOL USE — {task} ===")
    print(f"Prompt: {prompt}\n")

    messages = [{"role": "user", "content": prompt}]

    while True:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )
        msg = response.choices[0].message

        if msg.tool_calls:
            messages.append(msg)
            for tc in msg.tool_calls:
                args = json.loads(tc.function.arguments)
                print(f"Tool call: {tc.function.name}({args})")
                result = dispatch_tool(tc.function.name, args)
                print(f"Result: {result}\n")
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": json.dumps(result)
                })
        else:
            print(f"Final answer:\n{msg.content}\n")
            return msg.content


def main():
    task = SELECTED_TASK
    version = SELECTED_VERSION

    if version == "baseline":
        run_baseline(task)
    elif version == "structured_plan":
        run_structured_plan(task)
    elif version == "tool_use":
        run_tool_use(task)

    print("\n--- Comparison table ---")
    print("| Version         | Correct facts | Correct calculations | Unsupported claims | Useful to client |")
    print("|-----------------|---------------|----------------------|--------------------|------------------|")
    print("| Baseline        |               |                      |                    |                  |")
    print("| Structured plan |               |                      |                    |                  |")
    print("| Tool use        |               |                      |                    |                  |")


if __name__ == "__main__":
    main()
