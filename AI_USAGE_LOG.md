# AI Usage Log — [Project Name]

## Summary

| Member | Role          | Tools           | ~% code AI-assisted | Interpretation cells AI-assisted? |
| ------ | ------------- | --------------- | ------------------- | --------------------------------- |
| [Ahmad Fahmi Fadillah] | Data Engineer | Claude, Copilot | ~60%                | No                                |
| [Zaki Musthafa]        | Estimation Analyst  | Claude, Copilot | ~60%                | No                                |
| [Felisgi Mashinta]     | Inference Analyst   | Gemini | ~60%                | No                                |
| [M. Hikmal Mutaqin]    | Hypothesis Analyst  | Claude, Copilot | ~60%                | No                                |
| [Faadhel Mubaarak]     | Computation Analyst | Copilot | ~64%                | No                                |

## Per-Member Detail

### Member A — [Ahmad Fahmi Fadillah]

| #   | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1   | GitHub API Data Extraction Setup | Gemini | "How to fetch 5000 closed issues and 5000 closed PRs from GitHub REST API for pandas-dev/pandas efficiently?" | Used to structure the initial request parameters (`per_page=100` and loop pagination) in the `ambil_data.py` script. | Very helpful for boilerplate API connection code, but needed adjustments to handle GitHub rate limits manually. |
| 2   | Data Cleaning & Datetime Conversion | Gemini | "How to convert string timestamps into datetime object in Pandas and drop rows with missing close dates?" | Used to clean the raw API response and calculate the exact `close_time_days` metric for the EDA notebook. | Accurate and clean. It correctly suggested using `pd.to_datetime()` and `.dropna()`. |
| 3   | Python Virtual Environment & Path Bug | Gemini | "FileNotFoundError: [Errno 2] No such file or directory: '../data/clean/issues_clean.csv' in VS Code Jupyter notebook, how to fix working directory?" | Used to configure the notebook kernel settings in VS Code and fix the relative file pathing so the notebook could read the dataset correctly. | Excellent. It helped me understand that the VS Code notebook terminal was running from a different root path, saving debugging time. | terminal path errors and prevented accidental deletion of core project files. |

### Member B — [Zaki Musthafa]

| #   | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1   | ...  | ...  | ...    | ...                     | ...                            |

### Member C — [Felisgi Mashinta]

| #   | Task | Tool | Prompt | How the output was used | How do you evaluate the output |
| --- | ---- | ---- | ------ | ----------------------- | ------------------------------ |
| 1   | Mathematical Formula Verification in Python | Gemini | "How to implement Wald Interval for Bernoulli trials and Poisson confidence interval using scipy.stats efficiently?" | Used to construct the mathematical functions ci_bernoulli and ci_poisson_from_lambda to ensure accurate calculation of the critical z-value. | Highly helpful in ensuring the statistical formula syntax was correct |
| 2   | Visualisation Code Optimization | Gemini | "How to plot two subplots for Bernoulli and Poisson interval side by side using plt.subplots?" | Used as the foundation for creating the comparative visualization plots between the Frequentist and Bayesian methods at the end of the notebook. | The provided visualization code was well-structured, but it still required manual modifications for adjusting the axis labels and coloring. |

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
