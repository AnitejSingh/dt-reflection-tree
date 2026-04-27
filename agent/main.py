import csv

TREE_FILE = "tree/reflection-tree.tsv"

# Load tree
nodes = {}
children = {}

with open(TREE_FILE, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        nodes[row['id']] = row
        parent = row['parentId']
        if parent:
            children.setdefault(parent, []).append(row['id'])

# State
state = {
    "answers": {},
    "axis1": {"internal": 0, "external": 0},
    "axis2": {"contribution": 0, "entitlement": 0},
    "axis3": {"self": 0, "team": 0, "other": 0}
}

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
    for key, val in state["answers"].items():
        text = text.replace(f"{{{key}.answer}}", val)
    text = text.replace("{axis1.dominant}", get_dominant("axis1"))
    text = text.replace("{axis2.dominant}", get_dominant("axis2"))
    text = text.replace("{axis3.dominant}", get_dominant("axis3"))
    return text

def run():
    current = "START"

    while True:
        node = nodes[current]
        text = interpolate(node["text"])
        print("\n" + text)

        apply_signal(node["signal"])

        if node["type"] == "end":
            break

        elif node["type"] == "question":
            options = node["options"].split("|")
            for i, opt in enumerate(options, 1):
                print(f"{i}. {opt}")
            choice = int(input("Choose: ")) - 1
            answer = options[choice]
            state["answers"][current] = answer

            # move to next child
            current = children[current][0]

        elif node["type"] == "decision":
            rules = node["options"].split(";")
            last_answer = list(state["answers"].values())[-1]

            moved = False
            for rule in rules:
                cond, target = rule.split(":")
                if cond.startswith("answer="):
                    values = cond.replace("answer=", "").split("|")
                    if last_answer in values:
                        current = target
                        moved = True
                        break
                else:
                    # simple condition handling
                    if "axis1.internal>=3" in cond and state["axis1"]["internal"] >= 3:
                        current = target
                        moved = True
                        break
                    if "axis1.external>=3" in cond and state["axis1"]["external"] >= 3:
                        current = target
                        moved = True
                        break
                    if "axis1.internal>=1" in cond and state["axis1"]["internal"] >= 1:
                        current = target
                        moved = True
                        break

            if not moved:
                current = list(children[node["parentId"]])[0]

        elif node["type"] in ["reflection", "bridge"]:
            input("\nPress Enter to continue...")
            current = node["target"] if node["target"] else children[current][0]

        elif node["type"] == "summary":
            print("\n--- Summary ---")
            print(text)
            current = children[current][0]

        else:
            current = children[current][0]

if __name__ == "__main__":
    run()
