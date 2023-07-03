import pandas as pd

old_slugs = pd.read_csv("omt/toc_slugs.csv", header=None)
old_slugs.columns = ["Old"]
old_slugs["Old"] = old_slugs["Old"].str.rstrip()
new_slugs = pd.read_csv("omt/new_omt_slugs.csv")
new_slugs = new_slugs.set_index("Old")
mapping_dict = new_slugs.to_dict(orient="dict")["New"]
old_slugs = old_slugs.replace(mapping_dict)
old_slugs.to_csv("omt/updated_slugs.csv")
