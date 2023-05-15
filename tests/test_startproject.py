from pathlib import Path

from typer.testing import CliRunner

from flask_management.main import app

runner = CliRunner()

CREATED_SUCCESSFULLY = "Flask project created successfully! 🎉\n"
ALREADY_EXISTS = "Folder 'joe' already exists. 😞\n"


def test_startproject_default(tmp_path: Path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["startproject", "joe"])
        assert result.output == CREATED_SUCCESSFULLY
        assert result.exit_code == 0


def test_startproject_already_exists(tmp_path: Path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(app, ["startproject", "joe"])
        assert result.output == CREATED_SUCCESSFULLY
        assert result.exit_code == 0

        result = runner.invoke(app, ["startproject", "joe"])
        assert result.output == ALREADY_EXISTS
        assert result.exit_code == 0
