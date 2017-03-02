c = get_config()
c.NbConvertApp.notebooks = ["advancedLaneFinding.ipynb"]
c.NbConvertApp.export_format = 'html'
c.Exporter.preprocessors = ['extractoutput.ExtractOutputPreprocessor']
