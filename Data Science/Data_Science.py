import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Correct import for pyplot
import seaborn as sns

# Load the data
train = pd.read_csv('titanic_train.csv')

# Create a heatmap to visualize missing values
# sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap="viridis")

# # Show the plot
# plt.show()


# sns.set_style("whitegrid")
# sns.countplot(x='Sex',hue ='Sex',data = train,palette='RdBu_r')
# plt.show()



# sns.set_style("whitegrid")
# sns.countplot(x='Sex',hue ='Pclass',data = train,palette='rainbow')
# plt.show()




# sns.distplot(train['Age'].dropna(),kde='True',color='darkred',bins=40)
# plt.show()

# check for siblings

# sns.countplot(x='SibSp',data = train)
# plt.show()

sns.boxenplot(x='Pclass',y='Age' ,data = train)
plt.show()




    