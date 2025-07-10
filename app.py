import os
import streamlit as st
from google.cloud import storage
from PIL import Image

# 🔐 Set Google Cloud Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "crowdmanagement.json"

# 🧠 Streamlit Page Config
st.set_page_config(page_title="Project Drishti", layout="wide")
st.title("👁️ Project Drishti – AI Safety Assistant")

# Tabs for different features
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📍 Smart Parking & Seating",
    "🎟️ Wristband Violation Detection",
    "🧒 Lost Child Finder",
    "💧 Water Dispatch AI",
    "📢 Voice Alert Simulation",
    "☁️ Google Cloud Key Test"
])

# ---------------- TAB 1: Smart Seating & Parking ----------------
with tab1:
    st.subheader("🎯 Intelligent Seating & Parking Zone Planner")

    zone = st.selectbox(
        "Select your seating zone:",
        ["Platinum", "Diamond", "Gold"]
    )

    if zone == "Platinum":
        st.success("🚘 Park your vehicle in Row 1")
    elif zone == "Diamond":
        st.success("🚘 Park your vehicle in Row 2")
    else:
        st.success("🚘 Park your vehicle in Row 3")

# ---------------- TAB 2: Wristband Violation Detection ----------------
with tab2:
    st.subheader("🎟️ Wristband Zone Violation Checker")

    band_color = st.selectbox("What is your wristband color?", ["Red – Platinum", "Blue – Diamond", "Green – Gold"])
    current_zone = st.selectbox("Which zone are you currently in?", ["Platinum", "Diamond", "Gold"])

    violation_detected = False

    if ("Red" in band_color and current_zone != "Platinum") or \
       ("Blue" in band_color and current_zone != "Diamond") or \
       ("Green" in band_color and current_zone != "Gold"):
        violation_detected = True

    if violation_detected:
        st.error("🚨 Zone Violation Detected! Guard alerted + drone voice warning activated.")
        st.audio("https://actions.google.com/sounds/v1/alarms/beep_short.ogg")
    else:
        st.success("✅ You are in the correct zone.")

# ---------------- TAB 3: Lost Child Finder ----------------
with tab3:
    st.subheader("🧒 Lost Child Finder")

    uploaded_file = st.file_uploader("Upload your child's photo here:", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded photo", width=200)
        st.info("AI is scanning camera feeds...")
        st.success("✅ Possible match found in Zone A, Block 4")
        st.button("✅ Confirm it's my child")
        st.button("❌ Not my child – keep searching")

# ---------------- TAB 4: Water Dispatch AI ----------------
with tab4:
    st.subheader("💧 Smart Water Need Detection & Drone Dispatch System")

    zone_name = st.selectbox("Select zone for monitoring:", ["Zone A", "Zone B", "Zone C", "Zone D"])
    heat_index = st.slider("AI Detected Heat/Stress Level", 0, 100, 40)

    water_needed = heat_index > 70

    if water_needed:
        st.warning(f"🚨 High dehydration risk detected in {zone_name}! Notify security to initiate drone loading.")
        guard_confirm = st.checkbox("✅ Guard confirmed: Water bottle loaded into drone.")

        if guard_confirm:
            st.success(f"🚁 Drone dispatched to {zone_name} with water bottles!")
            st.image("https://media.giphy.com/media/iFY8jynx1q3QA/giphy.gif", caption="Drone en route with water 💧")
            st.audio("https://actions.google.com/sounds/v1/water/water_pour.ogg")
        else:
            st.info("⏳ Awaiting guard confirmation for drone loading...")
    else:
        st.success("✅ Zone conditions are normal. No water assistance needed right now.")

# ---------------- TAB 5: Voice Alert Simulation ----------------
with tab5:
    st.subheader("📢 AI-Powered Voice & Display Alerts")

    if st.button("Trigger Alert: High Crowd in Zone C"):
        st.warning("📢 Alert Sent: Zone C is overcrowded! Please move calmly.")
        st.audio("https://actions.google.com/sounds/v1/alarms/beep_short.ogg")
        st.info("🗣️ Voice message played + guards notified.")

# ---------------- TAB 6: Google Cloud Key Test ----------------
with tab6:
    st.subheader("☁️ Google Cloud Key File Verification")

    try:
        client = storage.Client()
        buckets = list(client.list_buckets())
        st.success("✅ Successfully connected to Google Cloud!")

        if buckets:
            st.write("📦 Storage Buckets found in your project:")
            for bucket in buckets:
                st.write(f"– {bucket.name}")
        else:
            st.info("ℹ️ No storage buckets found, but connection is working.")
    except Exception as e:
        st.error("❌ Failed to connect to Google Cloud:")
        st.code(str(e))

# ---------------- Footer ----------------
st.markdown("---")
st.caption("🔐 Project Drishti | Powered by AI + Human Collaboration | Prototype by Kamal Hasan")
