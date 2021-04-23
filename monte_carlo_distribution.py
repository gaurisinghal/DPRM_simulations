import matplotlib.pyplot as plt

with open("Monte Carlo Data/expected_put_100000.txt", "r") as filehandle: 
    text = filehandle.readlines() #reading all the expected call/put payouts from the file


for i in range(len(text)):
    text[i] = float(text[i].strip())

fig = plt.hist(text) 
#plt.title("Average(Max(ST - X, 0))") #histogram of expected call payouts
plt.title("Average(Max(X - ST, 0))") #histogram of expected put payouts
plt.show()
