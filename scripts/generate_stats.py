import pandas as pd
import plotly.express as px

# Load CSV
df = pd.read_csv("data/stats.csv")

# Summary table
summary_table = df.describe().to_html(classes="data-table")

# Example interactive plots
fig1 = px.histogram(df, x="some_column", title="Distribution of some_column")
fig2 = px.line(df, y="another_column", title="Trend of another_column")

# Export as HTML snippets (not full HTML docs)
plot1_html = fig1.to_html(include_plotlyjs="cdn", full_html=False)
plot2_html = fig2.to_html(include_plotlyjs=False, full_html=False)

# Build dashboard HTML
html = f"""
<html>
<head>
  <title>Statistics Dashboard</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 20px; }}
    select {{ font-size: 16px; padding: 5px; margin-bottom: 20px; }}
    .section {{ display: none; }}
    .data-table {{ border-collapse: collapse; width: 80%; }}
    .data-table th, .data-table td {{ border: 1px solid #ccc; padding: 8px; text-align: center; }}
    .data-table th {{ background-color: #f2f2f2; }}
  </style>
  <script>
    function showSection(id) {{
      document.querySelectorAll('.section').forEach(sec => sec.style.display = 'none');
      document.getElementById(id).style.display = 'block';
    }}
  </script>
</head>
<body>
  <h1>Statistics Dashboard</h1>

  <label for="view">Choose view:</label>
  <select id="view" onchange="showSection(this.value)">
    <option value="table">Table</option>
    <option value="plots">Plots</option>
  </select>

  <!-- Table section -->
  <div id="table" class="section" style="display:block;">
    <h2>Summary Table</h2>
    {summary_table}
  </div>

  <!-- Plots section -->
  <div id="plots" class="section">
    <h2>Interactive Plots</h2>
    {plot1_html}
    <br><br>
    {plot2_html}
  </div>

</body>
</html>
"""

# Save to docs/index.html
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Dashboard generated at docs/index.html")
