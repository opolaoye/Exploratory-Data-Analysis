# coding: utf-8

# Data Exploration - For K-Mean Clustering Technique
# ==========================================
# ***
# 
# ###UN Data on Countries of the World
# 
# I explored the dataset which I got in a csv format but
# may have missing values.  I driledl down on useful
# dimensions to explore after cleaning up the data.  Since I only
# have one observation per country, I may not have the option to use
# columns where there are many missing values as I'm effectively
# going to drop many countries when I drop rows with missing values.
# But then how did I drop such rows before? Because in those cases
# there were many observations per individual entity and dropping some
# did not eliminate an entity altogether.
# 
# So first I import the data and explore the columns and types - this
# time rather than doing it manually I am going to use list comprehension to do that.
# 

# In[5]:


import pandas as pd
df = pd.read_csv('UN.csv')
print('----')
# print the raw column information plus summary header
print(df)
print('----')
# look at the types of each column explicitly
print('Individual columns - Python data types')
[(x, type(df[x][0])) for x in df.columns] 


# Here we see that we have 14 columns with country and region being
# string types and the rest being floats.  We also see that the
# country column has 207 values, this is data on 207 countries.
# The region columns also has 207 entries, but the rest of the columns
# have many missing entries, indicated by number of non-null values
# less than 207.
# 
# We see that tfr, lifeMale, lifeFemale and GDP, and infantMortality
# are the columns closest to 207.  That is, if we use these columns we
# will only drop a few countries and not whole clusters as we might if
# we used educationMale and educationFemale.  On the other hand were
# we to use educationMale and educatonFemale, we would have to drop
# almost 2/3 of the data. So I focused on the columns with non-null
# values close to 207.
# 
# So the short list is now, country, region, tfr, lifeMale, lifeFemale
# and GDP, and infantMortality.
# 
# I suspect that there is clustering of lifeMale, lifeFemale and
# infantMortality according to GDP and I'm going to pull out the
# heavy machinery of K-Means technique to analyse this in detail and
# look at the clusters.
# 
# I don't know in advance how many clusters there will be 
# So while using KMeans technique, I will also look at some
# analytical measures to decide what the right number of clusters
# might be after looking at multiple such possibilities from 1 through
# 10 candidate clusters.
# 
# Finally, to be able to apply the KMeans algorithm, I will convert
# each field in the file to a scientific float format that the
# numerical algorithms expect.
# 
# 
