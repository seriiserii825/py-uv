import os
import shutil
from pathlib import Path

from classes.Command import Command
from classes.Print import Print


class Uv:
    @staticmethod
    def start():
        """
        Create .venv directory and install uv package.
        """
        if Path(".venv").exists():
            print("Virtual environment already exists.")
            return
        else:
            try:
                Command.run("uv venv .venv")
                print("Virtual environment created successfully.")
            except Exception as e:
                print(f"Error creating virtual environment: {e}")
                return

    @staticmethod
    def create_pyproject_toml():
        file_content = """
            [project]
            name = "my_project"
            version = "0.1.0"
            description = ""

            [tool.ruff]
            line-length = 88
            exclude = [
                "migrations",
                "tests",
                "docs",
                "build",
                "dist",
                "venv",
                ".venv",
                ".git",
                "__pycache__",
            ]
            fix = true
            unsafe-fixes = true
            target-version = "py312"  # <- specify Python 3.12 explicitly here

            [tool.ruff.lint]
            select = [
                "F401",  # Unused import
                "F403",  # Wildcard import
                "F405",  # Name may be undefined, or defined from star imports
                "F841",  # Local variable is assigned to but never used
                "E501",  # Line too long
                "I",     # Import sorting (isort-compatible)
            ]
        """
        with open("pyproject.toml", "w") as file:
            file.write(file_content.strip())

    @staticmethod
    def pre_commit_hook():
        if not os.path.exists(".git/hooks/pre-commit"):
            Print.error("No pre-commit hook found. Creating one...")
            os.makedirs(".git/hooks", exist_ok=True)
            os.system("touch .git/hooks/pre-commit")

        hook_path = Path(".git/hooks/pre-commit")

        hook_content = """
            #!/usr/bin/env bash
            echo "🔍 Running Ruff pre‑commit hook…"

            if ! command -v ruff >/dev/null 2>&1; then
              echo "❌ Ruff not found. Install it with: sudo pacman -S ruff"
              exit 1
            fi

            ruff check . --fix || { echo "❌ Commit aborted (Ruff check)"; exit 1; }
            ruff format .      || { echo "❌ Commit aborted (Ruff format)"; exit 1; }

            echo "✅ Ruff passed. Proceeding with commit."
            exit 0
        """
        with open(hook_path, "w") as hook_file:
            hook_file.write(hook_content.strip())
        hook_path.chmod(0o755)
        os.system(f"bat --color=always {hook_path}")

    @staticmethod
    def migrate_from_requirements():
        if not Path("requirements.txt").exists():
            Print.error("No requirements.txt file found.")
            return
        try:
            Command.run("uv add -r requirements.txt")
            requirements_path = Path("requirements.txt")
            venv_path = Path("venv")
            Path.unlink(requirements_path)
            if venv_path.exists():
                shutil.rmtree(venv_path)
            Print.success("requirements.txt migrated to uv.")
        except Exception as e:
            Print.error(f"Error migrating requirements.txt: {e}")
            return
