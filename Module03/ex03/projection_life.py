from load_csv import load
import matplotlib.pyplot as plt


def projection_life() -> None:
    """Shows a graph of correlation between life expectancy
    and income per person in 1900
    """
    # Load the csv files
    life_df = load("life_expectancy_years.csv")
    ipp_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    # Select the columns we want
    # "1900" to handle, "country" to merge
    life_1900 = life_df[["country", "1900"]]
    ipp_1900 = ipp_df[["country", "1900"]]

    # Merge life_1900 and ipp_1900 into a single dataframe
    # on the "country" column
    merged = life_1900.merge(ipp_1900, on='country')

    # Rename columns
    merged.columns = ["country", "life", "ipp"]

    # Use scatter to plot data as dots
    # x: Column to use for the x axis values
    # y: Column to use for the y axis values
    ax = merged.plot.scatter(
        x="ipp", y="life",
        title='1900', xlabel="Gross domestic product",
        ylabel='Life Expectancy')

    # Set the x axis to a logarithmic scale
    ax.set_xscale('log')

    # Replace the x axis ticks with 300, 1000, 10000
    # and label them as "300", "1k", "10k"
    ax.set_xticks([300, 1000, 10000], labels=["300", "1k", "10k"])

    # Show the plot
    plt.show()


def main():
    projection_life()


if __name__ == "__main__":
    main()
