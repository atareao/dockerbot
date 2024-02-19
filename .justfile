user    := "atareao"
name    := `basename ${PWD}`
version := `git tag -l | tail -n1`

default:
    @just --list

run:
    @poetry run python src/main.py

test:
    @poetry run pytest
