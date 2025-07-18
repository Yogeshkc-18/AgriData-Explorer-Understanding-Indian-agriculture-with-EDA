#import required libaries


import pandas as pd
import psycopg2 
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
#load the data
agri_data = pd.read_csv("C:/Users/Yokesh/AgriData-Explorer-Understanding-Indian-agriculture-with-EDA/ICRISAT-District Level Data - ICRISAT-District Level Data.csv")

print(agri_data)


#check the null values 

agri_data.info()

#check the data types

agri_data.dtypes



#required columns clean to the dataset

required_columns = ['Dist Code','Year','State Code','State Name',	'Dist Name','RICE AREA (1000 ha)','RICE PRODUCTION (1000 tons)',
              'RICE YIELD (Kg per ha)','WHEAT AREA (1000 ha)','WHEAT PRODUCTION (1000 tons)','WHEAT YIELD (Kg per ha)',
              'KHARIF SORGHUM AREA (1000 ha)','KHARIF SORGHUM PRODUCTION (1000 tons)','KHARIF SORGHUM YIELD (Kg per ha)',
              'RABI SORGHUM AREA (1000 ha)','RABI SORGHUM PRODUCTION (1000 tons)','RABI SORGHUM YIELD (Kg per ha)','SORGHUM AREA (1000 ha)',
              'SORGHUM PRODUCTION (1000 tons)','SORGHUM YIELD (Kg per ha)','PEARL MILLET AREA (1000 ha)','PEARL MILLET PRODUCTION (1000 tons)',
              'PEARL MILLET YIELD (Kg per ha)','MAIZE AREA (1000 ha)','MAIZE PRODUCTION (1000 tons)','MAIZE YIELD (Kg per ha)',
              'FINGER MILLET AREA (1000 ha)','FINGER MILLET PRODUCTION (1000 tons)','FINGER MILLET YIELD (Kg per ha)','BARLEY AREA (1000 ha)',
              'BARLEY PRODUCTION (1000 tons)','BARLEY YIELD (Kg per ha)','GROUNDNUT AREA (1000 ha)','GROUNDNUT PRODUCTION (1000 tons)','GROUNDNUT YIELD (Kg per ha)',
              'SUNFLOWER AREA (1000 ha)','SUNFLOWER PRODUCTION (1000 tons)','SUNFLOWER YIELD (Kg per ha)','SOYABEAN AREA (1000 ha)',
              'SOYABEAN PRODUCTION (1000 tons)','SOYABEAN YIELD (Kg per ha)','OILSEEDS AREA (1000 ha)','OILSEEDS PRODUCTION (1000 tons)',
              'OILSEEDS YIELD (Kg per ha)','SUGARCANE AREA (1000 ha)','SUGARCANE PRODUCTION (1000 tons)','SUGARCANE YIELD (Kg per ha)',
        	  'COTTON AREA (1000 ha)','COTTON PRODUCTION (1000 tons)','COTTON YIELD (Kg per ha)'
]

filtered_agri_data = agri_data[required_columns]

print(filtered_agri_data)

# storing to the csv file filtered data

filtered_agri_data.to_csv("filtered_agriculture_data.csv", index=False)


# #2 PostgreSQL connection details
# username = 'postgres'
# password = '9791243162'
# host = 'localhost'  # or your remote host IP
# port = '5432'       # default PostgreSQL port
# database = 'agriculture_database'

# #3 Create SQLAlchemy connection string
# engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

# # 4 Load the data into PostgreSQL table
# table_name = 'Agri_data'  # you can name it anything
# filtered_agri_data.to_sql(table_name, engine, if_exists='replace', index=False)

# print("✅ Data uploaded to PostgreSQL successfully.")


#---------------------------------------------------------------------------------------------------------------------------------------------
# eda

# 1.Group by state and calculate total rice production
top_rice_states = (
    filtered_agri_data.groupby("State Name")["RICE PRODUCTION (1000 tons)"]
    .sum()
    .sort_values(ascending=False)
    .head(7)
)

# Plotting
plt.figure(figsize=(10, 6))
top_rice_states.plot(kind="bar", color="Green")
plt.title("Top 7 Rice Producing States in India")
plt.ylabel("Rice Production (1000 tons)")
plt.xlabel("State")
plt.xticks(rotation=0)
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("top_7rice_state_1.png",transparent=True)
# Show the chart
plt.show()
#------------------------------------------------------------------------------------------------------------------------------------------------

