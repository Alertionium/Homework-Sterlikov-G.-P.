import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = [1, 2, 3, 4]
y = [12, 56, 67, 75]

plt.plot(x, y, marker='o')
ax = plt.gca()

ax.set_xlim(1, 5)
ax.set_ylim(0, 80)

ax.set_xticks([1, 2, 3, 4])
ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80])

ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

ax.xaxis.set_minor_formatter(ticker.FormatStrFormatter('%g'))
ax.yaxis.set_minor_formatter(ticker.FormatStrFormatter('%g'))
plt.plot(x, y, color='purple', marker='o', markersize=5)
plt.xlabel('Номер занятия') 
plt.ylabel('Заинтересованность в %') 
plt.title('Отношение к информатике') 
plt.grid(True)
plt.show()