import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("issues_clean.csv")          
data = df["close_time_days"].dropna()

print("=" * 55)
print("  UJI HIPOTESIS Z-TEST close_time_days")
print("=" * 55)

print()
print("Jumlah data (n)  :", len(data))
print("Rata-rata sampel :", round(data.mean(), 4), "hari")
print("Std deviasi      :", round(data.std(ddof=1), 4), "hari")
print("Min / Max        :", data.min(), "/", data.max(), "hari")

mu0  = 20          
arah = "two-sided" 

print()
print("-- Langkah 1 & 2: Hipotesis & alpha -------------")
print("  H0 : mean =", mu0, " (rata-rata =", mu0, "hari)")
if arah == "two-sided":
    print("  Ha : mean !=", mu0, " (rata-rata berbeda dari", mu0, "hari)")
elif arah == "greater":
    print("  Ha : mean >", mu0, " (rata-rata lebih dari", mu0, "hari)")
else:
    print("  Ha : mean <", mu0, " (rata-rata kurang dari", mu0, "hari)")

alpha = 0.05
print()
print("-- Langkah 3: Tingkat signifikansi --------------")
print("  alpha =", alpha)

n      = len(data)
mean   = data.mean()
std    = data.std(ddof=1)          
se     = std / np.sqrt(n)          
z_stat = (mean - mu0) / se

print()
print("-- Langkah 4: Hitung Z statistik ----------------")
print("  mean =", round(mean, 4))
print("  std  =", round(std, 4), " (std sampel, ddof=1)")
print("  SE   = std / sqrt(n) =", round(std, 4), "/ sqrt(" + str(n) + ") =", round(se, 6))
print("  Z    = (mean - mu0) / SE")
print("       = (" + str(round(mean, 4)) + " - " + str(mu0) + ") /", round(se, 6))
print("       =", round(z_stat, 4))

if arah == "two-sided":
    p_value  = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    z_kritis = stats.norm.ppf(1 - alpha / 2)
elif arah == "greater":
    p_value  = 1 - stats.norm.cdf(z_stat)
    z_kritis = stats.norm.ppf(1 - alpha)
else:
    p_value  = stats.norm.cdf(z_stat)
    z_kritis = stats.norm.ppf(alpha)

print()
print("-- Langkah 5: Hitung p-value --------------------")
print("  Arah uji  :", arah)
print("  p-value   =", round(p_value, 6))
if arah == "two-sided":
    print("  Z kritis  = +/-", round(z_kritis, 4), "  (alpha/2 =", alpha / 2, ")")
else:
    print("  Z kritis  =", round(z_kritis, 4))

print()
print("-- Langkah 6: Bandingkan & Kesimpulan -----------")
print("  p-value (" + str(round(p_value, 6)) + ")  vs  alpha (" + str(alpha) + ")")

if p_value < alpha:
    keputusan    = "REJECT H0"
    interpretasi = ("Terdapat cukup bukti statistik bahwa rata-rata waktu "
                    "penyelesaian issue BERBEDA dari " + str(mu0) + " hari "
                    "(alpha = " + str(alpha) + ").")
else:
    keputusan    = "FAIL TO REJECT H0"
    interpretasi = ("Tidak terdapat cukup bukti statistik untuk menyatakan "
                    "bahwa rata-rata waktu penyelesaian issue berbeda dari "
                    + str(mu0) + " hari (alpha = " + str(alpha) + ").")

print()
print("  Keputusan    :", keputusan)
print()
print("  Interpretasi :", interpretasi)
print("=" * 55)