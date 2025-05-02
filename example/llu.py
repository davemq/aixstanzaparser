import aixstanzaparser

# Create parser instance
config = aixstanzaparser.AIXStanzaParser()

# Read and parse lvupdate.date
config.read("lvupdate.data")

# Update llvupdate.llu to yes
if 'llvupdate' not in config.sections():
    config['llvupdate'] = {}
config['llvupdate']['llu'] = "yes"

# write updated lvupdate.data
with open("lvupdate.data", "w") as configfile:
    config.write(configfile)
