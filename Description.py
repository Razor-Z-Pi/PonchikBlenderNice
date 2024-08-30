import zipfile

print("Пончик для блендера находиться в архиви. -//- The blender donut is in the archive.")

fantasy_zip = zipfile.ZipFile('../untitled.7z') # Путь для архива 
fantasy_zip.extractall('...') # Путь для распаковки

fantasy_zip.close()