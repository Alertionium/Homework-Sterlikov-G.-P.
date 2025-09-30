import matplotlib.pyplot as plt
x = ['Ангем', 'Информатика', 'Ин. Яз', 'Общефиз', 'Матан']
y = [100, 100, 100, 65, 25]

plt.bar(x, y, label='Выполненое дз', alpha=0.1 )
plt.plot(x, y, color='Orange', marker='o', markersize=7)
plt.xlabel('Предмет')
plt.ylabel('% выполнения')
plt.title('Траблы с дз')
plt.legend(loc='upper right')
plt.show()