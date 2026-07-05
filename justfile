set shell := ["bash", "-cu"]

default:
    @just --list

fmt *args:
    uv run ruff format . {{args}}
    uv run ruff check --fix . {{args}}

fmt-check:
    uv run ruff format --check saxonche-stubs

lint-only:
    uv run ruff check saxonche-stubs
    uv run mypy saxonche-stubs

lint: fmt-check lint-only

stubtest:
    cd /tmp && PYTHONPATH={{justfile_directory()}} {{justfile_directory()}}/.venv/bin/stubtest saxonche --allowlist {{justfile_directory()}}/stubtest-allowlist.txt

test: lint stubtest
