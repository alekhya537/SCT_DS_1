# -*- coding: utf-8 -*-
"""
Week 1 Task: India Population Distribution Analysis
Intern: Your Name
Company: Skillcraft Technology
Date: [Today's Date]
"""

import matplotlib.pyplot as plt

def analyze_population():
    """Analyze and visualize India's population distribution by age groups"""
    
    print("🔍 Analyzing India Population Data...")
    print("=" * 50)
    
    # Dataset from USA Global Population Reports 2022
    age_groups = ['0 to 20 Years', '21 to 44 Years', '45+ Years']
    percentages = [36.1, 57.6, 4.7]
    population_millions = [51.3, 80.7, 98]
    
    # Display analysis
    print(f"📊 Total Population: 1.42 billion")
    print(f"📊 Median Age: 28 years")
    print("\n📈 Age Group Distribution:")
    print("-" * 30)
    
    for i in range(len(age_groups)):
        print(f"   {age_groups[i]}: {percentages[i]}%")
    
    # Create visualization
    create_population_chart(age_groups, percentages)
    
    return age_groups, percentages

def create_population_chart(age_groups, percentages):
    """Create a bar chart visualization"""
    
    # Set up the figure
    plt.figure(figsize=(12, 7))
    
    # Create bars
    bars = plt.bar(age_groups, percentages, 
                   color=['#FF9999', '#66B2FF', '#99FF99'],
                   edgecolor='navy', linewidth=1.5)
    
    # Customize chart
    plt.title('India Population Distribution by Age Groups (2022)', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Age Groups', fontsize=12, fontweight='bold')
    plt.ylabel('Percentage (%)', fontsize=12, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar, value in zip(bars, percentages):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{value}%', ha='center', va='bottom', 
                fontweight='bold', fontsize=11)
    
    # Add footer
    plt.figtext(0.5, 0.01, 
                'Source: USA Global Population Reports 2022 | Skillcraft Internship',
                ha='center', fontsize=9, style='italic')
    
    plt.tight_layout()
    plt.savefig('india_population_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\n✅ Visualization created successfully!")
    print("💾 Chart saved as 'india_population_distribution.png'")

# Run the analysis
if __name__ == "__main__":
    age_groups, percentages = analyze_population()
    
    print("\n" + "=" * 50)
    print("🎯 ANALYSIS COMPLETE!")
    print("=" * 50)
    print("💡 Key Insights:")
    print("   • Young population (21-44) dominates at 57.6%")
    print("   • Only 4.7% of population is above 45 years")
    print("   • India has a very young demographic structure")
