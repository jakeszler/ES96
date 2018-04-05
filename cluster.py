import pandas as pd

municipalities = {'Gloucester city' : 'A', 
				'Manchester-by-the-Sea town' : 'A', 
				'Newburyport city' : 'A', 
				'Rowley town' : 'A', 
				'Lynn city' : 'A', 
				'Nahant town' : 'A', 
				'Swampscott town' : 'A', 
				'Marblehead town' : 'A', 
				'Peabody city' : 'A', 
				'Wenham town': 'A', 
				'Saugus town' : 'A', 
				'Chelsea city' : 'A', 
				'Rockport town' : 'A', 
				'Revere city' : 'A', 
				'Hamilton town' : 'A', 
				'Salem city' : 'A', 
				'Ipswich town' : 'A', 
				'Danvers town' : 'A', 
				'Beverly city' : 'A',
				'Everett city' : 'A',
				'Acton town' : 'B', 
				'Littleton town' : 'B', 
				'Concord town' : 'B', 
				'Ayer town' : 'B', 
				'Belmont town' : 'B', 
				'Shirley town' : 'B',
				'Leominster city' : 'B',
			    'Littleton town' : 'B', 
			    'Fitchburg city' : 'B', 
			    'Maynard town' : 'B',
			    'Arlington town' : 'B', 
				'Lincoln town' : 'B',
				'Wilmington town' : 'C', 
				'Groveland town' : 'C', 
				'Andover town' : 'C', 
				'Lynnfield town' : 'C', 
				'Methuen Town city' : 'C', 
				'Reading town' : 'C', 
				'Wakefield town' : 'C', 
				'Lawrence city' : 'C', 
				'Winchester town' : 'C', 
				'Haverhill city' : 'C', 
			    'Woburn city' : 'C', 
				'North Andover town' : 'C',  
				'Malden city' : 'C', 
				'Melrose city' : 'C', 
				'Tewksbury town' : 'D', 
				'Billerica town' : 'D', 
				'Dracut town' : 'D', 
				'Stoneham town' : 'D', 
				'Lowell city' : 'D', 
				'Burlington town' : 'D',  
				'Medford city' : 'D', 
				'Wayland town' : 'E', 
				'Southborough town' : 'E', 
				'Hopkinton town' : 'E',
			    'Wellesley town' : 'E',
				'Worcester city' : 'E',
				'Framingham town' : 'E',
				'Grafton town' : 'E',
				'Westborough town' : 'E',
				'Ashland town' : 'E',
				'Natick town' : 'E',
				'Dedham town' : 'F', 
				'Needham town' : 'F', 
				'Dover city' :'F',
				'Norwood town' : 'G', 
				'Norfolk town' : 'G', 
				'Walpole town' : 'G',
				'Franklin Town city' : 'G',
				'Westwood town' : 'G',
				'Bellingham town' : 'G',
				'Halifax town' : 'H', 
				'Rockland town' : 'H',  
				'Quincy city' : 'H', 
				'Plymouth town' : 'H', 
				'Hanson town' : 'H', 
				'Duxbury town' : 'H', 
				'Whitman town' : 'H',
				'Braintree Town city' : 'H', 
				'Kingston town' : 'H',  
				'Abington town' : 'H', 
				'Milton town' : 'H', 
				'Scituate town' : 'I', 
				'Norwell town' : 'I', 
				'Cohasset town' : 'I', 
				'Marshfield town' : 'I', 
				'Hingham town' : 'I', 
				'Canton town' : 'J', 
				'Mansfield town' : 'J',
				'North Kingston town' : 'J',
				'Exeter town' : 'J',
				'Central Falls city' : 'J',
				'Cumberland town' : 'J',
				'Attleboro city' : 'J',
				'Warwick city' : 'J',
				'Foxborough town' : 'J', 
				'East Providence city' : 'J', 
				'Providenc city' : 'J',
				'Pawtucket city' : 'J',
				'Stoughton town' : 'J',
				'Sharon town' : 'J',
				'Middleborough town' : 'K', 
				'West Bridgewater town' : 'K',  
				'Avon town' : 'K', 
				'Holbrook town' : 'K',  
				'Randolph town' : 'K', 
				'Lakeville town' : 'K', 
				'Bridgewater town' : 'K', 
				'Brockton city' : 'K', 
				'Newton city' : 'L', 
				'Waltham city' : 'L', 
				'Watertown Town city' : 'L', 
				'Brookline town' : 'L', 
				'Weston town' : 'L',  
				#'Somerville city' : 'Q',
				#'Cambridge city' : 'Q',
				#'Boston city' : 'Q'
				}

