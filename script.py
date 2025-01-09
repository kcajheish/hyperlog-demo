from hyperlog import HyperLog
hyperlog = HyperLog(12)
N = 100000
for i in range(N):
    hyperlog.insert(str(i))
card = hyperlog.cardinality()
print("actual=", card, "expect=", N)
print("expect_err=", hyperlog.error(), "actual_err=",abs((card-N)/N * 100))
