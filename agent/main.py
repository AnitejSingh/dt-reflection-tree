import csv
import os

# -------- Load Tree --------
BASE_DIR = os.path.dirname(__file__)
TREE_FILE = os.path.join(BASE_DIR, "..", "tree", "reflection-tree.tsv")

nodes = {}
children = {}

with open(TREE_FILE, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        node_id = row['id'].strip()
        nodes[node_id] = row

        parent = row['parentId'].strip()
        if parent:
            children.setdefault(parent, []).append(node_id)

# -------- State --------
state = {
    "answers": {},
    "axis1": {"internal": 0, "external": 0},
    "axis2": {"contribution": 0, "entitlement": 0},
    "axis3": {"self": 0, "team": 0, "other": 0}
}

# -------- Helpers --------
def apply_signal(signal):
    if not signal:
        return
    parts = signal.split(":")
    if len(parts) == 2:
        axis, val = parts
        if axis in state and val in state[axis]:
            state[axis][val] += 1

def get_dominant(axis):
    return max(state[axis], key=state[axis].get)

def interpolate(text):
    # Replace answers
    for k, v in state["answers"].items():
        text = text.replace(f"{{{k}.answer}}", v)

    # Replace dominant axis values
    for axis in ["axis1", "axis2", "axis3"]:
        text = text.replace(f"{{{axis}.dominant}}", get_dominant(axis))

    return text

def evaluate_condition(cond):
    cond = cond.strip()

    # answer-based condition
    if cond.startswith("answer="):
        values = cond.split("=")[1].split("|")
        last_answer = list(state["answers"].values())[-1]
        return last_answer in values

    # axis-based condition
    if ">=" in cond:
        left, val = cond.split(">=")
        axis, key = left.split(".")
        return state[axis][key] >= int(val)

    return False

def handle_decision(options):
    rules = options.split(";")
    for rule in rules:
        if ":" not in rule:
            continue
        cond, target = rule.split(":")
        if evaluate_condition(cond):
            return target.strip()
    return None

# -------- Engine --------
current = "START"

while True:
    node = nodes[current]
    node_type = node["type"].strip()
    text = node["text"].strip()
    options = node["options"].strip()
    target = node["target"].strip()
    signal = node["signal"].strip()

    # Apply signal
    apply_signal(signal)

    # Print text
    if text:
        print("\n" + interpolate(text))

    # Handle node types
    if node_type == "start" or node_type == "bridge":
        current = target if target else children.get(current, [None])[0]

    elif node_type == "question":
        opts = options.split("|")
        for i, opt in enumerate(opts, 1):
            print(f"{i}. {opt}")

        while True:
            try:
                choice = int(input("Choose option: "))
                if 1 <= choice <= len(opts):
                    answer = opts[choice - 1]
                    state["answers"][current] = answer
                    break
            except:
                pass
            print("Invalid input. Try again.")

        current = children[current][0]

    elif node_type == "decision":
        next_node = handle_decision(options)
        if not next_node:
            print("Decision error. No valid path.")
            break
        current = next_node

    elif node_type == "reflection":
        input("\n(Press Enter to continue)")
        current = children.get(current, [target])[0] if not target else target

    elif node_type == "summary":
        print("\n--- Summary ---")
        print(interpolate(text))
        current = children.get(current, [target])[0] if not target else target

    elif node_type == "end":
        print("\n" + text)
        break

    else:
        print(f"Unknown node type: {node_type}")
        break
