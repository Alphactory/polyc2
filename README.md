# Combleaf
Combleaf is a modular data exfiltration framework and repository of data exfiltration methods

# Install
```git clone https://github.com/secureighty/combleaf```

# How do I get started
```
#read the module readme to find out what data you need for a module
data_dict = {
  csrf_token:"whatevertoken"
}
mycomb = combleaf.Combleaf("modules.<pick a module>", data_dict)
mycomb.send("whatever data you want")
mydata = mycomb.recv()
```
