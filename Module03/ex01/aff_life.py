from load_csv import load
import matplotlib.pyplot as plt


def aff_life(path: str) -> None:
    """Shows a graph of life expectancy in Morocco from 1800 to 2100
    Args:
        path: path to the csv file
    """
    # load the csv file
    df = load(path)
    if (df is None):
        return None
    # set the country column as index
    df.set_index("country", inplace=True)
    # get the Morocco data
    morocco_data = df.loc['Morocco']
    # extract year value & life expenctancy values
    years = morocco_data.keys()
    life_expectancy_values = morocco_data.values
    # plot values
    plt.plot(years, life_expectancy_values)
    plt.title("Morocco life expectancy projections")
    plt.xlabel("Year")

    plt.ylabel("Life Expectancy")
    plt.xticks(years[::40])
    plt.show()


def main():
    aff_life("life_expectancy_years.csv")


if __name__ == "__main__":
    main()
