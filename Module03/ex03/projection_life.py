from load_csv import load
import matplotlib.pyplot as plt


def projection_life() -> None:
    """Shows a graph of correlation between life expectancy
    and income per person in 1900
    """
    # load the csv files
    life_df = load("life_expectancy_years.csv")
    ipp_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if (life_df is None or ipp_df is None):
        return None
    # select life expectancy & ipp values for the year 1900
    life_1900 = life_df[["country", "1900"]]["1900"]
    ipp_1900 = ipp_df[["country", "1900"]]["1900"]
    # plot data
    plt.scatter(ipp_1900, life_1900)
    # customize graph
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], labels=["300", "1k", "10k"])

    plt.show()


def main():
    projection_life()


if __name__ == "__main__":
    main()
