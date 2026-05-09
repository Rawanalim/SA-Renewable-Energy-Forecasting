# Forecast Evaluation Function

# Define forecast evaluation function
def evaluate_forecast(

    # Predicted renewable capacity in 2030
    future_2030,
    
    # Vision 2030 renewable target
    vision_target,

    # R² trend fitting score
    trend_fit,

    # Yearly renewable capacity table
    yearly,

    # Estimated yearly renewable growth
    slope ):

    # Function description
    """
    Evaluate renewable energy forecast results.
    """

    # Calculate achievement percentage

    # Divide predicted capacity by Vision target
    achievement_rate = (

        # Predicted future renewable capacity
        future_2030

        # Divide by target capacity
        / vision_target

    # Convert to percentage
    ) * 100

    # Remaining MW needed to reach Vision target
    gap = vision_target - future_2030

    # Print evaluation title
    print("\nForecast Evaluation")

    # Print separator line
    print("-" * 35)

    # Display predicted renewable capacity
    print(f"Predicted capacity in 2030: {future_2030:,.0f} MW")

    # Display Vision 2030 target value
    print(f"Vision 2030 target: {vision_target:,.0f} MW")

    # Display target achievement percentage
    print(f"Achievement rate: {achievement_rate:.2f}%")

    # Display remaining MW gap
    print(f"Gap from Vision 2030 target: {gap:,.0f} MW")

    # Display R² score
    print(f"Trend Fit (R²): {trend_fit:.2f}")

    # Print yearly growth estimate

    # Display estimated yearly growth
    print(f"Estimated yearly growth: {slope:,.0f} MW/year")


    # Display interpretation title
    print("\nForecast Interpretation:")

    # Explain model behavior
    print("The model uses historical renewable energy growth to estimate future cumulative capacity.")

    # Explain limited historical data issue
    print("This forecast is approximate because it is based on limited historical data.")

    # Find strongest growth year

    # Get year with maximum added capacity
    best_year = yearly.loc[

        # Locate row with maximum capacity value
        yearly['Capacity'].idxmax(),

        # Select year column
        'Year'
    ]

    # Find strongest growth value
    best_val = yearly.loc[

        # Locate row with maximum capacity value
        yearly['Capacity'].idxmax(),

        # Select capacity column
        'Capacity'
    ]

    # Display strongest growth year
    print(f"Highest annual growth occurred in {best_year} with {best_val:,.0f} MW added.")

    # Check if target gap still exists
    if gap > 0:

        # Print below-target conclusion
        print(f"\nSaudi Arabia may remain approximately {gap:,.0f} MW below the Vision 2030 target."
        )

    # Otherwise target is reached
    else:

        # Print target achievement conclusion
        print("\nSaudi Arabia is projected to meet or exceed the Vision 2030 target.")

    # Return evaluation metrics

    # Return evaluation metrics
    return {

        # Store predicted capacity
        "predicted_2030": future_2030,

        # Store Vision target
        "vision_target": vision_target,

        # Store achievement percentage
        "achievement_rate": achievement_rate,

        # Store remaining gap
        "gap": gap,

        # Store trend fitting score
        "trend_fit": trend_fit,

        # Store yearly growth estimate
        "slope": slope
    }
