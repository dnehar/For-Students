sc.settings.set_figure_params(dpi=300)  # set sufficiently high resolution for saving
Genes =["PPBP","PF4", #mgk: 0-1
       "S100A8","CD14","LYZ","FCGR3A",#2-5
       'CD1C',"CST3","FCER1G", #6-8
       "IL7R","CD3E","CD3D","CD8A","CD8B", #9-13
       "GZMA","GZMB","GZMH","GZMK",
       "NKG7",'XCL1', #18-19
       "MS4A1", "CD79A", "IGHM","IGHD", #20-23
       "MZB1",'JCHAIN',"TNFRSF17", #24-26
       'LILRA4',"IRF7","TCF4", # 27-29
       'IFI44L','ISG15','IFI6'] #30-32
matplotlib.style.use('default')
ax = sc.pl.dotplot(corrected, Genes, 'clusters', dendrogram=True,
                  var_group_positions=[(0,1),(2,5), (6,8),(9,13),(14,17),(18,19),(20,23),(24,26),(27,29),(30,32)],
                  var_group_labels=['Mgk','Mono', 'DCs','T cells','Cytotox','NK','B cells','PCs','pDCs','ISGs'],
                  figsize=(10,5))# add save='_FileNames.pdf' to save a .pdf in figures folder 
