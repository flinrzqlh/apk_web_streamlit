# Nama 	: Muhammad Efflin Rizqallah Limbong
# Absen : 225371440007

# Core Pkgs
import streamlit as st
import sklearn
import joblib,os
import numpy as np

# Loading Models
def load_prediction_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model

def main():
	"""Regresi Linier Sederhana"""

	st.title("Prediksi Nilai Siswa")

	html_templ = """
	<div style="background-color:#726E6D;padding:10px;">
	<h3 style="color:white">Prediksi Nilai Siswa Menggunakan Regresi Linier</h3>
	</div>
	"""

	st.markdown(html_templ,unsafe_allow_html=True)

	activity = ["Prediksi Nilai Siswa","Apa itu Regresi?"]
	choice = st.sidebar.selectbox("Menu",activity)

# Salary Determination CHOICE
	if choice == 'Prediksi Nilai Siswa':

		st.subheader("Prediksi Nilai Siswa")

		jamBelajar = st.slider("Berapa Jam Siswa tersebut belajar?",0,24)

		#st.write(type(jamBelajar))

		if st.button("Proses"):

			regressor = load_prediction_model("linear_regression_student_marks.pkl")
			jamBelajar_reshaped = np.array(jamBelajar).reshape(-1,1)
			nilai = regressor.predict(jamBelajar_reshaped)
			nilai = nilai[0][0] if nilai[0][0] <= 100 else float(100)

			st.info("Nilai siswa yang belajar selama {} jam: {:.2f}".format(jamBelajar,(nilai)))

if __name__ == '__main__':
	main()