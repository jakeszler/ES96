city_cluster  = {'Cambridge' : 'A',
			     'Newton' : 'A',
			     'Salem' : 'B',
			     'Haverhill' : 'B',
			     'Framingham' : 'C',
			     'Natick' : 'C'
			     }

cluster_commute = {'AB' : {'commuters' : 0, 'moe' : 0}, 
				   'AC' : {'commuters' : 0, 'moe' : 0},
				   'BC' : {'commuters' : 0, 'moe' : 0}
				  }

# would commuting between the two clusters be benefitted by NSRL? 
cluster_count = ['AB', 'BC']


total_commuters = 0
total_moe = 0


	
# iterate over municipalities
for city in city_cluster:

	# retreive municipality's cluster
	home_cluster = city_cluster.get(city)

	# retreive all dataset rows where the home municipalities is the given municipality
	city_data = census_dataset$(home_municipality=city)

	# iterate over rows of city_data
	for element in city_data:

		# retrieve cluster of work municipality
		work_cluster = city_cluster.get(element$work_municipality)

		# increment cluster_commute corresponding to commute from home to work municipality 
		cluster_commute[(home_cluster + work_cluster)]['commuters'] += element$commuters_number
		cluster_commute[(home_cluster + work_cluster)]['moe'] += element$margin_of_error


# iterate over clusters
for cluster in cluster_commute:

	# check if cluster is in cluster_count
	if cluster in cluster_count:

		# increment total figures 
		total_commuters += cluster_commute[cluster]['commuters']
		total_moe += cluster_commute[cluster]['moe']
