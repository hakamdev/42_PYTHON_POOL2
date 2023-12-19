from load_csv import load
import matplotlib.pyplot as plt


def convert(val):
    multiplier = val[-1].lower()
    if multiplier == 'm':
        return float(val[:-1]) * 1000000
    elif multiplier == 'k':
        return float(val[:-1]) * 1000
    else:
        return float(val)


def aff_pop(path: str) -> None:
    """Shows a graph of population in Morocco vs France from 1800 to 2050
    Args:
        path: path to the csv file
    """
    # Load the csv file
    df = load(path)
    if (df is None):
        return None
    # Set the country column as index
    df.set_index("country", inplace=True)
    # Get the Morocco and France data and transpose it
    morocco_vs_france = df.loc[['Morocco', 'France'], '1800': '2050']

    # Convert the string values (20M, 20k...) to float
    m_vs_f_converted = morocco_vs_france.map(convert)

    # Transpose the data and plot the graph,
    ax = m_vs_f_converted.T.plot(
        title='Population Projections',
        xlabel="Year",
        ylabel='Population')

    # Change the y axis labels back to M and K
    ax.set_yticks([20000000, 40000000, 60000000], labels=['20M', '40M', '60M'])

    # Show the graph
    plt.show()


def main():
    aff_pop("population_total.csv")


if __name__ == "__main__":
    main()
