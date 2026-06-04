import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../data/clean/issues_clean.csv')

close_time_days = df['close_time_days'].dropna().values
len(close_time_days)

sample_demo = np.random.choice(close_time_days, size=len(close_time_days), replace=True)
print('Contoh proporsi >30 hari (satu resample):', np.mean(sample_demo > 30))

n_sim = 10000
sample_size = len(close_time_days)
results = np.empty(n_sim, dtype=float)

for i in range(n_sim):
    sample = np.random.choice(close_time_days, size=sample_size, replace=True)
    results[i] = np.mean(sample > 30)

estimate = results.mean()
ci_lower, ci_upper = np.percentile(results, [2.5, 97.5])
print(f'Estimasi probabilitas issue > 30 hari: {estimate:.4f}')
print(f'95% interval kepercayaan: {ci_lower:.4f} - {ci_upper:.4f}')

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(results, bins=30, color='tab:blue', edgecolor='black')
plt.axvline(estimate, color='red', linestyle='--', label=f'estimasi = {estimate:.3f}')
plt.xlabel('Probabilitas issue > 30 hari')
plt.ylabel('Frekuensi simulasi')
plt.title('Distribusi estimasi probabilitas dari simulasi Monte Carlo')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(close_time_days, bins=40, color='tab:green', edgecolor='black')
plt.axvline(30, color='red', linestyle='--', label='30 hari')
plt.xlabel('Waktu penyelesaian (close_time_days)')
plt.ylabel('Jumlah issue')
plt.title('Distribusi waktu penyelesaian issue')
plt.legend()

plt.tight_layout()
plt.show()