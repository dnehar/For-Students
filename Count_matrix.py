#--- save ount matrix (highly variable genes) .csv file 
adata.X.T.write_csvs(...)

#----  save raw counts .csv file
adata.raw.X.T.write_csvs(...)


#--- from AnnData to 10X 
pd.DataFrame(ad.var.index).to_csv(os.path.join(destination, "genes.tsv" ),   sep = "\t", index_col = False)
pd.DataFrame(ad.obs.index).to_csv(os.path.join(destination, "barcodes.tsv"), sep = "\t", index_col = False)
ad.obs.to_csv(os.path.join(destination, "metadata.tsv"), sep = "\t", index_col = True)
scipy.io.mmwrite(os.path.join(destination, "matrix.mtx"), ad.X)
