import android

app = android.Android()

app.dialogCreateAlert("Select an Athlete:")
app.dialogSetSingleChoiceItems(['Mickey', 'Sarah', 'James', 'Julie'])
app.dialogSetPositiveButtonText("Select")
app.dialogSetNegativeButtonText("Quit")
app.dialogShow()
resp = app.dialogGetResponse().result
