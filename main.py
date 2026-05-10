def main():

    # Load datasets
    try:
        data1_raw, data2_raw = load_data()

    except FileNotFoundError:
        print("Error: CSV files not found")
        return

    # Clean both datasets
    d1_cleaned = clean_data1(data1_raw)
    d2_cleaned = clean_data2(data2_raw)

    # Merge datasets for analysis and forecasting
    df_raw = pd.concat(
        [d2_cleaned, d1_cleaned],
        axis=0
    ).reset_index(drop=True)

    # Clean energy type values
    df_raw['Type (solar/ wind)'] = (
        df_raw['Type (solar/ wind)']
        .astype(str)
        .str.replace(' energy', '', case=False, regex=False)
        .str.strip()
        .str.title()
    )

    # Clean project status values
    df_raw['Installed / Planned'] = (
        df_raw['Installed / Planned']
        .astype(str)
        .str.strip()
        .str.title()
    )

    # Remove duplicate rows
    df_raw = df_raw.drop_duplicates(
        subset=[
            'Type (solar/ wind)',
            'Year',
            'Capacity',
            'City'
        ]
    )

    # Print forecast phase title
    print("Building Trend Forecast Model")

    print(
        "Forecast model uses Year → Cumulative Capacity "
        "without random train/test split."
    )

    # Print visualization phase title
    print("Generating Charts")

    # Plot yearly renewable energy growth
    plot_yearly_growth(df_raw)

    # Plot solar and wind comparison
    plot_solar_vs_wind(df_raw)

    # Plot renewable energy distribution by region
    plot_regional_distribution(df_raw)

    # Generate renewable energy forecast
    future_2030, vision_target, trend_fit, yearly, slope = plot_forecast(
        df_raw,
        forecast_until=2030
    )

    # Evaluate forecast results
    evaluate_forecast(
        future_2030=future_2030,
        vision_target=vision_target,
        trend_fit=trend_fit,
        yearly=yearly,
        slope=slope
    )

if __name__ == "__main__":
    main()
