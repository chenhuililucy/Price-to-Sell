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
In all cases, if the final price is less than $10^{3}$ or greater than $10^{6}$, the price will be $10^{3}$ and $10^{6}$, respectively. For any square footage, the square foot price is the mean of the prices at that square footage. Return an integer that represents the valuation of the seller's house.
For example, there are $n=6$ houses with area $=[1200,1300,1200,1300,1200,2000]$, price = $[12000,24000,14000,22000,13000,30000]$ and the house to value has reqArea $=1500$ square feet. The following table shows the test for outliers:
To Test
$\begin{array}{lllllll}\text { area/price } & \text { compList } & P_{m} & \sigma & \left|p r i c e-P_{m}\right| & 3 \star \sigma & \text { Is outlier? } \\ 1200 / 12000 & {[14000,13000]} & 13500 & 500 & 1500 & 1500 & \text { False } \\ 1300 / 24000 & {[22000]} & 22000 & 0 & 2000 & 0 & \text { True } \\ 1200 / 14000 & {[12000,13000]} & 12500 & 500 & 1500 & 1500 & \text { False } \\ 1300 / 22000 & {[24000]} & 24000 & 0 & 2000 & 0 & \text { True } \\ 1200 / 13000 & {[12000,14000]} & 13000 & 1000 & 1000 & 3000 & \text { False } \\ 2000 / 30000 & {[]} & \text { NIL } & \text { N/A } & & & \text { False* }\end{array}$
* There is only one house with this area, so it cannot be an outlier.
The 1300 square foot houses are both outliers, so they are discarded. The new arrays are area' $=$ $[1200,1200,1200,2000]$ and price' $=[12000,14000,13000,30000]$. Interpolate the price between the two house sizes remaining. The interpolated price is $13000+(30000-13000) /(2000-1200)$ * $(1500-1200)=19375$
Function Description
Complete the function valuation in the editor below. The function must return the expected price rounded to the nearest integer.
valuation has the following parameter(s):
int reqArea. the area of the seller's house in square feet int area[n]: each value is an area of a house sold in the past int price $[n]$ : price[i] is the price of the $i^{\text {th }}$ house in area[]
Constraints
- $500 \leq$ reqArea $\leq 10^{5}$
- $500 \leq$ area[i] $\leq 10^{5}$ for all $i$ such that $0 \leq i<n$
- $10^{3} \leq$ price[i] $\leq 10^{6}$ for all isuch that $0 \leq i<n$
- $1 \leq n \leq 10^{5}$

