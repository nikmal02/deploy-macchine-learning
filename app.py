import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# PAGE CONFIG
st.set_page_config(
    page_title="Diamond Price Predictor",
    page_icon="💎",
    layout="wide"
)

# CUSTOM CSS (BLUE AI STYLE)
st.markdown("""
<style>

.stApp{
background-color:#0F172A;
color:white;
}

h1,h2,h3{
color:#E2E8F0;
}

hr{
border:1px solid #FFFFFF;
opacity:0.8;
}

div.stButton > button{
background-color:#2563EB;
color:white;
border-radius:8px;
border:none;
padding:10px 20px;
font-weight:bold;
}

div.stButton > button:hover{
background-color:#1D4ED8;
}

[data-testid="stMetricValue"]{
color:#60A5FA;
font-size:40px;
}

[data-testid="stDataFrame"]{
background-color:#020617;
}

</style>
""", unsafe_allow_html=True)

# LOAD MODEL
model = joblib.load("best_diamond_model.pkl")

# TITLE
st.title("💎 Diamond Price Predictor 💎")

st.markdown(
"""
Estimate the **market price of a diamond** based on its characteristics.
"""
)

st.markdown("---")

# SPECIFICATIONS
st.header("Diamond Specifications")

col_left, col_right = st.columns(2)

# DIMENSIONS
with col_left:

    st.markdown("### Diamond Dimensions")

    c1,c2 = st.columns(2)

    with c1:
        carat = st.number_input("Carat",0.1,5.0,0.5)
        depth = st.number_input("Depth",40.0,80.0,60.0)
        table = st.number_input("Table",40.0,100.0,55.0)

    with c2:
        x = st.number_input("Length (x)",0.0,10.0,4.0)
        y = st.number_input("Width (y)",0.0,10.0,4.0)
        z = st.number_input("Height (z)",0.0,10.0,2.5)

# QUALITY
with col_right:

    st.markdown("### Diamond Quality")

    cut = st.selectbox("Cut",["Fair","Good","Very Good","Premium","Ideal"])
    color = st.selectbox("Color",["D","E","F","G","H","I","J"])
    clarity = st.selectbox("Clarity",["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"])

# DATAFRAME
data = pd.DataFrame({
    "carat":[carat],
    "depth":[depth],
    "table":[table],
    "x":[x],
    "y":[y],
    "z":[z],
    "cut":[cut],
    "color":[color],
    "clarity":[clarity]
})

st.markdown("---")

colA,colB = st.columns([1,1])

# INPUT DATA
with colA:

    st.subheader("Input Data")

    st.dataframe(
        data,
        use_container_width=True
    )

# PREDICTION RESULT
with colB:

    st.subheader("Prediction Result")

    if st.button("Predict Price 💰"):

        prediction = model.predict(data)

        price = prediction[0]

        st.markdown(f"""
        ## 💰 ${price:,.2f}
        ### Estimated Diamond Price
        """)

        st.success("Prediction completed successfully!")

st.markdown("---")