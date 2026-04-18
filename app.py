import streamlit as st
import pickle
import numpy as np

# ==================== Page Config & Assets ==================== #
st.set_page_config(page_title="Laptop Price Engine", page_icon="💻", layout="wide")

@st.cache_resource
def load_models():
    pipe = pickle.load(open('pipe.pkl','rb'))
    df = pickle.load(open('df.pkl','rb'))
    return pipe, df

pipe, df = load_models()

# ==================== Global Cyber CSS ==================== #
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Background Configuration: Obsidian with Neon Skybox */
    .stApp {
        background: linear-gradient(135deg, #090b10 0%, #151024 50%, #06141a 100%);
        color: #f1f5f9;
        overflow-x: hidden;
    }

    /* Ambient Animated Orbs */
    .blob1 {
        position: fixed;
        top: -15%; left: -10%;
        width: 50vw; height: 50vw;
        background: radial-gradient(circle, rgba(176, 38, 255, 0.15) 0%, transparent 70%);
        border-radius: 50%;
        z-index: -10;
        pointer-events: none;
        animation: float1 22s infinite ease-in-out alternate;
    }
    .blob2 {
        position: fixed;
        bottom: -20%; right: -10%;
        width: 60vw; height: 60vw;
        background: radial-gradient(circle, rgba(0, 212, 255, 0.12) 0%, transparent 60%);
        border-radius: 50%;
        z-index: -10;
        pointer-events: none;
        animation: float2 28s infinite ease-in-out alternate;
    }
    
    @keyframes float1 { 0% { transform: translate(0,0) scale(1); } 100% { transform: translate(15%, 20%) scale(1.15); } }
    @keyframes float2 { 0% { transform: translate(0,0) scale(1); } 100% { transform: translate(-10%, -15%) scale(1.1); } }

    /* Footer */
    .footer {
        position: fixed;
        bottom: 10px;
        left: 0;
        right: 0;
        text-align: center;
        color: #FFFFFF;
        font-size: 0.85rem;
        font-weight: 300;
        letter-spacing: 1px;
        z-index: 10;
    }
    
    /* Remove padding to make it wide and edgy */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        max-width: 1300px;
    }
    
    /* Main Glowing Title */
    .cyber-title {
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #b026ff 0%, #00d4ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: -10px;
        text-shadow: 0px 4px 50px rgba(176, 38, 255, 0.4);
    }
    
    .cyber-subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        letter-spacing: 4px;
        margin-bottom: 2rem;
        font-weight: 300;
        text-transform: uppercase;
    }

    /* Style the inputs to look like glass terminal modules */
    .stSelectbox>div>div>div, .stNumberInput>div>div>input {
        background-color: rgba(20, 20, 30, 0.6) !important;
        border: 1px solid rgba(176, 38, 255, 0.3) !important;
        color: #e2e8f0 !important;
        border-radius: 8px;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .stSelectbox>div>div>div:hover, .stNumberInput>div>div>input:hover {
        border-color: #00d4ff !important;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.2) inset !important;
    }
    
    /* Fancy Labels */
    .stSelectbox label, .stNumberInput label, .stSlider label {
        color: #cbd5e1 !important;
        font-weight: 500 !important;
        letter-spacing: 0.5px;
    }

    /* Predict Button Setup */
    .stButton>button {
        background: linear-gradient(90deg, #b026ff 0%, #00d4ff 100%);
        color: #ffffff;
        font-weight: 800;
        font-size: 1.3rem;
        border: none;
        border-radius: 12px;
        padding: 1rem;
        width: 100%;
        margin-top: 3rem;
        margin-bottom: 2rem;
        text-transform: uppercase;
        letter-spacing: 3px;
        transition: all 0.4s ease;
        box-shadow: 0 10px 30px rgba(176, 38, 255, 0.4);
    }
    
    .stButton>button:hover, .stButton>button:active, .stButton>button:focus {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0, 212, 255, 0.6);
        color: #ffffff !important;
        border: none !important;
        outline: none !important;
    }
    
    .stMarkdown p { color: #ffffff !important; }
    
    /* Output Animated Price Card */
    .price-card {
        background: rgba(15, 15, 20, 0.8);
        border: 1px solid rgba(0, 212, 255, 0.5);
        border-radius: 16px;
        padding: 3rem;
        text-align: center;
        max-width: 800px;
        margin: 0 auto;
        box-shadow: 0 15px 50px rgba(0, 212, 255, 0.15), inset 0 0 40px rgba(176, 38, 255, 0.1);
        backdrop-filter: blur(15px);
        animation: popUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    
    .price-label {
        font-size: 1.2rem;
        color: #94a3b8;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 5px;
    }
    
    .price-value {
        font-size: 5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ffffff 0%, #e2e8f0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -2px;
        margin: 10px 0;
        text-shadow: 0 0 30px rgba(255, 255, 255, 0.2);
    }
    
    .ai-badge {
        display: inline-block;
        background: rgba(0, 212, 255, 0.1);
        border: 1px solid #00d4ff;
        color: #00d4ff;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-family: monospace;
        letter-spacing: 1px;
        margin-top: 15px;
    }
    
    @keyframes popUp {
        0% { opacity: 0; transform: scale(0.95) translateY(20px); }
        100% { opacity: 1; transform: scale(1) translateY(0); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown("<div class='blob1'></div><div class='blob2'></div>", unsafe_allow_html=True)

# ==================== Header ==================== #
st.markdown('<h1 class="cyber-title">PREDATOR PREDICTOR</h1>', unsafe_allow_html=True)
st.markdown('<p class="cyber-subtitle">Laptop Price Estimation Engine</p>', unsafe_allow_html=True)

# ==================== Core UI Framework ==================== #
# We split the 12 inputs sequentially across 3 clean columns bridging the screen perfectly
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("<h3 style='color: #00d4ff;'>🖥️ Core Identity</h3>", unsafe_allow_html=True)
    company = st.selectbox('Brand Name', df['Company'].unique())
    type = st.selectbox('Chassis Type', df['TypeName'].unique())
    os = st.selectbox('Operating System', df['os'].unique())
    weight = st.number_input('Total Weight (kg)', min_value=0.5, max_value=6.0, value=2.0, step=0.1)

with col2:
    st.markdown("<h3 style='color: #00d4ff;'>⚡ Processing</h3>", unsafe_allow_html=True)
    cpu = st.selectbox('CPU Processor', df['Cpu brand'].unique())
    gpu = st.selectbox('Graphics Unit', df['Gpu brand'].unique())
    ram = st.selectbox('System Memory (RAM in GB)', [2,4,6,8,12,16,24,32,64], index=3)
    hdd = st.selectbox('Mechanical Drive (HDD in GB)', [0,128,256,512,1024,2048], index=0)
    ssd = st.selectbox('Solid State Drive (SSD in GB)', [0,8,128,256,512,1024], index=4)

with col3:
    st.markdown("<h3 style='color: #00d4ff;'>📱 Display Metrics</h3>", unsafe_allow_html=True)
    screen_size = st.slider('Display Size (Inches)', 10.0, 18.0, 15.6, step=0.1)
    resolution = st.selectbox('Screen Resolution', ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
    ips = st.selectbox('IPS Panel Engine', ['No','Yes'])
    touchscreen = st.selectbox('Touch Display Interaction', ['No','Yes'])

# ==================== Prediction Execution ==================== #
bcol1, bcol2, bcol3 = st.columns([1,2,1])
with bcol2:
    submit = st.button('GENERATE PREDICTION', use_container_width=True)

if submit:
    with st.spinner("Compiling hardware configuration metrics into neural network..."):
        # Explicit binary conversion natively identically structurally bridging the model mapping
        touchscreen_val = 1 if touchscreen == 'Yes' else 0
        ips_val = 1 if ips == 'Yes' else 0

        # PPI Resolution explicit metric logic exactly as requested initially
        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
        
        # Format the Heterogeneous Array mapping exactly preventing Unicode-3 string crashes
        query = np.array([company, type, ram, weight, touchscreen_val, ips_val, ppi, cpu, hdd, ssd, gpu, os], dtype=object)
        query = query.reshape(1,12)
        
        # Exponential inverse extraction mapping
        exact_prediction = int(np.exp(pipe.predict(query)[0]))
        
        # Format exactly as Indian Rupees nicely
        formatted_price = f"₹ {exact_prediction:,}"
        
        # Push the explicit structural card block replacing simple single-string header!
        st.markdown(f"""
        <div class="price-card">
            <div class="price-label">Estimated Current Market Value</div>
            <div class="price-value">{formatted_price}</div>
            <div class="ai-badge">⚡ Neural Appraisal Finalized</div>
        </div>
        """, unsafe_allow_html=True)

# Footer overlay
st.markdown("<div class='footer'>Developed by Komal Mittal</div>", unsafe_allow_html=True)
