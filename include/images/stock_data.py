import yfinance as yf
import pickle

tsla = yf.Ticker('TSLA')
print(tsla.quarterly_financials)
# Check if there are any recommendations
# if "To Grade" in tsla.recommendations:
#     to_grade_counts = tsla.recommendations["To Grade"].value_counts()

#     # Check if there are any values in the series
#     if not to_grade_counts.empty:
#         # Access the first element
#         print(to_grade_counts.keys()[0])
#     else:
#         print("No recommendations available.")
# else:
#     print("No 'To Grade' column in recommendations.")