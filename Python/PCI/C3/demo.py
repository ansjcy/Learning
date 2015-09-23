import clusters
blognames, words, data = clusters.readfile('blogdata.txt')
print(data)
clust = clusters.hcluster(data)
print(len(clust.vec))
clusters.printclust(clust, labels=blognames)