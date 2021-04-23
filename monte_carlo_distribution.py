import matplotlib.pyplot as plt

with open("expected_call_10000.txt", "r") as filehandle:
    text = filehandle.readlines()


for i in range(len(text)):
    text[i] = float(text[i].strip())

fig = plt.hist(text) #histogram of expected call payouts
plt.title("Average(Max(ST-X, 0))")
plt.show()
