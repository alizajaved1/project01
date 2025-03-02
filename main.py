import streamlit as st

# Conversion function
def convert_units(value, from_unit, to_unit, category):
    conversions = {
        "Length": {
            "Meter": {"Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Foot": 3.28084, "Inch": 39.3701},
            "Kilometer": {"Meter": 1000, "Centimeter": 100000, "Millimeter": 1e6, "Foot": 3280.84, "Inch": 39370.1},
            "Centimeter": {"Meter": 0.01, "Kilometer": 1e-5, "Millimeter": 10, "Foot": 0.0328084, "Inch": 0.393701},
            "Foot": {"Meter": 0.3048, "Kilometer": 0.0003048, "Centimeter": 30.48, "Millimeter": 304.8, "Inch": 12},
        },
        "Weight": {
            "Kilogram": {"Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
            "Gram": {"Kilogram": 0.001, "Pound": 0.00220462, "Ounce": 0.035274},
            "Pound": {"Kilogram": 0.453592, "Gram": 453.592, "Ounce": 16},
        },
        "Temperature": {
            "Celsius": {"Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15},
            "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5/9, "Kelvin": lambda f: (f - 32) * 5/9 + 273.15},
            "Kelvin": {"Celsius": lambda k: k - 273.15, "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32},
        }
    }

    if from_unit == to_unit:
        return value  # No conversion needed
    
    try:
        factor = conversions[category][from_unit][to_unit]
        return factor(value) if callable(factor) else value * factor
    except KeyError:
        return None

# Streamlit UI
st.set_page_config(page_title="Unit Converter", page_icon="🔄")

st.title("🔄 Simple Unit Converter")

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

# Unit selection
if category == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Foot", "Inch"]
elif category == "Weight":
    units = ["Kilogram", "Gram", "Pound", "Ounce"]
else:
    units = ["Celsius", "Fahrenheit", "Kelvin"]

from_unit = st.selectbox("Convert From", units)
to_unit = st.selectbox("Convert To", units)
value = st.number_input("Enter Value", format="%.2f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    if result is not None:
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    else:
        st.error("Conversion not supported!")

st.markdown("---")
st.caption("Made By ❤️ Aliza Javed")
