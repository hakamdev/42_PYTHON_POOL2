from load_csv import load
import matplotlib.pyplot as plt


def convert(val):
    suffix = val[-1].lower()
    if suffix == 'b':
        return int(float(val[:-1]) * 1000000000)
    if suffix == 'm':
        return int(float(val[:-1]) * 1000000)
    elif suffix == 'k':
        return int(float(val[:-1]) * 1000)
    else:
        return int(val)


def aff_pop(path: str) -> None:
    """Shows a graph of population in Morocco vs France from 1800 to 2050
    Args:
        path: path to the csv file
    """
    # load the csv file
    df = load(path)
    if (df is None):
        return None
    # set the country column as index
    df.set_index("country", inplace=True)
    # get the Morocco and France data
    morocco_data = df.loc["Morocco", '1800': '2050'].map(convert)
    france_data = df.loc["France", '1800': '2050'].map(convert)
    # extract years and life expectancy
    years = morocco_data.keys()
    morocco_life_expectancy = morocco_data.values
    france_life_expectancy = france_data.values
    # plot data
    plt.plot(years, morocco_life_expectancy, label="Morocco")
    plt.plot(years, france_life_expectancy, label="France")
    # customize graph
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc="lower right")
    plt.xticks(years[::40])
    plt.yticks([20000000, 40000000, 60000000], labels=['20M', '40M', '60M'])

    plt.show()


def main():
    aff_pop("population_total.csv")


if __name__ == "__main__":
    main()
