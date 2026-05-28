import numpy as np
from scipy import stats

def confidence_interval(theta_hat, sigma, n, confidence=0.95):
    """
    Rumus: $\hat{\theta} \pm z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}$
    Referensi: Tsun (2020), Halaman 300.
    """
    alpha = 1 - confidence
    z_critical = stats.norm.ppf(1 - alpha / 2)
    margin_of_error = z_critical * (sigma / np.sqrt(n))
    
    return {
        "theta_hat": float(theta_hat),
        "lower_bound": float(theta_hat - margin_of_error),
        "upper_bound": float(theta_hat + margin_of_error)
    }

def ci_bernoulli(k, n, confidence=0.95):
    """    
    Rumus: $\hat{\theta} \pm z_{\alpha/2} \times \sqrt{\frac{\hat{\theta}(1-\hat{\theta})}{n}}$
    Referensi: Tsun (2020), Halaman 300.
    """
    theta_hat = k / n
    alpha = 1 - confidence
    z_critical = stats.norm.ppf(1 - alpha / 2)
    standard_error = np.sqrt((theta_hat * (1 - theta_hat)) / n)
    margin_of_error = z_critical * standard_error
    
    return {
        "theta_hat": float(theta_hat),
        "lower_bound": float(max(0.0, theta_hat - margin_of_error)),
        "upper_bound": float(min(1.0, theta_hat + margin_of_error))
    }

def ci_poisson(data, confidence=0.95):
    """
    Rumus: $\hat{\theta} \pm z_{\alpha/2} \times \sqrt{\frac{\hat{\theta}}{n}}$
    Referensi: Tsun (2020), Halaman 254 (MLE) & Halaman 300 (CI).
    """
    n = len(data)
    theta_hat = np.sum(data) / n
    alpha = 1 - confidence
    z_critical = stats.norm.ppf(1 - alpha / 2)
    standard_error = np.sqrt(theta_hat / n)
    margin_of_error = z_critical * standard_error
    
    return {
        "theta_hat": float(theta_hat),
        "lower_bound": float(max(0.0, theta_hat - margin_of_error)),
        "upper_bound": float(theta_hat + margin_of_error)
    }

def credible_interval(alpha_post, beta_post, confidence=0.95):
    """
    Rumus: $[F^{-1}(\frac{\alpha_{tail}}{2}), F^{-1}(1 - \frac{\alpha_{tail}}{2})]$
    Referensi: Tsun (2020), Halaman 269.
    """
    alpha_tail = (1 - confidence) / 2
    lower_bound = stats.beta.ppf(alpha_tail, alpha_post, beta_post)
    upper_bound = stats.beta.ppf(1 - alpha_tail, alpha_post, beta_post)
    
    return {
        "lower_bound": float(lower_bound),
        "upper_bound": float(upper_bound)
    }