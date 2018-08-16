# Sources, descriptions, and citations for data sets

For your convenience, in this repository we provide preprocessed (excerpts) from temporal network data. All data files have been created based on publicly and freely available data sets. In the following, we give detailed source and citation information for these data sets:

| Datafile | Description | Citation | Weblink |
|----------|-------------|----------|---------|
| US_flights.ngram | Contains flight itineraries of American Airlines passengers between US airports. This data file is an exceprt generated from the RITA TransStat database. | NA | [link]() |
| tube.edges | Contains direct links between stations in the London Tube Metro Network. This data file was generated based on publicly available Wikipedia data. | NA | [link]() |
| tube_od.csv | Contains the volumes of passengers between origin and destination stations in the London Tube Metro Network. This data set is an excerpt from the Rolling Origin Destination Survey available from the OpenData platform of Transport for London | NA | [link]() |
| temporal_clusters.tedges | Synthetically generated data set | NA | [link]() | 

In addition to these datafiles, the SQLite database file `temporal_networks.db` contains the following tables:  

| Table name | Description | Citation | Weblink |
|------------|-------------|----------|---------|

# Reading data from code

Assuming that you have started Visual Studio Code in the root of the tutorial directory, files in this folder can be referenced from python code via the relative path `data/FILENAME`. If you start a `jupyter` notebook within the `code` folder, you will have to use the relative path `../data/FILENAME`.
