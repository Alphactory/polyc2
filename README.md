# Combleaf
Combleaf is a modular data exfiltration framework and repository of data exfiltration methods

# Install
```git clone https://github.com/secureighty/combleaf```

# How do I get started
```
mycomb = combleaf.Combleaf("modules.<pick a module>")
mycomb.send("whatever data you want")
mydata = mycomb.recv()
```
