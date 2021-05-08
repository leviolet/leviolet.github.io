from browser import document, alert

print(f"{sum(range(16))}")

def echo(event):
    alert(document["zone"].value)

document["mybutton"].bind("click", echo)
