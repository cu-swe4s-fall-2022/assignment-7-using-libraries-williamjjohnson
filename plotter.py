import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.data', header=None)
iris.columns = [
    'sepal_width','sepal_length','petal_width',
    'petal_length','species']

# Plot boxplot for each measurement of iris
measurement_names = [
    'sepal_length','sepal_width','petal_width','petal_length']
plt.figure()
plt.boxplot(iris[measurement_names],labels=measurement_names)
plt.ylabel('cm')
plt.savefig("iris_boxplot.png")

# plot scatter plot of petal length vs width with iris species
# colored differently
plt.figure()
for species_name in set(iris['species']):
    iris_subset = iris[iris['species'] == species_name]
    plt.scatter(iris_subset['petal_length'], iris_subset['petal_width'], 
         label=species_name, s=5)
plt.legend()
plt.xlabel('petal_length (cm)')
plt.ylabel('petal_width (cm)')
plt.savefig("iris_scatter.png")

# plot the above two plots as subplots
plt.figure()
fig, axes = plt.subplots(1,2)
fig.set_size_inches(10,5)

# left plot
axes[0].boxplot(iris[measurement_names],labels=measurement_names)
axes[0].set_ylabel('cm')

# right plot
for species_name in set(iris['species']):
    iris_subset = iris[iris['species'] == species_name]
    axes[1].scatter(iris_subset['petal_length'], iris_subset['petal_width'], 
         label=species_name, s=5)
axes[1].legend()
axes[1].set_xlabel('petal_length (cm)')
axes[1].set_ylabel('petal_width (cm)')

plt.savefig('combo_plot.png')
