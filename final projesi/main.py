from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# -------------------------------------------------------------
# 1. ADIM: İklim Değişikliği Haberleri ve "Neden Var?" Sayfası
# -------------------------------------------------------------
@app.route('/')
def haberler():
    # Haberler ve iklim değişikliğinin nedenleri burada gösterilir
    return render_template('index.html')

# -------------------------------------------------------------
# 2. ADIM: "Kime Zarar Veriyor?" ve "Nasıl Önleriz?" Sayfası
# -------------------------------------------------------------
@app.route('/etkiler-ve-cozumler')
def etkiler():
    # Zararlar ve çözüm yolları bilgisi yer alır
    return render_template("etkinlikler.html")

# -------------------------------------------------------------
# 3. ADIM: Yeşil Ev Anketi Sayfası
# -------------------------------------------------------------
@app.route('/yesil-ev-anketi')
def anket():
    # Kullanıcıya yeşil ev ve günlük alışkanlık soruları sorulur
    return render_template('anket.html')

# -------------------------------------------------------------
# 4. ADIM: Anket Sonuçları ve Kişiselleştirilmiş Öneriler Sayfası
# -------------------------------------------------------------
@app.route('/sonuc', methods=['POST'])
def sonuc():
    # Formdan gelen yanıtları alıyoruz
    isiklar = request.form.get('isiklar')          # evet / hayir
    ulasim = request.form.get('ulasim')            # araba / toplu / yuru
    geri_donusum = request.form.get('geri_donusum')# evet / hayir
    plastik = request.form.get('plastik')          # evet / hayir

    oneriler = []
    puan = 100

    # Yanıtlara göre öneriler ve puan hesaplama
    if isiklar == 'hayir':
        oneriler.append("💡 Odadan çıkarken lambaları kapatarak yılda yaklaşık 100 kg CO₂ salınımını engelleyebilirsin.")
        puan -= 20

    if ulasim == 'araba':
        oneriler.append("🚲 Short (kısa) mesafelerde araba yerine yürümeyi veya bisiklete binmeyi tercih ederek karbon ayak izini ciddi oranda düşürebilirsin.")
        puan -= 25
    elif ulasim == 'toplu':
        oneriler.append("🚌 Toplu taşıma harika bir tercih! İmkan buldukça yürümek daha da yeşil bir seçenek olacaktır.")

    if geri_donusum == 'hayir':
        oneriler.append("♻️ Kağıt, plastik ve cam atıklarını ayrı kutulara atarak geri dönüşüme kazandırmalısın.")
        puan -= 25

    if plastik == 'evet':
        oneriler.append("🛍️ Tek kullanımlık plastikler yerine matara ve bez çanta kullanarak doğayı koruyabilirsin.")
        puan -= 20

    if puan == 100:
        oneriler.append("🌟 Harikasın! Gerçek bir doğa dostu olarak Yeşil Ev standartlarına tam uyuyorsun!")

    return render_template("sonuç.html", oneriler=oneriler, puan=puan)

if __name__ == '__main__':
    app.run(debug=True)