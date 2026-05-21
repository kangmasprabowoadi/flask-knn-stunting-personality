from flask import Flask, render_template, request
import joblib 
import numpy as np
import pandas as pd

app = Flask(__name__)

# ==========================================
# LOAD SEMUA MODEL & SCALER
# ==========================================
try:
    # Model Stunting
    model_stunting = joblib.load('model_knn_stunting.pkl')
    scaler_stunting = joblib.load('scaler.pkl') 
    
    # Model Personality
    model_personality = joblib.load('model_knn_personality.pkl')
    scaler_personality = joblib.load('scaler_personality.pkl')
    label_encoders = joblib.load('label_encoders.pkl')
    
    print("Semua Model dan Scaler berhasil dimuat.")
except Exception as e:
    print(f"Error saat memuat file: {e}")

# ==========================================
# ROUTE HALAMAN UTAMA (MENU)
# ==========================================
@app.route('/')
def home():
    return render_template('index.html')

# ==========================================
# ROUTE PREDIKSI STUNTING
# ==========================================
@app.route('/stunting', methods=['GET', 'POST'])
def stunting():
    if request.method == 'GET':
        return render_template('stunting.html')
        
    if request.method == 'POST':
        try:
            umur = float(request.form['umur'])
            jk_input = request.form['jenis_kelamin']
            tinggi = float(request.form['tinggi'])

            jk = 1 if jk_input == 'laki-laki' else 0
            fitur_raw = np.array([[umur, jk, tinggi]])
            fitur_scaled = scaler_stunting.transform(fitur_raw)

            prediksi = model_stunting.predict(fitur_scaled)
            angka_hasil = int(prediksi[0])

            status_map = {
                0: {"label": "Normal", "color": "bg-lime-100 border-lime-400 text-lime-900", "keterangan": "Tinggi badan balita sesuai dengan standar usianya.", "saran": "Pertahankan asupan gizi seimbang, rutin kunjungi posyandu, dan berikan stimulasi sesuai usianya."},
                1: {"label": "Sangat Pendek", "color": "bg-red-100 border-red-500 text-red-900", "keterangan": "Tinggi badan balita sangat jauh di bawah standar usianya (Severely Stunted).", "saran": "Segera konsultasikan ke Dokter Spesialis Anak (DSA) atau puskesmas untuk mendapatkan intervensi gizi medis secepatnya."},
                2: {"label": "Pendek", "color": "bg-pink-100 border-pink-400 text-pink-900", "keterangan": "Tinggi badan balita di bawah rata-rata standar usianya (Stunted).", "saran": "Tingkatkan asupan protein hewani (telur, ikan, daging) dan evaluasi jadwal makan. Pantau ketat di faskes terdekat."},
                3: {"label": "Tinggi", "color": "bg-green-100 border-green-500 text-green-900", "keterangan": "Tinggi badan balita berada di atas standar usianya.", "saran": "Pastikan pertumbuhan tinggi badan proporsional dengan berat badannya. Jika ragu, cek ke dokter anak."}
            }

            hasil_analisis = status_map.get(angka_hasil, {
                "label": f"Tidak Diketahui (Kode: {angka_hasil})", "color": "bg-gray-100 border-gray-400 text-gray-800", "keterangan": "Terjadi kesalahan identifikasi kelas.", "saran": "Harap periksa kembali model klasifikasi."
            })

            return render_template('stunting.html', hasil=hasil_analisis)
        except Exception as e:
            return render_template('stunting.html', error=f'Kesalahan Sistem: {str(e)}')

# ==========================================
# ROUTE PREDIKSI PERSONALITY
# ==========================================
@app.route('/personality', methods=['GET', 'POST'])
def personality():
    if request.method == 'GET':
        return render_template('personality.html')
        
    if request.method == 'POST':
        try:
            data_input = {
                "Time_spent_Alone": int(request.form['time_alone']),
                "Social_event_attendance": int(request.form['social_event']),
                "Going_outside": int(request.form['going_outside']),
                "Friends_circle_size": int(request.form['friends_size']),
                "Post_frequency": int(request.form['post_freq']),
                "Stage_fear": request.form['stage_fear'],
                "Drained_after_socializing": request.form['drained']
            }

            new_data_df = pd.DataFrame([data_input])
            categorical_cols = ['Stage_fear', 'Drained_after_socializing']
            for col in categorical_cols:
                le = label_encoders[col]
                new_data_df[col] = le.transform(new_data_df[col])

            numerical_cols = ['Time_spent_Alone', 'Social_event_attendance', 'Going_outside', 'Friends_circle_size', 'Post_frequency']
            new_data_df[numerical_cols] = scaler_personality.transform(new_data_df[numerical_cols])
            new_data_df = new_data_df[model_personality.feature_names_in_]

            prediksi_encoded = model_personality.predict(new_data_df)
            personality_le = label_encoders['Personality']
            hasil_akhir = personality_le.inverse_transform(prediksi_encoded)[0]

            if hasil_akhir.lower() == 'introvert':
                hasil_ui = {"label": "Introvert", "color": "text-indigo-600", "bg": "bg-indigo-50 border-indigo-200", "image": "/static/introvert.png", "deskripsi": "Anda cenderung mendapatkan energi dari waktu sendirian dan refleksi mendalam."}
            else:
                hasil_ui = {"label": "Ekstrovert", "color": "text-rose-600", "bg": "bg-rose-50 border-rose-200", "image": "/static/extrovert.png", "deskripsi": "Anda cenderung mendapatkan energi dari interaksi sosial dan aktivitas luar."}

            return render_template('personality.html', hasil=hasil_ui)
        except Exception as e:
            return render_template('personality.html', error=f'Terjadi Kesalahan: {str(e)}')

if __name__ == "__main__": 
    app.run(debug=True)