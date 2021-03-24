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

The contents of this repository are organized by container. The [all_containers](./all_containers) folder has 4 subdirectories. 

1. [common_files](./all_containers/common_files): 

	* [data-original](./all_containers/common_files/data-original): Files assembled manually, resembling what could be expected expected outputs from data collection done by researchers.
		* [phenotypic](./all_containers/common_files/data-original/phenotypic): Files holding data from field phenotyping experiments with the CxE population.
			* [data_1999NL.csv](./all_containers/common_files/data-original/phenotypic/data_1999NL.csv): Data from the 1999 experiment conducted in the Netherlands by [B.C. Celis-Gamboa](https://doi.org/10.1111/j.1744-7348.2003.tb00284.x).
			* [data_2003VE.csv](./all_containers/common_files/data-original/phenotypic/data_2003VE.csv): Data from the 2003 experiment conducted in Venezuela.
			* [data_2004Fin.csv](./all_containers/common_files/data-original/phenotypic/data_2004Fin.csv), [data_2005Fin.csv](./all_containers/common_files/data-original/phenotypic/data_2005Fin.csv): Data from the 2004 and 2005 experiments conducted in Finland by [A. Zaban](https://doi.org/10.33354/smst.76724).
			* [data_2010ET.csv](./all_containers/common_files/data-original/phenotypic/data_2010ET.csv): Data from the 1999 experiment conducted in Ethiopia by [P.X. Hurtado-Lopez](https://doi.org/10.1007/s10681-015-1431-2).
		* [weather](./all_containers/common_files/data-original/weather): 
			* Tab-separated files with data about  the photoperiod (time between sunrise and sunset)  for the experiments. The contents have been retrieved from [timeanddate.com](https://www.timeanddate.com/)
				* [1999NL_sun.tsv](./all_containers/common_files/data-original/weather/1999NL_sun.tsv), [2003VE_sun.tsv](./all_containers/common_files/data-original/weather/2003VE_sun.tsv), [2004Fin_sun.tsv](./all_containers/common_files/data-original/weather/2004Fin_sun.tsv), [2005Fin_sun.tsv](./all_containers/common_files/data-original/weather/2005Fin_sun.tsv), [2010ET_sun.tsv](./all_containers/common_files/data-original/weather/2010ET_sun.tsv)
			* Tab-separated files with data about the temperature (daily average) for the experiments. The temperature records have been copied from P.X Hurtado-Lopez's files.
				* [1999NL_temp.tsv](./all_containers/common_files/data-original/weather/1999NL_temp.tsv), [2003VE_temp.tsv](./all_containers/common_files/data-original/weather/2003VE_temp.tsv), [2004Fin_temp.tsv](./all_containers/common_files/data-original/weather/2004Fin_temp.tsv), [2005Fin_temp.tsv](./all_containers/common_files/data-original/weather/2005Fin_temp.tsv), [2010ET_temp.tsv](./all_containers/common_files/data-original/weather/2010ET_temp.tsv)
		* [MIAPPE_CxE_v1.1.xlsx](./all_containers/common_files/data-original/MIAPPE_CxE_v1.1.xlsx): MIAPPE spreadsheet (see [here](https://github.com/MIAPPE/MIAPPE/tree/master/MIAPPE_Checklist-Data-Model-v1.1/MIAPPE_templates)) holding the metadata from the 5 experiments, as retrieved from the literature. 
		* [station_metadata.ttl](./all_containers/common_files/data-original/station_metadata.ttl): TTL file with metadata about the 4 weather stations that would theoretically hold the weather data.
		
	* [data-generated](./all_containers/common_files/data-generated): RDF (TTL) files that have been derived based on those in the data-original folder, to be imported into the SPARQL endpoint. Note that all weather data has been aggregated also into a single file, [all_weather.ttl](./all_containers/common_files/data-generated/weather/all_weather.ttl).
		
	* [pheno_meta-data_excel_to_rdf.ipynb](./all_containers/common_files/pheno_meta-data_excel_to_rdf.ipynb): Jupyter notebook that transforms the phenotypic data (from [data-original](./all_containers/common_files/data-original)) to RDF. Note that only the parts necessary for the present data have been implemented, i.e. empty MIAPPE sections and fields are not tackled here.
	
	* [Explore_data.ipynb](./all_containers/common_files/Explore_data.ipynb): Jupyter notebook that presents an exploration of the phenotypic data and metadata available, combines it and concludes with visualizations.
	* [pheno_setup.ttl](./all_containers/common_files/pheno_setup.ttl) and [weather_setup.ttl](./all_containers/common_files/weather_setup.ttl): Configuration files used by the triple store ([Fuseki](https://jena.apache.org/documentation/fuseki2/)) to create the datasets.
	
	* [requirements_jupyter.txt](./all_containers/common_files/requirements_jupyter.txt): Python libraries required for the Jupyter notebooks in this repository.

2. [server-fdp](./all_containers/server-fdp): Files required for the container hosting the FAIR Data Point (FDP).
	
	* [fdp.ttl](./all_containers/server-fdp/fdp.ttl), [catalog.ttl](./all_containers/server-fdp/catalog.ttl), [dataset.ttl](./all_containers/server-fdp/dataset.ttl), [distribution.ttl](./all_containers/server-fdp/distribution.ttl): Specifications (formatted as TTL) for each level of the FDP, based on the [FDP recommendations](https://github.com/FAIRDataTeam/FAIRDataPoint-Spec).
	* [templates folder](./all_containers/server-fdp/templates): HTML files based on the TTL files, so that the visual syntax formatting is preserved and links can be clickable [todo].
	* [fdp.py](./all_containers/server-fdp/fdp.py): Simple [Flask](https://flask.palletsprojects.com/en/1.1.x/) server (Python 3.4+) to host the FDP files. 
	* [requirements_fdp.txt](./all_containers/server-fdp/requirements_fdp.txt) and [Dockerfile](./all_containers/server-fdp/Dockerfile): Files to help set up the docker container.

3. [server-fuseki](./all_containers/server-fuseki): Files required for the container hosting the SPARQL endpoint(s).
   * [Dockerfile](./all_containers/server-fuseki/Dockerfile): File to help set up the docker container.

4. [server-jupyter](./all_containers/server-jupyter): Files required for the container hosting the Jupyter notebooks.
	* [requirements.txt](./all_containers/server-jupyter/requirements.txt) and [Dockerfile](./all_containers/server-jupyter/Dockerfile): File to help set up the docker container. [todo: remove unused files]


## How to use

This section describes how to run the Docker containers.
[todo]
