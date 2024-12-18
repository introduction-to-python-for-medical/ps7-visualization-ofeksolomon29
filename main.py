data = fetch_openml(name='boston', version=1, as_frame=True)

print(data.DESCRֿ)
df = data.frame
df.describe()
df.dtypes

features = df.columns
selected_features = [features[3], features[5], features[7], features[10], features[13]]
selected_features

features = list(df.columns)
print("Available features:", features)
selected_features = [features[3], features[5], features[7], features[10], features[13]]
print("Selected features: ", selected_features)

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))
for ax, f in zip(axs, selected_features):
    ax.hist(df[f], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel(f)

x = df[selected_features[4]]
y = df[selected_features[1]]

plt.scatter(x,y)
plt.xlabel(selected_features[4])
plt.ylabel(selected_features[1])
plt.show()

reference_feature = selected_features[4]
y = df[reference_feature]

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, features):
  ax.scatter(df[f], y)
  ax.set_xlabel(f)

plt.show()


reference_feature = selected_features[4]  
comparison_feature = selected_features[1] 

plt.figure(figsize=(8, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.6)
plt.xlabel(reference_feature)
plt.ylabel(comparison_feature)

plt.savefig('correlation_plot.png')

plt.show()
