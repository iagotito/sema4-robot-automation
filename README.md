# Robot Order Automation - Automation Certification Level II

This repository contains the solution for the **Automation Certification Level II** course from [Sema4.ai](https://sema4.ai/docs/automation/courses/build-a-robot-python). This robot automates the process of ordering robots from RobotSpareBin Industries Inc.

## What This Robot Does

The robot performs the following automated tasks:

1. **Downloads order data** from a CSV file containing robot orders
2. **Opens the RobotSpareBin website** and navigates to the robot order page
3. **Processes each order** by:
   - Filling out the robot configuration form (head, body, legs, address)
   - Previewing the robot configuration
   - Submitting the order
   - Handling order confirmation
4. **Generates receipts** by:
   - Capturing the order receipt as HTML
   - Converting the receipt to PDF format
   - Taking a screenshot of the configured robot
   - Embedding the robot screenshot into the PDF receipt
5. **Archives all receipts** into a ZIP file for easy distribution

## Course Context

This project is part of the **Automation Certification Level II** curriculum, which focuses on building practical automation solutions using Python and the Robocorp framework. The course teaches advanced automation concepts including web automation, file processing, PDF generation, and data handling.

👉 Learn more about the course: [Build a Robot - Python Course](https://sema4.ai/docs/automation/courses/build-a-robot-python)

## Running

#### VS Code
1. Get [Robocorp Code](https://robocorp.com/docs/developer-tools/visual-studio-code/extension-features) -extension for VS Code.
1. You'll get an easy-to-use side panel and powerful command-palette commands for running, debugging, code completion, docs, etc.

#### Command line

1. [Get RCC](https://github.com/robocorp/rcc?tab=readme-ov-file#getting-started)
1. Use the command: `rcc run`

## Results

🚀 After running the bot, check out the `log.html` under the `output` -folder.

## Dependencies

We strongly recommend getting familiar with adding your dependencies in [conda.yaml](conda.yaml) to control your Python dependencies and the whole Python environment for your automation.

<details>
  <summary>🙋‍♂️ "Why not just pip install...?"</summary>

Think of [conda.yaml](conda.yaml) as an equivalent of the requirements.txt, but much better. 👩‍💻 With `conda.yaml`, you are not just controlling your PyPI dependencies; you control the complete Python environment, which makes things repeatable and easy.

👉 You will probably need to run your code on another machine quite soon, so by using `conda.yaml`:
- You can avoid `Works on my machine` -cases
- You do not need to manage Python installations on all the machines
- You can control exactly which version of Python your automation will run on 
  - You'll also control the pip version to avoid dep. resolution changes
- No need for venv, pyenv, ... tooling and knowledge sharing inside your team.
- Define dependencies in conda.yaml, let our tooling do the heavy lifting.
- You get all the content of [conda-forge](https://prefix.dev/channels/conda-forge) without any extra tooling

> Dive deeper with [these](https://github.com/robocorp/rcc/blob/master/docs/recipes.md#what-is-in-condayaml) resources.

</details>
<br/>

> The full power of [rpaframework](https://robocorp.com/docs/python/rpa-framework) -libraries is also available on Python as a backup while we implement the new Python libraries.

## What now?

🚀 Now, go get'em

Start writing Python and remember that the AI/LLM's out there are getting really good and creating Python code specifically.

👉 Try out [Robocorp ReMark 💬](https://chat.robocorp.com)

For more information, do not forget to check out the following:
- [Robocorp Documentation -site](https://robocorp.com/docs)
- [Portal for more examples](https://robocorp.com/portal)
- Follow our main [robocorp -repository](https://github.com/robocorp/robocorp) as it is the main location where we developed the libraries and the framework.