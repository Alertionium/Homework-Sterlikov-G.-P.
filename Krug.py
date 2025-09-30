import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
amount=[0.22, 0.21, 0.2, 0.19, 0.18,]
labels = ['Да','Да, но серым','Определенно', 'Ты ещё спрашиваешь!?', 'Что ты сидишь тут иди матан учи!']
color_=['green','grey', 'blue', 'orange', 'red']
plt.title('Мне нужно поправить матан?')
plt.pie(amount, labels=labels, colors=color_)
plt.show()