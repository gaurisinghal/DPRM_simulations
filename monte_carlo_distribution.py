import matplotlib.pyplot as plt

with open("expected_call_1000.txt", "r") as filehandle:
    text = filehandle.readlines()


for i in range(len(text)):
    text[i] = float(text[i].strip())

#fig, ax = plt.subplots()
fig = plt.hist(text)
plt.title("Average(Max(ST-X, 0))")
plt.show()
