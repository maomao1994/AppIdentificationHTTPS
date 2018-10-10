import pandas as pd
payload_train=pd.read_csv("./data/payload_train.csv")
payload_val=pd.read_csv("./data/payload_val.csv")
print("payload_train:")
print(payload_train[payload_train["label"]==0]["ss0"].count())
print(payload_train[payload_train["label"]==1]["ss0"].count())
print(payload_train[payload_train["label"]==2]["ss0"].count())
print("payload_val:")
print(payload_val[payload_val["label"]==0]["ss0"].count())
print(payload_val[payload_val["label"]==1]["ss0"].count())
print(payload_val[payload_val["label"]==2]["ss0"].count())