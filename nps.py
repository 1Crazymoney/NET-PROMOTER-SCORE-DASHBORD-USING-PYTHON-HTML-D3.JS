import pandas as pd
import json

# Load the Excel file
file_path = 'C://Users//Administration//Downloads//Post Evaluation July.xlsx'
xls = pd.ExcelFile(file_path)

# Load the "July 2024" sheet
july_df = pd.read_excel(xls, sheet_name='July 2024')

# Extract the relevant column for NPS calculation
recommendation_scores = july_df["Would you recommend IRES-Kenya to colleagues for Training and Development? Yes/No Why"]

# Calculate the NPS
promoters = recommendation_scores[recommendation_scores >= 9].count()
passives = recommendation_scores[(recommendation_scores >= 7) & (recommendation_scores <= 8)].count()
detractors = recommendation_scores[recommendation_scores <= 6].count()

# Convert counts to native Python int
promoters = int(promoters)
passives = int(passives)
detractors = int(detractors)

# Prepare data for export
data = {
    'labels': ['Promoters', 'Passives', 'Detractors'],
    'counts': [promoters, passives, detractors],
    'colors': ['#4CAF50', '#FFC107', '#F44336']
}

# Save to JSON file
with open('nps_data.json', 'w') as f:
    json.dump(data, f, indent=4)  # Added indent for better readability

