from scipy.stats import bernoulli, binom

# Probability of coin with bias 0.35 heads and 10 rounds
print(bernoulli.rvs(p=0.35, size=10))

# Probablity of coin with bias 0.35 10 rounds 10 times
print(binom.rvs(n=10, p=0.35, size=10))