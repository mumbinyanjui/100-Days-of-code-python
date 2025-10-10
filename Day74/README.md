# Day 74 — Google Trends Data Visualization

## 🎯 Aim

On Day 74, the goal is to fetch, clean, resample, and visualize time-series data using Google Trends. You will practice time series handling in pandas and create insightful visualizations using Matplotlib (or other plotting libraries).

## 📚 Topics Covered

- Converting date strings to `datetime` objects  
- Resampling time series data (e.g. daily → monthly or weekly aggregates)  
- Dealing with missing data / interpolation  
- Plotting time series (line plots, markers, formatting dates)  
- Adjusting tick locators and date formatters  
- Customizing plots: titles, labels, legends, styles  
- Possibly combining multiple time series on one plot for comparison  

## 🧰 Tools & Libraries Used

- `pandas`  
- `matplotlib.pyplot`  
- (Optionally `seaborn`, or other styling libs)  
- (Possibly `pytrends` or other Google Trends client)  
- `datetime` module for date conversion  

## 📝 Suggested Workflow / Steps

1. **Fetch Google Trends data**  
   Use a library (e.g. `pytrends`) or API to request trend data for specific search terms over a date range.  
   
2. **Load into pandas DataFrame**  
   Ensure the index is properly set to a `DatetimeIndex`.

3. **Inspect and clean data**  
   Check for missing values, nulls, outliers. Decide on how to fill or drop them.  
   
4. **Resample / Aggregate**  
   - For example, resample daily data into monthly averages (`.resample('M').mean()`), or weekly sums, etc.  
   - Use functions like `.agg()`, `.groupby()`, `.interpolate()` if needed.  
   
5. **Plot the data**  
   - Create line plots of the original and resampled series.  
   - Format the x-axis to show readable date ticks (e.g. using `DateFormatter`, `AutoDateLocator`)  
   - Add labels, legends, title, grid lines  
   - Optionally overlay multiple time series (e.g. compare two search terms)  

6. **Refine visual aesthetics**  
   - Adjust figure size, colors, line styles, markers  
   - Rotate tick labels if overlapping  
   - Add annotations or highlights if needed  


