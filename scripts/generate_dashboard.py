import pandas as pd
import plotly.express as px

# === Load CSV ===
df = pd.read_csv("data/events.csv")

# === Summary table ===
summary_table = df.describe(include="all").to_html(classes="data-table", justify="center")

# === Example Plot 1: Histogram of Δt ===
fig1 = px.histogram(df, x="DeltaT_hours", nbins=20,
                    title="Reaction Time Distribution (Δt in hours)")

# === Example Plot 2: Timeline of events ===
fig2 = px.scatter(df, x="T0_UTC", y="DeltaT_hours", color="Instrument",
                  hover_data=["GRB_ID", "Status"],
                  title="Reaction Times vs T0")

# === Example Plot 3: Sky map (RA/Dec) ===
fig3 = px.scatter(df, x="RA_deg", y="Dec_deg", color="Status",
                  hover_data=["GRB_ID", "Instrument"],
                  title="Sky Distribution of Events")

# Export Plotly figs as HTML snippets
plot1_html = fig1.to_html(full_html=False, include_plotlyjs="cdn")
plot2_html = fig2.to_html(full_html=False, include_plotlyjs=False)
plot3_html = fig3.to_html(full_html=False, include_plotlyjs=False)

# === Dashboard HTML with dropdown ===
html = f"""
<html>
<head>
  <title>H.E.S.S. GRB Follow-up Dashboard</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 20px; }}
    select {{ font-size: 16px; padding: 5px; margin-bottom: 20px; }}
    .section {{ display: none; }}
    .data-table {{ border-collapse: collapse; margin-top: 20px; }}
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
  <h1>H.E.S.S. GRB Follow-up Dashboard</h1>

  <label for="view">Choose view:</label>
  <select id="view" onchange="showSection(this.value)">
    <option value="table">Summary Table</option>
    <option value="histogram">Δt Histogram</option>
    <option value="timeline">Timeline</option>
    <option value="skymap">Sky Map</option>
  </select>

  <!-- Table Section -->
  <div id="table" class="section" style="display:block;">
    <h2>Summary Table</h2>
    {summary_table}
  </div>

  <!-- Histogram Section -->
  <div id="histogram" class="section">
    <h2>Reaction Time Distribution</h2>
    {plot1_html}
  </div>

  <!-- Timeline Section -->
  <div id="timeline" class="section">
    <h2>Reaction Times vs T0</h2>
    {plot2_html}
  </div>

  <!-- Sky Map Section -->
  <div id="skymap" class="section">
    <h2>Sky Distribution</h2>
    {plot3_html}
  </div>

</body>
</html>
"""

# Save dashboard
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Dashboard generated at docs/index.html")
