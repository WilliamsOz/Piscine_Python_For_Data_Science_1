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

    if dataset is None:
        exit(1)

    if 'country' not in dataset.columns:
        print("\033[31mError: \'country\' columns not found\033[0m")
        exit(1)

    if not (dataset['country'] == 'France').any():
        print("\033[31mError: \'France\' data not found\033[0m")
        exit(1)

    tmp_dataset = dataset.set_index('country')
    for x in tmp_dataset.loc['France']:
        try:
            int(x)
        except Exception:
            print("\033[31mError: dataset must contains only integer\
or float values\033[0m")
            exit(1)

    french_data = dataset[dataset['country'] == 'France']
    years = french_data.columns[1:]
    life_expectancy = french_data.values[0][1:]

    plt.plot(years, life_expectancy, label='France')
    plt.title('France Life expectancy Projections')
    plt.xlabel('Year')
    plt.xticks(years[::40])
    plt.ylabel('Life expectancy')
    plt.yticks(range(30, 100, 10))
    plt.legend()
    plt.tight_layout()
    plt.show()

    return 0


if __name__ == "__main__":
    main()
