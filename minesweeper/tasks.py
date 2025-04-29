from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py")


@task
def test(ctx):
    ctx.run("pytest src")


@task
def lint(ctx):
    ctx.run("pylint src")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")


@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")


@task
def format_check(ctx):
    ctx.run("autopep8 --recursive --exit-code --diff src")

@task
def build(ctx):
    ctx.run("python3 src/initialize_database.py")
