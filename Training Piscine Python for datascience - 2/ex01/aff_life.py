from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load a CSV file about life expectancy, filter for france and display a
    graph.

    The graph showing the life expectancy in France over years.
    Title of graph : France Life expectancy Projections.
    x-axis : Years.
    y-axis : Life expectancy.
    """
    dataset = load("life_expectancy_years.csv")
    french_data = dataset[dataset['country'] == 'France']
    years = french_data.columns[1:]
    life_expectancy = french_data.values[0][1:]

    plt.plot(years, life_expectancy, label='France')
    plt.title('France Life expectancy Projections')
    plt.xlabel('Year')
    plt.xticks(years[::40])
    plt.ylabel('Life expectancy')
    plt.yticks(range(30, 101, 10))
    plt.legend()
    plt.tight_layout()
    plt.show()

    return 0


if __name__ == "__main__":
    main()
