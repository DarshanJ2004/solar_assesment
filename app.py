import streamlit as st
from PIL import Image
from image_utils import preprocess_image, estimate_usable_area
from solar_calculator import calculate_solar_output, estimate_roi, recommend_system
from llm_engine import generate_report

st.set_page_config(page_title="Rooftop Solar Analyzer", layout="wide")
st.title("☀️ AI-Powered Rooftop Solar Potential Analyzer")

uploaded_file = st.file_uploader("Upload a rooftop image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    edge_img, rgb_img = preprocess_image(image)
    st.image(edge_img, caption="Edge Detection", use_column_width=True)

    usable_ratio = estimate_usable_area(edge_img)
    roof_area = st.slider("Estimate Roof Area (m²)", 20, 200, 100)
    usable_area = roof_area * usable_ratio
    st.metric("Usable Rooftop Area (m²)", round(usable_area, 2))

    panel_count, system_kw = recommend_system(usable_area)
    yearly_output = calculate_solar_output(usable_area)
    savings = yearly_output * 0.15  # $0.15/kWh
    cost = panel_count * 700  # $700/panel approx
    payback, roi = estimate_roi(cost, savings)

    st.subheader("🔧 System Recommendation")
    st.write(f"• Panels: {panel_count}")
    st.write(f"• Estimated System Size: {system_kw} kW")
    st.write(f"• Estimated Annual Output: {yearly_output} kWh")
    st.write(f"• Estimated Cost: ${cost}")
    st.write(f"• Payback Period: {payback} years")
    st.write(f"• ROI over 25 years: {roi}%")

    if st.button("📋 Generate Full AI Report"):
        prompt = f"""
        A user has a roof of {roof_area} m², with {round(usable_area,2)} m² usable.
        They plan to install {panel_count} panels, totaling {system_kw} kW.
        The expected annual generation is {yearly_output} kWh.
        Estimate financials, installation considerations, and provide a professional recommendation.
        """
        report = generate_report(prompt)
        st.subheader("📑 AI-Generated Report")
        st.markdown(report)
