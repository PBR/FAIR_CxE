# FAIR_CxE: CxE potato data integration

This repository holds the files associated with Chapter 4 of E. Papoutsoglou's thesis. 

You can find 3 docker containers for the following:

1. A simple FAIR data point for the dataset in question (uses Python 3 / flask)
2. A SPARQL server hosting the phenotypic (meta)data and the weather datasets (uses Fuseki)
3. Jupyter notebooks for:
	* the conversion of a MIAPPE spreadsheet file to RDF (phenotypic metadata)
	* the conversion of tabular phenotypic data files to RDF
	* the exploration of the produced RDF as pulled from container (2), and some visualizations.


## Folders and files

The contents of this repository are organized by container. The [all_containers](all_containers) folder has 4 subdirectories. 
1. [common_files]
2. [server-fdp](all_containers/server-fdp)
3. [server-fuseki](./all_containers/server-fuseki)
4. [server-jupyter](./all_containers/server-jupyter/)

