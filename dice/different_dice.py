from dice.die import Die
import pygal


die_1 = Die()
die_2 = Die(10)

results = [die_1.roll()+die_2.roll() for result in range(50000)]

#for roll_num in range(50000):
#    result = die_1.roll()+die_2.roll()
#    results.append(result)


max_result = die_1.num_sides + die_2.num_sides

frequencies = [results.count(value) for value in range(2, max_result+1)]

#for value in range(2, max_result+1):
#    frequency = results.count(value)
#    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()
hist.title = 'Resultados de rolar um dado D6 e um d10 50000 vezes'

hist.x_labels = [str(number_side) for number_side in range(max_result+1) if number_side>1]
hist.x_title = 'Result'

hist.y_title = 'Resultado da Frequencia'

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_visual.svg')