# CongressTradesPBI
A detailed analysis of trades made by members of US Congress using all parts of the data analysis pipeline including data preprocessing, cleaning, analysis, and visualization with PowerBI.

# Overview
This project presents a comprehensive analysis of stock trading activities by members of the U.S. Congress and Senate. The dashboard, built using Power BI, aims to uncover key insights and patterns in the trading behavior of legislators, providing a high-level summary of total trades, trades by party, excess returns, and more.

## Key Features
* Total Number of Trades: Displays the overall count of stock trades analyzed.
* Trades by Party: Visual representation of the percentage of trades conducted by Republicans, Democrats, and Independents.
* Trades by Chamber: Distribution of trades between the House and Senate.
* Average Excess Return by Party: Comparison of average excess returns for each political party.
* Significant Findings: Highlight of notable trades, such as Senator Sheldon Whitehouse's 13,240% excess return on an NVDA stock purchase.
* Trade Activity Over Time: Trend analysis of trading activity over the years.
* Top Traded Tickers: Identification of the most frequently traded stocks.
* Interactive Elements: Slicers and filters for dynamic exploration of the data.
* To find updated data and export yourself visit Quiverquant.com

# Data Preprocessing:

In our original dataset pulled from Quiver Quantitative there are a number of missing values and edits that we needed to make to ensure a smooth analysis and usable dataset. Firstly, I converted the 'Traded' and 'Filed' columns to a datetime format so that we could accurately use it for time analysis. Then, as you can see in the original dataset, the trade size column uses ranges to represent unspecified trade sizes, which does not lend itself well to numerical analysis. To remedy this I created another column while retaining the original that creates a single midpoint for the rows which include the range. Lastly, to address the missing values without losing their corresponding rows I sweep the dataset (excluding ['excess_return', 'last_modified', 'Traded', 'Filed']) and fill in our missing text values with 'NA'. Now I have a consise, useable dataset. 

# Dashboard:

![1717357881889-a50656d5-a99f-4360-9618-c32e032225afTrades_1](https://github.com/CameronCMaples/CongressTradesPBI/assets/78427260/5558627c-0fbb-4505-9e39-7d69c0c42575)


