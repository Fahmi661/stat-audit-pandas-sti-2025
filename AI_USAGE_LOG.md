# AI Usage Log — [Project Name]

## Summary

| Member | Role          | Tools           | ~% code AI-assisted | Interpretation cells AI-assisted? |
| ------ | ------------- | --------------- | ------------------- | --------------------------------- |
| [Ahmad Fahmi Fadillah] | Data Engineer | Claude, Copilot | ~60%                | No                                |
| [Zaki Musthafa]        | Estimation Analyst  | Claude, Copilot | ~60%                | No                                |
| [Felisgi Mashinta]     | Inference Analyst   | Claude, Copilot | ~60%                | No                                |
| [M. Hikmal Mutaqin]    | Hypothesis Analyst  | Claude, Copilot | ~60%                | No                                |
| [Faadhel Mubaarak]     | Computation Analyst | Copilot | ~64%                | No                                |

## Per-Member Detail

### Member A — [Ahmad Fahmi Fadillah]

| #   | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1   | GitHub API Data Extraction Setup | Gemini | "How to fetch 5000 closed issues and 5000 closed PRs from GitHub REST API for pandas-dev/pandas efficiently?" | Used to structure the initial request parameters (`per_page=100` and loop pagination) in the `ambil_data.py` script. | Very helpful for boilerplate API connection code, but needed adjustments to handle GitHub rate limits manually. |
| 2   | Data Cleaning & Datetime Conversion | Gemini | "How to convert string timestamps into datetime object in Pandas and drop rows with missing close dates?" | Used to clean the raw API response and calculate the exact `close_time_days` metric for the EDA notebook. | Accurate and clean. It correctly suggested using `pd.to_datetime()` and `.dropna()`. |
| 3   | Git and Repository Troubleshooting | Gemini | "Why am I getting 'src refspec main does not match any' and how to clean a nested duplicated folder structure inside VS Code?" | Used to safely move the final PDF report using PowerShell commands and resolve git branching issues (`git branch -M main`). | Critical lifesaver. It helped fix terminal path errors and prevented accidental deletion of core project files. |

### Member B — [Zaki Musthafa]

| #   | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1   | ...  | ...  | ...    | ...                     | ...                            |

### Member C — [Felisgi Mashinta]

| #   | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1   | ...  | ...  | ...    | ...                     | ...                            |

### Member D — [Muhammad Hikmal Mutaqin]

| #   | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1   | ...  | ...  | ...    | ...                     | ...                            |

### Member E — [Faadhel Mubaarak]

| #   | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1   | Generated Notebook High-Level Overview | Copilot  | "Generate me an overview for this 05-simulation.ipynb task according to the specs" | ...                     | ...                            |
| 2   | Helping In Concept Understanding | Copilot | "What is monte carlo simulation? and how do i apply it to the notebook?" | ... | ... |
| 3   | Code Debugging | Copilot | "why cant the notebook run? is it dependencies or notebook kernel issues?" | ... | ...


## Group Reflection (150–300 words)

How did your group's use of AI evolve over three weeks? What did AI handle well?
Where did output need significant correction? Was there a moment you chose _not_
to use AI — and why?
