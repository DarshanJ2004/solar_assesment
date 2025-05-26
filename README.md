AI-Powered Rooftop Solar Analysis Tool
Overview
This project provides an intelligent system that analyzes satellite imagery of rooftops to assess solar panel installation potential. It generates detailed solar potential assessments, installation recommendations, and ROI estimates, catering to homeowners and solar professionals alike.

The system integrates AI-powered language models via the OpenRouter API with image processing techniques to deliver accurate and actionable insights.

Features
Satellite Image Analysis: Extract usable rooftop area suitable for solar panel installation.
Solar Potential Estimation: Calculate estimated solar energy output based on rooftop characteristics.
Installation Recommendations: Provide guidance on panel types, mounting, and permits.
ROI Calculation: Estimate costs, incentives, and payback periods.
User-Friendly Interface: Built with Streamlit for easy image upload and result visualization.
API Integration: Uses OpenRouter API for natural language report generation.
Project Structure
Setup Instructions
1. Clone the repository
git clone https://github.com/DarshanJ2004/solar_assesment.git
cd rooftop-solar-analysis


### 2 Create and activate a virtual environment

# On Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

### 3.Install dependencies
pip install -r requirements.txt


### 4. Put Your API Key in llm_engine.py

### 5 Run the application

streamlit run app.py
