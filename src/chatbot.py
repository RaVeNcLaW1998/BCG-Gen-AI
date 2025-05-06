import dataset


def simple_chatbot(user_query):
    data = dataset.load_data("../data.csv")
    if data is None:
        return "Sorry, I cannot access the financial data at the moment."

    # Handle predefined questions
    if user_query == "What is the total revenue?":
        total = data["Total Revenue"].sum()
        return f"The total revenue across all companies and years is ${total:,.2f}."

    elif user_query == "How has net income changed over the last year?":
        recent = data.sort_values(["Company", "Year"], ascending=[True, False])
        changes = []
        for company in recent["Company"].unique():
            df = recent[recent["Company"] == company].reset_index()
            if len(df) >= 2:
                change = df.loc[0, "Net Income"] - df.loc[1, "Net Income"]
                changes.append(
                    f"{company}: {'increased' if change > 0 else 'decreased'} by ${abs(change):,.2f}"
                )
        return "Net income changes:\n" + "\n".join(changes)

    elif user_query == "What is the average net income per company?":
        avg = data.groupby("Company")["Net Income"].mean().round(2)
        return "\n".join(
            [f"{company}: ${income:,.2f}" for company, income in avg.items()]
        )

    elif user_query == "What year had the highest revenue for each company?":
        result = []
        for company in data["Company"].unique():
            highest = (
                data[data["Company"] == company]
                .sort_values("Total Revenue", ascending=False)
                .iloc[0]
            )
            result.append(
                f"{company}: {int(highest['Year'])} with ${highest['Total Revenue']:,.2f}"
            )
        return "Highest revenue years:\n" + "\n".join(result)

    elif user_query == "What is the debt ratio for each company in the latest year?":
        result = []
        for company in data["Company"].unique():
            latest = (
                data[data["Company"] == company]
                .sort_values("Year", ascending=False)
                .iloc[0]
            )
            ratio = latest["Total Liabilities"] / latest["Total Assets"]
            result.append(
                f"{company} ({int(latest['Year'])}): Debt Ratio = {ratio:.2%}"
            )
        return "Debt ratios (Liabilities / Assets):\n" + "\n".join(result)

    elif user_query == "What is the trend in operating cash flow for Apple?":
        apple = data[data["Company"] == "Apple"].sort_values("Year")
        trend = "\n".join(
            [
                f"{int(row['Year'])}: ${row['Cash Flow from Operating Activities']:,.2f}"
                for _, row in apple.iterrows()
            ]
        )
        return "Apple Cash Flow from Operating Activities:\n" + trend

    elif user_query.startswith("Show me financials for"):
        parts = user_query.split()
        if len(parts) >= 6:
            company = parts[4]
            try:
                year = int(parts[5])
            except ValueError:
                return "Year must be a number."
            row = data[
                (data["Company"].str.lower() == company.lower())
                & (data["Year"] == year)
            ]
            if not row.empty:
                r = row.iloc[0]
                return (
                    f"Financials for {company} in {year}:\n"
                    f"Revenue: ${r['Total Revenue']:,.2f}\n"
                    f"Net Income: ${r['Net Income']:,.2f}\n"
                    f"Assets: ${r['Total Assets']:,.2f}\n"
                    f"Liabilities: ${r['Total Liabilities']:,.2f}\n"
                    f"Cash Flow: ${r['Cash Flow from Operating Activities']:,.2f}"
                )
            else:
                return f"No financial data found for {company} in {year}."
        else:
            return "To get financials, use: Show me financials for [Company] [Year]"

    elif user_query == "What is the current stock price?":
        return "The current stock price is [not available in this dataset]."

    else:
        return "Sorry, I can only provide information on predefined queries."


# Run chatbot in loop
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = simple_chatbot(user_input)
        print(f"Chatbot: {response}")