# 2.Top 5 wheat producing states
top_wheat_states = (
    filtered_agri_data.groupby("State Name")["WHEAT PRODUCTION (1000 tons)"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Create bar chart and pie chart
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Bar chart
top_wheat_states.plot(kind="bar", ax=axes[0], color="sienna")
axes[0].set_title("Top 5 Wheat Producing States in India")
axes[0].set_ylabel("Wheat Production (1000 tons)")
axes[0].set_xlabel("State")
axes[0].tick_params(axis='x', rotation=0)

# Pie chart
top_wheat_states_percent = top_wheat_states / top_wheat_states.sum() * 100
axes[1].pie(top_wheat_states_percent, labels=top_wheat_states.index, autopct="%1.1f%%", startangle=140)
axes[1].set_title("Production Share of Top 5 Wheat States")

plt.tight_layout()
plt.savefig("top5 state of wheat production_2.png",transparent=True)
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------
#3. oil seed production top 5 states

oilseed_production = filtered_agri_data.groupby("State Name")["OILSEEDS PRODUCTION (1000 tons)"].sum()

# Get top 5 states
top5_oilseed_states = oilseed_production.sort_values(ascending=False).head(5)

# Plot
plt.figure(figsize=(10, 6))
top5_oilseed_states.plot(kind='bar', color='olive')
plt.title('Top 5 Oilseed Producing States in India')
plt.xlabel('State')
plt.ylabel('Total Oilseed Production (1000 tons)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("oil seed top5 states_3.png",transparent=True)
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------
#4. top 7 sunflower production state
sunflower_production = filtered_agri_data.groupby("State Name")["SUNFLOWER PRODUCTION (1000 tons)"].sum()

# Get top 7 states
top7_sunflower_states = sunflower_production.sort_values(ascending=False).head(7)

# Plot
plt.figure(figsize=(10, 6))
top7_sunflower_states.plot(kind='bar', color='goldenrod')
plt.title('Top 7 Sunflower Producing States in India')
plt.xlabel('State')
plt.ylabel('Total Sunflower Production (1000 tons)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("top 7 sunflower production_4.png",transparent=True)
plt.show()
#-----------------------------------------------------------------------------------------------------------------------------------------------

#5. India sugarcane production last 50 years

sugarcane_by_year = filtered_agri_data.groupby("Year")["SUGARCANE PRODUCTION (1000 tons)"].sum()

# Filter last 50 years of data (adjust based on dataset range)
sugarcane_last50 = sugarcane_by_year.tail(50)

# Plot
plt.figure(figsize=(12, 6))
plt.plot(sugarcane_last50.index, sugarcane_last50.values, marker='o', color='darkgreen', linestyle='-')
plt.title("India's Sugarcane Production (Last 50 Years)")
plt.xlabel("Year")
plt.ylabel("Sugarcane Production (1000 tons)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("india sugarcane production_5.png",transparent=True)
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------
#6. rice production and wheat production last 50 year

production_by_year = filtered_agri_data.groupby("Year")[
    ["RICE PRODUCTION (1000 tons)", "WHEAT PRODUCTION (1000 tons)"]
].sum()

# Get the last 50 years of data (sorted by year)
production_last50 = production_by_year.sort_index().tail(50)

# Plot
plt.figure(figsize=(12, 6))
plt.plot(production_last50.index, production_last50["RICE PRODUCTION (1000 tons)"], label='Rice', color='green', marker='o')
plt.plot(production_last50.index, production_last50["WHEAT PRODUCTION (1000 tons)"], label='Wheat', color='orange', marker='s')

plt.title("Rice vs Wheat Production in India (Last 50 Years)")
plt.xlabel("Year")
plt.ylabel("Production (1000 tons)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("rice vs wheat production last 50 years_6.png",transparent=True)
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------
#7.Rice production by west bengal districts


wb_rice = filtered_agri_data[filtered_agri_data["State Name"] == "West Bengal"]

# Group by district and sum rice production
wb_districts_rice = wb_rice.groupby("Dist Name")["RICE PRODUCTION (1000 tons)"].sum().sort_values(ascending=False)
wb_rice_df = wb_districts_rice.to_frame().T  # Transpose for heatmap (1 row, many columns)

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 9), gridspec_kw={'height_ratios': [2, 1]})

#  Bar Chart - Rice Production by District
wb_districts_rice.plot(kind='bar', color='mediumseagreen', ax=ax1, legend=False)
ax1.set_title(" District-wise Rice Production in West Bengal", fontsize=14, fontweight='bold')
ax1.set_ylabel("Production (1000 tons)")
ax1.set_xlabel("")
ax1.set_xticklabels(wb_districts_rice.index, rotation=0, ha='right')
ax1.grid(axis='y', linestyle='--', alpha=0.5)

#  Heatmap - District-wise Rice Production (Single Row)
sns.heatmap(wb_rice_df, cmap="coolwarm", annot=True, fmt=".0f", linewidths=0.4, cbar=True,
            ax=ax2, xticklabels=True, yticklabels=["Production (1000 tons)"])
ax2.set_title(" Heatmap Overview: Rice Production by District", fontsize=13, fontweight='bold')
ax2.tick_params(axis='x', labelrotation=0)

# Layout adjustment
plt.tight_layout(pad=2)
plt.savefig("rice production by west bengal_7.png",transparent=True)
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------
# 8.top 10 wheat production years from up

# Filter data for Uttar Pradesh
up_wheat = filtered_agri_data[filtered_agri_data["State Name"] == "Uttar Pradesh"]

# Group by year and sum wheat production
up_wheat_yearly = up_wheat.groupby("Year")["WHEAT PRODUCTION (1000 tons)"].sum()

# Get top 10 years by wheat production
top10_years = up_wheat_yearly.sort_values(ascending=False).head(10).sort_index()

# Plot
plt.figure(figsize=(10, 6))
top10_years.plot(kind='bar', color='brown')
plt.title("Top 10 Wheat Production Years in Uttar Pradesh")
plt.xlabel("Year")
plt.ylabel("Wheat Production (1000 tons)")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("top 10 wheat production from up_8.png",transparent=True)
plt.show()

#-------------------------------------------------------------------------------------------------------------------------------------------------
#9. millet production last 50 year
filtered_agri_data = filtered_agri_data.copy()

#  Create "Total Millet Production" safely with .loc[]
filtered_agri_data.loc[:, "Total Millet Production"] = (
    filtered_agri_data["PEARL MILLET PRODUCTION (1000 tons)"] +
    filtered_agri_data["FINGER MILLET PRODUCTION (1000 tons)"]
)

#  Group by year and calculate total millet production
millet_by_year = (
    filtered_agri_data.groupby("Year")["Total Millet Production"]
    .sum()
    .sort_index()
)

#  Get last 50 years
millet_last50 = millet_by_year.tail(50)

#  Plot a line chart
plt.figure(figsize=(12, 6))
plt.plot(millet_last50.index, millet_last50.values, marker='o', color='purple')
plt.title("Millet Production in India (Last 50 Years)")
plt.xlabel("Year")
plt.ylabel("Total Millet Production (1000 tons)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("millet_line_last_50_years_9.png",transparent=True)
plt.show()

#-------------------------------------------------------------------------------------------------------------------------------------------------
#10.sorghum production (kharif and rabi) by region

kr_pro = filtered_agri_data.groupby("State Name")[[
    "KHARIF SORGHUM PRODUCTION (1000 tons)",
    "RABI SORGHUM PRODUCTION (1000 tons)"
]].sum().head(10)  # Top 10 states

# Plot
kr_pro.plot(kind='bar', figsize=(10, 6), color=['orange', 'blue'])
plt.title("Kharif vs Rabi Sorghum Production by State")
plt.ylabel("Production (1000 tons)")
plt.xticks()
plt.tight_layout()
plt.savefig("sorghum_kharif_rabi_simple_bar_10.png",transparent=True)
plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------

#11. Top 7 States for Groundnut Production

# Group by state and get total groundnut production
top_groundnut = (
    filtered_agri_data.groupby("State Name")["GROUNDNUT PRODUCTION (1000 tons)"]
    .sum()
    .sort_values(ascending=True)  # Sort ascending for horizontal bar
    .tail(7)  # Get top 7
)

# Plot horizontal bar chart
plt.figure(figsize=(10, 6))
top_groundnut.plot(kind='barh', color='peru', edgecolor='black')
plt.title("Top 7 Groundnut Producing States in India", fontsize=14)
plt.xlabel("Total Groundnut Production (1000 tons)")
plt.ylabel("State Name")
plt.tight_layout()
plt.savefig("top_7_groundnut_production_horizontal_bar_11.png",transparent=True)
plt.show()
#------------------------------------------------------------------------------------------------------------------------------------------------

#12.Soybean production by top 5 states and yield efficiency

#  Group by state and calculate total production & area
grouped = filtered_agri_data.groupby("State Name")[["SOYABEAN PRODUCTION (1000 tons)", "SOYABEAN AREA (1000 ha)"]].sum()

#  Calculate yield efficiency (tons per hectare)
grouped["Yield Efficiency"] = grouped["SOYABEAN PRODUCTION (1000 tons)"] / grouped["SOYABEAN AREA (1000 ha)"]

#  Select Top 5 states by production
top5 = grouped.sort_values("SOYABEAN PRODUCTION (1000 tons)", ascending=False).head(5)

#  Create Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(
    top5["Yield Efficiency"],                      # X-axis: efficiency
    top5["SOYABEAN PRODUCTION (1000 tons)"],       # Y-axis: production
    color='green', s=100                           # Color and size
)

#  Add state labels next to each point
for state in top5.index:
    x = top5.loc[state, "Yield Efficiency"]
    y = top5.loc[state, "SOYABEAN PRODUCTION (1000 tons)"]
    plt.text(x + 0.01, y, state, fontsize=9)

#  Add titles and labels
plt.title("Top 5 Soybean Producing States (Scatter Plot)")
plt.xlabel("Yield Efficiency (tons per hectare)")
plt.ylabel("Production (1000 tons)")
plt.grid(True)
plt.tight_layout()
plt.savefig("soyebean_production_top5states_12.png",transparent=True)
plt.show()
#-----------------------------------------------------------------------------------------------------------------------------------------------
#13. oilseed production in major states

# Group by State and sum total oilseed production
oilseed_data = filtered_agri_data.groupby("State Name")["OILSEEDS PRODUCTION (1000 tons)"].sum().reset_index()

# Sort and filter top producers (e.g., top 10 states)
top_states = oilseed_data.sort_values(by="OILSEEDS PRODUCTION (1000 tons)", ascending=False).head(10)

# Set state name as index to form matrix (for heatmap)
heatmap_data = top_states.set_index("State Name")

# Plotting the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", fmt=".1f", linewidths=0.5)

plt.title("Heatmap: Total Oilseed Production in Major Indian States")
plt.xlabel("Oilseed Metric")
plt.ylabel("State")
plt.tight_layout()
plt.savefig("oilseed_production_states_13.png",transparent=True)
plt.show()

#----------------------------------
#14.Impact of Area cultivated on production(Rice,Wheat,Maize)

# Group by state and sum area and production
grouped = filtered_agri_data.groupby("State Name")[[
    "RICE AREA (1000 ha)", "RICE PRODUCTION (1000 tons)",
    "WHEAT AREA (1000 ha)", "WHEAT PRODUCTION (1000 tons)",
    "MAIZE AREA (1000 ha)", "MAIZE PRODUCTION (1000 tons)"
]].sum()

# Plotting scatter plots
plt.figure(figsize=(10, 7))

# Rice
plt.scatter(grouped["RICE AREA (1000 ha)"], grouped["RICE PRODUCTION (1000 tons)"], 
            color='green', label='Rice', s=60)

# Wheat
plt.scatter(grouped["WHEAT AREA (1000 ha)"], grouped["WHEAT PRODUCTION (1000 tons)"], 
            color='blue', label='Wheat', s=60)

# Maize
plt.scatter(grouped["MAIZE AREA (1000 ha)"], grouped["MAIZE PRODUCTION (1000 tons)"], 
            color='orange', label='Maize', s=60)

# Labels and legend
plt.xlabel("Area Cultivated (1000 hectares)")
plt.ylabel("Production (1000 tons)")
plt.title("Impact of Area Cultivated on Production (Rice, Wheat, Maize)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("rice_wheat_maize_14.png",transparent=True)
plt.show()
#--------------------------------------------------------------------------------------------------------------------------------------------------

#15.Rice vs Wheat Yield Across States

# Calculate rice and wheat yield (tons per hectare)
filtered_agri_data["Rice_Yield"] = filtered_agri_data["RICE PRODUCTION (1000 tons)"] * 1000 / (filtered_agri_data["RICE AREA (1000 ha)"] * 1000)
filtered_agri_data["Wheat_Yield"] = filtered_agri_data["WHEAT PRODUCTION (1000 tons)"] * 1000 / (filtered_agri_data["WHEAT AREA (1000 ha)"] * 1000)

# Group by state and calculate average yields
yield_by_state = filtered_agri_data.groupby("State Name")[["Rice_Yield", "Wheat_Yield"]].mean()

# Compute correlation matrix
corr_matrix = yield_by_state.corr()

# Plot heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", square=True,
            linewidths=0.5, linecolor='gray')
plt.title("Correlation between Rice and Wheat Yields Across States")
plt.tight_layout()
plt.savefig("rice_wheat_states_15.png",transparent=True)
plt.show()
