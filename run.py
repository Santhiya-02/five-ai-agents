import subprocess
import sys

AGENTS = {
    "1": ("Resume Review Agent",        "resume-review-agent"),
    "2": ("Email Classification Agent", "email-classification-agent"),
    "3": ("Study Planner Agent",        "study-planner-agent"),
    "4": ("Contract Risk Analyzer",     "contract-risk-analyzer-agent"),
    "5": ("Bug Report Analyzer Agent",  "bug-report-analyzer-agent"),
}

print("\n========== AI AGENTS MENU ==========")
for key, (name, _) in AGENTS.items():
    print(f"  {key}. {name}")
print("=====================================")

choice = input("\nEnter number to run: ").strip()

if choice in AGENTS:
    name, folder = AGENTS[choice]
    print(f"\nRunning {name}...\n")
    subprocess.run([sys.executable, f"{folder}/main.py"])
else:
    print("Invalid choice.")
