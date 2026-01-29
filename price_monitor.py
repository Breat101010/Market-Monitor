import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime
import time
import random

# 1. Page Config (Wide Layout & Cyberpunk Title)
st.set_page_config(
    page_title="NEXUS | Market Intelligence",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for "Hacker Mode" styling
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
        color: #00FF41;
    }
    .metric-box {
        background-color: #161B22;
        border: 1px solid #30363D;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,255,65,0.1);
    }
    [data-testid="stMetricValue"] {
        font-family: "Courier New", monospace;
        color: #00FF41 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Control Center
with st.sidebar:
    st.title("👾 SYSTEM CONTROLS")
    st.markdown("---")
    st.success("✅ API CONNECTION: ACTIVE")
    st.info("📡 PROXY NETWORK: ROTATING")
    
    target_site = st.selectbox("Target Domain", ["Amazon", "eBay", "BestBuy", "Alibaba", "Local Stores"])
    refresh_rate = st.slider("Scrape Interval (Seconds)", 5, 300, 60)
    
    st.markdown("### 📝 Live Logs")
    log_placeholder = st.empty()
    st.markdown("---")
    st.caption("NEXUS v2.4.0 | Build 2026.01")

# 4. Mock Data Generator (Simulating Complex Data)
def get_data():
    data = {
        'Product': ['Gaming Laptop X1', 'Wireless Mouse Pro', '4K Monitor 27"', 'Mech Keyboard', 'USB-C Hub', 'GPU RTX 4090', 'Smart Watch Ultra'],
        'My_Price': [1200, 45, 300, 85, 25, 1600, 750],
        'Competitor_Price': [1150, 50, 320, 90, 20, 1550, 780],
        'Competitor': ['Amazon', 'eBay', 'BestBuy', 'Amazon', 'Walmart', 'Newegg', 'Apple'],
        'Demand_Score': [88, 45, 60, 75, 30, 95, 80]
    }
    df = pd.read_json(pd.DataFrame(data).to_json())
    df['Difference'] = df['Competitor_Price'] - df['My_Price']
    df['Status'] = df.apply(lambda x: '⚠️ CRITICAL' if x['Difference'] < 0 else '✅ OPTIMAL', axis=1)
    return df

df = get_data()

# 5. Main Dashboard Layout
st.title("🕸️ NEXUS INTELLIGENCE HUB")
st.markdown(f"**Target:** {target_site} | **Last Sync:** {datetime.datetime.now().strftime('%H:%M:%S')}")

# Top KPI Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total SKUs Tracked", "1,240", "+12")
with col2:
    st.metric("Price Undercuts", "3", "-1", delta_color="inverse")
with col3:
    st.metric("Market Opportunity", "$4,250", "+$150")
with col4:
    st.metric("Avg. Margin", "22%", "+1.5%")

st.markdown("---")

# Tabs for Different Views
tab1, tab2, tab3 = st.tabs(["📊 Live Monitor", "📈 Trend Analysis", "💾 Data Export"])

with tab1:
    # Split into 2 columns: Chart on Left, Data on Right
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader("Price Gap Analysis")
        # Cyberpunk Bar Chart
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df['Product'], y=df['My_Price'],
            name='My Price', marker_color='#00FF41' # Neon Green
        ))
        fig.add_trace(go.Bar(
            x=df['Product'], y=df['Competitor_Price'],
            name='Competitor', marker_color='#FF0055' # Neon Red
        ))
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            barmode='group',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.subheader("🚨 Action Required")
        # Highlighting the bad rows
        bad_rows = df[df['Status'] == '⚠️ CRITICAL'][['Product', 'My_Price', 'Competitor_Price']]
        st.dataframe(bad_rows, hide_index=True)
        
        st.warning("⚠️ 3 Products are priced higher than competitors. Recommendation: Lower prices by 5%.")

with tab2:
    st.subheader("Market Demand Heatmap")
    # A futuristic scatter plot showing Demand vs Price
    fig2 = px.scatter(df, x="My_Price", y="Demand_Score", size="My_Price", color="Status",
                     hover_name="Product", template="plotly_dark",
                     color_discrete_map={'⚠️ CRITICAL': '#FF0055', '✅ OPTIMAL': '#00FF41'})
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.subheader("Raw Data Extraction")
    st.write("Download the full scraping report for offline analysis.")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download CSV Report", data=csv, file_name="nexus_report.csv", mime="text/csv")

# 6. Simulated Live Log in Sidebar (The "Active" feel)
logs = [
    "Connecting to proxy 192.168.x.x...",
    "Bypassing Cloudflare...",
    "Scraping product_id: 4492...",
    "Data parsing complete.",
    "Syncing with database..."
]
with log_placeholder.container():
    for log in logs:
        st.sidebar.text(f"> {log}")
        # No sleep here so it renders instantly for the screenshot, 
        # but in real life, you'd put a time.sleep()