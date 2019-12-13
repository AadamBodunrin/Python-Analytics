import pandas as pd
confusion = pd.read_csv("ConfusionMatrix.csv")

x = pd.DataFrame(confusion.iloc[:,2])
y = pd.DataFrame(confusion.iloc[:,-1])

print(x.head(5))
print(y.head(5))

from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 

results = confusion_matrix(y, x) 
print ('Confusion Matrix :')
print(results) 
print ('Accuracy Score :',accuracy_score(x, y) )
print ('Report : ')
print (classification_report(x, y) )

from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
fpr, tpr, thresholds = metrics.roc_curve(x, y)
# create plot
plt.plot(fpr, tpr, label='ROC curve')
plt.plot([0, 1], [0, 1], 'k--', label='Random guess')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve Threshold 0.05')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.legend(loc="lower right")
print(plt.show())

'''from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(x_train, y_train)
predicted_probas = nb.predict_proba(x_test)

# The magic happens here
import matplotlib.pyplot as plt
import scikitplot as skplt
skplt.metrics.plot_cumulative_gain(y_test, predicted_probas)
plt.show() '''