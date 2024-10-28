from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load 2 CSV files Gross National Product and Life Expectancy.
    Create a scatter plot with GNP in x axis and LE in y axis, then
    visualize the correlation between them.
    """
    path_gnp = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    path_le = "life_expectancy_years.csv"
    gross_national_product_data = load(path_gnp)
    life_expectancy_data = load(path_le)
    year_1900_column = '1900'
    gnp_1900 = gross_national_product_data[year_1900_column]
    le_1900 = life_expectancy_data[year_1900_column]

    plt.figure(figsize=(10, 6))
    plt.scatter(gnp_1900, le_1900)
    plt.title("Life Expectancy and Gross Domestic Product (Year 1900)")
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy (Years)")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=["300", "1k", "10k"])
    plt.tight_layout()
    plt.show()

    return 0


if __name__ == "__main__":
    main()
