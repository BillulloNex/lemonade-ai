from datasets import load_dataset
ds = load_dataset("ybisk/piqa",trust_remote_code=True)
print(ds)