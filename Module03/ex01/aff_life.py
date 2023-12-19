from load_csv import load
import matplotlib.pyplot as plt


def aff_life(path: str) -> None:
    """Shows a graph of life expectancy in Morocco from 1800 to 2100
    Args:
        path: path to the csv file
    """
    # Load the csv file
    df = load(path)
    if (df is None):
        return None
    # Set the country column as index
    df.set_index("country", inplace=True)
    # Get the Morocco data and transpose it
    morocco_data = df.loc['Morocco'].T
    # Plot the graph
    morocco_data.plot(
        title='Morocco life expectancy projections',
        xlabel="Year",
        ylabel='Life Expectancy')
    plt.show()


def main():
    aff_life("life_expectancy_years.csv")


if __name__ == "__main__":
    main()
