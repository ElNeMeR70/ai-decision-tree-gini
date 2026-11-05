"""Decision Tree Gini Impurity Evaluator"""

def gini_impurity(labels):
    total = len(labels)
    if total == 0: return 0.0
    counts = {}
    for l in labels: counts[l] = counts.get(l, 0) + 1
    return 1.0 - sum((c / total) ** 2 for c in counts.values())

if __name__ == "__main__":
    print("[RUN] Decision Tree Gini Impurity...")
    g = gini_impurity(["cat", "cat", "dog", "cat"])
    print(f"[OK] Gini Impurity: {g:.4f}")
