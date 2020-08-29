import pip._internal as pip

print([i.key for i in pip.get_installed_distributions()])
# or
pip.main(['freeze'])