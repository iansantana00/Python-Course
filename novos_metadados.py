from importlib import metadata

# print(metadata.version('pip'))

metadados_pip = metadata.metadata('pip')

print(metadados_pip)

print(list(metadados_pip))

print(metadados_pip['Project-URL'])

print(len(metadata.files('django')))

print(metadata.requires('django'))
