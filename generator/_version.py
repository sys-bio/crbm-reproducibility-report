from pathlib import Path
import re


def _read_project_version() -> str:
	pyproject_path = Path(__file__).resolve().parents[1] / "pyproject.toml"

	if not pyproject_path.exists():
		return "0.0.0"

	try:
		import tomllib  # Python 3.11+

		with pyproject_path.open("rb") as f:
			data = tomllib.load(f)

		return data.get("project", {}).get("version", "0.0.0")
	except Exception:
		# Fallback for older Python or unexpected TOML parse issues.
		text = pyproject_path.read_text(encoding="utf-8")

		in_project_section = False
		for line in text.splitlines():
			stripped = line.strip()

			if stripped.startswith("[") and stripped.endswith("]"):
				in_project_section = stripped == "[project]"
				continue

			if in_project_section:
				match = re.match(r'^version\s*=\s*["\']([^"\']+)["\']\s*$', stripped)
				if match:
					return match.group(1)

		return "0.0.0"


__version__ = _read_project_version()
