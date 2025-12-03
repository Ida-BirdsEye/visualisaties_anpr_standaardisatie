import yaml
import csv

def define_env(env):
    @env.macro
    def render_yaml_table(path):
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        if not data:
            return f"> ⚠ Geen datavelden gevonden in `{path}` (YAML leeg of ongeldig)."

        rows = data.get("columns", [])
        if not rows:
            return f"> ⚠ YAML in `{path}` bevat geen `columns`-sleutel."

        md = "| NL (camelCase) | EN (snake_case) | Type | Omschrijving |\n"
        md += "|---|---|---|---|\n"

        for c in rows:
            md += f"| {c['name_nl']} | {c['name_en']} | {c.get('type', '')} | {c.get('description', '')} |\n"

        return md

    @env.macro
    def render_csv_table(path):
        """
        Lees een CSV en zet 'm om naar een Markdown-tabel,
        zonder gebruik van pandas (robuster, geen EmptyDataError).
        """
        rows = []
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                # sla volledig lege regels over
                if not row or all(cell.strip() == "" for cell in row):
                    continue
                rows.append(row)

        if not rows:
            return f"> ⚠ Geen data gevonden in `{path}`."

        header = rows[0]
        data_rows = rows[1:]

        # Bouw markdown-tabel
        md = "|" + "|".join(header) + "|\n"
        md += "|" + "|".join(["---"] * len(header)) + "|\n"

        for r in data_rows:
            md += "|" + "|".join(str(cell) for cell in r) + "|\n"

        return md


