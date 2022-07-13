# Price-to-Sell
Solution to Hackerrank Problem Price to Sell

A real estate agent is advising a seller on the price to ask for a home. To do this, the agent will look at homes that have sold in the area and base the valuation on this data. The only factors that will be considered are square footage and sale price.

The agent starts by removing any outliers from the list of comparable homes. To determine the outliers:
- Select the home to test.
- Create a list of prices of other homes of the same size. It will be called compList in the examples.
- If there are no other homes of the same size, the house being tested is not an outlier.
- Otherwise:
- Calculate the mean price, $P_{m}$, and the standard deviation, $\sigma$, for the homes complist.
- If $\mid$ price[i] $-P_{m} \mid>3^{*} \sigma$, the house is an outlier.
The valuation is then calculated against the resulting list using the following rules:
- If there are no houses in the list, use 1000 per square foot as the price.
- If there is only 1 house in the list, its square foot price is used.
- If there are 1 or more houses in the list with the exact square footage of the house to price, use the mean of those prices.
- If the required square footage is between the square footage of two houses in the list, interpolate the square foot price using the means of the closest higher and lower-priced homes.
- If the required square footage is outside of the range of houses listed, extrapolate the price based on the means of the two square footage values that are closest to the home to value.
In all cases, if the final price is less than $10^{3}$ or greater than $10^{6}$, the price will be $10^{3}$ and $10^{6}$, respectively. 





