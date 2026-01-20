
from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Data Science Report: Trader Behavior & Market Sentiment', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(220, 230, 241)
        self.cell(0, 8, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 5, body)
        self.ln()

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 11)

report_text = """
1. Objective
Explore the relationship between trader performance (PnL, Win Rate, Risk) and market sentiment (Fear vs Greed Index) to uncover hidden patterns and strategic insights.

2. Methodology
- Data Integration: Merged HFT-style trader data with daily Fear & Greed Index (Forward-fill alignment).
- Advanced Metrics: Analyzed PnL Volatility (Risk) and Position Sizing alongside standard PnL.
- Proxies: Used 'Size USD' as a proxy for conviction/leverage as the 'Leverage' column was missing.

3. Key Insights & "Hidden Patterns"

A. Risk & Volatility Profile (The "Fat Tail" Risk)
Violin plot analysis reveals a "Fat Tail" risk in Extreme Greed. While average PnL is highest in Extreme Greed ($67.89), the volatility (StdDev) is also significant. The trader takes larger positions and accepts wider PnL swings during euphoric markets.

B. The "Safety" of Fear
Contrarian efficiency is high. During "Fear" states, the win rate remains robust (42%) with a healthy average PnL ($54.29). This suggests the trader is effective at buying dips or shorting panic without over-leveraging, as evidenced by tighter PnL distributions (smaller violin shape).

C. Position Sizing Signal
Average position size increases linearly with Greed.
- Neutral/Fear: Smaller positions (Caution).
- Extreme Greed: Largest positions (High Conviction).
 This alignment of Size with Sentiment is a key driver of the cumulative PnL outperformance in bull runs.

4. Performance Summary by Sentiment
- Extreme Greed: $67.89 Avg PnL | High Risk | High Conviction
- Fear: $54.29 Avg PnL | Moderate Risk | Contrarian Edge
- Greed: $42.74 Avg PnL
- Extreme Fear: $34.54 Avg PnL | Low Win Rate (37%) - WEAKNESS IDENTIFIED

5. Recommendations
1. Optimizing Extreme Fear: The lowest win rate occurs here. Reduce position size by 20% when Sentiment < 25 to preserve capital.
2. Leverage the "Greed" Edge: The strategy thrives in momentum. Consider trailing stops rather than fixed targets in Extreme Greed to capture "fat tail" upside.
"""

pdf.multi_cell(0, 5, report_text)

# Add images
output_dir = "ds_sohel/outputs"
# Order matters for narrative flow
images = [
    ("cumulative_pnl.png", "Cumulative Performance Over Time"),
    ("pnl_distribution_violin.png", "Risk Analysis: PnL Distribution by Sentiment"), 
    ("position_sizing.png", "Behavior Analysis: Position Sizing by Sentiment"),
    ("risk_volatility.png", "Volatility Profile (Standard Deviation)")
]

for img_name, title in images:
    img_path = os.path.join(output_dir, img_name)
    if os.path.exists(img_path):
        pdf.add_page()
        pdf.chapter_title(f"Visualization: {title}")
        pdf.image(img_path, w=170)

pdf.output("ds_sohel/ds_report.pdf")
print("PDF Report generated.")
