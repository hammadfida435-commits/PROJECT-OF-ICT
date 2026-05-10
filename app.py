import streamlit as st

# --- UI Header ---
st.set_page_config(page_title="Mechanical Toolkit", page_icon="⚙️")
st.title("⚙️ Mechanical Unit Converter & Density Checker")

# PERSONAL INFO - Update these with your details
st.sidebar.markdown("### Developer Info")
st.sidebar.write("**Name:** Your Full Name")
st.sidebar.write("**Roll Number:** Your Roll Number")

# --- Section 1: Unit Converter ---
st.header("1. Mechanical Unit Converter")
col1, col2 = st.columns(2)

with col1:
    value = st.number_input("Enter Value:", value=1.0)
    conversion_type = st.selectbox("Select Conversion:", [
        "Force: Newtons to Pounds (lbf)",
        "Pressure: Pascal to Bar",
        "Torque: Nm to lb-ft",
        "Power: Watts to Horsepower (hp)"
    ])

with col2:
    if "Force" in conversion_type:
        result = value * 0.224809
        unit = "lbf"
    elif "Pressure" in conversion_type:
        result = value / 100000
        unit = "Bar"
    elif "Torque" in conversion_type:
        result = value * 0.73756
        unit = "lb-ft"
    else:
        result = value / 745.7
        unit = "hp"
    
    st.metric("Converted Value", f"{result:.4f} {unit}")

st.divider()

# --- Section 2: Material Density Checker ---
st.header("2. Material Density Checker")
materials = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Titanium": 4500,
    "Cast Iron": 7200
}

selected_material = st.selectbox("Select a Material:", list(materials.keys()))
density = materials[selected_material]

st.info(f"The density of **{selected_material}** is approximately **{density} kg/m³**.")

# Mass Calculation Feature
st.subheader("Estimate Mass")
volume = st.number_input("Enter Volume (m³):", min_value=0.0, value=0.1)
mass = volume * density
st.success(f"Estimated Mass: **{mass:.2f} kg**")
