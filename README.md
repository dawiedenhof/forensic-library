# Introduction 
Environment setup to run the analysis for the a project on the Forensic Analytics Server

When copying this template, please make sure to replace the 'MY_PROJECT' placeholders with 
your project nane in the text below and in the pyproject.toml file.

# Installation

This project uses Poetry for dependency management (and if you want also for virtual environment management). If you haven't installed it already please use Poetry's [official docs](https://python-poetry.org/docs/#installation) for instructions. If you find that your installation of Poetry on the AVD is being blocked by group policies, ensure that you have been added to the NL AVD PRD FAFOC group. Contact IT support to explain the issue and let them add you to this group.


1. Clone the repository to your local computer 

*NOTE: AMEND BELOW FOR YOUR PROJECT

```bash
git clone https://dev.azure.com/dttnl-fa-forensic-and-financial-crime/_git/<MY_PROJECT>
cd <MY_PROJECT>
```

2. Switch to a virtual environment [Optional]

Usually, this would be the moment you switch to a virtual environment so you can install project dependencies in an isolated environment. 

You can do this with Poetry or with another preferred virtual environment manager. If you do not want to use a virtual environment, you can continue to the next step.  

With poetry, you can ask it to create the virtual environment within the project repo with this command:
```bash
poetry config virtualenvs.in-project true  
``` 

3. Install project dependencies and create virtual environment if you did not already have one. 

```bash
poetry install
```

4. Install pre-commit hooks

```bash
poetry run pre-commit install
```

You are ready to rock.

5. To using the virtual environment from the terminal, you can use the following command:  

```bash
poetry run python [yourfile].py
```

If you want to use the virtual environment from a notebook, just select the Python executable from the venv as the notebook kernel. 

6. If you want to add new packages to the project, use 

```bash
poetry add [package-name]
```

This will update the poetry.lock file and pyproject.toml files so everyone in the project will use the same version of the package you just added. Make sure to commit and push the changes to these two files if you want to add them to the project.