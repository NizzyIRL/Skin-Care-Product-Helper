print("Welcome to the IPI's Product Recommender!")
print("What skin condition do you need help with? (you can choose multiple conditions):")
print("1. Dry skin")
print("2. Oily skin")
print("3. Sensitive skin")
print("4. Acne or blemishes")
print("5. Wrinkles or fine lines")
print("6. Dark spots or hyperpigmentation")
print("7. Redness or irritation")
print("8. None of the above")

# Define the recommendations dictionary
recommendations = {
    1: ["- Dr. Wong's Moisturizer with Hyaluronic Acid",
        "- Dr. Wong's Nourishing Body Lotion with Aloe Vera",
        "- Dr. Wong's Hydrating Face Mask"],
    2: ["- Dr.Wong's Oil-Free Moisturizer",
        "- Dr. Wong's Clay Mask for Oily Skin",
        "- Dr. Wong's Mattifying Primer"],
    3: ["- Dr. Wong's Fragrance-Free Gentle Cleanser",
        "- Dr. Wong's Soothing Aloe Vera Gel",
        "- Dr. Wong's Hypoallergenic Moisturizer"],
    4: ["- Dr. Wong's Acne Treatment Gel with Benzoyl Peroxide",
        "- Dr. Wong's Salicylic Acid Cleanser",
        "- Dr. Wong's Tea Tree Oil Spot Treatment"],
    5: ["- Dr. Wong's Retinol Night Cream",
        "- Dr. Wong's Vitamin C Serum",
        "- Dr. Wong's Anti-Aging Eye Cream"],
    6: ["- Dr. Wong's Brightening Serum with Niacinamide",
        "- Dr. Wong's Vitamin C & E Serum",
        "- Dr. Wong's SPF 50+ Sunscreen"],
    7: ["- Dr. Wong's Calming Gel with Chamomile",
        "- Dr. Wong's Redness Relief Cream",
        "- Dr. Wong's Anti-Inflammatory Hydrating Serum"]
}

# List to store user selections
selected_conditions = []

# Loop for user input
while True:
    try:
        condition = int(input("Enter the number corresponding to a skin condition (or 0 to stop): "))
        if condition == 0:
            break
        elif 1 <= condition <= 8:
            if condition not in selected_conditions:
                selected_conditions.append(condition)
                print("Condition added.")
            else:
                print("You already selected this condition.")
        else:
            print("Invalid option. Please select a number between 1 and 8.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Display recommendations after selection
if selected_conditions:
    print("\nThank you for your input! Based on your selections, we recommend the following products:")
    for condition in selected_conditions:
        print(f"\nFor condition {condition}:")
        for product in recommendations.get(condition, []):
            print(product)
else:
    print("\nNo conditions selected. Consider a general skincare routine.")

print("\nThank you for choosing IPI!")