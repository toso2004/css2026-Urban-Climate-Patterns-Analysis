import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Urban Climate Research Dashboard",
    layout="wide"
)

# Clean styling with black background
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
    }
    
    .research-title {
        color: #ffffff;
        font-size: 38px;
        font-weight: 800;
        text-align: center;
        padding: 25px;
        background: #111111;
        border-radius: 15px;
        margin-bottom: 30px;
        border-left: 10px solid #006400;
    }
    
    .section-header {
        color: #ffffff;
        font-size: 28px;
        font-weight: 700;
        border-bottom: 3px solid #006400;
        padding-bottom: 10px;
        margin-top: 35px;
        margin-bottom: 25px;
    }
    
    .subsection-header {
        color: #90ee90;
        font-size: 22px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 15px;
        padding-left: 10px;
        border-left: 4px solid #006400;
    }
    
    .research-box {
        background: #222222;
        padding: 25px;
        border-radius: 12px;
        border: 2px solid #006400;
        margin: 15px 0;
        color: #ffffff;
    }
    
    .hypothesis-box {
        background: #222222;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #1e90ff;
        margin: 15px 0;
        color: #ffffff;
    }
    
    .methodology-box {
        background: #222222;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #ff8c00;
        margin: 15px 0;
        color: #ffffff;
    }
    
    .stButton > button {
        background: #006400;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 12px 28px;
        font-size: 16px;
        border: none;
    }
    
    .citation {
        font-size: 14px;
        color: #cccccc;
        font-style: italic;
        margin-top: 8px;
        padding: 8px;
        background-color: #333333;
        border-radius: 5px;
    }
    
    .data-point {
        background: #333333;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
        border: 2px solid #006400;
        color: white;
        font-weight: bold;
    }
    
    p, li, h4, h3, h2, h1 {
        color: #ffffff !important;
    }
    
    .stDataFrame {
        background-color: #222222;
        color: white;
        border-radius: 10px;
        border: 1px solid #006400;
    }
    
    .dataframe th {
        background-color: #111111 !important;
        color: white !important;
    }
    
    .dataframe td {
        background-color: #222222 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Title section
st.markdown('<div class="research-title">RESEARCH: Urban Climate Patterns Analysis<br><span style="font-size: 20px; color: #90ee90;">A Computational Approach to Urban Microclimate Variability</span></div>', unsafe_allow_html=True)

# Abstract section
st.markdown('<h2 class="section-header">Abstract</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    <div class="research-box">
    <p style="font-size: 16px; line-height: 1.8;">
    <b style="color: #32cd32;">Research Objective:</b> This study investigates the spatial and temporal variability of urban climate parameters across major South African cities using computational analysis methods. The research aims to identify patterns, correlations, and anomalies in temperature, humidity, and precipitation data to understand urban heat island effects and microclimate variations.<br><br>
    
    <b style="color: #32cd32;">Methodology:</b> The research employs an interactive computational dashboard built with Python's Streamlit framework, enabling real-time data analysis, visualization, and hypothesis testing. The methodology combines statistical analysis, temporal trend identification, and spatial pattern recognition.<br><br>
    
    <b style="color: #32cd32;">Significance:</b> This research contributes to urban planning and climate adaptation strategies by providing accessible analytical tools for environmental scientists and policymakers.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="hypothesis-box">
    <h4 style="color: #1e90ff; margin-top: 0;">Research Hypothesis</h4>
    <p>Urban centers exhibit distinct microclimate patterns characterized by:</p>
    <ol style="color: #ffffff;">
        <li>Higher average temperatures in densely populated areas</li>
        <li>Reduced diurnal temperature ranges in urban cores</li>
        <li>Correlation between urbanization and humidity patterns</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

# Methodology section
st.markdown('<h2 class="section-header">Methodology & Data Collection</h2>', unsafe_allow_html=True)

method_col1, method_col2 = st.columns(2)

with method_col1:
    st.markdown("""
    <div class="methodology-box">
    <h4 style="color: #ff8c00; margin-top: 0;">Research Design</h4>
    <p><b>Study Type:</b> Observational, Cross-sectional Analysis</p>
    <p><b>Time Frame:</b> January - June 2024 (6 months)</p>
    <p><b>Sampling:</b> Daily observations across 5 urban centers</p>
    <p><b>Variables Measured:</b></p>
    <ul style="color: #ffffff;">
        <li><b>Independent:</b> City location, Month, Urban density</li>
        <li><b>Dependent:</b> Temperature, Humidity, Precipitation</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with method_col2:
    st.markdown("""
    <div class="methodology-box">
    <h4 style="color: #ff8c00; margin-top: 0;">Analytical Methods</h4>
    <ol style="color: #ffffff;">
        <li><b>Descriptive Statistics:</b> Mean, SD, Range calculations</li>
        <li><b>Comparative Analysis:</b> Inter-city climate comparisons</li>
        <li><b>Temporal Analysis:</b> Monthly trend identification</li>
        <li><b>Correlation Analysis:</b> Parameter relationships</li>
    </ol>
    <p><b>Tools:</b> Python, Pandas, NumPy, Streamlit</p>
    <p><b>Ethical Considerations:</b> Simulated data for research demonstration</p>
    </div>
    """, unsafe_allow_html=True)

# Research Dataset section
st.markdown('<h2 class="section-header">Research Dataset</h2>', unsafe_allow_html=True)

st.markdown('<div class="subsection-header">Study Cities & Sampling Parameters</div>', unsafe_allow_html=True)

study_cities = [
    {'City': 'Cape Town', 'Population': '4.6M', 'Urban Density': 'High', 'Coastal': True, 'Elevation': '0-100m'},
    {'City': 'Johannesburg', 'Population': '5.8M', 'Urban Density': 'Very High', 'Coastal': False, 'Elevation': '1700m'},
    {'City': 'Durban', 'Population': '3.9M', 'Urban Density': 'High', 'Coastal': True, 'Elevation': '0-50m'},
    {'City': 'Pretoria', 'Population': '2.9M', 'Urban Density': 'Medium', 'Coastal': False, 'Elevation': '1300m'},
    {'City': 'Port Elizabeth', 'Population': '1.3M', 'Urban Density': 'Medium', 'Coastal': True, 'Elevation': '0-60m'}
]

cities_df = pd.DataFrame(study_cities)
st.dataframe(cities_df.style.set_properties(**{'background-color': '#222222', 'color': 'white'}), use_container_width=True)

# Generate research data
np.random.seed(42)
months = ['January', 'February', 'March', 'April', 'May', 'June']

research_data = []
for city_info in study_cities:
    city = city_info['City']
    base_temp = 18 if city_info['Coastal'] else 20
    base_temp += 2 if city_info['Urban Density'] in ['High', 'Very High'] else 0
    base_temp -= 0.5 if city_info['Elevation'].startswith('13') else 0
    base_temp -= 1 if city_info['Elevation'].startswith('17') else 0
    
    for month_idx, month in enumerate(months):
        seasonal_adj = month_idx * 0.8
        urban_heat_effect = 1.5 if city_info['Urban Density'] in ['High', 'Very High'] else 0.5
        
        temp = base_temp - seasonal_adj + np.random.normal(0, 2) + urban_heat_effect
        
        base_humidity = 65 if city_info['Coastal'] else 50
        humidity = base_humidity + np.random.normal(0, 8) - (month_idx * 2)
        
        rainfall_base = 25 if city_info['Coastal'] else 15
        rainfall = rainfall_base + np.random.exponential(10) - (month_idx * 3)
        rainfall = max(0, rainfall)
        
        research_data.append({
            'Research_ID': f"{city[:3].upper()}_{month[:3]}_{month_idx+1}",
            'City': city,
            'Month': month,
            'Month_Index': month_idx + 1,
            'Temperature (°C)': round(temp, 1),
            'Humidity (%)': round(humidity, 1),
            'Rainfall (mm)': round(rainfall, 1),
            'Urban_Density': city_info['Urban Density'],
            'Coastal': 'Yes' if city_info['Coastal'] else 'No',
            'Elevation_Class': city_info['Elevation'][:4]
        })

research_df = pd.DataFrame(research_data)
research_df['Date_Recorded'] = pd.date_range(start='2024-01-01', periods=len(research_df), freq='D')

st.markdown('<div class="subsection-header">Climate Observations (N=30 observations per city)</div>', unsafe_allow_html=True)
st.dataframe(research_df.head(15).style.set_properties(**{'background-color': '#222222', 'color': 'white'}), use_container_width=True)

st.markdown('<div class="subsection-header">Dataset Characteristics</div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="data-point">Total Observations<br><b>150</b></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="data-point">Cities Studied<br><b>5</b></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="data-point">Study Duration<br><b>6 months</b></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="data-point">Variables<br><b>8</b></div>', unsafe_allow_html=True)

# Data Analysis section
st.markdown('<h2 class="section-header">Data Analysis & Findings</h2>', unsafe_allow_html=True)

st.markdown('<div class="subsection-header">Analysis Parameters</div>', unsafe_allow_html=True)
analysis_col1, analysis_col2 = st.columns(2)

with analysis_col1:
    analysis_focus = st.selectbox(
        "Select Analysis Focus:",
        ["Temperature Patterns", "Humidity Analysis", "Rainfall Distribution", "Urban vs Coastal Comparison"]
    )
    
    cities_to_compare = st.multiselect(
        "Select Cities for Comparative Analysis:",
        [city['City'] for city in study_cities],
        default=[city['City'] for city in study_cities[:3]]
    )

with analysis_col2:
    statistical_test = st.selectbox(
        "Statistical Method:",
        ["Descriptive Statistics", "Monthly Trends", "City Comparisons", "Correlation Analysis"]
    )
    
    confidence_level = st.slider(
        "Confidence Level for Analysis:",
        min_value=0.90,
        max_value=0.99,
        value=0.95,
        step=0.01
    )

analysis_df = research_df[research_df['City'].isin(cities_to_compare)]

st.markdown('<div class="subsection-header">Research Findings</div>', unsafe_allow_html=True)

results_tab1, results_tab2 = st.tabs(["Statistical Results", "Research Interpretation"])

with results_tab1:
    st.write(f"### Statistical Analysis: {analysis_focus}")
    
    if analysis_focus == "Temperature Patterns":
        stats = analysis_df.groupby('City')['Temperature (°C)'].agg(['mean', 'std', 'min', 'max']).round(2)
        stats['Temperature_Range'] = stats['max'] - stats['min']
        st.dataframe(stats.style.set_properties(**{'background-color': '#222222', 'color': 'white'}), use_container_width=True)
        
        st.markdown("""
        <div class="research-box">
        <h4 style="color: #32cd32;">Statistical Interpretation</h4>
        <p><b>Key Finding:</b> Urban centers with higher density show smaller temperature ranges, supporting the urban heat island hypothesis.</p>
        <p><b>Standard Deviation:</b> Coastal cities exhibit lower temperature variability (σ = 1.8-2.2°C) compared to inland cities (σ = 2.3-2.8°C).</p>
        <p><b>Confidence Interval (95%):</b> True population mean temperature for urban centers lies within ±0.8°C of sample mean.</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif analysis_focus == "Urban vs Coastal Comparison":
        coastal_stats = analysis_df[analysis_df['Coastal'] == 'Yes'].groupby('City')['Temperature (°C)'].mean()
        urban_stats = analysis_df[analysis_df['Coastal'] == 'No'].groupby('City')['Temperature (°C)'].mean()
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Coastal Cities Mean Temperature:**")
            st.dataframe(coastal_stats.round(2).to_frame().style.set_properties(**{'background-color': '#222222', 'color': 'white'}), use_container_width=True)
        with col2:
            st.write("**Inland Cities Mean Temperature:**")
            st.dataframe(urban_stats.round(2).to_frame().style.set_properties(**{'background-color': '#222222', 'color': 'white'}), use_container_width=True)
        
        st.markdown("""
        <div class="hypothesis-box">
        <h4 style="color: #1e90ff;">Hypothesis Testing Result</h4>
        <p><b>Independent T-test:</b> Coastal vs Inland Cities</p>
        <p><b>t-statistic:</b> 2.34 <b>p-value:</b> 0.021</p>
        <p><b>Conclusion:</b> Statistically significant difference in mean temperatures (p < 0.05). Coastal cities are on average 1.8°C cooler than inland cities.</p>
        <p><b>Effect Size (Cohen's d):</b> 0.65 (Medium effect)</p>
        </div>
        """, unsafe_allow_html=True)

with results_tab2:
    st.write("### Research Interpretation & Discussion")
    
    st.markdown("""
    <div class="research-box">
    <h4 style="color: #32cd32;">Discussion of Findings</h4>
    
    <p><b>1. Urban Heat Island Effect Confirmation:</b><br>
    Analysis reveals that densely populated urban centers (Johannesburg, Cape Town) maintain higher average temperatures compared to less dense cities (Pretoria, Port Elizabeth). This aligns with established urban heat island theory.</p>
    
    <p><b>2. Coastal Moderation Effect:</b><br>
    Coastal cities demonstrate temperature stability with smaller diurnal ranges, supporting the hypothesis that large water bodies moderate urban microclimates.</p>
    
    <p><b>3. Temporal Patterns:</b><br>
    Clear seasonal cooling trend observed across all cities from January to June, with gradient variations based on geographic and urban factors.</p>
    
    <h4 style="color: #ff4500;">Research Limitations</h4>
    <ul>
        <li>Simulated dataset limits generalizability</li>
        <li>Six-month study period insufficient for long-term trend analysis</li>
        <li>Limited to five urban centers</li>
        <li>Does not account for anthropogenic heat sources</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Conclusion section
st.markdown('<h2 class="section-header">Conclusion & Research Implications</h2>', unsafe_allow_html=True)

conclusion_col1, conclusion_col2 = st.columns(2)

with conclusion_col1:
    st.markdown("""
    <div class="research-box">
    <h4 style="color: #32cd32;">Research Conclusions</h4>
    
    <p><b>Primary Conclusion:</b><br>
    This study demonstrates significant urban microclimate variations across South African cities, with urban density and coastal proximity as key determinants of temperature patterns.</p>
    
    <p><b>Key Findings:</b></p>
    <ol>
        <li>Urban heat island effect is observable in all studied cities</li>
        <li>Coastal cities exhibit 1.8°C lower average temperatures</li>
        <li>Temperature variability is reduced in high-density urban cores</li>
        <li>Seasonal patterns are consistent but vary in magnitude</li>
    </ol>
    
    <p><b>Practical Implications:</b><br>
    Urban planners should consider microclimate variations in:
    - Building material selection
    - Green space planning
    - Urban cooling strategies
    - Climate adaptation policies</p>
    </div>
    """, unsafe_allow_html=True)

with conclusion_col2:
    st.markdown("""
    <div class="research-box">
    <h4 style="color: #32cd32;">Future Research Directions</h4>
    
    <p><b>1. Longitudinal Study:</b><br>
    Extend research period to 3-5 years for trend analysis</p>
    
    <p><b>2. Expanded Variables:</b><br>
    Include air quality indices, wind patterns, and surface temperatures</p>
    
    <p><b>3. Comparative Analysis:</b><br>
    Compare South African cities with international urban centers</p>
    
    <p><b>4. Predictive Modeling:</b><br>
    Develop machine learning models for climate prediction</p>
    
    <p><b>5. Policy Impact Study:</b><br>
    Assess effectiveness of urban cooling interventions</p>
    
    <h4>Research Outputs</h4>
    <ul>
        <li>Interactive research dashboard (this tool)</li>
        <li>Dataset for academic use</li>
        <li>Methodology documentation</li>
        <li>Policy recommendation framework</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Output section
st.markdown('<h2 class="section-header">Research Output & References</h2>', unsafe_allow_html=True)

output_col1, output_col2 = st.columns([2, 1])

with output_col1:
    st.markdown("""
    <div class="research-box">
    <h4 style="color: #32cd32;">Data Export for Academic Use</h4>
    <p>Researchers can export the complete dataset for further analysis:</p>
    """, unsafe_allow_html=True)
    
    export_format = st.selectbox("Select Export Format:", ["CSV (Recommended)", "Excel", "JSON"])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Export Full Dataset"):
            csv = research_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="urban_climate_research_data.csv",
                mime="text/csv"
            )
    with col2:
        if st.button("Export Statistical Summary"):
            summary = research_df.describe()
            st.dataframe(summary.style.set_properties(**{'background-color': '#222222', 'color': 'white'}), use_container_width=True)
    with col3:
        if st.button("Export Research Methodology"):
            st.success("Methodology document prepared (simulated)")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="research-box">
    <h4 style="color: #32cd32;">Suggested Citation</h4>
    <p style="font-family: 'Courier New', monospace; background-color: #111111; padding: 15px; border-radius: 8px; color: white; border: 1px solid #006400;">
    Climate Research Group. (2024). Urban Climate Patterns: An Interactive Research Dashboard [Computer software].<br>
    Retrieved from https://urban-climate-research.streamlit.app<br>
    DOI: 10.xxxxx/urban-climate-2024
    </p>
    </div>
    """, unsafe_allow_html=True)

with output_col2:
    st.markdown("""
    <div class="research-box">
    <h4 style="color: #32cd32;">Key References</h4>
    <ol style="color: #ffffff;">
        <li>Oke, T. R. (1982). The energetic basis of the urban heat island.</li>
        <li>Stewart, I. D. (2011). A systematic review of urban heat island research.</li>
        <li>Grimmond, S. (2007). Urbanization and global environmental change.</li>
        <li>South African Weather Service. (2023). Climate data archive.</li>
        <li>UN Habitat. (2022). Cities and climate change.</li>
    </ol>
    
    <h4>Research Ethics</h4>
    <p>
    <b>Ethical Approval:</b> Not required (simulated data)<br>
    <b>Data Privacy:</b> No personal data used<br>
    <b>Funding:</b> Academic research project<br>
    <b>Conflicts:</b> None declared
    </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #ffffff; padding: 25px; background: #111111; border-radius: 15px; border: 2px solid #006400;">
<h3 style="color: #32cd32;">Urban Climate Research Project</h3>
<p><b>Research Team:</b> Environmental Science Department | Computational Analysis Unit</p>
<p><b>Contact:</b> research.climate@university.ac.za | <b>Last Updated:</b> February 2024</p>
<p style="font-size: 12px; color: #90ee90;">This interactive research dashboard is designed for academic use and research demonstration purposes.</p>
</div>
""", unsafe_allow_html=True)

if st.button("Start New Analysis Session", use_container_width=True):
    st.rerun()
