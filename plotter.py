import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.data', header=None)
iris.columns = [
    'sepal_width', 'sepal_length', 'petal_width',
    'petal_length', 'species']


def make_boxplot(data_set, columns, ylabel, file_name):
    plt.figure()
    plt.boxplot(iris[columns], labels=columns)
    plt.ylabel(ylabel)
    plt.savefig(file_name)


measurement_names = [
    'sepal_length', 'sepal_width', 'petal_width', 'petal_length']


def make_scatterplot(
        data_set, color_column, xcol, ycol, xlab, ylab, file_name):
    plt.figure()
    for n in set(data_set[color_column]):
        data_subset = iris[data_set[color_column] == n]
        plt.scatter(data_subset[xcol], data_subset[ycol],
                    label=n, s=5)
    plt.legend()
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.savefig(file_name)


plt.savefig('combo_plot.png')


def main():
    # plot scatter plot of petal length vs width with iris species
    make_boxplot(iris, measurement_names, 'cm', 'iris_boxplot.png')
    # plot scatter plot of petal length vs width with iris species
    # colored differently
    make_scatterplot(
        iris, 'species', 'petal_length', 'petal_width',
        'petal_length (cm)', 'petal_width (cm)', 'iris_scatter.png')

    # plot the above two plots as subplots
    plt.figure()
    fig, axes = plt.subplots(1, 2)
    fig.set_size_inches(10, 5)

    # left plot
    axes[0].boxplot(iris[measurement_names], labels=measurement_names)
    axes[0].set_ylabel('cm')

    # right plot
    for species_name in set(iris['species']):
        iris_subset = iris[iris['species'] == species_name]
        axes[1].scatter(iris_subset['petal_length'],
                        iris_subset['petal_width'], label=species_name, s=5)
    axes[1].legend()
    axes[1].set_xlabel('petal_length (cm)')
    axes[1].set_ylabel('petal_width (cm)')

    plt.savefig('combo_plot.png')
    print("Script is finished running")


if __name__ == '__main__':
    main()
