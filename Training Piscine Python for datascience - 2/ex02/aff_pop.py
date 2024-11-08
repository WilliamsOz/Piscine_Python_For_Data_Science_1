from load_csv import load
import matplotlib.pyplot as plt


def prepare_data_str_to_int(string):
    """
    Prepare population data from string to integer.

    Args (string) :
        The string to convert in integer, can be in million, in k.

    Returns :
        The converted value.
    """
    if string.endswith("M"):
        return float(string[:-1]) * 1e6
    elif string.endswith("K"):
        return float(string[:-1]) * 1e3
    else:
        return float(string)


def main():
    """
    Load a CSV file about population through years and show France curve and
    another country.

    The graph showing 2 country's populations through years.
    Title of graph : Population Projections.
    x-axis : Years.
    y-axis : Population.
    """
    dataset = load("population_total.csv")

    if dataset is None:
        exit(1)

    if 'country' not in dataset.columns:
        print("\033[31mError: \'country\' columns not found\033[0m")
        exit(1)

    if not (dataset['country'] == 'France').any():
        print("\033[31mError: \'France\' data not found\033[0m")
        exit(1)
    if not (dataset['country'] == 'Germany').any():
        print("\033[31mError: \'Germany\' data not found\033[0m")
        exit(1)

    try:
        french_data = dataset[dataset['country'] == 'France'].iloc[:, 1:]
        germany_data = dataset[dataset['country'] == 'Germany'].iloc[:, 1:]

        french_pop = french_data.values.flatten()
        german_pop = germany_data.values.flatten()
        years = french_data.columns.astype(int)

        french_pop = [prepare_data_str_to_int(pop) for pop in
                      french_pop if pop == pop]
        german_pop = [prepare_data_str_to_int(pop) for pop in
                      german_pop if pop == pop]

        plt.plot(years, french_pop, label="France")
        plt.plot(years, german_pop, label="Germany")

        plt.title("Population Projections")
        plt.xlabel("Years")
        plt.xticks(range(1800, 2050, 40))
        plt.xlim(1800, 2050)
        plt.ylabel("Population")
        plt.legend()
        plt.tight_layout()
        max_pop = max(max(french_pop), max(german_pop))
        y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
        plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
        plt.show()

    except Exception as error:
        print("\033[31m", Exception.__name__ + ":", error, "\033[0m")

    return 0


if __name__ == "__main__":
    main()
