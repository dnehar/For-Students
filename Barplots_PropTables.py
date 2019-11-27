#-- proportion table
Groups_tab = pd.crosstab(index=cDC.obs['louvain'],  # Make a crosstab
                       columns=cDC.obs['Groups'],
                        margins=True)               # Name the count column
#-- change index and columns order
Groups_tab = Groups_tab.reindex(['All','0','1','2','3','4','5'])
Groups_tab = Groups_tab[['HI','HC','HY','HO','All']]
MyTab= Groups_tab.div(Groups_tab["All"], axis=0)
MyTab2 = MyTab.drop(columns="All")
#Col_Group=["dimgrey","lightcoral",'royalblue',"darkseagreen"]
MyTab2.plot(kind="bar",
           figsize=(12,6),
           stacked=True,
           linewidth=0.5,
           width=0.5, #***
           fontsize=20,
           color=col_groups)
plt.title("Proportion of cells across clusters", fontsize=18)
plt.ylabel("Prop. of cells", fontsize=18)
plt.xlabel("Clusters", fontsize=18)
plt.ylim=1.0
plt.legend(loc='center left', bbox_to_anchor=(1, 0.6), fontsize=18)
plt.show()
