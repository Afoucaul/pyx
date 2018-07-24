# Pyx, the task-oriented project manager

This project was primarily inspired by [mix](https://hexdocs.pm/mix/Mix.html), project management tool for Elixir projects.
It provides generic tasks for creating, testing, running... Python projects, available as command-line tools.


## Structure of a Pyx project

You can create a new project with the following command:

```bash
pyx new my_project
```

This will create the following directory:

```txt
my_project/
├── .gitignore
├── main.py
├── my_project
│   └── __init__.py
├── Pipfile
├── .pyx
│   ├── project.py
│   └── tasks
├── README.md
├── setup.py
└── test
    └── test_my_project.py
```

Let's have a look at this.
Your code goes in the directory named after your project; here it's `./my_project/`.
The reason behind this is that `pyx` will help you build your project as a package.

The entry point of a Pyx project is `main.py`.
It will be run when calling `pyx run` at the root of the project.
This task will actually activate the corresponding `pipenv` environment, and run the project there.

The `test` directory is where unit tests files should be placed.
There's already one provided, `./test/test_my_project.py`.
The unit tests are run with `pyx test`, which will call the `unittest` module.

The project also contains a `README.md` and a `.gitignore` files, for git projects.
It contains a `setup.py` for distributing your project to PyPI, which can be done through the `pyx release` task.
The credentials and repository for distribution are stored in `./.pyx/project.py'; although you don't need to write these: if Pyx cannot find them, you'll be prompted to type them.
