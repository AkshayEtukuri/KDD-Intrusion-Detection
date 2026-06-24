import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load the data
file_path = 'KDD_Cup_Data/kddcup.data_10_percent.gz'
df = pd.read_csv(file_path, header=None, compression='gzip')

# 2. Assign Column Names
columns = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", "wrong_fragment", 
           "urgent", "hot", "num_failed_logins", "logged_in", "num_compromised", "root_shell", "su_attempted", 
           "num_root", "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login", 
           "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate", 
           "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count", 
           "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate", 
           "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate", 
           "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "target"]
df.columns = columns

# 3. Preprocess
df = pd.get_dummies(df, columns=['protocol_type', 'service', 'flag'])
X = df.drop('target', axis=1)
y = df['target']

# 4. Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=10, n_jobs=-1)
model.fit(X_train, y_train)

# 5. Evaluate and Print Report
predictions = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, predictions):.4f}")
print("\nDetailed Performance Report:")
print(classification_report(y_test, predictions))

# 6. Show Feature Importance Chart
importances = pd.Series(model.feature_importances_, index=X.columns)
importances.nlargest(10).plot(kind='barh')
plt.title("Top 10 Important Features")
plt.show()


from sklearn.metrics import confusion_matrix
import seaborn as sns

# Generate the confusion matrix
cm = confusion_matrix(y_test, predictions)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()