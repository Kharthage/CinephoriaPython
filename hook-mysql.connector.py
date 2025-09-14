from PyInstaller.utils.hooks import collect_data_files

# Inclure tous les fichiers de données de mysql.connector (y compris les locales)
datas = collect_data_files('mysql.connector', include_py_files=True)