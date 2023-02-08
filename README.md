# Combleaf
Combleaf is a modular data exfiltration framework and repository of data exfiltration methods

# Install
```git clone https://github.com/secureighty/combleaf```

# How do I get started
```
data_dict = {
  csrf_token:"whatevertokenbase64"
}
mycomb = combleaf.Combleaf("modules.<pick a module>", data_dict)
mycomb.send("whatever data you want")
mydata = mycomb.recv()
```