cluster_commute = {
				    'AA' : {'commuters' : 0, 'moe' : 0}, 
					'AB' : {'commuters' : 0, 'moe' : 0}, 
				    'AC' : {'commuters' : 0, 'moe' : 0},
				    'AD' : {'commuters' : 0, 'moe' : 0},
				   	'AE' : {'commuters' : 0, 'moe' : 0}, 
				    'AF' : {'commuters' : 0, 'moe' : 0},
				    'AG' : {'commuters' : 0, 'moe' : 0},
				   	'AH' : {'commuters' : 0, 'moe' : 0}, 
				    'AI' : {'commuters' : 0, 'moe' : 0},
				    'AJ' : {'commuters' : 0, 'moe' : 0},
				   	'AK' : {'commuters' : 0, 'moe' : 0}, 
				    'AL' : {'commuters' : 0, 'moe' : 0},
				    'BA' : {'commuters' : 0, 'moe' : 0},
				    'BB' : {'commuters' : 0, 'moe' : 0},
				    'BC' : {'commuters' : 0, 'moe' : 0}, 
				    'BD' : {'commuters' : 0, 'moe' : 0},
				    'BE' : {'commuters' : 0, 'moe' : 0},
				   	'BF' : {'commuters' : 0, 'moe' : 0}, 
				    'BG' : {'commuters' : 0, 'moe' : 0},
				    'BH' : {'commuters' : 0, 'moe' : 0},
				   	'BI' : {'commuters' : 0, 'moe' : 0}, 
				    'BJ' : {'commuters' : 0, 'moe' : 0},
				    'BK' : {'commuters' : 0, 'moe' : 0},
				   	'BL' : {'commuters' : 0, 'moe' : 0}, 
				    'CA' : {'commuters' : 0, 'moe' : 0},
				    'CB' : {'commuters' : 0, 'moe' : 0},
	 			    'CC' : {'commuters' : 0, 'moe' : 0},
				    'CD' : {'commuters' : 0, 'moe' : 0}, 
				    'CE' : {'commuters' : 0, 'moe' : 0},
				    'CF' : {'commuters' : 0, 'moe' : 0},
				   	'CG' : {'commuters' : 0, 'moe' : 0}, 
				    'CH' : {'commuters' : 0, 'moe' : 0},
				    'CI' : {'commuters' : 0, 'moe' : 0},
				   	'CJ' : {'commuters' : 0, 'moe' : 0}, 
				    'CK' : {'commuters' : 0, 'moe' : 0},
				    'CL' : {'commuters' : 0, 'moe' : 0},
				   	'DA' : {'commuters' : 0, 'moe' : 0}, 
				    'DB' : {'commuters' : 0, 'moe' : 0},
				    'DC' : {'commuters' : 0, 'moe' : 0},
				    'DD' : {'commuters' : 0, 'moe' : 0},
				    'DE' : {'commuters' : 0, 'moe' : 0},
				    'DF' : {'commuters' : 0, 'moe' : 0},
				   	'DG' : {'commuters' : 0, 'moe' : 0}, 
				    'DH' : {'commuters' : 0, 'moe' : 0},
				    'DI' : {'commuters' : 0, 'moe' : 0},
				   	'DJ' : {'commuters' : 0, 'moe' : 0}, 
				    'DK' : {'commuters' : 0, 'moe' : 0},
				    'DL' : {'commuters' : 0, 'moe' : 0},
				   	'EA' : {'commuters' : 0, 'moe' : 0}, 
				    'EB' : {'commuters' : 0, 'moe' : 0},
				    'EC' : {'commuters' : 0, 'moe' : 0},
				    'ED' : {'commuters' : 0, 'moe' : 0}, 
				    'EE' : {'commuters' : 0, 'moe' : 0},
				    'EF' : {'commuters' : 0, 'moe' : 0},
				    'EG' : {'commuters' : 0, 'moe' : 0},
				   	'EH' : {'commuters' : 0, 'moe' : 0}, 
				    'EI' : {'commuters' : 0, 'moe' : 0},
				    'EJ' : {'commuters' : 0, 'moe' : 0},
				   	'EK' : {'commuters' : 0, 'moe' : 0}, 
				    'EL' : {'commuters' : 0, 'moe' : 0},
				    'FA' : {'commuters' : 0, 'moe' : 0},
				   	'FB' : {'commuters' : 0, 'moe' : 0}, 
				    'FC' : {'commuters' : 0, 'moe' : 0},
				    'FD' : {'commuters' : 0, 'moe' : 0},
				    'FE' : {'commuters' : 0, 'moe' : 0}, 
				    'FF' : {'commuters' : 0, 'moe' : 0},
				    'FG' : {'commuters' : 0, 'moe' : 0},
				    'FH' : {'commuters' : 0, 'moe' : 0},
				   	'FI' : {'commuters' : 0, 'moe' : 0}, 
				    'FJ' : {'commuters' : 0, 'moe' : 0},
				    'FK' : {'commuters' : 0, 'moe' : 0},
				   	'FL' : {'commuters' : 0, 'moe' : 0}, 
				    'GA' : {'commuters' : 0, 'moe' : 0},
				    'GB' : {'commuters' : 0, 'moe' : 0},
				   	'GC' : {'commuters' : 0, 'moe' : 0}, 
				    'GD' : {'commuters' : 0, 'moe' : 0},
				    'GE' : {'commuters' : 0, 'moe' : 0},
				    'GF' : {'commuters' : 0, 'moe' : 0},
				    'GG' : {'commuters' : 0, 'moe' : 0}, 
				    'GH' : {'commuters' : 0, 'moe' : 0},
				    'GI' : {'commuters' : 0, 'moe' : 0},
				   	'GJ' : {'commuters' : 0, 'moe' : 0}, 
				    'GK' : {'commuters' : 0, 'moe' : 0},
				    'GL' : {'commuters' : 0, 'moe' : 0},
				   	'HA' : {'commuters' : 0, 'moe' : 0}, 
				    'HB' : {'commuters' : 0, 'moe' : 0},
				    'HC' : {'commuters' : 0, 'moe' : 0},
				   	'HD' : {'commuters' : 0, 'moe' : 0}, 
				    'HE' : {'commuters' : 0, 'moe' : 0},
				    'HF' : {'commuters' : 0, 'moe' : 0},
				    'HG' : {'commuters' : 0, 'moe' : 0},
				    'HH' : {'commuters' : 0, 'moe' : 0},
				    'HI' : {'commuters' : 0, 'moe' : 0},
				   	'HJ' : {'commuters' : 0, 'moe' : 0}, 
				    'HK' : {'commuters' : 0, 'moe' : 0},
				    'HL' : {'commuters' : 0, 'moe' : 0},
				   	'IA' : {'commuters' : 0, 'moe' : 0}, 
				    'IB' : {'commuters' : 0, 'moe' : 0},
				    'IC' : {'commuters' : 0, 'moe' : 0},
				   	'ID' : {'commuters' : 0, 'moe' : 0}, 
				    'IE' : {'commuters' : 0, 'moe' : 0},
				    'IF' : {'commuters' : 0, 'moe' : 0},
				    'IG' : {'commuters' : 0, 'moe' : 0},
				    'IH' : {'commuters' : 0, 'moe' : 0},
				    'II' : {'commuters' : 0, 'moe' : 0},
				   	'IJ' : {'commuters' : 0, 'moe' : 0}, 
				    'IK' : {'commuters' : 0, 'moe' : 0},
				    'IL' : {'commuters' : 0, 'moe' : 0},
				   	'JA' : {'commuters' : 0, 'moe' : 0}, 
				    'JB' : {'commuters' : 0, 'moe' : 0},
				    'JC' : {'commuters' : 0, 'moe' : 0},
				    'JD' : {'commuters' : 0, 'moe' : 0}, 
				    'JE' : {'commuters' : 0, 'moe' : 0}, 
				    'JF' : {'commuters' : 0, 'moe' : 0},
				    'JG' : {'commuters' : 0, 'moe' : 0},
				   	'JH' : {'commuters' : 0, 'moe' : 0}, 
				    'JI' : {'commuters' : 0, 'moe' : 0},
				    'JJ' : {'commuters' : 0, 'moe' : 0},
				   	'JK' : {'commuters' : 0, 'moe' : 0}, 
				    'JL' : {'commuters' : 0, 'moe' : 0},
				    'KA' : {'commuters' : 0, 'moe' : 0},
				   	'KB' : {'commuters' : 0, 'moe' : 0}, 
				    'KC' : {'commuters' : 0, 'moe' : 0},
				    'KD' : {'commuters' : 0, 'moe' : 0},
				    'KE' : {'commuters' : 0, 'moe' : 0}, 
				    'KF' : {'commuters' : 0, 'moe' : 0}, 
				    'KG' : {'commuters' : 0, 'moe' : 0},
				    'KH' : {'commuters' : 0, 'moe' : 0},
				   	'KI' : {'commuters' : 0, 'moe' : 0}, 
				    'KJ' : {'commuters' : 0, 'moe' : 0},
				    'KK' : {'commuters' : 0, 'moe' : 0},
				    'KL' : {'commuters' : 0, 'moe' : 0},
				    'LA' : {'commuters' : 0, 'moe' : 0},
				    'LB' : {'commuters' : 0, 'moe' : 0},
				   	'LC' : {'commuters' : 0, 'moe' : 0}, 
				    'LD' : {'commuters' : 0, 'moe' : 0},
				    'LE' : {'commuters' : 0, 'moe' : 0},
				    'LF' : {'commuters' : 0, 'moe' : 0}, 
				    'LG' : {'commuters' : 0, 'moe' : 0}, 
				    'LH' : {'commuters' : 0, 'moe' : 0},
				    'LI' : {'commuters' : 0, 'moe' : 0},
				   	'LJ' : {'commuters' : 0, 'moe' : 0}, 
				    'LK' : {'commuters' : 0, 'moe' : 0},
				    'LL' : {'commuters' : 0, 'moe' : 0},
				   }

