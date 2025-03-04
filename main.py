import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: Set a style for better visuals
sns.set(style="whitegrid")


mode = 5


# Load the CSV file with semicolon as the separator
df = pd.read_csv('bank-full.csv', sep=';')


if mode == 1:
    # Check the first few rows to make sure it loaded correctly
    print(df.head())

elif mode == 2:
    # Check the basic info about the data
    print(df.info())

elif mode == 3:
    # Get descriptive statistics for numerical columns
    print(df.describe())

elif mode == 4:
    # Check for missing values
    print(df.isnull().sum())

elif mode == 5:
    # Average Balance by Job
    average_balance = df.groupby('job')['balance'].mean().sort_values(ascending=False)
    print(average_balance)
    
    # Visualization
    plt.figure(figsize=(10, 6))
    sns.barplot(x=average_balance.values, y=average_balance.index, palette='viridis')
    plt.title('Average Balance by Job Type')
    plt.xlabel('How much usless money we agreed to give them') # Average Balance
    plt.ylabel('Slave Type') # Job Type
    plt.tight_layout()
    plt.show()

elif mode == 6:
    # Marital Status Distribution
    marital_distribution = df['marital'].value_counts()
    print(marital_distribution)
    
    # Visualization
    plt.figure(figsize=(8, 6))
    plt.pie(marital_distribution, labels=marital_distribution.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
    plt.title('Marital Status Distribution')
    plt.axis('equal')  # Ensures pie is drawn as a circle.
    plt.show()

elif mode == 7:
    # Campaign Success Rate
    campaign_success_rate = df['y'].value_counts(normalize=True) * 100
    print(campaign_success_rate)
    
    # Visualization
    plt.figure(figsize=(6, 4))
    sns.barplot(x=campaign_success_rate.index, y=campaign_success_rate.values, palette='coolwarm')
    plt.title('Campaign Success Rate')
    plt.xlabel('Campaign Outcome')
    plt.ylabel('Percentage (%)')
    plt.show()

elif mode == 8:
    # Filter the Data by Gender and Marital Status
    single_data = df[(df['marital'] == 'single')]
    married_data = df[(df['marital'] == 'married')]

    # Calculate average balance for single vs married
    average_balance_single = single_data['balance'].mean()
    average_balance_married = married_data['balance'].mean()

    print(f"Average Balance for Single People: {average_balance_single:.2f}")
    print(f"Average Balance for Married People: {average_balance_married:.2f}")

    # Example: Average balance by marital status and housing ownership
    balance_by_status_and_housing = df.groupby(['marital', 'housing'])['balance'].mean()
    print("Balance by status and housing: ",balance_by_status_and_housing)

    # Prepare data for visualization
    balance_comparison = {
        'Marital Status': ['Single', 'Married'],
        'Average Balance': [average_balance_single, average_balance_married]
    }

    # Create a DataFrame for visualization
    df_balance_comparison = pd.DataFrame(balance_comparison)

    # Plot the data
    plt.figure(figsize=(6, 4))
    sns.barplot(x='Marital Status', y='Average Balance', data=df_balance_comparison, palette='Set2')
    plt.title('Average Bank Balance: Single vs. Married')
    plt.xlabel('Marital Status')
    plt.ylabel('Average Balance')
    plt.show()

    
