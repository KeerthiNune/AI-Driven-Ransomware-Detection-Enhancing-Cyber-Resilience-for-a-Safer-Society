import streamlit as st
import numpy as np
import joblib

xgb_class = joblib.load("xgb_class.pkl")
xgb_family = joblib.load("xgb_family.pkl")    
scaler_fam = joblib.load("scaler_fam.pkl")    
le_fam = joblib.load("le_fam.pkl")            
indices = joblib.load("feature_indices.pkl")  


feature_names = [
    "network_http",
    "files_unknown",
    "total_procsses",
    "network_dns",
    "files_suspicious",
    "registry_read",
    "processes_monitored",
    "registry_total",
    "files_malicious",
    "processes_malicious"
]


st.set_page_config(page_title="Ransomware Detection Dashboard", page_icon="🧠", layout="centered")

st.title(" Ransomware Detection & Family Classification")
st.write("""
This application uses trained AI models to:
1. Detect whether the given file behavior is **Benign** or **Ransomware**.  
2. If it's ransomware, identify the **Ransomware Family**.
""")

st.markdown("---")
st.subheader(" Enter Feature Values")


feature_values = []
for name in feature_names:
    val = st.number_input(f"{name}", value=0.0, step=0.01)
    feature_values.append(val)

if st.button(" Predict"):
    features_array = np.array(feature_values).reshape(1, -1)

    label_map = {0: "Benign", 1: "Ransomware"}
    pred_det = xgb_class.predict(features_array)[0]
    pred_det_label = label_map.get(int(pred_det), str(pred_det))

    st.markdown("### Detection Result")
    if pred_det_label.lower() == "benign":
        st.success(" The file is **Benign** No ransomware family detected.")
    else:
        st.error(" The file is **Ransomware**.")

        
        full_vector = np.zeros((1, scaler_fam.mean_.shape[0]))
        full_vector[:, indices] = features_array  
        full_scaled = scaler_fam.transform(full_vector)

        fam_input = full_scaled[:, indices]

        pred_fam_enc = xgb_family.predict(fam_input)[0]
        pred_fam_label = le_fam.inverse_transform([pred_fam_enc])[0]

        st.markdown("###  Family Classification Result")
        st.warning(f"Predicted Ransomware Family: **{pred_fam_label}**")

        fam_proba = np.max(xgb_family.predict_proba(fam_input)[0]) * 100
        st.info(f"Prediction Confidence: {fam_proba:.2f}%")