# would commuting between the two clusters be benefitted by NSRL? 
cluster_count = [#'AE',
'AF','AG','AH','AI','AJ','AK',
				 'BF','BG','BH','BI','BJ','BK',
				 #'CE',
				 'CF','CG','CH','CI','CJ','CK',
				 #'DE',
				 'DF','DG','DH','DI','DJ','DK',
				 #'EA','EC','ED',
				 'FA', 'FB','FC','FD',
				 'GA', 'GB','GC','GD',
				 'HA', 'HB','HC','HD',
				 'IA', 'IB','IC','ID',
				 'JA', 'JB','JC','JD',
				 'KA', 'KB','KC','KD'
				 ]


total_commuters = 0
total_moe = 0

df = pd.read_csv("FilteredDataset.csv")
	
i = 0 

# iterate over municipalities
for city in municipalities:

	# retreive municipality's cluster
	home_cluster = municipalities.get(city)

	# retreive all dataset rows where the home municipalities is the given municipality
	df_filtered = df[(df['Minor Civil Division'] == city)]

	# iterate over rows where the home municipalities is the given municipality
	for index, row in df_filtered.iterrows():

		# retreive name of work city
		work_city = row['Minor Civil Division.1']

		# check whether work city is served by commuter rail network 
		if work_city in municipalities:

			# retrieve cluster of work municipality
			work_cluster = municipalities.get(work_city)

			# increment cluster_commute corresponding to commute from home to work municipality 
			cluster_commute[(home_cluster + work_cluster)]['commuters'] += int(row['Work Flow of People'].replace(",",""))
			cluster_commute[(home_cluster + work_cluster)]['moe'] += int(row['Margin of Error'].replace(",",""))  


# iterate over clusters
for cluster in cluster_commute:

	# check if cluster is in cluster_count
	if cluster in cluster_count:

		print(cluster, cluster_commute[cluster])

		# increment total figures 
		total_commuters += cluster_commute[cluster]['commuters']
		total_moe += cluster_commute[cluster]['moe']

print(total_commuters, total_moe)




